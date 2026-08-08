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
from dataclasses import dataclass
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
AUDIO_DECODE_BOUNDARY_TOLERANCE_SECONDS = 0.01
# Container duration metadata can extend slightly beyond the final decodable PCM
# sample. Keep this allowance final-window-only so interior ownership stays strict.
FINAL_AUDIO_DECODE_SHORTFALL_TOLERANCE_SECONDS = 0.125
DEFAULT_CHUNK_CONTEXT_SECONDS = 5.0
DEFAULT_FINAL_OUTRO_EXEMPTION_SECONDS = 0.0
MAX_FINAL_OUTRO_EXEMPTION_SECONDS = 30.0
SEAM_MATCH_TOLERANCE_SECONDS = 1.0
MIN_SEAM_ANCHOR_RUN_CHARACTERS = 3
MIN_STRICT_SEAM_ANCHOR_RUN_CHARACTERS = 2
STRICT_SEAM_ANCHOR_MAX_DELTA_SECONDS = 0.25
BOUNDARY_RECONCILIATION_METHOD = "forced-alignment-time-crossover-v2"
ALIGNMENT_COVERAGE_GUARD = "active-audio-coverage-v1"
ALIGNED_GAP_GUARD = "low-energy-gap-v1"
COVERAGE_FRAME_SECONDS = 0.5
COVERAGE_ACTIVE_DBFS = -35.0
COVERAGE_MIN_ACTIVE_SECONDS = 10.0
COVERAGE_MIN_ACTIVE_FRACTION = 0.5
GAP_SILENCE_WINDOW_SECONDS = 0.1
GAP_SILENCE_DBFS = -40.0
GAP_MAX_ACTIVE_SECONDS = 0.25
GAP_MAX_ACTIVE_FRACTION = 0.25
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


@dataclass(frozen=True)
class AudioChunkWindow:
    """One contiguous ownership range decoded with bounded acoustic context."""

    ownership_start: float
    ownership_end: float
    decode_start: float
    decode_end: float


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
        help="Own this many seconds per chunk before adding bounded context",
    )
    parser.add_argument(
        "--chunk-context",
        type=float,
        default=DEFAULT_CHUNK_CONTEXT_SECONDS,
        help=(
            "Decode this many extra seconds on each side, then reconcile the "
            "overlap with forced-alignment timestamps"
        ),
    )
    parser.add_argument(
        "--final-outro-exemption-seconds",
        type=float,
        default=DEFAULT_FINAL_OUTRO_EXEMPTION_SECONDS,
        help=(
            "Explicitly permit at most this many uncovered seconds after the "
            "last aligned item of the final ownership chunk; requires external "
            "human or publisher evidence and is capped at 30 seconds"
        ),
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
        "final_outro_exemption_seconds": args.final_outro_exemption_seconds,
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
        "chunk_context_seconds": args.chunk_context,
        "boundary_reconciliation": BOUNDARY_RECONCILIATION_METHOD,
        "alignment_coverage_guard": ALIGNMENT_COVERAGE_GUARD,
        "aligned_gap_guard": ALIGNED_GAP_GUARD,
        "final_outro_exemption_seconds": args.final_outro_exemption_seconds,
    }


