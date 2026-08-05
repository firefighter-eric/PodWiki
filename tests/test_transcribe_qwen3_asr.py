from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from transcribe_qwen3_asr import (  # noqa: E402
    alignment_units,
    sentence_segments,
    sentence_texts,
)
from render_asr_transcript import clean_text  # noqa: E402


class RefinementTests(unittest.TestCase):
    def test_normalizes_qwen_proper_noun_variants(self) -> None:
        self.assertEqual(
            clean_text("翁嘉译在 WhyNot TV 介绍天授。"),
            "翁家翌在 WhynotTV 介绍Tianshou。",
        )


class AlignmentUnitsTests(unittest.TestCase):
    def test_tokenizes_chinese_and_latin_like_forced_aligner(self) -> None:
        self.assertEqual(
            alignment_units("翁家翌在 OpenAI 做 RL-infra。"),
            ["翁", "家", "翌", "在", "OpenAI", "做", "RL", "infra"],
        )


class SentenceTextTests(unittest.TestCase):
    def test_preserves_sentence_punctuation(self) -> None:
        self.assertEqual(
            sentence_texts("第一句。第二句？第三句！", max_characters=160),
            ["第一句。", "第二句？", "第三句！"],
        )

    def test_splits_long_clause_only_at_soft_punctuation(self) -> None:
        self.assertEqual(
            sentence_texts("一二三四五六，七八九。", max_characters=6),
            ["一二三四五六，", "七八九。"],
        )


class SentenceSegmentsTests(unittest.TestCase):
    def test_maps_sentences_to_aligned_timestamps(self) -> None:
        text = "你好，OpenAI。再见！"
        items = [
            {"text": "你", "start_time": 0.1, "end_time": 0.2},
            {"text": "好", "start_time": 0.2, "end_time": 0.3},
            {"text": "OpenAI", "start_time": 0.4, "end_time": 0.8},
            {"text": "再", "start_time": 1.0, "end_time": 1.1},
            {"text": "见", "start_time": 1.1, "end_time": 1.2},
        ]

        self.assertEqual(
            sentence_segments(
                text=text,
                aligned_items=items,
                offset_seconds=60.0,
                chunk_id=2,
                first_segment_id=9,
                max_characters=160,
            ),
            [
                {
                    "id": 9,
                    "start": 60.1,
                    "end": 60.8,
                    "text": "你好，OpenAI。",
                    "source_chunk_id": 2,
                },
                {
                    "id": 10,
                    "start": 61.0,
                    "end": 61.2,
                    "text": "再见！",
                    "source_chunk_id": 2,
                },
            ],
        )


if __name__ == "__main__":
    unittest.main()
