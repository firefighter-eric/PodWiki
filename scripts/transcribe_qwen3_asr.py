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
from typing import Any

from asr_lineage import (
    LINEAGE_SCHEMA_VERSION,
    build_model_identity,
    pinned_revision,
    require_requested_identity,
    validate_model_identity,
)


DEFAULT_MODEL = "mlx-community/Qwen3-ASR-1.7B-8bit"
DEFAULT_ALIGNER = "mlx-community/Qwen3-ForcedAligner-0.6B-8bit"
SAMPLE_RATE = 16_000
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SENTENCE_ENDINGS = frozenset("。！？!?.")
SOFT_ENDINGS = frozenset("，,；;：:")
MAX_SAFE_JSON_INTEGER = (1 << 53) - 1
MIN_AUDIO_DURATION_SECONDS = 0.001
MAX_AUDIO_DURATION_SECONDS = 359_999.999
MIN_CHUNK_DURATION_SECONDS = 1.0
MAX_CHUNK_DURATION_SECONDS = 300.0
MIN_AUDIO_SAMPLE_COUNT = math.ceil(MIN_AUDIO_DURATION_SECONDS * SAMPLE_RATE)
MAX_AUDIO_SAMPLE_COUNT = int(MAX_AUDIO_DURATION_SECONDS * SAMPLE_RATE)
MAX_PLANNED_CHUNK_COUNT = math.ceil(MAX_AUDIO_DURATION_SECONDS / MIN_CHUNK_DURATION_SECONDS)
LEGACY_RAW_CHUNK_BOUNDARY_TOLERANCE_SECONDS = 0.1
RAW_TIMESTAMP_ROUNDING_SECONDS = 0.001
RAW_FLOAT_COMPARISON_EPSILON_SECONDS = 1e-9
RAW_V2_CHUNK_BOUNDARY_TOLERANCE_SECONDS = (
    RAW_TIMESTAMP_ROUNDING_SECONDS + RAW_FLOAT_COMPARISON_EPSILON_SECONDS
)
# Existing tracked v2 artifacts contain at most two independent 1 ms rounding
# differences in either direction. Track gaps and overlaps separately so they
# cannot cancel each other while preserving those real artifacts.
RAW_V2_CUMULATIVE_BOUNDARY_TOLERANCE_SECONDS = (
    2 * RAW_TIMESTAMP_ROUNDING_SECONDS + RAW_FLOAT_COMPARISON_EPSILON_SECONDS
)
MLX_PER_CHUNK_TOKEN_BUDGET_SCOPE = "per-planned-chunk-v1"
MLX_LEGACY_ADAPTIVE_TOKEN_BUDGET_SCOPE = "adaptive-bisect-per-leaf-v1"
MLX_ADAPTIVE_TOKEN_BUDGET_SCOPE = "adaptive-bisect-per-leaf-v2"
MLX_ADAPTIVE_SPLIT_ALGORITHM = "adaptive-low-energy-bisect-v1"
MLX_ADAPTIVE_MIN_LEAF_SAMPLES = 20 * SAMPLE_RATE
MLX_LEGACY_ADAPTIVE_MAX_DEPTH = 3
MLX_ADAPTIVE_MAX_DEPTH = 4
MLX_ADAPTIVE_DEPTH_BY_SCOPE = {
    MLX_LEGACY_ADAPTIVE_TOKEN_BUDGET_SCOPE: MLX_LEGACY_ADAPTIVE_MAX_DEPTH,
    MLX_ADAPTIVE_TOKEN_BUDGET_SCOPE: MLX_ADAPTIVE_MAX_DEPTH,
}
MLX_ADAPTIVE_MAX_SPLIT_COUNT = 64
MLX_ADAPTIVE_ENERGY_WINDOW_SAMPLES = SAMPLE_RATE // 10
MLX_ADAPTIVE_QUANTIZATION = "pcm-s16-round-half-away-v1"
MLX_ADAPTIVE_TIE_BREAK = "energy-center-left-v1"
MAX_MLX_LEAF_CHUNK_COUNT = MAX_PLANNED_CHUNK_COUNT + MLX_ADAPTIVE_MAX_SPLIT_COUNT


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=("Run Qwen3-ASR and Qwen3-ForcedAligner locally through MLX Audio.")
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
        "--model-revision",
        help="Pinned full Hugging Face model commit; defaults to the project pin",
    )
    parser.add_argument(
        "--model-path",
        type=Path,
        help="Optional local model directory; artifact metadata still uses --model",
    )
    parser.add_argument("--aligner", default=DEFAULT_ALIGNER)
    parser.add_argument(
        "--aligner-revision",
        help="Pinned full Hugging Face aligner commit; defaults to the project pin",
    )
    parser.add_argument(
        "--aligner-path",
        type=Path,
        help="Optional local aligner directory; artifact metadata still uses --aligner",
    )
    parser.add_argument("--language", default="Chinese")
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=4096,
        help=(
            "Generation token budget applied independently to each exact MLX "
            "silence-aware chunk or adaptive retry leaf"
        ),
    )
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


def effective_total_token_budget(
    *,
    per_chunk_budget: int,
    planned_chunk_count: int,
) -> int:
    """Expand the per-chunk CLI budget for MLX Audio's planned chunks."""
    bounded_document_integer(
        per_chunk_budget,
        field="per-chunk token budget",
        minimum=1,
        maximum=MAX_SAFE_JSON_INTEGER,
    )
    bounded_document_integer(
        planned_chunk_count,
        field="planned chunk count",
        minimum=1,
        maximum=MAX_MLX_LEAF_CHUNK_COUNT,
    )
    total_token_budget = per_chunk_budget * planned_chunk_count
    if total_token_budget > MAX_SAFE_JSON_INTEGER:
        raise ValueError("effective total token budget exceeds the JSON safe-integer limit")
    return total_token_budget


def plan_mlx_generation(
    audio_array: Any,
    *,
    sample_rate: int,
    chunk_duration_seconds: float,
    per_chunk_budget: int,
    split_audio_into_chunks: Any,
) -> tuple[list[tuple[Any, float]], int]:
    """Return MLX Audio's exact split plan and its aggregate audit budget.

    MLX Audio may move a nominal boundary up to five seconds earlier while
    looking for silence. That can produce more chunks than
    ``ceil(duration / chunk_duration)``. The returned chunks are reused as the
    public ``model.generate`` inputs, so the full decoded array is split only
    once. Each planned chunk receives its own token budget; the aggregate is
    retained solely as auditable raw metadata and a legacy-compatible guard.
    """
    if type(sample_rate) is not int or sample_rate != SAMPLE_RATE:
        raise ValueError(f"MLX planning sample rate must equal {SAMPLE_RATE}")
    finite_document_number(
        chunk_duration_seconds,
        field="requested chunk duration",
        minimum=MIN_CHUNK_DURATION_SECONDS,
        maximum=MAX_CHUNK_DURATION_SECONDS,
        maximum_exclusive=True,
    )
    bounded_document_integer(
        per_chunk_budget,
        field="per-chunk token budget",
        minimum=1,
        maximum=MAX_SAFE_JSON_INTEGER,
    )
    bounded_document_integer(
        len(audio_array),
        field="decoded audio sample count",
        minimum=MIN_AUDIO_SAMPLE_COUNT,
        maximum=MAX_AUDIO_SAMPLE_COUNT,
    )
    chunks = split_audio_into_chunks(
        audio_array,
        sr=sample_rate,
        chunk_duration=chunk_duration_seconds,
    )
    planned_chunk_count = len(chunks)
    total_token_budget = effective_total_token_budget(
        per_chunk_budget=per_chunk_budget,
        planned_chunk_count=planned_chunk_count,
    )
    return chunks, total_token_budget


