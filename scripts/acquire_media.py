#!/usr/bin/env python3
"""Acquire one public podcast episode or video as a verified local audio file."""

from __future__ import annotations

import argparse
import codecs
import copy
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from contextlib import ExitStack, contextmanager
from datetime import datetime, timezone
from html.parser import HTMLParser
from http.client import HTTPException
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlparse
from urllib.request import HTTPRedirectHandler, Request, build_opener, urlopen


ROOT = Path(__file__).resolve().parents[1]
BILIBILI_VIDEO_RE = re.compile(r"^/video/(BV[A-Za-z0-9]+)/?$")
YOUTUBE_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")
XIAOYUZHOU_ID_RE = re.compile(r"^[0-9a-f]{24}$")
XIAOYUZHOU_EPISODE_RE = re.compile(r"^/episode/([0-9a-f]{24})/?$")
XIAOYUZHOU_MEDIA_ID_RE = re.compile(
    r"^([0-9a-f]{24})/([A-Za-z0-9_-]+\.m4a)$"
)
XIAOYUZHOU_MAX_PAGE_BYTES = 16 * 1024 * 1024
XIAOYUZHOU_PUBLIC_TRANSCRIPT_FIELDS = {
    "transcript": False,
    "transcripts": False,
    "subtitle": False,
    "subtitles": False,
    "caption": False,
    "captions": False,
    "automaticCaption": True,
    "automaticCaptions": True,
    "automatic_caption": True,
    "automatic_captions": True,
}
XIAOYUZHOU_TRANSCRIPT_MARKER_FIELD = "transcriptMediaId"
XIAOYUZHOU_LANGUAGE_RE = re.compile(
    r"^(?:und|[A-Za-z]{2,3}(?:-[A-Za-z0-9]{2,8})*)$"
)
XIAOYUZHOU_TRACK_LANGUAGE_FIELDS = (
    "language",
    "languageCode",
    "lang",
    "locale",
)
XIAOYUZHOU_TRACK_AUTOMATIC_FIELDS = ("automatic", "isAutomatic")
XIAOYUZHOU_TRACK_TEXT_FIELDS = ("text", "content", "body")
XIAOYUZHOU_TRACK_FIELDS = {
    "url",
    "mediaId",
    "segments",
    "kind",
    "type",
    "label",
    "name",
    "format",
    "ext",
    "mimeType",
    *XIAOYUZHOU_TRACK_LANGUAGE_FIELDS,
    *XIAOYUZHOU_TRACK_AUTOMATIC_FIELDS,
    *XIAOYUZHOU_TRACK_TEXT_FIELDS,
}
XIAOYUZHOU_TRACK_CONTAINER_FIELDS = {
    "tracks",
    "mediaId",
    *XIAOYUZHOU_TRACK_LANGUAGE_FIELDS,
    *XIAOYUZHOU_TRACK_AUTOMATIC_FIELDS,
}
XIAOYUZHOU_SEGMENT_FIELDS = {
    "text",
    "startMs",
    "endMs",
    "durationMs",
    "speaker",
    "speakerId",
}
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
        "--repair-metadata",
        action="store_true",
        help=(
            "Rebuild a missing sidecar for an existing audio file after "
            "anonymous source verification; requires --metadata-only and "
            "--expected-sha256"
        ),
    )
    parser.add_argument(
        "--expected-sha256",
        help=(
            "Previously verified lowercase SHA-256 for the existing audio used "
            "by --repair-metadata"
        ),
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
            "Accept-Encoding": "identity",
            "User-Agent": "Mozilla/5.0 PodWiki/0.1",
        },
    )
    opener = build_opener(RejectRedirects())
    page_bytes: bytes | None = None
    last_error: Exception | None = None
    for attempt in range(4):
        try:
            with opener.open(request, timeout=60) as response:
                if response.geturl() != canonical_url:
                    raise PermissionError(
                        "Xiaoyuzhou episode page changed its canonical URL"
                    )
                if getattr(response, "status", None) != 200:
                    raise ValueError("Xiaoyuzhou episode page did not return HTTP 200")
                content_type = response.headers.get("Content-Type")
                if (
                    not isinstance(content_type, str)
                    or content_type.split(";", 1)[0].strip().lower()
                    not in {"text/html", "application/xhtml+xml"}
                ):
                    raise ValueError("Xiaoyuzhou episode page is not HTML")
                content_encoding = response.headers.get("Content-Encoding")
                if content_encoding is not None and content_encoding.strip().lower() != "identity":
                    raise ValueError("Xiaoyuzhou episode page uses unsupported encoding")
                page_bytes = response.read(XIAOYUZHOU_MAX_PAGE_BYTES + 1)
            break
        except PermissionError:
            raise
        except HTTPError as error:
            retryable = retryable_http_error(error)
            error.close()
            if not retryable:
                raise
            last_error = error
            if attempt == 3:
                break
            time.sleep(2**attempt)
        except (TimeoutError, URLError, OSError, HTTPException) as error:
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
    try:
        page_html = page_bytes.decode("utf-8")
    except UnicodeDecodeError as error:
        raise ValueError("Xiaoyuzhou episode page is not valid UTF-8") from error
    return extract_xiaoyuzhou_next_data(page_html)


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


