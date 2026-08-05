from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from render_asr_transcript import refine_segments  # noqa: E402


class RefineSegmentTimestampTests(unittest.TestCase):
    def test_preserves_valid_bounds_without_mutating_raw_segments(self) -> None:
        raw_segments = [
            {"id": 4, "start": 12.25, "end": 13.75, "text": "正常段落。"}
        ]
        raw_before = copy.deepcopy(raw_segments)

        refined = refine_segments(raw_segments)

        self.assertEqual(raw_segments, raw_before)
        self.assertEqual(refined[0]["start"], 12.25)
        self.assertEqual(refined[0]["end"], 13.75)

    def test_clamps_small_reversed_end_without_mutating_raw_segments(self) -> None:
        raw_segments = [
            {"id": 131, "start": 290.16, "end": 290.12, "text": "模型时间抖动。"}
        ]
        raw_before = copy.deepcopy(raw_segments)

        refined = refine_segments(raw_segments)

        self.assertEqual(raw_segments, raw_before)
        self.assertEqual(refined[0]["start"], 290.16)
        self.assertEqual(refined[0]["end"], 290.16)

    def test_clamps_reversal_at_tolerance_boundary(self) -> None:
        refined = refine_segments(
            [{"id": 1, "start": 5.25, "end": 5.0, "text": "边界。"}]
        )

        self.assertEqual(refined[0]["end"], 5.25)

    def test_rejects_reversal_above_tolerance(self) -> None:
        with self.assertRaisesRegex(ValueError, "exceeding the 0.250s tolerance"):
            refine_segments(
                [{"id": 1, "start": 5.251, "end": 5.0, "text": "损坏。"}]
            )

    def test_rejects_large_reversal_before_duplicate_folding(self) -> None:
        with self.assertRaisesRegex(ValueError, "segment 1 end precedes start"):
            refine_segments(
                [
                    {"id": 10, "start": 4.0, "end": 5.0, "text": "重复内容"},
                    {"id": 11, "start": 5.0, "end": 4.0, "text": "重复内容"},
                ]
            )

    def test_clamps_small_start_regression_across_segments(self) -> None:
        raw_segments = [
            {"id": 130, "start": 289.42, "end": 290.16, "text": "前一段"},
            {"id": 131, "start": 290.16, "end": 290.12, "text": "抖动段"},
            {"id": 132, "start": 290.12, "end": 291.44, "text": "后一段"},
        ]
        raw_before = copy.deepcopy(raw_segments)

        refined = refine_segments(raw_segments)

        self.assertEqual(raw_segments, raw_before)
        self.assertEqual(
            [(segment["start"], segment["end"]) for segment in refined],
            [(289.42, 290.16), (290.16, 290.16), (290.16, 291.44)],
        )

    def test_rejects_large_start_regression_across_segments(self) -> None:
        with self.assertRaisesRegex(
            ValueError, "start precedes the previous segment start"
        ):
            refine_segments(
                [
                    {"id": 1, "start": 5.0, "end": 5.5, "text": "前一段"},
                    {"id": 2, "start": 4.7, "end": 5.1, "text": "后一段"},
                ]
            )

    def test_rejects_negative_start(self) -> None:
        with self.assertRaisesRegex(ValueError, "negative timestamp bounds"):
            refine_segments(
                [{"id": 1, "start": -0.001, "end": 1.0, "text": "损坏。"}]
            )

    def test_rejects_negative_end(self) -> None:
        with self.assertRaisesRegex(ValueError, "negative timestamp bounds"):
            refine_segments(
                [{"id": 1, "start": 0.0, "end": -0.001, "text": "损坏。"}]
            )

    def test_consecutive_duplicate_folding_is_unchanged(self) -> None:
        refined = refine_segments(
            [
                {"id": 7, "start": 1.0, "end": 2.0, "text": "重复内容"},
                {"id": 8, "start": 2.1, "end": 2.3, "text": "重复内容！"},
            ]
        )

        self.assertEqual(
            refined,
            [
                {
                    "start": 1.0,
                    "end": 2.0,
                    "text": "重复内容",
                    "source_segment_indexes": [0, 1],
                    "source_segment_ids": [7, 8],
                }
            ],
        )


class RefineSegmentContentTests(unittest.TestCase):
    def test_preserves_chinese_latin_and_numeric_content(self) -> None:
        refined = refine_segments(
            [
                {"id": 1, "start": 0.0, "end": 1.0, "text": "中文！"},
                {"id": 2, "start": 1.0, "end": 2.0, "text": "OpenAI..."},
                {"id": 3, "start": 2.0, "end": 3.0, "text": "2026 🚀"},
            ]
        )

        self.assertEqual(
            [segment["text"] for segment in refined],
            ["中文！", "OpenAI...", "2026 🚀"],
        )

    def test_drops_punctuation_symbol_and_emoji_before_timestamp_validation(self) -> None:
        for text in ("!", "...", "🚀"):
            with self.subTest(text=text):
                self.assertEqual(
                    refine_segments(
                        [{"id": 1, "start": 5.0, "end": 4.0, "text": text}]
                    ),
                    [],
                )


if __name__ == "__main__":
    unittest.main()
