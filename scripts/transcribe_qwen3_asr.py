#!/usr/bin/env python3
"""Transcribe audio with Qwen3-ASR on MLX and add forced-aligned timestamps."""

from __future__ import annotations

import argparse
import json
import tempfile
import time
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


DEFAULT_MODEL = "mlx-community/Qwen3-ASR-1.7B-8bit"
DEFAULT_ALIGNER = "mlx-community/Qwen3-ForcedAligner-0.6B-8bit"
SAMPLE_RATE = 16_000
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
    return parser.parse_args()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def rounded_seconds(value: float) -> float:
    return round(float(value), 3)


def write_json_atomically(path: Path, document: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
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
    if not 0 < args.chunk_duration < 300:
        raise ValueError("chunk duration must be greater than 0 and less than 300 seconds")
    if args.max_tokens <= 0:
        raise ValueError("max tokens must be greater than 0")
    if args.max_sentence_characters <= 0:
        raise ValueError("max sentence characters must be greater than 0")

    try:
        import mlx.core as mx
        import numpy as np
        from mlx_audio.stt import load
        from mlx_audio.stt.utils import load_audio
    except ImportError as error:
        raise SystemExit(
            "MLX Audio is unavailable; run this script with `uv run --group asr`"
        ) from error

    model_load_started = time.perf_counter()
    model = load(args.model)
    model_load_seconds = time.perf_counter() - model_load_started

    audio = load_audio(input_path.as_posix())
    audio_duration_seconds = len(audio) / SAMPLE_RATE

    transcription_started = time.perf_counter()
    result = model.generate(
        audio,
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
    write_json_atomically(output_path, raw_document)

    del model
    mx.clear_cache()

    aligner_load_started = time.perf_counter()
    aligner_load_target = (
        args.aligner_path.resolve().as_posix()
        if args.aligner_path is not None
        else args.aligner
    )
    aligner = load(aligner_load_target)
    aligner_load_seconds = time.perf_counter() - aligner_load_started

    audio_array = np.array(audio)
    aligned_chunks: list[dict[str, Any]] = []
    all_segments: list[dict[str, Any]] = []
    alignment_started = time.perf_counter()
    for chunk in raw_chunks:
        start_sample = round(float(chunk["start"]) * SAMPLE_RATE)
        end_sample = round(float(chunk["end"]) * SAMPLE_RATE)
        chunk_audio = audio_array[start_sample:end_sample]
        chunk_text = str(chunk["text"]).strip()
        if not chunk_text:
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
        mx.clear_cache()

    alignment_seconds = time.perf_counter() - alignment_started
    aligned_document = {
        "schema_version": 1,
        "kind": "aligned-asr",
        "language": args.language,
        "source": {
            "raw_asr_path": args.output.as_posix(),
            "engine": "mlx-audio",
            "model": args.model,
            "aligner": args.aligner,
        },
        "generated_at": utc_now(),
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
        "text": result.text,
        "chunks": aligned_chunks,
        "segments": all_segments,
    }
    write_json_atomically(aligned_output_path, aligned_document)

    print(
        json.dumps(
            {
                "input": input_path.as_posix(),
                "output": output_path.as_posix(),
                "aligned_output": aligned_output_path.as_posix(),
                "model": args.model,
                "aligner": args.aligner,
                "duration_seconds": rounded_seconds(audio_duration_seconds),
                "chunks": len(raw_chunks),
                "sentence_segments": len(all_segments),
                "model_load_seconds": rounded_seconds(model_load_seconds),
                "transcription_seconds": rounded_seconds(transcription_seconds),
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
