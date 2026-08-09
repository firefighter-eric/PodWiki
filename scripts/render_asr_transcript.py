#!/usr/bin/env python3
"""Refine structured ASR output and render a readable Markdown transcript."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import tempfile
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]


REPLACEMENTS: tuple[tuple[re.Pattern[str], str], ...] = (
    (
        re.compile(
            r"(?<![A-Za-z0-9])(?:OPNI|OPI|Openei|Openai)(?![A-Za-z0-9])",
            re.IGNORECASE,
        ),
        "OpenAI",
    ),
    (re.compile(r"Open啊"), "OpenAI"),
    (
        re.compile(r"(?:翁嘉义|翁嘉译|温嘉义|翁家义|温家翌|Wong嘉义)"),
        "翁家翌",
    ),
    (
        re.compile(
            r"(?<![A-Za-z0-9])(?:Chair|Chai)\s*GPT(?![A-Za-z0-9])",
            re.IGNORECASE,
        ),
        "ChatGPT",
    ),
    (
        re.compile(
            r"(?<![A-Za-z0-9])Chai\s*GP(?![A-Za-z0-9])", re.IGNORECASE
        ),
        "ChatGPT",
    ),
    (
        re.compile(r"(?<![A-Za-z0-9])GP5(?![A-Za-z0-9])", re.IGNORECASE),
        "GPT-5",
    ),
    (
        re.compile(r"(?<![A-Za-z0-9])GPT5(?![A-Za-z0-9])", re.IGNORECASE),
        "GPT-5",
    ),
    (
        re.compile(r"(?<![A-Za-z0-9])GPT4O(?![A-Za-z0-9])", re.IGNORECASE),
        "GPT-4o",
    ),
    (
        re.compile(r"(?<![A-Za-z0-9])GP4(?![A-Za-z0-9])", re.IGNORECASE),
        "GPT-4",
    ),
    (
        re.compile(r"(?<![A-Za-z0-9])RUHF(?![A-Za-z0-9])", re.IGNORECASE),
        "RLHF",
    ),
    (re.compile(r"(?<![A-Za-z0-9])RO(?=\s|$)"), "RL"),
    (
        re.compile(
            r"(?<![A-Za-z0-9])(?:PFGD|PHD)(?![A-Za-z0-9])",
            re.IGNORECASE,
        ),
        "PhD",
    ),
    (
        re.compile(
            r"(?<![A-Za-z0-9])Deep[- ]?Seek(?![A-Za-z0-9])",
            re.IGNORECASE,
        ),
        "DeepSeek",
    ),
    (
        re.compile(
            r"(?<![A-Za-z0-9])Why\s*Not\s*TV(?![A-Za-z0-9])", re.IGNORECASE
        ),
        "WhynotTV",
    ),
    (re.compile(r"(?:添售|天兽|天授)"), "Tianshou"),
    (
        re.compile(r"(?<![A-Za-z0-9])Josman(?![A-Za-z0-9])", re.IGNORECASE),
        "John Schulman",
    ),
    (
        re.compile(
            r"(?<![A-Za-z0-9])Sam Outman(?![A-Za-z0-9])", re.IGNORECASE
        ),
        "Sam Altman",
    ),
)
TRAILING_PUNCTUATION_RE = re.compile(r"[，。！？；：、,.!?;:]$")
LEADING_PUNCTUATION_RE = re.compile(r"^[，。！？；：、,.!?;:]")
MAX_REVERSED_TIMESTAMP_JITTER_SECONDS = 0.250


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Preserve a refined JSON artifact and render it as transcript Markdown."
        )
    )
    parser.add_argument(
        "--input", required=True, type=Path, help="Raw or aligned ASR JSON"
    )
    parser.add_argument(
        "--refined-output", required=True, type=Path, help="Refined ASR JSON"
    )
    parser.add_argument(
        "--output", required=True, type=Path, help="Rendered transcript Markdown"
    )
    parser.add_argument("--episode-id", required=True)
    parser.add_argument("--title", required=True, help="Episode title")
    parser.add_argument("--engine", default="mlx-whisper")
    parser.add_argument("--model", required=True)
    parser.add_argument("--language", default="zh-CN")
    return parser.parse_args()


def clean_text(value: Any) -> str:
    text = re.sub(r"\uFFFDN?", "", str(value or ""))
    text = re.sub(r"\s+", " ", text).strip()

    for pattern, replacement in REPLACEMENTS:
        text = pattern.sub(replacement, text)

    text = re.sub(r"\s+([，。！？；：、])", r"\1", text)
    text = re.sub(r"([，。！？；：、])\s+", r"\1", text)
    return text.strip()


def normalized(text: str) -> str:
    return "".join(
        character.lower()
        for character in text
        if not character.isspace()
        and unicodedata.category(character)[0] not in {"P", "S"}
    )


def contains_lexical_content(text: str) -> bool:
    return any(unicodedata.category(character)[0] in {"L", "N"} for character in text)


def append_text(left: str, right: str) -> str:
    if not left:
        return right
    if not right:
        return left
    if TRAILING_PUNCTUATION_RE.search(left) or LEADING_PUNCTUATION_RE.search(right):
        return f"{left}{right}"
    if left[-1].isascii() and left[-1].isalnum() and right[0].isascii() and right[0].isalnum():
        return f"{left} {right}"
    return f"{left}{right}"


def finite_number(value: Any, *, field: str, segment_index: int) -> float:
    if not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(
            f"segment {segment_index} has invalid {field}: {value!r}"
        )
    return float(value)


def normalize_timestamp_bounds(
    *, start: Any, end: Any, segment_index: int
) -> tuple[float, float]:
    normalized_start = finite_number(
        start, field="start", segment_index=segment_index
    )
    normalized_end = finite_number(end, field="end", segment_index=segment_index)

    if normalized_start < 0 or normalized_end < 0:
        raise ValueError(
            f"segment {segment_index} has negative timestamp bounds: "
            f"start={normalized_start!r}, end={normalized_end!r}"
        )

    reversed_by = normalized_start - normalized_end
    if reversed_by > MAX_REVERSED_TIMESTAMP_JITTER_SECONDS:
        raise ValueError(
            f"segment {segment_index} end precedes start by "
            f"{reversed_by:.3f}s, exceeding the "
            f"{MAX_REVERSED_TIMESTAMP_JITTER_SECONDS:.3f}s tolerance"
        )
    if reversed_by > 0:
        normalized_end = normalized_start

    return normalized_start, normalized_end


def refine_segments(raw_segments: list[dict[str, Any]]) -> list[dict[str, Any]]:
    refined: list[dict[str, Any]] = []
    previous_start: float | None = None

    for source_index, segment in enumerate(raw_segments):
        text = clean_text(segment.get("text"))
        if not text or not contains_lexical_content(text):
            continue

        start, end = normalize_timestamp_bounds(
            start=segment.get("start"),
            end=segment.get("end"),
            segment_index=source_index,
        )
        if previous_start is not None:
            reversed_by = previous_start - start
            if reversed_by > MAX_REVERSED_TIMESTAMP_JITTER_SECONDS:
                raise ValueError(
                    f"segment {source_index} start precedes the previous "
                    f"segment start by {reversed_by:.3f}s, exceeding the "
                    f"{MAX_REVERSED_TIMESTAMP_JITTER_SECONDS:.3f}s tolerance"
                )
            if reversed_by > 0:
                start = previous_start
                end = max(end, start)
        previous_start = start
        source_id = segment.get("id", source_index)

        if refined and normalized(text) == normalized(refined[-1]["text"]):
            refined[-1]["source_segment_indexes"].append(source_index)
            refined[-1]["source_segment_ids"].append(source_id)
            continue

        refined.append(
            {
                "start": start,
                "end": end,
                "text": text,
                "source_segment_indexes": [source_index],
                "source_segment_ids": [source_id],
            }
        )

    return refined


def merge_blocks(refined_segments: list[dict[str, Any]]) -> list[dict[str, Any]]:
    blocks: list[dict[str, Any]] = []

    for refined_index, segment in enumerate(refined_segments):
        if blocks:
            current = blocks[-1]
            gap = segment["start"] - current["end"]
            merged_text = append_text(current["text"], segment["text"])
            can_merge = (
                gap <= 2.5
                and segment["end"] - current["start"] <= 35
                and len(merged_text) <= 260
            )
        else:
            current = None
            merged_text = segment["text"]
            can_merge = False

        if current is not None and can_merge:
            current["end"] = max(current["end"], segment["end"])
            current["text"] = merged_text
            current["refined_segment_indexes"].append(refined_index)
        else:
            blocks.append(
                {
                    "start": segment["start"],
                    "end": segment["end"],
                    "text": segment["text"],
                    "refined_segment_indexes": [refined_index],
                }
            )

    return blocks


def format_timestamp(seconds: float) -> str:
    total_seconds = max(0, math.floor(seconds))
    hours, remainder = divmod(total_seconds, 3600)
    minutes, remaining_seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{remaining_seconds:02d}"


def render_markdown(
    *,
    refined_segments: list[dict[str, Any]],
    title: str,
) -> str:
    body = "\n".join(
        f'[{format_timestamp(segment["start"])}] {segment["text"]}  '
        for segment in refined_segments
    )
    return f"""# {title}

