#!/usr/bin/env python3
"""Transcribe audio with Qwen3-ASR on MLX and add forced-aligned timestamps."""

from __future__ import annotations

import argparse
import gc
import hashlib
import json
import math
import tempfile
import time
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


DEFAULT_MODEL = "mlx-community/Qwen3-ASR-1.7B-8bit"
DEFAULT_ALIGNER = "mlx-community/Qwen3-ForcedAligner-0.6B-8bit"
SAMPLE_RATE = 16_000
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SENTENCE_ENDINGS = frozenset("。！？!?")
SOFT_ENDINGS = frozenset("，,；;：:")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run Qwen3-ASR and Qwen3-ForcedAligner locally through MLX Audio."
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
        help="Optional local model directory; artifact metadata still uses --model",
    )
    parser.add_argument("--aligner", default=DEFAULT_ALIGNER)
    parser.add_argument(
        "--aligner-path",
        type=Path,
        help="Optional local aligner directory; artifact metadata still uses --aligner",
    )
    parser.add_argument("--language", default="Chinese")
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--max-tokens", type=int, default=4096)
    parser.add_argument(
        "--chunk-duration",
        type=float,
        default=240.0,
        help="Maximum ASR/alignment chunk length in seconds; keep below 300",
    )
    parser.add_argument(
        "--max-sentence-characters",
        type=int,
        default=160,
        help="Split very long clauses at soft punctuation after this length",
    )
    parser.add_argument(
        "--verbose",
        action=argparse.BooleanOptionalAction,
        default=True,
    )
    replacement = parser.add_mutually_exclusive_group()
    replacement.add_argument(
        "--retranscribe",
        action="store_true",
        help="Explicitly replace both raw and aligned artifacts",
    )
    replacement.add_argument(
        "--realign",
        action="store_true",
        help="Reuse a valid raw artifact and explicitly replace aligned output",
    )
    return parser.parse_args()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def rounded_seconds(value: float) -> float:
    return round(float(value), 3)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def repository_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return resolved.as_posix()


def local_model_target(path: Path | None, *, label: str, fallback: str) -> str:
    if path is None:
        return fallback
    resolved = path.resolve()
    if not resolved.is_dir():
        raise FileNotFoundError(f"local {label} directory does not exist: {resolved}")
    if not (resolved / "config.json").is_file():
        raise FileNotFoundError(f"local {label} has no config.json: {resolved}")
    weight_files = list(resolved.glob("*.safetensors"))
    if not weight_files or any(not weight_file.exists() for weight_file in weight_files):
        raise FileNotFoundError(f"local {label} has missing model weights: {resolved}")
    return resolved.as_posix()


def resume_mode(
    *,
    raw_exists: bool,
    aligned_exists: bool,
    retranscribe: bool,
    realign: bool,
) -> str:
    if retranscribe:
        return "fresh"
    if realign:
        if not raw_exists:
            raise FileNotFoundError("--realign requires an existing raw ASR artifact")
        return "align-only"
    if aligned_exists and not raw_exists:
        raise FileNotFoundError("aligned artifact exists without its raw ASR artifact")
    if aligned_exists:
        return "complete"
    if raw_exists:
        return "align-only"
    return "fresh"


def finite_document_number(value: Any, *, field: str) -> float:
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(value)
    ):
        raise ValueError(f"raw ASR has invalid {field}: {value!r}")
    return float(value)