def validated_final_outro_exemption_seconds(value: Any) -> float:
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(value)
        or value < 0.0
        or value > MAX_FINAL_OUTRO_EXEMPTION_SECONDS
    ):
        raise ValueError(
            "final outro exemption must be between 0 and 30 seconds"
        )
    return float(value)


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
        "chunk_context_seconds": args.chunk_context,
        "boundary_reconciliation": BOUNDARY_RECONCILIATION_METHOD,
        "alignment_coverage_guard": ALIGNMENT_COVERAGE_GUARD,
        "aligned_gap_guard": ALIGNED_GAP_GUARD,
        **backend_options,
    }
    options = document.get("options")
    if options != expected_options:
        raise ValueError("raw ASR decoding options do not match exactly")
    if not isinstance(options, dict):
        raise ValueError("raw ASR decoding options do not match exactly")
    recorded_final_outro = validated_final_outro_exemption_seconds(
        options.get("final_outro_exemption_seconds")
    )
    if recorded_final_outro != args.final_outro_exemption_seconds:
        raise ValueError("raw ASR final outro exemption does not match")
    audio = document.get("audio")
    if not isinstance(audio, dict) or audio.get("sample_rate_hz") != SAMPLE_RATE:
        raise ValueError("raw ASR sample rate does not match the CUDA backend")
    reconciliation = document.get("boundary_reconciliation")
    if (
        not isinstance(reconciliation, dict)
        or reconciliation.get("method") != BOUNDARY_RECONCILIATION_METHOD
        or reconciliation.get("status") not in {"pending", "complete"}
        or reconciliation.get("chunk_context_seconds") != args.chunk_context
    ):
        raise ValueError("raw ASR has invalid boundary reconciliation metadata")
    segments = document.get("segments")
    if not isinstance(segments, list):
        raise ValueError("raw ASR has invalid source chunks")
    recorded_duration = finite_document_number(
        audio.get("duration_seconds"), field="audio duration"
    )
    expected_windows = list(
        audio_chunk_ranges(
            recorded_duration,
            chunk_duration=args.chunk_duration,
            chunk_context=args.chunk_context,
        )
    )
    if len(segments) != len(expected_windows):
        raise ValueError("raw ASR source chunk count does not match its audio windows")
    previous_ownership_end = 0.0
    for index, (segment, expected_window) in enumerate(
        zip(segments, expected_windows)
    ):
        if not isinstance(segment, dict):
            raise ValueError(f"raw ASR source chunk {index} is invalid")
        decoded_text = segment.get("decoded_text")
        if not isinstance(decoded_text, str):
            raise ValueError(f"raw ASR source chunk {index} has no decoded text")
        ownership_start = finite_document_number(
            segment.get("start"), field=f"chunk {index} ownership start"
        )
        ownership_end = finite_document_number(
            segment.get("end"), field=f"chunk {index} ownership end"
        )
        decode_start = finite_document_number(
            segment.get("decode_start"), field=f"chunk {index} decode start"
        )
        decode_end = finite_document_number(
            segment.get("decode_end"), field=f"chunk {index} decode end"
        )
        expected_ownership_start = rounded_seconds(
            expected_window.ownership_start
        )
        expected_ownership_end = rounded_seconds(expected_window.ownership_end)
        expected_decode_start = rounded_seconds(expected_window.decode_start)
        expected_decode_end = rounded_seconds(expected_window.decode_end)
        decode_end_shortfall = expected_decode_end - decode_end
        maximum_decode_shortfall = (
            FINAL_AUDIO_DECODE_SHORTFALL_TOLERANCE_SECONDS
            if index == len(expected_windows) - 1
            else AUDIO_DECODE_BOUNDARY_TOLERANCE_SECONDS
        )
        if (
            abs(ownership_start - expected_ownership_start) > 0.001
            or abs(ownership_end - expected_ownership_end) > 0.001
            or abs(decode_start - expected_decode_start) > 0.001
            or decode_end_shortfall < -AUDIO_DECODE_BOUNDARY_TOLERANCE_SECONDS
            or decode_end_shortfall > maximum_decode_shortfall
            or not 0.0 <= decode_start < decode_end
            or decode_end
            > recorded_duration + AUDIO_DECODE_BOUNDARY_TOLERANCE_SECONDS
            or decode_end - decode_start
            > MAX_ALIGNMENT_CHUNK_SECONDS
            + AUDIO_DECODE_BOUNDARY_TOLERANCE_SECONDS
        ):
            raise ValueError(f"raw ASR source chunk {index} has invalid ownership")
        previous_ownership_end = ownership_end
        if reconciliation["status"] == "pending":
            if segment.get("text") != decoded_text:
                raise ValueError("pending raw ASR must preserve each full decoded candidate")
            if "owned_item_start" in segment or "owned_item_stop" in segment:
                raise ValueError("pending raw ASR cannot claim reconciled ownership")
        else:
            owned_start = segment.get("owned_item_start")
            owned_stop = segment.get("owned_item_stop")
            if (
                not isinstance(owned_start, int)
                or not isinstance(owned_stop, int)
                or owned_start < 0
                or owned_stop < owned_start
            ):
                raise ValueError(f"raw ASR source chunk {index} has invalid ownership items")
    if abs(previous_ownership_end - recorded_duration) > 0.1:
        raise ValueError("raw ASR chunk ownership does not cover the full audio")
    seams = reconciliation.get("seams")
    if not isinstance(seams, list):
        raise ValueError("raw ASR boundary reconciliation has invalid seams")
    if reconciliation["status"] == "pending" and seams:
        raise ValueError("pending raw ASR cannot contain completed seam records")
    if reconciliation["status"] == "complete":
        if len(seams) != max(0, len(segments) - 1):
            raise ValueError("raw ASR boundary reconciliation seam count is invalid")
        for index, seam in enumerate(seams):
            if (
                not isinstance(seam, dict)
                or seam.get("left_chunk_id") != index
                or seam.get("right_chunk_id") != index + 1
                or seam.get("strategy") not in {"exact-time-anchor", "aligned-gap"}
                or seam.get("seam_seconds") != segments[index].get("end")
            ):
                raise ValueError(f"raw ASR boundary reconciliation seam {index} is invalid")
            matched_characters = seam.get("matched_characters")
            if not isinstance(matched_characters, int) or matched_characters < 0:
                raise ValueError(f"raw ASR boundary seam {index} has invalid confidence")
            if seam["strategy"] == "exact-time-anchor":
                anchor_run_characters = seam.get("anchor_run_characters")
                anchor_run_max_delta = seam.get(
                    "anchor_run_max_pair_delta_seconds"
                )
                strict_short_anchor = anchor_run_characters == (
                    MIN_STRICT_SEAM_ANCHOR_RUN_CHARACTERS
                )
                invalid_anchor_delta = anchor_run_max_delta is not None and (
                    not isinstance(anchor_run_max_delta, (int, float))
                    or isinstance(anchor_run_max_delta, bool)
                    or not math.isfinite(float(anchor_run_max_delta))
                    or float(anchor_run_max_delta) > SEAM_MATCH_TOLERANCE_SECONDS
                )
                if (
                    not isinstance(seam.get("anchor_text"), str)
                    or not seam["anchor_text"]
                    or seam.get("anchor_owner") not in {"left", "right"}
                    or not isinstance(anchor_run_characters, int)
                    or anchor_run_characters
                    < MIN_STRICT_SEAM_ANCHOR_RUN_CHARACTERS
                    or matched_characters < anchor_run_characters
                    or invalid_anchor_delta
                    or (
                        strict_short_anchor
                        and (
                            seam.get("anchor_confidence")
                            != "unique-tight-two-character-run"
                            or anchor_run_max_delta is None
                            or float(anchor_run_max_delta)
                            > STRICT_SEAM_ANCHOR_MAX_DELTA_SECONDS
                        )
                    )
                    or (
                        not strict_short_anchor
                        and "anchor_confidence" in seam
                    )
                ):
                    raise ValueError(
                        f"raw ASR boundary seam {index} has an unreliable exact anchor"
                    )
                finite_document_number(
                    seam.get("anchor_midpoint_seconds"),
                    field=f"boundary seam {index} anchor midpoint",
                )
            else:
                gap_start = finite_document_number(
                    seam.get("gap_start_seconds"),
                    field=f"boundary seam {index} gap start",
                )
                gap_end = finite_document_number(
                    seam.get("gap_end_seconds"),
                    field=f"boundary seam {index} gap end",
                )
                if not gap_start < float(seam["seam_seconds"]) < gap_end:
                    raise ValueError(
                        f"raw ASR boundary seam {index} has invalid gap bounds"
                    )
                if seam.get("acoustic_guard") != {
                    "method": ALIGNED_GAP_GUARD,
                    "status": "verified",
                    "window_seconds": GAP_SILENCE_WINDOW_SECONDS,
                    "maximum_dbfs": GAP_SILENCE_DBFS,
                    "maximum_active_seconds": GAP_MAX_ACTIVE_SECONDS,
                    "maximum_active_fraction": GAP_MAX_ACTIVE_FRACTION,
                }:
                    raise ValueError(
                        f"raw ASR boundary seam {index} has no verified acoustic gap"
                    )
    expected_text = join_transcript_chunks(
        [
            str(segment.get("text", ""))
            for segment in segments
            if isinstance(segment, dict)
        ],
        language=args.language,
    )
    if document.get("text") != expected_text:
        raise ValueError("raw ASR text does not match its source chunks")


def validate_cuda_aligned_integrity(
    document: dict[str, Any],
    *,
    raw_output_path: Path,
    raw_document: dict[str, Any],
) -> None:
    aligned_options = document.get("options")
    raw_options = raw_document.get("options")
    if not isinstance(aligned_options, dict) or not isinstance(raw_options, dict):
        raise ValueError("aligned ASR has invalid final outro provenance")
    aligned_final_outro = validated_final_outro_exemption_seconds(
        aligned_options.get("final_outro_exemption_seconds")
    )
    raw_final_outro = validated_final_outro_exemption_seconds(
        raw_options.get("final_outro_exemption_seconds")
    )
    if aligned_final_outro != raw_final_outro:
        raise ValueError("aligned ASR final outro provenance does not match raw")
    source = document.get("source")
    if not isinstance(source, dict) or source.get("raw_asr_path") != repository_path(
        raw_output_path
    ):
        raise ValueError("aligned ASR raw artifact path does not match")
    reconciliation = raw_document.get("boundary_reconciliation")
    if not isinstance(reconciliation, dict) or reconciliation.get("status") != "complete":
        raise ValueError("aligned ASR requires a completed boundary reconciliation")
    chunks = document.get("chunks")
    raw_chunks = raw_document.get("segments")
    if not isinstance(chunks, list) or not isinstance(raw_chunks, list):
        raise ValueError("aligned ASR has invalid CUDA chunk lineage")
    previous_start = -1.0
    for index, (chunk, raw_chunk) in enumerate(zip(chunks, raw_chunks)):
        if not isinstance(chunk, dict) or not isinstance(raw_chunk, dict):
            raise ValueError(f"aligned ASR CUDA chunk {index} is invalid")
        for field in (
            "decode_start",
            "decode_end",
            "decoded_text",
            "owned_item_start",
            "owned_item_stop",
        ):
            if chunk.get(field) != raw_chunk.get(field):
                raise ValueError(
                    f"aligned ASR CUDA chunk {index} field {field} does not match raw"
                )
        alignment = chunk.get("alignment")
        if not isinstance(alignment, list):
            raise ValueError(f"aligned ASR CUDA chunk {index} has no alignment")
        owned_start = raw_chunk.get("owned_item_start")
        owned_stop = raw_chunk.get("owned_item_stop")
        if (
            not isinstance(owned_start, int)
            or not isinstance(owned_stop, int)
            or owned_start < 0
            or owned_stop < owned_start
            or len(alignment) != owned_stop - owned_start
        ):
            raise ValueError(f"aligned ASR CUDA chunk {index} has invalid ownership")
        if cleaned_alignment_text(str(chunk.get("text", ""))) != "".join(
            cleaned_alignment_text(str(item.get("text", "")))
            for item in alignment
            if isinstance(item, dict)
        ):
            raise ValueError(
                f"aligned ASR CUDA chunk {index} text does not match owned items"
            )
        decode_start = float(chunk["decode_start"])
        decode_end = float(chunk["decode_end"])
        for item in alignment:
            if not isinstance(item, dict):
                raise ValueError(f"aligned ASR CUDA chunk {index} item is invalid")
            item_start = finite_document_number(
                item.get("start"), field=f"CUDA chunk {index} alignment start"
            )
            item_end = finite_document_number(
                item.get("end"), field=f"CUDA chunk {index} alignment end"
            )
            if (
                item_start + ALIGNMENT_TIMESTAMP_TOLERANCE_SECONDS < decode_start
                or item_end < item_start
                or item_start > decode_end + ALIGNMENT_TIMESTAMP_TOLERANCE_SECONDS
                or item_end > decode_end + ALIGNMENT_TIMESTAMP_TOLERANCE_SECONDS
                or item_start + ALIGNMENT_TIMESTAMP_TOLERANCE_SECONDS < previous_start
            ):
                raise ValueError(
                    f"aligned ASR CUDA chunk {index} has invalid owned timestamps"
                )
            previous_start = max(previous_start, item_start)


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
    duration_seconds: float,
    *,
    chunk_duration: float,
    chunk_context: float,
) -> Iterator[AudioChunkWindow]:
    chunk_count = max(1, math.ceil(duration_seconds / chunk_duration))
    ownership_ranges: list[tuple[float, float]] = []
    if chunk_count == 1:
        ownership_ranges.append((0.0, duration_seconds))
    else:
        prefix_count = chunk_count - 2
        for index in range(prefix_count):
            ownership_ranges.append(
                (index * chunk_duration, (index + 1) * chunk_duration)
            )
        tail_start = prefix_count * chunk_duration
        tail_midpoint = tail_start + (duration_seconds - tail_start) / 2.0
        ownership_ranges.extend(
            [
                (tail_start, tail_midpoint),
                (tail_midpoint, duration_seconds),
            ]
        )

    for ownership_start, ownership_end in ownership_ranges:
        if (
            ownership_end <= ownership_start
            or ownership_end - ownership_start > chunk_duration + 0.001
        ):
            raise ValueError("audio chunk duration did not advance within its limit")
        yield AudioChunkWindow(
            ownership_start=ownership_start,
            ownership_end=ownership_end,
            decode_start=max(0.0, ownership_start - chunk_context),
            decode_end=min(duration_seconds, ownership_end + chunk_context),
        )


