#!/usr/bin/env python3
"""Transcribe audio with official Qwen3-ASR Transformers models on CUDA."""

from __future__ import annotations

import argparse
import gc
import json
import math
import os
import re
import shutil
import subprocess
import sys
import time
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any, Iterator

from transcribe_qwen3_asr import (
    SAMPLE_RATE,
    finite_document_number,
    is_alignment_character,
    local_model_target,
    read_json_strict,
    repository_path,
    resume_mode,
    rounded_seconds,
    sentence_texts,
    sha256_file,
    utc_now,
    validate_aligned_document,
    validate_raw_document,
    write_json_atomically,
)


DEFAULT_MODEL = "Qwen/Qwen3-ASR-1.7B"
DEFAULT_ALIGNER = "Qwen/Qwen3-ForcedAligner-0.6B"
ENGINE = "qwen-asr-transformers"
BACKEND = "transformers"
QWEN_ASR_PACKAGE_VERSION = "0.0.6"
TORCH_PUBLIC_VERSION = "2.11.0"
MAX_INFERENCE_BATCH_SIZE = 1
MAX_ALIGNMENT_CHUNK_SECONDS = 180.0
ALIGNMENT_TIMESTAMP_TOLERANCE_SECONDS = 1.0
SUPPORTED_ALIGNMENT_LANGUAGES = frozenset(
    {
        "Chinese",
        "Cantonese",
        "English",
        "German",
        "Spanish",
        "French",
        "Italian",
        "Portuguese",
        "Russian",
        "Korean",
        "Japanese",
    }
)
NO_SPACE_CHUNK_JOIN_LANGUAGES = frozenset({"Chinese", "Cantonese", "Japanese"})
CUDA_DEVICE_RE = re.compile(r"^cuda:(\d+)$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run official Qwen3-ASR and Qwen3-ForcedAligner models locally "
            "with the Transformers CUDA backend."
        )
    )
    parser.add_argument("--input", required=True, type=Path, help="Local audio file")
    parser.add_argument("--output", required=True, type=Path, help="Raw ASR JSON")
    parser.add_argument(
        "--aligned-output",
        required=True,
        type=Path,
        help="Forced-aligned ASR JSON",
    )
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument(
        "--model-path",
        type=Path,
        help="Optional local model directory; metadata still records --model",
    )
    parser.add_argument("--aligner", default=DEFAULT_ALIGNER)
    parser.add_argument(
        "--aligner-path",
        type=Path,
        help="Optional local aligner directory; metadata still records --aligner",
    )
    parser.add_argument("--language", default="Chinese")
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.0,
        help="Compatibility field; the official Transformers backend requires 0",
    )
    parser.add_argument("--max-tokens", type=int, default=2048)
    parser.add_argument(
        "--chunk-duration",
        type=float,
        default=120.0,
        help="Decode and process one bounded chunk; must not exceed 180 seconds",
    )
    parser.add_argument("--max-sentence-characters", type=int, default=160)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument(
        "--dtype",
        choices=("float16", "bfloat16"),
        default="bfloat16",
    )
    parser.add_argument(
        "--attention-implementation",
        choices=("sdpa", "eager"),
        default="sdpa",
        help="Use built-in attention implementations; FlashAttention is not required",
    )
    parser.add_argument(
        "--verbose",
        action=argparse.BooleanOptionalAction,
        default=True,
    )
    replacement = parser.add_mutually_exclusive_group()
    replacement.add_argument("--retranscribe", action="store_true")
    replacement.add_argument("--realign", action="store_true")
    return parser.parse_args()


def raw_backend_options(args: argparse.Namespace) -> dict[str, Any]:
    return {
        "backend": BACKEND,
        "qwen_asr_version": QWEN_ASR_PACKAGE_VERSION,
        "torch_version": TORCH_PUBLIC_VERSION,
        "device": args.device,
        "dtype": args.dtype,
        "attention_implementation": args.attention_implementation,
        "max_inference_batch_size": MAX_INFERENCE_BATCH_SIZE,
    }