def quantize_pcm_s16(audio: Any) -> Any:
    """Return deterministic PCM-s16 samples for adaptive energy decisions."""

    import numpy as np

    samples = np.asarray(audio)
    if samples.ndim != 1 or not np.all(np.isfinite(samples)):
        raise ValueError("adaptive MLX split input must be finite mono PCM")
    clipped = np.clip(samples.astype(np.float64, copy=False), -1.0, 1.0)
    magnitude = np.floor(np.abs(clipped) * 32768.0 + 0.5)
    signed = np.where(np.signbit(clipped), -magnitude, magnitude)
    return np.clip(signed, -32768, 32767).astype(np.int16)


def select_adaptive_split_sample(
    pcm_s16: Any,
    *,
    parent_start_sample: int,
    parent_end_sample: int,
) -> tuple[int, int]:
    """Choose the lowest-energy legal split, then center-most and left-most."""

    import numpy as np

    parent_sample_count = parent_end_sample - parent_start_sample
    if len(pcm_s16) != parent_sample_count:
        raise ValueError("adaptive MLX split PCM does not match its source ownership")
    legal_lo = MLX_ADAPTIVE_MIN_LEAF_SAMPLES
    legal_hi = parent_sample_count - MLX_ADAPTIVE_MIN_LEAF_SAMPLES
    if legal_lo > legal_hi:
        raise ValueError("exhausted MLX chunk cannot preserve the 20-second leaf minimum")

    half_window = MLX_ADAPTIVE_ENERGY_WINDOW_SAMPLES // 2
    int64_samples = np.asarray(pcm_s16, dtype=np.int64)
    squared = int64_samples * int64_samples
    prefix = np.empty(parent_sample_count + 1, dtype=np.int64)
    prefix[0] = 0
    np.cumsum(squared, dtype=np.int64, out=prefix[1:])
    energies = (
        prefix[legal_lo + half_window : legal_hi + half_window + 1]
        - prefix[legal_lo - half_window : legal_hi - half_window + 1]
    )
    minimum_energy = int(energies.min())
    equal_centers = np.flatnonzero(energies == minimum_energy) + legal_lo
    # Integer distance avoids a floating midpoint for odd-sized parents.
    distances = np.abs(2 * equal_centers - parent_sample_count)
    chosen_local_sample = int(equal_centers[int(np.argmin(distances))])
    return parent_start_sample + chosen_local_sample, minimum_energy


