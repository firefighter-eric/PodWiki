#!/usr/bin/env python3
"""Acquire one public podcast episode or video as a verified local audio file."""

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
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.error import URLError
from urllib.parse import parse_qs, urlparse
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
BILIBILI_VIDEO_RE = re.compile(r"^/video/(BV[A-Za-z0-9]+)/?$")
YOUTUBE_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")
XIAOYUZHOU_ID_RE = re.compile(r"^[0-9a-f]{24}$")
XIAOYUZHOU_EPISODE_RE = re.compile(r"^/episode/([0-9a-f]{24})/?$")
XIAOYUZHOU_MAX_PAGE_BYTES = 16 * 1024 * 1024
BILIBILI_PUBLIC_ACCESS_FLAGS = (
    "pay",
    "ugc_pay",
    "ugc_pay_preview",
    "arc_pay",
    "is_chargeable_season",
    "is_upower_exclusive",
    "is_upower_play",
)
BILIBILI_EXTRACTOR_FALLBACK_MARKERS = (
    "Unable to extract initial state",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Download one public Bilibili or YouTube video, or one public "
            "Xiaoyuzhou episode, as audio and save reproducible source metadata."
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

    if hostname in {"xiaoyuzhoufm.com", "www.xiaoyuzhoufm.com"}:
        match = XIAOYUZHOU_EPISODE_RE.fullmatch(parsed.path)
        if match is None:
            raise ValueError(
                "Xiaoyuzhou URL must point to one /episode/<episode-id> page"
            )
        return (
            "xiaoyuzhou",
            f"https://www.xiaoyuzhoufm.com/episode/{match.group(1)}",
        )

    raise ValueError(
        "only public Bilibili and YouTube videos or Xiaoyuzhou episodes are supported"
    )


class XiaoyuzhouNextDataParser(HTMLParser):
    """Extract the public Next.js data document without executing page scripts."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self._capturing = False
        self._chunks: list[str] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        attributes = dict(attrs)
        if tag == "script" and attributes.get("id") == "__NEXT_DATA__":
            self._capturing = True

    def handle_data(self, data: str) -> None:
        if self._capturing:
            self._chunks.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._capturing:
            self._capturing = False

    @property
    def document_text(self) -> str:
        return "".join(self._chunks)


def extract_xiaoyuzhou_next_data(page_html: str) -> dict[str, Any]:
    parser = XiaoyuzhouNextDataParser()
    parser.feed(page_html)
    document_text = parser.document_text
    if not document_text:
        raise ValueError("Xiaoyuzhou page has no __NEXT_DATA__ document")
    document = json.loads(document_text)
    if not isinstance(document, dict):
        raise ValueError("Xiaoyuzhou __NEXT_DATA__ is not an object")
    return document


def fetch_xiaoyuzhou_next_data(episode_id: str) -> dict[str, Any]:
    if not XIAOYUZHOU_ID_RE.fullmatch(episode_id):
        raise ValueError("invalid Xiaoyuzhou episode ID")
    canonical_url = f"https://www.xiaoyuzhoufm.com/episode/{episode_id}"
    request = Request(
        canonical_url,
        headers={
            "Accept": "text/html,application/xhtml+xml",
            "User-Agent": "Mozilla/5.0 PodWiki/0.1",
        },
    )
    page_bytes: bytes | None = None
    last_error: Exception | None = None
    for attempt in range(4):
        try:
            with urlopen(request, timeout=60) as response:
                page_bytes = response.read(XIAOYUZHOU_MAX_PAGE_BYTES + 1)
            break
        except (TimeoutError, URLError, OSError) as error:
            last_error = error
            if attempt == 3:
                break
            time.sleep(2**attempt)
    if page_bytes is None:
        raise ConnectionError(
            "Xiaoyuzhou episode page failed after retries"
        ) from last_error
    if len(page_bytes) > XIAOYUZHOU_MAX_PAGE_BYTES:
        raise ValueError("Xiaoyuzhou episode page exceeds the safe size limit")
    return extract_xiaoyuzhou_next_data(page_bytes.decode("utf-8"))


def rfc3339_timestamp(value: Any, *, field: str) -> int:
    if not isinstance(value, str) or not value:
        raise ValueError(f"Xiaoyuzhou metadata has no {field}")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise ValueError(f"Xiaoyuzhou metadata has invalid {field}") from error
    if parsed.tzinfo is None:
        raise ValueError(f"Xiaoyuzhou metadata {field} has no timezone")
    return int(parsed.timestamp())


def parse_xiaoyuzhou_episode_metadata(
    document: dict[str, Any], expected_episode_id: str
) -> dict[str, Any]:
    props = document.get("props")
    props = props if isinstance(props, dict) else {}
    page_props = props.get("pageProps")
    page_props = page_props if isinstance(page_props, dict) else {}
    episode = page_props.get("episode")
    if not isinstance(episode, dict) or episode.get("type") != "EPISODE":
        raise ValueError("Xiaoyuzhou page has no episode metadata")

    episode_id = episode.get("eid")
    if episode_id != expected_episode_id:
        raise ValueError(
            "Xiaoyuzhou requested/episode eid mismatch: "
            f"requested={expected_episode_id} actual={episode_id}"
        )
    if not isinstance(episode_id, str) or not XIAOYUZHOU_ID_RE.fullmatch(
        episode_id
    ):
        raise ValueError("Xiaoyuzhou episode metadata has no stable eid")

    podcast_id = episode.get("pid")
    if not isinstance(podcast_id, str) or not XIAOYUZHOU_ID_RE.fullmatch(
        podcast_id
    ):
        raise ValueError("Xiaoyuzhou episode metadata has no stable pid")
    podcast = episode.get("podcast")
    if not isinstance(podcast, dict):
        raise ValueError("Xiaoyuzhou episode metadata has no podcast identity")
    if podcast.get("pid") != podcast_id:
        raise ValueError(
            "Xiaoyuzhou episode/podcast pid mismatch: "
            f"episode={podcast_id} podcast={podcast.get('pid')}"
        )

    media = episode.get("media")
    media = media if isinstance(media, dict) else {}
    media_source = media.get("source")
    media_source = media_source if isinstance(media_source, dict) else {}
    enclosure = episode.get("enclosure")
    enclosure = enclosure if isinstance(enclosure, dict) else {}
    media_key = episode.get("mediaKey")
    media_id = media.get("id")
    if not isinstance(media_key, str) or not media_key:
        raise ValueError("Xiaoyuzhou episode metadata has no mediaKey")
    if media_id != media_key:
        raise ValueError(
            "Xiaoyuzhou media id/mediaKey mismatch: "
            f"media={media_id} mediaKey={media_key}"
        )

    title = episode.get("title")
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Xiaoyuzhou episode metadata has no title")
    published_at = episode.get("pubDate")
    published_timestamp = rfc3339_timestamp(published_at, field="pubDate")

    return {
        "eid": episode_id,
        "pid": podcast_id,
        "title": title,
        "description": episode.get("description"),
        "published_at": published_at,
        "published_timestamp": published_timestamp,
        "duration_seconds": episode.get("duration"),
        "status": episode.get("status"),
        "pay_type": episode.get("payType"),
        "is_private_media": episode.get("isPrivateMedia"),
        "podcast": {
            "id": podcast_id,
            "title": podcast.get("title"),
            "author": podcast.get("author"),
        },
        "media": {
            "id": media_id,
            "size_bytes": media.get("size"),
            "mime_type": media.get("mimeType"),
            "mode": media_source.get("mode"),
            "url": media_source.get("url"),
        },
        "enclosure_url": enclosure.get("url"),
    }


def validate_xiaoyuzhou_public_access(
    platform_metadata: dict[str, Any],
) -> None:
    """Fail closed unless the public page explicitly exposes a free enclosure."""
    if platform_metadata.get("status") != "NORMAL":
        raise PermissionError("unavailable Xiaoyuzhou media is unsupported")
    if platform_metadata.get("pay_type") != "FREE":
        raise PermissionError("paid Xiaoyuzhou media is unsupported")
    if platform_metadata.get("is_private_media") is not False:
        raise PermissionError("private Xiaoyuzhou media is unsupported")

    duration = platform_metadata.get("duration_seconds")
    if isinstance(duration, bool) or not isinstance(duration, (int, float)):
        raise ValueError("Xiaoyuzhou metadata has no numeric duration")
    if duration <= 0:
        raise ValueError("Xiaoyuzhou metadata has no positive duration")

    media = platform_metadata.get("media")
    if not isinstance(media, dict):
        raise PermissionError("Xiaoyuzhou public media metadata is missing")
    if media.get("mode") != "PUBLIC":
        raise PermissionError("non-public Xiaoyuzhou media is unsupported")
    media_url = media.get("url")
    if not isinstance(media_url, str) or not media_url:
        raise PermissionError("Xiaoyuzhou public media URL is missing")
    parsed_media_url = urlparse(media_url)
    if (
        parsed_media_url.scheme != "https"
        or parsed_media_url.netloc != "media.xyzcdn.net"
        or parsed_media_url.username is not None
        or parsed_media_url.password is not None
        or not parsed_media_url.path.endswith(".m4a")
        or bool(parsed_media_url.query)
        or bool(parsed_media_url.fragment)
    ):
        raise PermissionError("Xiaoyuzhou media URL is not an approved public CDN URL")
    if platform_metadata.get("enclosure_url") != media_url:
        raise ValueError("Xiaoyuzhou public media/enclosure URL mismatch")

    size_bytes = media.get("size_bytes")
    if isinstance(size_bytes, bool) or not isinstance(size_bytes, int):
        raise ValueError("Xiaoyuzhou public media size is missing")
    if size_bytes <= 0:
        raise ValueError("Xiaoyuzhou public media size is not positive")
    if media.get("mime_type") not in {"audio/mp4", "audio/m4a", "audio/x-m4a"}:
        raise ValueError("Xiaoyuzhou public media is not an M4A audio resource")


def xiaoyuzhou_platform_metadata(episode_id: str) -> dict[str, Any]:
    metadata = parse_xiaoyuzhou_episode_metadata(
        fetch_xiaoyuzhou_next_data(episode_id), episode_id
    )
    validate_xiaoyuzhou_public_access(metadata)
    return metadata


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


def bilibili_api_integer(value: Any, *, field: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"Bilibili API returned no numeric {field}")
    return value


def validate_bilibili_public_access(platform_metadata: dict[str, Any]) -> None:
    """Fail closed unless the anonymous APIs explicitly describe public media."""
    state = platform_metadata.get("state")
    if isinstance(state, bool) or not isinstance(state, int):
        raise PermissionError("Bilibili availability state is missing or invalid")
    if state != 0:
        raise PermissionError("unavailable Bilibili media is unsupported")

    rights = platform_metadata.get("rights")
    if not isinstance(rights, dict):
        raise PermissionError("Bilibili access metadata is missing")
    for field in BILIBILI_PUBLIC_ACCESS_FLAGS:
        if field not in rights:
            raise PermissionError(f"Bilibili access flag {field} is missing")
        value = rights[field]
        if isinstance(value, bool):
            blocked = value
        elif isinstance(value, int):
            blocked = value != 0
        else:
            raise PermissionError(
                f"Bilibili access flag {field} is not explicitly public"
            )
        if blocked:
            raise PermissionError(
                f"paid or access-controlled Bilibili media is unsupported: {field}"
            )


def is_bilibili_extractor_compatibility_error(error: Exception | None) -> bool:
    """Limit the API fallback to known public-page extractor compatibility errors."""
    if error is None:
        return False
    message = str(error)
    return any(marker in message for marker in BILIBILI_EXTRACTOR_FALLBACK_MARKERS)


def bilibili_platform_metadata(bvid: str) -> dict[str, Any]:
    view = fetch_bilibili_api("/x/web-interface/view", f"bvid={bvid}")
    view_bvid = view.get("bvid")
    if not isinstance(view_bvid, str):
        raise ValueError("Bilibili view API returned no BVID")
    if view_bvid != bvid:
        raise ValueError(
            f"Bilibili view API BVID mismatch: requested={bvid} actual={view_bvid}"
        )
    aid = bilibili_api_integer(view.get("aid"), field="view aid")
    view_cid = bilibili_api_integer(view.get("cid"), field="view cid")
    pages = view.get("pages")
    if not isinstance(pages, list) or len(pages) != 1:
        raise ValueError("only single-page Bilibili videos are supported")
    page = pages[0]
    if not isinstance(page, dict):
        raise ValueError("Bilibili view API returned invalid page metadata")
    page_number = bilibili_api_integer(page.get("page"), field="page number")
    if page_number != 1:
        raise ValueError("only page 1 of a Bilibili video is supported")
    page_cid = bilibili_api_integer(page.get("cid"), field="page cid")
    if page_cid != view_cid:
        raise ValueError(
            f"Bilibili view/page cid mismatch: view={view_cid} page={page_cid}"
        )

    player = fetch_bilibili_api("/x/player/v2", f"bvid={bvid}&cid={view_cid}")
    player_bvid = player.get("bvid")
    player_aid = bilibili_api_integer(player.get("aid"), field="player aid")
    player_cid = bilibili_api_integer(player.get("cid"), field="player cid")
    if player_bvid != bvid:
        raise ValueError(
            f"Bilibili player API BVID mismatch: expected={bvid} actual={player_bvid}"
        )
    if player_aid != aid:
        raise ValueError(
            f"Bilibili view/player aid mismatch: view={aid} player={player_aid}"
        )
    if player_cid != view_cid:
        raise ValueError(
            f"Bilibili view/player cid mismatch: view={view_cid} player={player_cid}"
        )
    subtitle = player.get("subtitle")
    subtitle = subtitle if isinstance(subtitle, dict) else {}
    tracks = subtitle.get("subtitles")
    tracks = tracks if isinstance(tracks, list) else []
    owner = view.get("owner")
    owner = owner if isinstance(owner, dict) else {}
    rights = view.get("rights")
    rights = rights if isinstance(rights, dict) else {}
    view_points = player.get("view_points")
    view_points = view_points if isinstance(view_points, list) else []
    return {
        "aid": aid,
        "bvid": view_bvid,
        "cid": view_cid,
        "page": page_number,
        "part": page.get("part"),
        "title": view.get("title"),
        "description": view.get("desc"),
        "state": view.get("state"),
        "published_timestamp": view.get("pubdate"),
        "created_timestamp": view.get("ctime"),
        "duration_seconds": view.get("duration"),
        "owner": {"id": owner.get("mid"), "name": owner.get("name")},
        "rights": {
            "download": rights.get("download"),
            "no_reprint": rights.get("no_reprint"),
            "pay": rights.get("pay"),
            "ugc_pay": rights.get("ugc_pay"),
            "ugc_pay_preview": rights.get("ugc_pay_preview"),
            "arc_pay": rights.get("arc_pay"),
            "is_cooperation": rights.get("is_cooperation"),
            "is_chargeable_season": view.get("is_chargeable_season"),
            "is_upower_exclusive": view.get("is_upower_exclusive"),
            "is_upower_play": view.get("is_upower_play"),
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
        "chapters": [
            {
                "start_time": point.get("from"),
                "end_time": point.get("to"),
                "title": point.get("content"),
            }
            for point in view_points
            if isinstance(point, dict)
        ],
    }


def bilibili_api_info(platform_metadata: dict[str, Any]) -> dict[str, Any]:
    """Build the yt-dlp-compatible metadata subset from public Bilibili APIs."""
    owner = platform_metadata.get("owner")
    owner = owner if isinstance(owner, dict) else {}
    subtitle = platform_metadata.get("subtitle")
    subtitle = subtitle if isinstance(subtitle, dict) else {}
    tracks = subtitle.get("tracks")
    tracks = tracks if isinstance(tracks, list) else []
    subtitles = {
        str(track["language"]): []
        for track in tracks
        if isinstance(track, dict) and track.get("language")
    }
    return validate_extracted_info(
        {
            "id": platform_metadata.get("bvid"),
            "display_id": platform_metadata.get("bvid"),
            "bvid": platform_metadata.get("bvid"),
            "aid": platform_metadata.get("aid"),
            "cid": platform_metadata.get("cid"),
            "page": platform_metadata.get("page") or 1,
            "title": platform_metadata.get("title") or platform_metadata.get("part"),
            "description": platform_metadata.get("description"),
            "uploader": owner.get("name"),
            "uploader_id": (
                str(owner["id"]) if owner.get("id") is not None else None
            ),
            "timestamp": platform_metadata.get("published_timestamp"),
            "duration": platform_metadata.get("duration_seconds"),
            "extractor": "BiliBiliPublicAPI",
            "extractor_key": "BiliBiliPublicAPI",
            "availability": None,
            "live_status": None,
            "subtitles": subtitles,
            "automatic_captions": {},
            "chapters": platform_metadata.get("chapters") or [],
        }
    )


def xiaoyuzhou_api_info(platform_metadata: dict[str, Any]) -> dict[str, Any]:
    """Build the common source metadata subset from a public episode page."""
    validate_xiaoyuzhou_public_access(platform_metadata)
    podcast = platform_metadata.get("podcast")
    podcast = podcast if isinstance(podcast, dict) else {}
    return validate_extracted_info(
        {
            "id": platform_metadata.get("eid"),
            "display_id": platform_metadata.get("eid"),
            "eid": platform_metadata.get("eid"),
            "pid": platform_metadata.get("pid"),
            "title": platform_metadata.get("title"),
            "description": platform_metadata.get("description"),
            "uploader": podcast.get("author"),
            "uploader_id": platform_metadata.get("pid"),
            "channel": podcast.get("title"),
            "channel_id": platform_metadata.get("pid"),
            "timestamp": platform_metadata.get("published_timestamp"),
            "duration": platform_metadata.get("duration_seconds"),
            "extractor": "XiaoyuzhouPublicPage",
            "extractor_key": "XiaoyuzhouPublicPage",
            "availability": None,
            "live_status": None,
            "subtitles": {},
            "automatic_captions": {},
            "chapters": [],
        }
    )


def bilibili_public_audio(
    platform_metadata: dict[str, Any],
) -> dict[str, Any]:
    """Select the highest-bandwidth anonymous DASH audio returned by Bilibili."""
    validate_bilibili_public_access(platform_metadata)
    bvid = platform_metadata.get("bvid")
    cid = platform_metadata.get("cid")
    if not isinstance(bvid, str) or not isinstance(cid, int):
        raise ValueError("Bilibili metadata has no stable BVID/CID identity")
    playurl = fetch_bilibili_api(
        "/x/player/playurl",
        f"bvid={bvid}&cid={cid}&fnval=16&fnver=0&fourk=1",
    )
    dash = playurl.get("dash")
    dash = dash if isinstance(dash, dict) else {}
    candidates = dash.get("audio")
    candidates = candidates if isinstance(candidates, list) else []
    public_audio = [
        candidate
        for candidate in candidates
        if isinstance(candidate, dict)
        and isinstance(candidate.get("baseUrl") or candidate.get("base_url"), str)
        and bool(candidate.get("baseUrl") or candidate.get("base_url"))
    ]
    if not public_audio:
        raise PermissionError("Bilibili public playurl returned no anonymous audio")
    selected = max(
        public_audio,
        key=lambda candidate: (
            candidate.get("bandwidth")
            if isinstance(candidate.get("bandwidth"), (int, float))
            else 0
        ),
    )
    base_url = selected.get("baseUrl") or selected.get("base_url")
    backups = selected.get("backupUrl") or selected.get("backup_url") or []
    urls = [base_url]
    if isinstance(backups, list):
        urls.extend(url for url in backups if isinstance(url, str))
    timelength = playurl.get("timelength")
    return {
        "urls": urls,
        "duration_seconds": (
            float(timelength) / 1000
            if isinstance(timelength, (int, float)) and timelength > 0
            else platform_metadata.get("duration_seconds")
        ),
        "format_id": selected.get("id"),
        "bandwidth": selected.get("bandwidth"),
    }


def xiaoyuzhou_public_audio(
    platform_metadata: dict[str, Any],
) -> dict[str, Any]:
    """Select the public M4A enclosure exposed by an episode page."""
    validate_xiaoyuzhou_public_access(platform_metadata)
    media = platform_metadata["media"]
    return {
        "urls": [media["url"]],
        "duration_seconds": platform_metadata["duration_seconds"],
        "format_id": media["id"],
        "filesize": media["size_bytes"],
        "mime_type": media["mime_type"],
    }


def download_direct_public_audio(
    *,
    audio: dict[str, Any],
    options: dict[str, Any],
    canonical_url: str,
    expected_output: Path,
    downloader_type: Any,
    download_error_type: type[Exception],
    source_label: str,
) -> None:
    """Download one validated public stream, retrying only transport errors."""
    urls = audio.get("urls")
    if not isinstance(urls, list) or not urls:
        raise ValueError(f"{source_label} public audio selection has no URLs")
    direct_options = dict(options)
    direct_options.pop("match_filter", None)
    direct_options["http_headers"] = {
        "Referer": canonical_url,
        "User-Agent": "Mozilla/5.0 PodWiki/0.1",
    }
    last_error: Exception | None = None
    for url in urls:
        if not isinstance(url, str) or not url:
            continue
        try:
            with downloader_type(direct_options) as downloader:
                downloader.download([url])
            if expected_output.is_file():
                return
            raise FileNotFoundError(
                f"{source_label} direct download produced no output: {expected_output}"
            )
        except download_error_type as error:
            last_error = error
    if last_error is not None:
        raise last_error
    raise ValueError(f"{source_label} public audio selection has no usable URLs")


def download_bilibili_public_audio(
    *,
    audio: dict[str, Any],
    options: dict[str, Any],
    canonical_url: str,
    expected_output: Path,
    downloader_type: Any,
    download_error_type: type[Exception],
) -> None:
    """Download one anonymous Bilibili stream without persisting its signed URL."""
    download_direct_public_audio(
        audio=audio,
        options=options,
        canonical_url=canonical_url,
        expected_output=expected_output,
        downloader_type=downloader_type,
        download_error_type=download_error_type,
        source_label="Bilibili",
    )


def download_xiaoyuzhou_public_audio(
    *,
    audio: dict[str, Any],
    options: dict[str, Any],
    canonical_url: str,
    expected_output: Path,
    downloader_type: Any,
    download_error_type: type[Exception],
) -> None:
    """Download one public Xiaoyuzhou enclosure without credentials."""
    download_direct_public_audio(
        audio=audio,
        options=options,
        canonical_url=canonical_url,
        expected_output=expected_output,
        downloader_type=downloader_type,
        download_error_type=download_error_type,
        source_label="Xiaoyuzhou",
    )


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
        "eid": platform_metadata.get("eid") or info.get("eid"),
        "pid": platform_metadata.get("pid") or info.get("pid"),
        "aid": platform_metadata.get("aid") or info.get("aid"),
        "cid": platform_metadata.get("cid") or info.get("cid"),
        "page": (
            None
            if platform == "xiaoyuzhou"
            else (
                platform_metadata.get("page")
                or info.get("page")
                or info.get("playlist_index")
                or 1
            )
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


def validate_public_enclosure_size(
    media: dict[str, Any], *, platform_metadata: dict[str, Any]
) -> None:
    source_media = platform_metadata.get("media")
    source_media = source_media if isinstance(source_media, dict) else {}
    expected_size = source_media.get("size_bytes")
    if expected_size is not None:
        actual_size = media.get("size_bytes")
        if actual_size != expected_size:
            raise ValueError(
                "downloaded audio size differs from the public enclosure: "
                f"expected={expected_size} actual={actual_size}"
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
    if platform == "bilibili":
        match = BILIBILI_VIDEO_RE.fullmatch(urlparse(canonical_url).path)
        if match is None:
            raise ValueError("canonical Bilibili URL has no BVID")
        platform_metadata = bilibili_platform_metadata(match.group(1))
    elif platform == "xiaoyuzhou":
        match = XIAOYUZHOU_EPISODE_RE.fullmatch(urlparse(canonical_url).path)
        if match is None:
            raise ValueError("canonical Xiaoyuzhou URL has no episode ID")
        platform_metadata = xiaoyuzhou_platform_metadata(match.group(1))
    else:
        platform_metadata = {}
    if platform == "bilibili":
        validate_bilibili_public_access(platform_metadata)
    elif platform == "xiaoyuzhou":
        validate_xiaoyuzhou_public_access(platform_metadata)
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
        if platform != "xiaoyuzhou" and shutil.which("ffmpeg") is None:
            raise SystemExit("ffmpeg is required to extract downloaded audio")
        if shutil.which("ffprobe") is None:
            raise SystemExit("ffprobe is required to validate downloaded audio")
    staging_directory: Path | None = None
    download_output = output_path
    if download_requested:
        if platform == "bilibili":
            source_id = platform_metadata.get("bvid")
        elif platform == "xiaoyuzhou":
            source_id = platform_metadata.get("eid")
        else:
            source_id = parse_qs(urlparse(canonical_url).query)["v"][0]
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
    if download_requested and platform != "xiaoyuzhou":
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
    if platform == "xiaoyuzhou":
        info = xiaoyuzhou_api_info(platform_metadata)
        if download_requested:
            public_audio = xiaoyuzhou_public_audio(platform_metadata)
            download_xiaoyuzhou_public_audio(
                audio=public_audio,
                options=options,
                canonical_url=canonical_url,
                expected_output=download_output,
                downloader_type=YoutubeDL,
                download_error_type=DownloadError,
            )
    else:
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
            if platform != "bilibili":
                raise ConnectionError(
                    "yt-dlp failed after extractor retries"
                ) from last_download_error
            if not is_bilibili_extractor_compatibility_error(last_download_error):
                if last_download_error is not None:
                    raise last_download_error
                raise ConnectionError("yt-dlp failed without an extractor error")
            info = bilibili_api_info(platform_metadata)
            if download_requested:
                public_audio = bilibili_public_audio(platform_metadata)
                if isinstance(public_audio.get("duration_seconds"), (int, float)):
                    info["duration"] = public_audio["duration_seconds"]
                download_bilibili_public_audio(
                    audio=public_audio,
                    options=options,
                    canonical_url=canonical_url,
                    expected_output=download_output,
                    downloader_type=YoutubeDL,
                    download_error_type=DownloadError,
                )
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
        validate_public_enclosure_size(
            downloaded_media,
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
        validate_public_enclosure_size(
            media,
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
