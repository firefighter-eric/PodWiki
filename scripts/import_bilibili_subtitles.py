#!/usr/bin/env python3
"""Import one authenticated Bilibili AI subtitle from ignored cached inputs."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import tempfile
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Any

from acquire_media import canonical_source_url


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RUN_ID = "bilibili-subtitles"
DEFAULT_LANGUAGE = "zh-CN"
MAX_EDGE_GAP_SECONDS = 30


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", required=True)
    parser.add_argument("--episode-dir", required=True, type=Path)
    parser.add_argument("--metadata-json", required=True, type=Path)
    parser.add_argument("--subtitle-json", required=True, type=Path)
    parser.add_argument(
        "--access-context",
        required=True,
        choices=("anonymous", "authenticated"),
        help="Record only the non-sensitive access mode used to discover the track.",
    )
    parser.add_argument("--title")
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def reject_non_finite(value: str) -> None:
    raise ValueError(f"non-finite JSON value {value}")


def load_json(payload: bytes, *, label: str) -> dict[str, Any]:
    document = json.loads(
        payload.decode("utf-8"),
        object_pairs_hook=reject_duplicate_keys,
        parse_constant=reject_non_finite,
    )
    if not isinstance(document, dict):
        raise ValueError(f"{label} must be a JSON object")
    return document


def require_cache_file(path: Path, *, label: str) -> Path:
    cache_root = (ROOT / ".cache").resolve()
    resolved = path.resolve()
    try:
        resolved.relative_to(cache_root)
    except ValueError as error:
        raise ValueError(f"{label} must be inside the repository .cache/") from error
    if not resolved.is_file():
        raise FileNotFoundError(resolved)
    return resolved


def validate_public_free_bilibili_source(info: dict[str, Any]) -> None:
    platform_metadata = info.get("platform_metadata")
    if not isinstance(platform_metadata, dict):
        raise ValueError("metadata has no Bilibili platform metadata")
    if platform_metadata.get("state") != 0:
        raise ValueError("Bilibili source is not in the public playable state")
    rights = platform_metadata.get("rights")
    if not isinstance(rights, dict):
        raise ValueError("Bilibili metadata has no access-rights mapping")
    denied_flags = (
        "pay",
        "ugc_pay",
        "ugc_pay_preview",
        "arc_pay",
        "is_chargeable_season",
        "is_upower_exclusive",
        "is_upower_play",
    )
    for flag in denied_flags:
        if rights.get(flag) not in (0, False):
            raise ValueError(f"Bilibili source is access-restricted by rights.{flag}")


def load_cached_inputs(
    *, metadata_path: Path, subtitle_path: Path, canonical_url: str
) -> tuple[dict[str, Any], bytes]:
    resolved_metadata = require_cache_file(metadata_path, label="metadata JSON")
    resolved_subtitle = require_cache_file(subtitle_path, label="subtitle JSON")
    metadata = load_json(resolved_metadata.read_bytes(), label="metadata JSON")
    info = metadata.get("source")
    if not isinstance(info, dict):
        raise ValueError("metadata JSON must be an acquire_media source sidecar")
    if info.get("platform") != "bilibili" or info.get("canonical_url") != canonical_url:
        raise ValueError("cached metadata does not match the canonical Bilibili URL")
    if info.get("page") != 1:
        raise ValueError("Bilibili subtitle import currently requires a single page-1 video")
    if not isinstance(info.get("bvid"), str):
        raise ValueError("Bilibili metadata has no BVID")
    for field in ("aid", "cid"):
        value = info.get(field)
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise ValueError(f"Bilibili metadata has no valid {field}")
    validate_public_free_bilibili_source(info)
    return info, resolved_subtitle.read_bytes()


def milliseconds(value: Any, *, field: str) -> int:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field} must be a finite non-negative number")
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError(f"{field} must be a finite non-negative number")
    try:
        decimal_value = Decimal(str(value))
    except InvalidOperation as error:
        raise ValueError(f"{field} must be a finite non-negative number") from error
    if not decimal_value.is_finite() or decimal_value < 0:
        raise ValueError(f"{field} must be a finite non-negative number")
    return int((decimal_value * 1000).to_integral_value(rounding=ROUND_HALF_UP))


def normalize_text(value: Any, *, field: str) -> str:
    if not isinstance(value, str):
        raise ValueError(f"{field} must be text")
    text = re.sub(r"\s+", " ", value.replace("\u200b", " ")).strip()
    if not text:
        raise ValueError(f"{field} has no visible subtitle text")
    return text


def subtitle_segments(document: dict[str, Any]) -> list[dict[str, Any]]:
    if document.get("type") != "AIsubtitle":
        raise ValueError("subtitle JSON is not a Bilibili AI subtitle document")
    if document.get("lang") != "zh":
        raise ValueError("Bilibili AI subtitle language must be zh")
    body = document.get("body")
    if not isinstance(body, list) or not body:
        raise ValueError("subtitle.body must be a non-empty list")

    result: list[dict[str, Any]] = []
    previous_start = -1
    seen_sids: set[int] = set()
    for index, item in enumerate(body):
        field = f"subtitle.body[{index}]"
        if not isinstance(item, dict):
            raise ValueError(f"{field} must be an object")
        sid = item.get("sid")
        if isinstance(sid, bool) or not isinstance(sid, int) or sid <= 0:
            raise ValueError(f"{field}.sid must be a positive integer")
        if sid in seen_sids:
            raise ValueError(f"{field}.sid is duplicated")
        seen_sids.add(sid)
        start_ms = milliseconds(item.get("from"), field=f"{field}.from")
        end_ms = milliseconds(item.get("to"), field=f"{field}.to")
        if end_ms <= start_ms:
            raise ValueError(f"{field}.to must be later than from")
        if start_ms < previous_start:
            raise ValueError(f"{field}.from is not monotonic")
        previous_start = start_ms
        result.append(
            {
                "source_segment_index": index,
                "sid": sid,
                "start_ms": start_ms,
                "end_ms": end_ms,
                "text": normalize_text(item.get("content"), field=f"{field}.content"),
            }
        )
    return result


def source_duration_ms(info: dict[str, Any]) -> int:
    platform_metadata = info.get("platform_metadata")
    platform_duration = (
        platform_metadata.get("duration_seconds")
        if isinstance(platform_metadata, dict)
        else None
    )
    duration = platform_duration if platform_duration is not None else info.get("duration_seconds")
    result = milliseconds(duration, field="metadata duration_seconds")
    if result <= 0:
        raise ValueError("metadata duration_seconds must be positive")
    return result


def validate_edge_coverage(segments: list[dict[str, Any]], *, duration_ms: int) -> None:
    allowance = MAX_EDGE_GAP_SECONDS * 1000
    first_start = segments[0]["start_ms"]
    last_end = segments[-1]["end_ms"]
    if first_start > allowance:
        raise ValueError("Bilibili AI subtitle begins more than 30 seconds after the source")
    if last_end < duration_ms - allowance:
        raise ValueError("Bilibili AI subtitle ends more than 30 seconds before the source")
    if last_end > duration_ms + allowance:
        raise ValueError("Bilibili AI subtitle extends more than 30 seconds past the source")


def format_timestamp(milliseconds_value: int) -> str:
    total_seconds = milliseconds_value // 1000
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    if hours > 99:
        raise ValueError("subtitle timestamp exceeds the two-digit-hour transcript contract")
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def transcript_bytes(title: str, segments: list[dict[str, Any]]) -> bytes:
    if not title.strip() or "\n" in title or "\r" in title:
        raise ValueError("title must be one non-empty line")
    lines = [f"# {title}", ""]
    lines.extend(
        f"[{format_timestamp(segment['start_ms'])}] {segment['text']}  "
        for segment in segments
    )
    return ("\n".join(lines) + "\n").encode("utf-8")


def json_bytes(document: dict[str, Any]) -> bytes:
    return (
        json.dumps(document, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n"
    ).encode("utf-8")


def build_outputs(
    *,
    canonical_url: str,
    info: dict[str, Any],
    subtitle_payload_bytes: bytes,
    title: str,
    generated_at: str,
    language: str,
    access_context: str,
    raw_repository_path: str,
    transcript_repository_path: str,
) -> tuple[bytes, bytes, bytes]:
    payload = load_json(subtitle_payload_bytes, label="subtitle JSON")
    segments = subtitle_segments(payload)
    duration_ms = source_duration_ms(info)
    validate_edge_coverage(segments, duration_ms=duration_ms)
    transcript = transcript_bytes(title, segments)

    raw_document = {
        "schema_version": 1,
        "kind": "podwiki-bilibili-subtitle-raw",
        "generated_at": generated_at,
        "source": {
            "platform": "bilibili",
            "canonical_url": canonical_url,
            "bvid": info["bvid"],
            "aid": info["aid"],
            "cid": info["cid"],
            "page": info["page"],
            "uploader": info.get("uploader"),
            "uploader_id": info.get("uploader_id"),
            "language": language,
            "track_type": "bilibili-ai-subtitle",
            "format": "bilibili-ai-subtitle-json",
            "access_context": access_context,
            "payload_sha256": sha256_bytes(subtitle_payload_bytes),
        },
        "payload": payload,
    }
    raw = json_bytes(raw_document)
    refined_document = {
        "schema_version": 1,
        "kind": "podwiki-bilibili-subtitle-refined",
        "generated_at": generated_at,
        "source": {
            "raw_path": raw_repository_path,
            "raw_sha256": sha256_bytes(raw),
            "normalization": "bilibili-ai-subtitle-body-v1",
        },
        "segments": segments,
        "quality": {
            "source_segments": len(segments),
            "rendered_lines": len(segments),
            "source_duration_ms": duration_ms,
            "first_start_ms": segments[0]["start_ms"],
            "last_end_ms": segments[-1]["end_ms"],
            "max_edge_gap_seconds": MAX_EDGE_GAP_SECONDS,
        },
        "rendered_transcript": {
            "path": transcript_repository_path,
            "sha256": sha256_bytes(transcript),
        },
    }
    return raw, json_bytes(refined_document), transcript


def write_atomically(path: Path, payload: bytes, *, overwrite: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.is_file() and path.read_bytes() == payload:
            return
        if not overwrite:
            raise FileExistsError(f"refusing to replace existing output without --overwrite: {path}")
    descriptor, temporary_name = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.")
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def reject_output_conflicts(outputs: dict[Path, bytes], *, overwrite: bool) -> None:
    if overwrite:
        return
    for path, payload in outputs.items():
        if path.exists() and (not path.is_file() or path.read_bytes() != payload):
            raise FileExistsError(f"refusing to replace existing output without --overwrite: {path}")


def main() -> int:
    args = parse_args()
    platform, canonical_url = canonical_source_url(args.url)
    if platform != "bilibili":
        raise ValueError("subtitle import requires one canonical Bilibili video")

    episode_dir = args.episode_dir.resolve()
    try:
        episode_relative = episode_dir.relative_to(ROOT)
    except ValueError as error:
        raise ValueError("episode directory must be inside the repository") from error
    if (
        len(episode_relative.parts) != 4
        or episode_relative.parts[0] != "shows"
        or episode_relative.parts[2] != "episodes"
    ):
        raise ValueError("episode directory must be shows/<show>/episodes/<episode>")

    info, subtitle_payload = load_cached_inputs(
        metadata_path=args.metadata_json,
        subtitle_path=args.subtitle_json,
        canonical_url=canonical_url,
    )
    title = args.title or info.get("title")
    if not isinstance(title, str):
        raise ValueError("Bilibili metadata has no title")
    generated_at = utc_now()
    run_dir = episode_dir / "asr" / DEFAULT_RUN_ID
    run_relative = run_dir.relative_to(ROOT).as_posix()
    raw, refined, transcript = build_outputs(
        canonical_url=canonical_url,
        info=info,
        subtitle_payload_bytes=subtitle_payload,
        title=title,
        generated_at=generated_at,
        language=DEFAULT_LANGUAGE,
        access_context=args.access_context,
        raw_repository_path=f"{run_relative}/raw.json",
        transcript_repository_path=f"{run_relative}/transcript.{DEFAULT_LANGUAGE}.md",
    )
    outputs = {
        run_dir / "raw.json": raw,
        run_dir / "refined.json": refined,
        run_dir / f"transcript.{DEFAULT_LANGUAGE}.md": transcript,
        episode_dir / f"transcript.{DEFAULT_LANGUAGE}.md": transcript,
    }
    reject_output_conflicts(outputs, overwrite=args.overwrite)
    for path, payload in outputs.items():
        write_atomically(path, payload, overwrite=args.overwrite)

    refined_document = json.loads(refined)
    quality = refined_document.get("quality")
    print(
        json.dumps(
            {
                "canonical_url": canonical_url,
                "bvid": info.get("bvid"),
                "aid": info.get("aid"),
                "cid": info.get("cid"),
                "generated_at": generated_at,
                "access_context": args.access_context,
                "quality": quality,
                "outputs": [path.relative_to(ROOT).as_posix() for path in outputs],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