def generate_mlx_planned_chunks(
    model: Any,
    planned_chunks: list[tuple[Any, float]],
    *,
    audio_sample_count: int,
    sample_rate: int,
    per_chunk_budget: int,
    temperature: float,
    language: str,
    verbose: bool,
    clear_cache: Any,
    quantize_pcm: Any | None = None,
) -> dict[str, Any]:
    """Generate each planned chunk with bounded adaptive leaf retries.

    ``mlx-audio==0.4.7`` treats ``max_tokens`` as one shared remaining-token
    counter inside a single ``generate`` call. Calling it once per already
    planned chunk prevents an anomalous chunk from consuming later chunks'
    budgets. A legal result that consumes the complete per-call budget is
    discarded and retried as two low-energy leaves. The fixed 20-second leaf
    minimum and depth/split caps keep that recovery bounded and fail closed.
    """

    if type(sample_rate) is not int or sample_rate != SAMPLE_RATE:
        raise ValueError(f"MLX generation sample rate must equal {SAMPLE_RATE}")
    bounded_document_integer(
        audio_sample_count,
        field="decoded audio sample count",
        minimum=MIN_AUDIO_SAMPLE_COUNT,
        maximum=MAX_AUDIO_SAMPLE_COUNT,
    )
    bounded_document_integer(
        per_chunk_budget,
        field="per-chunk token budget",
        minimum=1,
        maximum=MAX_SAFE_JSON_INTEGER,
    )
    bounded_document_integer(
        len(planned_chunks),
        field="planned chunk count",
        minimum=1,
        maximum=MAX_PLANNED_CHUNK_COUNT,
    )
    if (
        isinstance(temperature, bool)
        or not isinstance(temperature, (int, float))
        or temperature != 0.0
    ):
        raise ValueError("adaptive MLX generation requires temperature=0.0")
    if quantize_pcm is None:
        quantize_pcm = quantize_pcm_s16

    normalized_plan: list[tuple[Any, int, int]] = []
    start_samples: list[int] = []
    for index, planned_chunk in enumerate(planned_chunks):
        if not isinstance(planned_chunk, (tuple, list)) or len(planned_chunk) != 2:
            raise ValueError(f"MLX split plan chunk {index} is invalid")
        chunk_audio, offset_seconds = planned_chunk
        offset = finite_document_number(
            offset_seconds,
            field=f"split plan chunk {index} offset",
            minimum=0.0,
            maximum=audio_sample_count / sample_rate,
        )
        start_sample = round(offset * sample_rate)
        if not math.isclose(
            offset,
            start_sample / sample_rate,
            rel_tol=0.0,
            abs_tol=RAW_FLOAT_COMPARISON_EPSILON_SECONDS,
        ):
            raise ValueError(f"MLX split plan chunk {index} offset is not sample-aligned")
        if (index == 0 and start_sample != 0) or (index > 0 and start_sample <= start_samples[-1]):
            raise ValueError("MLX split plan does not continuously cover from zero")
        try:
            chunk_sample_count = len(chunk_audio)
        except (OverflowError, TypeError) as error:
            raise ValueError(f"MLX split plan chunk {index} has invalid audio") from error
        bounded_document_integer(
            chunk_sample_count,
            field=f"split plan chunk {index} sample count",
            minimum=MIN_AUDIO_SAMPLE_COUNT,
            maximum=MAX_AUDIO_SAMPLE_COUNT,
        )
        start_samples.append(start_sample)
        normalized_plan.append((chunk_audio, start_sample, chunk_sample_count))

    # Validate every dependency-produced boundary before starting any expensive
    # model generation. A malformed later chunk must not waste earlier decode.
    for index, (_, start_sample, chunk_sample_count) in enumerate(normalized_plan):
        end_sample = (
            normalized_plan[index + 1][1]
            if index + 1 < len(normalized_plan)
            else audio_sample_count
        )
        expected_source_samples = end_sample - start_sample
        expected_planned_samples = (
            max(expected_source_samples, sample_rate)
            if index + 1 == len(normalized_plan)
            else expected_source_samples
        )
        if expected_source_samples <= 0 or chunk_sample_count != expected_planned_samples:
            raise ValueError(
                f"MLX split plan chunk {index} sample count does not match its offsets"
            )

    initial_boundaries = start_samples + [audio_sample_count]
    raw_chunks: list[dict[str, Any]] = []
    texts: list[str] = []
    split_events: list[dict[str, Any]] = []
    total_prompt_tokens = 0
    total_generation_tokens = 0
    attempt_prompt_tokens = 0
    attempt_generation_tokens = 0
    generation_call_count = 0
    pcm_s16le_hasher = hashlib.sha256()

    def add_bounded_total(current: int, value: int, *, field: str) -> int:
        if current > MAX_SAFE_JSON_INTEGER - value:
            raise ValueError(f"aggregate {field} exceeds JSON safe integer")
        return current + value

    def generate_node(
        node_audio: Any,
        *,
        initial_chunk_id: int,
        split_path: str,
        depth: int,
        start_sample: int,
        end_sample: int,
        pcm_s16: Any | None = None,
    ) -> None:
        nonlocal attempt_generation_tokens
        nonlocal attempt_prompt_tokens
        nonlocal generation_call_count
        nonlocal total_generation_tokens
        nonlocal total_prompt_tokens

        node_sample_count = len(node_audio)
        nested_chunk_duration = (node_sample_count + 1) / sample_rate
        try:
            result = model.generate(
                node_audio,
                max_tokens=per_chunk_budget,
                temperature=temperature,
                language=language,
                chunk_duration=nested_chunk_duration,
                verbose=verbose,
            )
        finally:
            clear_cache()
        generation_call_count += 1
        label = f"{initial_chunk_id}:{split_path or 'root'}"
        if not isinstance(getattr(result, "text", None), str) or not isinstance(
            getattr(result, "segments", None), list
        ):
            raise ValueError(f"Qwen3-ASR chunk {label} returned an unexpected result")
        if len(result.segments) != 1:
            raise ValueError(f"Qwen3-ASR chunk {label} did not return exactly one segment")
        nested_segment = result.segments[0]
        if (
            not isinstance(nested_segment, dict)
            or not isinstance(nested_segment.get("text"), str)
            or nested_segment["text"] != result.text
        ):
            raise ValueError(f"Qwen3-ASR chunk {label} returned inconsistent segment text")
        nested_start = finite_document_number(
            nested_segment.get("start"),
            field=f"generated chunk {label} start",
        )
        nested_end = finite_document_number(
            nested_segment.get("end"),
            field=f"generated chunk {label} end",
        )
        if not math.isclose(
            nested_start,
            0.0,
            rel_tol=0.0,
            abs_tol=RAW_V2_CHUNK_BOUNDARY_TOLERANCE_SECONDS,
        ) or not math.isclose(
            nested_end,
            node_sample_count / sample_rate,
            rel_tol=0.0,
            abs_tol=RAW_V2_CHUNK_BOUNDARY_TOLERANCE_SECONDS,
        ):
            raise ValueError(f"Qwen3-ASR chunk {label} did not cover its planned audio")

        prompt_tokens = bounded_document_integer(
            getattr(result, "prompt_tokens", None),
            field=f"chunk {label} prompt token accounting",
            minimum=0,
            maximum=MAX_SAFE_JSON_INTEGER,
        )
        generation_tokens = bounded_document_integer(
            getattr(result, "generation_tokens", None),
            field=f"chunk {label} generation token accounting",
            minimum=0,
            maximum=per_chunk_budget,
        )
        attempt_prompt_tokens = add_bounded_total(
            attempt_prompt_tokens, prompt_tokens, field="attempt prompt token accounting"
        )
        attempt_generation_tokens = add_bounded_total(
            attempt_generation_tokens,
            generation_tokens,
            field="attempt generation token accounting",
        )

        if generation_tokens == per_chunk_budget:
            if depth >= MLX_ADAPTIVE_MAX_DEPTH:
                raise ValueError(f"Qwen3-ASR chunk {label} exhausted the adaptive depth limit")
            if len(split_events) >= MLX_ADAPTIVE_MAX_SPLIT_COUNT:
                raise ValueError("Qwen3-ASR exhausted the adaptive split-count limit")
            source_sample_count = end_sample - start_sample
            if source_sample_count < 2 * MLX_ADAPTIVE_MIN_LEAF_SAMPLES:
                raise ValueError(
                    f"Qwen3-ASR chunk {label} exhausted its budget below the adaptive leaf minimum"
                )
            source_audio = node_audio[:source_sample_count]
            if pcm_s16 is None:
                pcm_s16 = quantize_pcm(source_audio)
            split_sample, split_energy = select_adaptive_split_sample(
                pcm_s16,
                parent_start_sample=start_sample,
                parent_end_sample=end_sample,
            )
            local_split = split_sample - start_sample
            split_events.append(
                {
                    "initial_chunk_id": initial_chunk_id,
                    "split_path": split_path,
                    "depth": depth,
                    "parent_start_sample": start_sample,
                    "parent_end_sample": end_sample,
                    "legal_start_sample": start_sample + MLX_ADAPTIVE_MIN_LEAF_SAMPLES,
                    "legal_end_sample": end_sample - MLX_ADAPTIVE_MIN_LEAF_SAMPLES,
                    "split_sample": split_sample,
                    "cut_energy_sum_squares": split_energy,
                    "parent_prompt_tokens": prompt_tokens,
                    "parent_generation_tokens": generation_tokens,
                }
            )
            generate_node(
                source_audio[:local_split],
                initial_chunk_id=initial_chunk_id,
                split_path=f"{split_path}L",
                depth=depth + 1,
                start_sample=start_sample,
                end_sample=split_sample,
                pcm_s16=pcm_s16[:local_split],
            )
            generate_node(
                source_audio[local_split:],
                initial_chunk_id=initial_chunk_id,
                split_path=f"{split_path}R",
                depth=depth + 1,
                start_sample=split_sample,
                end_sample=end_sample,
                pcm_s16=pcm_s16[local_split:],
            )
            return

        total_prompt_tokens = add_bounded_total(
            total_prompt_tokens, prompt_tokens, field="prompt token accounting"
        )
        total_generation_tokens = add_bounded_total(
            total_generation_tokens,
            generation_tokens,
            field="generation token accounting",
        )
        texts.append(result.text)
        raw_chunks.append(
            {
                "id": len(raw_chunks),
                "initial_chunk_id": initial_chunk_id,
                "split_path": split_path,
                "start_sample": start_sample,
                "end_sample": end_sample,
                # Preserve sample-derived ownership boundaries. Rounding a
                # final 1-sample tail to milliseconds can collapse start=end.
                "start": start_sample / sample_rate,
                "end": end_sample / sample_rate,
                "text": result.text,
                "generation_tokens": generation_tokens,
            }
        )

    for index, (chunk_audio, start_sample, _) in enumerate(normalized_plan):
        source_sample_count = initial_boundaries[index + 1] - start_sample
        pcm_s16 = quantize_pcm(chunk_audio[:source_sample_count])
        if len(pcm_s16) != source_sample_count:
            raise ValueError("canonical PCM-s16 does not match its source ownership")
        # Explicit little-endian bytes make the commitment independent of the
        # worker host byte order. Quantization is bounded to one initial chunk.
        pcm_s16le_hasher.update(pcm_s16.astype("<i2", copy=False).tobytes(order="C"))
        generate_node(
            chunk_audio,
            initial_chunk_id=index,
            split_path="",
            depth=0,
            start_sample=start_sample,
            end_sample=initial_boundaries[index + 1],
            pcm_s16=pcm_s16,
        )

    return {
        "text": " ".join(texts),
        "segments": raw_chunks,
        "prompt_tokens": total_prompt_tokens,
        "generation_tokens": total_generation_tokens,
        "attempt_prompt_tokens": attempt_prompt_tokens,
        "attempt_generation_tokens": attempt_generation_tokens,
        "generation_call_count": generation_call_count,
        "initial_chunk_count": len(normalized_plan),
        "final_leaf_chunk_count": len(raw_chunks),
        "adaptive_split_count": len(split_events),
        "pcm_s16le_sha256": pcm_s16le_hasher.hexdigest(),
        "generation_plan": {
            "schema_version": 1,
            "pcm_s16le_sha256": pcm_s16le_hasher.hexdigest(),
            "initial_chunk_boundaries_samples": initial_boundaries,
            "split_events": split_events,
        },
    }


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


def finite_document_number(
    value: Any,
    *,
    field: str,
    minimum: float | None = None,
    maximum: float | None = None,
    maximum_exclusive: bool = False,
) -> float:
    """Return a bounded JSON number without leaking conversion overflows."""

    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"raw ASR has invalid {field}; expected a finite number")
    try:
        number = float(value)
    except (OverflowError, TypeError, ValueError) as error:
        raise ValueError(f"raw ASR has invalid {field}; expected a finite number") from error
    if not math.isfinite(number):
        raise ValueError(f"raw ASR has invalid {field}; expected a finite number")
    if minimum is not None and number < minimum:
        raise ValueError(f"raw ASR has invalid {field}; expected a value >= {minimum}")
    if maximum is not None and (number >= maximum if maximum_exclusive else number > maximum):
        comparison = "<" if maximum_exclusive else "<="
        raise ValueError(f"raw ASR has invalid {field}; expected a value {comparison} {maximum}")
    return number


def bounded_document_integer(
    value: Any,
    *,
    field: str,
    minimum: int,
    maximum: int,
) -> int:
    """Return a bounded JSON integer, rejecting booleans and arbitrary bignums."""

    if type(value) is not int or not minimum <= value <= maximum:
        raise ValueError(
            f"raw ASR has invalid {field}; expected an integer in [{minimum}, {maximum}]"
        )
    return value