def validate_xiaoyuzhou_public_track_url(value: Any, *, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Xiaoyuzhou {field} has no public track URL")
    url = value.strip()
    parsed = urlparse(url)
    if (
        parsed.scheme != "https"
        or parsed.hostname is None
        or parsed.username is not None
        or parsed.password is not None
        or not parsed.path
        or bool(parsed.fragment)
    ):
        raise ValueError(f"Xiaoyuzhou {field} has an invalid public track URL")
    return url


def xiaoyuzhou_track_language(
    track: dict[str, Any],
    *,
    field: str,
    inherited_language: str | None,
) -> str:
    candidates: list[str] = []
    if inherited_language is not None:
        candidates.append(inherited_language)
    for language_field in XIAOYUZHOU_TRACK_LANGUAGE_FIELDS:
        if language_field not in track:
            continue
        value = track[language_field]
        if not isinstance(value, str) or not value.strip():
            raise ValueError(
                f"Xiaoyuzhou {field}.{language_field} is not a language tag"
            )
        candidates.append(value.strip())
    if not candidates:
        return "und"
    if any(value.casefold() != candidates[0].casefold() for value in candidates[1:]):
        raise ValueError(f"Xiaoyuzhou {field} has ambiguous language metadata")
    if XIAOYUZHOU_LANGUAGE_RE.fullmatch(candidates[0]) is None:
        raise ValueError(f"Xiaoyuzhou {field} has an invalid language tag")
    return candidates[0]


def xiaoyuzhou_track_automatic(
    track: dict[str, Any],
    *,
    field: str,
    default_automatic: bool,
) -> bool:
    candidates: list[bool] = []
    for automatic_field in XIAOYUZHOU_TRACK_AUTOMATIC_FIELDS:
        if automatic_field not in track:
            continue
        value = track[automatic_field]
        if not isinstance(value, bool):
            raise ValueError(
                f"Xiaoyuzhou {field}.{automatic_field} is not boolean"
            )
        candidates.append(value)

    classification_values = {
        "automatic": True,
        "automatic_caption": True,
        "auto": True,
        "machine": True,
        "manual": False,
        "human": False,
        "transcript": False,
        "subtitle": False,
        "caption": False,
    }
    for classification_field in ("kind", "type"):
        if classification_field not in track:
            continue
        value = track[classification_field]
        if not isinstance(value, str) or not value.strip():
            raise ValueError(
                f"Xiaoyuzhou {field}.{classification_field} is not a track kind"
            )
        normalized = value.strip().lower().replace("-", "_").replace(" ", "_")
        if normalized in classification_values:
            candidates.append(classification_values[normalized])

    if candidates and any(value != candidates[0] for value in candidates[1:]):
        raise ValueError(f"Xiaoyuzhou {field} has ambiguous automatic-caption metadata")
    if default_automatic and candidates and candidates[0] is not True:
        raise ValueError(f"Xiaoyuzhou {field} contradicts its automatic-caption field")
    return candidates[0] if candidates else default_automatic


def validate_xiaoyuzhou_transcript_segments(
    value: Any, *, field: str
) -> list[dict[str, Any]]:
    if not isinstance(value, list) or not value:
        raise ValueError(f"Xiaoyuzhou {field}.segments is not a non-empty list")
    segments: list[dict[str, Any]] = []
    for index, segment in enumerate(value):
        segment_field = f"{field}.segments[{index}]"
        if not isinstance(segment, dict):
            raise ValueError(f"Xiaoyuzhou {segment_field} is not an object")
        unknown = set(segment) - XIAOYUZHOU_SEGMENT_FIELDS
        if unknown:
            raise ValueError(
                f"Xiaoyuzhou {segment_field} has unknown fields: "
                f"{', '.join(sorted(unknown))}"
            )
        text = segment.get("text")
        if not isinstance(text, str) or not text.strip():
            raise ValueError(f"Xiaoyuzhou {segment_field} has no text")
        for timing_field in ("startMs", "endMs", "durationMs"):
            if timing_field not in segment:
                continue
            timing = segment[timing_field]
            if isinstance(timing, bool) or not isinstance(timing, (int, float)):
                raise ValueError(
                    f"Xiaoyuzhou {segment_field}.{timing_field} is not numeric"
                )
            if timing < 0:
                raise ValueError(
                    f"Xiaoyuzhou {segment_field}.{timing_field} is negative"
                )
        for speaker_field in ("speaker", "speakerId"):
            if speaker_field in segment and not isinstance(
                segment[speaker_field], str
            ):
                raise ValueError(
                    f"Xiaoyuzhou {segment_field}.{speaker_field} is not text"
                )
        segments.append(copy.deepcopy(segment))
    return segments


def xiaoyuzhou_public_track_from_scalar(
    value: str,
    *,
    source_field: str,
    media_id: str,
    inherited_language: str | None,
    default_automatic: bool,
) -> list[dict[str, Any]]:
    stripped = value.strip()
    if not stripped:
        return []
    if source_field.startswith("transcript") and stripped == media_id:
        return []
    if XIAOYUZHOU_MEDIA_ID_RE.fullmatch(stripped) is not None:
        raise ValueError(
            f"Xiaoyuzhou {source_field} has an ambiguous transcript media id"
        )

    track = {
        "source_field": source_field,
        "kind": "automatic_caption" if default_automatic else source_field.rstrip("s"),
        "language": inherited_language or "und",
        "automatic": default_automatic,
    }
    looks_like_url = bool(
        re.match(r"^[A-Za-z][A-Za-z0-9+.-]*://", stripped)
    ) or stripped.startswith("//")
    if looks_like_url:
        track["url"] = validate_xiaoyuzhou_public_track_url(
            stripped, field=source_field
        )
    else:
        track["text"] = stripped
    return [track]


def xiaoyuzhou_public_track_from_object(
    track: dict[str, Any],
    *,
    source_field: str,
    media_id: str,
    inherited_language: str | None,
    default_automatic: bool,
) -> list[dict[str, Any]]:
    unknown = set(track) - XIAOYUZHOU_TRACK_FIELDS
    if unknown:
        raise ValueError(
            f"Xiaoyuzhou {source_field} track has unknown fields: "
            f"{', '.join(sorted(unknown))}"
        )

    track_media_id = track.get("mediaId")
    if "mediaId" in track and (
        not isinstance(track_media_id, str) or not track_media_id.strip()
    ):
        raise ValueError(f"Xiaoyuzhou {source_field}.mediaId is not text")

    text_values: list[str] = []
    for text_field in XIAOYUZHOU_TRACK_TEXT_FIELDS:
        if text_field not in track:
            continue
        value = track[text_field]
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Xiaoyuzhou {source_field}.{text_field} has no text")
        text_values.append(value.strip())
    if text_values and any(value != text_values[0] for value in text_values[1:]):
        raise ValueError(f"Xiaoyuzhou {source_field} has ambiguous transcript text")

    public_url = (
        validate_xiaoyuzhou_public_track_url(track["url"], field=source_field)
        if "url" in track
        else None
    )
    segments = (
        validate_xiaoyuzhou_transcript_segments(
            track["segments"], field=source_field
        )
        if "segments" in track
        else None
    )
    if public_url is None and not text_values and segments is None:
        if (
            source_field.startswith("transcript")
            and set(track) == {"mediaId"}
            and track_media_id == media_id
        ):
            return []
        raise ValueError(
            f"Xiaoyuzhou {source_field} has no explicit public text or track URL"
        )

    language = xiaoyuzhou_track_language(
        track,
        field=source_field,
        inherited_language=inherited_language,
    )
    automatic = xiaoyuzhou_track_automatic(
        track,
        field=source_field,
        default_automatic=default_automatic,
    )
    normalized: dict[str, Any] = {
        "source_field": source_field,
        "kind": "automatic_caption" if automatic else source_field.rstrip("s"),
        "language": language,
        "automatic": automatic,
    }
    if public_url is not None:
        normalized["url"] = public_url
    if text_values:
        normalized["text"] = text_values[0]
    if segments is not None:
        normalized["segments"] = segments
    for metadata_field in (
        "mediaId",
        "label",
        "name",
        "format",
        "ext",
        "mimeType",
    ):
        if metadata_field not in track:
            continue
        value = track[metadata_field]
        if not isinstance(value, str) or not value.strip():
            raise ValueError(
                f"Xiaoyuzhou {source_field}.{metadata_field} is not text"
            )
        normalized[metadata_field] = value.strip()
    return [normalized]


def parse_xiaoyuzhou_public_track_value(
    value: Any,
    *,
    source_field: str,
    media_id: str,
    default_automatic: bool,
    inherited_language: str | None = None,
    depth: int = 0,
) -> list[dict[str, Any]]:
    if depth > 4:
        raise ValueError(f"Xiaoyuzhou {source_field} track metadata is too deeply nested")
    if value is None or value == "" or value == [] or value == {}:
        return []
    if isinstance(value, str):
        return xiaoyuzhou_public_track_from_scalar(
            value,
            source_field=source_field,
            media_id=media_id,
            inherited_language=inherited_language,
            default_automatic=default_automatic,
        )
    if isinstance(value, list):
        container_tracks: list[dict[str, Any]] = []
        for item in value:
            if not isinstance(item, (str, dict)):
                raise ValueError(f"Xiaoyuzhou {source_field} track list is malformed")
            container_tracks.extend(
                parse_xiaoyuzhou_public_track_value(
                    item,
                    source_field=source_field,
                    media_id=media_id,
                    default_automatic=default_automatic,
                    inherited_language=inherited_language,
                    depth=depth + 1,
                )
            )
        return container_tracks
    if not isinstance(value, dict):
        raise ValueError(f"Xiaoyuzhou {source_field} metadata is malformed")

    if "tracks" in value:
        unknown = set(value) - XIAOYUZHOU_TRACK_CONTAINER_FIELDS
        if unknown:
            raise ValueError(
                f"Xiaoyuzhou {source_field} track container has unknown fields: "
                f"{', '.join(sorted(unknown))}"
            )
        raw_tracks = value["tracks"]
        if not isinstance(raw_tracks, list):
            raise ValueError(f"Xiaoyuzhou {source_field}.tracks is not a list")
        container_media_id = value.get("mediaId")
        if "mediaId" in value and (
            not isinstance(container_media_id, str) or not container_media_id
        ):
            raise ValueError(f"Xiaoyuzhou {source_field}.mediaId is not text")
        if not raw_tracks and container_media_id not in {None, media_id}:
            raise ValueError(
                f"Xiaoyuzhou {source_field} has an ambiguous transcript media id"
            )
        container_language = (
            xiaoyuzhou_track_language(
                value,
                field=source_field,
                inherited_language=inherited_language,
            )
            if inherited_language is not None
            or any(field in value for field in XIAOYUZHOU_TRACK_LANGUAGE_FIELDS)
            else None
        )
        container_automatic = xiaoyuzhou_track_automatic(
            value,
            field=source_field,
            default_automatic=default_automatic,
        )
        tracks: list[dict[str, Any]] = []
        for item in raw_tracks:
            if not isinstance(item, (str, dict)):
                raise ValueError(f"Xiaoyuzhou {source_field}.tracks is malformed")
            tracks.extend(
                parse_xiaoyuzhou_public_track_value(
                    item,
                    source_field=source_field,
                    media_id=media_id,
                    default_automatic=container_automatic,
                    inherited_language=container_language,
                    depth=depth + 1,
                )
            )
        return tracks

    if value and not set(value).intersection(XIAOYUZHOU_TRACK_FIELDS) and all(
        isinstance(language, str)
        and XIAOYUZHOU_LANGUAGE_RE.fullmatch(language) is not None
        for language in value
    ):
        tracks = []
        for language, item in value.items():
            tracks.extend(
                parse_xiaoyuzhou_public_track_value(
                    item,
                    source_field=source_field,
                    media_id=media_id,
                    default_automatic=default_automatic,
                    inherited_language=language,
                    depth=depth + 1,
                )
            )
        return tracks

    return xiaoyuzhou_public_track_from_object(
        value,
        source_field=source_field,
        media_id=media_id,
        inherited_language=inherited_language,
        default_automatic=default_automatic,
    )


def extract_xiaoyuzhou_public_transcripts(
    episode: dict[str, Any], *, media_id: str
) -> dict[str, Any]:
    allowed_fields = {
        *XIAOYUZHOU_PUBLIC_TRANSCRIPT_FIELDS,
        XIAOYUZHOU_TRANSCRIPT_MARKER_FIELD,
    }
    for field in episode:
        if not isinstance(field, str):
            continue
        lowered = field.lower()
        if any(name in lowered for name in ("transcript", "subtitle", "caption")):
            if field not in allowed_fields:
                raise ValueError(
                    f"Xiaoyuzhou episode has unknown transcript field: {field}"
                )

    page_fields: dict[str, Any] = {}
    tracks: list[dict[str, Any]] = []
    for field, automatic in XIAOYUZHOU_PUBLIC_TRANSCRIPT_FIELDS.items():
        if field not in episode:
            continue
        page_fields[field] = copy.deepcopy(episode[field])
        tracks.extend(
            parse_xiaoyuzhou_public_track_value(
                episode[field],
                source_field=field,
                media_id=media_id,
                default_automatic=automatic,
            )
        )

    if XIAOYUZHOU_TRANSCRIPT_MARKER_FIELD in episode:
        transcript_media_id = episode[XIAOYUZHOU_TRANSCRIPT_MARKER_FIELD]
        page_fields[XIAOYUZHOU_TRANSCRIPT_MARKER_FIELD] = copy.deepcopy(
            transcript_media_id
        )
        if transcript_media_id is not None:
            if not isinstance(transcript_media_id, str) or not transcript_media_id:
                raise ValueError("Xiaoyuzhou transcriptMediaId is malformed")
            if transcript_media_id != media_id and not tracks:
                raise ValueError(
                    "Xiaoyuzhou transcriptMediaId is ambiguous without a public track"
                )

    subtitle: dict[str, Any] = {"tracks": tracks}
    if page_fields:
        subtitle["page_fields"] = page_fields
    return subtitle


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
    if not isinstance(media_id, str):
        raise ValueError("Xiaoyuzhou episode metadata has no media id")
    subtitle = extract_xiaoyuzhou_public_transcripts(episode, media_id=media_id)

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
        "subtitle": subtitle,
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
    media_id = media.get("id")
    media_id_match = (
        XIAOYUZHOU_MEDIA_ID_RE.fullmatch(media_id)
        if isinstance(media_id, str)
        else None
    )
    if media_id_match is None or media_id_match.group(1) != platform_metadata.get(
        "pid"
    ):
        raise ValueError("Xiaoyuzhou episode/podcast/media identity mismatch")
    parsed_media_url = urlparse(media_url)
    if (
        parsed_media_url.scheme != "https"
        or parsed_media_url.netloc != "media.xyzcdn.net"
        or parsed_media_url.username is not None
        or parsed_media_url.password is not None
        or parsed_media_url.path != f"/{media_id}"
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
            newline="\n",
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


def render_json_for_stdout(
    document: dict[str, Any], *, encoding: str | None
) -> str:
    """Render readable UTF-8 JSON and portable ASCII JSON elsewhere."""
    rendered = json.dumps(document, ensure_ascii=False, indent=2, allow_nan=False)
    if encoding is None:
        return rendered
    try:
        if codecs.lookup(encoding).name == "utf-8":
            return rendered
    except LookupError:
        pass
    return json.dumps(document, ensure_ascii=True, indent=2, allow_nan=False)


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
    subtitles: dict[str, list[Any]] = {
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
    subtitle = platform_metadata.get("subtitle")
    if not isinstance(subtitle, dict):
        raise ValueError("Xiaoyuzhou subtitle metadata is missing")
    tracks = subtitle.get("tracks")
    if not isinstance(tracks, list):
        raise ValueError("Xiaoyuzhou subtitle tracks are malformed")
    subtitles: dict[str, list[dict[str, Any]]] = {}
    automatic_captions: dict[str, list[dict[str, Any]]] = {}
    for index, track in enumerate(tracks):
        if not isinstance(track, dict):
            raise ValueError(f"Xiaoyuzhou subtitle track {index} is malformed")
        language = track.get("language")
        automatic = track.get("automatic")
        if (
            not isinstance(language, str)
            or not language
            or not isinstance(automatic, bool)
        ):
            raise ValueError(f"Xiaoyuzhou subtitle track {index} is ambiguous")
        target = automatic_captions if automatic else subtitles
        target.setdefault(language, []).append(copy.deepcopy(track))
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
            "subtitles": subtitles,
            "automatic_captions": automatic_captions,
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
        key=lambda candidate: float(candidate.get("bandwidth", 0))
        if isinstance(candidate.get("bandwidth"), (int, float))
        else 0.0,
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


class RejectRedirects(HTTPRedirectHandler):
    """Reject redirects before urllib can send a request to another location."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if fp is not None:
            try:
                fp.close()
            except Exception:
                pass
        raise PermissionError("Xiaoyuzhou redirects are unsupported")


class RetryableMediaDownloadError(Exception):
    """A transport failure that may succeed when the same byte range is retried."""


class MediaRepresentationChangedError(Exception):
    """The enclosure changed while a byte-range download was in progress."""


def retryable_http_error(error: HTTPError) -> bool:
    return error.code in {408, 429} or 500 <= error.code <= 599


def is_strong_etag(value: Any) -> bool:
    return (
        isinstance(value, str)
        and len(value) >= 2
        and value.startswith('"')
        and value.endswith('"')
        and not value.startswith('W/"')
    )


@contextmanager
def exclusive_download_lock(path: Path):
    """Hold a non-blocking OS lock for one output without stale lock semantics."""
    path.parent.mkdir(parents=True, exist_ok=True)
    stream = path.open("a+b")
    try:
        if os.name == "nt":
            import msvcrt

            if path.stat().st_size == 0:
                stream.write(b"\0")
                stream.flush()
            stream.seek(0)
            try:
                msvcrt.locking(  # type: ignore[attr-defined]
                    stream.fileno(), msvcrt.LK_NBLCK, 1  # type: ignore[attr-defined]
                )
            except OSError as error:
                raise FileExistsError(
                    f"another download is already using this output: {path}"
                ) from error
        else:
            import fcntl

            try:
                fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError as error:
                raise FileExistsError(
                    f"another download is already using this output: {path}"
                ) from error
        try:
            yield
        finally:
            if os.name == "nt":
                stream.seek(0)
                msvcrt.locking(  # type: ignore[attr-defined]
                    stream.fileno(), msvcrt.LK_UNLCK, 1  # type: ignore[attr-defined]
                )
            else:
                fcntl.flock(stream.fileno(), fcntl.LOCK_UN)
    finally:
        stream.close()


def acquisition_resource_lock_path(resource_path: Path) -> Path:
    """Map a resource to a sibling lock whose aliases follow filesystem semantics."""
    normalized_path = os.path.realpath(os.path.abspath(os.fspath(resource_path)))
    if os.name == "nt":
        if normalized_path.startswith("\\\\?\\UNC\\"):
            normalized_path = f"\\\\{normalized_path[8:]}"
        elif normalized_path.startswith("\\\\?\\"):
            normalized_path = normalized_path[4:]
    normalized_resource = Path(normalized_path)
    return (
        normalized_resource.parent
        / ".podwiki-locks"
        / f"{normalized_resource.name}.lock"
    )


@contextmanager
def exclusive_acquisition_locks(resource_paths: list[Path]):
    """Lock final audio and metadata resources in a deadlock-free order."""
    lock_paths = sorted(
        {acquisition_resource_lock_path(path) for path in resource_paths},
        key=lambda path: path.as_posix(),
    )
    with ExitStack() as stack:
        for lock_path in lock_paths:
            stack.enter_context(exclusive_download_lock(lock_path))
        yield


def discard_partial_download(partial_path: Path, checkpoint_path: Path) -> None:
    partial_path.unlink(missing_ok=True)
    checkpoint_path.unlink(missing_ok=True)


def validated_partial_checkpoint(
    *,
    partial_path: Path,
    checkpoint_path: Path,
    media_url: str,
    expected_size: int,
) -> tuple[int, str | None]:
    if not partial_path.is_file():
        try:
            checkpoint_path.unlink(missing_ok=True)
        except OSError:
            pass
        return 0, None
    partial_size = partial_path.stat().st_size
    if partial_size <= 0 or partial_size >= expected_size or not checkpoint_path.is_file():
        discard_partial_download(partial_path, checkpoint_path)
        return 0, None
    try:
        checkpoint = json.loads(checkpoint_path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        discard_partial_download(partial_path, checkpoint_path)
        return 0, None
    if not isinstance(checkpoint, dict):
        discard_partial_download(partial_path, checkpoint_path)
        return 0, None
    resume_etag = checkpoint.get("etag")
    valid_identity = (
        checkpoint.get("schema_version") == 1
        and checkpoint.get("media_url") == media_url
        and checkpoint.get("expected_size") == expected_size
        and checkpoint.get("size_bytes") == partial_size
        and is_strong_etag(resume_etag)
    )
    expected_hash = checkpoint.get("sha256")
    if (
        not valid_identity
        or not isinstance(expected_hash, str)
        or not re.fullmatch(r"[0-9a-f]{64}", expected_hash)
        or sha256_file(partial_path) != expected_hash
    ):
        discard_partial_download(partial_path, checkpoint_path)
        return 0, None
    return partial_size, resume_etag


def write_partial_checkpoint(
    *,
    partial_path: Path,
    checkpoint_path: Path,
    media_url: str,
    expected_size: int,
    etag: str,
) -> None:
    partial_size = partial_path.stat().st_size if partial_path.is_file() else 0
    if partial_size <= 0 or partial_size >= expected_size or not is_strong_etag(etag):
        discard_partial_download(partial_path, checkpoint_path)
        return
    write_json_atomically(
        checkpoint_path,
        {
            "schema_version": 1,
            "media_url": media_url,
            "expected_size": expected_size,
            "etag": etag,
            "size_bytes": partial_size,
            "sha256": sha256_file(partial_path),
        },
    )


def download_xiaoyuzhou_public_audio(
    *,
    audio: dict[str, Any],
    canonical_url: str,
    expected_output: Path,
) -> None:
    expected_output.parent.mkdir(parents=True, exist_ok=True)
    lock_path = acquisition_resource_lock_path(expected_output)
    with exclusive_download_lock(lock_path):
        _download_xiaoyuzhou_public_audio_locked(
            audio=audio,
            canonical_url=canonical_url,
            expected_output=expected_output,
        )


def _download_xiaoyuzhou_public_audio_locked(
    *,
    audio: dict[str, Any],
    canonical_url: str,
    expected_output: Path,
) -> None:
    """Atomically stream and resume one enclosure without following redirects."""
    urls = audio.get("urls")
    expected_size = audio.get("filesize")
    if (
        not isinstance(urls, list)
        or len(urls) != 1
        or not isinstance(urls[0], str)
        or not urls[0]
    ):
        raise ValueError("Xiaoyuzhou public audio selection must have one URL")
    if isinstance(expected_size, bool) or not isinstance(expected_size, int):
        raise ValueError("Xiaoyuzhou public audio selection has no byte size")
    if expected_size <= 0:
        raise ValueError("Xiaoyuzhou public audio byte size is not positive")

    media_url = urls[0]
    expected_output.parent.mkdir(parents=True, exist_ok=True)
    media_identity = hashlib.sha256(media_url.encode("utf-8")).hexdigest()[:16]
    partial_path = expected_output.with_name(
        f".{expected_output.name}.{media_identity}.part"
    )
    checkpoint_path = partial_path.with_suffix(
        f"{partial_path.suffix}.checkpoint.json"
    )

    opener = build_opener(RejectRedirects())
    last_error: Exception | None = None
    for attempt in range(4):
        partial_size, resume_etag = validated_partial_checkpoint(
            partial_path=partial_path,
            checkpoint_path=checkpoint_path,
            media_url=media_url,
            expected_size=expected_size,
        )
        headers = {
            "Accept": "audio/mp4,audio/m4a,audio/x-m4a",
            "Accept-Encoding": "identity",
            "Referer": canonical_url,
            "User-Agent": "Mozilla/5.0 PodWiki/0.1",
        }
        if partial_size:
            if resume_etag is None:
                raise ValueError("partial download checkpoint has no strong ETag")
            headers["Range"] = f"bytes={partial_size}-"
            headers["If-Range"] = resume_etag
        request = Request(media_url, headers=headers)

        response_etag: str | None = None
        try:
            try:
                response = opener.open(request, timeout=60)
            except PermissionError:
                raise
            except HTTPError as error:
                retryable = retryable_http_error(error)
                error.close()
                if not retryable:
                    raise
                raise RetryableMediaDownloadError(
                    f"retryable Xiaoyuzhou HTTP status {error.code}"
                ) from error
            except (TimeoutError, URLError, OSError, HTTPException) as error:
                raise RetryableMediaDownloadError(
                    "Xiaoyuzhou media connection failed"
                ) from error

            with response:
                if response.geturl() != media_url:
                    raise PermissionError(
                        "Xiaoyuzhou public media response changed enclosure URL"
                    )
                status = getattr(response, "status", None)
                expected_status = 206 if partial_size else 200
                if partial_size and status == 200:
                    raise MediaRepresentationChangedError(
                        "Xiaoyuzhou public media changed during range resume"
                    )
                if status != expected_status:
                    raise ValueError(
                        "Xiaoyuzhou public media returned an unexpected status: "
                        f"expected={expected_status} actual={status}"
                    )
                content_encoding = response.headers.get("Content-Encoding")
                if (
                    content_encoding is not None
                    and content_encoding.strip().lower() != "identity"
                ):
                    raise ValueError(
                        "Xiaoyuzhou public media uses unsupported content encoding"
                    )
                expected_response_size = expected_size - partial_size
                content_length = response.headers.get("Content-Length")
                if content_length is not None:
                    try:
                        response_size = int(content_length)
                    except ValueError as error:
                        raise ValueError(
                            "Xiaoyuzhou public media has invalid Content-Length"
                        ) from error
                    if response_size != expected_response_size:
                        raise ValueError(
                            "Xiaoyuzhou public media Content-Length differs from metadata: "
                            f"expected={expected_response_size} actual={response_size}"
                        )
                if partial_size:
                    expected_range = (
                        f"bytes {partial_size}-{expected_size - 1}/{expected_size}"
                    )
                    if response.headers.get("Content-Range") != expected_range:
                        raise ValueError(
                            "Xiaoyuzhou public media returned an invalid Content-Range"
                        )
                response_etag = response.headers.get("ETag")
                if partial_size and response_etag != resume_etag:
                    raise MediaRepresentationChangedError(
                        "Xiaoyuzhou public media ETag changed during range resume"
                    )
                content_type = response.headers.get("Content-Type")
                if (
                    content_type is not None
                    and content_type.split(";", 1)[0].strip().lower()
                    not in {"audio/mp4", "audio/m4a", "audio/x-m4a"}
                ):
                    raise ValueError(
                        "Xiaoyuzhou public media response is not M4A audio"
                    )

                with partial_path.open("ab" if partial_size else "wb") as stream:
                    downloaded_size = partial_size
                    while True:
                        try:
                            chunk = response.read(1024 * 1024)
                        except (TimeoutError, URLError, OSError, HTTPException) as error:
                            raise RetryableMediaDownloadError(
                                "Xiaoyuzhou media transfer was interrupted"
                            ) from error
                        if not chunk:
                            break
                        downloaded_size += len(chunk)
                        if downloaded_size > expected_size:
                            raise ValueError(
                                "Xiaoyuzhou public media exceeds its published byte size"
                            )
                        stream.write(chunk)
                if downloaded_size != expected_size:
                    raise RetryableMediaDownloadError(
                        "Xiaoyuzhou public media download is incomplete: "
                        f"expected={expected_size} actual={downloaded_size}"
                    )
            try:
                checkpoint_path.unlink(missing_ok=True)
            except OSError:
                pass
            partial_path.replace(expected_output)
            return
        except MediaRepresentationChangedError as error:
            discard_partial_download(partial_path, checkpoint_path)
            last_error = error
        except RetryableMediaDownloadError as error:
            last_error = error
            if is_strong_etag(response_etag):
                if not isinstance(response_etag, str):
                    raise AssertionError("strong ETag validator accepted a non-string")
                write_partial_checkpoint(
                    partial_path=partial_path,
                    checkpoint_path=checkpoint_path,
                    media_url=media_url,
                    expected_size=expected_size,
                    etag=response_etag,
                )
            elif partial_size == 0:
                discard_partial_download(partial_path, checkpoint_path)
            if attempt < 3:
                time.sleep(2**attempt)
    raise ConnectionError(
        "Xiaoyuzhou public media download failed after retries"
    ) from last_error


def source_metadata(
    info: dict[str, Any],
    *,
    platform: str,
    canonical_url: str,
    platform_metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    platform_metadata = platform_metadata or {}
    platform_media = platform_metadata.get("media")
    platform_media = platform_media if isinstance(platform_media, dict) else {}
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
        "video_id": info.get("id") if platform == "youtube" else None,
        "display_id": info.get("display_id"),
        "bvid": platform_metadata.get("bvid") or info.get("bvid") or (
            info.get("id") if platform == "bilibili" else None
        ),
        "eid": platform_metadata.get("eid") or info.get("eid"),
        "pid": platform_metadata.get("pid") or info.get("pid"),
        "media_id": platform_media.get("id"),
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
    return {
        "path": path.as_posix(),
        "size_bytes": int(format_info["size"]),
        "duration_ms": round(float(format_info["duration"]) * 1000),
        "codec": stream.get("codec_name"),
        "sample_rate_hz": int(stream["sample_rate"]),
        "channels": int(stream["channels"]),
        "sha256": sha256_file(path),
    }


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def acquisition_transaction_path(
    *, output_path: Path, metadata_output: Path
) -> Path:
    identity = "\0".join(
        sorted((output_path.resolve().as_posix(), metadata_output.resolve().as_posix()))
    )
    suffix = hashlib.sha256(identity.encode("utf-8")).hexdigest()[:16]
    return metadata_output.resolve().parent / (
        f".podwiki-acquire-{suffix}.transaction.json"
    )


def promote_acquisition_artifact(temporary_path: Path, target_path: Path) -> None:
    temporary_path.replace(target_path)


def validate_acquisition_temporary_path(
    *, label: str, temporary: Path, target: Path
) -> None:
    expected_prefix = f".podwiki-{target.name}."
    if temporary == target:
        raise ValueError(
            f"acquisition transaction {label} temporary path equals its target"
        )
    if temporary.parent != target.parent:
        raise ValueError(
            f"acquisition transaction {label} temporary path is outside the target directory"
        )
    if not (
        temporary.name.startswith(expected_prefix)
        and temporary.name.endswith(".tmp")
    ):
        raise ValueError(
            f"acquisition transaction {label} temporary filename is invalid"
        )


def prepare_acquisition_media_temporary(
    *, staged_audio: Path, output_path: Path
) -> Path:
    descriptor, temporary_name = tempfile.mkstemp(
        dir=output_path.parent,
        prefix=f".podwiki-{output_path.name}.",
        suffix=".tmp",
    )
    os.close(descriptor)
    temporary = Path(temporary_name)
    temporary.unlink()
    try:
        try:
            os.link(staged_audio, temporary)
        except OSError:
            shutil.copyfile(staged_audio, temporary)
        with temporary.open("rb+") as stream:
            stream.flush()
            os.fsync(stream.fileno())
        if sha256_file(temporary) != sha256_file(staged_audio):
            raise ValueError("prepared acquisition media does not match staged audio")
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise
    return temporary


def recover_acquisition_transaction(
    *, output_path: Path, metadata_output: Path
) -> bool:
    transaction_path = acquisition_transaction_path(
        output_path=output_path,
        metadata_output=metadata_output,
    )
    if not transaction_path.is_file():
        return False
    transaction = json.loads(transaction_path.read_text(encoding="utf-8"))
    if not isinstance(transaction, dict) or transaction.get("schema_version") != 1:
        raise ValueError(f"invalid acquisition transaction: {transaction_path}")
    if transaction.get("kind") != "podwiki-acquisition-transaction":
        raise ValueError(f"invalid acquisition transaction kind: {transaction_path}")
    artifacts = transaction.get("artifacts")
    if not isinstance(artifacts, dict) or set(artifacts) != {"media", "metadata"}:
        raise ValueError(f"invalid acquisition transaction artifacts: {transaction_path}")
    expected_targets = {
        "media": output_path.resolve(),
        "metadata": metadata_output.resolve(),
    }
    validated_artifacts: list[tuple[str, Path, Path, str]] = []
    for label in ("media", "metadata"):
        entry = artifacts.get(label)
        if not isinstance(entry, dict):
            raise ValueError(f"invalid acquisition transaction {label} entry")
        target = Path(str(entry.get("target"))).resolve()
        temporary = Path(str(entry.get("temporary"))).resolve()
        expected_sha256 = entry.get("sha256")
        if target != expected_targets[label]:
            raise ValueError(f"acquisition transaction {label} target changed")
        if not isinstance(expected_sha256, str) or re.fullmatch(
            r"[0-9a-f]{64}", expected_sha256
        ) is None:
            raise ValueError(f"acquisition transaction {label} hash is invalid")
        validate_acquisition_temporary_path(
            label=label,
            temporary=temporary,
            target=target,
        )
        validated_artifacts.append((label, temporary, target, expected_sha256))

    for label, temporary, target, expected_sha256 in validated_artifacts:
        if target.is_file() and sha256_file(target) == expected_sha256:
            temporary.unlink(missing_ok=True)
            continue
        if not temporary.is_file() or sha256_file(temporary) != expected_sha256:
            raise ValueError(
                f"cannot recover {label} from acquisition transaction: "
                f"{transaction_path}"
            )
        promote_acquisition_artifact(temporary, target)
        target.chmod(0o644)
    transaction_path.unlink()
    return True


def commit_acquired_media_pair(
    *,
    staged_audio: Path,
    output_path: Path,
    metadata_output: Path,
    document: dict[str, Any],
) -> None:
    if staged_audio.resolve() == output_path.resolve():
        raise ValueError("staged and final audio paths must be distinct")
    if not staged_audio.is_file():
        raise FileNotFoundError(f"staged audio does not exist: {staged_audio}")
    metadata_output.parent.mkdir(parents=True, exist_ok=True)
    metadata_text = (
        json.dumps(document, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    media_temporary: Path | None = None
    metadata_temporary: Path | None = None
    transaction_path = acquisition_transaction_path(
        output_path=output_path,
        metadata_output=metadata_output,
    )
    transaction_written = False
    try:
        media_temporary = prepare_acquisition_media_temporary(
            staged_audio=staged_audio,
            output_path=output_path,
        )
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="\n",
            dir=metadata_output.parent,
            prefix=f".podwiki-{metadata_output.name}.",
            suffix=".tmp",
            delete=False,
        ) as stream:
            stream.write(metadata_text)
            stream.flush()
            os.fsync(stream.fileno())
            metadata_temporary = Path(stream.name)
        write_json_atomically(
            transaction_path,
            {
                "schema_version": 1,
                "kind": "podwiki-acquisition-transaction",
                "artifacts": {
                    "media": {
                        "target": output_path.resolve().as_posix(),
                        "temporary": media_temporary.resolve().as_posix(),
                        "sha256": sha256_file(media_temporary),
                    },
                    "metadata": {
                        "target": metadata_output.resolve().as_posix(),
                        "temporary": metadata_temporary.resolve().as_posix(),
                        "sha256": hashlib.sha256(
                            metadata_text.encode("utf-8")
                        ).hexdigest(),
                    },
                },
            },
        )
        transaction_written = True
        promote_acquisition_artifact(media_temporary, output_path)
        media_temporary = None
        output_path.chmod(0o644)
        staged_audio.unlink()
        promote_acquisition_artifact(metadata_temporary, metadata_output)
        metadata_temporary = None
        metadata_output.chmod(0o644)
        transaction_path.unlink()
        transaction_written = False
    finally:
        if not transaction_written:
            if metadata_temporary is not None:
                metadata_temporary.unlink(missing_ok=True)
            if media_temporary is not None and media_temporary.is_file():
                media_temporary.unlink()


def validate_repair_request(
    *,
    output_path: Path,
    metadata_output: Path,
    expected_sha256: str | None,
) -> str:
    """Validate an explicit, fail-closed orphan-sidecar recovery request."""
    if not isinstance(expected_sha256, str) or re.fullmatch(
        r"[0-9a-f]{64}", expected_sha256
    ) is None:
        raise ValueError(
            "--repair-metadata requires --expected-sha256 as 64 lowercase hex digits"
        )
    if not output_path.is_file():
        raise FileNotFoundError(
            f"--repair-metadata requires an existing audio file: {output_path}"
        )
    if metadata_output.exists():
        raise FileExistsError(
            "--repair-metadata only rebuilds a missing sidecar; the metadata output "
            f"already exists: {metadata_output}"
        )
    actual_sha256 = sha256_file(output_path)
    if actual_sha256 != expected_sha256:
        raise ValueError(
            "existing audio SHA-256 does not match --expected-sha256; "
            "metadata was not repaired"
        )
    return actual_sha256


def repair_existing_media(
    *,
    output_path: Path,
    expected_sha256: str,
    info: dict[str, Any],
    platform_metadata: dict[str, Any],
) -> dict[str, Any]:
    """Re-probe an already hash-bound audio file without claiming when it was acquired."""
    if sha256_file(output_path) != expected_sha256:
        raise ValueError(
            "existing audio changed after repair preflight; metadata was not repaired"
        )
    media = probe_audio(output_path)
    if media.get("sha256") != expected_sha256:
        raise ValueError("ffprobe media SHA-256 differs from --expected-sha256")
    validate_media_duration(
        media,
        info=info,
        platform_metadata=platform_metadata,
    )
    validate_public_enclosure_size(media, platform_metadata=platform_metadata)
    return media


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
    if sha256_file(output_path) != expected_hash:
        raise ValueError(f"existing audio hash does not match {metadata_output}")


def validate_reusable_source_identity(
    *, existing_document: dict[str, Any], current_source: dict[str, Any]
) -> None:
    existing_source = existing_document.get("source")
    if not isinstance(existing_source, dict):
        raise ValueError("existing media metadata has no source identity")
    platform = current_source.get("platform")
    if not isinstance(platform, str):
        raise ValueError("current source has no platform identity")
    identity_fields = {
        "bilibili": ("bvid", "aid", "cid", "page"),
        "youtube": ("id",),
        "xiaoyuzhou": ("eid", "pid", "media_id"),
    }.get(platform)
    if identity_fields is None:
        raise ValueError(f"unsupported reusable source platform: {platform!r}")
    if existing_source.get("platform") != platform:
        raise FileExistsError(
            "existing audio platform differs from the current source; "
            "use --overwrite to replace it"
        )
    for field in identity_fields:
        current_value = current_source.get(field)
        if current_value is None:
            raise ValueError(f"current {platform} source has no stable {field} identity")
        if existing_source.get(field) != current_value:
            raise FileExistsError(
                f"existing audio {field} identity differs from the current source; "
                "use --overwrite to replace it"
            )


def refresh_existing_media(
    *,
    output_path: Path,
    metadata_output: Path,
    canonical_url: str,
    info: dict[str, Any],
    platform_metadata: dict[str, Any],
) -> dict[str, Any] | None:
    if not output_path.is_file():
        return None
    validate_reusable_media(
        output_path=output_path,
        metadata_output=metadata_output,
        canonical_url=canonical_url,
    )
    media = probe_audio(output_path)
    validate_media_duration(
        media,
        info=info,
        platform_metadata=platform_metadata,
    )
    validate_public_enclosure_size(media, platform_metadata=platform_metadata)
    return media


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


def validate_output_path(path: Path) -> None:
    if path.suffix != ".m4a":
        raise ValueError("output path must end in lowercase .m4a")


def main() -> int:
    args = parse_args()
    platform, canonical_url = canonical_source_url(args.url)
    output_path = args.output.resolve()
    metadata_output = (
        args.metadata_output.resolve()
        if args.metadata_output is not None
        else output_path.with_name(f"{output_path.stem}.metadata.json")
    )
    validate_output_path(output_path)
    if metadata_output == output_path:
        raise ValueError("metadata output must not overwrite the audio output")
    repair_metadata = bool(getattr(args, "repair_metadata", False))
    expected_sha256 = getattr(args, "expected_sha256", None)
    if args.metadata_only and args.overwrite:
        raise ValueError("--overwrite cannot be combined with --metadata-only")
    if repair_metadata and not args.metadata_only:
        raise ValueError("--repair-metadata requires --metadata-only")
    if repair_metadata and args.overwrite:
        raise ValueError("--repair-metadata cannot be combined with --overwrite")
    if expected_sha256 is not None and not repair_metadata:
        raise ValueError("--expected-sha256 is only valid with --repair-metadata")
    with exclusive_acquisition_locks([output_path, metadata_output]):
        recover_acquisition_transaction(
            output_path=output_path,
            metadata_output=metadata_output,
        )
        return acquire_media_locked(
            args=args,
            platform=platform,
            canonical_url=canonical_url,
            output_path=output_path,
            metadata_output=metadata_output,
        )


def acquire_media_locked(
    *,
    args: argparse.Namespace,
    platform: str,
    canonical_url: str,
    output_path: Path,
    metadata_output: Path,
) -> int:
    repair_metadata = bool(getattr(args, "repair_metadata", False))
    expected_sha256 = getattr(args, "expected_sha256", None)
    existing_document = read_existing_metadata(
        metadata_output=metadata_output,
        canonical_url=canonical_url,
        allow_replacement=args.overwrite,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_exists = output_path.exists()
    if output_exists and not output_path.is_file():
        raise FileExistsError(f"audio output exists but is not a file: {output_path}")
    if repair_metadata:
        expected_sha256 = validate_repair_request(
            output_path=output_path,
            metadata_output=metadata_output,
            expected_sha256=expected_sha256,
        )
    elif output_exists and not args.overwrite:
        validate_reusable_media(
            output_path=output_path,
            metadata_output=metadata_output,
            canonical_url=canonical_url,
        )
    media_reused = (
        repair_metadata
        or (not args.metadata_only and output_exists and not args.overwrite)
    )
    download_requested = not args.metadata_only and (args.overwrite or not output_exists)
    if download_requested and platform != "xiaoyuzhou" and shutil.which("ffmpeg") is None:
        raise SystemExit("ffmpeg is required to extract downloaded audio")
    if (not args.metadata_only or output_exists) and shutil.which("ffprobe") is None:
        raise SystemExit("ffprobe is required to validate downloaded audio")

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

    YoutubeDL: Any = None
    DownloadError: type[Exception] = Exception
    if platform != "xiaoyuzhou":
        try:
            from yt_dlp import YoutubeDL  # type: ignore[no-redef]
            from yt_dlp.utils import DownloadError  # type: ignore[no-redef]
        except ImportError as error:
            raise SystemExit(
                "yt-dlp is unavailable; install the project with `uv sync --extra media`"
            ) from error

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
                canonical_url=canonical_url,
                expected_output=download_output,
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
    current_source = source_metadata(
        info,
        platform=platform,
        canonical_url=canonical_url,
        platform_metadata=platform_metadata,
    )
    if output_exists and not args.overwrite and not repair_metadata:
        if not isinstance(existing_document, dict):
            raise ValueError("existing audio has no reusable source metadata")
        validate_reusable_source_identity(
            existing_document=existing_document,
            current_source=current_source,
        )
    refreshed_media: dict[str, Any] | None
    if repair_metadata:
        if not isinstance(expected_sha256, str):
            raise AssertionError("repair preflight did not bind an expected SHA-256")
        refreshed_media = repair_existing_media(
            output_path=output_path,
            expected_sha256=expected_sha256,
            info=info,
            platform_metadata=platform_metadata,
        )
    elif args.metadata_only:
        refreshed_media = refresh_existing_media(
            output_path=output_path,
            metadata_output=metadata_output,
            canonical_url=canonical_url,
            info=info,
            platform_metadata=platform_metadata,
        )
    else:
        refreshed_media = None
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
        downloaded_media["path"] = output_path.as_posix()
    inspected_at = utc_now()
    document: dict[str, Any] = {
        "schema_version": 1,
        "kind": "podwiki-source-media",
        "inspected_at": inspected_at,
        "source": current_source,
        "download_requested": download_requested,
        "media_reused": media_reused,
    }
    if args.metadata_only:
        if refreshed_media is not None:
            document["media"] = refreshed_media
            document["media_reused"] = True
            document["verified_at"] = inspected_at
            if repair_metadata:
                document["recovered_at"] = inspected_at
                document["recovery"] = {
                    "method": "verified-existing-audio-v1",
                    "expected_sha256": expected_sha256,
                    "acquired_at_status": "unknown-legacy",
                }
            elif (
                isinstance(existing_document, dict)
                and existing_document.get("acquired_at") is not None
            ):
                document["acquired_at"] = existing_document["acquired_at"]
    if not args.metadata_only:
        committed_or_staged_path = download_output if download_requested else output_path
        if not committed_or_staged_path.is_file():
            raise FileNotFoundError(
                f"yt-dlp did not produce expected output: {committed_or_staged_path}"
            )
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

    if download_requested:
        commit_acquired_media_pair(
            staged_audio=download_output,
            output_path=output_path,
            metadata_output=metadata_output,
            document=document,
        )
        if staging_directory is not None:
            try:
                staging_directory.rmdir()
                staging_directory.parent.rmdir()
            except OSError:
                pass
    else:
        write_json_atomically(metadata_output, document)
    print(render_json_for_stdout(document, encoding=sys.stdout.encoding))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
