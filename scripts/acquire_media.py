#!/usr/bin/env python3
"""Acquire one public podcast video as a local audio file with yt-dlp."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse
from urllib.error import URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
BILIBILI_VIDEO_RE = re.compile(r"^/video/(BV[A-Za-z0-9]+)/?$")
YOUTUBE_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Download one public Bilibili or YouTube video as audio and save "
            "reproducible source metadata."
        )
    )
    parser.add_argument("--url", required=True)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--metadata-output", type=Path)
    parser.add_argument(
        "--metadata-only",
        action="store_true",
        help="Inspect the source without downloading media",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace an existing local audio file",
    )
    parser.add_argument(
        "--verbose",
        action=argparse.BooleanOptionalAction,
        default=True,
    )
    return parser.parse_args()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def canonical_source_url(url: str) -> tuple[str, str]:
    parsed = urlparse(url.strip())
    hostname = (parsed.hostname or "").lower()

    if hostname == "bilibili.com" or hostname.endswith(".bilibili.com"):
        match = BILIBILI_VIDEO_RE.fullmatch(parsed.path)
        if match is None:
            raise ValueError("Bilibili URL must point to one /video/BV... page")
        page_values = parse_qs(parsed.query).get("p", ["1"])
        if len(page_values) != 1 or page_values[0] != "1":
            raise ValueError("only page 1 of a Bilibili video is supported")
        return "bilibili", f"https://www.bilibili.com/video/{match.group(1)}/"

    if hostname in {"youtube.com", "www.youtube.com", "m.youtube.com"}:
        video_id = parse_qs(parsed.query).get("v", [""])[0]
        if parsed.path != "/watch" or not YOUTUBE_ID_RE.fullmatch(video_id):
            raise ValueError("YouTube URL must point to one /watch?v=... video")
        return "youtube", f"https://www.youtube.com/watch?v={video_id}"

    if hostname == "youtu.be":
        video_id = parsed.path.strip("/")
        if not YOUTUBE_ID_RE.fullmatch(video_id):
            raise ValueError("youtu.be URL must contain one valid video ID")
        return "youtube", f"https://www.youtube.com/watch?v={video_id}"

    raise ValueError("only public Bilibili and YouTube video URLs are supported")


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
            json.dump(document, stream, ensure_ascii=False, indent=2, allow_nan=False)
            stream.write("\n")
            temporary_path = Path(stream.name)
        temporary_path.replace(path)
        temporary_path = None
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def compact_chapters(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []
    return [
        {
            "start_time": chapter.get("start_time"),
            "end_time": chapter.get("end_time"),
            "title": chapter.get("title"),
        }
        for chapter in value
        if isinstance(chapter, dict)
    ]


def fetch_bilibili_api(path: str, parameters: str) -> dict[str, Any]:
    request = Request(
        f"https://api.bilibili.com{path}?{parameters}",
        headers={
            "Accept": "application/json",
            "Referer": "https://www.bilibili.com/",
            "User-Agent": "Mozilla/5.0 PodWiki/0.1",
        },
    )
    document: dict[str, Any] | None = None
    last_error: Exception | None = None
    for attempt in range(4):
        try:
            with urlopen(request, timeout=60) as response:
                candidate = json.load(response)
            if not isinstance(candidate, dict):
                raise ValueError(f"Bilibili API {path} returned invalid JSON")
            document = candidate
            break
        except (TimeoutError, URLError, OSError) as error:
            last_error = error
            if attempt == 3:
                break
            time.sleep(2**attempt)
    if document is None:
        raise ConnectionError(f"Bilibili API {path} failed after retries") from last_error
    if document.get("code") != 0 or not isinstance(document.get("data"), dict):
        raise ValueError(
            f"Bilibili API {path} failed with code {document.get('code')!r}"
        )
    return document["data"]


def bilibili_platform_metadata(bvid: str) -> dict[str, Any]:
    view = fetch_bilibili_api("/x/web-interface/view", f"bvid={bvid}")
    pages = view.get("pages")
    if not isinstance(pages, list) or len(pages) != 1:
        raise ValueError("only single-page Bilibili videos are supported")
    page = pages[0]
    if not isinstance(page, dict):
        raise ValueError("Bilibili view API returned invalid page metadata")
    cid = page.get("cid")
    if not isinstance(cid, int):
        raise ValueError("Bilibili view API did not return a numeric cid")
    player = fetch_bilibili_api("/x/player/v2", f"bvid={bvid}&cid={cid}")
    subtitle = player.get("subtitle")
    subtitle = subtitle if isinstance(subtitle, dict) else {}
    tracks = subtitle.get("subtitles")
    tracks = tracks if isinstance(tracks, list) else []
    owner = view.get("owner")
    owner = owner if isinstance(owner, dict) else {}
    rights = view.get("rights")
    rights = rights if isinstance(rights, dict) else {}
    return {
        "aid": view.get("aid"),
        "bvid": view.get("bvid") or bvid,
        "cid": cid,
        "page": page.get("page") or 1,
        "part": page.get("part"),
        "published_timestamp": view.get("pubdate"),
        "created_timestamp": view.get("ctime"),
        "duration_seconds": view.get("duration"),
        "owner": {"id": owner.get("mid"), "name": owner.get("name")},
        "rights": {
            "download": rights.get("download"),
            "no_reprint": rights.get("no_reprint"),
            "pay": rights.get("pay"),
            "ugc_pay": rights.get("ugc_pay"),
            "is_cooperation": rights.get("is_cooperation"),
            "is_chargeable_season": view.get("is_chargeable_season"),
            "is_upower_exclusive": view.get("is_upower_exclusive"),
        },
        "subtitle": {
            "need_login": (
                subtitle.get("need_login_subtitle")
                if subtitle.get("need_login_subtitle") is not None
                else player.get("need_login_subtitle")
            ),
            "tracks": [
                {
                    "id": track.get("id"),
                    "language": track.get("lan"),
                    "language_label": track.get("lan_doc"),
                }
                for track in tracks
                if isinstance(track, dict)
            ],
        },
    }


def source_metadata(
    info: dict[str, Any],
    *,
    platform: str,
    canonical_url: str,
    platform_metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    platform_metadata = platform_metadata or {}
    subtitles = info.get("subtitles")
    automatic_captions = info.get("automatic_captions")
    subtitle_languages = sorted(
        language
        for language in subtitles
        if language.lower() not in {"danmaku", "comments", "live_chat"}
    ) if isinstance(subtitles, dict) else []
    comment_stream_languages = sorted(
        language
        for language in subtitles
        if language.lower() in {"danmaku", "comments", "live_chat"}
    ) if isinstance(subtitles, dict) else []
    return {
        "platform": platform,
        "canonical_url": canonical_url,
        "id": info.get("id"),
        "display_id": info.get("display_id"),
        "bvid": platform_metadata.get("bvid") or info.get("bvid") or (
            info.get("id") if platform == "bilibili" else None
        ),
        "aid": platform_metadata.get("aid") or info.get("aid"),
        "cid": platform_metadata.get("cid") or info.get("cid"),
        "page": (
            platform_metadata.get("page")
            or info.get("page")
            or info.get("playlist_index")
            or 1
        ),
        "title": info.get("title"),
        "description": info.get("description"),
        "uploader": info.get("uploader"),
        "uploader_id": info.get("uploader_id"),
        "channel": info.get("channel"),
        "channel_id": info.get("channel_id"),
        "timestamp": info.get("timestamp"),
        "release_timestamp": info.get("release_timestamp"),
        "duration_seconds": info.get("duration"),
        "language": info.get("language"),
        "extractor": info.get("extractor"),
        "extractor_key": info.get("extractor_key"),
        "availability": info.get("availability"),
        "live_status": info.get("live_status"),
        "subtitle_languages": subtitle_languages,
        "comment_stream_languages": comment_stream_languages,
        "automatic_caption_languages": (
            sorted(automatic_captions)
            if isinstance(automatic_captions, dict)
            else []
        ),
        "chapters": compact_chapters(info.get("chapters")),
        "platform_metadata": platform_metadata,
    }


def validate_extracted_info(info: Any) -> dict[str, Any]:
    if not isinstance(info, dict):
        raise ValueError("yt-dlp returned unexpected source metadata")
    if info.get("is_live") or info.get("live_status") in {
        "is_live",
        "is_upcoming",
    }:
        raise PermissionError("live or upcoming media is unsupported")
    if info.get("availability") in {
        "private",
        "premium_only",
        "subscriber_only",
        "needs_auth",
    }:
        raise PermissionError(
            f"access-controlled media is unsupported: {info.get('availability')}"
        )
    duration = info.get("duration")
    if not isinstance(duration, (int, float)) or duration <= 0:
        raise ValueError("source metadata has no positive duration")
    return info


def validate_media_duration(
    media: dict[str, Any],
    *,
    info: dict[str, Any],
    platform_metadata: dict[str, Any],
) -> None:
    expected_seconds = platform_metadata.get("duration_seconds") or info.get("duration")
    if not isinstance(expected_seconds, (int, float)) or expected_seconds <= 0:
        raise ValueError("cannot validate media without a positive source duration")
    actual_ms = media.get("duration_ms")
    if not isinstance(actual_ms, int):
        raise ValueError("media probe has no integer duration_ms")
    expected_ms = round(float(expected_seconds) * 1000)
    tolerance_ms = max(5000, round(expected_ms * 0.005))
    if abs(actual_ms - expected_ms) > tolerance_ms:
        raise ValueError(
            "downloaded audio duration differs from the source: "
            f"expected={expected_ms}ms actual={actual_ms}ms"
        )


def available_javascript_runtime() -> str | None:
    for runtime in ("deno", "node"):
        if shutil.which(runtime) is not None:
            return runtime
    return None


def yt_dlp_access_filter(
    info: dict[str, Any], *, incomplete: bool = False
) -> str | None:
    if incomplete:
        return None
    try:
        validate_extracted_info(info)
    except (PermissionError, ValueError) as error:
        return str(error)
    return None


def probe_audio(path: Path) -> dict[str, Any]:
    ffprobe = shutil.which("ffprobe")
    if ffprobe is None:
        raise SystemExit("ffprobe is required to validate downloaded audio")
    completed = subprocess.run(
        [
            ffprobe,
            "-v",
            "error",
            "-show_entries",
            "format=duration,size:stream=codec_type,codec_name,sample_rate,channels",
            "-of",
            "json",
            path.as_posix(),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    document = json.loads(completed.stdout)
    audio_streams = [
        stream
        for stream in document.get("streams", [])
        if stream.get("codec_type") == "audio"
    ]
    if not audio_streams:
        raise ValueError(f"downloaded file has no audio stream: {path}")
    stream = audio_streams[0]
    format_info = document.get("format", {})
    digest = hashlib.sha256()
    with path.open("rb") as stream_reader:
        for chunk in iter(lambda: stream_reader.read(1024 * 1024), b""):
            digest.update(chunk)
    return {
        "path": path.as_posix(),
        "size_bytes": int(format_info["size"]),
        "duration_ms": round(float(format_info["duration"]) * 1000),
        "codec": stream.get("codec_name"),
        "sample_rate_hz": int(stream["sample_rate"]),
        "channels": int(stream["channels"]),
        "sha256": digest.hexdigest(),
    }


def validate_reusable_media(
    *, output_path: Path, metadata_output: Path, canonical_url: str
) -> None:
    if not metadata_output.is_file():
        raise FileExistsError(
            f"audio already exists without identity metadata: {output_path}; "
            "use --overwrite to replace it"
        )
    existing = json.loads(metadata_output.read_text(encoding="utf-8"))
    existing_source = existing.get("source")
    existing_media = existing.get("media")
    if not isinstance(existing_source, dict) or not isinstance(existing_media, dict):
        raise ValueError(f"invalid existing media metadata: {metadata_output}")
    if existing_source.get("canonical_url") != canonical_url:
        raise FileExistsError(
            f"audio belongs to {existing_source.get('canonical_url')!r}, "
            f"not {canonical_url!r}; use --overwrite to replace it"
        )
    expected_hash = existing_media.get("sha256")
    if not isinstance(expected_hash, str):
        raise ValueError(
            f"existing media metadata has no sha256: {metadata_output}; "
            "use --overwrite to recreate it"
        )
    digest = hashlib.sha256()
    with output_path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    if digest.hexdigest() != expected_hash:
        raise ValueError(f"existing audio hash does not match {metadata_output}")


def read_existing_metadata(
    *, metadata_output: Path, canonical_url: str, allow_replacement: bool
) -> dict[str, Any] | None:
    if not metadata_output.is_file():
        return None
    existing = json.loads(metadata_output.read_text(encoding="utf-8"))
    if not isinstance(existing, dict):
        raise ValueError(f"invalid existing media metadata: {metadata_output}")
    existing_source = existing.get("source")
    existing_url = (
        existing_source.get("canonical_url")
        if isinstance(existing_source, dict)
        else None
    )
    if existing_url != canonical_url and not allow_replacement:
        raise FileExistsError(
            f"metadata belongs to {existing_url!r}, not {canonical_url!r}; "
            "choose another output or use --overwrite"
        )
    return existing


def retain_existing_media(
    document: dict[str, Any], existing_document: dict[str, Any] | None
) -> None:
    if not isinstance(existing_document, dict):
        return
    existing_media = existing_document.get("media")
    if not isinstance(existing_media, dict):
        return
    document["media"] = existing_media
    if existing_document.get("acquired_at") is not None:
        document["acquired_at"] = existing_document["acquired_at"]


def main() -> int:
    args = parse_args()
    platform, canonical_url = canonical_source_url(args.url)
    platform_metadata = (
        bilibili_platform_metadata(
            BILIBILI_VIDEO_RE.fullmatch(urlparse(canonical_url).path).group(1)  # type: ignore[union-attr]
        )
        if platform == "bilibili"
        else {}
    )
    rights = platform_metadata.get("rights")
    if isinstance(rights, dict) and any(
        rights.get(key)
        for key in (
            "pay",
            "ugc_pay",
            "is_chargeable_season",
            "is_upower_exclusive",
        )
    ):
        raise PermissionError("paid or access-controlled Bilibili media is unsupported")
    output_path = args.output.resolve()
    metadata_output = (
        args.metadata_output.resolve()
        if args.metadata_output is not None
        else output_path.with_name(f"{output_path.stem}.metadata.json")
    )
    if output_path.suffix.lower() != ".m4a":
        raise ValueError("output path must end in .m4a")
    if metadata_output == output_path:
        raise ValueError("metadata output must not overwrite the audio output")
    if args.metadata_only and args.overwrite:
        raise ValueError("--overwrite cannot be combined with --metadata-only")
    existing_document = read_existing_metadata(
        metadata_output=metadata_output,
        canonical_url=canonical_url,
        allow_replacement=args.overwrite,
    )

    try:
        from yt_dlp import YoutubeDL
        from yt_dlp.utils import DownloadError
    except ImportError as error:
        raise SystemExit(
            "yt-dlp is unavailable; run `uv sync --all-groups` before workers"
        ) from error

    output_path.parent.mkdir(parents=True, exist_ok=True)
    media_reused = not args.metadata_only and output_path.exists() and not args.overwrite
    if media_reused:
        validate_reusable_media(
            output_path=output_path,
            metadata_output=metadata_output,
            canonical_url=canonical_url,
        )
    download_requested = not args.metadata_only and (args.overwrite or not output_path.exists())
    if download_requested:
        if shutil.which("ffmpeg") is None:
            raise SystemExit("ffmpeg is required to extract downloaded audio")
        if shutil.which("ffprobe") is None:
            raise SystemExit("ffprobe is required to validate downloaded audio")
    staging_directory: Path | None = None
    download_output = output_path
    if download_requested:
        source_id = (
            platform_metadata.get("bvid")
            if platform == "bilibili"
            else parse_qs(urlparse(canonical_url).query)["v"][0]
        )
        staging_directory = output_path.parent / ".downloads" / str(source_id)
        staging_directory.mkdir(parents=True, exist_ok=True)
        download_output = staging_directory / output_path.name
    output_template = download_output.with_suffix(".%(ext)s").as_posix()
    options: dict[str, Any] = {
        "cachedir": (ROOT / ".cache" / "yt-dlp").as_posix(),
        "format": "bestaudio/best",
        "noplaylist": True,
        "outtmpl": output_template,
        "overwrites": True,
        "continuedl": True,
        "socket_timeout": 60,
        "retries": 10,
        "fragment_retries": 10,
        "extractor_retries": 5,
        "file_access_retries": 3,
        "match_filter": yt_dlp_access_filter,
        "quiet": not args.verbose,
        "no_warnings": False,
    }
    if platform == "youtube":
        javascript_runtime = available_javascript_runtime()
        if javascript_runtime is None:
            raise SystemExit("Deno or Node.js is required for full YouTube support")
        options["js_runtimes"] = {javascript_runtime: {}}
    if download_requested:
        options["postprocessors"] = [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "m4a",
                "preferredquality": "0",
            }
        ]

    downloaded_media: dict[str, Any] | None = None
    last_download_error: Exception | None = None
    info: dict[str, Any] | None = None
    for attempt in range(5):
        try:
            with YoutubeDL(options) as downloader:
                info = validate_extracted_info(
                    downloader.extract_info(
                        canonical_url,
                        download=download_requested,
                    )
                )
            break
        except DownloadError as error:
            last_download_error = error
            if attempt == 4:
                break
            time.sleep(2**attempt)
    if info is None:
        raise ConnectionError("yt-dlp failed after extractor retries") from last_download_error
    if download_requested:
        if not download_output.is_file():
            raise FileNotFoundError(
                f"yt-dlp did not produce expected staging output: {download_output}"
            )
        downloaded_media = probe_audio(download_output)
        validate_media_duration(
            downloaded_media,
            info=info,
            platform_metadata=platform_metadata,
        )
        download_output.replace(output_path)
        downloaded_media["path"] = output_path.as_posix()
        if staging_directory is not None:
            try:
                staging_directory.rmdir()
                staging_directory.parent.rmdir()
            except OSError:
                pass
    inspected_at = utc_now()
    document: dict[str, Any] = {
        "schema_version": 1,
        "kind": "podwiki-source-media",
        "inspected_at": inspected_at,
        "source": source_metadata(
            info,
            platform=platform,
            canonical_url=canonical_url,
            platform_metadata=platform_metadata,
        ),
        "download_requested": download_requested,
        "media_reused": media_reused,
    }
    if args.metadata_only:
        retain_existing_media(document, existing_document)
    if not args.metadata_only:
        if not output_path.is_file():
            raise FileNotFoundError(f"yt-dlp did not produce expected output: {output_path}")
        media = downloaded_media or probe_audio(output_path)
        validate_media_duration(
            media,
            info=info,
            platform_metadata=platform_metadata,
        )
        document["media"] = media
        document["verified_at"] = inspected_at
        document["acquired_at"] = (
            inspected_at
            if download_requested
            else (
                existing_document.get("acquired_at") or inspected_at
                if isinstance(existing_document, dict)
                else inspected_at
            )
        )

    write_json_atomically(metadata_output, document)
    print(json.dumps(document, ensure_ascii=False, indent=2, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