def validate_adaptive_generation_plan_document(
    document: dict[str, Any],
    *,
    segments: list[Any],
    sample_count: int,
    max_tokens: int,
    initial_chunk_count: int,
    generation_tokens: int,
    expected_pcm_s16le_sha256: str | None = None,
) -> int:
    """Validate and replay an adaptive MLX split tree from untrusted JSON."""

    options = document["options"]
    performance = document["performance"]
    adaptive_scope = options.get("token_budget_scope")
    adaptive_max_depth = MLX_ADAPTIVE_DEPTH_BY_SCOPE.get(adaptive_scope)
    if adaptive_max_depth is None:
        raise ValueError("raw ASR has an unsupported adaptive token budget scope")
    expected_options = {
        "adaptive_split_algorithm": MLX_ADAPTIVE_SPLIT_ALGORITHM,
        "adaptive_min_leaf_samples": MLX_ADAPTIVE_MIN_LEAF_SAMPLES,
        "adaptive_max_depth": adaptive_max_depth,
        "adaptive_max_split_count": MLX_ADAPTIVE_MAX_SPLIT_COUNT,
        "adaptive_energy_window_samples": MLX_ADAPTIVE_ENERGY_WINDOW_SAMPLES,
        "adaptive_quantization": MLX_ADAPTIVE_QUANTIZATION,
        "adaptive_tie_break": MLX_ADAPTIVE_TIE_BREAK,
    }
    for field, expected in expected_options.items():
        if options.get(field) != expected:
            raise ValueError(f"raw ASR adaptive option {field} mismatch")
    final_leaf_count = bounded_document_integer(
        options.get("final_leaf_chunk_count"),
        field="final adaptive leaf chunk count",
        minimum=1,
        maximum=MAX_MLX_LEAF_CHUNK_COUNT,
    )
    split_count = bounded_document_integer(
        options.get("adaptive_split_count"),
        field="adaptive split count",
        minimum=0,
        maximum=MLX_ADAPTIVE_MAX_SPLIT_COUNT,
    )
    if final_leaf_count != len(segments) or final_leaf_count != initial_chunk_count + split_count:
        raise ValueError("raw ASR adaptive initial/final/split chunk counts are inconsistent")

    plan = document.get("generation_plan")
    if not isinstance(plan, dict) or set(plan) != {
        "schema_version",
        "pcm_s16le_sha256",
        "initial_chunk_boundaries_samples",
        "split_events",
    }:
        raise ValueError("raw ASR has an invalid adaptive generation plan")
    if type(plan.get("schema_version")) is not int or plan.get("schema_version") != 1:
        raise ValueError("raw ASR has an unsupported adaptive generation plan schema")
    pcm_s16le_sha256 = plan.get("pcm_s16le_sha256")
    if (
        not isinstance(pcm_s16le_sha256, str)
        or len(pcm_s16le_sha256) != 64
        or any(character not in "0123456789abcdef" for character in pcm_s16le_sha256)
    ):
        raise ValueError("raw ASR adaptive PCM commitment is not a lowercase SHA-256")
    if expected_pcm_s16le_sha256 is not None and pcm_s16le_sha256 != expected_pcm_s16le_sha256:
        raise ValueError("raw ASR adaptive PCM commitment does not match generated PCM")
    boundaries = plan.get("initial_chunk_boundaries_samples")
    if not isinstance(boundaries, list) or len(boundaries) != initial_chunk_count + 1:
        raise ValueError("raw ASR adaptive initial boundaries do not match planned chunks")
    validated_boundaries = [
        bounded_document_integer(
            boundary,
            field=f"adaptive initial boundary {index}",
            minimum=0,
            maximum=sample_count,
        )
        for index, boundary in enumerate(boundaries)
    ]
    if (
        validated_boundaries[0] != 0
        or validated_boundaries[-1] != sample_count
        or any(right <= left for left, right in zip(validated_boundaries, validated_boundaries[1:]))
    ):
        raise ValueError("raw ASR adaptive initial boundaries do not continuously cover the audio")

    split_events = plan.get("split_events")
    if not isinstance(split_events, list) or len(split_events) != split_count:
        raise ValueError("raw ASR adaptive split events do not match adaptive_split_count")
    active_nodes: dict[tuple[int, str], tuple[int, int]] = {
        (index, ""): (validated_boundaries[index], validated_boundaries[index + 1])
        for index in range(initial_chunk_count)
    }
    event_fields = {
        "initial_chunk_id",
        "split_path",
        "depth",
        "parent_start_sample",
        "parent_end_sample",
        "legal_start_sample",
        "legal_end_sample",
        "split_sample",
        "cut_energy_sum_squares",
        "parent_prompt_tokens",
        "parent_generation_tokens",
    }
    maximum_window_energy = MLX_ADAPTIVE_ENERGY_WINDOW_SAMPLES * 32768**2
    discarded_prompt_tokens = 0
    for index, event in enumerate(split_events):
        if not isinstance(event, dict) or set(event) != event_fields:
            raise ValueError(f"raw ASR adaptive split event {index} is invalid")
        initial_chunk_id = bounded_document_integer(
            event.get("initial_chunk_id"),
            field=f"adaptive split event {index} initial chunk id",
            minimum=0,
            maximum=initial_chunk_count - 1,
        )
        split_path = event.get("split_path")
        if (
            not isinstance(split_path, str)
            or len(split_path) >= adaptive_max_depth
            or any(step not in "LR" for step in split_path)
        ):
            raise ValueError(f"raw ASR adaptive split event {index} has an invalid path")
        depth = bounded_document_integer(
            event.get("depth"),
            field=f"adaptive split event {index} depth",
            minimum=0,
            maximum=adaptive_max_depth - 1,
        )
        if depth != len(split_path):
            raise ValueError(f"raw ASR adaptive split event {index} depth does not match its path")
        key = (initial_chunk_id, split_path)
        if key not in active_nodes:
            raise ValueError(f"raw ASR adaptive split event {index} does not name an active node")
        parent_start, parent_end = active_nodes[key]
        legal_start = parent_start + MLX_ADAPTIVE_MIN_LEAF_SAMPLES
        legal_end = parent_end - MLX_ADAPTIVE_MIN_LEAF_SAMPLES
        if legal_start > legal_end:
            raise ValueError(f"raw ASR adaptive split event {index} violates the leaf minimum")
        expected_event_values = {
            "parent_start_sample": parent_start,
            "parent_end_sample": parent_end,
            "legal_start_sample": legal_start,
            "legal_end_sample": legal_end,
            "parent_generation_tokens": max_tokens,
        }
        for field, expected in expected_event_values.items():
            if event.get(field) != expected or type(event.get(field)) is not int:
                raise ValueError(f"raw ASR adaptive split event {index} has invalid {field}")
        split_sample = bounded_document_integer(
            event.get("split_sample"),
            field=f"adaptive split event {index} split sample",
            minimum=legal_start,
            maximum=legal_end,
        )
        bounded_document_integer(
            event.get("cut_energy_sum_squares"),
            field=f"adaptive split event {index} cut energy",
            minimum=0,
            maximum=maximum_window_energy,
        )
        parent_prompt_tokens = bounded_document_integer(
            event.get("parent_prompt_tokens"),
            field=f"adaptive split event {index} parent prompt tokens",
            minimum=0,
            maximum=MAX_SAFE_JSON_INTEGER,
        )
        if discarded_prompt_tokens > MAX_SAFE_JSON_INTEGER - parent_prompt_tokens:
            raise ValueError("raw ASR adaptive parent prompt token sum exceeds JSON safe integer")
        discarded_prompt_tokens += parent_prompt_tokens
        del active_nodes[key]
        active_nodes[(initial_chunk_id, f"{split_path}L")] = (parent_start, split_sample)
        active_nodes[(initial_chunk_id, f"{split_path}R")] = (split_sample, parent_end)

    ordered_leaves = sorted(
        (
            (start, end, initial_chunk_id, split_path)
            for (initial_chunk_id, split_path), (start, end) in active_nodes.items()
        ),
        key=lambda leaf: (leaf[0], leaf[1]),
    )
    if len(ordered_leaves) != final_leaf_count:
        raise ValueError("raw ASR adaptive split tree has an invalid final leaf count")
    segment_fields = {
        "id",
        "initial_chunk_id",
        "split_path",
        "start_sample",
        "end_sample",
        "start",
        "end",
        "text",
        "generation_tokens",
    }
    for index, (segment, leaf) in enumerate(zip(segments, ordered_leaves)):
        if not isinstance(segment, dict) or set(segment) != segment_fields:
            raise ValueError(f"raw ASR adaptive segment {index} has invalid fields")
        start, end, initial_chunk_id, split_path = leaf
        expected_values = {
            "initial_chunk_id": initial_chunk_id,
            "split_path": split_path,
            "start_sample": start,
            "end_sample": end,
        }
        for field, expected in expected_values.items():
            if segment.get(field) != expected or type(segment.get(field)) is not type(expected):
                raise ValueError(f"raw ASR adaptive segment {index} has invalid {field}")
        if not math.isclose(
            finite_document_number(segment.get("start"), field=f"segment {index} start"),
            start / SAMPLE_RATE,
            rel_tol=0.0,
            abs_tol=RAW_FLOAT_COMPARISON_EPSILON_SECONDS,
        ) or not math.isclose(
            finite_document_number(segment.get("end"), field=f"segment {index} end"),
            end / SAMPLE_RATE,
            rel_tol=0.0,
            abs_tol=RAW_FLOAT_COMPARISON_EPSILON_SECONDS,
        ):
            raise ValueError(f"raw ASR adaptive segment {index} seconds do not match samples")

    prompt_tokens = bounded_document_integer(
        performance.get("prompt_tokens"),
        field="prompt token accounting",
        minimum=0,
        maximum=MAX_SAFE_JSON_INTEGER,
    )
    attempt_prompt_tokens = bounded_document_integer(
        performance.get("attempt_prompt_tokens"),
        field="attempt prompt token accounting",
        minimum=0,
        maximum=MAX_SAFE_JSON_INTEGER,
    )
    if attempt_prompt_tokens != prompt_tokens + discarded_prompt_tokens:
        raise ValueError("raw ASR adaptive attempt prompt tokens are inconsistent")
    attempt_generation_tokens = bounded_document_integer(
        performance.get("attempt_generation_tokens"),
        field="attempt generation token accounting",
        minimum=0,
        maximum=MAX_SAFE_JSON_INTEGER,
    )
    if attempt_generation_tokens != generation_tokens + split_count * max_tokens:
        raise ValueError("raw ASR adaptive attempt generation tokens are inconsistent")
    generation_call_count = bounded_document_integer(
        performance.get("generation_call_count"),
        field="generation call count",
        minimum=1,
        maximum=MAX_PLANNED_CHUNK_COUNT + 2 * MLX_ADAPTIVE_MAX_SPLIT_COUNT,
    )
    if generation_call_count != initial_chunk_count + 2 * split_count:
        raise ValueError("raw ASR adaptive generation call count is inconsistent")
    return final_leaf_count


