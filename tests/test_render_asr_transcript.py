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
    load_correction_map,
    main,
    read_json_strict,
    recover_artifact_pair_transaction,
    refine_segments,
    render_transaction_path,
    repository_path,
    sha256_text,
    write_artifact_pair_atomically,
    validate_correction_hits,
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

    def test_applies_only_episode_scoped_audited_corrections_and_counts_hits(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            correction_path = Path(directory) / "corrections.json"
            correction_path.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "episode_id": "show:001",
                        "version": 3,
                        "input_asr_sha256": "0" * 64,
                        "rules": [
                            {
                                "id": "guest-name",
                                "match": "翁嘉义",
                                "replacement": "翁家翌",
                                "reason": "publisher metadata and human review",
                                "expected_hits": 2,
                            }
                        ],
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            correction_map = load_correction_map(
                correction_path,
                episode_id="show:001",
            )
            hits = {"guest-name": 0}

            refined = refine_segments(
                [
                    {
                        "id": 1,
                        "start": 0.0,
                        "end": 1.0,
                        "text": "翁嘉义采访翁嘉义。",
                    }
                ],
                correction_rules=correction_map.rules,
                correction_hits=hits,
            )

        self.assertEqual(refined[0]["text"], "翁家翌采访翁家翌。")
        self.assertEqual(hits, {"guest-name": 2})
        validate_correction_hits(correction_map, hits=hits)
        self.assertEqual(
            refine_segments(
                [{"id": 1, "start": 0.0, "end": 1.0, "text": "翁嘉义。"}]
            )[0]["text"],
            "翁嘉义。",
        )

    def test_correction_map_is_bound_to_one_episode(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "corrections.json"
            path.write_text(
                '{"schema_version":1,"episode_id":"show:001",'
                '"version":1,"input_asr_sha256":"' + "0" * 64 + '","rules":[]}',
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "episode_id"):
                load_correction_map(path, episode_id="show:002")

    def test_correction_map_rejects_unexpected_hit_count(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "corrections.json"
            path.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "episode_id": "show:001",
                        "version": 1,
                        "input_asr_sha256": "0" * 64,
                        "rules": [
                            {
                                "id": "verified-name",
                                "match": "误写",
                                "replacement": "正名",
                                "reason": "publisher metadata",
                                "expected_hits": 2,
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            correction_map = load_correction_map(path, episode_id="show:001")

        with self.assertRaisesRegex(ValueError, "expected=2, actual=1"):
            validate_correction_hits(correction_map, hits={"verified-name": 1})


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

    def test_recovers_pair_after_failure_between_the_two_promotions(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            refined_path = root / "refined.json"
            transcript_path = root / "transcript.md"
            original_promote = __import__(
                "render_asr_transcript"
            ).promote_transaction_artifact
            promotion_count = 0

            def fail_second_promotion(temporary: Path, target: Path) -> None:
                nonlocal promotion_count
                promotion_count += 1
                if promotion_count == 2:
                    raise OSError("injected refined promotion failure")
                original_promote(temporary, target)

            with patch(
                "render_asr_transcript.promote_transaction_artifact",
                side_effect=fail_second_promotion,
            ), self.assertRaisesRegex(OSError, "injected"):
                write_artifact_pair_atomically(
                    refined_path=refined_path,
                    refined_text='{"kind":"refined-asr"}\n',
                    transcript_path=transcript_path,
                    transcript_text="# title\n",
                )

            journal = render_transaction_path(
                refined_path=refined_path,
                transcript_path=transcript_path,
            )
            self.assertTrue(journal.is_file())
            self.assertTrue(
                recover_artifact_pair_transaction(
                    refined_path=refined_path,
                    transcript_path=transcript_path,
                )
            )
            self.assertEqual(
                refined_path.read_text(encoding="utf-8"),
                '{"kind":"refined-asr"}\n',
            )
            self.assertEqual(transcript_path.read_text(encoding="utf-8"), "# title\n")
            self.assertFalse(journal.exists())
            self.assertEqual(list(root.rglob(".podwiki-*.tmp")), [])

    def test_recovery_rejects_target_or_external_temporary_without_mutation(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target_directory = root / "targets"
            target_directory.mkdir()
            refined_path = target_directory / "refined.json"
            transcript_path = target_directory / "transcript.md"
            refined_bytes = b'{"kind":"existing refined"}\n'
            transcript_bytes = b"# existing transcript\n"
            refined_path.write_bytes(refined_bytes)
            transcript_path.write_bytes(transcript_bytes)
            external = root / ".podwiki-transcript.md.external.tmp"
            external_bytes = b"external file must survive"
            external.write_bytes(external_bytes)
            safe_refined_temporary = (
                target_directory / ".podwiki-refined.json.safe.tmp"
            )
            journal = render_transaction_path(
                refined_path=refined_path,
                transcript_path=transcript_path,
            )

            for temporary, message in (
                (transcript_path, "equals its target"),
                (external, "outside the target directory"),
            ):
                with self.subTest(message=message):
                    journal.write_text(
                        json.dumps(
                            {
                                "schema_version": 1,
                                "kind": "podwiki-render-transaction",
                                "artifacts": {
                                    "refined": {
                                        "target": refined_path.resolve().as_posix(),
                                        "temporary": (
                                            safe_refined_temporary.resolve().as_posix()
                                        ),
                                        "sha256": hashlib.sha256(
                                            refined_bytes
                                        ).hexdigest(),
                                    },
                                    "transcript": {
                                        "target": transcript_path.resolve().as_posix(),
                                        "temporary": temporary.resolve().as_posix(),
                                        "sha256": hashlib.sha256(
                                            transcript_bytes
                                        ).hexdigest(),
                                    },
                                },
                            }
                        ),
                        encoding="utf-8",
                    )
                    with self.assertRaisesRegex(ValueError, message):
                        recover_artifact_pair_transaction(
                            refined_path=refined_path,
                            transcript_path=transcript_path,
                        )
                    self.assertEqual(refined_path.read_bytes(), refined_bytes)
                    self.assertEqual(transcript_path.read_bytes(), transcript_bytes)
                    self.assertEqual(external.read_bytes(), external_bytes)

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

    def test_refined_v2_copies_model_and_aligner_identity_and_repository(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            input_path = root / "aligned.json"
            refined_path = root / "refined.json"
            transcript_path = root / "transcript.md"
            model_identity = {
                "schema_version": 1,
                "repository": "example/model",
                "requested_revision": "a" * 40,
                "resolved_commit": "a" * 40,
                "files_sha256": {
                    "config.json": "1" * 64,
                    "model.safetensors": "2" * 64,
                },
            }
            aligner_identity = {
                **model_identity,
                "repository": "example/aligner",
                "requested_revision": "b" * 40,
                "resolved_commit": "b" * 40,
            }
            input_path.write_text(
                json.dumps(
                    {
                        "lineage_schema_version": 2,
                        "source": {
                            "model": "example/model",
                            "aligner": "example/aligner",
                            "model_identity": model_identity,
                            "aligner_identity": aligner_identity,
                        },
                        "segments": [
                            {"id": 0, "start": 0.0, "end": 1.0, "text": "内容"}
                        ],
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
                "example/model",
            ]

            with patch.object(sys, "argv", arguments), contextlib.redirect_stdout(
                io.StringIO()
            ):
                self.assertEqual(main(), 0)

            refined = json.loads(refined_path.read_text(encoding="utf-8"))
            self.assertEqual(refined["lineage_schema_version"], 2)
            self.assertEqual(refined["source"]["model_identity"], model_identity)
            self.assertEqual(refined["source"]["aligner_identity"], aligner_identity)
            self.assertEqual(refined["source"]["aligner"], "example/aligner")

    def test_main_reuses_a_valid_pair_without_rewriting_it(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            input_path = root / "aligned.json"
            refined_path = root / "refined.json"
            transcript_path = root / "transcript.md"
            input_path.write_text(
                '{"segments":[{"id":0,"start":0,"end":1,"text":"内容"}]}',
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
            first_refined = refined_path.read_bytes()
            first_transcript = transcript_path.read_bytes()
            stdout = io.StringIO()
            with patch.object(sys, "argv", arguments), contextlib.redirect_stdout(stdout):
                self.assertEqual(main(), 0)

            self.assertEqual(refined_path.read_bytes(), first_refined)
            self.assertEqual(transcript_path.read_bytes(), first_transcript)
            self.assertEqual(json.loads(stdout.getvalue())["status"], "skipped-valid")

    def test_main_reuses_legacy_pair_when_episode_map_exactly_reproduces_it(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            input_path = root / "aligned.json"
            correction_path = root / "corrections.json"
            refined_path = root / "refined.json"
            transcript_path = root / "transcript.md"
            input_path.write_text(
                '{"segments":[{"id":0,"start":0,"end":1,"text":"Deep Seek"}]}',
                encoding="utf-8",
            )
            correction_path.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "episode_id": "show:001",
                        "version": "legacy-global-v1-migration",
                        "input_asr_sha256": hashlib.sha256(
                            input_path.read_bytes()
                        ).hexdigest(),
                        "rules": [
                            {
                                "id": "deepseek-spaced",
                                "match": "Deep Seek",
                                "replacement": "DeepSeek",
                                "reason": "canonical DeepSeek brand spelling",
                                "case_sensitive": True,
                                "expected_hits": 1,
                            }
                        ],
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
                "--correction-map",
                str(correction_path),
            ]
            with patch.object(sys, "argv", arguments), contextlib.redirect_stdout(
                io.StringIO()
            ):
                self.assertEqual(main(), 0)
            legacy_refined = json.loads(refined_path.read_text(encoding="utf-8"))
            del legacy_refined["corrections"]
            refined_path.write_text(
                json.dumps(legacy_refined, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            first_refined = refined_path.read_bytes()
            first_transcript = transcript_path.read_bytes()
            stdout = io.StringIO()

            with patch.object(sys, "argv", arguments), contextlib.redirect_stdout(stdout):
                self.assertEqual(main(), 0)

            self.assertEqual(refined_path.read_bytes(), first_refined)
            self.assertEqual(transcript_path.read_bytes(), first_transcript)
            self.assertEqual(json.loads(stdout.getvalue())["status"], "skipped-valid")

    def test_strict_reader_rejects_duplicate_keys_and_non_finite_values(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.json"
            path.write_text('{"segments":[],"segments":[]}', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
                read_json_strict(path)
            path.write_text('{"value":NaN}', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "non-finite"):
                read_json_strict(path)

    def test_main_rejects_unknown_or_non_integer_lineage_marker(self) -> None:
        for marker in (1, 3, "2", True):
            with self.subTest(marker=marker), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                input_path = root / "aligned.json"
                refined_path = root / "refined.json"
                transcript_path = root / "transcript.md"
                input_path.write_text(
                    json.dumps(
                        {
                            "lineage_schema_version": marker,
                            "segments": [
                                {
                                    "id": 0,
                                    "start": 0.0,
                                    "end": 1.0,
                                    "text": "内容",
                                }
                            ],
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

                with patch.object(sys, "argv", arguments), self.assertRaisesRegex(
                    ValueError, "lineage_schema_version"
                ):
                    main()

                self.assertFalse(refined_path.exists())
                self.assertFalse(transcript_path.exists())


if __name__ == "__main__":
    unittest.main()
