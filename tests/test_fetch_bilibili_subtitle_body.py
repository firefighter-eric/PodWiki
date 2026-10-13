from __future__ import annotations

import contextlib
import getpass
import io
import json
import sys
import tempfile
import unittest
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import fetch_bilibili_subtitle_body as fetcher  # noqa: E402


VIDEO_URL = "https://www.bilibili.com/video/BV1yFbo66E4q/"
# Synthetic test data only; never use a live transport capability as a fixture.
TRANSPORT_URL = (
    "https://aisubtitle.hdslb.com/bfs/ai_subtitle/example.json"
    "?auth_key=SYNTHETIC_TEST_SIGNATURE&other=kept"
)


def source_metadata() -> dict[str, Any]:
    return {
        "platform": "bilibili",
        "canonical_url": VIDEO_URL,
        "bvid": "BV1yFbo66E4q",
        "aid": 117124093713367,
        "cid": 41078688449,
        "page": 1,
        "duration_seconds": 120,
        "platform_metadata": {
            "bvid": "BV1yFbo66E4q",
            "aid": 117124093713367,
            "cid": 41078688449,
            "page": 1,
            "state": 0,
            "duration_seconds": 120,
            "rights": {
                "pay": 0,
                "ugc_pay": 0,
                "ugc_pay_preview": 0,
                "arc_pay": 0,
                "is_chargeable_season": False,
                "is_upower_exclusive": False,
                "is_upower_play": False,
            },
        },
    }


def payload(**overrides: object) -> bytes:
    document = {
        "type": "AIsubtitle",
        "lang": "zh",
        "body": [
            {"from": 0.04, "to": 2.6, "sid": 1, "content": "第一段"},
            {"from": 3, "to": 119.2, "sid": 2, "content": "第二段"},
        ],
        **overrides,
    }
    return json.dumps(document, ensure_ascii=False).encode("utf-8")


class Response(io.BytesIO):
    def __init__(self, body: bytes, *, length: str | None = None) -> None:
        super().__init__(body)
        self.status = 200
        self.headers = {} if length is None else {"Content-Length": length}