def aligned_backend_options(args: argparse.Namespace) -> dict[str, Any]:
    return {
        "backend": BACKEND,
        "qwen_asr_version": QWEN_ASR_PACKAGE_VERSION,
        "torch_version": TORCH_PUBLIC_VERSION,
        "device": args.device,
        "dtype": args.dtype,
        "attention_implementation": args.attention_implementation,
        "max_inference_batch_size": MAX_INFERENCE_BATCH_SIZE,
    }


def join_transcript_chunks(texts: list[str], *, language: str) -> str:
    nonempty_texts = [text for text in texts if text]
    separator = "" if language in NO_SPACE_CHUNK_JOIN_LANGUAGES else " "
    return separator.join(nonempty_texts)


def validate_cuda_raw_integrity(
    document: dict[str, Any],
    *,
    args: argparse.Namespace,
    backend_options: dict[str, Any],
) -> None:
    expected_options = {
        "temperature": args.temperature,
        "max_tokens_per_chunk": args.max_tokens,
        "chunk_duration_seconds": args.chunk_duration,
        **backend_options,
    }
    if document.get("options") != expected_options:
        raise ValueError("raw ASR decoding options do not match exactly")
    audio = document.get("audio")
    if not isinstance(audio, dict) or audio.get("sample_rate_hz") != SAMPLE_RATE:
        raise ValueError("raw ASR sample rate does not match the CUDA backend")
    segments = document.get("segments")
    if not isinstance(segments, list) or document.get("text") != join_transcript_chunks(
        [
            str(segment.get("text", ""))
            for segment in segments
            if isinstance(segment, dict)
        ],
        language=args.language,
    ):
        raise ValueError("raw ASR text does not match its source chunks")


def validate_cuda_aligned_integrity(
    document: dict[str, Any], *, raw_output_path: Path
) -> None:
    source = document.get("source")
    if not isinstance(source, dict) or source.get("raw_asr_path") != repository_path(
        raw_output_path
    ):
        raise ValueError("aligned ASR raw artifact path does not match")


def validate_file_identity(
    path: Path,
    *,
    expected_size_bytes: int,
    expected_sha256: str,
    label: str,
) -> None:
    if not path.is_file() or path.stat().st_size != expected_size_bytes:
        raise ValueError(f"{label} size changed while ASR was running")
    if sha256_file(path) != expected_sha256:
        raise ValueError(f"{label} SHA-256 changed while ASR was running")


def audio_chunk_ranges(
    duration_seconds: float, *, chunk_duration: float
) -> Iterator[tuple[float, float]]:
    start = 0.0
    while start < duration_seconds:
        end = min(duration_seconds, start + chunk_duration)
        if end <= start:
            raise ValueError("audio chunk duration did not advance")
        yield start, end
        start = end