{body}
"""


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


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write_artifact_pair_atomically(
    *, refined_path: Path, refined_text: str, transcript_path: Path, transcript_text: str
) -> None:
    if refined_path.resolve() == transcript_path.resolve():
        raise ValueError("refined JSON and transcript paths must be distinct")
    temporary_paths: dict[str, Path] = {}
    try:
        for label, path, text in (
            ("refined", refined_path, refined_text),
            ("transcript", transcript_path, transcript_text),
        ):
            path.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(
                mode="w",
                encoding="utf-8",
                newline="\n",
                dir=path.parent,
                prefix=f".podwiki-{path.name}.",
                suffix=".tmp",
                delete=False,
            ) as stream:
                stream.write(text)
                stream.flush()
                os.fsync(stream.fileno())
                temporary_paths[label] = Path(stream.name)

        temporary_paths["transcript"].replace(transcript_path)
        transcript_path.chmod(0o644)
        temporary_paths.pop("transcript")
        temporary_paths["refined"].replace(refined_path)
        refined_path.chmod(0o644)
        temporary_paths.pop("refined")
    finally:
        for temporary_path in temporary_paths.values():
            temporary_path.unlink(missing_ok=True)


def main() -> int:
    args = parse_args()
    if len(
        {
            args.input.resolve(),
            args.refined_output.resolve(),
            args.output.resolve(),
        }
    ) != 3:
        raise ValueError("input, refined output, and transcript paths must be distinct")
    raw = json.loads(
        args.input.read_text(encoding="utf-8"),
        parse_constant=lambda _constant: None,
    )
    raw_segments = raw.get("segments", [])
    if not isinstance(raw_segments, list):
        raise ValueError("input JSON field 'segments' must be a list")

    refined_segments = refine_segments(raw_segments)
    blocks = merge_blocks(refined_segments)
    generated_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    markdown = render_markdown(
        refined_segments=refined_segments,
        title=args.title,
    )

    refined_document = {
        "schema_version": 1,
        "kind": "refined-asr",
        "episode_id": args.episode_id,
        "language": args.language,
        "source": {
            "input_asr_path": repository_path(args.input),
            "input_asr_sha256": sha256_file(args.input),
            "engine": args.engine,
            "model": args.model,
        },
        "rendered_transcript": {
            "path": repository_path(args.output),
            "sha256": sha256_text(markdown),
        },
        "generated_at": generated_at,
        "statistics": {
            "source_segments": len(raw_segments),
            "refined_segments": len(refined_segments),
            "rendered_blocks": len(blocks),
            "rendered_lines": len(refined_segments),
        },
        "segments": refined_segments,
        "blocks": blocks,
    }

    refined_text = (
        json.dumps(
            refined_document,
            ensure_ascii=False,
            indent=2,
            allow_nan=False,
        )
        + "\n"
    )
    write_artifact_pair_atomically(
        refined_path=args.refined_output,
        refined_text=refined_text,
        transcript_path=args.output,
        transcript_text=markdown,
    )

    print(
        json.dumps(
            {
                "input": args.input.as_posix(),
                "refined_output": args.refined_output.as_posix(),
                "output": args.output.as_posix(),
                "source_segments": len(raw_segments),
                "refined_segments": len(refined_segments),
                "rendered_blocks": len(blocks),
                "rendered_lines": len(refined_segments),
                "generated_at": generated_at,
                "markdown_characters": len(markdown),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
