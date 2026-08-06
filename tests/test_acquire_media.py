from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import call, patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from acquire_media import (  # noqa: E402
    available_javascript_runtime,
    bilibili_api_info,
    bilibili_platform_metadata,
    bilibili_public_audio,
    canonical_source_url,
    download_bilibili_public_audio,
    is_bilibili_extractor_compatibility_error,
    retain_existing_media,
    source_metadata,
    validate_bilibili_public_access,
)


def public_bilibili_metadata() -> dict[str, object]:
    return {
        "aid": 123,
        "bvid": "BV1Example",
        "cid": 456,
        "page": 1,
        "state": 0,
        "rights": {
            "download": 1,
            "no_reprint": 1,
            "pay": 0,
            "ugc_pay": 0,
            "ugc_pay_preview": 0,
            "arc_pay": 0,
            "is_chargeable_season": False,
            "is_upower_exclusive": False,
            "is_upower_play": False,
        },
    }


def bilibili_view_response() -> dict[str, object]:
    return {
        **public_bilibili_metadata(),
        "pages": [{"page": 1, "cid": 456, "part": "Public title"}],
        "title": "Public title",
        "desc": "Public description",
        "owner": {"mid": 789, "name": "Publisher"},
    }


def bilibili_player_response() -> dict[str, object]:
    return {
        "aid": 123,
        "bvid": "BV1Example",
        "cid": 456,
        "subtitle": {"subtitles": []},
        "view_points": [],
    }


