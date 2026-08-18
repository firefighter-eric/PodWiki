from __future__ import annotations

import copy
import hashlib
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from urllib.error import HTTPError, URLError
from unittest.mock import call, patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import acquire_media as acquire_module  # noqa: E402
from acquire_media import (  # noqa: E402
    acquisition_transaction_path,
    acquisition_resource_lock_path,
    available_javascript_runtime,
    bilibili_api_info,
    bilibili_platform_metadata,
    bilibili_public_audio,
    canonical_source_url,
    commit_acquired_media_pair,
    download_bilibili_public_audio,
    download_xiaoyuzhou_public_audio,
    exclusive_acquisition_locks,
    exclusive_download_lock,
    extract_xiaoyuzhou_next_data,
    fetch_xiaoyuzhou_next_data,
    is_bilibili_extractor_compatibility_error,
    main,
    parse_xiaoyuzhou_episode_metadata,
    refresh_existing_media,
    recover_acquisition_transaction,
    RejectRedirects,
    render_json_for_stdout,
    sha256_file,
    source_metadata,
    validate_bilibili_public_access,
    validate_public_enclosure_size,
    validate_reusable_source_identity,
    validate_output_path,
    validate_xiaoyuzhou_public_access,
    write_json_atomically,
    xiaoyuzhou_api_info,
    xiaoyuzhou_public_audio,
)


