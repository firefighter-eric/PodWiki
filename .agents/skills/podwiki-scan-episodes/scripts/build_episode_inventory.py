#!/usr/bin/env python3
"""Build a deterministic repository identity inventory for episode scans."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlencode, urlsplit, urlunsplit


STABLE_IDENTIFIER_FIELDS = {
    "bvid",
    "aid",
    "cid",
    "eid",
    "guid",
    "rss_guid",
    "episode_guid",
    "video_id",
    "media_id",
}


def extract_front_matter_lines(text: str) -> list[str]:
    if not text.startswith("---\n"):
        return []
    closing = text.find("\n---\n", 4)
    if closing < 0:
        return []
    return text[4:closing].splitlines()


def decode_scalar(value: str) -> Any:
    raw = value.strip()
    if raw == "[]":
        return []
    if raw.lower() in {"null", "~"}:
        return None
    if raw == "true":
        return True
    if raw == "false":
        return False
    if re.fullmatch(r"-?\d+", raw):
        return int(raw)
    if len(raw) >= 2 and raw[0] == raw[-1] == '"':
        try:
            decoded = json.loads(raw)
        except json.JSONDecodeError:
            return raw
        return decoded if isinstance(decoded, str) else raw
    if len(raw) >= 2 and raw[0] == raw[-1] == "'":
        return raw[1:-1].replace("''", "'")
    return raw


def top_level_value(lines: list[str], key: str) -> Any:
    prefix = f"{key}:"
    for line in lines:
        if line and not line.startswith(" ") and line.startswith(prefix):
            return decode_scalar(line.split(":", 1)[1])
    return None


def parse_mapping_list(lines: list[str], section: str) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    nested_field: str | None = None
    in_section = False

    for line in lines:
        stripped = line.strip()
        indent = len(line) - len(line.lstrip(" "))
        if not in_section:
            if indent == 0 and stripped.startswith(f"{section}:"):
                if stripped.split(":", 1)[1].strip() == "[]":
                    return []
                in_section = True
            continue
        if stripped and indent == 0:
            break
        if not stripped or stripped.startswith("#"):
            continue
        if indent == 2 and (stripped == "-" or stripped.startswith("- ")):
            current = {}
            items.append(current)
            nested_field = None
            inline = stripped[1:].strip()
            if inline and ":" in inline:
                key, value = inline.split(":", 1)
                current[key.strip()] = decode_scalar(value)
            continue
        if current is None:
            continue
        if indent == 4 and ":" in stripped:
            key, value = stripped.split(":", 1)
            key = key.strip()
            raw_value = value.strip()
            if raw_value:
                current[key] = decode_scalar(raw_value)
                nested_field = None
            else:
                current[key] = {}
                nested_field = key
            continue
        if indent == 6 and nested_field is not None and ":" in stripped:
            nested = current.get(nested_field)
            if isinstance(nested, dict):
                key, value = stripped.split(":", 1)
                nested[key.strip()] = decode_scalar(value)
    return items


def canonical_url(value: Any) -> str | None:
    if not isinstance(value, str) or not value:
        return None
    try:
        parsed = urlsplit(value)
    except ValueError:
        return None
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return None
    host = parsed.netloc.lower()
    if host in {"youtube.com", "www.youtube.com", "m.youtube.com"}:
        query = parse_qs(parsed.query)
        if parsed.path == "/watch" and len(query.get("v", [])) == 1:
            video_id = query["v"][0]
            if re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
                return urlunsplit(
                    ("https", "www.youtube.com", "/watch", urlencode({"v": video_id}), "")
                )
        if parsed.path == "/playlist" and len(query.get("list", [])) == 1:
            playlist_id = query["list"][0]
            if re.fullmatch(r"[A-Za-z0-9_-]{10,64}", playlist_id):
                return urlunsplit(
                    (
                        "https",
                        "www.youtube.com",
                        "/playlist",
                        urlencode({"list": playlist_id}),
                        "",
                    )
                )
        return None
    return urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), parsed.path, "", ""))


def source_keys(source: dict[str, Any]) -> list[str]:
    platform = str(source.get("platform") or "unknown").lower()
    keys: set[str] = set()
    normalized_url = canonical_url(source.get("url"))
    if normalized_url:
        keys.add(f"url:{normalized_url}")
    identifiers = source.get("identifiers")
    if isinstance(identifiers, dict):
        for name, value in identifiers.items():
            if name not in STABLE_IDENTIFIER_FIELDS or value is None or value == "":
                continue
            normalized = str(value)
            if name in {"bvid", "eid"}:
                normalized = normalized.lower()
            keys.add(f"{platform}:{name}:{normalized}")
    return sorted(keys)


def normalized_source(source: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {
        "platform": source.get("platform"),
        "kind": source.get("kind"),
        "url": canonical_url(source.get("url")),
    }
    identifiers = source.get("identifiers")
    if isinstance(identifiers, dict):
        result["identifiers"] = {
            str(key): value
            for key, value in sorted(identifiers.items())
            if value is not None and value != ""
        }
    result["source_keys"] = source_keys(source)
    return result


def git_commit(repository_root: Path) -> str | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(repository_root), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    commit = result.stdout.strip().lower()
    return commit if re.fullmatch(r"[0-9a-f]{40}", commit) else None


def publication_sort_key(value: Any) -> float:
    if not isinstance(value, str):
        return float("-inf")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return float("-inf")
    if parsed.tzinfo is None:
        return float("-inf")
    return parsed.timestamp()


def parse_publication(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def incremental_coverage_start(episodes: list[dict[str, Any]]) -> str | None:
    publications = [
        parsed
        for episode in episodes
        if (parsed := parse_publication(episode.get("published_at"))) is not None
    ]
    if not publications:
        return None
    publications.sort(reverse=True)
    ninety_days_before_newest = publications[0] - timedelta(days=90)
    stored_overlap = publications[2] if len(publications) >= 3 else publications[-1]
    start = min(ninety_days_before_newest, stored_overlap)
    return start.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def build_inventory(
    repository_root: Path,
    *,
    selected_show_ids: set[str] | None = None,
    generated_at: str | None = None,
) -> dict[str, Any]:
    root = repository_root.resolve()
    shows_root = root / "shows"
    if not shows_root.is_dir():
        raise ValueError(f"{repository_root} does not contain shows/")

    shows: list[dict[str, Any]] = []
    found_show_ids: set[str] = set()
    for show_readme in sorted(shows_root.glob("*/README.md")):
        show_lines = extract_front_matter_lines(show_readme.read_text(encoding="utf-8"))
        show_id = top_level_value(show_lines, "id")
        if not isinstance(show_id, str) or not show_id:
            raise ValueError(f"{show_readme.relative_to(root)} has no valid show id")
        found_show_ids.add(show_id)
        if selected_show_ids is not None and show_id not in selected_show_ids:
            continue

        show_sources = [normalized_source(item) for item in parse_mapping_list(show_lines, "sources")]
        episodes: list[dict[str, Any]] = []
        episode_root = show_readme.parent / "episodes"
        for episode_readme in sorted(episode_root.glob("*/README.md")):
            lines = extract_front_matter_lines(episode_readme.read_text(encoding="utf-8"))
            episode_id = top_level_value(lines, "id")
            if not isinstance(episode_id, str) or not episode_id:
                raise ValueError(f"{episode_readme.relative_to(root)} has no valid episode id")
            sources = [normalized_source(item) for item in parse_mapping_list(lines, "sources")]
            keys = sorted({key for source in sources for key in source["source_keys"]})
            episodes.append(
                {
                    "id": episode_id,
                    "episode_key": top_level_value(lines, "episode_key"),
                    "episode_number": top_level_value(lines, "episode_number"),
                    "title": top_level_value(lines, "title"),
                    "published_at": top_level_value(lines, "published_at"),
                    "directory": episode_readme.parent.relative_to(root).as_posix(),
                    "sources": sources,
                    "source_keys": keys,
                }
            )

        episodes.sort(
            key=lambda item: (
                publication_sort_key(item.get("published_at")),
                str(item.get("id") or ""),
            ),
            reverse=True,
        )
        known_keys = sorted({key for episode in episodes for key in episode["source_keys"]})
        shows.append(
            {
                "show_id": show_id,
                "title": top_level_value(show_lines, "title"),
                "status": top_level_value(show_lines, "status"),
                "readme": show_readme.relative_to(root).as_posix(),
                "sources": show_sources,
                "episode_count": len(episodes),
                "latest_published_at": (
                    episodes[0].get("published_at")
                    if episodes
                    and publication_sort_key(episodes[0].get("published_at")) != float("-inf")
                    else None
                ),
                "recommended_incremental_coverage_start": incremental_coverage_start(episodes),
                "known_source_keys": known_keys,
                "episodes": episodes,
            }
        )

    if selected_show_ids is not None:
        missing = sorted(selected_show_ids - found_show_ids)
        if missing:
            raise ValueError(f"unknown show id(s): {', '.join(missing)}")
    shows.sort(key=lambda item: item["show_id"])
    timestamp = generated_at or datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    return {
        "schema_version": 1,
        "kind": "podwiki-repository-episode-inventory",
        "generated_at": timestamp,
        "repository_commit": git_commit(root),
        "shows": shows,
    }


def write_json_atomic(path: Path, document: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            "w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            json.dump(document, handle, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
            temporary = handle.name
        os.replace(temporary, path)
        temporary = None
    finally:
        if temporary is not None:
            Path(temporary).unlink(missing_ok=True)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", type=Path, default=Path.cwd())
    parser.add_argument("--show", action="append", default=[], help="Show id; repeat as needed")
    parser.add_argument("--generated-at", help="Override UTC timestamp for reproducible tests")
    parser.add_argument("--output", type=Path, help="Write atomically instead of printing")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    selected = set(args.show) if args.show else None
    try:
        document = build_inventory(
            args.repository_root,
            selected_show_ids=selected,
            generated_at=args.generated_at,
        )
    except (OSError, UnicodeError, ValueError) as error:
        print(f"inventory error: {error}", file=sys.stderr)
        return 1
    if args.output:
        write_json_atomic(args.output, document)
        print(f"wrote {args.output}")
    else:
        json.dump(document, sys.stdout, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False)
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