def alignment_item_midpoint(item: dict[str, Any]) -> float:
    return (float(item["start"]) + float(item["end"])) / 2.0


def _monotonic_exact_match_chain(
    left_items: list[tuple[int, dict[str, Any]]],
    right_items: list[tuple[int, dict[str, Any]]],
    *,
    tolerance_seconds: float,
) -> tuple[list[tuple[int, int]], int]:
    """Match exact alignment units monotonically inside one acoustic overlap."""

    left_texts = [cleaned_alignment_text(str(item["text"])) for _, item in left_items]
    right_texts = [cleaned_alignment_text(str(item["text"])) for _, item in right_items]
    rows = len(left_items)
    columns = len(right_items)
    scores = [[0] * (columns + 1) for _ in range(rows + 1)]
    for left_index in range(rows):
        for right_index in range(columns):
            left_text = left_texts[left_index]
            right_text = right_texts[right_index]
            matches = (
                bool(left_text)
                and left_text == right_text
                and abs(
                    alignment_item_midpoint(left_items[left_index][1])
                    - alignment_item_midpoint(right_items[right_index][1])
                )
                <= tolerance_seconds
            )
            diagonal = (
                scores[left_index][right_index] + len(left_text)
                if matches
                else -1
            )
            scores[left_index + 1][right_index + 1] = max(
                diagonal,
                scores[left_index][right_index + 1],
                scores[left_index + 1][right_index],
            )

    chain: list[tuple[int, int]] = []
    left_index = rows
    right_index = columns
    while left_index and right_index:
        left_text = left_texts[left_index - 1]
        right_text = right_texts[right_index - 1]
        matches = (
            bool(left_text)
            and left_text == right_text
            and abs(
                alignment_item_midpoint(left_items[left_index - 1][1])
                - alignment_item_midpoint(right_items[right_index - 1][1])
            )
            <= tolerance_seconds
        )
        if (
            matches
            and scores[left_index][right_index]
            == scores[left_index - 1][right_index - 1] + len(left_text)
        ):
            chain.append((left_index - 1, right_index - 1))
            left_index -= 1
            right_index -= 1
        elif scores[left_index - 1][right_index] >= scores[left_index][right_index - 1]:
            left_index -= 1
        else:
            right_index -= 1
    chain.reverse()
    return chain, scores[rows][columns]


def _maximal_exact_match_runs(
    left_items: list[tuple[int, dict[str, Any]]],
    right_items: list[tuple[int, dict[str, Any]]],
    *,
    tolerance_seconds: float,
) -> list[list[tuple[int, int]]]:
    """Enumerate every maximal contiguous exact/time-gated match run.

    A single weighted-LCS traceback is insufficient here: repeated speech can have
    multiple equally valid tracebacks, and choosing one can silently drop or duplicate
    words at the ownership seam. Enumerating maximal diagonal runs exposes every
    reliable candidate mapping before a crossover is selected.
    """

    left_texts = [cleaned_alignment_text(str(item["text"])) for _, item in left_items]
    right_texts = [cleaned_alignment_text(str(item["text"])) for _, item in right_items]

    def matches(left_index: int, right_index: int) -> bool:
        left_text = left_texts[left_index]
        return (
            bool(left_text)
            and left_text == right_texts[right_index]
            and abs(
                alignment_item_midpoint(left_items[left_index][1])
                - alignment_item_midpoint(right_items[right_index][1])
            )
            <= tolerance_seconds
        )

    runs: list[list[tuple[int, int]]] = []
    for left_index in range(len(left_items)):
        for right_index in range(len(right_items)):
            if not matches(left_index, right_index):
                continue
            if (
                left_index > 0
                and right_index > 0
                and matches(left_index - 1, right_index - 1)
            ):
                continue
            run: list[tuple[int, int]] = []
            offset = 0
            while (
                left_index + offset < len(left_items)
                and right_index + offset < len(right_items)
                and matches(left_index + offset, right_index + offset)
            ):
                run.append((left_index + offset, right_index + offset))
                offset += 1
            runs.append(run)
    return runs


def _match_runs_are_disjoint_and_ordered(
    left_run: list[tuple[int, int]],
    right_run: list[tuple[int, int]],
) -> bool:
    left_first, right_first = left_run[0]
    left_last, right_last = left_run[-1]
    other_left_first, other_right_first = right_run[0]
    other_left_last, other_right_last = right_run[-1]
    left_before = left_last < other_left_first
    right_before = right_last < other_right_first
    left_after = other_left_last < left_first
    right_after = other_right_last < right_first
    return (left_before and right_before) or (left_after and right_after)


def _drop_strictly_dominated_match_runs(
    runs: list[tuple[list[tuple[int, int]], int, float]],
) -> list[tuple[list[tuple[int, int]], int, float]]:
    """Discard only weaker conflicts that cannot represent a better mapping.

    A short common phrase can appear inside a much longer, tighter exact match and
    again nearby.  Treating that incidental phrase as an equal alternative makes
    valid speech fail closed.  It is safe to discard it only when a conflicting run
    has strictly more exact characters and no worse maximum timestamp delta.  Equal
    length, tighter, or otherwise incomparable conflicts remain ambiguous.
    """

    def dominates(
        stronger: tuple[list[tuple[int, int]], int, float],
        weaker: tuple[list[tuple[int, int]], int, float],
    ) -> bool:
        stronger_run, stronger_characters, stronger_delta = stronger
        weaker_run, weaker_characters, weaker_delta = weaker
        return (
            not _match_runs_are_disjoint_and_ordered(stronger_run, weaker_run)
            and stronger_characters > weaker_characters
            and stronger_delta <= weaker_delta
        )

    frontier_indices = {
        index
        for index, candidate in enumerate(runs)
        if not any(
            other_index != index and dominates(other, candidate)
            for other_index, other in enumerate(runs)
        )
    }
    return [
        candidate
        for index, candidate in enumerate(runs)
        if index in frontier_indices
        or not any(
            dominates(runs[frontier_index], candidate)
            for frontier_index in frontier_indices
        )
    ]


