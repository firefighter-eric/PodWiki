#!/usr/bin/env python3
"""Refine raw MLX Whisper output and render a readable Markdown transcript."""

from __future__ import annotations

import argparse
import json
import math
import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPLACEMENTS: tuple[tuple[re.Pattern[str], str], ...] = (
    (
        re.compile(
            r"(?<![A-Za-z0-9])(?:OPNI|OPI|Openei|Openai)(?![A-Za-z0-9])",
            re.IGNORECASE,
        ),
        "OpenAI",
    ),
    (re.compile(r"Open啊"), "OpenAI"),
    (re.compile(r"(?:翁嘉义|温嘉义|翁家义|温家翌|Wong嘉义)"), "翁家翌"),
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
            r"(?<![A-Za-z0-9])WhyNotTV(?![A-Za-z0-9])", re.IGNORECASE
        ),
        "WhynotTV",
    ),
    (re.compile(r"(?:添售|天兽)"), "Tianshou"),
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Preserve a refined JSON artifact and render it as transcript Markdown."
        )
    )
    parser.add_argument("--input", required=True, type=Path, help="Raw ASR JSON")
    parser.add_argument(
        "--refined-output", required=True, type=Path, help="Refined ASR JSON"
    )
    parser.add_argument(
        "--output", required=True, type=Path, help="Rendered transcript Markdown"
    )
    parser.add_argument("--episode-id", required=True)
    parser.add_argument("--title", required=True, help="Episode title")
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


def refine_segments(raw_segments: list[dict[str, Any]]) -> list[dict[str, Any]]:
    refined: list[dict[str, Any]] = []

    for source_index, segment in enumerate(raw_segments):
        text = clean_text(segment.get("text"))
        if not text:
            continue

        start = finite_number(
            segment.get("start"), field="start", segment_index=source_index
        )
        end = finite_number(
            segment.get("end"), field="end", segment_index=source_index
        )
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
            current["end"] = segment["end"]
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


def main() -> int:
    args = parse_args()
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

    refined_document = {
        "schema_version": 1,
        "kind": "refined-asr",
        "episode_id": args.episode_id,
        "language": args.language,
        "source": {
            "raw_asr_path": args.input.as_posix(),
            "engine": "mlx-whisper",
            "model": args.model,
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

    args.refined_output.parent.mkdir(parents=True, exist_ok=True)
    args.refined_output.write_text(
        json.dumps(
            refined_document,
            ensure_ascii=False,
            indent=2,
            allow_nan=False,
        )
        + "\n",
        encoding="utf-8",
    )

    markdown = render_markdown(
        refined_segments=refined_segments,
        title=args.title,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(markdown, encoding="utf-8")

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
