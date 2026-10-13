#!/usr/bin/env python3
"""Fetch one authorized subtitle body without putting its transport URL in logs.

The temporary URL is accepted only through a hidden terminal prompt. The caller
must obtain it from the active Chinese subtitle on the exact approved video.
This is a body downloader, not browser authentication or subtitle discovery.
"""

from __future__ import annotations

import argparse
import getpass
import hashlib
import json
import os
import re
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import warnings
from pathlib import Path
from typing import Any, NoReturn

from acquire_media import canonical_source_url
from import_bilibili_subtitles import (
    load_json,
    require_cache_file,
    source_duration_ms,
    subtitle_segments,
    validate_edge_coverage,
    validate_public_free_bilibili_source,
)


ROOT = Path(__file__).resolve().parents[1]
MAX_BODY_BYTES = 16 * 1024 * 1024
REQUEST_TIMEOUT_SECONDS = 20
TOTAL_TIMEOUT_SECONDS = 60
SUBTITLE_HOST = "aisubtitle.hdslb.com"
SUBTITLE_PATH_PREFIX = "/bfs/ai_subtitle/"
CANONICAL_BVID_RE = re.compile(r"https://www\.bilibili\.com/video/(BV[0-9A-Za-z]{10})/")


class SafeFetchError(Exception):
    """A fixed diagnostic category; never retain the rejected transport URL."""

    def __init__(self, category: str, *, http_status: int | None = None) -> None:
        super().__init__(category)
        self.category = category
        self.http_status = http_status


class SafeArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> NoReturn:
        # argparse's usual diagnostic echoes unexpected argument values.
        raise SafeFetchError("invalid-command-line")


class RejectRedirects(urllib.request.HTTPRedirectHandler):
    def redirect_request(
        self,
        req: urllib.request.Request,
        fp: Any,
        code: int,
        msg: str,
        headers: Any,
        newurl: str,
    ) -> None:
        raise SafeFetchError("redirect-rejected", http_status=code)


def validate_transport_url(value: str) -> str:
    """Keep the full signature for transport, without returning it in receipts."""
    try:
        if (
            not value
            or value != value.strip()
            or any(ord(character) < 33 or ord(character) > 126 for character in value)
        ):
            raise ValueError
        parsed = urllib.parse.urlsplit(value)
        if (
            parsed.scheme != "https"
            or parsed.netloc != SUBTITLE_HOST
            or parsed.fragment
            or not parsed.path.startswith(SUBTITLE_PATH_PREFIX)
            or not parsed.path[len(SUBTITLE_PATH_PREFIX) :]
            or re.fullmatch(r"/[A-Za-z0-9/_.-]+", parsed.path) is None
            or any(part in {".", ".."} for part in parsed.path.split("/"))
        ):
            raise ValueError
        pairs = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
        signatures = [item for key, item in pairs if key == "auth_key"]
        if len(signatures) != 1 or not signatures[0]:
            raise ValueError
    except (ValueError, UnicodeError):
        raise SafeFetchError("transport-url-rejected") from None
    return value


def load_source_metadata(metadata_path: Path, canonical_url: str) -> dict[str, Any]:
    try:
        match = CANONICAL_BVID_RE.fullmatch(canonical_url)
        if match is None:
            raise ValueError
        platform, normalized = canonical_source_url(canonical_url)
        if platform != "bilibili" or normalized != canonical_url:
            raise ValueError
        path = require_cache_file(metadata_path, label="metadata JSON")
        metadata = load_json(path.read_bytes(), label="metadata JSON")
        source = metadata.get("source")
        if not isinstance(source, dict):
            raise ValueError
        if (
            source.get("platform") != "bilibili"
            or source.get("canonical_url") != canonical_url
            or source.get("bvid") != match.group(1)
            or type(source.get("page")) is not int
            or source.get("page") != 1
        ):
            raise ValueError
        for field in ("aid", "cid"):
            number = source.get(field)
            if isinstance(number, bool) or not isinstance(number, int) or number <= 0:
                raise ValueError
        platform_metadata = source.get("platform_metadata")
        if not isinstance(platform_metadata, dict):
            raise ValueError
        for field in ("bvid", "aid", "cid", "page"):
            if (
                type(platform_metadata.get(field)) is not type(source[field])
                or platform_metadata.get(field) != source[field]
            ):
                raise ValueError
        validate_public_free_bilibili_source(source)
        source_duration_ms(source)
    except (OSError, ValueError, TypeError, UnicodeError):
        raise SafeFetchError("source-metadata-rejected") from None
    return source