def probe_audio_duration(input_path: Path, *, ffprobe: str) -> float:
    completed = subprocess.run(
        [
            ffprobe,
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "json",
            input_path.as_posix(),
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            "ffprobe could not read the input audio: "
            f"{completed.stderr.strip() or 'unknown error'}"
        )
    try:
        document = json.loads(completed.stdout)
        duration = float(document["format"]["duration"])
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        raise ValueError("ffprobe returned no finite audio duration") from error
    if not math.isfinite(duration) or duration <= 0:
        raise ValueError("ffprobe returned no finite audio duration")
    return duration


def decode_audio_chunk(
    input_path: Path,
    *,
    start_seconds: float,
    end_seconds: float,
    ffmpeg: str,
    numpy_module: Any,
) -> Any:
    duration = end_seconds - start_seconds
    completed = subprocess.run(
        [
            ffmpeg,
            "-nostdin",
            "-hide_banner",
            "-loglevel",
            "error",
            "-ss",
            f"{start_seconds:.6f}",
            "-i",
            input_path.as_posix(),
            "-t",
            f"{duration:.6f}",
            "-map",
            "0:a:0",
            "-vn",
            "-ac",
            "1",
            "-ar",
            str(SAMPLE_RATE),
            "-c:a",
            "pcm_f32le",
            "-f",
            "f32le",
            "pipe:1",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode != 0:
        detail = completed.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"ffmpeg could not decode an audio chunk: {detail}")
    if len(completed.stdout) % 4 != 0:
        raise ValueError("ffmpeg returned malformed float32 audio")
    audio = numpy_module.frombuffer(completed.stdout, dtype=numpy_module.float32).copy()
    if getattr(audio, "ndim", None) != 1 or len(audio) == 0:
        raise ValueError("ffmpeg returned an empty audio chunk")
    return audio


def load_cuda_runtime() -> tuple[Any, Any, Any, Any]:
    try:
        import numpy as np
        import torch
        from qwen_asr import Qwen3ASRModel, Qwen3ForcedAligner
        qwen_asr_version = version("qwen-asr")
    except (ImportError, PackageNotFoundError) as error:
        raise SystemExit(
            "the CUDA Qwen backend is unavailable; run `uv sync --group "
            "asr-cuda`, then use `uv run --no-sync` for this worker"
        ) from error
    if qwen_asr_version != QWEN_ASR_PACKAGE_VERSION:
        raise SystemExit(
            "unsupported qwen-asr package version: "
            f"expected={QWEN_ASR_PACKAGE_VERSION}, actual={qwen_asr_version}"
        )
    torch_version = str(torch.__version__).partition("+")[0]
    if torch_version != TORCH_PUBLIC_VERSION:
        raise SystemExit(
            "unsupported PyTorch package version: "
            f"expected={TORCH_PUBLIC_VERSION}, actual={torch.__version__}"
        )
    return np, torch, Qwen3ASRModel, Qwen3ForcedAligner


def validate_cuda_device(
    torch_module: Any, *, device: str, dtype_name: str
) -> tuple[Any, int, str, int]:
    match = CUDA_DEVICE_RE.fullmatch(device)
    if match is None:
        raise ValueError("device must use the explicit cuda:<index> form")
    device_index = int(match.group(1))
    if not torch_module.cuda.is_available():
        raise SystemExit("CUDA is unavailable; this worker never falls back to CPU")
    if device_index >= torch_module.cuda.device_count():
        raise ValueError(f"CUDA device index is unavailable: {device}")
    if getattr(torch_module.version, "cuda", None) is None:
        raise SystemExit("the installed PyTorch build has no CUDA runtime")
    torch_module.cuda.set_device(device_index)
    if dtype_name == "bfloat16" and not torch_module.cuda.is_bf16_supported():
        raise ValueError(f"CUDA device {device} does not support bfloat16")
    dtype = getattr(torch_module, dtype_name)
    properties = torch_module.cuda.get_device_properties(device_index)
    return dtype, device_index, str(properties.name), int(properties.total_memory)


def clear_cuda(torch_module: Any) -> None:
    gc.collect()
    torch_module.cuda.empty_cache()


def cuda_synchronize(torch_module: Any, device_index: int) -> None:
    torch_module.cuda.synchronize(device_index)


def cuda_peak_memory(torch_module: Any, device_index: int) -> int:
    return int(torch_module.cuda.max_memory_allocated(device_index))


def validate_alignment_items(items: Any, *, chunk_duration: float) -> list[dict[str, Any]]:
    try:
        values = list(items)
    except TypeError as error:
        raise ValueError("Qwen3-ForcedAligner returned a non-iterable result") from error
    serialized: list[dict[str, Any]] = []
    previous_start = -1.0
    for index, item in enumerate(values):
        text = getattr(item, "text", None)
        if not isinstance(text, str) or not text:
            raise ValueError(f"forced-alignment item {index} has no text")
        start = finite_document_number(
            getattr(item, "start_time", None), field=f"alignment item {index} start"
        )
        end = finite_document_number(
            getattr(item, "end_time", None), field=f"alignment item {index} end"
        )
        if start < previous_start or start < 0 or end < start:
            raise ValueError(f"forced-alignment item {index} has invalid timestamps")
        if (
            start > chunk_duration + ALIGNMENT_TIMESTAMP_TOLERANCE_SECONDS
            or end > chunk_duration + ALIGNMENT_TIMESTAMP_TOLERANCE_SECONDS
        ):
            raise ValueError(
                f"forced-alignment item {index} exceeds its audio chunk: "
                f"start={start}, end={end}, chunk_duration={chunk_duration}"
            )
        start = min(start, chunk_duration)
        end = min(end, chunk_duration)
        serialized.append(
            {
                "text": text,
                "start_time": rounded_seconds(start),
                "end_time": rounded_seconds(end),
            }
        )
        previous_start = start
    return serialized


def cleaned_alignment_text(text: str) -> str:
    """Match the official aligner's punctuation-removal identity."""
    return "".join(character for character in text if is_alignment_character(character))


def transformers_sentence_segments(
    *,
    text: str,
    aligned_items: list[dict[str, Any]],
    offset_seconds: float,
    chunk_id: int,
    first_segment_id: int,
    max_characters: int,
) -> list[dict[str, Any]]:
    """Map sentences to official qwen-asr alignment items without splitting an item.

    qwen-asr 0.0.6 removes punctuation from each whitespace-delimited token before
    it splits CJK characters. Consequently, text such as ``AI、ASR`` is one
    alignment item. Sentence boundaries that fall inside such an item are safely
    coalesced so timestamps never invent a subdivision the aligner did not return.
    """
    expected_text = cleaned_alignment_text(text)
    item_texts = [cleaned_alignment_text(str(item["text"])) for item in aligned_items]
    if any(not item_text for item_text in item_texts):
        raise ValueError("forced alignment returned an empty normalized item")
    actual_text = "".join(item_texts)
    if expected_text != actual_text:
        mismatch_index = next(
            (
                index
                for index, pair in enumerate(zip(expected_text, actual_text))
                if pair[0] != pair[1]
            ),
            min(len(expected_text), len(actual_text)),
        )
        raise ValueError(
            "forced-alignment text mismatch at character "
            f"{mismatch_index}: expected={expected_text[mismatch_index:mismatch_index + 12]!r}, "
            f"actual={actual_text[mismatch_index:mismatch_index + 12]!r}"
        )
    if not aligned_items:
        raise ValueError("forced alignment returned no timestamp items")

    item_boundaries: dict[int, int] = {}
    item_character_count = 0
    for index, item_text in enumerate(item_texts):
        item_character_count += len(item_text)
        item_boundaries[item_character_count] = index

    segments: list[dict[str, Any]] = []
    pending_text = ""
    sentence_character_count = 0
    first_item_index = 0
    for sentence in sentence_texts(text, max_characters=max_characters):
        pending_text += sentence
        sentence_character_count += len(cleaned_alignment_text(sentence))
        last_item_index = item_boundaries.get(sentence_character_count)
        if last_item_index is None:
            continue
        if last_item_index < first_item_index:
            if segments:
                segments[-1]["text"] += pending_text
                pending_text = ""
            continue
        first_item = aligned_items[first_item_index]
        last_item = aligned_items[last_item_index]
        segments.append(
            {
                "id": first_segment_id + len(segments),
                "start": rounded_seconds(
                    offset_seconds + float(first_item["start_time"])
                ),
                "end": rounded_seconds(
                    offset_seconds + float(last_item["end_time"])
                ),
                "text": pending_text,
                "source_chunk_id": chunk_id,
            }
        )
        pending_text = ""
        first_item_index = last_item_index + 1

    if pending_text:
        if not segments:
            raise ValueError("sentence boundaries could not be mapped to alignment items")
        segments[-1]["text"] += pending_text
    if first_item_index != len(aligned_items):
        raise ValueError(
            "alignment item accounting mismatch: "
            f"used={first_item_index}, available={len(aligned_items)}"
        )
    return segments


def validate_arguments(args: argparse.Namespace) -> None:
    if not 0 < args.chunk_duration <= MAX_ALIGNMENT_CHUNK_SECONDS:
        raise ValueError(
            "chunk duration must be greater than 0 and at most 180 seconds"
        )
    if args.max_tokens <= 0:
        raise ValueError("max tokens must be greater than 0")
    if args.max_sentence_characters <= 0:
        raise ValueError("max sentence characters must be greater than 0")
    if args.temperature != 0.0:
        raise ValueError("the official Transformers backend supports temperature 0 only")
    if CUDA_DEVICE_RE.fullmatch(args.device) is None:
        raise ValueError("device must use the explicit cuda:<index> form")
    if args.language not in SUPPORTED_ALIGNMENT_LANGUAGES:
        raise ValueError(
            "language is not supported by Qwen3-ForcedAligner: "
            f"{args.language!r}"
        )


def main() -> int:
    args = parse_args()
    validate_arguments(args)
    input_path = args.input.resolve()
    output_path = args.output.resolve()
    aligned_output_path = args.aligned_output.resolve()
    if not input_path.is_file():
        raise FileNotFoundError(f"audio file does not exist: {input_path}")
    if len({input_path, output_path, aligned_output_path}) != 3:
        raise ValueError("input, raw output, and aligned output paths must be distinct")

    mode = resume_mode(
        raw_exists=output_path.is_file(),
        aligned_exists=aligned_output_path.is_file(),
        retranscribe=args.retranscribe,
        realign=args.realign,
    )
    audio_size_bytes = input_path.stat().st_size
    audio_sha256 = sha256_file(input_path)
    raw_options = raw_backend_options(args)
    alignment_options = aligned_backend_options(args)

    raw_document: dict[str, Any] | None = None
    if mode in {"align-only", "complete"}:
        raw_document = validate_raw_document(
            read_json_strict(output_path),
            engine=ENGINE,
            model=args.model,
            language=args.language,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            chunk_duration=args.chunk_duration,
            audio_size_bytes=audio_size_bytes,
            audio_sha256=audio_sha256,
            backend_options=raw_options,
        )
        validate_cuda_raw_integrity(
            raw_document,
            args=args,
            backend_options=raw_options,
        )
    if mode == "complete":
        raw_asr_sha256 = sha256_file(output_path)
        aligned_document = validate_aligned_document(
            read_json_strict(aligned_output_path),
            engine=ENGINE,
            model=args.model,
            aligner=args.aligner,
            language=args.language,
            audio_sha256=audio_sha256,
            raw_asr_sha256=raw_asr_sha256,
            raw_document=raw_document,
            max_sentence_characters=args.max_sentence_characters,
            backend_options=alignment_options,
        )
        validate_cuda_aligned_integrity(
            aligned_document,
            raw_output_path=output_path,
        )
        validate_file_identity(
            input_path,
            expected_size_bytes=audio_size_bytes,
            expected_sha256=audio_sha256,
            label="input audio",
        )
        if sha256_file(output_path) != raw_asr_sha256:
            raise ValueError("raw ASR changed while its aligned artifact was checked")
        print(
            json.dumps(
                {
                    "status": "skipped-valid",
                    "input": input_path.as_posix(),
                    "output": output_path.as_posix(),
                    "aligned_output": aligned_output_path.as_posix(),
                    "chunks": len(raw_document["segments"]),
                    "sentence_segments": len(aligned_document["segments"]),
                    "engine": ENGINE,
                },
                ensure_ascii=True,
                indent=2,
                allow_nan=False,
            )
        )
        return 0

    model_load_target = (
        local_model_target(args.model_path, label="model", fallback=args.model)
        if mode == "fresh"
        else None
    )
    aligner_load_target = local_model_target(
        args.aligner_path,
        label="aligner",
        fallback=args.aligner,
    )
    if args.model_path is not None and args.aligner_path is not None:
        os.environ["HF_HUB_OFFLINE"] = "1"
        os.environ["TRANSFORMERS_OFFLINE"] = "1"
    ffmpeg = shutil.which("ffmpeg")
    ffprobe = shutil.which("ffprobe")
    if ffmpeg is None or ffprobe is None:
        raise SystemExit("ffmpeg and ffprobe are required for bounded CUDA audio chunks")

    np, torch, Qwen3ASRModel, Qwen3ForcedAligner = load_cuda_runtime()
    dtype, device_index, device_name, total_memory_bytes = validate_cuda_device(
        torch, device=args.device, dtype_name=args.dtype
    )
    audio_duration_seconds = probe_audio_duration(input_path, ffprobe=ffprobe)
    load_kwargs = {
        "dtype": dtype,
        "device_map": args.device,
        "attn_implementation": args.attention_implementation,
    }

    model_load_seconds: float | None = None
    transcription_seconds: float | None = None
    transcription_peak_memory_bytes: int | None = None
    if raw_document is None:
        torch.cuda.reset_peak_memory_stats(device_index)
        model_load_started = time.perf_counter()
        model = Qwen3ASRModel.from_pretrained(
            model_load_target,
            max_inference_batch_size=MAX_INFERENCE_BATCH_SIZE,
            max_new_tokens=args.max_tokens,
            **load_kwargs,
        )
        cuda_synchronize(torch, device_index)
        model_load_seconds = time.perf_counter() - model_load_started

        raw_chunks: list[dict[str, Any]] = []
        text_parts: list[str] = []
        transcription_started = time.perf_counter()
        for chunk_id, (start, requested_end) in enumerate(
            audio_chunk_ranges(
                audio_duration_seconds, chunk_duration=args.chunk_duration
            )
        ):
            if args.verbose:
                print(
                    f"transcribing chunk {chunk_id + 1} at {start:.3f}s",
                    file=sys.stderr,
                    flush=True,
                )
            chunk_audio = decode_audio_chunk(
                input_path,
                start_seconds=start,
                end_seconds=requested_end,
                ffmpeg=ffmpeg,
                numpy_module=np,
            )
            actual_end = min(
                audio_duration_seconds,
                requested_end,
                start + len(chunk_audio) / SAMPLE_RATE,
            )
            if actual_end + 0.5 < requested_end:
                raise ValueError(
                    "ffmpeg decoded an unexpectedly short audio chunk: "
                    f"requested_end={requested_end:.3f}, actual_end={actual_end:.3f}"
                )
            results = model.transcribe(
                audio=(chunk_audio, SAMPLE_RATE),
                language=args.language,
                return_time_stamps=False,
            )
            if not isinstance(results, list) or len(results) != 1:
                raise ValueError("Qwen3-ASR returned an unexpected result count")
            text = getattr(results[0], "text", None)
            if not isinstance(text, str):
                raise ValueError("Qwen3-ASR returned no transcript text")
            text = text.strip()
            raw_chunks.append(
                {
                    "id": chunk_id,
                    "start": rounded_seconds(start),
                    "end": rounded_seconds(actual_end),
                    "text": text,
                }
            )
            text_parts.append(text)
            del results, chunk_audio
            clear_cuda(torch)
        cuda_synchronize(torch, device_index)
        transcription_seconds = time.perf_counter() - transcription_started
        transcription_peak_memory_bytes = cuda_peak_memory(torch, device_index)
        transcript_text = join_transcript_chunks(
            text_parts,
            language=args.language,
        )
        if not transcript_text.strip():
            raise ValueError("Qwen3-ASR returned an empty transcript")

        raw_document = {
            "schema_version": 1,
            "kind": "raw-asr",
            "engine": ENGINE,
            "model": args.model,
            "language": args.language,
            "generated_at": utc_now(),
            "audio": {
                "duration_seconds": rounded_seconds(audio_duration_seconds),
                "sample_rate_hz": SAMPLE_RATE,
                "size_bytes": audio_size_bytes,
                "sha256": audio_sha256,
            },
            "options": {
                "temperature": args.temperature,
                "max_tokens_per_chunk": args.max_tokens,
                "chunk_duration_seconds": args.chunk_duration,
                **raw_options,
            },
            "performance": {
                "model_load_seconds": rounded_seconds(model_load_seconds),
                "transcription_seconds": rounded_seconds(transcription_seconds),
                "cuda_device_name": device_name,
                "cuda_total_memory_bytes": total_memory_bytes,
                "cuda_peak_memory_bytes": transcription_peak_memory_bytes,
            },
            "text": transcript_text,
            "segments": raw_chunks,
        }
        validate_raw_document(
            raw_document,
            engine=ENGINE,
            model=args.model,
            language=args.language,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            chunk_duration=args.chunk_duration,
            audio_size_bytes=audio_size_bytes,
            audio_sha256=audio_sha256,
            backend_options=raw_options,
        )
        validate_cuda_raw_integrity(
            raw_document,
            args=args,
            backend_options=raw_options,
        )
        validate_file_identity(
            input_path,
            expected_size_bytes=audio_size_bytes,
            expected_sha256=audio_sha256,
            label="input audio",
        )
        write_json_atomically(output_path, raw_document)
        if args.retranscribe:
            aligned_output_path.unlink(missing_ok=True)
        del model
        clear_cuda(torch)
    else:
        recorded_duration = finite_document_number(
            raw_document["audio"].get("duration_seconds"), field="audio duration"
        )
        if abs(recorded_duration - audio_duration_seconds) > 0.01:
            raise ValueError("raw ASR duration does not match the decoded input audio")

    raw_chunks = raw_document["segments"]
    raw_asr_sha256 = sha256_file(output_path)
    torch.cuda.reset_peak_memory_stats(device_index)
    aligner_load_started = time.perf_counter()
    aligner = Qwen3ForcedAligner.from_pretrained(
        aligner_load_target,
        **load_kwargs,
    )
    cuda_synchronize(torch, device_index)
    aligner_load_seconds = time.perf_counter() - aligner_load_started

    aligned_chunks: list[dict[str, Any]] = []
    all_segments: list[dict[str, Any]] = []
    alignment_started = time.perf_counter()
    for chunk in raw_chunks:
        chunk_start = float(chunk["start"])
        chunk_end = float(chunk["end"])
        chunk_text = str(chunk["text"]).strip()
        if not chunk_text:
            aligned_chunks.append(
                {
                    **chunk,
                    "alignment_seconds": 0.0,
                    "alignment": [],
                    "sentence_segment_ids": [],
                }
            )
            continue
        if args.verbose:
            print(
                f"aligning chunk {int(chunk['id']) + 1} at {chunk_start:.3f}s",
                file=sys.stderr,
                flush=True,
            )
        chunk_audio = decode_audio_chunk(
            input_path,
            start_seconds=chunk_start,
            end_seconds=chunk_end,
            ffmpeg=ffmpeg,
            numpy_module=np,
        )
        chunk_alignment_started = time.perf_counter()
        alignment_results = aligner.align(
            audio=(chunk_audio, SAMPLE_RATE),
            text=chunk_text,
            language=args.language,
        )
        if not isinstance(alignment_results, list) or len(alignment_results) != 1:
            raise ValueError("Qwen3-ForcedAligner returned an unexpected result count")
        aligned_items = validate_alignment_items(
            alignment_results[0], chunk_duration=chunk_end - chunk_start
        )
        chunk_segments = transformers_sentence_segments(
            text=chunk_text,
            aligned_items=aligned_items,
            offset_seconds=chunk_start,
            chunk_id=int(chunk["id"]),
            first_segment_id=len(all_segments),
            max_characters=args.max_sentence_characters,
        )
        chunk_alignment_seconds = time.perf_counter() - chunk_alignment_started
        all_segments.extend(chunk_segments)
        aligned_chunks.append(
            {
                **chunk,
                "alignment_seconds": rounded_seconds(chunk_alignment_seconds),
                "alignment": [
                    {
                        "text": item["text"],
                        "start": rounded_seconds(
                            chunk_start + float(item["start_time"])
                        ),
                        "end": rounded_seconds(
                            chunk_start + float(item["end_time"])
                        ),
                    }
                    for item in aligned_items
                ],
                "sentence_segment_ids": [
                    segment["id"] for segment in chunk_segments
                ],
            }
        )
        del alignment_results, aligned_items, chunk_segments, chunk_audio
        clear_cuda(torch)
    cuda_synchronize(torch, device_index)
    alignment_seconds = time.perf_counter() - alignment_started
    alignment_peak_memory_bytes = cuda_peak_memory(torch, device_index)

    aligned_document = {
        "schema_version": 1,
        "kind": "aligned-asr",
        "language": args.language,
        "source": {
            "raw_asr_path": repository_path(output_path),
            "engine": ENGINE,
            "model": args.model,
            "aligner": args.aligner,
            "audio_sha256": audio_sha256,
            "raw_asr_sha256": raw_asr_sha256,
        },
        "generated_at": utc_now(),
        "options": {
            "max_sentence_characters": args.max_sentence_characters,
            **alignment_options,
        },
        "performance": {
            "aligner_load_seconds": rounded_seconds(aligner_load_seconds),
            "alignment_seconds": rounded_seconds(alignment_seconds),
            "cuda_device_name": device_name,
            "cuda_total_memory_bytes": total_memory_bytes,
            "cuda_peak_memory_bytes": alignment_peak_memory_bytes,
        },
        "statistics": {
            "source_chunks": len(raw_chunks),
            "aligned_chunks": len(aligned_chunks),
            "alignment_items": sum(
                len(chunk["alignment"]) for chunk in aligned_chunks
            ),
            "sentence_segments": len(all_segments),
        },
        "text": raw_document["text"],
        "chunks": aligned_chunks,
        "segments": all_segments,
    }
    validate_aligned_document(
        aligned_document,
        engine=ENGINE,
        model=args.model,
        aligner=args.aligner,
        language=args.language,
        audio_sha256=audio_sha256,
        raw_asr_sha256=raw_asr_sha256,
        raw_document=raw_document,
        max_sentence_characters=args.max_sentence_characters,
        backend_options=alignment_options,
    )
    validate_cuda_aligned_integrity(
        aligned_document,
        raw_output_path=output_path,
    )
    validate_file_identity(
        input_path,
        expected_size_bytes=audio_size_bytes,
        expected_sha256=audio_sha256,
        label="input audio",
    )
    if sha256_file(output_path) != raw_asr_sha256:
        raise ValueError("raw ASR changed while forced alignment was running")
    write_json_atomically(aligned_output_path, aligned_document)

    del aligner
    clear_cuda(torch)
    status = (
        "aligned-from-existing-raw"
        if mode == "align-only"
        else "transcribed-and-aligned"
    )
    print(
        json.dumps(
            {
                "status": status,
                "input": input_path.as_posix(),
                "output": output_path.as_posix(),
                "aligned_output": aligned_output_path.as_posix(),
                "engine": ENGINE,
                "model": args.model,
                "aligner": args.aligner,
                "duration_seconds": rounded_seconds(audio_duration_seconds),
                "chunks": len(raw_chunks),
                "sentence_segments": len(all_segments),
                "model_load_seconds": (
                    rounded_seconds(model_load_seconds)
                    if model_load_seconds is not None
                    else None
                ),
                "transcription_seconds": (
                    rounded_seconds(transcription_seconds)
                    if transcription_seconds is not None
                    else None
                ),
                "aligner_load_seconds": rounded_seconds(aligner_load_seconds),
                "alignment_seconds": rounded_seconds(alignment_seconds),
            },
            ensure_ascii=True,
            indent=2,
            allow_nan=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