def validate_raw_document(
    document: Any,
    *,
    model: str,
    language: str,
    temperature: float,
    max_tokens: int,
    chunk_duration: float,
    audio_size_bytes: int,
    audio_sha256: str,
) -> dict[str, Any]:
    if not isinstance(document, dict) or document.get("schema_version") != 1:
        raise ValueError("raw ASR artifact must contain a JSON object")
    expected_values = {
        "kind": "raw-asr",
        "engine": "mlx-audio",
        "model": model,
        "language": language,
    }
    for field, expected in expected_values.items():
        if document.get(field) != expected:
            raise ValueError(
                f"raw ASR {field} mismatch: expected={expected!r}, "
                f"actual={document.get(field)!r}"
            )

    audio = document.get("audio")
    if not isinstance(audio, dict):
        raise ValueError("raw ASR has no audio identity")
    if audio.get("size_bytes") != audio_size_bytes:
        raise ValueError("raw ASR audio size does not match the current input")
    if audio.get("sha256") != audio_sha256:
        raise ValueError("raw ASR audio SHA-256 does not match the current input")
    duration_seconds = finite_document_number(
        audio.get("duration_seconds"), field="audio duration"
    )

    options = document.get("options")
    if not isinstance(options, dict):
        raise ValueError("raw ASR has no decoding options")
    expected_options = {
        "temperature": temperature,
        "max_tokens_per_chunk": max_tokens,
        "chunk_duration_seconds": chunk_duration,
    }
    for field, expected in expected_options.items():
        if options.get(field) != expected:
            raise ValueError(
                f"raw ASR option {field} mismatch: expected={expected!r}, "
                f"actual={options.get(field)!r}"
            )

    text = document.get("text")
    segments = document.get("segments")
    if not isinstance(text, str) or not text.strip():
        raise ValueError("raw ASR has no transcript text")
    if not isinstance(segments, list) or not segments:
        raise ValueError("raw ASR has no segments")
    previous_start = -1.0
    for index, segment in enumerate(segments):
        if not isinstance(segment, dict) or not isinstance(segment.get("text"), str):
            raise ValueError(f"raw ASR segment {index} is invalid")
        if segment.get("id") != index:
            raise ValueError(f"raw ASR segment {index} has a non-contiguous id")
        start = finite_document_number(segment.get("start"), field=f"segment {index} start")
        end = finite_document_number(segment.get("end"), field=f"segment {index} end")
        if start < previous_start or end <= start or end > duration_seconds + 0.1:
            raise ValueError(f"raw ASR segment {index} has invalid timestamp bounds")
        previous_start = start
    return document


def validate_aligned_document(
    document: Any,
    *,
    model: str,
    aligner: str,
    language: str,
    audio_sha256: str,
    raw_asr_sha256: str,
    raw_document: dict[str, Any],
    max_sentence_characters: int,
) -> dict[str, Any]:
    if (
        not isinstance(document, dict)
        or document.get("schema_version") != 1
        or document.get("kind") != "aligned-asr"
    ):
        raise ValueError("aligned ASR artifact has an invalid kind")
    if document.get("language") != language:
        raise ValueError("aligned ASR language does not match the requested language")
    source = document.get("source")
    if not isinstance(source, dict):
        raise ValueError("aligned ASR has no source identity")
    expected_source = {
        "engine": "mlx-audio",
        "model": model,
        "aligner": aligner,
        "audio_sha256": audio_sha256,
        "raw_asr_sha256": raw_asr_sha256,
    }
    for field, expected in expected_source.items():
        if source.get(field) != expected:
            raise ValueError(f"aligned ASR source {field} does not match")
    if document.get("options") != {
        "max_sentence_characters": max_sentence_characters
    }:
        raise ValueError("aligned ASR sentence-splitting options do not match")
    if document.get("text") != raw_document.get("text"):
        raise ValueError("aligned ASR text does not match the raw artifact")

    raw_chunks = raw_document.get("segments")
    chunks = document.get("chunks")
    if not isinstance(raw_chunks, list) or not isinstance(chunks, list):
        raise ValueError("aligned ASR has invalid chunk data")
    if len(chunks) != len(raw_chunks):
        raise ValueError("aligned ASR chunk count does not match raw ASR")
    for index, (chunk, raw_chunk) in enumerate(zip(chunks, raw_chunks)):
        if not isinstance(chunk, dict):
            raise ValueError(f"aligned ASR chunk {index} is invalid")
        for field in ("id", "start", "end", "text"):
            if chunk.get(field) != raw_chunk.get(field):
                raise ValueError(
                    f"aligned ASR chunk {index} field {field} does not match raw ASR"
                )
        if not isinstance(chunk.get("alignment"), list):
            raise ValueError(f"aligned ASR chunk {index} has no alignment items")

    segments = document.get("segments")
    if not isinstance(segments, list) or not segments:
        raise ValueError("aligned ASR has no sentence segments")
    previous_start = -1.0
    for index, segment in enumerate(segments):
        if not isinstance(segment, dict) or not str(segment.get("text", "")).strip():
            raise ValueError(f"aligned ASR segment {index} is invalid")
        if segment.get("id") != index:
            raise ValueError(f"aligned ASR segment {index} has a non-contiguous id")
        start = finite_document_number(
            segment.get("start"), field=f"aligned segment {index} start"
        )
        end = finite_document_number(
            segment.get("end"), field=f"aligned segment {index} end"
        )
        if start < previous_start or end < start:
            raise ValueError(f"aligned ASR segment {index} has invalid timestamp order")
        source_chunk_id = segment.get("source_chunk_id")
        if not isinstance(source_chunk_id, int) or not 0 <= source_chunk_id < len(chunks):
            raise ValueError(f"aligned ASR segment {index} has an invalid source chunk")
        previous_start = start

    statistics = document.get("statistics")
    expected_statistics = {
        "source_chunks": len(raw_chunks),
        "aligned_chunks": len(chunks),
        "alignment_items": sum(len(chunk["alignment"]) for chunk in chunks),
        "sentence_segments": len(segments),
    }
    if statistics != expected_statistics:
        raise ValueError("aligned ASR statistics do not match its content")
    return document


