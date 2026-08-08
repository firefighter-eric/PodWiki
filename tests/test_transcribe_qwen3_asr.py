from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from transcribe_qwen3_asr import (  # noqa: E402
    alignment_units,
    finite_document_number,
    read_json_strict,
    resume_mode,
    sentence_segments,
    sentence_texts,
    validate_aligned_document,
    validate_raw_document,
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

    def test_tokenizes_english_like_forced_aligner(self) -> None:
        self.assertEqual(
            alignment_units("A sci-fi world's version 3.14.", language="English"),
            ["A", "scifi", "world's", "version", "314"],
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

    def test_splits_english_sentences_without_splitting_decimal_points(self) -> None:
        self.assertEqual(
            sentence_texts(
                "First sentence. Version 3.14 works! Final question?",
                max_characters=160,
            ),
            ["First sentence.", "Version 3.14 works!", "Final question?"],
        )

    def test_keeps_periods_inside_one_english_token_together(self) -> None:
        self.assertEqual(
            sentence_texts("D.N.A. works.", max_characters=160),
            ["D.N.A.", "works."],
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

    def test_merges_false_english_boundary_inside_one_aligner_token(self) -> None:
        text = "CEO。If the cycle changes."
        items = [
            {"text": "CEOIf", "start_time": 0.1, "end_time": 0.3},
            {"text": "the", "start_time": 0.31, "end_time": 0.4},
            {"text": "cycle", "start_time": 0.41, "end_time": 0.5},
            {"text": "changes", "start_time": 0.51, "end_time": 0.6},
        ]

        self.assertEqual(
            sentence_segments(
                text=text,
                aligned_items=items,
                offset_seconds=12.0,
                chunk_id=3,
                first_segment_id=7,
                max_characters=160,
                language="English",
            ),
            [
                {
                    "id": 7,
                    "start": 12.1,
                    "end": 12.6,
                    "text": text,
                    "source_chunk_id": 3,
                }
            ],
        )


class ResumeModeTests(unittest.TestCase):
    def test_resumes_at_the_next_incomplete_stage(self) -> None:
        self.assertEqual(
            resume_mode(
                raw_exists=False,
                aligned_exists=False,
                retranscribe=False,
                realign=False,
            ),
            "fresh",
        )
        self.assertEqual(
            resume_mode(
                raw_exists=True,
                aligned_exists=False,
                retranscribe=False,
                realign=False,
            ),
            "align-only",
        )
        self.assertEqual(
            resume_mode(
                raw_exists=True,
                aligned_exists=True,
                retranscribe=False,
                realign=False,
            ),
            "complete",
        )

    def test_rejects_aligned_without_raw(self) -> None:
        with self.assertRaisesRegex(FileNotFoundError, "without its raw"):
            resume_mode(
                raw_exists=False,
                aligned_exists=True,
                retranscribe=False,
                realign=False,
            )

    def test_explicit_replacement_modes(self) -> None:
        self.assertEqual(
            resume_mode(
                raw_exists=True,
                aligned_exists=True,
                retranscribe=True,
                realign=False,
            ),
            "fresh",
        )
        self.assertEqual(
            resume_mode(
                raw_exists=True,
                aligned_exists=True,
                retranscribe=False,
                realign=True,
            ),
            "align-only",
        )


class ArtifactValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.raw = {
            "schema_version": 1,
            "kind": "raw-asr",
            "engine": "mlx-audio",
            "model": "model-id",
            "language": "Chinese",
            "audio": {
                "duration_seconds": 2.0,
                "sample_rate_hz": 16000,
                "size_bytes": 123,
                "sha256": "audio-sha",
            },
            "options": {
                "temperature": 0.0,
                "max_tokens_per_chunk": 4096,
                "chunk_duration_seconds": 240.0,
            },
            "text": "测试。",
            "segments": [
                {"id": 0, "start": 0.0, "end": 2.0, "text": "测试。"}
            ],
        }

    def validate_raw(self) -> dict[str, object]:
        return validate_raw_document(
            self.raw,
            model="model-id",
            language="Chinese",
            temperature=0.0,
            max_tokens=4096,
            chunk_duration=240.0,
            audio_size_bytes=123,
            audio_sha256="audio-sha",
        )

    def test_accepts_matching_raw_identity(self) -> None:
        self.assertIs(self.validate_raw(), self.raw)

    def test_rejects_raw_from_another_audio_file(self) -> None:
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            validate_raw_document(
                self.raw,
                model="model-id",
                language="Chinese",
                temperature=0.0,
                max_tokens=4096,
                chunk_duration=240.0,
                audio_size_bytes=123,
                audio_sha256="other-sha",
            )

    def test_rejects_boolean_timestamp(self) -> None:
        with self.assertRaisesRegex(ValueError, "invalid timestamp"):
            finite_document_number(True, field="timestamp")

    def test_strict_reader_rejects_duplicate_keys(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "raw.json"
            path.write_text('{"kind":"raw-asr","kind":"other"}', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
                read_json_strict(path)

    def test_accepts_aligned_artifact_tied_to_raw_hash(self) -> None:
        self.validate_raw()
        aligned = {
            "schema_version": 1,
            "kind": "aligned-asr",
            "language": "Chinese",
            "source": {
                "engine": "mlx-audio",
                "model": "model-id",
                "aligner": "aligner-id",
                "audio_sha256": "audio-sha",
                "raw_asr_sha256": "raw-sha",
            },
            "options": {"max_sentence_characters": 160},
            "statistics": {
                "source_chunks": 1,
                "aligned_chunks": 1,
                "alignment_items": 2,
                "sentence_segments": 1,
            },
            "text": "测试。",
            "chunks": [
                {
                    "id": 0,
                    "start": 0.0,
                    "end": 2.0,
                    "text": "测试。",
                    "alignment": [
                        {"text": "测", "start": 0.1, "end": 0.5},
                        {"text": "试", "start": 0.5, "end": 1.0},
                    ],
                }
            ],
            "segments": [
                {
                    "id": 0,
                    "start": 0.1,
                    "end": 1.0,
                    "text": "测试。",
                    "source_chunk_id": 0,
                }
            ],
        }

        self.assertIs(
            validate_aligned_document(
                aligned,
                model="model-id",
                aligner="aligner-id",
                language="Chinese",
                audio_sha256="audio-sha",
                raw_asr_sha256="raw-sha",
                raw_document=self.raw,
                max_sentence_characters=160,
            ),
            aligned,
        )


if __name__ == "__main__":
    unittest.main()