def read_hidden_transport_url() -> str:
    # getpass otherwise warns and falls back to echoed stdin. Fail closed instead.
    if not sys.stdin.isatty() or not sys.stderr.isatty():
        raise SafeFetchError("interactive-terminal-required")
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error", getpass.GetPassWarning)
            value = getpass.getpass("Temporary subtitle URL (hidden; not saved): ")
    except (getpass.GetPassWarning, EOFError, OSError):
        raise SafeFetchError("hidden-input-unavailable") from None
    return validate_transport_url(value)


def download_body(transport_url: str) -> bytes:
    transport_url = validate_transport_url(transport_url)
    # Preserve the operator's network routing. Never export browser cookies.
    opener = urllib.request.build_opener(RejectRedirects())
    request = urllib.request.Request(
        transport_url, headers={"Accept": "application/json"}, method="GET"
    )
    deadline = time.monotonic() + TOTAL_TIMEOUT_SECONDS
    try:
        with opener.open(request, timeout=REQUEST_TIMEOUT_SECONDS) as response:
            if response.status != 200:
                raise SafeFetchError("http-status-rejected", http_status=response.status)
            length = response.headers.get("Content-Length")
            if length is not None:
                try:
                    advertised_size = int(length)
                except ValueError:
                    raise SafeFetchError("invalid-response-length") from None
                if advertised_size < 0:
                    raise SafeFetchError("invalid-response-length")
                if advertised_size > MAX_BODY_BYTES:
                    raise SafeFetchError("body-too-large")
            chunks: list[bytes] = []
            total = 0
            while True:
                if time.monotonic() > deadline:
                    raise SafeFetchError("request-timeout")
                chunk = response.read(min(64 * 1024, MAX_BODY_BYTES + 1 - total))
                if not chunk:
                    break
                total += len(chunk)
                if total > MAX_BODY_BYTES:
                    raise SafeFetchError("body-too-large")
                chunks.append(chunk)
            payload = b"".join(chunks)
            if length is not None and len(payload) != advertised_size:
                raise SafeFetchError("incomplete-response-body")
            return payload
    except SafeFetchError:
        raise
    except urllib.error.HTTPError as error:
        category = "redirect-rejected" if 300 <= error.code < 400 else "http-error"
        raise SafeFetchError(category, http_status=error.code) from None
    except TimeoutError:
        raise SafeFetchError("request-timeout") from None
    except (urllib.error.URLError, OSError, ValueError):
        raise SafeFetchError("transport-failed") from None


def reject_decoded_transport_secrets(document: Any, transport_url: str) -> None:
    signature = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(transport_url).query))["auth_key"]
    pending = [document]
    while pending:
        value = pending.pop()
        if isinstance(value, dict):
            pending.extend(value.keys())
            pending.extend(value.values())
        elif isinstance(value, list):
            pending.extend(value)
        elif isinstance(value, str) and (
            transport_url in value or signature in value or "auth_key" in value.lower()
        ):
            raise SafeFetchError("subtitle-body-rejected")