def write_json_atomically(path: Path, document: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".podwiki-{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as stream:
            json.dump(
                document,
                stream,
                ensure_ascii=False,
                indent=2,
                allow_nan=False,
            )
            stream.write("\n")
            temporary_path = Path(stream.name)
        temporary_path.replace(path)
        path.chmod(0o644)
        temporary_path = None
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def read_json_strict(path: Path) -> Any:
    def reject_constant(constant: str) -> None:
        raise ValueError(f"non-standard JSON constant {constant!r} in {path}")

    def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        document: dict[str, Any] = {}
        for key, value in pairs:
            if key in document:
                raise ValueError(f"duplicate JSON key {key!r} in {path}")
            document[key] = value
        return document

    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=reject_duplicate_keys,
        parse_constant=reject_constant,
    )


def is_cjk_character(character: str) -> bool:
    codepoint = ord(character)
    return (
        0x3400 <= codepoint <= 0x4DBF
        or 0x4E00 <= codepoint <= 0x9FFF
        or 0xF900 <= codepoint <= 0xFAFF
        or 0x20000 <= codepoint <= 0x2CEAF
    )


def is_alignment_character(character: str) -> bool:
    if character == "'":
        return True
    return unicodedata.category(character).startswith(("L", "N"))


def alignment_units(text: str) -> list[str]:
    """Tokenize like Qwen3 ForcedAligner's Chinese mixed-text processor."""
    units: list[str] = []
    latin_buffer: list[str] = []

    def flush_latin() -> None:
        if latin_buffer:
            units.append("".join(latin_buffer))
            latin_buffer.clear()

    for character in text:
        if is_cjk_character(character):
            flush_latin()
            units.append(character)
        elif is_alignment_character(character):
            latin_buffer.append(character)
        else:
            flush_latin()

    flush_latin()
    return units


def sentence_texts(text: str, *, max_characters: int) -> list[str]:
    """Split ASR text without dropping punctuation or inventing boundaries."""
    sentences: list[str] = []
    buffer: list[str] = []

    def flush() -> None:
        sentence = "".join(buffer).strip()
        buffer.clear()
        if sentence:
            sentences.append(sentence)

    for character in text:
        buffer.append(character)
        if character in SENTENCE_ENDINGS:
            flush()
        elif len(buffer) >= max_characters and character in SOFT_ENDINGS:
            flush()

    flush()
    return sentences


def sentence_segments(
    *,
    text: str,
    aligned_items: list[dict[str, Any]],
    offset_seconds: float,
    chunk_id: int,
    first_segment_id: int,
    max_characters: int,
) -> list[dict[str, Any]]:
    """Map sentence text back onto character/word alignment items."""
    sentences = sentence_texts(text, max_characters=max_characters)
    expected_units = alignment_units(text)
    actual_units = [str(item["text"]) for item in aligned_items]
    if expected_units != actual_units:
        mismatch_index = next(
            (
                index
                for index, pair in enumerate(zip(expected_units, actual_units))
                if pair[0] != pair[1]
            ),
            min(len(expected_units), len(actual_units)),
        )
        raise ValueError(
            "forced-alignment token mismatch at index "
            f"{mismatch_index}: expected={expected_units[mismatch_index:mismatch_index + 5]!r}, "
            f"actual={actual_units[mismatch_index:mismatch_index + 5]!r}"
        )

    segments: list[dict[str, Any]] = []
    item_index = 0
    for sentence in sentences:
        unit_count = len(alignment_units(sentence))
        if unit_count == 0:
            if segments:
                segments[-1]["text"] += sentence
            continue

        first_item = aligned_items[item_index]
        last_item = aligned_items[item_index + unit_count - 1]
        segments.append(
            {
                "id": first_segment_id + len(segments),
                "start": rounded_seconds(
                    offset_seconds + float(first_item["start_time"])
                ),
                "end": rounded_seconds(
                    offset_seconds + float(last_item["end_time"])
                ),
                "text": sentence,
                "source_chunk_id": chunk_id,
            }
        )
        item_index += unit_count

    if item_index != len(aligned_items):
        raise ValueError(
            f"alignment item accounting mismatch: used={item_index}, "
            f"available={len(aligned_items)}"
        )
    return segments