def validate_raw_document(
    document: Any,
    *,
    engine: str = "mlx-audio",
    model: str,
    language: str,
    temperature: float,
    max_tokens: int,
    chunk_duration: float,
    audio_size_bytes: int,
    audio_sha256: str,
    backend_options: dict[str, Any] | None = None,
    model_identity: dict[str, Any] | None = None,
    adaptive_pcm_s16le_sha256: str | None = None,
) -> dict[str, Any]:
    mlx_backend = engine == "mlx-audio"
    if mlx_backend:
        bounded_document_integer(
            max_tokens,
            field="requested max tokens",
            minimum=1,
            maximum=MAX_SAFE_JSON_INTEGER,
        )
        validated_chunk_duration = finite_document_number(
            chunk_duration,
            field="requested chunk duration",
            minimum=MIN_CHUNK_DURATION_SECONDS,
            maximum=MAX_CHUNK_DURATION_SECONDS,
            maximum_exclusive=True,
        )
    else:
        validated_chunk_duration = chunk_duration
    if not isinstance(document, dict) or document.get("schema_version") != 1:
        raise ValueError("raw ASR artifact must contain a JSON object")
    expected_values: dict[str, Any] = {
        "kind": "raw-asr",
        "engine": engine,
        "model": model,
        "language": language,
    }
    for field, expected in expected_values.items():
        if document.get(field) != expected:
            raise ValueError(
                f"raw ASR {field} mismatch: expected={expected!r}, actual={document.get(field)!r}"
            )

    lineage_version = document.get("lineage_schema_version")
    if lineage_version is not None:
        if type(lineage_version) is not int or lineage_version != LINEAGE_SCHEMA_VERSION:
            raise ValueError("raw ASR has an unsupported lineage schema version")
        recorded_identity = validate_model_identity(document.get("model_identity"), label="raw ASR")
        if model_identity is not None and recorded_identity != model_identity:
            raise ValueError("raw ASR model identity does not match the pinned local model")

    audio = document.get("audio")
    if not isinstance(audio, dict):
        raise ValueError("raw ASR has no audio identity")
    if audio.get("size_bytes") != audio_size_bytes:
        raise ValueError("raw ASR audio size does not match the current input")
    if audio.get("sha256") != audio_sha256:
        raise ValueError("raw ASR audio SHA-256 does not match the current input")
    duration_seconds = (
        finite_document_number(
            audio.get("duration_seconds"),
            field="audio duration",
            minimum=MIN_AUDIO_DURATION_SECONDS,
            maximum=MAX_AUDIO_DURATION_SECONDS,
        )
        if mlx_backend
        else finite_document_number(audio.get("duration_seconds"), field="audio duration")
    )

    options = document.get("options")
    if not isinstance(options, dict):
        raise ValueError("raw ASR has no decoding options")
    expected_options: dict[str, Any] = {
        "temperature": temperature,
        "max_tokens_per_chunk": max_tokens,
        "chunk_duration_seconds": validated_chunk_duration,
    }
    if backend_options is not None:
        expected_options.update(backend_options)
    for field, expected in expected_options.items():
        if options.get(field) != expected:
            raise ValueError(
                f"raw ASR option {field} mismatch: expected={expected!r}, "
                f"actual={options.get(field)!r}"
            )

    performance = document.get("performance")
    generation_tokens: int | None = None
    if mlx_backend and (performance is not None or lineage_version == LINEAGE_SCHEMA_VERSION):
        if not isinstance(performance, dict):
            raise ValueError("raw ASR has invalid performance data")
        recorded_generation_tokens = performance.get("generation_tokens")
        generation_tokens = bounded_document_integer(
            recorded_generation_tokens,
            field="generation token accounting",
            minimum=0,
            maximum=MAX_SAFE_JSON_INTEGER,
        )

    text = document.get("text")
    segments = document.get("segments")
    if not isinstance(text, str) or not text.strip():
        raise ValueError("raw ASR has no transcript text")
    if not isinstance(segments, list) or not segments:
        raise ValueError("raw ASR has no segments")
    previous_start = -1.0
    previous_end = 0.0
    v2_mlx_backend = mlx_backend and lineage_version == LINEAGE_SCHEMA_VERSION
    boundary_tolerance = (
        RAW_V2_CHUNK_BOUNDARY_TOLERANCE_SECONDS
        if v2_mlx_backend
        else LEGACY_RAW_CHUNK_BOUNDARY_TOLERANCE_SECONDS
    )
    cumulative_gap_seconds = 0.0
    cumulative_overlap_seconds = 0.0
    token_budget_scope_recorded = "token_budget_scope" in options
    token_budget_scope = options.get("token_budget_scope")
    per_chunk_token_budget = False
    adaptive_token_budget = False
    if token_budget_scope_recorded:
        if token_budget_scope not in {
            MLX_PER_CHUNK_TOKEN_BUDGET_SCOPE,
            MLX_LEGACY_ADAPTIVE_TOKEN_BUDGET_SCOPE,
            MLX_ADAPTIVE_TOKEN_BUDGET_SCOPE,
        }:
            raise ValueError("raw ASR has an unsupported MLX token budget scope")
        if lineage_version != LINEAGE_SCHEMA_VERSION:
            raise ValueError("raw ASR per-chunk token budget scope requires v2 lineage")
        per_chunk_token_budget = True
        adaptive_token_budget = token_budget_scope in MLX_ADAPTIVE_DEPTH_BY_SCOPE
        if adaptive_token_budget and (
            isinstance(options.get("temperature"), bool)
            or not isinstance(options.get("temperature"), (int, float))
            or options.get("temperature") != 0.0
        ):
            raise ValueError("raw ASR adaptive token budget scope requires temperature=0.0")
    segment_generation_tokens = 0
    for index, segment in enumerate(segments):
        if not isinstance(segment, dict) or not isinstance(segment.get("text"), str):
            raise ValueError(f"raw ASR segment {index} is invalid")
        if type(segment.get("id")) is not int or segment.get("id") != index:
            raise ValueError(f"raw ASR segment {index} has a non-contiguous id")
        if per_chunk_token_budget:
            chunk_generation_tokens = bounded_document_integer(
                segment.get("generation_tokens"),
                field=f"segment {index} generation token accounting",
                minimum=0,
                maximum=max_tokens - 1,
            )
            if segment_generation_tokens > MAX_SAFE_JSON_INTEGER - chunk_generation_tokens:
                raise ValueError(
                    "raw ASR segment generation token accounting exceeds the "
                    "JSON safe-integer limit"
                )
            segment_generation_tokens += chunk_generation_tokens
        start = finite_document_number(segment.get("start"), field=f"segment {index} start")
        end = finite_document_number(segment.get("end"), field=f"segment {index} end")
        if (
            start < previous_start
            or start < -boundary_tolerance
            or end <= start
            or end > duration_seconds + boundary_tolerance
        ):
            raise ValueError(f"raw ASR segment {index} has invalid timestamp bounds")
        boundary_delta = start - previous_end
        if mlx_backend and not math.isclose(
            start,
            previous_end,
            rel_tol=0.0,
            abs_tol=boundary_tolerance,
        ):
            raise ValueError(f"raw ASR segment {index} does not continuously cover the audio")
        if v2_mlx_backend:
            if boundary_delta > 0:
                cumulative_gap_seconds += boundary_delta
            else:
                cumulative_overlap_seconds -= boundary_delta
        previous_start = start
        previous_end = end
    tail_delta = duration_seconds - previous_end
    if mlx_backend and not math.isclose(
        previous_end,
        duration_seconds,
        rel_tol=0.0,
        abs_tol=boundary_tolerance,
    ):
        raise ValueError("raw ASR segments do not cover the audio through its end")
    if v2_mlx_backend:
        if tail_delta > 0:
            cumulative_gap_seconds += tail_delta
        else:
            cumulative_overlap_seconds -= tail_delta
        if cumulative_gap_seconds > RAW_V2_CUMULATIVE_BOUNDARY_TOLERANCE_SECONDS:
            raise ValueError("raw ASR has excessive cumulative chunk-boundary gaps")
        if cumulative_overlap_seconds > RAW_V2_CUMULATIVE_BOUNDARY_TOLERANCE_SECONDS:
            raise ValueError("raw ASR has excessive cumulative chunk-boundary overlaps")
    if per_chunk_token_budget and text != " ".join(segment["text"] for segment in segments):
        raise ValueError("raw ASR text does not match its per-chunk segment text")

    if mlx_backend:
        precise_budget_markers = (
            "sample_count" in audio,
            "planned_chunk_count" in options,
            "effective_total_token_budget" in options,
        )
        if any(precise_budget_markers) and not all(precise_budget_markers):
            raise ValueError("raw ASR has incomplete precise MLX token budget metadata")
        if per_chunk_token_budget and not all(precise_budget_markers):
            raise ValueError("raw ASR per-chunk token budget scope requires precise MLX metadata")
        if all(precise_budget_markers):
            sample_count = audio.get("sample_count")
            sample_rate_hz = audio.get("sample_rate_hz")
            planned_chunk_count = options.get("planned_chunk_count")
            recorded_total_token_budget = options.get("effective_total_token_budget")
            sample_count = bounded_document_integer(
                sample_count,
                field="audio sample count",
                minimum=MIN_AUDIO_SAMPLE_COUNT,
                maximum=MAX_AUDIO_SAMPLE_COUNT,
            )
            if type(sample_rate_hz) is not int or sample_rate_hz != SAMPLE_RATE:
                raise ValueError(f"raw ASR has invalid audio sample rate; expected {SAMPLE_RATE}")
            if not math.isclose(
                duration_seconds,
                rounded_seconds(sample_count / sample_rate_hz),
                rel_tol=0.0,
                abs_tol=1e-9,
            ):
                raise ValueError("raw ASR audio duration does not match its sample count")
            planned_chunk_count = bounded_document_integer(
                planned_chunk_count,
                field="planned chunk count",
                minimum=1,
                maximum=MAX_PLANNED_CHUNK_COUNT,
            )
            if not adaptive_token_budget and planned_chunk_count != len(segments):
                raise ValueError("raw ASR segment count does not match its planned chunk count")
            budget_chunk_count = planned_chunk_count
            if adaptive_token_budget:
                if generation_tokens is None:
                    raise ValueError("raw ASR adaptive generation has no token accounting")
                budget_chunk_count = validate_adaptive_generation_plan_document(
                    document,
                    segments=segments,
                    sample_count=sample_count,
                    max_tokens=max_tokens,
                    initial_chunk_count=planned_chunk_count,
                    generation_tokens=generation_tokens,
                    expected_pcm_s16le_sha256=adaptive_pcm_s16le_sha256,
                )
            total_token_budget = effective_total_token_budget(
                per_chunk_budget=max_tokens,
                planned_chunk_count=budget_chunk_count,
            )
            recorded_total_token_budget = bounded_document_integer(
                recorded_total_token_budget,
                field="effective total token budget",
                minimum=1,
                maximum=MAX_SAFE_JSON_INTEGER,
            )
            if recorded_total_token_budget != total_token_budget:
                raise ValueError("raw ASR has an invalid effective total token budget")
        else:
            # Old markerless/v2 artifacts did not persist the exact MLX split plan.
            # Retain their stricter nominal-duration reconstruction rather than
            # guessing a larger budget from rounded duration or segment count.
            total_token_budget = effective_total_token_budget(
                per_chunk_budget=max_tokens,
                planned_chunk_count=math.ceil(duration_seconds / validated_chunk_duration),
            )
        if generation_tokens is not None and generation_tokens >= total_token_budget:
            raise ValueError("raw ASR exhausted its effective full-audio token budget")
        if per_chunk_token_budget and generation_tokens != segment_generation_tokens:
            raise ValueError(
                "raw ASR segment generation tokens do not match performance accounting"
            )
    return document