def _validate_unique_monotonic_match_runs(
    runs: list[list[tuple[int, int]]],
) -> None:
    """Reject candidate runs that permit more than one monotonic item mapping."""

    for index, left_run in enumerate(runs):
        for right_run in runs[index + 1 :]:
            if not _match_runs_are_disjoint_and_ordered(left_run, right_run):
                raise ValueError(
                    "overlapping ASR chunks have ambiguous exact alignment candidates"
                )


def _gap_crossover(
    left_items: list[dict[str, Any]],
    right_items: list[dict[str, Any]],
    *,
    seam_seconds: float,
) -> tuple[int, int, float, float] | None:
    """Return a deterministic crossover only when both decodes expose a gap."""

    def gap(items: list[dict[str, Any]]) -> tuple[float, float, int]:
        next_index = next(
            (
                index
                for index, item in enumerate(items)
                if alignment_item_midpoint(item) >= seam_seconds
            ),
            len(items),
        )
        before_end = (
            max(float(item["end"]) for item in items[:next_index])
            if next_index
            else float("-inf")
        )
        after_start = (
            min(float(item["start"]) for item in items[next_index:])
            if next_index < len(items)
            else float("inf")
        )
        return before_end, after_start, next_index

    left_before, left_after, left_cut = gap(left_items)
    right_before, right_after, right_cut = gap(right_items)
    common_gap_start = max(left_before, right_before)
    common_gap_end = min(left_after, right_after)
    if common_gap_start <= seam_seconds <= common_gap_end:
        return left_cut, right_cut, common_gap_start, common_gap_end
    return None


def seam_crossover(
    left_items: list[dict[str, Any]],
    right_items: list[dict[str, Any]],
    *,
    seam_seconds: float,
    shared_start: float,
    shared_end: float,
    tolerance_seconds: float = SEAM_MATCH_TOLERANCE_SECONDS,
) -> tuple[int, int, dict[str, Any]]:
    """Choose one exact, time-constrained ownership switch for a seam."""

    left_overlap = [
        (index, item)
        for index, item in enumerate(left_items)
        if shared_start <= alignment_item_midpoint(item) <= shared_end
    ]
    right_overlap = [
        (index, item)
        for index, item in enumerate(right_items)
        if shared_start <= alignment_item_midpoint(item) <= shared_end
    ]
    _, matched_characters = _monotonic_exact_match_chain(
        left_overlap,
        right_overlap,
        tolerance_seconds=tolerance_seconds,
    )
    anchors: list[tuple[float, float, int, int, str, int, float]] = []
    anchor_confidence: str | None = None
    match_runs = _maximal_exact_match_runs(
        left_overlap,
        right_overlap,
        tolerance_seconds=tolerance_seconds,
    )
    reliable_match_runs: list[
        tuple[list[tuple[int, int]], int, float]
    ] = []
    for run in match_runs:
        run_characters = sum(
            len(
                cleaned_alignment_text(
                    str(left_overlap[left_local][1]["text"])
                )
            )
            for left_local, _ in run
        )
        run_max_pair_delta = max(
            abs(
                alignment_item_midpoint(left_overlap[left_local][1])
                - alignment_item_midpoint(right_overlap[right_local][1])
            )
            for left_local, right_local in run
        )
        if run_characters < MIN_SEAM_ANCHOR_RUN_CHARACTERS:
            continue
        reliable_match_runs.append(
            (run, run_characters, run_max_pair_delta)
        )
    reliable_match_runs = _drop_strictly_dominated_match_runs(
        reliable_match_runs
    )
    if reliable_match_runs:
        try:
            _validate_unique_monotonic_match_runs(
                [run for run, _, _ in reliable_match_runs]
            )
        except ValueError as error:
            candidate_summary = [
                {
                    "left": [
                        left_overlap[run[0][0]][0],
                        left_overlap[run[-1][0]][0],
                    ],
                    "right": [
                        right_overlap[run[0][1]][0],
                        right_overlap[run[-1][1]][0],
                    ],
                    "characters": run_characters,
                    "maximum_pair_delta_seconds": rounded_seconds(
                        run_max_pair_delta
                    ),
                    "text": "".join(
                        cleaned_alignment_text(
                            str(left_overlap[left_local][1]["text"])
                        )
                        for left_local, _ in run
                    ),
                }
                for run, run_characters, run_max_pair_delta in reliable_match_runs
            ]
            raise ValueError(
                f"{error} at {seam_seconds:.3f}s: "
                f"{json.dumps(candidate_summary, ensure_ascii=False)}"
            ) from error
    for run, run_characters, run_max_pair_delta in reliable_match_runs:
        run_anchors: list[tuple[float, float, int, int, str, int, float]] = []
        for left_local, right_local in run:
            left_index, left_item = left_overlap[left_local]
            right_index, right_item = right_overlap[right_local]
            left_midpoint = alignment_item_midpoint(left_item)
            right_midpoint = alignment_item_midpoint(right_item)
            anchor_midpoint = (left_midpoint + right_midpoint) / 2.0
            run_anchors.append(
                (
                    abs(anchor_midpoint - seam_seconds),
                    abs(left_midpoint - right_midpoint),
                    left_index,
                    right_index,
                    cleaned_alignment_text(str(left_item["text"])),
                    run_characters,
                    run_max_pair_delta,
                )
            )
        anchors.extend(run_anchors)
    if not anchors:
        strict_short_anchor_runs: list[
            list[tuple[float, float, int, int, str, int, float]]
        ] = []
        for left_local in range(len(left_overlap) - 1):
            left_pair = left_overlap[left_local : left_local + 2]
            left_texts = [
                cleaned_alignment_text(str(item["text"]))
                for _, item in left_pair
            ]
            if (
                left_pair[1][0] != left_pair[0][0] + 1
                or any(len(text) != 1 for text in left_texts)
            ):
                continue
            for right_local in range(len(right_overlap) - 1):
                right_pair = right_overlap[right_local : right_local + 2]
                right_texts = [
                    cleaned_alignment_text(str(item["text"]))
                    for _, item in right_pair
                ]
                if (
                    right_pair[1][0] != right_pair[0][0] + 1
                    or left_texts != right_texts
                    or any(len(text) != 1 for text in right_texts)
                ):
                    continue
                pair_deltas = [
                    abs(
                        alignment_item_midpoint(left_pair[offset][1])
                        - alignment_item_midpoint(right_pair[offset][1])
                    )
                    for offset in range(2)
                ]
                if max(pair_deltas) > STRICT_SEAM_ANCHOR_MAX_DELTA_SECONDS:
                    continue
                run_max_pair_delta = max(pair_deltas)
                run_anchors = []
                for offset in range(2):
                    left_index, left_item = left_pair[offset]
                    right_index, right_item = right_pair[offset]
                    left_midpoint = alignment_item_midpoint(left_item)
                    right_midpoint = alignment_item_midpoint(right_item)
                    anchor_midpoint = (left_midpoint + right_midpoint) / 2.0
                    run_anchors.append(
                        (
                            abs(anchor_midpoint - seam_seconds),
                            abs(left_midpoint - right_midpoint),
                            left_index,
                            right_index,
                            left_texts[offset],
                            MIN_STRICT_SEAM_ANCHOR_RUN_CHARACTERS,
                            run_max_pair_delta,
                        )
                    )
                strict_short_anchor_runs.append(run_anchors)
        if len(strict_short_anchor_runs) == 1:
            anchors = strict_short_anchor_runs[0]
            anchor_confidence = "unique-tight-two-character-run"
    if anchors:
        (
            _,
            _,
            left_index,
            right_index,
            anchor_text,
            anchor_run_characters,
            anchor_run_max_pair_delta,
        ) = min(anchors)
        left_midpoint = alignment_item_midpoint(left_items[left_index])
        right_midpoint = alignment_item_midpoint(right_items[right_index])
        anchor_midpoint = (left_midpoint + right_midpoint) / 2.0
        if anchor_midpoint <= seam_seconds:
            left_stop = left_index + 1
            right_start = right_index + 1
            owner = "left"
        else:
            left_stop = left_index
            right_start = right_index
            owner = "right"
        record = {
            "seam_seconds": rounded_seconds(seam_seconds),
            "strategy": "exact-time-anchor",
            "anchor_text": anchor_text,
            "anchor_midpoint_seconds": rounded_seconds(anchor_midpoint),
            "anchor_owner": owner,
            "matched_characters": matched_characters,
            "anchor_run_characters": anchor_run_characters,
            "anchor_run_max_pair_delta_seconds": rounded_seconds(
                anchor_run_max_pair_delta
            ),
        }
        if anchor_confidence is not None:
            record["anchor_confidence"] = anchor_confidence
        return (
            left_stop,
            right_start,
            record,
        )

    gap = _gap_crossover(
        left_items,
        right_items,
        seam_seconds=seam_seconds,
    )
    if gap is not None:
        gap_start = max(shared_start, gap[2])
        gap_end = min(shared_end, gap[3])
        if not gap_start < seam_seconds < gap_end:
            raise ValueError(
                "overlapping ASR chunks have no positive aligned gap around "
                f"{seam_seconds:.3f}s"
            )
        return (
            gap[0],
            gap[1],
            {
                "seam_seconds": rounded_seconds(seam_seconds),
                "strategy": "aligned-gap",
                "matched_characters": matched_characters,
                "gap_start_seconds": rounded_seconds(gap_start),
                "gap_end_seconds": rounded_seconds(gap_end),
            },
        )
    raise ValueError(
        "overlapping ASR chunks have no reliable exact alignment crossover at "
        f"{seam_seconds:.3f}s"
    )


