from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from import_youtube_captions import (  # noqa: E402
    build_outputs,
    caption_segments,
    load_cached_inputs,
)


def caption_payload(first: str, second: str, *, shifted: bool = False) -> bytes:
    return json.dumps(
        {
            "wireMagic": "pb3",
            "events": [
                {
                    "tStartMs": 80,
                    "dDurationMs": 3600,
                    "segs": [{"utf8": first}],
                },
                {
                    "tStartMs": 3681 if shifted else 3680,
                    "dDurationMs": 3840,
                    "segs": [{"utf8": second}],
                },
            ],
        },
        ensure_ascii=False,
    ).encode("utf-8")


class YoutubeCaptionImportTests(unittest.TestCase):
    def test_resumes_only_from_source_bound_cache_inputs(self) -> None:
        cache_root = ROOT / ".cache"
        cache_root.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=cache_root) as directory:
            input_dir = Path(directory)
            metadata_path = input_dir / "source.metadata.json"
            source_path = input_dir / "subtitle.en.json3"
            translation_path = input_dir / "subtitle.zh-Hans-en.json3"
            metadata_path.write_text(
                json.dumps(
                    {
                        "source": {
                            "platform": "youtube",
                            "canonical_url": (
                                "https://www.youtube.com/watch?v=-RXD4bTuFTo"
                            ),
                            "id": "-RXD4bTuFTo",
                            "channel_id": "UCXl4i9dYBrFOabk0xGmbkRA",
                            "availability": "public",
                            "live_status": "not_live",
                        }
                    }
                ),
                encoding="utf-8",
            )
            source_path.write_bytes(caption_payload("One", "Two"))
            translation_path.write_bytes(caption_payload("一", "二"))

            info, source, translation = load_cached_inputs(
                metadata_path=metadata_path,
                source_path=source_path,
                translation_path=translation_path,
                canonical_url="https://www.youtube.com/watch?v=-RXD4bTuFTo",
            )

            self.assertEqual(info["id"], "-RXD4bTuFTo")
            self.assertEqual(source, source_path.read_bytes())
            self.assertEqual(translation, translation_path.read_bytes())

    def test_rejects_cached_inputs_outside_repository_cache(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            input_path = Path(directory) / "input.json"
            input_path.write_text("{}", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "repository .cache"):
                load_cached_inputs(
                    metadata_path=input_path,
                    source_path=input_path,
                    translation_path=input_path,
                    canonical_url="https://www.youtube.com/watch?v=-RXD4bTuFTo",
                )

    def test_builds_aligned_english_and_chinese_transcripts(self) -> None:
        raw, refined, english, chinese = build_outputs(
            canonical_url="https://www.youtube.com/watch?v=-RXD4bTuFTo",
            info={
                "id": "-RXD4bTuFTo",
                "channel_id": "UCXl4i9dYBrFOabk0xGmbkRA",
                "uploader": "Dwarkesh Patel",
            },
            source_payload_bytes=caption_payload("Hello\nworld", "Second  segment"),
            translation_payload_bytes=caption_payload("你好\n世界", "第二段"),
            title="An episode",
            generated_at="2026-08-18T00:00:00Z",
            source_language="en",
            translation_track="zh-Hans-en",
            raw_repository_path="shows/example/episodes/example/asr/youtube-subtitles/raw.json",
            transcript_repository_path=(
                "shows/example/episodes/example/asr/youtube-subtitles/transcript.en.md"
            ),
            translation_repository_path=(
                "shows/example/episodes/example/transcript.zh-CN.md"
            ),
        )

        raw_document = json.loads(raw)
        refined_document = json.loads(refined)
        self.assertEqual(raw_document["source"]["video_id"], "-RXD4bTuFTo")
        self.assertEqual(len(refined_document["segments"]), 2)
        self.assertIn("[00:00:00] Hello world  \n", english.decode("utf-8"))
        self.assertIn("[00:00:00] 你好 世界  \n", chinese.decode("utf-8"))
        self.assertEqual(
            refined_document["translation"]["event_count"],
            len(caption_segments(json.loads(caption_payload("一", "二")), label="test")),
        )

    def test_rejects_translation_timestamp_drift(self) -> None:
        with self.assertRaisesRegex(ValueError, "does not preserve source start_ms"):
            build_outputs(
                canonical_url="https://www.youtube.com/watch?v=-RXD4bTuFTo",
                info={
                    "id": "-RXD4bTuFTo",
                    "channel_id": "UCXl4i9dYBrFOabk0xGmbkRA",
                    "uploader": "Dwarkesh Patel",
                },
                source_payload_bytes=caption_payload("One", "Two"),
                translation_payload_bytes=caption_payload("一", "二", shifted=True),
                title="An episode",
                generated_at="2026-08-18T00:00:00Z",
                source_language="en",
                translation_track="zh-Hans-en",
                raw_repository_path="raw.json",
                transcript_repository_path="transcript.en.md",
                translation_repository_path="transcript.zh-CN.md",
            )


if __name__ == "__main__":
    unittest.main()