def validate_aligned_document(
    document: Any,
    *,
    engine: str = "mlx-audio",
    model: str,
    aligner: str,
    language: str,
    audio_sha256: str,
    raw_asr_sha256: str,
    raw_document: dict[str, Any],
    max_sentence_characters: int,
    backend_options: dict[str, Any] | None = None,
    model_identity: dict[str, Any] | None = None,
    aligner_identity: dict[str, Any] | None = None,
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
        "engine": engine,
        "model": model,
        "aligner": aligner,
        "audio_sha256": audio_sha256,
        "raw_asr_sha256": raw_asr_sha256,
    }
    for field, expected in expected_source.items():
        if source.get(field) != expected:
            raise ValueError(f"aligned ASR source {field} does not match")
    lineage_version = document.get("lineage_schema_version")
    raw_lineage_version = raw_document.get("lineage_schema_version")
    if lineage_version != raw_lineage_version:
        raise ValueError("aligned ASR lineage schema does not match raw ASR")
    if lineage_version is not None:
        if type(lineage_version) is not int or lineage_version != LINEAGE_SCHEMA_VERSION:
            raise ValueError("aligned ASR has an unsupported lineage schema version")
        recorded_model_identity = validate_model_identity(
            source.get("model_identity"), label="aligned ASR model"
        )
        recorded_aligner_identity = validate_model_identity(
            source.get("aligner_identity"), label="aligned ASR aligner"
        )
        raw_model_identity = validate_model_identity(
            raw_document.get("model_identity"), label="raw ASR"
        )
        if recorded_model_identity != raw_model_identity:
            raise ValueError("aligned ASR model identity does not match raw ASR")
        if model_identity is not None and recorded_model_identity != model_identity:
            raise ValueError("aligned ASR model identity does not match the pinned model")
        if aligner_identity is not None and recorded_aligner_identity != aligner_identity:
            raise ValueError("aligned ASR aligner identity does not match the pinned aligner")
    expected_options = {"max_sentence_characters": max_sentence_characters}
    if backend_options is not None:
        expected_options.update(backend_options)
    if document.get("options") != expected_options:
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
                raise ValueError(f"aligned ASR chunk {index} field {field} does not match raw ASR")
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
        start = finite_document_number(segment.get("start"), field=f"aligned segment {index} start")
        end = finite_document_number(segment.get("end"), field=f"aligned segment {index} end")
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
            newline="\n",
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


