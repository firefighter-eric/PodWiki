#!/usr/bin/env python3
"""Import one public YouTube publisher caption and aligned Chinese machine translation."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from acquire_media import (
    available_javascript_runtime,
    canonical_source_url,
    validate_extracted_info,
)


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RUN_ID = "youtube-subtitles"
DEFAULT_SOURCE_LANGUAGE = "en"
DEFAULT_TRANSLATION_TRACK = "zh-Hans-en"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", required=True)
    parser.add_argument("--episode-dir", required=True, type=Path)
    parser.add_argument("--title")
    parser.add_argument("--source-language", default=DEFAULT_SOURCE_LANGUAGE)
    parser.add_argument("--translation-track", default=DEFAULT_TRANSLATION_TRACK)
    parser.add_argument("--run-id", default=DEFAULT_RUN_ID)
    parser.add_argument("--metadata-json", type=Path)
    parser.add_argument("--source-json3", type=Path)
    parser.add_argument("--translation-json3", type=Path)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument(
        "--verbose",
        action=argparse.BooleanOptionalAction,
        default=True,
    )
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


def load_json3(payload: bytes, *, label: str) -> dict[str, Any]:
    document = json.loads(
        payload.decode("utf-8"),
        object_pairs_hook=reject_duplicate_keys,
        parse_constant=reject_non_finite,
    )
    if not isinstance(document, dict) or document.get("wireMagic") != "pb3":
        raise ValueError(f"{label} must be a YouTube json3 caption document")
    return document


def load_cached_inputs(
    *,
    metadata_path: Path,
    source_path: Path,
    translation_path: Path,
    canonical_url: str,
) -> tuple[dict[str, Any], bytes, bytes]:
    cache_root = (ROOT / ".cache").resolve()
    resolved_paths = [path.resolve() for path in (metadata_path, source_path, translation_path)]
    for path in resolved_paths:
        try:
            path.relative_to(cache_root)
        except ValueError as error:
            raise ValueError("cached caption inputs must be inside the repository .cache/") from error
        if not path.is_file():
            raise FileNotFoundError(path)
    metadata = json.loads(
        resolved_paths[0].read_text(encoding="utf-8"),
        object_pairs_hook=reject_duplicate_keys,
        parse_constant=reject_non_finite,
    )
    if not isinstance(metadata, dict) or not isinstance(metadata.get("source"), dict):
        raise ValueError("metadata JSON must be an acquire_media source sidecar")
    info = metadata["source"]
    if info.get("platform") != "youtube" or info.get("canonical_url") != canonical_url:
        raise ValueError("cached metadata does not match the canonical YouTube URL")
    if info.get("availability") != "public" or info.get("live_status") != "not_live":
        raise ValueError("cached YouTube source must be public and not live")
    return info, resolved_paths[1].read_bytes(), resolved_paths[2].read_bytes()


def normalize_caption_text(event: dict[str, Any], *, field: str) -> str:
    segments = event.get("segs")
    if not isinstance(segments, list) or not segments:
        raise ValueError(f"{field}.segs must be a non-empty list")
    parts: list[str] = []
    for index, segment in enumerate(segments):
        if not isinstance(segment, dict) or not isinstance(segment.get("utf8"), str):
            raise ValueError(f"{field}.segs[{index}].utf8 must be text")
        parts.append(segment["utf8"])
    text = re.sub(r"\s+", " ", "".join(parts).replace("\u200b", " ")).strip()
    if not text:
        raise ValueError(f"{field} has no visible caption text")
    return text


def caption_segments(document: dict[str, Any], *, label: str) -> list[dict[str, Any]]:
    events = document.get("events")
    if not isinstance(events, list) or not events:
        raise ValueError(f"{label}.events must be a non-empty list")
    result: list[dict[str, Any]] = []
    previous_start = -1
    for index, event in enumerate(events):
        field = f"{label}.events[{index}]"
        if not isinstance(event, dict):
            raise ValueError(f"{field} must be an object")
        start_ms = event.get("tStartMs")
        duration_ms = event.get("dDurationMs")
        if (
            isinstance(start_ms, bool)
            or not isinstance(start_ms, int)
            or start_ms < 0
        ):
            raise ValueError(f"{field}.tStartMs must be a non-negative integer")
        if (
            isinstance(duration_ms, bool)
            or not isinstance(duration_ms, int)
            or duration_ms <= 0
        ):
            raise ValueError(f"{field}.dDurationMs must be a positive integer")
        if start_ms < previous_start:
            raise ValueError(f"{field}.tStartMs is not monotonic")
        previous_start = start_ms
        result.append(
            {
                "source_event_index": index,
                "start_ms": start_ms,
                "end_ms": start_ms + duration_ms,
                "text": normalize_caption_text(event, field=field),
            }
        )
    return result


def validate_aligned_translation(
    source: list[dict[str, Any]], translation: list[dict[str, Any]]
) -> None:
    if len(source) != len(translation):
        raise ValueError("source and translated captions must have the same event count")
    for index, (source_segment, translation_segment) in enumerate(zip(source, translation)):
        for key in ("source_event_index", "start_ms", "end_ms"):
            if source_segment[key] != translation_segment[key]:
                raise ValueError(
                    f"translated caption event {index} does not preserve source {key}"
                )


def format_timestamp(milliseconds: int) -> str:
    total_seconds = milliseconds // 1000
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    if hours > 99:
        raise ValueError("caption timestamp exceeds the two-digit-hour transcript contract")
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


def download_caption_payloads(
    canonical_url: str,
    *,
    source_language: str,
    translation_track: str,
    verbose: bool,
) -> tuple[dict[str, Any], bytes, bytes]:
    try:
        from yt_dlp import YoutubeDL
    except ImportError as error:
        raise SystemExit("yt-dlp is unavailable; install the project media extra") from error

    javascript_runtime = available_javascript_runtime()
    if javascript_runtime is None:
        raise SystemExit("Deno or Node.js is required for YouTube subtitle import")

    cache_root = ROOT / ".cache" / "youtube-subtitles"
    cache_root.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=cache_root) as directory:
        workdir = Path(directory)
        options: dict[str, Any] = {
            "cachedir": (ROOT / ".cache" / "yt-dlp").as_posix(),
            "js_runtimes": {javascript_runtime: {}},
            "noplaylist": True,
            "outtmpl": (workdir / "caption.%(ext)s").as_posix(),
            "quiet": not verbose,
            "skip_download": True,
            "subtitlesformat": "json3",
            "subtitleslangs": [source_language, translation_track],
            "writeautomaticsub": True,
            "writesubtitles": True,
        }
        with YoutubeDL(options) as downloader:
            extracted = downloader.extract_info(canonical_url, download=True)
        info = validate_extracted_info(extracted)
        subtitles = info.get("subtitles")
        automatic = info.get("automatic_captions")
        if not isinstance(subtitles, dict) or source_language not in subtitles:
            raise ValueError(f"YouTube has no publisher subtitle track {source_language!r}")
        if not isinstance(automatic, dict) or translation_track not in automatic:
            raise ValueError(
                f"YouTube has no aligned automatic translation track {translation_track!r}"
            )
        source_path = workdir / f"caption.{source_language}.json3"
        translation_path = workdir / f"caption.{translation_track}.json3"
        if not source_path.is_file() or not translation_path.is_file():
            raise FileNotFoundError("yt-dlp did not write both requested json3 caption tracks")
        return info, source_path.read_bytes(), translation_path.read_bytes()


def build_outputs(
    *,
    canonical_url: str,
    info: dict[str, Any],
    source_payload_bytes: bytes,
    translation_payload_bytes: bytes,
    title: str,
    generated_at: str,
    source_language: str,
    translation_track: str,
    raw_repository_path: str,
    transcript_repository_path: str,
    translation_repository_path: str,
) -> tuple[bytes, bytes, bytes, bytes]:
    source_payload = load_json3(source_payload_bytes, label="source caption")
    translation_payload = load_json3(
        translation_payload_bytes,
        label="translated caption",
    )
    source_segments = caption_segments(source_payload, label="source caption")
    translated_segments = caption_segments(translation_payload, label="translated caption")
    validate_aligned_translation(source_segments, translated_segments)
    source_transcript = transcript_bytes(title, source_segments)
    translated_transcript = transcript_bytes(title, translated_segments)

    video_id = info.get("id")
    channel_id = info.get("channel_id")
    if not isinstance(video_id, str) or re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id) is None:
        raise ValueError("YouTube metadata has no valid video ID")
    if (
        not isinstance(channel_id, str)
        or re.fullmatch(r"UC[A-Za-z0-9_-]{22}", channel_id) is None
    ):
        raise ValueError("YouTube metadata has no valid channel ID")

    raw_document = {
        "schema_version": 1,
        "kind": "podwiki-youtube-subtitle-raw",
        "generated_at": generated_at,
        "source": {
            "platform": "youtube",
            "canonical_url": canonical_url,
            "video_id": video_id,
            "channel_id": channel_id,
            "uploader": info.get("uploader"),
            "language": source_language,
            "track_type": "publisher-subtitle",
            "format": "json3",
            "payload_sha256": sha256_bytes(source_payload_bytes),
        },
        "payload": source_payload,
    }
    raw = json_bytes(raw_document)
    refined_document = {
        "schema_version": 1,
        "kind": "podwiki-youtube-subtitle-refined",
        "generated_at": generated_at,
        "source": {
            "raw_path": raw_repository_path,
            "raw_sha256": sha256_bytes(raw),
            "normalization": "youtube-json3-events-v1",
        },
        "segments": source_segments,
        "rendered_transcript": {
            "path": transcript_repository_path,
            "sha256": sha256_bytes(source_transcript),
        },
        "translation": {
            "language": "zh-CN",
            "source_track": translation_track,
            "track_type": "youtube-auto-translate",
            "payload_sha256": sha256_bytes(translation_payload_bytes),
            "event_count": len(translated_segments),
            "rendered_path": translation_repository_path,
            "rendered_sha256": sha256_bytes(translated_transcript),
        },
    }
    return raw, json_bytes(refined_document), source_transcript, translated_transcript


def main() -> int:
    args = parse_args()
    platform, canonical_url = canonical_source_url(args.url)
    if platform != "youtube":
        raise ValueError("caption import requires one canonical YouTube video")

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

    cached_paths = (args.metadata_json, args.source_json3, args.translation_json3)
    if any(path is not None for path in cached_paths) and not all(
        path is not None for path in cached_paths
    ):
        raise ValueError(
            "--metadata-json, --source-json3, and --translation-json3 must be provided together"
        )
    if all(path is not None for path in cached_paths):
        info, source_payload, translation_payload = load_cached_inputs(
            metadata_path=args.metadata_json,
            source_path=args.source_json3,
            translation_path=args.translation_json3,
            canonical_url=canonical_url,
        )
    else:
        info, source_payload, translation_payload = download_caption_payloads(
            canonical_url,
            source_language=args.source_language,
            translation_track=args.translation_track,
            verbose=args.verbose,
        )
    title = args.title or info.get("title")
    if not isinstance(title, str):
        raise ValueError("YouTube metadata has no title")
    generated_at = utc_now()
    run_dir = episode_dir / "asr" / args.run_id
    run_relative = run_dir.relative_to(ROOT).as_posix()
    translation_relative = (episode_dir / "transcript.zh-CN.md").relative_to(ROOT).as_posix()
    raw, refined, source_transcript, translated_transcript = build_outputs(
        canonical_url=canonical_url,
        info=info,
        source_payload_bytes=source_payload,
        translation_payload_bytes=translation_payload,
        title=title,
        generated_at=generated_at,
        source_language=args.source_language,
        translation_track=args.translation_track,
        raw_repository_path=f"{run_relative}/raw.json",
        transcript_repository_path=f"{run_relative}/transcript.en.md",
        translation_repository_path=translation_relative,
    )
    outputs = {
        run_dir / "raw.json": raw,
        run_dir / "refined.json": refined,
        run_dir / "transcript.en.md": source_transcript,
        episode_dir / "transcript.en.md": source_transcript,
        episode_dir / "transcript.zh-CN.md": translated_transcript,
    }
    for path, payload in outputs.items():
        write_atomically(path, payload, overwrite=args.overwrite)

    refined_document = json.loads(refined)
    refined_segments = refined_document.get("segments")
    translation_document = refined_document.get("translation")
    source_segment_count = len(refined_segments) if isinstance(refined_segments, list) else 0
    translation_segment_count = (
        translation_document.get("event_count")
        if isinstance(translation_document, dict)
        else 0
    )
    print(
        json.dumps(
            {
                "canonical_url": canonical_url,
                "video_id": info.get("id"),
                "channel_id": info.get("channel_id"),
                "generated_at": generated_at,
                "source_segments": source_segment_count,
                "translation_segments": translation_segment_count,
                "outputs": [path.relative_to(ROOT).as_posix() for path in outputs],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
