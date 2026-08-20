from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from import_bilibili_subtitles import (  # noqa: E402
    build_outputs,
    load_cached_inputs,
    reject_output_conflicts,
    subtitle_segments,
)


CANONICAL_URL = "https://www.bilibili.com/video/BV1yFbo66E4q/"


def metadata_document() -> dict[str, object]:
    return {
        "source": {
            "platform": "bilibili",
            "canonical_url": CANONICAL_URL,
            "bvid": "BV1yFbo66E4q",
            "aid": 117124093713367,
            "cid": 41078688449,
            "page": 1,
            "uploader": "硅谷101播客",
            "uploader_id": "3546860354538082",
            "duration_seconds": 120.0,
            "platform_metadata": {
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
    }


def subtitle_payload(*, last_end: float = 119.2, reversed_order: bool = False) -> bytes:
    body = [
        {"from": 0.04, "to": 2.6, "sid": 1, "content": "第一段"},
        {"from": 3.0, "to": last_end, "sid": 2, "content": "第二段"},
    ]
    if reversed_order:
        body.reverse()
    return json.dumps(
        {"version": "v1.7.0.4", "type": "AIsubtitle", "lang": "zh", "body": body},
        ensure_ascii=False,
    ).encode("utf-8")


class BilibiliSubtitleImportTests(unittest.TestCase):
    def test_resumes_only_from_source_bound_cache_inputs(self) -> None:
        cache_root = ROOT / ".cache"
        cache_root.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=cache_root) as directory:
            input_dir = Path(directory)
            metadata_path = input_dir / "source.metadata.json"
            subtitle_path = input_dir / "subtitle.zh-CN.json"
            metadata_path.write_text(json.dumps(metadata_document()), encoding="utf-8")
            subtitle_path.write_bytes(subtitle_payload())

            info, subtitle = load_cached_inputs(
                metadata_path=metadata_path,
                subtitle_path=subtitle_path,
                canonical_url=CANONICAL_URL,
            )

            self.assertEqual(info["bvid"], "BV1yFbo66E4q")
            self.assertEqual(subtitle, subtitle_path.read_bytes())

    def test_rejects_cached_inputs_outside_repository_cache(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            input_path = Path(directory) / "input.json"
            input_path.write_text("{}", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "repository .cache"):
                load_cached_inputs(
                    metadata_path=input_path,
                    subtitle_path=input_path,
                    canonical_url=CANONICAL_URL,
                )

    def test_builds_machine_subtitle_lineage_and_transcript(self) -> None:
        info = metadata_document()["source"]
        assert isinstance(info, dict)
        raw, refined, transcript = build_outputs(
            canonical_url=CANONICAL_URL,
            info=info,
            subtitle_payload_bytes=subtitle_payload(),
            title="An episode",
            generated_at="2026-08-20T00:00:00Z",
            language="zh-CN",
            access_context="authenticated",
            raw_repository_path=(
                "shows/example/episodes/example/asr/bilibili-subtitles/raw.json"
            ),
            transcript_repository_path=(
                "shows/example/episodes/example/asr/bilibili-subtitles/transcript.zh-CN.md"
            ),
        )

        raw_document = json.loads(raw)
        refined_document = json.loads(refined)
        self.assertEqual(raw_document["source"]["track_type"], "bilibili-ai-subtitle")
        self.assertEqual(raw_document["source"]["access_context"], "authenticated")
        self.assertEqual(len(refined_document["segments"]), 2)
        self.assertIn("[00:00:00] 第一段  \n", transcript.decode("utf-8"))

    def test_rejects_incomplete_edge_coverage(self) -> None:
        info = metadata_document()["source"]
        assert isinstance(info, dict)
        with self.assertRaisesRegex(ValueError, "ends more than 30 seconds"):
            build_outputs(
                canonical_url=CANONICAL_URL,
                info=info,
                subtitle_payload_bytes=subtitle_payload(last_end=80.0),
                title="An episode",
                generated_at="2026-08-20T00:00:00Z",
                language="zh-CN",
                access_context="authenticated",
                raw_repository_path="raw.json",
                transcript_repository_path="transcript.zh-CN.md",
            )

    def test_rejects_non_monotonic_segments(self) -> None:
        with self.assertRaisesRegex(ValueError, "not monotonic"):
            subtitle_segments(json.loads(subtitle_payload(reversed_order=True)))

    def test_preflights_all_output_conflicts_before_writing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "raw.json"
            output.write_bytes(b"old")
            with self.assertRaisesRegex(FileExistsError, "without --overwrite"):
                reject_output_conflicts({output: b"new"}, overwrite=False)
            self.assertEqual(output.read_bytes(), b"old")


if __name__ == "__main__":
    unittest.main()
