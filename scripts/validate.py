#!/usr/bin/env python3
"""Validate PodWiki Markdown structure and canonical source URLs."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SHOWS_ROOT = ROOT / "shows"
BILIBILI_URL_RE = re.compile(
    r"https://www\.bilibili\.com/video/[^\s)\]\"']+"
)
CANONICAL_BILIBILI_URL_RE = re.compile(
    r"https://www\.bilibili\.com/video/BV[A-Za-z0-9]+/"
)
TRACKING_PARAMETERS = ("spm_id_from", "vd_source")


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def check_front_matter(path: Path, text: str, errors: list[str]) -> None:
    if not text.startswith("---\n"):
        errors.append(f"{relative(path)} must begin with YAML front matter")
        return

    if "\n---\n" not in text[4:]:
        errors.append(f"{relative(path)} has no closing front matter marker")


def check_bilibili_urls(path: Path, text: str, errors: list[str]) -> int:
    for parameter in TRACKING_PARAMETERS:
        if parameter in text:
            errors.append(
                f"{relative(path)} contains tracking parameter {parameter}"
            )

    count = 0
    for match in BILIBILI_URL_RE.finditer(text):
        count += 1
        url = match.group(0)
        if CANONICAL_BILIBILI_URL_RE.fullmatch(url) is None:
            errors.append(
                f"{relative(path)} contains non-canonical Bilibili URL: {url}"
            )
    return count


def main() -> int:
    errors: list[str] = []
    markdown_count = 0
    bilibili_url_count = 0

    if not SHOWS_ROOT.is_dir():
        print("PodWiki validation failed:\n\n- shows directory is missing", file=sys.stderr)
        return 1

    for path in sorted(SHOWS_ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        markdown_count += 1
        if path.name == "README.md":
            check_front_matter(path, text, errors)
        elif path.name.startswith("transcript.") and text.startswith("---\n"):
            errors.append(
                f"{relative(path)} must keep metadata in its episode README"
            )
        bilibili_url_count += check_bilibili_urls(path, text, errors)

    if errors:
        print("PodWiki validation failed:\n", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "PodWiki validation passed: "
        f"{markdown_count} Markdown files, "
        f"{bilibili_url_count} Bilibili URLs."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