def text_for_alignment_slice(
    text: str,
    aligned_items: list[dict[str, Any]],
    *,
    start_item: int,
    stop_item: int,
) -> str:
    """Map one contiguous aligner-item slice back to the original punctuation."""

    if not 0 <= start_item <= stop_item <= len(aligned_items):
        raise ValueError("alignment ownership slice is out of bounds")
    normalized_items = [
        cleaned_alignment_text(str(item["text"])) for item in aligned_items
    ]
    if any(not item for item in normalized_items):
        raise ValueError("forced alignment returned an empty normalized item")
    expected_text = cleaned_alignment_text(text)
    if "".join(normalized_items) != expected_text:
        raise ValueError("forced-alignment text cannot be mapped back to its decode")
    if start_item == stop_item:
        return ""

    significant_positions = [
        index for index, character in enumerate(text) if is_alignment_character(character)
    ]
    item_character_offsets = [0]
    for item in normalized_items:
        item_character_offsets.append(item_character_offsets[-1] + len(item))
    if item_character_offsets[-1] != len(significant_positions):
        raise ValueError("forced-alignment character accounting mismatch")

    if start_item == 0:
        original_start = 0
    else:
        original_start = significant_positions[item_character_offsets[start_item]]
    if stop_item == len(aligned_items):
        original_stop = len(text)
    else:
        original_stop = significant_positions[item_character_offsets[stop_item]]
    owned_text = text[original_start:original_stop].strip()
    expected_owned_text = "".join(normalized_items[start_item:stop_item])
    if cleaned_alignment_text(owned_text) != expected_owned_text:
        raise ValueError("reconciled text does not match its owned alignment items")
    return owned_text


def reconcile_candidate_slices(
    candidates: list[dict[str, Any]],
) -> tuple[list[tuple[int, int]], list[dict[str, Any]]]:
    """Assign every overlap through one monotonic, auditable crossover."""

    slices = [[0, len(candidate["alignment"])] for candidate in candidates]
    seam_records: list[dict[str, Any]] = []
    for index in range(len(candidates) - 1):
        left = candidates[index]
        right = candidates[index + 1]
        seam_seconds = float(left["ownership_end"])
        if abs(seam_seconds - float(right["ownership_start"])) > 0.001:
            raise ValueError("ASR chunk ownership ranges are not contiguous")
        shared_start = max(float(left["decode_start"]), float(right["decode_start"]))
        shared_end = min(float(left["decode_end"]), float(right["decode_end"]))
        if not shared_start < seam_seconds < shared_end:
            raise ValueError("ASR chunk context does not surround its ownership seam")
        left_stop, right_start, record = seam_crossover(
            left["alignment"],
            right["alignment"],
            seam_seconds=seam_seconds,
            shared_start=shared_start,
            shared_end=shared_end,
        )
        slices[index][1] = left_stop
        slices[index + 1][0] = right_start
        seam_records.append(
            {
                "left_chunk_id": index,
                "right_chunk_id": index + 1,
                **record,
            }
        )

    previous_start = -1.0
    finalized: list[tuple[int, int]] = []
    for index, (start_item, stop_item) in enumerate(slices):
        if not 0 <= start_item <= stop_item <= len(candidates[index]["alignment"]):
            raise ValueError(f"ASR chunk {index} has an invalid ownership slice")
        for item in candidates[index]["alignment"][start_item:stop_item]:
            item_start = float(item["start"])
            if item_start + ALIGNMENT_TIMESTAMP_TOLERANCE_SECONDS < previous_start:
                raise ValueError("reconciled alignment items are not globally monotonic")
            previous_start = max(previous_start, item_start)
        finalized.append((start_item, stop_item))
    return finalized, seam_records


def alignment_coverage_suspicions(
    *,
    ownership_start: float,
    ownership_end: float,
    text: str,
    alignment: list[dict[str, Any]],
    is_first_chunk: bool,
    is_last_chunk: bool,
) -> list[dict[str, Any]]:
    """Find every large ownership gap that requires an active-audio probe.

    Chunk position remains part of the call contract, but neither first/last
    position nor terminal punctuation exempts uncovered audio. The acoustic
    probe decides whether a leading, internal, or trailing gap is safe.
    """

    duration = ownership_end - ownership_start
    if duration <= 0:
        raise ValueError("alignment coverage ownership duration is invalid")
    suspicions: list[dict[str, Any]] = []
    normalized_characters = len(cleaned_alignment_text(text))
    density = normalized_characters / duration
    if duration >= 60.0 and density < 0.5:
        suspicions.append(
            {
                "kind": "sparse-text",
                "start": ownership_start,
                "end": ownership_end,
                "detail": f"{density:.3f} normalized characters/second",
            }
        )

    moderate_threshold = max(15.0, 0.15 * duration)
    coverage_intervals = sorted(
        (
            max(ownership_start, float(item["start"])),
            min(ownership_end, float(item["end"])),
        )
        for item in alignment
        if float(item["end"]) > ownership_start
        and float(item["start"]) < ownership_end
    )
    merged_intervals: list[list[float]] = []
    for interval_start, interval_end in coverage_intervals:
        if interval_end < interval_start:
            raise ValueError("alignment coverage interval is invalid")
        if merged_intervals and interval_start <= merged_intervals[-1][1]:
            merged_intervals[-1][1] = max(merged_intervals[-1][1], interval_end)
        else:
            merged_intervals.append([interval_start, interval_end])

    if not merged_intervals:
        suspicions.append(
            {
                "kind": "active-leading-gap",
                "start": ownership_start,
                "end": ownership_end,
                "detail": f"{duration:.3f}s with no aligned item",
            }
        )
        return suspicions

    first_start = merged_intervals[0][0]
    leading_gap = max(0.0, first_start - ownership_start)
    if leading_gap >= moderate_threshold:
        suspicions.append(
            {
                "kind": "active-leading-gap",
                "start": ownership_start,
                "end": first_start,
                "detail": f"{leading_gap:.3f}s before the first aligned item",
            }
        )

    for left_interval, right_interval in zip(
        merged_intervals,
        merged_intervals[1:],
    ):
        gap_start = left_interval[1]
        gap_end = right_interval[0]
        internal_gap = max(0.0, gap_end - gap_start)
        if internal_gap >= moderate_threshold:
            suspicions.append(
                {
                    "kind": "active-internal-gap",
                    "start": gap_start,
                    "end": gap_end,
                    "detail": f"{internal_gap:.3f}s between aligned items",
                }
            )

    last_end = merged_intervals[-1][1]
    trailing_gap = max(0.0, ownership_end - last_end)
    if trailing_gap >= moderate_threshold:
        suspicions.append(
            {
                "kind": "active-trailing-gap",
                "start": last_end,
                "end": ownership_end,
                "detail": f"{trailing_gap:.3f}s after the last aligned item",
            }
        )
    return suspicions