def serialize_chunks(chunks: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "id": index,
            "start": rounded_seconds(chunk["start"]),
            "end": rounded_seconds(chunk["end"]),
            "text": str(chunk["text"]),
        }
        for index, chunk in enumerate(chunks)
    ]


def main() -> int:
    args = parse_args()
    input_path = args.input.resolve()
    output_path = args.output.resolve()
    aligned_output_path = args.aligned_output.resolve()
    if not input_path.is_file():
        raise FileNotFoundError(f"audio file does not exist: {input_path}")
    if len({input_path, output_path, aligned_output_path}) != 3:
        raise ValueError("input, raw output, and aligned output paths must be distinct")
    if not 0 < args.chunk_duration < 300:
        raise ValueError("chunk duration must be greater than 0 and less than 300 seconds")
    if args.max_tokens <= 0:
        raise ValueError("max tokens must be greater than 0")
    if args.max_sentence_characters <= 0:
        raise ValueError("max sentence characters must be greater than 0")

    mode = resume_mode(
        raw_exists=output_path.is_file(),
        aligned_exists=aligned_output_path.is_file(),
        retranscribe=args.retranscribe,
        realign=args.realign,
    )
    audio_size_bytes = input_path.stat().st_size
    audio_sha256 = sha256_file(input_path)

    raw_document: dict[str, Any] | None = None
    if mode in {"align-only", "complete"}:
        raw_document = validate_raw_document(
            read_json_strict(output_path),
            model=args.model,
            language=args.language,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            chunk_duration=args.chunk_duration,
            audio_size_bytes=audio_size_bytes,
            audio_sha256=audio_sha256,
        )
    if mode == "complete":
        raw_asr_sha256 = sha256_file(output_path)
        aligned_document = validate_aligned_document(
            read_json_strict(aligned_output_path),
            model=args.model,
            aligner=args.aligner,
            language=args.language,
            audio_sha256=audio_sha256,
            raw_asr_sha256=raw_asr_sha256,
            raw_document=raw_document,
            max_sentence_characters=args.max_sentence_characters,
        )
        print(
            json.dumps(
                {
                    "status": "skipped-valid",
                    "input": input_path.as_posix(),
                    "output": output_path.as_posix(),
                    "aligned_output": aligned_output_path.as_posix(),
                    "chunks": len(raw_document["segments"]),
                    "sentence_segments": len(aligned_document["segments"]),
                },
                ensure_ascii=False,
                indent=2,
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

    try:
        import mlx.core as mx
        import numpy as np
        from mlx_audio.stt import load
        from mlx_audio.stt.utils import load_audio
    except ImportError as error:
        raise SystemExit(
            "MLX Audio is unavailable; run `uv sync --all-groups`, then use "
            "`uv run --no-sync` for this worker"
        ) from error

    audio_mx = load_audio(input_path.as_posix())
    audio_array = np.array(audio_mx)
    audio_duration_seconds = len(audio_array) / SAMPLE_RATE
    del audio_mx
    gc.collect()
    mx.clear_cache()

    if raw_document is None:
        model_load_started = time.perf_counter()
        model = load(model_load_target)
        model_load_seconds = time.perf_counter() - model_load_started

        transcription_started = time.perf_counter()
        result = model.generate(
            audio_array,
            max_tokens=args.max_tokens,
            temperature=args.temperature,
            language=args.language,
            chunk_duration=args.chunk_duration,
            verbose=args.verbose,
        )
        transcription_seconds = time.perf_counter() - transcription_started
        if not isinstance(result.text, str) or not isinstance(result.segments, list):
            raise ValueError("Qwen3-ASR returned an unexpected result")

        raw_chunks = serialize_chunks(result.segments)
        raw_document = {
            "schema_version": 1,
            "kind": "raw-asr",
            "engine": "mlx-audio",
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
            },
            "performance": {
                "model_load_seconds": rounded_seconds(model_load_seconds),
                "transcription_seconds": rounded_seconds(transcription_seconds),
                "prompt_tokens": result.prompt_tokens,
                "generation_tokens": result.generation_tokens,
                "prompt_tokens_per_second": rounded_seconds(result.prompt_tps),
                "generation_tokens_per_second": rounded_seconds(result.generation_tps),
            },
            "text": result.text,
            "segments": raw_chunks,
        }
        validate_raw_document(
            raw_document,
            model=args.model,
            language=args.language,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            chunk_duration=args.chunk_duration,
            audio_size_bytes=audio_size_bytes,
            audio_sha256=audio_sha256,
        )
        write_json_atomically(output_path, raw_document)
        if args.retranscribe:
            aligned_output_path.unlink(missing_ok=True)
        del result, model
        gc.collect()
        mx.clear_cache()
    else:
        recorded_duration = finite_document_number(
            raw_document["audio"].get("duration_seconds"),
            field="audio duration",
        )
        if abs(recorded_duration - audio_duration_seconds) > 0.01:
            raise ValueError("raw ASR duration does not match the decoded input audio")

    raw_chunks = raw_document["segments"]
    raw_asr_sha256 = sha256_file(output_path)

    aligner_load_started = time.perf_counter()
    aligner = load(aligner_load_target)
    aligner_load_seconds = time.perf_counter() - aligner_load_started

    aligned_chunks: list[dict[str, Any]] = []
    all_segments: list[dict[str, Any]] = []
    alignment_started = time.perf_counter()
    for chunk in raw_chunks:
        start_sample = round(float(chunk["start"]) * SAMPLE_RATE)
        end_sample = round(float(chunk["end"]) * SAMPLE_RATE)
        chunk_audio = audio_array[start_sample:end_sample]
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

        chunk_alignment_started = time.perf_counter()
        alignment = aligner.generate(
            chunk_audio,
            text=chunk_text,
            language=args.language,
        )
        chunk_alignment_seconds = time.perf_counter() - chunk_alignment_started
        aligned_items = [
            {
                "text": item.text,
                "start_time": rounded_seconds(item.start_time),
                "end_time": rounded_seconds(item.end_time),
            }
            for item in alignment
        ]
        chunk_segments = sentence_segments(
            text=chunk_text,
            aligned_items=aligned_items,
            offset_seconds=float(chunk["start"]),
            chunk_id=int(chunk["id"]),
            first_segment_id=len(all_segments),
            max_characters=args.max_sentence_characters,
        )
        all_segments.extend(chunk_segments)
        aligned_chunks.append(
            {
                **chunk,
                "alignment_seconds": rounded_seconds(chunk_alignment_seconds),
                "alignment": [
                    {
                        "text": item["text"],
                        "start": rounded_seconds(
                            float(chunk["start"]) + float(item["start_time"])
                        ),
                        "end": rounded_seconds(
                            float(chunk["start"]) + float(item["end_time"])
                        ),
                    }
                    for item in aligned_items
                ],
                "sentence_segment_ids": [
                    segment["id"] for segment in chunk_segments
                ],
            }
        )
        del alignment, aligned_items, chunk_segments, chunk_audio
        mx.clear_cache()

    alignment_seconds = time.perf_counter() - alignment_started
    aligned_document = {
        "schema_version": 1,
        "kind": "aligned-asr",
        "language": args.language,
        "source": {
            "raw_asr_path": repository_path(output_path),
            "engine": "mlx-audio",
            "model": args.model,
            "aligner": args.aligner,
            "audio_sha256": audio_sha256,
            "raw_asr_sha256": raw_asr_sha256,
        },
        "generated_at": utc_now(),
        "options": {
            "max_sentence_characters": args.max_sentence_characters,
        },
        "performance": {
            "aligner_load_seconds": rounded_seconds(aligner_load_seconds),
            "alignment_seconds": rounded_seconds(alignment_seconds),
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
        model=args.model,
        aligner=args.aligner,
        language=args.language,
        audio_sha256=audio_sha256,
        raw_asr_sha256=raw_asr_sha256,
        raw_document=raw_document,
        max_sentence_characters=args.max_sentence_characters,
    )
    write_json_atomically(aligned_output_path, aligned_document)

    del aligner, audio_array
    gc.collect()
    mx.clear_cache()

    raw_performance = raw_document.get("performance", {})
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
                "model": args.model,
                "aligner": args.aligner,
                "duration_seconds": rounded_seconds(audio_duration_seconds),
                "chunks": len(raw_chunks),
                "sentence_segments": len(all_segments),
                "model_load_seconds": raw_performance.get("model_load_seconds"),
                "transcription_seconds": raw_performance.get(
                    "transcription_seconds"
                ),
                "aligner_load_seconds": rounded_seconds(aligner_load_seconds),
                "alignment_seconds": rounded_seconds(alignment_seconds),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