def alignment_units(text: str, *, language: str = "Chinese") -> list[str]:
    """Tokenize like Qwen3 ForcedAligner for Chinese or space-delimited text."""
    if language.lower() != "chinese":
        spaced_units: list[str] = []
        for segment in text.split():
            cleaned = "".join(
                character for character in segment if is_alignment_character(character)
            )
            spaced_latin_buffer: list[str] = []

            def flush_space_latin() -> None:
                if spaced_latin_buffer:
                    spaced_units.append("".join(spaced_latin_buffer))
                    spaced_latin_buffer.clear()

            for character in cleaned:
                if is_cjk_character(character):
                    flush_space_latin()
                    spaced_units.append(character)
                else:
                    spaced_latin_buffer.append(character)
            flush_space_latin()
        return spaced_units

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

    for index, character in enumerate(text):
        buffer.append(character)
        is_english_period_ending = character == "." and (
            index + 1 == len(text) or text[index + 1].isspace()
        )
        if character in SENTENCE_ENDINGS.difference({"."}) or is_english_period_ending:
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
    language: str = "Chinese",
) -> list[dict[str, Any]]:
    """Map sentence text back onto character/word alignment items."""
    sentences = sentence_texts(text, max_characters=max_characters)
    expected_units = alignment_units(text, language=language)
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
            f"{mismatch_index}: expected={expected_units[mismatch_index : mismatch_index + 5]!r}, "
            f"actual={actual_units[mismatch_index : mismatch_index + 5]!r}"
        )

    segments: list[dict[str, Any]] = []
    item_index = 0
    sentence_ranges: list[tuple[int, int]] = []
    search_index = 0
    for sentence in sentences:
        sentence_start = text.find(sentence, search_index)
        if sentence_start < 0:
            raise ValueError(f"could not locate sentence text after index {search_index}")
        sentence_end = sentence_start + len(sentence)
        sentence_ranges.append((sentence_start, sentence_end))
        search_index = sentence_end

    pending_start: int | None = None
    for sentence_start, sentence_end in sentence_ranges:
        if pending_start is None:
            pending_start = sentence_start
        sentence = text[pending_start:sentence_end].strip()
        sentence_units = alignment_units(sentence, language=language)
        unit_count = len(sentence_units)
        expected_prefix = expected_units[item_index : item_index + unit_count]
        if sentence_units != expected_prefix:
            # English alignment removes punctuation inside each whitespace-delimited
            # token. When mixed-language text has no gap after punctuation (for
            # example, ``CEO。If``), the aligner emits one ``CEOIf`` item even though
            # sentence splitting found a boundary. Keep the original intervening
            # text and accumulate sentences until the token boundary is real.
            continue

        if unit_count == 0:
            if segments:
                segments[-1]["text"] += sentence
            pending_start = None
            continue

        first_item = aligned_items[item_index]
        last_item = aligned_items[item_index + unit_count - 1]
        segments.append(
            {
                "id": first_segment_id + len(segments),
                "start": rounded_seconds(offset_seconds + float(first_item["start_time"])),
                "end": rounded_seconds(offset_seconds + float(last_item["end_time"])),
                "text": sentence,
                "source_chunk_id": chunk_id,
            }
        )
        item_index += unit_count
        pending_start = None

    if pending_start is not None:
        pending_text = text[pending_start : sentence_ranges[-1][1]].strip()
        pending_units = alignment_units(pending_text, language=language)
        raise ValueError(
            "sentence/alignment boundary mismatch after item "
            f"{item_index}: sentence_units={pending_units[:5]!r}, "
            f"expected={expected_units[item_index : item_index + 5]!r}"
        )

    if item_index != len(aligned_items):
        raise ValueError(
            f"alignment item accounting mismatch: used={item_index}, available={len(aligned_items)}"
        )
    return segments