XIAOYUZHOU_EID = "6a6605846356eb2d9be8aa8c"
XIAOYUZHOU_PID = "6697cbecf103d7b06d18488b"
XIAOYUZHOU_MEDIA_ID = f"{XIAOYUZHOU_PID}/public-media.m4a"
XIAOYUZHOU_MEDIA_URL = (
    f"https://media.xyzcdn.net/{XIAOYUZHOU_MEDIA_ID}"
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


def xiaoyuzhou_episode_document() -> dict[str, object]:
    return {
        "props": {
            "pageProps": {
                "episode": {
                    "type": "EPISODE",
                    "eid": XIAOYUZHOU_EID,
                    "pid": XIAOYUZHOU_PID,
                    "title": "公开节目 & 跑步",
                    "description": "公开单集",
                    "pubDate": "2026-08-07T12:34:56.789Z",
                    "duration": 122.5,
                    "status": "NORMAL",
                    "payType": "FREE",
                    "isPrivateMedia": False,
                    "mediaKey": XIAOYUZHOU_MEDIA_ID,
                    "transcript": {"mediaId": XIAOYUZHOU_MEDIA_ID},
                    "transcriptMediaId": XIAOYUZHOU_MEDIA_ID,
                    "media": {
                        "id": XIAOYUZHOU_MEDIA_ID,
                        "size": 1_234_567,
                        "mimeType": "audio/mp4",
                        "source": {
                            "mode": "PUBLIC",
                            "url": XIAOYUZHOU_MEDIA_URL,
                        },
                    },
                    "enclosure": {"url": XIAOYUZHOU_MEDIA_URL},
                    "podcast": {
                        "pid": XIAOYUZHOU_PID,
                        "title": "跑步播客「大概纸示」",
                        "author": "大概指示",
                    },
                }
            }
        }
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

    def test_normalizes_xiaoyuzhou_episode_url(self) -> None:
        self.assertEqual(
            canonical_source_url(
                f"https://www.xiaoyuzhoufm.com/episode/{XIAOYUZHOU_EID}/"
                "?utm_source=test#comments"
            ),
            (
                "xiaoyuzhou",
                f"https://www.xiaoyuzhoufm.com/episode/{XIAOYUZHOU_EID}",
            ),
        )

    def test_rejects_non_video_bilibili_url(self) -> None:
        with self.assertRaisesRegex(ValueError, "Bilibili URL"):
            canonical_source_url("https://space.bilibili.com/14145636/")

    def test_rejects_multi_page_bilibili_url(self) -> None:
        with self.assertRaisesRegex(ValueError, "only page 1"):
            canonical_source_url(
                "https://www.bilibili.com/video/BV18Qg96YE1W/?p=2"
            )

    def test_rejects_xiaoyuzhou_podcast_url(self) -> None:
        with self.assertRaisesRegex(ValueError, "Xiaoyuzhou URL"):
            canonical_source_url(
                f"https://www.xiaoyuzhoufm.com/podcast/{XIAOYUZHOU_PID}"
            )


class XiaoyuzhouMetadataTests(unittest.TestCase):
    class Response:
        def __init__(
            self,
            body: bytes,
            *,
            content_type: str = "text/html; charset=utf-8",
            content_encoding: str | None = None,
            url: str | None = None,
        ) -> None:
            self.body = body
            self.headers = {"Content-Type": content_type}
            if content_encoding is not None:
                self.headers["Content-Encoding"] = content_encoding
            self.status = 200
            self.url = url or (
                f"https://www.xiaoyuzhoufm.com/episode/{XIAOYUZHOU_EID}"
            )
            self.offset = 0

        def __enter__(self):
            return self

        def __exit__(self, *args) -> None:
            return None

        def geturl(self) -> str:
            return self.url

        def read(self, size: int) -> bytes:
            chunk = self.body[self.offset : self.offset + size]
            self.offset += len(chunk)
            return chunk

    class Opener:
        def __init__(self, response) -> None:
            self.response = response
            self.requests = []

        def open(self, request, timeout: int):
            self.requests.append((request, timeout))
            return self.response

    def test_extracts_embedded_next_data_without_executing_scripts(self) -> None:
        document = xiaoyuzhou_episode_document()
        page = (
            "<!doctype html><script>window.unrelated = true</script>"
            '<script id="__NEXT_DATA__" type="application/json">'
            f"{json.dumps(document, ensure_ascii=False)}"
            "</script>"
        )
        self.assertEqual(extract_xiaoyuzhou_next_data(page), document)

    def test_fetches_only_the_canonical_html_page_without_redirects(self) -> None:
        document = xiaoyuzhou_episode_document()
        page = (
            '<script id="__NEXT_DATA__" type="application/json">'
            f"{json.dumps(document, ensure_ascii=False)}"
            "</script>"
        ).encode()
        response = self.Response(page)
        opener = self.Opener(response)

        with patch("acquire_media.build_opener", return_value=opener) as build:
            fetched = fetch_xiaoyuzhou_next_data(XIAOYUZHOU_EID)

        self.assertEqual(fetched, document)
        self.assertIsInstance(build.call_args.args[0], RejectRedirects)
        self.assertEqual(len(opener.requests), 1)
        self.assertEqual(
            opener.requests[0][0].get_header("Accept-encoding"), "identity"
        )

    def test_rejects_changed_page_url_before_reading_body(self) -> None:
        response = self.Response(
            b"must-not-be-read",
            url=f"https://example.com/episode/{XIAOYUZHOU_EID}",
        )
        with patch(
            "acquire_media.build_opener", return_value=self.Opener(response)
        ), self.assertRaisesRegex(PermissionError, "changed its canonical URL"):
            fetch_xiaoyuzhou_next_data(XIAOYUZHOU_EID)

        self.assertEqual(response.offset, 0)

    def test_rejects_non_html_and_oversized_episode_pages(self) -> None:
        wrong_type = self.Response(b"must-not-be-read", content_type="text/plain")
        with patch(
            "acquire_media.build_opener", return_value=self.Opener(wrong_type)
        ), self.assertRaisesRegex(ValueError, "is not HTML"):
            fetch_xiaoyuzhou_next_data(XIAOYUZHOU_EID)
        self.assertEqual(wrong_type.offset, 0)

        encoded = self.Response(b"must-not-be-read", content_encoding="gzip")
        with patch(
            "acquire_media.build_opener", return_value=self.Opener(encoded)
        ), self.assertRaisesRegex(ValueError, "unsupported encoding"):
            fetch_xiaoyuzhou_next_data(XIAOYUZHOU_EID)
        self.assertEqual(encoded.offset, 0)

        oversized = self.Response(b"123456789")
        with patch("acquire_media.XIAOYUZHOU_MAX_PAGE_BYTES", 8), patch(
            "acquire_media.build_opener", return_value=self.Opener(oversized)
        ), self.assertRaisesRegex(ValueError, "safe size limit"):
            fetch_xiaoyuzhou_next_data(XIAOYUZHOU_EID)

    def test_parses_matching_episode_podcast_and_media_identity(self) -> None:
        metadata = parse_xiaoyuzhou_episode_metadata(
            xiaoyuzhou_episode_document(), XIAOYUZHOU_EID
        )
        self.assertEqual(metadata["eid"], XIAOYUZHOU_EID)
        self.assertEqual(metadata["pid"], XIAOYUZHOU_PID)
        self.assertEqual(metadata["media"]["url"], XIAOYUZHOU_MEDIA_URL)
        self.assertEqual(metadata["published_timestamp"], 1_786_106_096)

    def test_real_transcript_media_stub_is_not_reported_as_subtitles(self) -> None:
        metadata = parse_xiaoyuzhou_episode_metadata(
            xiaoyuzhou_episode_document(), XIAOYUZHOU_EID
        )
        info = xiaoyuzhou_api_info(metadata)
        source = source_metadata(
            info,
            platform="xiaoyuzhou",
            canonical_url=(
                f"https://www.xiaoyuzhoufm.com/episode/{XIAOYUZHOU_EID}"
            ),
            platform_metadata=metadata,
        )

        self.assertEqual(metadata["subtitle"]["tracks"], [])
        self.assertEqual(
            metadata["subtitle"]["page_fields"]["transcript"],
            {"mediaId": XIAOYUZHOU_MEDIA_ID},
        )
        self.assertEqual(info["subtitles"], {})
        self.assertEqual(info["automatic_captions"], {})
        self.assertEqual(source["subtitle_languages"], [])
        self.assertEqual(source["automatic_caption_languages"], [])

    def test_preserves_and_discovers_public_transcript_tracks(self) -> None:
        document = xiaoyuzhou_episode_document()
        episode = document["props"]["pageProps"]["episode"]
        episode["transcript"] = {
            "tracks": [
                {
                    "language": "zh-CN",
                    "url": "https://public.example/transcript.zh-CN.vtt",
                    "format": "vtt",
                }
            ]
        }
        episode["automaticCaptions"] = {
            "en": [
                {
                    "text": "Public automatic caption text.",
                    "isAutomatic": True,
                }
            ]
        }

        metadata = parse_xiaoyuzhou_episode_metadata(document, XIAOYUZHOU_EID)
        info = xiaoyuzhou_api_info(metadata)
        source = source_metadata(
            info,
            platform="xiaoyuzhou",
            canonical_url=(
                f"https://www.xiaoyuzhoufm.com/episode/{XIAOYUZHOU_EID}"
            ),
            platform_metadata=metadata,
        )

        self.assertEqual(len(metadata["subtitle"]["tracks"]), 2)
        self.assertEqual(
            metadata["subtitle"]["tracks"][0]["url"],
            "https://public.example/transcript.zh-CN.vtt",
        )
        self.assertEqual(list(info["subtitles"]), ["zh-CN"])
        self.assertEqual(list(info["automatic_captions"]), ["en"])
        self.assertEqual(source["subtitle_languages"], ["zh-CN"])
        self.assertEqual(source["automatic_caption_languages"], ["en"])
        self.assertEqual(
            source["platform_metadata"]["subtitle"]["page_fields"][
                "automaticCaptions"
            ],
            episode["automaticCaptions"],
        )

    def test_rejects_unknown_ambiguous_or_malformed_transcript_fields(self) -> None:
        cases: list[tuple[str, dict[str, object], str]] = []

        document = xiaoyuzhou_episode_document()
        episode = document["props"]["pageProps"]["episode"]
        episode["subtitleBlob"] = {
            "url": "https://public.example/transcript.vtt"
        }
        cases.append(("unknown", document, "unknown transcript field"))

        document = xiaoyuzhou_episode_document()
        episode = document["props"]["pageProps"]["episode"]
        episode["subtitles"] = {"tracks": "not-a-list"}
        cases.append(("malformed tracks", document, "tracks is not a list"))

        document = xiaoyuzhou_episode_document()
        episode = document["props"]["pageProps"]["episode"]
        episode["transcript"] = {
            "mediaId": f"{XIAOYUZHOU_PID}/different-transcript.m4a"
        }
        cases.append(("ambiguous media id", document, "no explicit public text"))

        document = xiaoyuzhou_episode_document()
        episode = document["props"]["pageProps"]["episode"]
        episode["captions"] = [
            {"language": "zh-CN", "url": "http://public.example/captions.vtt"}
        ]
        cases.append(("non-https URL", document, "invalid public track URL"))

        for label, document, message in cases:
            with self.subTest(label=label), self.assertRaisesRegex(
                ValueError, message
            ):
                parse_xiaoyuzhou_episode_metadata(document, XIAOYUZHOU_EID)

    def test_rejects_identity_mismatches(self) -> None:
        cases: list[tuple[str, dict[str, object]]] = []

        document = xiaoyuzhou_episode_document()
        episode = document["props"]["pageProps"]["episode"]
        episode["eid"] = "6a6605846356eb2d9be8aa8d"
        cases.append(("requested/episode eid", document))

        document = xiaoyuzhou_episode_document()
        episode = document["props"]["pageProps"]["episode"]
        episode["podcast"]["pid"] = "6951e312febad13106eb017e"
        cases.append(("episode/podcast pid", document))

        document = xiaoyuzhou_episode_document()
        episode = document["props"]["pageProps"]["episode"]
        episode["media"]["id"] = "different-media"
        cases.append(("media id/key", document))

        for label, document in cases:
            with self.subTest(label=label), self.assertRaisesRegex(
                ValueError, "mismatch"
            ):
                parse_xiaoyuzhou_episode_metadata(document, XIAOYUZHOU_EID)

    def test_builds_common_info_and_public_audio(self) -> None:
        metadata = parse_xiaoyuzhou_episode_metadata(
            xiaoyuzhou_episode_document(), XIAOYUZHOU_EID
        )
        info = xiaoyuzhou_api_info(metadata)
        audio = xiaoyuzhou_public_audio(metadata)

        self.assertEqual(info["id"], XIAOYUZHOU_EID)
        self.assertEqual(info["channel_id"], XIAOYUZHOU_PID)
        self.assertEqual(info["extractor"], "XiaoyuzhouPublicPage")
        self.assertEqual(info["subtitles"], {})
        self.assertEqual(info["automatic_captions"], {})
        self.assertEqual(audio["urls"], [XIAOYUZHOU_MEDIA_URL])
        self.assertEqual(audio["filesize"], 1_234_567)

    def test_stdout_json_escapes_values_unsupported_by_console_encoding(self) -> None:
        document = {"title": "越野跑 🍠"}

        rendered = render_json_for_stdout(document, encoding="gbk")

        self.assertEqual(json.loads(rendered), document)
        self.assertIn("\\ud83c\\udf60", rendered)

    def test_stdout_json_stays_readable_with_utf8_output(self) -> None:
        document = {"title": "越野跑 🍠"}

        rendered = render_json_for_stdout(document, encoding="utf-8")

        self.assertIn("越野跑 🍠", rendered)


class XiaoyuzhouAccessTests(unittest.TestCase):
    def metadata(self) -> dict[str, object]:
        return parse_xiaoyuzhou_episode_metadata(
            xiaoyuzhou_episode_document(), XIAOYUZHOU_EID
        )

    def test_accepts_explicit_free_public_m4a(self) -> None:
        validate_xiaoyuzhou_public_access(self.metadata())

    def test_rejects_paid_private_or_nonpublic_media(self) -> None:
        for path, value in (
            (("pay_type",), "PAY_EPISODE"),
            (("is_private_media",), True),
            (("media", "mode"), "PRIVATE"),
            (("media", "url"), None),
        ):
            metadata = copy.deepcopy(self.metadata())
            target = metadata
            for key in path[:-1]:
                target = target[key]
            target[path[-1]] = value
            with self.subTest(path=path), self.assertRaises(PermissionError):
                validate_xiaoyuzhou_public_access(metadata)

    def test_rejects_unapproved_or_inconsistent_enclosures(self) -> None:
        for field, value in (
            ("media_url", "https://example.com/public-media.m4a"),
            ("enclosure_url", "https://media.xyzcdn.net/other.m4a"),
            ("mime_type", "audio/mpeg"),
            ("size_bytes", 0),
        ):
            metadata = copy.deepcopy(self.metadata())
            media = metadata["media"]
            if field == "media_url":
                media["url"] = value
            elif field == "enclosure_url":
                metadata["enclosure_url"] = value
            else:
                media[field] = value
            expected_error = PermissionError if field == "media_url" else ValueError
            with self.subTest(field=field), self.assertRaises(expected_error):
                validate_xiaoyuzhou_public_access(metadata)

    def test_binds_media_id_and_cdn_path_to_episode_podcast(self) -> None:
        other_pid = "6951e312febad13106eb017e"
        other_media_id = f"{other_pid}/public-media.m4a"
        metadata = copy.deepcopy(self.metadata())
        metadata["media"]["id"] = other_media_id
        metadata["media"]["url"] = f"https://media.xyzcdn.net/{other_media_id}"
        metadata["enclosure_url"] = metadata["media"]["url"]

        with self.assertRaisesRegex(ValueError, "identity mismatch"):
            validate_xiaoyuzhou_public_access(metadata)

    def test_requires_media_url_path_to_equal_media_id(self) -> None:
        metadata = copy.deepcopy(self.metadata())
        other_url = f"https://media.xyzcdn.net/{XIAOYUZHOU_PID}/other.m4a"
        metadata["media"]["url"] = other_url
        metadata["enclosure_url"] = other_url

        with self.assertRaisesRegex(PermissionError, "approved public CDN"):
            validate_xiaoyuzhou_public_access(metadata)

    def test_validates_downloaded_enclosure_size(self) -> None:
        metadata = self.metadata()
        with self.assertRaisesRegex(ValueError, "size differs"):
            validate_public_enclosure_size(
                {"duration_ms": 122_500, "size_bytes": 1_234_566},
                platform_metadata=metadata,
            )


class SourceMetadataTests(unittest.TestCase):
    def test_records_case_sensitive_youtube_video_id(self) -> None:
        metadata = source_metadata(
            {
                "id": "-RXD4bTuFTo",
                "channel_id": "UCXl4i9dYBrFOabk0xGmbkRA",
            },
            platform="youtube",
            canonical_url="https://www.youtube.com/watch?v=-RXD4bTuFTo",
        )
        self.assertEqual(metadata["video_id"], "-RXD4bTuFTo")

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

    def test_records_xiaoyuzhou_episode_and_podcast_ids(self) -> None:
        metadata = parse_xiaoyuzhou_episode_metadata(
            xiaoyuzhou_episode_document(), XIAOYUZHOU_EID
        )
        info = xiaoyuzhou_api_info(metadata)
        source = source_metadata(
            info,
            platform="xiaoyuzhou",
            canonical_url=(
                f"https://www.xiaoyuzhoufm.com/episode/{XIAOYUZHOU_EID}"
            ),
            platform_metadata=metadata,
        )
        self.assertEqual(source["eid"], XIAOYUZHOU_EID)
        self.assertEqual(source["pid"], XIAOYUZHOU_PID)
        self.assertEqual(source["media_id"], XIAOYUZHOU_MEDIA_ID)

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


class XiaoyuzhouDownloadTests(unittest.TestCase):
    ETAG = '"public-media-v1"'

    @staticmethod
    def partial_path(output: Path) -> Path:
        identity = hashlib.sha256(XIAOYUZHOU_MEDIA_URL.encode("utf-8")).hexdigest()[:16]
        return output.with_name(f".{output.name}.{identity}.part")

    @classmethod
    def checkpoint_path(cls, output: Path) -> Path:
        partial = cls.partial_path(output)
        return partial.with_suffix(f"{partial.suffix}.checkpoint.json")

    @classmethod
    def write_checkpoint(
        cls, output: Path, *, expected_size: int, etag: str
    ) -> None:
        partial = cls.partial_path(output)
        cls.checkpoint_path(output).write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "media_url": XIAOYUZHOU_MEDIA_URL,
                    "expected_size": expected_size,
                    "etag": etag,
                    "size_bytes": partial.stat().st_size,
                    "sha256": hashlib.sha256(partial.read_bytes()).hexdigest(),
                }
            ),
            encoding="utf-8",
        )

    class Response:
        def __init__(
            self,
            body: bytes,
            *,
            status: int,
            headers: dict[str, str],
            url: str = XIAOYUZHOU_MEDIA_URL,
        ) -> None:
            self.body = body
            self.status = status
            self.headers = headers
            self.url = url
            self.offset = 0

        def __enter__(self):
            return self

        def __exit__(self, *args) -> None:
            return None

        def geturl(self) -> str:
            return self.url

        def read(self, size: int) -> bytes:
            chunk = self.body[self.offset : self.offset + size]
            self.offset += len(chunk)
            return chunk

    class Opener:
        def __init__(self, responses) -> None:
            self.responses = list(responses)
            self.requests = []

        def open(self, request, timeout: int):
            self.requests.append((request, timeout))
            response = self.responses.pop(0)
            if isinstance(response, Exception):
                raise response
            return response

    class InterruptedResponse(Response):
        def __init__(self, first_chunk: bytes, *, headers: dict[str, str]) -> None:
            super().__init__(b"", status=200, headers=headers)
            self.first_chunk = first_chunk
            self.read_count = 0

        def read(self, size: int) -> bytes:
            self.read_count += 1
            if self.read_count == 1:
                return self.first_chunk
            raise URLError("connection interrupted")

    def test_downloads_atomically_with_redirects_disabled(self) -> None:
        body = b"public-media"
        response = self.Response(
            body,
            status=200,
            headers={
                "Content-Length": str(len(body)),
                "Content-Type": "audio/mp4; charset=binary",
                "ETag": self.ETAG,
            },
        )
        opener = self.Opener([response])
        with tempfile.TemporaryDirectory() as directory, patch(
            "acquire_media.build_opener", return_value=opener
        ) as build:
            output = Path(directory) / "source.m4a"

            download_xiaoyuzhou_public_audio(
                audio={"urls": [XIAOYUZHOU_MEDIA_URL], "filesize": len(body)},
                canonical_url=f"https://www.xiaoyuzhoufm.com/episode/{XIAOYUZHOU_EID}",
                expected_output=output,
            )

            self.assertEqual(output.read_bytes(), body)
            self.assertFalse(self.partial_path(output).exists())
            self.assertIsInstance(build.call_args.args[0], RejectRedirects)
            self.assertIsNone(opener.requests[0][0].get_header("Range"))
            self.assertEqual(
                opener.requests[0][0].get_header("Accept-encoding"), "identity"
            )

    def test_resumes_only_with_matching_range_response(self) -> None:
        prefix = b"public-"
        suffix = b"media"
        total = len(prefix) + len(suffix)
        response = self.Response(
            suffix,
            status=206,
            headers={
                "Content-Length": str(len(suffix)),
                "Content-Range": f"bytes {len(prefix)}-{total - 1}/{total}",
                "Content-Type": "audio/mp4",
                "ETag": self.ETAG,
            },
        )
        opener = self.Opener([response])
        with tempfile.TemporaryDirectory() as directory, patch(
            "acquire_media.build_opener", return_value=opener
        ):
            output = Path(directory) / "source.m4a"
            partial = self.partial_path(output)
            partial.write_bytes(prefix)
            self.write_checkpoint(output, expected_size=total, etag=self.ETAG)

            download_xiaoyuzhou_public_audio(
                audio={"urls": [XIAOYUZHOU_MEDIA_URL], "filesize": total},
                canonical_url=f"https://www.xiaoyuzhoufm.com/episode/{XIAOYUZHOU_EID}",
                expected_output=output,
            )

            self.assertEqual(output.read_bytes(), prefix + suffix)
            self.assertEqual(
                opener.requests[0][0].get_header("Range"),
                f"bytes={len(prefix)}-",
            )
            self.assertEqual(
                opener.requests[0][0].get_header("If-range"), self.ETAG
            )

    def test_corrupt_partial_checkpoint_is_discarded_before_resume(self) -> None:
        prefix = b"public-"
        body = prefix + b"media"
        response = self.Response(
            body,
            status=200,
            headers={
                "Content-Length": str(len(body)),
                "Content-Type": "audio/mp4",
                "ETag": self.ETAG,
            },
        )
        opener = self.Opener([response])

        with tempfile.TemporaryDirectory() as directory, patch(
            "acquire_media.build_opener", return_value=opener
        ):
            output = Path(directory) / "source.m4a"
            partial = self.partial_path(output)
            partial.write_bytes(prefix)
            self.write_checkpoint(output, expected_size=len(body), etag=self.ETAG)
            partial.write_bytes(b"publjc-")

            download_xiaoyuzhou_public_audio(
                audio={"urls": [XIAOYUZHOU_MEDIA_URL], "filesize": len(body)},
                canonical_url=f"https://www.xiaoyuzhoufm.com/episode/{XIAOYUZHOU_EID}",
                expected_output=output,
            )
            downloaded = output.read_bytes()

        self.assertEqual(downloaded, body)
        self.assertIsNone(opener.requests[0][0].get_header("Range"))

    def test_interrupted_transfer_resumes_with_if_range(self) -> None:
        prefix = b"public-"
        suffix = b"media"
        total = len(prefix) + len(suffix)
        interrupted = self.InterruptedResponse(
            prefix,
            headers={
                "Content-Length": str(total),
                "Content-Type": "audio/mp4",
                "ETag": self.ETAG,
            },
        )
        resumed = self.Response(
            suffix,
            status=206,
            headers={
                "Content-Length": str(len(suffix)),
                "Content-Range": f"bytes {len(prefix)}-{total - 1}/{total}",
                "Content-Type": "audio/mp4",
                "ETag": self.ETAG,
            },
        )
        opener = self.Opener([interrupted, resumed])

        with tempfile.TemporaryDirectory() as directory, patch(
            "acquire_media.build_opener", return_value=opener
        ), patch("acquire_media.time.sleep"):
            output = Path(directory) / "source.m4a"
            download_xiaoyuzhou_public_audio(
                audio={"urls": [XIAOYUZHOU_MEDIA_URL], "filesize": total},
                canonical_url=f"https://www.xiaoyuzhoufm.com/episode/{XIAOYUZHOU_EID}",
                expected_output=output,
            )
            downloaded = output.read_bytes()

        self.assertEqual(downloaded, prefix + suffix)
        self.assertIsNone(opener.requests[0][0].get_header("Range"))
        self.assertEqual(
            opener.requests[1][0].get_header("Range"), f"bytes={len(prefix)}-"
        )
        self.assertEqual(
            opener.requests[1][0].get_header("If-range"), self.ETAG
        )

    def test_changed_etag_discards_partial_and_restarts(self) -> None:
        prefix = b"old-"
        body = b"new-public-media"
        changed = self.Response(
            b"must-not-be-read",
            status=206,
            headers={
                "Content-Length": str(len(body) - len(prefix)),
                "Content-Range": f"bytes {len(prefix)}-{len(body) - 1}/{len(body)}",
                "Content-Type": "audio/mp4",
                "ETag": '"public-media-v2"',
            },
        )
        restarted = self.Response(
            body,
            status=200,
            headers={
                "Content-Length": str(len(body)),
                "Content-Type": "audio/mp4",
                "ETag": '"public-media-v2"',
            },
        )
        opener = self.Opener([changed, restarted])

        with tempfile.TemporaryDirectory() as directory, patch(
            "acquire_media.build_opener", return_value=opener
        ):
            output = Path(directory) / "source.m4a"
            partial = self.partial_path(output)
            partial.write_bytes(prefix)
            self.write_checkpoint(output, expected_size=len(body), etag=self.ETAG)
            download_xiaoyuzhou_public_audio(
                audio={"urls": [XIAOYUZHOU_MEDIA_URL], "filesize": len(body)},
                canonical_url=f"https://www.xiaoyuzhoufm.com/episode/{XIAOYUZHOU_EID}",
                expected_output=output,
            )
            downloaded = output.read_bytes()

        self.assertEqual(downloaded, body)
        self.assertEqual(changed.offset, 0)
        self.assertEqual(opener.requests[0][0].get_header("Range"), "bytes=4-")
        self.assertIsNone(opener.requests[1][0].get_header("Range"))

    def test_complete_transfer_does_not_require_an_etag(self) -> None:
        body = b"public-media"
        response = self.Response(
            body,
            status=200,
            headers={
                "Content-Length": str(len(body)),
                "Content-Type": "audio/mp4",
            },
        )
        opener = self.Opener([response])

        with tempfile.TemporaryDirectory() as directory, patch(
            "acquire_media.build_opener", return_value=opener
        ):
            output = Path(directory) / "source.m4a"
            download_xiaoyuzhou_public_audio(
                audio={"urls": [XIAOYUZHOU_MEDIA_URL], "filesize": len(body)},
                canonical_url=f"https://www.xiaoyuzhoufm.com/episode/{XIAOYUZHOU_EID}",
                expected_output=output,
            )
            downloaded = output.read_bytes()
            partial_exists = self.partial_path(output).exists()

        self.assertEqual(downloaded, body)
        self.assertFalse(partial_exists)

    def test_completed_resume_survives_checkpoint_cleanup_failure(self) -> None:
        prefix = b"public-"
        suffix = b"media"
        total = len(prefix) + len(suffix)
        response = self.Response(
            suffix,
            status=206,
            headers={
                "Content-Length": str(len(suffix)),
                "Content-Range": f"bytes {len(prefix)}-{total - 1}/{total}",
                "Content-Type": "audio/mp4",
                "ETag": self.ETAG,
            },
        )
        opener = self.Opener([response])
        real_unlink = Path.unlink

        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "source.m4a"
            partial = self.partial_path(output)
            checkpoint = self.checkpoint_path(output)
            partial.write_bytes(prefix)
            self.write_checkpoint(output, expected_size=total, etag=self.ETAG)

            def fail_checkpoint_cleanup(path: Path, *args, **kwargs):
                if path == checkpoint:
                    raise PermissionError("temporarily locked")
                return real_unlink(path, *args, **kwargs)

            with (
                patch("acquire_media.build_opener", return_value=opener),
                patch(
                    "pathlib.Path.unlink",
                    autospec=True,
                    side_effect=fail_checkpoint_cleanup,
                ),
            ):
                download_xiaoyuzhou_public_audio(
                    audio={"urls": [XIAOYUZHOU_MEDIA_URL], "filesize": total},
                    canonical_url=(
                        f"https://www.xiaoyuzhoufm.com/episode/{XIAOYUZHOU_EID}"
                    ),
                    expected_output=output,
                )

            self.assertEqual(output.read_bytes(), prefix + suffix)
            self.assertTrue(checkpoint.is_file())

    def test_rejects_encoded_media_response_before_reading(self) -> None:
        body = b"public-media"
        response = self.Response(
            body,
            status=200,
            headers={
                "Content-Length": str(len(body)),
                "Content-Type": "audio/mp4",
                "Content-Encoding": "gzip",
            },
        )
        opener = self.Opener([response])

        with tempfile.TemporaryDirectory() as directory, patch(
            "acquire_media.build_opener", return_value=opener
        ), self.assertRaisesRegex(ValueError, "unsupported content encoding"):
            download_xiaoyuzhou_public_audio(
                audio={"urls": [XIAOYUZHOU_MEDIA_URL], "filesize": len(body)},
                canonical_url=f"https://www.xiaoyuzhoufm.com/episode/{XIAOYUZHOU_EID}",
                expected_output=Path(directory) / "source.m4a",
            )

        self.assertEqual(response.offset, 0)

    def test_retries_transient_http_status_but_not_permanent_4xx(self) -> None:
        body = b"public-media"
        successful = self.Response(
            body,
            status=200,
            headers={
                "Content-Length": str(len(body)),
                "Content-Type": "audio/mp4",
            },
        )
        transient_fp = io.BytesIO(b"unavailable")
        transient = HTTPError(
            XIAOYUZHOU_MEDIA_URL, 503, "Unavailable", {}, transient_fp
        )
        opener = self.Opener([transient, successful])
        with tempfile.TemporaryDirectory() as directory, patch(
            "acquire_media.build_opener", return_value=opener
        ), patch("acquire_media.time.sleep") as sleep:
            output = Path(directory) / "source.m4a"
            download_xiaoyuzhou_public_audio(
                audio={"urls": [XIAOYUZHOU_MEDIA_URL], "filesize": len(body)},
                canonical_url=f"https://www.xiaoyuzhoufm.com/episode/{XIAOYUZHOU_EID}",
                expected_output=output,
            )
            downloaded = output.read_bytes()
        self.assertEqual(downloaded, body)
        self.assertEqual(len(opener.requests), 2)
        sleep.assert_called_once_with(1)
        self.assertTrue(transient_fp.closed)

        permanent_fp = io.BytesIO(b"not found")
        permanent = HTTPError(
            XIAOYUZHOU_MEDIA_URL, 404, "Not Found", {}, permanent_fp
        )
        opener = self.Opener([permanent, successful])
        with tempfile.TemporaryDirectory() as directory, patch(
            "acquire_media.build_opener", return_value=opener
        ), self.assertRaises(HTTPError):
            download_xiaoyuzhou_public_audio(
                audio={"urls": [XIAOYUZHOU_MEDIA_URL], "filesize": len(body)},
                canonical_url=f"https://www.xiaoyuzhoufm.com/episode/{XIAOYUZHOU_EID}",
                expected_output=Path(directory) / "source.m4a",
            )
        self.assertEqual(len(opener.requests), 1)
        self.assertTrue(permanent_fp.closed)

    def test_local_write_failure_is_not_retried(self) -> None:
        body = b"public-media"
        response = self.Response(
            body,
            status=200,
            headers={
                "Content-Length": str(len(body)),
                "Content-Type": "audio/mp4",
            },
        )
        opener = self.Opener([response])
        real_path_open = Path.open

        def fail_partial_write(path: Path, *args, **kwargs):
            if path.name.endswith(".part"):
                raise OSError("disk full")
            return real_path_open(path, *args, **kwargs)

        with (
            tempfile.TemporaryDirectory() as directory,
            patch("acquire_media.build_opener", return_value=opener),
            patch(
                "pathlib.Path.open",
                autospec=True,
                side_effect=fail_partial_write,
            ),
            self.assertRaisesRegex(OSError, "disk full"),
        ):
            download_xiaoyuzhou_public_audio(
                audio={"urls": [XIAOYUZHOU_MEDIA_URL], "filesize": len(body)},
                canonical_url=f"https://www.xiaoyuzhoufm.com/episode/{XIAOYUZHOU_EID}",
                expected_output=Path(directory) / "source.m4a",
            )
        self.assertEqual(len(opener.requests), 1)

    def test_rejects_changed_response_url_before_reading_body(self) -> None:
        response = self.Response(
            b"must-not-be-read",
            status=200,
            headers={
                "Content-Length": "16",
                "Content-Type": "audio/mp4",
                "ETag": self.ETAG,
            },
            url="https://example.com/redirected.m4a",
        )
        opener = self.Opener([response])
        with tempfile.TemporaryDirectory() as directory, patch(
            "acquire_media.build_opener", return_value=opener
        ):
            with self.assertRaisesRegex(PermissionError, "changed enclosure URL"):
                download_xiaoyuzhou_public_audio(
                    audio={"urls": [XIAOYUZHOU_MEDIA_URL], "filesize": 16},
                    canonical_url=(
                        f"https://www.xiaoyuzhoufm.com/episode/{XIAOYUZHOU_EID}"
                    ),
                    expected_output=Path(directory) / "source.m4a",
                )

        self.assertEqual(response.offset, 0)

    def test_redirect_handler_refuses_redirect_request(self) -> None:
        class RedirectResponse:
            closed = False

            def close(self) -> None:
                self.closed = True

        response = RedirectResponse()
        with self.assertRaisesRegex(PermissionError, "redirects are unsupported"):
            RejectRedirects().redirect_request(
                None, response, 302, "Found", {}, "https://example.com/media.m4a"
            )
        self.assertTrue(response.closed)

    def test_same_output_has_an_exclusive_process_lock(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            lock_path = Path(directory) / ".source.m4a.lock"
            with exclusive_download_lock(lock_path):
                with self.assertRaisesRegex(FileExistsError, "already using"):
                    with exclusive_download_lock(lock_path):
                        self.fail("second lock unexpectedly succeeded")

    def test_final_audio_and_sidecar_resources_are_locked_independently(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            audio_a = root / "a.m4a"
            audio_b = root / "b.m4a"
            metadata_a = root / "a.metadata.json"
            metadata_b = root / "b.metadata.json"

            with exclusive_acquisition_locks([audio_a, metadata_a]):
                for competing_resources in (
                    [audio_a, metadata_b],
                    [audio_b, metadata_a],
                ):
                    with self.subTest(resources=competing_resources):
                        with self.assertRaisesRegex(FileExistsError, "already using"):
                            with exclusive_acquisition_locks(competing_resources):
                                self.fail("a shared final resource was not locked")
                with exclusive_acquisition_locks([audio_b, metadata_b]):
                    pass

    @unittest.skipUnless(sys.platform == "win32", "Windows path alias regression")
    def test_windows_extended_path_alias_uses_the_same_resource_lock(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            normal_path = Path(directory) / "future.metadata.json"
            extended_path = Path(f"\\\\?\\{normal_path}")

            with exclusive_download_lock(
                acquisition_resource_lock_path(normal_path)
            ):
                with self.assertRaisesRegex(FileExistsError, "already using"):
                    with exclusive_download_lock(
                        acquisition_resource_lock_path(extended_path)
                    ):
                        self.fail("a Windows path alias bypassed the resource lock")

    def test_resource_locks_follow_filesystem_case_and_unicode_semantics(self) -> None:
        name_pairs = (
            ("Audio.m4a", "audio.m4a"),
            ("straße.m4a", "strasse.m4a"),
            ("é.m4a", "e\N{COMBINING ACUTE ACCENT}.m4a"),
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for first_name, second_name in name_pairs:
                first = root / first_name
                second = root / second_name
                first.write_bytes(b"first")
                second.write_bytes(b"second")
                same_resource = os.path.samefile(first, second)

                with self.subTest(first=first_name, second=second_name):
                    with exclusive_download_lock(
                        acquisition_resource_lock_path(first)
                    ):
                        second_lock = acquisition_resource_lock_path(second)
                        if same_resource:
                            with self.assertRaisesRegex(
                                FileExistsError, "already using"
                            ):
                                with exclusive_download_lock(second_lock):
                                    self.fail("one resource received two locks")
                        else:
                            with exclusive_download_lock(second_lock):
                                pass


class RuntimeTests(unittest.TestCase):
    def test_requires_exact_lowercase_m4a_output_suffix(self) -> None:
        validate_output_path(Path("source.m4a"))
        for path in (Path("source.M4A"), Path("source.mp3"), Path("source")):
            with self.subTest(path=path), self.assertRaisesRegex(
                ValueError, "lowercase .m4a"
            ):
                validate_output_path(path)

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


class AcquisitionTransactionTests(unittest.TestCase):
    def test_prepare_failure_keeps_unique_staging_and_final_targets_untouched(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            staged = root / ".downloads" / "episode" / "source.m4a"
            staged.parent.mkdir(parents=True)
            staged_bytes = b"unique verified staged audio"
            staged.write_bytes(staged_bytes)
            output = root / "source.m4a"
            sidecar = root / "source.metadata.json"
            document = {
                "schema_version": 1,
                "kind": "podwiki-source-media",
                "media": {"sha256": hashlib.sha256(staged_bytes).hexdigest()},
            }

            def fail_before_journal(path: Path, payload: object) -> None:
                self.assertEqual(
                    path,
                    acquisition_transaction_path(
                        output_path=output,
                        metadata_output=sidecar,
                    ),
                )
                self.assertIsInstance(payload, dict)
                if not isinstance(payload, dict):
                    raise AssertionError("transaction payload must be a mapping")
                artifacts = payload.get("artifacts")
                if not isinstance(artifacts, dict):
                    raise AssertionError("transaction artifacts must be a mapping")
                media = artifacts.get("media")
                if not isinstance(media, dict):
                    raise AssertionError("transaction media must be a mapping")
                prepared = Path(str(media.get("temporary")))
                self.assertEqual(staged.read_bytes(), staged_bytes)
                self.assertEqual(prepared.read_bytes(), staged_bytes)
                self.assertFalse(output.exists())
                self.assertFalse(sidecar.exists())
                raise OSError("injected failure before journal commit")

            with patch(
                "acquire_media.write_json_atomically",
                side_effect=fail_before_journal,
            ), self.assertRaisesRegex(OSError, "before journal"):
                commit_acquired_media_pair(
                    staged_audio=staged,
                    output_path=output,
                    metadata_output=sidecar,
                    document=document,
                )

            self.assertEqual(staged.read_bytes(), staged_bytes)
            self.assertFalse(output.exists())
            self.assertFalse(sidecar.exists())
            self.assertFalse(
                acquisition_transaction_path(
                    output_path=output,
                    metadata_output=sidecar,
                ).exists()
            )
            self.assertEqual(list(root.rglob(".podwiki-*.tmp")), [])

    def test_recovers_audio_and_sidecar_after_second_promotion_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            staged = root / ".downloads" / "episode" / "source.m4a"
            staged.parent.mkdir(parents=True)
            staged.write_bytes(b"verified staged audio")
            output = root / "source.m4a"
            sidecar = root / "source.metadata.json"
            document = {
                "schema_version": 1,
                "kind": "podwiki-source-media",
                "media": {"sha256": sha256_file(staged)},
            }
            original_promote = acquire_module.promote_acquisition_artifact
            promotion_count = 0

            def fail_second_promotion(temporary: Path, target: Path) -> None:
                nonlocal promotion_count
                promotion_count += 1
                if promotion_count == 2:
                    raise OSError("injected sidecar promotion failure")
                original_promote(temporary, target)

            with patch(
                "acquire_media.promote_acquisition_artifact",
                side_effect=fail_second_promotion,
            ), self.assertRaisesRegex(OSError, "injected"):
                commit_acquired_media_pair(
                    staged_audio=staged,
                    output_path=output,
                    metadata_output=sidecar,
                    document=document,
                )

            journal = acquisition_transaction_path(
                output_path=output,
                metadata_output=sidecar,
            )
            self.assertTrue(output.is_file())
            self.assertFalse(sidecar.exists())
            self.assertTrue(journal.is_file())
            self.assertTrue(
                recover_acquisition_transaction(
                    output_path=output,
                    metadata_output=sidecar,
                )
            )
            self.assertEqual(json.loads(sidecar.read_text("utf-8")), document)
            self.assertFalse(journal.exists())
            self.assertEqual(list(root.rglob(".podwiki-*.tmp")), [])

    def test_recovery_rejects_target_or_external_temporary_without_mutation(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target_directory = root / "targets"
            target_directory.mkdir()
            output = target_directory / "source.m4a"
            sidecar = target_directory / "source.metadata.json"
            output_bytes = b"existing verified media"
            sidecar_bytes = b'{"kind":"existing metadata"}\n'
            output.write_bytes(output_bytes)
            sidecar.write_bytes(sidecar_bytes)
            external = root / ".podwiki-source.m4a.external.tmp"
            external_bytes = b"external file must survive"
            external.write_bytes(external_bytes)
            safe_metadata_temporary = (
                target_directory / ".podwiki-source.metadata.json.safe.tmp"
            )
            journal = acquisition_transaction_path(
                output_path=output,
                metadata_output=sidecar,
            )

            for temporary, message in (
                (output, "equals its target"),
                (external, "outside the target directory"),
            ):
                with self.subTest(message=message):
                    journal.write_text(
                        json.dumps(
                            {
                                "schema_version": 1,
                                "kind": "podwiki-acquisition-transaction",
                                "artifacts": {
                                    "media": {
                                        "target": output.resolve().as_posix(),
                                        "temporary": temporary.resolve().as_posix(),
                                        "sha256": hashlib.sha256(
                                            output_bytes
                                        ).hexdigest(),
                                    },
                                    "metadata": {
                                        "target": sidecar.resolve().as_posix(),
                                        "temporary": (
                                            safe_metadata_temporary.resolve().as_posix()
                                        ),
                                        "sha256": hashlib.sha256(
                                            sidecar_bytes
                                        ).hexdigest(),
                                    },
                                },
                            }
                        ),
                        encoding="utf-8",
                    )
                    with self.assertRaisesRegex(ValueError, message):
                        recover_acquisition_transaction(
                            output_path=output,
                            metadata_output=sidecar,
                        )
                    self.assertEqual(output.read_bytes(), output_bytes)
                    self.assertEqual(sidecar.read_bytes(), sidecar_bytes)
                    self.assertEqual(external.read_bytes(), external_bytes)


class MetadataRefreshTests(unittest.TestCase):
    def write_sidecar(self, path: Path, *, canonical_url: str, digest: str) -> None:
        path.write_text(
            json.dumps(
                {
                    "source": {"canonical_url": canonical_url},
                    "media": {"sha256": digest},
                }
            ),
            encoding="utf-8",
        )

    def test_metadata_only_omits_media_when_local_audio_is_missing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            media = refresh_existing_media(
                output_path=root / "source.m4a",
                metadata_output=root / "source.metadata.json",
                canonical_url="https://example.com/episode",
                info={"duration": 1},
                platform_metadata={},
            )

        self.assertIsNone(media)

    def test_rejects_reuse_when_remote_media_identity_changed(self) -> None:
        current_source = source_metadata(
            xiaoyuzhou_api_info(
                parse_xiaoyuzhou_episode_metadata(
                    xiaoyuzhou_episode_document(), XIAOYUZHOU_EID
                )
            ),
            platform="xiaoyuzhou",
            canonical_url=f"https://www.xiaoyuzhoufm.com/episode/{XIAOYUZHOU_EID}",
            platform_metadata=parse_xiaoyuzhou_episode_metadata(
                xiaoyuzhou_episode_document(), XIAOYUZHOU_EID
            ),
        )
        existing_source = copy.deepcopy(current_source)
        existing_source["media_id"] = f"{XIAOYUZHOU_PID}/replaced-media.m4a"

        with self.assertRaisesRegex(FileExistsError, "media_id identity differs"):
            validate_reusable_source_identity(
                existing_document={"source": existing_source},
                current_source=current_source,
            )

    @patch("acquire_media.probe_audio")
    def test_metadata_only_reprobes_hash_and_current_enclosure(self, probe) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / "source.m4a"
            sidecar = root / "source.metadata.json"
            output.write_bytes(b"verified audio")
            self.write_sidecar(
                sidecar,
                canonical_url="https://example.com/episode",
                digest=sha256_file(output),
            )
            probe.return_value = {
                "path": output.as_posix(),
                "sha256": sha256_file(output),
                "duration_ms": 1000,
                "size_bytes": len(b"verified audio"),
            }

            media = refresh_existing_media(
                output_path=output,
                metadata_output=sidecar,
                canonical_url="https://example.com/episode",
                info={"duration": 1},
                platform_metadata={
                    "duration_seconds": 1,
                    "media": {"size_bytes": len(b"verified audio")},
                },
            )

        self.assertEqual(media, probe.return_value)

    @patch("acquire_media.probe_audio")
    def test_metadata_only_rejects_stale_hash_or_new_enclosure_size(self, probe) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / "source.m4a"
            sidecar = root / "source.metadata.json"
            output.write_bytes(b"current audio")
            self.write_sidecar(
                sidecar,
                canonical_url="https://example.com/episode",
                digest="0" * 64,
            )
            with self.assertRaisesRegex(ValueError, "hash does not match"):
                refresh_existing_media(
                    output_path=output,
                    metadata_output=sidecar,
                    canonical_url="https://example.com/episode",
                    info={"duration": 1},
                    platform_metadata={},
                )

            self.write_sidecar(
                sidecar,
                canonical_url="https://example.com/episode",
                digest=sha256_file(output),
            )
            probe.return_value = {
                "duration_ms": 1000,
                "size_bytes": len(b"current audio"),
            }
            with self.assertRaisesRegex(ValueError, "size differs"):
                refresh_existing_media(
                    output_path=output,
                    metadata_output=sidecar,
                    canonical_url="https://example.com/episode",
                    info={"duration": 1},
                    platform_metadata={
                        "duration_seconds": 1,
                        "media": {"size_bytes": len(b"current audio") + 1},
                    },
                )


class MainWorkflowTests(unittest.TestCase):
    def arguments(
        self,
        root: Path,
        *,
        metadata_only: bool,
        overwrite: bool = False,
        repair_metadata: bool = False,
        expected_sha256: str | None = None,
    ) -> SimpleNamespace:
        return SimpleNamespace(
            url=f"https://www.xiaoyuzhoufm.com/episode/{XIAOYUZHOU_EID}",
            output=root / "source.m4a",
            metadata_output=None,
            metadata_only=metadata_only,
            overwrite=overwrite,
            repair_metadata=repair_metadata,
            expected_sha256=expected_sha256,
            verbose=False,
        )

    @patch("builtins.print")
    @patch("acquire_media.probe_audio")
    @patch("acquire_media.shutil.which", return_value="ffprobe")
    @patch("acquire_media.xiaoyuzhou_platform_metadata")
    @patch("acquire_media.parse_args")
    def test_repairs_missing_sidecar_only_after_hash_source_and_probe_verification(
        self,
        parse_args,
        platform_metadata,
        _which,
        probe,
        _print_output,
    ) -> None:
        metadata = parse_xiaoyuzhou_episode_metadata(
            xiaoyuzhou_episode_document(), XIAOYUZHOU_EID
        )
        platform_metadata.return_value = metadata
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / "source.m4a"
            original_bytes = b"already acquired public audio"
            output.write_bytes(original_bytes)
            digest = sha256_file(output)
            probe.return_value = {
                "path": output.resolve().as_posix(),
                "size_bytes": 1_234_567,
                "duration_ms": 122_500,
                "codec": "aac",
                "sample_rate_hz": 48_000,
                "channels": 1,
                "sha256": digest,
            }
            parse_args.return_value = self.arguments(
                root,
                metadata_only=True,
                repair_metadata=True,
                expected_sha256=digest,
            )

            self.assertEqual(main(), 0)

            sidecar = json.loads(
                (root / "source.metadata.json").read_text(encoding="utf-8")
            )
            self.assertEqual(output.read_bytes(), original_bytes)

        self.assertEqual(sidecar["media"]["sha256"], digest)
        self.assertTrue(sidecar["media_reused"])
        self.assertEqual(sidecar["verified_at"], sidecar["recovered_at"])
        self.assertNotIn("acquired_at", sidecar)
        self.assertEqual(
            sidecar["recovery"],
            {
                "method": "verified-existing-audio-v1",
                "expected_sha256": digest,
                "acquired_at_status": "unknown-legacy",
            },
        )

    @patch("acquire_media.xiaoyuzhou_platform_metadata")
    @patch("acquire_media.parse_args")
    def test_repair_rejects_wrong_hash_before_anonymous_platform_request(
        self, parse_args, platform_metadata
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "source.m4a").write_bytes(b"different bytes")
            parse_args.return_value = self.arguments(
                root,
                metadata_only=True,
                repair_metadata=True,
                expected_sha256="0" * 64,
            )

            with self.assertRaisesRegex(ValueError, "does not match"):
                main()

            self.assertFalse((root / "source.metadata.json").exists())

        platform_metadata.assert_not_called()

    @patch("builtins.print")
    @patch("acquire_media.probe_audio")
    @patch("acquire_media.shutil.which", return_value="ffprobe")
    @patch("acquire_media.xiaoyuzhou_platform_metadata")
    @patch("acquire_media.parse_args")
    def test_repair_can_resume_after_atomic_sidecar_write_failure(
        self,
        parse_args,
        platform_metadata,
        _which,
        probe,
        _print_output,
    ) -> None:
        metadata = parse_xiaoyuzhou_episode_metadata(
            xiaoyuzhou_episode_document(), XIAOYUZHOU_EID
        )
        platform_metadata.return_value = metadata
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / "source.m4a"
            original_bytes = b"recoverable public audio"
            output.write_bytes(original_bytes)
            digest = sha256_file(output)
            probe.return_value = {
                "path": output.resolve().as_posix(),
                "size_bytes": 1_234_567,
                "duration_ms": 122_500,
                "codec": "aac",
                "sample_rate_hz": 48_000,
                "channels": 1,
                "sha256": digest,
            }
            parse_args.return_value = self.arguments(
                root,
                metadata_only=True,
                repair_metadata=True,
                expected_sha256=digest,
            )

            with patch(
                "acquire_media.write_json_atomically",
                side_effect=OSError("injected sidecar promotion failure"),
            ), self.assertRaisesRegex(OSError, "injected"):
                main()

            self.assertEqual(output.read_bytes(), original_bytes)
            self.assertFalse((root / "source.metadata.json").exists())
            self.assertEqual(main(), 0)
            self.assertTrue((root / "source.metadata.json").is_file())

    @patch("builtins.print")
    @patch("acquire_media.xiaoyuzhou_platform_metadata")
    @patch("acquire_media.parse_args")
    def test_xiaoyuzhou_metadata_only_needs_no_yt_dlp_or_local_audio(
        self, parse_args, platform_metadata, print_output
    ) -> None:
        metadata = parse_xiaoyuzhou_episode_metadata(
            xiaoyuzhou_episode_document(), XIAOYUZHOU_EID
        )
        platform_metadata.return_value = metadata
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            parse_args.return_value = self.arguments(root, metadata_only=True)

            self.assertEqual(main(), 0)

            sidecar = json.loads(
                (root / "source.metadata.json").read_text(encoding="utf-8")
            )

        self.assertNotIn("media", sidecar)
        self.assertFalse(sidecar["download_requested"])
        self.assertEqual(sidecar["source"]["media_id"], XIAOYUZHOU_MEDIA_ID)
        self.assertEqual(sidecar["source"]["subtitle_languages"], [])
        self.assertEqual(sidecar["source"]["automatic_caption_languages"], [])
        print_output.assert_called_once()

    @patch("builtins.print")
    @patch("acquire_media.xiaoyuzhou_platform_metadata")
    @patch("acquire_media.parse_args")
    def test_metadata_only_sidecar_surfaces_public_transcript_branch(
        self, parse_args, platform_metadata, _print_output
    ) -> None:
        document = xiaoyuzhou_episode_document()
        episode = document["props"]["pageProps"]["episode"]
        episode["subtitles"] = {
            "zh-CN": [{"url": "https://public.example/subtitles.vtt"}]
        }
        metadata = parse_xiaoyuzhou_episode_metadata(document, XIAOYUZHOU_EID)
        platform_metadata.return_value = metadata

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            parse_args.return_value = self.arguments(root, metadata_only=True)

            self.assertEqual(main(), 0)
            sidecar = json.loads(
                (root / "source.metadata.json").read_text(encoding="utf-8")
            )

        self.assertEqual(sidecar["source"]["subtitle_languages"], ["zh-CN"])
        self.assertEqual(sidecar["source"]["automatic_caption_languages"], [])
        self.assertEqual(
            sidecar["source"]["platform_metadata"]["subtitle"]["tracks"][0][
                "url"
            ],
            "https://public.example/subtitles.vtt",
        )

    @patch("builtins.print")
    @patch("acquire_media.write_json_atomically")
    @patch("acquire_media.xiaoyuzhou_platform_metadata")
    @patch("acquire_media.parse_args")
    def test_main_holds_final_resource_locks_through_sidecar_write(
        self,
        parse_args,
        platform_metadata,
        atomic_write,
        _print_output,
    ) -> None:
        metadata = parse_xiaoyuzhou_episode_metadata(
            xiaoyuzhou_episode_document(), XIAOYUZHOU_EID
        )
        platform_metadata.return_value = metadata
        observed_locked_write = False

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / "source.m4a"
            sidecar = root / "source.metadata.json"
            parse_args.return_value = self.arguments(root, metadata_only=True)

            def assert_transaction_is_locked(path: Path, document: dict) -> None:
                nonlocal observed_locked_write
                for resource in (output, sidecar):
                    with self.subTest(resource=resource):
                        with self.assertRaisesRegex(FileExistsError, "already using"):
                            with exclusive_acquisition_locks([resource]):
                                self.fail(
                                    "main released a final resource lock before sidecar write"
                                )
                observed_locked_write = True
                write_json_atomically(path, document)

            atomic_write.side_effect = assert_transaction_is_locked

            self.assertEqual(main(), 0)
            self.assertTrue(observed_locked_write)
            with exclusive_acquisition_locks([output, sidecar]):
                pass

    @patch("builtins.print")
    @patch("acquire_media.probe_audio")
    @patch("acquire_media.download_xiaoyuzhou_public_audio")
    @patch("acquire_media.shutil.which", return_value="ffprobe")
    @patch("acquire_media.xiaoyuzhou_platform_metadata")
    @patch("acquire_media.parse_args")
    def test_xiaoyuzhou_download_stages_probes_and_atomically_promotes(
        self,
        parse_args,
        platform_metadata,
        _which,
        download,
        probe,
        _print_output,
    ) -> None:
        metadata = parse_xiaoyuzhou_episode_metadata(
            xiaoyuzhou_episode_document(), XIAOYUZHOU_EID
        )
        platform_metadata.return_value = metadata

        def write_staged_audio(*, expected_output: Path, **_kwargs) -> None:
            self.assertEqual(expected_output.parent.name, XIAOYUZHOU_EID)
            expected_output.write_bytes(b"guarded public audio")

        download.side_effect = write_staged_audio
        probe.return_value = {
            "path": "staged/source.m4a",
            "size_bytes": 1_234_567,
            "duration_ms": 122_500,
            "codec": "aac",
            "sample_rate_hz": 48_000,
            "channels": 1,
            "sha256": "a" * 64,
        }

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            parse_args.return_value = self.arguments(root, metadata_only=False)

            self.assertEqual(main(), 0)

            output = root / "source.m4a"
            sidecar = json.loads(
                (root / "source.metadata.json").read_text(encoding="utf-8")
            )
            self.assertEqual(output.read_bytes(), b"guarded public audio")

        self.assertTrue(sidecar["download_requested"])
        self.assertFalse(sidecar["media_reused"])
        self.assertEqual(sidecar["source"]["media_id"], XIAOYUZHOU_MEDIA_ID)
        self.assertEqual(sidecar["media"]["path"], output.resolve().as_posix())
        download.assert_called_once()
        probe.assert_called_once()

    @patch("acquire_media.xiaoyuzhou_platform_metadata")
    @patch("acquire_media.parse_args")
    def test_invalid_existing_media_fails_before_platform_request(
        self, parse_args, platform_metadata
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "source.m4a").write_bytes(b"unidentified audio")
            parse_args.return_value = self.arguments(root, metadata_only=False)

            with self.assertRaisesRegex(FileExistsError, "without identity metadata"):
                main()

        platform_metadata.assert_not_called()


if __name__ == "__main__":
    unittest.main()
