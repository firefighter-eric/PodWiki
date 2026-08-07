from __future__ import annotations

import copy
import contextlib
import hashlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from render_asr_transcript import (  # noqa: E402
    main,
    refine_segments,
    repository_path,
    sha256_text,
    write_artifact_pair_atomically,
)


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


class AtomicArtifactTests(unittest.TestCase):
    def test_writes_matching_refined_and_transcript_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            refined_path = root / "asr" / "refined.json"
            transcript_path = root / "transcript.zh-CN.md"
            transcript = "# 标题\n\n[00:00:00] 内容  \n"

            write_artifact_pair_atomically(
                refined_path=refined_path,
                refined_text='{"kind":"refined-asr"}\n',
                transcript_path=transcript_path,
                transcript_text=transcript,
            )

            self.assertEqual(
                refined_path.read_text(encoding="utf-8"),
                '{"kind":"refined-asr"}\n',
            )
            self.assertEqual(
                transcript_path.read_text(encoding="utf-8"), transcript
            )
            self.assertNotIn(b"\r\n", refined_path.read_bytes())
            self.assertNotIn(b"\r\n", transcript_path.read_bytes())
            self.assertEqual(
                sha256_text(transcript),
                hashlib.sha256(transcript.encode("utf-8")).hexdigest(),
            )
            self.assertEqual(list(root.rglob(".podwiki-*.tmp")), [])

    def test_rejects_the_same_output_path(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "artifact"
            with self.assertRaisesRegex(ValueError, "must be distinct"):
                write_artifact_pair_atomically(
                    refined_path=path,
                    refined_text="{}",
                    transcript_path=path,
                    transcript_text="# 标题",
                )

    def test_repository_path_is_portable_for_tracked_artifacts(self) -> None:
        self.assertEqual(
            repository_path(ROOT / "shows" / "example" / "aligned.json"),
            "shows/example/aligned.json",
        )

    def test_refined_lineage_names_generic_input_asr(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            input_path = root / "aligned.json"
            refined_path = root / "refined.json"
            transcript_path = root / "transcript.md"
            input_path.write_text(
                json.dumps(
                    {
                        "segments": [
                            {"id": 0, "start": 0.0, "end": 1.0, "text": "内容"}
                        ]
                    }
                ),
                encoding="utf-8",
            )
            arguments = [
                "render_asr_transcript.py",
                "--input",
                str(input_path),
                "--refined-output",
                str(refined_path),
                "--output",
                str(transcript_path),
                "--episode-id",
                "show:001",
                "--title",
                "标题",
                "--model",
                "model",
            ]

            with patch.object(sys, "argv", arguments), contextlib.redirect_stdout(
                io.StringIO()
            ):
                self.assertEqual(main(), 0)

            source = json.loads(refined_path.read_text(encoding="utf-8"))["source"]
            self.assertIn("input_asr_path", source)
            self.assertIn("input_asr_sha256", source)
            self.assertNotIn("raw_asr_path", source)


if __name__ == "__main__":
    unittest.main()