class CanonicalSourceUrlTests(unittest.TestCase):
    def test_strips_bilibili_tracking_parameters(self) -> None:
        self.assertEqual(
            canonical_source_url(
                "https://www.bilibili.com/video/BV18Qg96YE1W/"
                "?spm_id_from=333.1387.homepage.video_card.click"
            ),
            ("bilibili", "https://www.bilibili.com/video/BV18Qg96YE1W/"),
        )

    def test_normalizes_youtube_watch_url(self) -> None:
        self.assertEqual(
            canonical_source_url(
                "https://www.youtube.com/watch?v=dQw4w9WgXcQ&utm_source=test"
            ),
            ("youtube", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
        )

    def test_normalizes_youtu_be_url(self) -> None:
        self.assertEqual(
            canonical_source_url("https://youtu.be/dQw4w9WgXcQ?t=10"),
            ("youtube", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
        )

    def test_rejects_non_video_bilibili_url(self) -> None:
        with self.assertRaisesRegex(ValueError, "Bilibili URL"):
            canonical_source_url("https://space.bilibili.com/14145636/")

    def test_rejects_multi_page_bilibili_url(self) -> None:
        with self.assertRaisesRegex(ValueError, "only page 1"):
            canonical_source_url(
                "https://www.bilibili.com/video/BV18Qg96YE1W/?p=2"
            )


class SourceMetadataTests(unittest.TestCase):
    def test_does_not_treat_danmaku_as_a_subtitle_track(self) -> None:
        metadata = source_metadata(
            {
                "id": "BV18Qg96YE1W",
                "subtitles": {"danmaku": [{"ext": "xml"}], "zh-CN": []},
            },
            platform="bilibili",
            canonical_url="https://www.bilibili.com/video/BV18Qg96YE1W/",
        )
        self.assertEqual(metadata["subtitle_languages"], ["zh-CN"])
        self.assertEqual(metadata["comment_stream_languages"], ["danmaku"])

    def test_builds_fallback_info_from_public_api_metadata(self) -> None:
        info = bilibili_api_info(
            {
                "aid": 123,
                "bvid": "BV1Example",
                "cid": 456,
                "page": 1,
                "title": "Public title",
                "description": "Public description",
                "published_timestamp": 1_700_000_000,
                "duration_seconds": 120,
                "owner": {"id": 789, "name": "Publisher"},
                "subtitle": {"tracks": []},
                "chapters": [],
            }
        )
        self.assertEqual(info["id"], "BV1Example")
        self.assertEqual(info["uploader_id"], "789")
        self.assertEqual(info["duration"], 120)
        self.assertEqual(info["extractor"], "BiliBiliPublicAPI")

    @patch("acquire_media.fetch_bilibili_api")
    def test_selects_highest_bandwidth_public_audio(self, fetch) -> None:
        fetch.return_value = {
            "timelength": 120_500,
            "dash": {
                "audio": [
                    {"id": 30216, "bandwidth": 64_000, "baseUrl": "https://a"},
                    {
                        "id": 30280,
                        "bandwidth": 128_000,
                        "baseUrl": "https://b",
                        "backupUrl": ["https://backup"],
                    },
                ]
            },
        }
        audio = bilibili_public_audio(public_bilibili_metadata())
        self.assertEqual(audio["format_id"], 30280)
        self.assertEqual(audio["urls"], ["https://b", "https://backup"])
        self.assertEqual(audio["duration_seconds"], 120.5)

    @patch("acquire_media.fetch_bilibili_api")
    def test_rejects_missing_public_audio(self, fetch) -> None:
        fetch.return_value = {"dash": {"audio": []}}
        with self.assertRaisesRegex(PermissionError, "no anonymous audio"):
            bilibili_public_audio(public_bilibili_metadata())


class BilibiliIdentityTests(unittest.TestCase):
    @patch("acquire_media.fetch_bilibili_api")
    def test_requires_matching_view_page_and_player_identity(self, fetch) -> None:
        fetch.side_effect = [bilibili_view_response(), bilibili_player_response()]

        metadata = bilibili_platform_metadata("BV1Example")

        self.assertEqual(
            (metadata["bvid"], metadata["aid"], metadata["cid"], metadata["page"]),
            ("BV1Example", 123, 456, 1),
        )
        self.assertEqual(
            fetch.call_args_list,
            [
                call("/x/web-interface/view", "bvid=BV1Example"),
                call("/x/player/v2", "bvid=BV1Example&cid=456"),
            ],
        )

    @patch("acquire_media.fetch_bilibili_api")
    def test_rejects_identity_mismatches(self, fetch) -> None:
        cases = []

        view = bilibili_view_response()
        view["bvid"] = "BV1Different"
        cases.append(("requested/view bvid", view, bilibili_player_response()))

        view = bilibili_view_response()
        view["pages"] = [{"page": 1, "cid": 999}]
        cases.append(("view/page cid", view, bilibili_player_response()))

        for field, value in (("bvid", "BV1Different"), ("aid", 999), ("cid", 999)):
            player = bilibili_player_response()
            player[field] = value
            cases.append((f"view/player {field}", bilibili_view_response(), player))

        for label, view, player in cases:
            with self.subTest(label=label):
                fetch.reset_mock()
                fetch.side_effect = [view, player]
                with self.assertRaisesRegex(ValueError, "mismatch"):
                    bilibili_platform_metadata("BV1Example")

    @patch("acquire_media.fetch_bilibili_api")
    def test_rejects_missing_critical_identity_fields(self, fetch) -> None:
        cases: list[tuple[str, dict[str, object], dict[str, object]]] = []
        for field in ("bvid", "aid", "cid"):
            view = bilibili_view_response()
            view.pop(field)
            cases.append((f"view {field}", view, bilibili_player_response()))

        view = bilibili_view_response()
        view["pages"] = [{"cid": 456}]
        cases.append(("page number", view, bilibili_player_response()))

        view = bilibili_view_response()
        view["pages"] = [{"page": 1}]
        cases.append(("page cid", view, bilibili_player_response()))

        for field in ("bvid", "aid", "cid"):
            player = bilibili_player_response()
            player.pop(field)
            cases.append((f"player {field}", bilibili_view_response(), player))

        for label, view, player in cases:
            with self.subTest(label=label):
                fetch.reset_mock()
                fetch.side_effect = [view, player]
                with self.assertRaises(ValueError):
                    bilibili_platform_metadata("BV1Example")


class BilibiliAccessTests(unittest.TestCase):
    def test_accepts_explicit_public_flags_without_treating_no_reprint_as_access(self) -> None:
        metadata = public_bilibili_metadata()
        validate_bilibili_public_access(metadata)

    def test_rejects_missing_or_invalid_state(self) -> None:
        for state in (None, True, "0", 1):
            metadata = public_bilibili_metadata()
            if state is None:
                metadata.pop("state")
            else:
                metadata["state"] = state
            with self.subTest(state=state), self.assertRaises(PermissionError):
                validate_bilibili_public_access(metadata)

    def test_rejects_missing_or_nonpublic_access_flags(self) -> None:
        for field in (
            "pay",
            "ugc_pay",
            "ugc_pay_preview",
            "arc_pay",
            "is_chargeable_season",
            "is_upower_exclusive",
            "is_upower_play",
        ):
            for value in (None, 1, True, "0"):
                metadata = public_bilibili_metadata()
                rights = metadata["rights"]
                self.assertIsInstance(rights, dict)
                if value is None:
                    rights.pop(field)
                else:
                    rights[field] = value
                with (
                    self.subTest(field=field, value=value),
                    self.assertRaises(PermissionError),
                ):
                    validate_bilibili_public_access(metadata)


class BilibiliFallbackTests(unittest.TestCase):
    def test_fallback_is_limited_to_known_initial_state_failure(self) -> None:
        self.assertTrue(
            is_bilibili_extractor_compatibility_error(
                RuntimeError(
                    "ERROR: [BiliBili] 1Ed7n6TEr1: Unable to extract initial state"
                )
            )
        )
        for error in (
            None,
            RuntimeError("login required"),
            RuntimeError("network timeout"),
            RuntimeError("extractor failed"),
        ):
            with self.subTest(error=error):
                self.assertFalse(is_bilibili_extractor_compatibility_error(error))

    def test_direct_download_retries_only_transport_download_errors(self) -> None:
        class TransportDownloadError(Exception):
            pass

        calls: list[str] = []
        with tempfile.TemporaryDirectory() as directory:
            expected_output = Path(directory) / "source.m4a"

            class Downloader:
                def __init__(self, options) -> None:
                    self.options = options

                def __enter__(self):
                    return self

                def __exit__(self, *args) -> None:
                    return None

                def download(self, urls) -> None:
                    calls.extend(urls)
                    if urls == ["https://primary"]:
                        raise TransportDownloadError("primary unavailable")
                    expected_output.write_bytes(b"audio")

            download_bilibili_public_audio(
                audio={"urls": ["https://primary", "https://backup"]},
                options={"match_filter": object()},
                canonical_url="https://www.bilibili.com/video/BV1Example/",
                expected_output=expected_output,
                downloader_type=Downloader,
                download_error_type=TransportDownloadError,
            )

        self.assertEqual(calls, ["https://primary", "https://backup"])

    def test_direct_download_preserves_nontransport_errors(self) -> None:
        class TransportDownloadError(Exception):
            pass

        for expected_error in (
            PermissionError("access denied"),
            OSError("disk full"),
            ValueError("programming error"),
        ):
            class Downloader:
                def __init__(self, options) -> None:
                    pass

                def __enter__(self):
                    return self

                def __exit__(self, *args) -> None:
                    return None

                def download(self, urls) -> None:
                    raise expected_error

            with self.subTest(error=type(expected_error).__name__):
                with self.assertRaises(type(expected_error)) as caught:
                    download_bilibili_public_audio(
                        audio={"urls": ["https://audio"]},
                        options={},
                        canonical_url=(
                            "https://www.bilibili.com/video/BV1Example/"
                        ),
                        expected_output=Path("does-not-exist.m4a"),
                        downloader_type=Downloader,
                        download_error_type=TransportDownloadError,
                    )
                self.assertIs(caught.exception, expected_error)


class RuntimeTests(unittest.TestCase):
    def test_prefers_deno_then_node(self) -> None:
        with patch(
            "acquire_media.shutil.which",
            side_effect=lambda name: f"/bin/{name}" if name in {"deno", "node"} else None,
        ):
            self.assertEqual(available_javascript_runtime(), "deno")

    def test_falls_back_to_node(self) -> None:
        with patch(
            "acquire_media.shutil.which",
            side_effect=lambda name: "/bin/node" if name == "node" else None,
        ):
            self.assertEqual(available_javascript_runtime(), "node")


class MetadataRetentionTests(unittest.TestCase):
    def test_metadata_inspection_preserves_existing_media_identity(self) -> None:
        document = {"inspected_at": "2026-08-05T00:00:00Z"}
        retain_existing_media(
            document,
            {
                "acquired_at": "2026-08-04T00:00:00Z",
                "media": {"sha256": "abc", "duration_ms": 1000},
            },
        )
        self.assertEqual(document["acquired_at"], "2026-08-04T00:00:00Z")
        self.assertEqual(
            document["media"], {"sha256": "abc", "duration_ms": 1000}
        )


if __name__ == "__main__":
    unittest.main()