def main() -> int:
    args = parse_args()
    input_path = args.input.resolve()
    output_path = args.output.resolve()
    aligned_output_path = args.aligned_output.resolve()
    if not input_path.is_file():
        raise FileNotFoundError(f"audio file does not exist: {input_path}")
    if len({input_path, output_path, aligned_output_path}) != 3:
        raise ValueError("input, raw output, and aligned output paths must be distinct")
    finite_document_number(
        args.chunk_duration,
        field="requested chunk duration",
        minimum=MIN_CHUNK_DURATION_SECONDS,
        maximum=MAX_CHUNK_DURATION_SECONDS,
        maximum_exclusive=True,
    )
    bounded_document_integer(
        args.max_tokens,
        field="requested max tokens",
        minimum=1,
        maximum=MAX_SAFE_JSON_INTEGER,
    )
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
    model_revision = pinned_revision(args.model, getattr(args, "model_revision", None))
    aligner_revision = pinned_revision(args.aligner, getattr(args, "aligner_revision", None))

    raw_document: dict[str, Any] | None = None
    if mode in {"align-only", "complete"}:
        loaded_raw_document = read_json_strict(output_path)
        loaded_lineage_version = loaded_raw_document.get("lineage_schema_version")
        if loaded_lineage_version is not None and (
            type(loaded_lineage_version) is not int
            or loaded_lineage_version != LINEAGE_SCHEMA_VERSION
        ):
            raise ValueError("raw ASR has an unsupported lineage schema version")
        if mode == "align-only" and loaded_lineage_version is None:
            raise ValueError(
                "markerless legacy raw ASR cannot be aligned or realigned; "
                "pass --retranscribe to establish v2 model and aligner lineage"
            )
        raw_document = validate_raw_document(
            loaded_raw_document,
            model=args.model,
            language=args.language,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            chunk_duration=args.chunk_duration,
            audio_size_bytes=audio_size_bytes,
            audio_sha256=audio_sha256,
        )
        if raw_document.get("lineage_schema_version") == LINEAGE_SCHEMA_VERSION:
            require_requested_identity(
                raw_document.get("model_identity"),
                repository=args.model,
                requested_revision=model_revision,
                label="raw ASR model",
            )
    if mode == "complete":
        if raw_document is None:
            raise AssertionError("complete ASR has no loaded raw document")
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
        if aligned_document.get("lineage_schema_version") == LINEAGE_SCHEMA_VERSION:
            require_requested_identity(
                aligned_document["source"].get("aligner_identity"),
                repository=args.aligner,
                requested_revision=aligner_revision,
                label="aligned ASR aligner",
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

    if mode == "fresh" and args.model_path is None:
        raise ValueError("fresh ASR requires --model-path for pinned model verification")
    if mode == "align-only" and args.model_path is None:
        raise ValueError("v2 alignment requires --model-path to verify the original model identity")
    if args.aligner_path is None:
        raise ValueError("alignment requires --aligner-path for pinned model verification")
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
    model_identity = (
        build_model_identity(
            repository=args.model,
            requested_revision=model_revision,
            local_path=args.model_path,
        )
        if args.model_path is not None
        else None
    )
    aligner_identity = build_model_identity(
        repository=args.aligner,
        requested_revision=aligner_revision,
        local_path=args.aligner_path,
    )
    if raw_document is not None and raw_document.get("lineage_schema_version") == 2:
        if raw_document.get("model_identity") != model_identity and model_identity is not None:
            raise ValueError("raw ASR model identity does not match the local model files")

    try:
        import mlx.core as mx
        import numpy as np
        from mlx_audio.stt import load
        from mlx_audio.stt.models.qwen3_asr.qwen3_asr import split_audio_into_chunks
        from mlx_audio.stt.utils import load_audio
    except ImportError as error:
        raise SystemExit(
            "MLX Audio is unavailable; run `uv sync --extra media --extra asr`, then use "
            "`uv run --no-sync` for this worker"
        ) from error

    audio_mx = load_audio(input_path.as_posix())
    audio_array = np.array(audio_mx)
    audio_sample_count = bounded_document_integer(
        len(audio_array),
        field="decoded audio sample count",
        minimum=MIN_AUDIO_SAMPLE_COUNT,
        maximum=MAX_AUDIO_SAMPLE_COUNT,
    )
    audio_duration_seconds = audio_sample_count / SAMPLE_RATE
    del audio_mx
    gc.collect()
    mx.clear_cache()

    if raw_document is None:
        planned_chunks, _initial_total_token_budget = plan_mlx_generation(
            audio_array,
            sample_rate=SAMPLE_RATE,
            chunk_duration_seconds=args.chunk_duration,
            per_chunk_budget=args.max_tokens,
            split_audio_into_chunks=split_audio_into_chunks,
        )
        planned_chunk_count = len(planned_chunks)
        model_load_started = time.perf_counter()
        model = load(model_load_target)
        model_load_seconds = time.perf_counter() - model_load_started

        transcription_started = time.perf_counter()
        generation = generate_mlx_planned_chunks(
            model,
            planned_chunks,
            audio_sample_count=audio_sample_count,
            sample_rate=SAMPLE_RATE,
            per_chunk_budget=args.max_tokens,
            temperature=args.temperature,
            language=args.language,
            verbose=args.verbose,
            clear_cache=mx.clear_cache,
        )
        total_token_budget = effective_total_token_budget(
            per_chunk_budget=args.max_tokens,
            planned_chunk_count=generation["final_leaf_chunk_count"],
        )
        transcription_seconds = time.perf_counter() - transcription_started
        raw_chunks = generation["segments"]
        raw_document = {
            "schema_version": 1,
            "lineage_schema_version": LINEAGE_SCHEMA_VERSION,
            "kind": "raw-asr",
            "engine": "mlx-audio",
            "model": args.model,
            "model_identity": model_identity,
            "language": args.language,
            "generated_at": utc_now(),
            "audio": {
                "duration_seconds": rounded_seconds(audio_duration_seconds),
                "sample_count": audio_sample_count,
                "sample_rate_hz": SAMPLE_RATE,
                "size_bytes": audio_size_bytes,
                "sha256": audio_sha256,
            },
            "options": {
                "temperature": args.temperature,
                "max_tokens_per_chunk": args.max_tokens,
                "chunk_duration_seconds": args.chunk_duration,
                "planned_chunk_count": planned_chunk_count,
                "final_leaf_chunk_count": generation["final_leaf_chunk_count"],
                "adaptive_split_count": generation["adaptive_split_count"],
                "adaptive_split_algorithm": MLX_ADAPTIVE_SPLIT_ALGORITHM,
                "adaptive_min_leaf_samples": MLX_ADAPTIVE_MIN_LEAF_SAMPLES,
                "adaptive_max_depth": MLX_ADAPTIVE_MAX_DEPTH,
                "adaptive_max_split_count": MLX_ADAPTIVE_MAX_SPLIT_COUNT,
                "adaptive_energy_window_samples": MLX_ADAPTIVE_ENERGY_WINDOW_SAMPLES,
                "adaptive_quantization": MLX_ADAPTIVE_QUANTIZATION,
                "adaptive_tie_break": MLX_ADAPTIVE_TIE_BREAK,
                "effective_total_token_budget": total_token_budget,
                "token_budget_scope": MLX_ADAPTIVE_TOKEN_BUDGET_SCOPE,
            },
            "performance": {
                "model_load_seconds": rounded_seconds(model_load_seconds),
                "transcription_seconds": rounded_seconds(transcription_seconds),
                "prompt_tokens": generation["prompt_tokens"],
                "generation_tokens": generation["generation_tokens"],
                "attempt_prompt_tokens": generation["attempt_prompt_tokens"],
                "attempt_generation_tokens": generation["attempt_generation_tokens"],
                "generation_call_count": generation["generation_call_count"],
                "prompt_tokens_per_second": rounded_seconds(
                    generation["prompt_tokens"] / transcription_seconds
                    if transcription_seconds > 0
                    else 0
                ),
                "generation_tokens_per_second": rounded_seconds(
                    generation["generation_tokens"] / transcription_seconds
                    if transcription_seconds > 0
                    else 0
                ),
            },
            "generation_plan": generation["generation_plan"],
            "text": generation["text"],
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
            model_identity=model_identity,
            adaptive_pcm_s16le_sha256=generation["pcm_s16le_sha256"],
        )
        write_json_atomically(output_path, raw_document)
        if args.retranscribe:
            aligned_output_path.unlink(missing_ok=True)
        del generation, planned_chunks, model
        gc.collect()
        mx.clear_cache()
    else:
        recorded_duration = finite_document_number(
            raw_document["audio"].get("duration_seconds"),
            field="audio duration",
        )
        if abs(recorded_duration - audio_duration_seconds) > 0.01:
            raise ValueError("raw ASR duration does not match the decoded input audio")
        recorded_sample_count = raw_document["audio"].get("sample_count")
        if recorded_sample_count is not None and recorded_sample_count != audio_sample_count:
            raise ValueError("raw ASR sample count does not match the decoded input audio")

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
            language=args.language,
        )
        all_segments.extend(chunk_segments)
        aligned_chunks.append(
            {
                **chunk,
                "alignment_seconds": rounded_seconds(chunk_alignment_seconds),
                "alignment": [
                    {
                        "text": item["text"],
                        "start": rounded_seconds(float(chunk["start"]) + float(item["start_time"])),
                        "end": rounded_seconds(float(chunk["start"]) + float(item["end_time"])),
                    }
                    for item in aligned_items
                ],
                "sentence_segment_ids": [segment["id"] for segment in chunk_segments],
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
            "alignment_items": sum(len(chunk["alignment"]) for chunk in aligned_chunks),
            "sentence_segments": len(all_segments),
        },
        "text": raw_document["text"],
        "chunks": aligned_chunks,
        "segments": all_segments,
    }
    if raw_document.get("lineage_schema_version") == LINEAGE_SCHEMA_VERSION:
        aligned_document["lineage_schema_version"] = LINEAGE_SCHEMA_VERSION
        aligned_document["source"]["model_identity"] = raw_document["model_identity"]
        aligned_document["source"]["aligner_identity"] = aligner_identity
    validate_aligned_document(
        aligned_document,
        model=args.model,
        aligner=args.aligner,
        language=args.language,
        audio_sha256=audio_sha256,
        raw_asr_sha256=raw_asr_sha256,
        raw_document=raw_document,
        max_sentence_characters=args.max_sentence_characters,
        model_identity=model_identity,
        aligner_identity=aligner_identity,
    )
    write_json_atomically(aligned_output_path, aligned_document)

    del aligner, audio_array
    gc.collect()
    mx.clear_cache()

    raw_performance = raw_document.get("performance", {})
    status = "aligned-from-existing-raw" if mode == "align-only" else "transcribed-and-aligned"

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
                "transcription_seconds": raw_performance.get("transcription_seconds"),
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
