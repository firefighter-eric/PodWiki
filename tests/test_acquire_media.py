from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from acquire_media import (  # noqa: E402
    available_javascript_runtime,
    canonical_source_url,
    retain_existing_media,
    source_metadata,
)


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