class FetchBilibiliSubtitleBodyTests(unittest.TestCase):
    def test_keeps_exact_signed_query_without_cookies_or_routing_override(self) -> None:
        opener = MagicMock()
        opener.open.return_value = Response(payload())
        with patch.object(fetcher.urllib.request, "build_opener", return_value=opener) as build:
            result = fetcher.download_body(TRANSPORT_URL)
        self.assertEqual(result, payload())
        request = opener.open.call_args.args[0]
        self.assertEqual(request.full_url, TRANSPORT_URL)
        self.assertIsNone(request.get_header("Cookie"))
        self.assertEqual(opener.open.call_args.kwargs["timeout"], 20)
        self.assertEqual(len(build.call_args.args), 1)
        self.assertIsInstance(build.call_args.args[0], fetcher.RejectRedirects)

    def test_rejects_wrong_origin_scheme_path_or_missing_signature(self) -> None:
        rejected = [
            TRANSPORT_URL.replace("https:", "http:"),
            TRANSPORT_URL.replace("aisubtitle.hdslb.com", "example.com"),
            TRANSPORT_URL.replace("aisubtitle.hdslb.com", "aisubtitle.hdslb.com.evil.test"),
            TRANSPORT_URL.replace("aisubtitle.hdslb.com", "user:pass@aisubtitle.hdslb.com"),
            TRANSPORT_URL.replace("aisubtitle.hdslb.com", "aisubtitle.hdslb.com:443"),
            TRANSPORT_URL.replace("/bfs/ai_subtitle/", "/elsewhere/"),
            TRANSPORT_URL.replace("example.json", "../example.json"),
            TRANSPORT_URL.replace("example.json", "%2e%2e/example.json"),
            TRANSPORT_URL.split("?", 1)[0],
            TRANSPORT_URL + "&auth_key=duplicate",
            TRANSPORT_URL + "#fragment",
            TRANSPORT_URL + "\n",
        ]
        for url in rejected:
            with self.subTest(url_kind=rejected.index(url)):
                with self.assertRaisesRegex(fetcher.SafeFetchError, "transport-url-rejected"):
                    fetcher.validate_transport_url(url)

    def test_rejects_redirect_even_to_same_host(self) -> None:
        handler = fetcher.RejectRedirects()
        for destination in [TRANSPORT_URL, "https://example.com/"]:
            with self.assertRaises(fetcher.SafeFetchError) as caught:
                handler.redirect_request(
                    urllib.request.Request(TRANSPORT_URL), None, 302, "Found", {}, destination
                )
            self.assertEqual(caught.exception.category, "redirect-rejected")
            self.assertEqual(caught.exception.http_status, 302)

    def test_sanitizes_http_and_transport_exceptions(self) -> None:
        exceptions = [
            urllib.error.HTTPError(TRANSPORT_URL, 403, "secret reason", {}, None),
            urllib.error.HTTPError(TRANSPORT_URL, 302, "secret redirect", {}, None),
            urllib.error.URLError(TRANSPORT_URL),
            OSError(TRANSPORT_URL),
            TimeoutError(TRANSPORT_URL),
        ]
        for error in exceptions:
            opener = MagicMock()
            opener.open.side_effect = error
            with patch.object(fetcher.urllib.request, "build_opener", return_value=opener):
                with self.assertRaises(fetcher.SafeFetchError) as caught:
                    fetcher.download_body(TRANSPORT_URL)
            self.assertNotIn("SYNTHETIC_TEST_SIGNATURE", str(caught.exception))
            self.assertNotIn("https://", str(caught.exception))
            if isinstance(error, urllib.error.HTTPError):
                self.assertEqual(caught.exception.http_status, error.code)

    def test_enforces_advertised_and_streamed_size_limit(self) -> None:
        for response in [Response(b"12345"), Response(b"12345", length="5")]:
            opener = MagicMock()
            opener.open.return_value = response
            with (
                patch.object(fetcher, "MAX_BODY_BYTES", 4),
                patch.object(fetcher.urllib.request, "build_opener", return_value=opener),
            ):
                with self.assertRaisesRegex(fetcher.SafeFetchError, "body-too-large"):
                    fetcher.download_body(TRANSPORT_URL)

    def test_rejects_short_body_and_total_time_limit(self) -> None:
        opener = MagicMock()
        opener.open.return_value = Response(b"123", length="4")
        with patch.object(fetcher.urllib.request, "build_opener", return_value=opener):
            with self.assertRaisesRegex(fetcher.SafeFetchError, "incomplete-response-body"):
                fetcher.download_body(TRANSPORT_URL)
        opener.open.return_value = Response(b"123")
        with (
            patch.object(fetcher.urllib.request, "build_opener", return_value=opener),
            patch.object(fetcher.time, "monotonic", side_effect=[0, 61]),
        ):
            with self.assertRaisesRegex(fetcher.SafeFetchError, "request-timeout"):
                fetcher.download_body(TRANSPORT_URL)

    def test_rejects_wrong_format_language_nonmonotonic_or_incomplete_body(self) -> None:
        bad_payloads = [
            b"not JSON containing SYNTHETIC_TEST_SIGNATURE",
            payload(type="publisher-caption"),
            payload(lang="en"),
            payload(body=[]),
            payload(body=[{"from": 45, "to": 119, "sid": 1, "content": "late"}]),
            payload(body=[{"from": 0, "to": 60, "sid": 1, "content": "short"}]),
            payload(
                body=[
                    {"from": 3, "to": 119, "sid": 2, "content": "late"},
                    {"from": 0, "to": 1, "sid": 1, "content": "early"},
                ]
            ),
            b'{"type":"AIsubtitle","type":"AIsubtitle","lang":"zh","body":[]}',
        ]
        for body in bad_payloads:
            with self.assertRaises(fetcher.SafeFetchError) as caught:
                fetcher.validate_body(body, source_metadata())
            self.assertEqual(str(caught.exception), "subtitle-body-rejected")
        self.assertEqual(len(fetcher.validate_body(payload(), source_metadata())), 2)

    def test_metadata_must_match_public_free_single_page_and_exact_bvid(self) -> None:
        (ROOT / ".cache").mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=ROOT / ".cache") as directory:
            path = Path(directory) / "source.metadata.json"
            valid = source_metadata()
            path.write_text(json.dumps({"source": valid}), encoding="utf-8")
            self.assertEqual(fetcher.load_source_metadata(path, VIDEO_URL), valid)
            for field, value in [
                ("bvid", "BV1different"),
                ("page", 2),
                ("page", True),
                ("cid", True),
            ]:
                path.write_text(json.dumps({"source": {**valid, field: value}}))
                with self.assertRaisesRegex(fetcher.SafeFetchError, "source-metadata-rejected"):
                    fetcher.load_source_metadata(path, VIDEO_URL)
            denied = source_metadata()
            denied["platform_metadata"]["rights"]["pay"] = 1
            path.write_text(json.dumps({"source": denied}))
            with self.assertRaisesRegex(fetcher.SafeFetchError, "source-metadata-rejected"):
                fetcher.load_source_metadata(path, VIDEO_URL)

    def test_rejects_missing_or_conflicting_nested_source_identity(self) -> None:
        (ROOT / ".cache").mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=ROOT / ".cache") as directory:
            path = Path(directory) / "source.metadata.json"
            for field, value in [
                ("bvid", "BV1different"),
                ("aid", 42),
                ("cid", 42),
                ("page", 2),
                ("page", True),
            ]:
                changed = source_metadata()
                changed["platform_metadata"][field] = value
                path.write_text(json.dumps({"source": changed}))
                with self.assertRaisesRegex(fetcher.SafeFetchError, "source-metadata-rejected"):
                    fetcher.load_source_metadata(path, VIDEO_URL)
            for field in ("bvid", "aid", "cid", "page"):
                missing = source_metadata()
                del missing["platform_metadata"][field]
                path.write_text(json.dumps({"source": missing}))
                with self.assertRaisesRegex(fetcher.SafeFetchError, "source-metadata-rejected"):
                    fetcher.load_source_metadata(path, VIDEO_URL)

    def test_atomic_cache_is_idempotent_and_never_overwrites_conflicting_body(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "subtitle.json"
            self.assertEqual(fetcher.write_body_without_overwrite(path, payload()), "saved")
            self.assertEqual(fetcher.write_body_without_overwrite(path, payload()), "reused")
            with self.assertRaisesRegex(fetcher.SafeFetchError, "body-cache-conflict"):
                fetcher.write_body_without_overwrite(path, b"different")
            self.assertEqual(path.read_bytes(), payload())
            self.assertEqual([item.name for item in path.parent.iterdir()], ["subtitle.json"])

    def test_rejects_symlink_cache_and_escape(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            with patch.object(fetcher, "ROOT", root):
                expected = root / ".cache/intake/BV1yFbo66E4q/subtitle.zh-CN.ai.json"
                self.assertEqual(fetcher.cache_destination("BV1yFbo66E4q"), expected)
                expected.parent.mkdir(parents=True)
                expected.symlink_to(root / "outside")
                with self.assertRaisesRegex(fetcher.SafeFetchError, "cache-destination-rejected"):
                    fetcher.cache_destination("BV1yFbo66E4q")

    def test_rejects_body_echoing_signature_without_writing_it(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with (
                patch.object(fetcher, "ROOT", root),
                patch.object(fetcher, "load_source_metadata", return_value=source_metadata()),
                patch.object(
                    fetcher,
                    "download_body",
                    return_value=payload(error_echo="SYNTHETIC_TEST_SIGNATURE"),
                ),
            ):
                with self.assertRaisesRegex(fetcher.SafeFetchError, "subtitle-body-rejected"):
                    fetcher.fetch_authorized_body(
                        canonical_url=VIDEO_URL,
                        metadata_path=root / "unused.json",
                        transport_url=TRANSPORT_URL,
                    )
            self.assertEqual(list(root.iterdir()), [])

    def test_rejects_json_escaped_secrets_in_nested_keys_and_strings(self) -> None:
        secret = "SYNTHETIC_TEST_SIGNATURE"
        escaped_signature = "".join(f"\\u{ord(character):04x}" for character in secret)
        escaped_url = TRANSPORT_URL.replace("/", "\\/").replace(secret, escaped_signature)
        variants = [
            payload(debug={"nested": [TRANSPORT_URL]}).replace(
                TRANSPORT_URL.encode(), escaped_url.encode()
            ),
            payload(debug={"nested": [secret]}).replace(
                secret.encode(), escaped_signature.encode()
            ),
            payload(debug={secret: "value"}).replace(secret.encode(), escaped_signature.encode()),
            payload(debug={"auth_key": "unrelated value"}).replace(b"auth_key", b"auth_\\u006bey"),
        ]
        for body in variants:
            with tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                with (
                    patch.object(fetcher, "ROOT", root),
                    patch.object(fetcher, "load_source_metadata", return_value=source_metadata()),
                    patch.object(fetcher, "download_body", return_value=body),
                ):
                    with self.assertRaises(fetcher.SafeFetchError) as caught:
                        fetcher.fetch_authorized_body(
                            canonical_url=VIDEO_URL,
                            metadata_path=root / "unused.json",
                            transport_url=TRANSPORT_URL,
                        )
                self.assertEqual(str(caught.exception), "subtitle-body-rejected")
                self.assertEqual(list(root.iterdir()), [])

    def test_refuses_non_tty_and_getpass_echo_fallback(self) -> None:
        with patch.object(fetcher.sys.stdin, "isatty", return_value=False):
            with self.assertRaisesRegex(fetcher.SafeFetchError, "interactive-terminal-required"):
                fetcher.read_hidden_transport_url()
        with (
            patch.object(fetcher.sys.stdin, "isatty", return_value=True),
            patch.object(fetcher.sys.stderr, "isatty", return_value=True),
            patch.object(fetcher.getpass, "getpass", side_effect=getpass.GetPassWarning("echo")),
        ):
            with self.assertRaisesRegex(fetcher.SafeFetchError, "hidden-input-unavailable"):
                fetcher.read_hidden_transport_url()

    def test_cli_never_echoes_unknown_arguments_or_invalid_signed_video_url(self) -> None:
        for arguments in [
            ["program", "--unexpected", TRANSPORT_URL],
            ["program", "--url", TRANSPORT_URL, "--metadata-json", "unread-path"],
        ]:
            stdout, stderr = io.StringIO(), io.StringIO()
            with (
                patch.object(fetcher.sys, "argv", arguments),
                contextlib.redirect_stdout(stdout),
                contextlib.redirect_stderr(stderr),
            ):
                self.assertEqual(fetcher.main(), 1)
            emitted = stdout.getvalue() + stderr.getvalue()
            self.assertNotIn("SYNTHETIC_TEST_SIGNATURE", emitted)
            self.assertNotIn("auth_key", emitted)
            self.assertNotIn("aisubtitle.hdslb.com", emitted)
            self.assertEqual(stdout.getvalue(), "")
            self.assertEqual(json.loads(stderr.getvalue())["status"], "failed")

    def test_success_receipt_contains_only_public_identity_and_body_facts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with (
                patch.object(fetcher, "ROOT", root),
                patch.object(fetcher, "load_source_metadata", return_value=source_metadata()),
                patch.object(fetcher, "download_body", return_value=payload()),
            ):
                receipt = fetcher.fetch_authorized_body(
                    canonical_url=VIDEO_URL,
                    metadata_path=root / "unused.json",
                    transport_url=TRANSPORT_URL,
                )
            encoded = json.dumps(receipt)
            self.assertNotIn("SYNTHETIC_TEST_SIGNATURE", encoded)
            self.assertNotIn("auth_key", encoded)
            self.assertEqual(receipt["canonical_url"], VIDEO_URL)
            self.assertEqual(receipt["cue_count"], 2)
            body = root / receipt["body_path"]
            self.assertEqual(body.read_bytes(), payload())


if __name__ == "__main__":
    unittest.main()