def active_audio_statistics(
    audio: Any,
    *,
    numpy_module: Any,
    frame_seconds: float = COVERAGE_FRAME_SECONDS,
    active_dbfs: float = COVERAGE_ACTIVE_DBFS,
) -> tuple[float, float]:
    """Return active seconds and active-frame fraction for float32 mono audio."""

    frame_samples = max(1, round(frame_seconds * SAMPLE_RATE))
    active_seconds = 0.0
    total_seconds = 0.0
    active_frames = 0
    total_frames = 0
    for start in range(0, len(audio), frame_samples):
        frame = audio[start : start + frame_samples]
        if len(frame) == 0:
            continue
        centered = frame - numpy_module.mean(frame)
        rms = float(numpy_module.sqrt(numpy_module.mean(centered * centered)))
        dbfs = 20.0 * math.log10(max(rms, 1e-12))
        seconds = len(frame) / SAMPLE_RATE
        total_seconds += seconds
        total_frames += 1
        if dbfs >= active_dbfs:
            active_seconds += seconds
            active_frames += 1
    active_fraction = active_frames / total_frames if total_frames else 0.0
    return active_seconds, active_fraction


def contains_low_energy_window(
    audio: Any,
    *,
    numpy_module: Any,
    window_seconds: float = GAP_SILENCE_WINDOW_SECONDS,
    maximum_dbfs: float = GAP_SILENCE_DBFS,
) -> bool:
    """Return whether audio contains one short, genuinely low-energy window."""

    window_samples = max(1, round(window_seconds * SAMPLE_RATE))
    if len(audio) < window_samples:
        return False
    hop_samples = max(1, window_samples // 2)
    starts = list(range(0, len(audio) - window_samples + 1, hop_samples))
    final_start = len(audio) - window_samples
    if not starts or starts[-1] != final_start:
        starts.append(final_start)
    for start in starts:
        frame = audio[start : start + window_samples]
        centered = frame - numpy_module.mean(frame)
        rms = float(numpy_module.sqrt(numpy_module.mean(centered * centered)))
        dbfs = 20.0 * math.log10(max(rms, 1e-12))
        if dbfs <= maximum_dbfs:
            return True
    return False


def enforce_aligned_gap_silence(
    *,
    input_path: Path,
    seam_records: list[dict[str, Any]],
    ffmpeg: str,
    numpy_module: Any,
) -> None:
    """Permit an alignment-gap crossover only after an acoustic silence check."""

    for seam in seam_records:
        if seam.get("strategy") != "aligned-gap":
            continue
        gap_start = float(seam["gap_start_seconds"])
        gap_end = float(seam["gap_end_seconds"])
        if gap_end - gap_start < GAP_SILENCE_WINDOW_SECONDS:
            raise ValueError(
                "aligned ASR gap is too short for an acoustic silence check at "
                f"{float(seam['seam_seconds']):.3f}s"
            )
        gap_audio = decode_audio_chunk(
            input_path,
            start_seconds=gap_start,
            end_seconds=gap_end,
            ffmpeg=ffmpeg,
            numpy_module=numpy_module,
        )
        verified = contains_low_energy_window(
            gap_audio,
            numpy_module=numpy_module,
        )
        active_seconds, active_fraction = active_audio_statistics(
            gap_audio,
            numpy_module=numpy_module,
            frame_seconds=GAP_SILENCE_WINDOW_SECONDS,
            active_dbfs=COVERAGE_ACTIVE_DBFS,
        )
        del gap_audio
        if (
            not verified
            or active_seconds > GAP_MAX_ACTIVE_SECONDS
            or active_fraction > GAP_MAX_ACTIVE_FRACTION
        ):
            raise ValueError(
                "aligned ASR gap is not acoustically quiet at "
                f"{float(seam['seam_seconds']):.3f}s: "
                f"active_seconds={active_seconds:.3f}, "
                f"active_fraction={active_fraction:.3f}"
            )
        seam["acoustic_guard"] = {
            "method": ALIGNED_GAP_GUARD,
            "status": "verified",
            "window_seconds": GAP_SILENCE_WINDOW_SECONDS,
            "maximum_dbfs": GAP_SILENCE_DBFS,
            "maximum_active_seconds": GAP_MAX_ACTIVE_SECONDS,
            "maximum_active_fraction": GAP_MAX_ACTIVE_FRACTION,
        }


def enforce_alignment_coverage(
    *,
    input_path: Path,
    chunks: list[dict[str, Any]],
    ffmpeg: str,
    numpy_module: Any,
    final_outro_exemption_seconds: float = DEFAULT_FINAL_OUTRO_EXEMPTION_SECONDS,
) -> None:
    """Fail closed when a long untranscribed region contains sustained audio."""

    final_outro_exemption_seconds = validated_final_outro_exemption_seconds(
        final_outro_exemption_seconds
    )

    global_owned_alignment: list[dict[str, Any]] = []
    for index, chunk in enumerate(chunks):
        alignment = chunk.get("alignment")
        if not isinstance(alignment, list):
            raise ValueError(f"ASR chunk {index} has invalid owned alignment")
        for item_index, item in enumerate(alignment):
            if not isinstance(item, dict):
                raise ValueError(
                    f"ASR chunk {index} owned alignment {item_index} is invalid"
                )
            item_start = finite_document_number(
                item.get("start"),
                field=f"chunk {index} owned alignment {item_index} start",
            )
            item_end = finite_document_number(
                item.get("end"),
                field=f"chunk {index} owned alignment {item_index} end",
            )
            if item_end < item_start:
                raise ValueError(
                    f"ASR chunk {index} owned alignment {item_index} is invalid"
                )
            global_owned_alignment.append(item)

    for index, chunk in enumerate(chunks):
        ownership_start = float(chunk["start"])
        ownership_end = float(chunk["end"])
        core_alignment = [
            item
            for item in global_owned_alignment
            if float(item["end"]) > ownership_start
            and float(item["start"]) < ownership_end
        ]
        core_text = "".join(str(item.get("text", "")) for item in core_alignment)
        suspicions = alignment_coverage_suspicions(
            ownership_start=ownership_start,
            ownership_end=ownership_end,
            text=core_text,
            alignment=core_alignment,
            is_first_chunk=index == 0,
            is_last_chunk=index == len(chunks) - 1,
        )
        for suspicion in suspicions:
            probe_start = float(suspicion["start"])
            probe_end = float(suspicion["end"])
            if probe_end <= probe_start:
                continue
            if (
                final_outro_exemption_seconds > 0.0
                and index == len(chunks) - 1
                and suspicion["kind"] == "active-trailing-gap"
                and probe_end - probe_start
                <= final_outro_exemption_seconds + 0.001
            ):
                continue
            probe_audio = decode_audio_chunk(
                input_path,
                start_seconds=probe_start,
                end_seconds=probe_end,
                ffmpeg=ffmpeg,
                numpy_module=numpy_module,
            )
            active_seconds, active_fraction = active_audio_statistics(
                probe_audio,
                numpy_module=numpy_module,
            )
            del probe_audio
            if (
                active_seconds >= COVERAGE_MIN_ACTIVE_SECONDS
                and active_fraction >= COVERAGE_MIN_ACTIVE_FRACTION
            ):
                raise ValueError(
                    f"ASR chunk {index} failed {ALIGNMENT_COVERAGE_GUARD}: "
                    f"{suspicion['kind']} ({suspicion['detail']}), "
                    f"active_seconds={active_seconds:.3f}, "
                    f"active_fraction={active_fraction:.3f}"
                )


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
    item_source_chunk_ids: list[int] | None = None,
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
    if item_source_chunk_ids is not None and (
        len(item_source_chunk_ids) != len(aligned_items)
        or any(
            not isinstance(source_chunk_id, int) or source_chunk_id < 0
            for source_chunk_id in item_source_chunk_ids
        )
    ):
        raise ValueError("forced alignment has invalid source chunk ownership")
    previous_item_start = -1.0
    for index, item in enumerate(aligned_items):
        item_start = finite_document_number(
            item.get("start_time"), field=f"sentence alignment item {index} start"
        )
        item_end = finite_document_number(
            item.get("end_time"), field=f"sentence alignment item {index} end"
        )
        if item_start < previous_item_start or item_end < item_start:
            raise ValueError("forced alignment is not globally monotonic")
        previous_item_start = item_start

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
                "source_chunk_id": (
                    chunk_id
                    if item_source_chunk_ids is None
                    else item_source_chunk_ids[first_item_index]
                ),
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
    if not math.isfinite(args.chunk_duration) or args.chunk_duration <= 0:
        raise ValueError("chunk duration must be greater than 0")
    if not math.isfinite(args.chunk_context) or args.chunk_context <= 0:
        raise ValueError("chunk context must be greater than 0")
    if args.chunk_duration + 2 * args.chunk_context > MAX_ALIGNMENT_CHUNK_SECONDS:
        raise ValueError(
            "chunk duration plus both context margins must be at most 180 seconds"
        )
    validated_final_outro_exemption_seconds(
        args.final_outro_exemption_seconds
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
    loaded_raw_asr_sha256: str | None = None
    replace_final_outro_option = False
    replace_reconciliation_evidence = False
    if mode in {"align-only", "complete"}:
        raw_sha256_before_read = sha256_file(output_path)
        loaded_raw_document = read_json_strict(output_path)
        loaded_options = (
            loaded_raw_document.get("options")
            if isinstance(loaded_raw_document, dict)
            else None
        )
        if args.realign and isinstance(loaded_options, dict):
            if "final_outro_exemption_seconds" in loaded_options:
                recorded_final_outro = validated_final_outro_exemption_seconds(
                    loaded_options["final_outro_exemption_seconds"]
                )
            else:
                recorded_final_outro = None
            if recorded_final_outro != args.final_outro_exemption_seconds:
                loaded_raw_document = {
                    **loaded_raw_document,
                    "options": {
                        **loaded_options,
                        "final_outro_exemption_seconds": (
                            args.final_outro_exemption_seconds
                        ),
                    },
                }
                replace_final_outro_option = True
        raw_document = validate_raw_document(
            loaded_raw_document,
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
        loaded_raw_asr_sha256 = sha256_file(output_path)
        if loaded_raw_asr_sha256 != raw_sha256_before_read:
            raise ValueError("raw ASR changed while it was being loaded")
        if (
            mode == "complete"
            and raw_document["boundary_reconciliation"]["status"] == "pending"
        ):
            mode = "align-only"
    if mode == "complete":
        raw_asr_sha256 = loaded_raw_asr_sha256
        if raw_asr_sha256 is None:
            raise AssertionError("complete ASR has no loaded raw identity")
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
            raw_document=raw_document,
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
        chunk_windows = list(
            audio_chunk_ranges(
                audio_duration_seconds,
                chunk_duration=args.chunk_duration,
                chunk_context=args.chunk_context,
            )
        )
        for chunk_id, window in enumerate(chunk_windows):
            if args.verbose:
                print(
                    f"transcribing chunk {chunk_id + 1} at "
                    f"{window.decode_start:.3f}s",
                    file=sys.stderr,
                    flush=True,
                )
            chunk_audio = decode_audio_chunk(
                input_path,
                start_seconds=window.decode_start,
                end_seconds=window.decode_end,
                ffmpeg=ffmpeg,
                numpy_module=np,
            )
            actual_end = min(
                audio_duration_seconds,
                window.decode_end,
                window.decode_start + len(chunk_audio) / SAMPLE_RATE,
            )
            maximum_decode_shortfall = (
                FINAL_AUDIO_DECODE_SHORTFALL_TOLERANCE_SECONDS
                if chunk_id == len(chunk_windows) - 1
                else AUDIO_DECODE_BOUNDARY_TOLERANCE_SECONDS
            )
            if window.decode_end - actual_end > maximum_decode_shortfall:
                raise ValueError(
                    "ffmpeg decoded an unexpectedly short audio chunk: "
                    f"requested_end={window.decode_end:.3f}, "
                    f"actual_end={actual_end:.3f}"
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
                    "start": rounded_seconds(window.ownership_start),
                    "end": rounded_seconds(window.ownership_end),
                    "decode_start": rounded_seconds(window.decode_start),
                    "decode_end": rounded_seconds(actual_end),
                    "decoded_text": text,
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
                "chunk_context_seconds": args.chunk_context,
                "boundary_reconciliation": BOUNDARY_RECONCILIATION_METHOD,
                "alignment_coverage_guard": ALIGNMENT_COVERAGE_GUARD,
                "aligned_gap_guard": ALIGNED_GAP_GUARD,
                **raw_options,
            },
            "performance": {
                "model_load_seconds": rounded_seconds(model_load_seconds),
                "transcription_seconds": rounded_seconds(transcription_seconds),
                "cuda_device_name": device_name,
                "cuda_total_memory_bytes": total_memory_bytes,
                "cuda_peak_memory_bytes": transcription_peak_memory_bytes,
            },
            "boundary_reconciliation": {
                "method": BOUNDARY_RECONCILIATION_METHOD,
                "status": "pending",
                "chunk_context_seconds": args.chunk_context,
                "seams": [],
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
        if args.retranscribe:
            aligned_output_path.unlink(missing_ok=True)
        write_json_atomically(output_path, raw_document)
        loaded_raw_asr_sha256 = sha256_file(output_path)
        del model
        clear_cuda(torch)
    else:
        recorded_duration = finite_document_number(
            raw_document["audio"].get("duration_seconds"), field="audio duration"
        )
        if abs(recorded_duration - audio_duration_seconds) > 0.01:
            raise ValueError("raw ASR duration does not match the decoded input audio")

    raw_chunks = raw_document["segments"]
    torch.cuda.reset_peak_memory_stats(device_index)
    aligner_load_started = time.perf_counter()
    aligner = Qwen3ForcedAligner.from_pretrained(
        aligner_load_target,
        **load_kwargs,
    )
    cuda_synchronize(torch, device_index)
    aligner_load_seconds = time.perf_counter() - aligner_load_started

    aligned_candidates: list[dict[str, Any]] = []
    alignment_started = time.perf_counter()
    for chunk in raw_chunks:
        decode_start = float(chunk["decode_start"])
        decode_end = float(chunk["decode_end"])
        decoded_text = str(chunk["decoded_text"]).strip()
        if not decoded_text:
            aligned_candidates.append(
                {
                    "chunk": chunk,
                    "ownership_start": float(chunk["start"]),
                    "ownership_end": float(chunk["end"]),
                    "decode_start": decode_start,
                    "decode_end": decode_end,
                    "alignment_seconds": 0.0,
                    "relative_alignment": [],
                    "alignment": [],
                }
            )
            continue
        if args.verbose:
            print(
                f"aligning chunk {int(chunk['id']) + 1} at {decode_start:.3f}s",
                file=sys.stderr,
                flush=True,
            )
        chunk_audio = decode_audio_chunk(
            input_path,
            start_seconds=decode_start,
            end_seconds=decode_end,
            ffmpeg=ffmpeg,
            numpy_module=np,
        )
        chunk_alignment_started = time.perf_counter()
        alignment_results = aligner.align(
            audio=(chunk_audio, SAMPLE_RATE),
            text=decoded_text,
            language=args.language,
        )
        if not isinstance(alignment_results, list) or len(alignment_results) != 1:
            raise ValueError("Qwen3-ForcedAligner returned an unexpected result count")
        aligned_items = validate_alignment_items(
            alignment_results[0], chunk_duration=decode_end - decode_start
        )
        chunk_alignment_seconds = time.perf_counter() - chunk_alignment_started
        absolute_alignment = [
            {
                "text": item["text"],
                "start": rounded_seconds(
                    decode_start + float(item["start_time"])
                ),
                "end": rounded_seconds(decode_start + float(item["end_time"])),
            }
            for item in aligned_items
        ]
        aligned_candidates.append(
            {
                "chunk": chunk,
                "ownership_start": float(chunk["start"]),
                "ownership_end": float(chunk["end"]),
                "decode_start": decode_start,
                "decode_end": decode_end,
                "alignment_seconds": rounded_seconds(chunk_alignment_seconds),
                "relative_alignment": aligned_items,
                "alignment": absolute_alignment,
            }
        )
        del alignment_results, aligned_items, absolute_alignment, chunk_audio
        clear_cuda(torch)
    cuda_synchronize(torch, device_index)
    alignment_seconds = time.perf_counter() - alignment_started
    alignment_peak_memory_bytes = cuda_peak_memory(torch, device_index)

    ownership_slices, seam_records = reconcile_candidate_slices(
        aligned_candidates
    )
    enforce_aligned_gap_silence(
        input_path=input_path,
        seam_records=seam_records,
        ffmpeg=ffmpeg,
        numpy_module=np,
    )
    reconciled_raw_chunks: list[dict[str, Any]] = []
    aligned_chunks: list[dict[str, Any]] = []
    for candidate, (start_item, stop_item) in zip(
        aligned_candidates, ownership_slices
    ):
        chunk = candidate["chunk"]
        relative_alignment = candidate["relative_alignment"]
        owned_relative_alignment = relative_alignment[start_item:stop_item]
        owned_text = text_for_alignment_slice(
            str(chunk["decoded_text"]),
            relative_alignment,
            start_item=start_item,
            stop_item=stop_item,
        )
        reconciled_chunk = {
            **chunk,
            "text": owned_text,
            "owned_item_start": start_item,
            "owned_item_stop": stop_item,
        }
        reconciled_raw_chunks.append(reconciled_chunk)
        aligned_chunks.append(
            {
                **reconciled_chunk,
                "alignment_seconds": candidate["alignment_seconds"],
                "alignment": candidate["alignment"][start_item:stop_item],
            }
        )

    enforce_alignment_coverage(
        input_path=input_path,
        chunks=aligned_chunks,
        ffmpeg=ffmpeg,
        numpy_module=np,
        final_outro_exemption_seconds=args.final_outro_exemption_seconds,
    )

    reconciled_text = join_transcript_chunks(
        [str(chunk["text"]) for chunk in reconciled_raw_chunks],
        language=args.language,
    )
    if not reconciled_text.strip():
        raise ValueError("boundary reconciliation returned an empty transcript")
    global_alignment: list[dict[str, Any]] = []
    global_source_chunk_ids: list[int] = []
    for chunk in aligned_chunks:
        source_chunk_id = int(chunk["id"])
        for item in chunk["alignment"]:
            global_alignment.append(
                {
                    "text": item["text"],
                    "start_time": item["start"],
                    "end_time": item["end"],
                }
            )
            global_source_chunk_ids.append(source_chunk_id)
    all_segments = transformers_sentence_segments(
        text=reconciled_text,
        aligned_items=global_alignment,
        offset_seconds=0.0,
        chunk_id=0,
        first_segment_id=0,
        max_characters=args.max_sentence_characters,
        item_source_chunk_ids=global_source_chunk_ids,
    )
    for chunk in aligned_chunks:
        chunk["sentence_segment_ids"] = [
            segment["id"]
            for segment in all_segments
            if segment["source_chunk_id"] == chunk["id"]
        ]
    reconciliation = {
        "method": BOUNDARY_RECONCILIATION_METHOD,
        "status": "complete",
        "chunk_context_seconds": args.chunk_context,
        "seams": seam_records,
    }
    reconciled_raw_document = {
        **raw_document,
        "boundary_reconciliation": reconciliation,
        "text": reconciled_text,
        "segments": reconciled_raw_chunks,
    }
    validate_raw_document(
        reconciled_raw_document,
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
        reconciled_raw_document,
        args=args,
        backend_options=raw_options,
    )
    if raw_document["boundary_reconciliation"]["status"] == "complete":
        if raw_document != reconciled_raw_document:
            previous_segments = raw_document.get("segments")
            changed_chunk_ids = [
                index
                for index, (previous, current) in enumerate(
                    zip(
                        previous_segments
                        if isinstance(previous_segments, list)
                        else [],
                        reconciled_raw_chunks,
                    )
                )
                if previous != current
            ]
            previous_reconciliation = raw_document.get("boundary_reconciliation")
            previous_seams = (
                previous_reconciliation.get("seams")
                if isinstance(previous_reconciliation, dict)
                else None
            )
            changed_seam_ids = [
                index
                for index, (previous, current) in enumerate(
                    zip(
                        previous_seams if isinstance(previous_seams, list) else [],
                        seam_records,
                    )
                )
                if previous != current
            ]
            previous_without_reconciliation = dict(raw_document)
            previous_without_reconciliation.pop("boundary_reconciliation", None)
            current_without_reconciliation = dict(reconciled_raw_document)
            current_without_reconciliation.pop("boundary_reconciliation", None)
            if (
                args.realign
                and previous_without_reconciliation
                == current_without_reconciliation
            ):
                replace_reconciliation_evidence = True
            else:
                raise ValueError(
                    "completed raw ASR does not reproduce its reconciliation: "
                    f"text_changed={raw_document.get('text') != reconciled_text}, "
                    f"changed_chunk_ids={changed_chunk_ids}, "
                    f"changed_seam_ids={changed_seam_ids}"
                )
        if (
            loaded_raw_asr_sha256 is None
            or sha256_file(output_path) != loaded_raw_asr_sha256
        ):
            raise ValueError("raw ASR changed while forced alignment was running")
        if replace_final_outro_option or replace_reconciliation_evidence:
            validate_file_identity(
                input_path,
                expected_size_bytes=audio_size_bytes,
                expected_sha256=audio_sha256,
                label="input audio",
            )
            write_json_atomically(output_path, reconciled_raw_document)
            raw_asr_sha256 = sha256_file(output_path)
        else:
            raw_asr_sha256 = loaded_raw_asr_sha256
    else:
        if (
            loaded_raw_asr_sha256 is None
            or not output_path.is_file()
            or sha256_file(output_path) != loaded_raw_asr_sha256
        ):
            raise ValueError("raw ASR changed while forced alignment was running")
        validate_file_identity(
            input_path,
            expected_size_bytes=audio_size_bytes,
            expected_sha256=audio_sha256,
            label="input audio",
        )
        write_json_atomically(output_path, reconciled_raw_document)
        raw_asr_sha256 = sha256_file(output_path)
    raw_document = reconciled_raw_document
    raw_chunks = reconciled_raw_chunks

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
        raw_document=raw_document,
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