def validate_body(
    payload: bytes, source: dict[str, Any], *, transport_url: str | None = None
) -> list[dict[str, Any]]:
    try:
        document = load_json(payload, label="subtitle JSON")
        if transport_url is not None:
            # Inspect decoded keys and strings, including fields outside body.
            # JSON escaping must not hide a temporary transport capability.
            reject_decoded_transport_secrets(document, transport_url)
        segments = subtitle_segments(document)
        validate_edge_coverage(segments, duration_ms=source_duration_ms(source))
    except (ValueError, TypeError, UnicodeError):
        raise SafeFetchError("subtitle-body-rejected") from None
    return segments


def cache_destination(bvid: str) -> Path:
    try:
        if re.fullmatch(r"BV[0-9A-Za-z]{10}", bvid) is None:
            raise ValueError
        cache = (ROOT / ".cache").resolve()
        cache.relative_to(ROOT.resolve())
        destination = cache / "intake" / bvid / "subtitle.zh-CN.ai.json"
        destination.parent.resolve().relative_to(cache)
        if destination.is_symlink():
            raise ValueError
    except (OSError, ValueError):
        raise SafeFetchError("cache-destination-rejected") from None
    return destination


def write_body_without_overwrite(destination: Path, payload: bytes) -> str:
    temporary: Path | None = None
    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.is_symlink():
            raise SafeFetchError("cache-destination-rejected")
        if destination.exists():
            if not destination.is_file() or destination.read_bytes() != payload:
                raise SafeFetchError("body-cache-conflict")
            return "reused"
        with tempfile.NamedTemporaryFile(
            prefix=".subtitle-body-", dir=destination.parent, delete=False
        ) as stream:
            temporary = Path(stream.name)
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        try:
            # Link publishes the complete file atomically and refuses replacement.
            os.link(temporary, destination)
        except FileExistsError:
            if (
                destination.is_symlink()
                or not destination.is_file()
                or destination.read_bytes() != payload
            ):
                raise SafeFetchError("body-cache-conflict") from None
            return "reused"
        return "saved"
    except SafeFetchError:
        raise
    except OSError:
        raise SafeFetchError("body-cache-write-failed") from None
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def fetch_authorized_body(
    *, canonical_url: str, metadata_path: Path, transport_url: str
) -> dict[str, Any]:
    transport_url = validate_transport_url(transport_url)
    source = load_source_metadata(metadata_path, canonical_url)
    destination = cache_destination(source["bvid"])
    payload = download_body(transport_url)
    segments = validate_body(payload, source, transport_url=transport_url)
    status = write_body_without_overwrite(destination, payload)
    return {
        "status": status,
        "canonical_url": canonical_url,
        "bvid": source["bvid"],
        "aid": source["aid"],
        "cid": source["cid"],
        "page": 1,
        "body_path": destination.relative_to(ROOT.resolve()).as_posix(),
        "body_sha256": hashlib.sha256(payload).hexdigest(),
        "body_bytes": len(payload),
        "cue_count": len(segments),
        "first_cue_ms": segments[0]["start_ms"],
        "last_cue_ms": segments[-1]["end_ms"],
    }


def main() -> int:
    parser = SafeArgumentParser(description=__doc__)
    parser.add_argument("--url", required=True, help="Canonical Bilibili video URL")
    parser.add_argument("--metadata-json", required=True, type=Path)
    try:
        args = parser.parse_args()
        # Validate the public source before requesting hidden transport input.
        load_source_metadata(args.metadata_json, args.url)
        receipt = fetch_authorized_body(
            canonical_url=args.url,
            metadata_path=args.metadata_json,
            transport_url=read_hidden_transport_url(),
        )
    except SafeFetchError as error:
        diagnostic: dict[str, Any] = {"status": "failed", "category": error.category}
        if error.http_status is not None:
            diagnostic["http_status"] = error.http_status
        print(json.dumps(diagnostic), file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print('{"status":"failed","category":"cancelled"}', file=sys.stderr)
        return 1
    except Exception:
        # Neither a network library exception nor a traceback may expose URLs.
        print('{"status":"failed","category":"internal-error"}', file=sys.stderr)
        return 1
    print(json.dumps(receipt, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
