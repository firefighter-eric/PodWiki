from __future__ import annotations

import argparse
import copy
import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import transcribe_qwen3_asr_cuda as cuda_worker  # noqa: E402
from transcribe_qwen3_asr import (  # noqa: E402
    read_json_strict,
    sha256_file,
    write_json_atomically,
)


class FakeAudio:
    def __init__(self, samples: int = 32_000) -> None:
        self.samples = samples

    def __len__(self) -> int:
        return self.samples


class FakeCuda:
    def __init__(self) -> None:
        self.current_device = 0

    def is_available(self) -> bool:
        return True

    def device_count(self) -> int:
        return 1

    def is_bf16_supported(self) -> bool:
        return True

    def set_device(self, index: int) -> None:
        self.current_device = index

    def get_device_properties(self, index: int) -> SimpleNamespace:
        if index != 0:
            raise AssertionError(f"unexpected device index: {index}")
        return SimpleNamespace(name="Fake RTX", total_memory=8 * 1024**3)

    def reset_peak_memory_stats(self, index: int) -> None:
        if index != 0:
            raise AssertionError(f"unexpected device index: {index}")

    def synchronize(self, index: int) -> None:
        if index != 0:
            raise AssertionError(f"unexpected device index: {index}")

    def max_memory_allocated(self, index: int) -> int:
        if index != 0:
            raise AssertionError(f"unexpected device index: {index}")
        return 512 * 1024**2

    def empty_cache(self) -> None:
        return None


class FakeTorch:
    def __init__(self) -> None:
        self.cuda = FakeCuda()
        self.version = SimpleNamespace(cuda="12.8")
        self.float16 = object()
        self.bfloat16 = object()


class WorkerHarness:
    def __init__(self) -> None:
        self.events: list[tuple[str, object]] = []
        self.torch = FakeTorch()
        events = self.events

        class FakeASRModel:
            @classmethod
            def from_pretrained(cls, target: str, **kwargs: object) -> "FakeASRModel":
                events.append(("load-asr", (target, kwargs)))
                return cls()

            def transcribe(self, **kwargs: object) -> list[SimpleNamespace]:
                events.append(("transcribe", kwargs))
                return [SimpleNamespace(text="Test.")]

        class FakeAligner:
            @classmethod
            def from_pretrained(cls, target: str, **kwargs: object) -> "FakeAligner":
                events.append(("load-aligner", (target, kwargs)))
                return cls()

            def align(self, **kwargs: object) -> list[list[SimpleNamespace]]:
                events.append(("align", kwargs))
                return [
                    [
                        SimpleNamespace(
                            text="Test",
                            start_time=0.1,
                            end_time=1.5,
                        )
                    ]
                ]

        self.asr_model = FakeASRModel
        self.aligner = FakeAligner

    def runtime(self) -> tuple[object, FakeTorch, type[object], type[object]]:
        return object(), self.torch, self.asr_model, self.aligner


def worker_args(directory: Path) -> argparse.Namespace:
    return argparse.Namespace(
        input=directory / "source.m4a",
        output=directory / "raw.json",
        aligned_output=directory / "aligned.json",
        model=cuda_worker.DEFAULT_MODEL,
        model_path=None,
        aligner=cuda_worker.DEFAULT_ALIGNER,
        aligner_path=None,
        language="English",
        temperature=0.0,
        max_tokens=2048,
        chunk_duration=120.0,
        chunk_context=5.0,
        max_sentence_characters=160,
        device="cuda:0",
        dtype="float16",
        attention_implementation="sdpa",
        verbose=False,
        retranscribe=False,
        realign=False,
    )


class ArgumentAndResultValidationTests(unittest.TestCase):
    def test_cli_defaults_to_bfloat16_batch_one_configuration(self) -> None:
        argv = [
            "transcribe_qwen3_asr_cuda.py",
            "--input",
            "source.m4a",
            "--output",
            "raw.json",
            "--aligned-output",
            "aligned.json",
        ]
        with patch.object(cuda_worker.sys, "argv", argv):
            args = cuda_worker.parse_args()

        self.assertEqual(args.dtype, "bfloat16")
        self.assertEqual(args.chunk_duration, 120.0)
        self.assertEqual(args.chunk_context, 5.0)
        self.assertEqual(cuda_worker.MAX_INFERENCE_BATCH_SIZE, 1)

    def test_chunks_audio_with_bounded_context_and_gapless_ownership(self) -> None:
        self.assertEqual(
            list(
                cuda_worker.audio_chunk_ranges(
                    250.0,
                    chunk_duration=120.0,
                    chunk_context=5.0,
                )
            ),
            [
                cuda_worker.AudioChunkWindow(0.0, 120.0, 0.0, 125.0),
                cuda_worker.AudioChunkWindow(120.0, 185.0, 115.0, 190.0),
                cuda_worker.AudioChunkWindow(185.0, 250.0, 180.0, 250.0),
            ],
        )

    def test_rebalances_a_short_final_remainder_across_the_last_two_chunks(self) -> None:
        windows = list(
            cuda_worker.audio_chunk_ranges(
                2171.5,
                chunk_duration=120.0,
                chunk_context=5.0,
            )
        )

        self.assertEqual(len(windows), 19)
        self.assertEqual(
            windows[-2:],
            [
                cuda_worker.AudioChunkWindow(2040.0, 2105.75, 2035.0, 2110.75),
                cuda_worker.AudioChunkWindow(2105.75, 2171.5, 2100.75, 2171.5),
            ],
        )
        self.assertTrue(
            all(
                window.ownership_end - window.ownership_start <= 120.0
                and window.decode_end - window.decode_start <= 130.0
                for window in windows
            )
        )

    def test_allows_sample_rounding_at_the_final_decode_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            args = worker_args(Path(directory))
            backend_options = cuda_worker.raw_backend_options(args)
            document = {
                "audio": {
                    "sample_rate_hz": cuda_worker.SAMPLE_RATE,
                    "duration_seconds": 2.001,
                },
                "options": {
                    "temperature": args.temperature,
                    "max_tokens_per_chunk": args.max_tokens,
                    "chunk_duration_seconds": args.chunk_duration,
                    "chunk_context_seconds": args.chunk_context,
                    "boundary_reconciliation": (
                        cuda_worker.BOUNDARY_RECONCILIATION_METHOD
                    ),
                    "alignment_coverage_guard": cuda_worker.ALIGNMENT_COVERAGE_GUARD,
                    "aligned_gap_guard": cuda_worker.ALIGNED_GAP_GUARD,
                    **backend_options,
                },
                "boundary_reconciliation": {
                    "method": cuda_worker.BOUNDARY_RECONCILIATION_METHOD,
                    "status": "pending",
                    "chunk_context_seconds": args.chunk_context,
                    "seams": [],
                },
                "text": "Test.",
                "segments": [
                    {
                        "id": 0,
                        "start": 0.0,
                        "end": 2.001,
                        "decode_start": 0.0,
                        "decode_end": 2.0,
                        "decoded_text": "Test.",
                        "text": "Test.",
                    }
                ],
            }

            cuda_worker.validate_cuda_raw_integrity(
                document,
                args=args,
                backend_options=backend_options,
            )

    def test_allows_bounded_container_shortfall_only_at_final_decode_end(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            args = worker_args(Path(directory))
            backend_options = cuda_worker.raw_backend_options(args)
            duration_seconds = 3598.1
            windows = list(
                cuda_worker.audio_chunk_ranges(
                    duration_seconds,
                    chunk_duration=args.chunk_duration,
                    chunk_context=args.chunk_context,
                )
            )
            segments = [
                {
                    "id": index,
                    "start": cuda_worker.rounded_seconds(window.ownership_start),
                    "end": cuda_worker.rounded_seconds(window.ownership_end),
                    "decode_start": cuda_worker.rounded_seconds(window.decode_start),
                    "decode_end": cuda_worker.rounded_seconds(window.decode_end),
                    "decoded_text": "Test.",
                    "text": "Test.",
                }
                for index, window in enumerate(windows)
            ]
            # Real #20 shape: ffprobe reports 3598.100s, while the final
            # 16 kHz decode contains samples only through 3598.002s.
            segments[-1]["decode_end"] = 3598.002
            document = {
                "audio": {
                    "sample_rate_hz": cuda_worker.SAMPLE_RATE,
                    "duration_seconds": duration_seconds,
                },
                "options": {
                    "temperature": args.temperature,
                    "max_tokens_per_chunk": args.max_tokens,
                    "chunk_duration_seconds": args.chunk_duration,
                    "chunk_context_seconds": args.chunk_context,
                    "boundary_reconciliation": (
                        cuda_worker.BOUNDARY_RECONCILIATION_METHOD
                    ),
                    "alignment_coverage_guard": cuda_worker.ALIGNMENT_COVERAGE_GUARD,
                    "aligned_gap_guard": cuda_worker.ALIGNED_GAP_GUARD,
                    **backend_options,
                },
                "boundary_reconciliation": {
                    "method": cuda_worker.BOUNDARY_RECONCILIATION_METHOD,
                    "status": "pending",
                    "chunk_context_seconds": args.chunk_context,
                    "seams": [],
                },
                "text": cuda_worker.join_transcript_chunks(
                    [segment["text"] for segment in segments],
                    language=args.language,
                ),
                "segments": segments,
            }

            cuda_worker.validate_cuda_raw_integrity(
                document,
                args=args,
                backend_options=backend_options,
            )

            internal_shortfall = copy.deepcopy(document)
            internal_shortfall["segments"][0]["decode_end"] = 124.989
            with self.assertRaisesRegex(ValueError, "invalid ownership"):
                cuda_worker.validate_cuda_raw_integrity(
                    internal_shortfall,
                    args=args,
                    backend_options=backend_options,
                )

            excessive_final_shortfall = copy.deepcopy(document)
            excessive_final_shortfall["segments"][-1]["decode_end"] = 3597.974
            with self.assertRaisesRegex(ValueError, "invalid ownership"):
                cuda_worker.validate_cuda_raw_integrity(
                    excessive_final_shortfall,
                    args=args,
                    backend_options=backend_options,
                )

    def test_reconciles_an_exact_time_constrained_boundary_once(self) -> None:
        left = [
            {"text": "它", "start": 119.5, "end": 119.8},
            {"text": "离", "start": 119.8, "end": 120.1},
            {"text": "呃", "start": 120.6, "end": 120.9},
            {"text": "上", "start": 120.9, "end": 121.1},
        ]
        right = [
            {"text": "它", "start": 119.45, "end": 119.75},
            {"text": "离", "start": 119.78, "end": 120.12},
            {"text": "呃", "start": 120.65, "end": 120.85},
            {"text": "上", "start": 120.92, "end": 121.08},
        ]

        left_stop, right_start, record = cuda_worker.seam_crossover(
            left,
            right,
            seam_seconds=120.0,
            shared_start=115.0,
            shared_end=125.0,
        )

        self.assertEqual(left_stop, 2)
        self.assertEqual(right_start, 2)
        self.assertEqual(
            "".join(item["text"] for item in left[:left_stop])
            + "".join(item["text"] for item in right[right_start:]),
            "它离呃上",
        )
        self.assertEqual(record["strategy"], "exact-time-anchor")

    def test_rejects_same_text_outside_the_time_gate(self) -> None:
        with self.assertRaisesRegex(ValueError, "no reliable exact"):
            cuda_worker.seam_crossover(
                [{"text": "甲", "start": 119.0, "end": 121.0}],
                [{"text": "甲", "start": 125.0, "end": 127.0}],
                seam_seconds=120.0,
                shared_start=115.0,
                shared_end=130.0,
            )

    def test_does_not_choose_an_isolated_filler_over_a_reliable_match_run(self) -> None:
        left = [
            {"text": "甲", "start": 115.9, "end": 116.1},
            {"text": "乙", "start": 116.1, "end": 116.3},
            {"text": "丙", "start": 116.3, "end": 116.5},
            {"text": "嗯", "start": 119.8, "end": 120.0},
        ]
        right = [
            {"text": "甲", "start": 115.95, "end": 116.15},
            {"text": "乙", "start": 116.15, "end": 116.35},
            {"text": "丙", "start": 116.35, "end": 116.55},
            {"text": "啊", "start": 119.5, "end": 119.7},
            {"text": "嗯", "start": 119.85, "end": 120.05},
        ]

        _, _, record = cuda_worker.seam_crossover(
            left,
            right,
            seam_seconds=120.0,
            shared_start=115.0,
            shared_end=125.0,
        )

        self.assertEqual(record["anchor_text"], "丙")
        self.assertEqual(record["anchor_run_characters"], 3)

    def test_accepts_one_unique_tightly_aligned_two_character_run(self) -> None:
        left = [
            {"text": "a", "start": 119.0, "end": 119.1},
            {"text": "b", "start": 119.1, "end": 119.2},
            {"text": "x", "start": 119.8, "end": 120.2},
        ]
        right = [
            {"text": "a", "start": 119.08, "end": 119.18},
            {"text": "b", "start": 119.18, "end": 119.28},
            {"text": "y", "start": 119.8, "end": 120.2},
        ]

        _, _, record = cuda_worker.seam_crossover(
            left,
            right,
            seam_seconds=120.0,
            shared_start=115.0,
            shared_end=125.0,
        )

        self.assertEqual(record["anchor_run_characters"], 2)
        self.assertEqual(
            record["anchor_confidence"],
            "unique-tight-two-character-run",
        )
        self.assertAlmostEqual(
            record["anchor_run_max_pair_delta_seconds"],
            0.08,
        )

    def test_rejects_an_ambiguous_tightly_aligned_two_character_run(self) -> None:
        left = [
            {"text": "a", "start": 119.0, "end": 119.1},
            {"text": "b", "start": 119.1, "end": 119.2},
            {"text": "x", "start": 119.8, "end": 120.2},
        ]
        right = [
            {"text": "a", "start": 118.85, "end": 118.95},
            {"text": "b", "start": 118.95, "end": 119.05},
            {"text": "a", "start": 119.15, "end": 119.25},
            {"text": "b", "start": 119.25, "end": 119.35},
            {"text": "y", "start": 119.8, "end": 120.2},
        ]

        with self.assertRaisesRegex(ValueError, "no reliable exact"):
            cuda_worker.seam_crossover(
                left,
                right,
                seam_seconds=120.0,
                shared_start=115.0,
                shared_end=125.0,
            )

    def test_rejects_a_two_character_run_outside_the_strict_time_gate(self) -> None:
        left = [
            {"text": "a", "start": 119.0, "end": 119.1},
            {"text": "b", "start": 119.1, "end": 119.2},
            {"text": "x", "start": 119.8, "end": 120.2},
        ]
        right = [
            {"text": "a", "start": 119.251, "end": 119.351},
            {"text": "b", "start": 119.351, "end": 119.451},
            {"text": "y", "start": 119.8, "end": 120.2},
        ]

        with self.assertRaisesRegex(ValueError, "no reliable exact"):
            cuda_worker.seam_crossover(
                left,
                right,
                seam_seconds=120.0,
                shared_start=115.0,
                shared_end=125.0,
            )

    def test_maps_owned_items_back_to_original_punctuation(self) -> None:
        text = "前句。圣安东尼奥，下一句。"
        items = [
            {"text": character, "start_time": index, "end_time": index + 0.5}
            for index, character in enumerate("前句圣安东尼奥下一句")
        ]
        self.assertEqual(
            cuda_worker.text_for_alignment_slice(
                text,
                items,
                start_item=2,
                stop_item=7,
            ),
            "圣安东尼奥，",
        )

    def test_flags_sparse_text_and_a_long_unfinished_active_tail(self) -> None:
        suspicions = cuda_worker.alignment_coverage_suspicions(
            ownership_start=3240.0,
            ownership_end=3360.0,
            text="这段只有很少的识别文字",
            alignment=[{"text": "字", "start": 3240.48, "end": 3243.92}],
            is_first_chunk=False,
            is_last_chunk=False,
        )

        self.assertEqual(
            [suspicion["kind"] for suspicion in suspicions],
            ["sparse-text", "active-trailing-gap"],
        )

    def test_terminal_punctuation_only_exempts_a_moderate_tail(self) -> None:
        moderate = cuda_worker.alignment_coverage_suspicions(
            ownership_start=0.0,
            ownership_end=120.0,
            text="这是一段足够长的完整句子。" * 6,
            alignment=[{"text": "句", "start": 0.0, "end": 98.0}],
            is_first_chunk=True,
            is_last_chunk=False,
        )
        severe = cuda_worker.alignment_coverage_suspicions(
            ownership_start=0.0,
            ownership_end=120.0,
            text="这是一段足够长的完整句子。" * 6,
            alignment=[{"text": "句", "start": 0.0, "end": 80.0}],
            is_first_chunk=True,
            is_last_chunk=False,
        )

        self.assertFalse(any(item["kind"] == "active-trailing-gap" for item in moderate))
        self.assertTrue(any(item["kind"] == "active-trailing-gap" for item in severe))

    def test_flags_internal_leading_gaps_and_sparse_final_chunks(self) -> None:
        leading = cuda_worker.alignment_coverage_suspicions(
            ownership_start=120.0,
            ownership_end=240.0,
            text="这是一段持续说话而且足够长的识别文字" * 8,
            alignment=[{"text": "这", "start": 140.0, "end": 220.0}],
            is_first_chunk=False,
            is_last_chunk=False,
        )
        sparse_final = cuda_worker.alignment_coverage_suspicions(
            ownership_start=240.0,
            ownership_end=360.0,
            text="太短",
            alignment=[{"text": "短", "start": 240.0, "end": 244.0}],
            is_first_chunk=False,
            is_last_chunk=True,
        )

        self.assertTrue(any(item["kind"] == "active-leading-gap" for item in leading))
        self.assertTrue(any(item["kind"] == "sparse-text" for item in sparse_final))

    def test_coverage_ignores_items_that_only_touch_core_boundaries(self) -> None:
        suspicions = cuda_worker.alignment_coverage_suspicions(
            ownership_start=120.0,
            ownership_end=240.0,
            text="这是一段持续说话而且足够长的识别文字。" * 8,
            alignment=[
                {"text": "前", "start": 119.0, "end": 120.0},
                {"text": "中", "start": 140.0, "end": 200.0},
                {"text": "后", "start": 240.0, "end": 241.0},
            ],
            is_first_chunk=False,
            is_last_chunk=False,
        )

        kinds = {item["kind"] for item in suspicions}
        self.assertIn("active-leading-gap", kinds)
        self.assertIn("active-trailing-gap", kinds)

    def test_aligned_gap_requires_quiet_audio_across_the_gap(self) -> None:
        seam = {
            "strategy": "aligned-gap",
            "seam_seconds": 120.0,
            "gap_start_seconds": 119.0,
            "gap_end_seconds": 121.0,
        }
        with (
            patch.object(cuda_worker, "decode_audio_chunk", return_value=FakeAudio()),
            patch.object(cuda_worker, "contains_low_energy_window", return_value=True),
            patch.object(cuda_worker, "active_audio_statistics", return_value=(0.0, 0.0)),
        ):
            quiet = [copy.deepcopy(seam)]
            cuda_worker.enforce_aligned_gap_silence(
                input_path=Path("source.m4a"),
                seam_records=quiet,
                ffmpeg="ffmpeg",
                numpy_module=object(),
            )
        self.assertEqual(quiet[0]["acoustic_guard"]["status"], "verified")

        with (
            patch.object(cuda_worker, "decode_audio_chunk", return_value=FakeAudio()),
            patch.object(cuda_worker, "contains_low_energy_window", return_value=True),
            patch.object(cuda_worker, "active_audio_statistics", return_value=(0.5, 0.3)),
        ):
            with self.assertRaisesRegex(ValueError, "not acoustically quiet"):
                cuda_worker.enforce_aligned_gap_silence(
                    input_path=Path("source.m4a"),
                    seam_records=[copy.deepcopy(seam)],
                    ffmpeg="ffmpeg",
                    numpy_module=object(),
                )

    def test_coverage_guard_only_rejects_sustained_active_audio(self) -> None:
        chunks = [
            {
                "start": 0.0,
                "end": 120.0,
                "text": "太短",
                "alignment": [{"text": "短", "start": 0.0, "end": 4.0}],
            },
            {
                "start": 120.0,
                "end": 121.0,
                "text": "结尾",
                "alignment": [{"text": "结", "start": 120.0, "end": 121.0}],
            },
        ]
        with (
            patch.object(cuda_worker, "decode_audio_chunk", return_value=FakeAudio()),
            patch.object(cuda_worker, "active_audio_statistics", return_value=(0.0, 0.0)),
        ):
            cuda_worker.enforce_alignment_coverage(
                input_path=Path("source.m4a"),
                chunks=chunks,
                ffmpeg="ffmpeg",
                numpy_module=object(),
            )

        with (
            patch.object(cuda_worker, "decode_audio_chunk", return_value=FakeAudio()),
            patch.object(
                cuda_worker,
                "active_audio_statistics",
                return_value=(116.0, 0.99),
            ),
        ):
            with self.assertRaisesRegex(ValueError, "active-audio-coverage-v1"):
                cuda_worker.enforce_alignment_coverage(
                    input_path=Path("source.m4a"),
                    chunks=chunks,
                    ffmpeg="ffmpeg",
                    numpy_module=object(),
                )

    def test_short_final_unfinished_tail_is_probed_without_rejecting_outro(self) -> None:
        truncated = [
            {
                "start": 0.0,
                "end": 49.85,
                "text": "unfinished",
                "alignment": [{"text": "unfinished", "start": 0.0, "end": 10.0}],
            }
        ]
        with (
            patch.object(cuda_worker, "decode_audio_chunk", return_value=FakeAudio()),
            patch.object(
                cuda_worker,
                "active_audio_statistics",
                return_value=(39.85, 0.99),
            ),
        ):
            with self.assertRaisesRegex(ValueError, "active-trailing-gap"):
                cuda_worker.enforce_alignment_coverage(
                    input_path=Path("source.m4a"),
                    chunks=truncated,
                    ffmpeg="ffmpeg",
                    numpy_module=object(),
                )

        with (
            patch.object(cuda_worker, "decode_audio_chunk", return_value=FakeAudio()),
            patch.object(
                cuda_worker,
                "active_audio_statistics",
                return_value=(0.0, 0.0),
            ),
        ):
            cuda_worker.enforce_alignment_coverage(
                input_path=Path("source.m4a"),
                chunks=truncated,
                ffmpeg="ffmpeg",
                numpy_module=object(),
            )

        completed_before_outro = copy.deepcopy(truncated)
        completed_before_outro[0]["text"] = "Finished."
        with patch.object(
            cuda_worker,
            "decode_audio_chunk",
            side_effect=AssertionError("completed outro must not be probed"),
        ):
            cuda_worker.enforce_alignment_coverage(
                input_path=Path("source.m4a"),
                chunks=completed_before_outro,
                ffmpeg="ffmpeg",
                numpy_module=object(),
            )

    def test_joins_space_delimited_languages_without_merging_words(self) -> None:
        self.assertEqual(
            cuda_worker.join_transcript_chunks(
                ["first chunk", "", "second chunk"],
                language="English",
            ),
            "first chunk second chunk",
        )
        self.assertEqual(
            cuda_worker.join_transcript_chunks(
                ["第一段", "第二段"],
                language="Chinese",
            ),
            "第一段第二段",
        )

    def test_segments_a_sentence_once_across_reconciled_chunk_ownership(self) -> None:
        text = "它离呃上海火车站非常的近。"
        items = [
            {
                "text": character,
                "start_time": 119.0 + index * 0.2,
                "end_time": 119.1 + index * 0.2,
            }
            for index, character in enumerate("它离呃上海火车站非常的近")
        ]
        segments = cuda_worker.transformers_sentence_segments(
            text=text,
            aligned_items=items,
            offset_seconds=0.0,
            chunk_id=0,
            first_segment_id=0,
            max_characters=160,
            item_source_chunk_ids=[0, 0, *([1] * (len(items) - 2))],
        )

        self.assertEqual(len(segments), 1)
        self.assertEqual(segments[0]["text"], text)
        self.assertEqual(segments[0]["source_chunk_id"], 0)

    def test_rejects_non_monotonic_global_sentence_alignment(self) -> None:
        with self.assertRaisesRegex(ValueError, "globally monotonic"):
            cuda_worker.transformers_sentence_segments(
                text="AB",
                aligned_items=[
                    {"text": "A", "start_time": 1.0, "end_time": 1.2},
                    {"text": "B", "start_time": 0.9, "end_time": 1.1},
                ],
                offset_seconds=0.0,
                chunk_id=0,
                first_segment_id=0,
                max_characters=160,
            )

    def test_detects_same_size_input_mutation_during_processing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "source.m4a"
            path.write_bytes(b"original")
            digest = sha256_file(path)
            path.write_bytes(b"modified")

            with self.assertRaisesRegex(ValueError, "SHA-256 changed"):
                cuda_worker.validate_file_identity(
                    path,
                    expected_size_bytes=8,
                    expected_sha256=digest,
                    label="input audio",
                )

    def test_rejects_cpu_fallback_and_sampling_temperature(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            args = worker_args(Path(directory))
            args.device = "cpu"
            with self.assertRaisesRegex(ValueError, "explicit cuda"):
                cuda_worker.validate_arguments(args)

            args.device = "cuda:0"
            args.temperature = 0.1
            with self.assertRaisesRegex(ValueError, "temperature 0"):
                cuda_worker.validate_arguments(args)

            args.temperature = 0.0
            args.chunk_duration = float("nan")
            with self.assertRaisesRegex(ValueError, "chunk duration"):
                cuda_worker.validate_arguments(args)

            args.chunk_duration = 120.0
            args.chunk_context = float("nan")
            with self.assertRaisesRegex(ValueError, "chunk context"):
                cuda_worker.validate_arguments(args)

            args.chunk_context = 5.0
            args.chunk_duration = 181.0
            with self.assertRaisesRegex(ValueError, "both context margins"):
                cuda_worker.validate_arguments(args)

            args.chunk_duration = 120.0
            args.language = "Arabic"
            with self.assertRaisesRegex(ValueError, "not supported"):
                cuda_worker.validate_arguments(args)

    def test_rejects_non_finite_or_out_of_bounds_alignment(self) -> None:
        with self.assertRaisesRegex(ValueError, "invalid alignment item 0 start"):
            cuda_worker.validate_alignment_items(
                [SimpleNamespace(text="Test", start_time=float("nan"), end_time=1.0)],
                chunk_duration=2.0,
            )
        with self.assertRaisesRegex(ValueError, "exceeds its audio chunk"):
            cuda_worker.validate_alignment_items(
                [SimpleNamespace(text="Test", start_time=0.1, end_time=3.1)],
                chunk_duration=2.0,
            )

    def test_clamps_alignment_timestamp_inside_model_tolerance(self) -> None:
        self.assertEqual(
            cuda_worker.validate_alignment_items(
                [SimpleNamespace(text="Test", start_time=1.9, end_time=2.2)],
                chunk_duration=2.0,
            ),
            [{"text": "Test", "start_time": 1.9, "end_time": 2.0}],
        )

    def test_clamps_observed_cuda_alignment_boundary_drift(self) -> None:
        self.assertEqual(
            cuda_worker.validate_alignment_items(
                [SimpleNamespace(text="尾", start_time=2.08, end_time=2.8)],
                chunk_duration=2.0,
            ),
            [{"text": "尾", "start_time": 2.0, "end_time": 2.0}],
        )

    def test_maps_official_tokens_after_punctuation_is_removed(self) -> None:
        segments = cuda_worker.transformers_sentence_segments(
            text="Qwen3-ASR 3.14 AI、ASR。",
            aligned_items=[
                {"text": "Qwen3ASR", "start_time": 0.1, "end_time": 0.5},
                {"text": "314", "start_time": 0.6, "end_time": 0.9},
                {"text": "AIASR", "start_time": 1.0, "end_time": 1.4},
            ],
            offset_seconds=10.0,
            chunk_id=2,
            first_segment_id=5,
            max_characters=160,
        )

        self.assertEqual(
            segments,
            [
                {
                    "id": 5,
                    "start": 10.1,
                    "end": 11.4,
                    "text": "Qwen3-ASR 3.14 AI、ASR。",
                    "source_chunk_id": 2,
                }
            ],
        )

    def test_coalesces_sentence_boundary_inside_one_official_token(self) -> None:
        segments = cuda_worker.transformers_sentence_segments(
            text="AI。ASR。",
            aligned_items=[
                {"text": "AIASR", "start_time": 0.1, "end_time": 0.8},
            ],
            offset_seconds=0.0,
            chunk_id=0,
            first_segment_id=0,
            max_characters=160,
        )

        self.assertEqual(len(segments), 1)
        self.assertEqual(segments[0]["text"], "AI。ASR。")


class ResumableWorkerTests(unittest.TestCase):
    def run_worker(
        self,
        args: argparse.Namespace,
        harness: WorkerHarness,
        *,
        duration_seconds: float = 2.0,
    ) -> int:
        def decoded_audio(*_args: object, **kwargs: object) -> FakeAudio:
            duration = float(kwargs["end_seconds"]) - float(kwargs["start_seconds"])
            return FakeAudio(round(duration * cuda_worker.SAMPLE_RATE))

        with (
            patch.object(cuda_worker, "parse_args", return_value=args),
            patch.object(cuda_worker.shutil, "which", side_effect=lambda name: name),
            patch.object(
                cuda_worker,
                "probe_audio_duration",
                return_value=duration_seconds,
            ),
            patch.object(cuda_worker, "decode_audio_chunk", side_effect=decoded_audio),
            patch.object(cuda_worker, "load_cuda_runtime", side_effect=harness.runtime),
            contextlib.redirect_stdout(io.StringIO()),
        ):
            return cuda_worker.main()

    def test_fresh_run_writes_strict_lineage_and_uses_batch_one(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            harness = WorkerHarness()

            self.assertEqual(self.run_worker(args, harness), 0)

            raw = read_json_strict(args.output)
            aligned = read_json_strict(args.aligned_output)
            self.assertEqual(raw["engine"], "qwen-asr-transformers")
            self.assertEqual(raw["model"], cuda_worker.DEFAULT_MODEL)
            self.assertEqual(raw["options"]["backend"], "transformers")
            self.assertEqual(raw["options"]["qwen_asr_version"], "0.0.6")
            self.assertEqual(raw["options"]["torch_version"], "2.11.0")
            self.assertEqual(raw["options"]["max_inference_batch_size"], 1)
            self.assertEqual(aligned["source"]["aligner"], cuda_worker.DEFAULT_ALIGNER)
            self.assertEqual(aligned["source"]["audio_sha256"], sha256_file(args.input))
            self.assertEqual(aligned["source"]["raw_asr_sha256"], sha256_file(args.output))
            self.assertNotIn(b"\r\n", args.output.read_bytes())
            self.assertNotIn(b"\r\n", args.aligned_output.read_bytes())

            load_asr = next(value for event, value in harness.events if event == "load-asr")
            load_aligner = next(
                value for event, value in harness.events if event == "load-aligner"
            )
            self.assertEqual(load_asr[1]["max_inference_batch_size"], 1)
            self.assertEqual(load_asr[1]["device_map"], "cuda:0")
            self.assertEqual(load_asr[1]["attn_implementation"], "sdpa")
            self.assertNotIn("max_inference_batch_size", load_aligner[1])
            self.assertEqual(harness.torch.cuda.current_device, 0)
            self.assertLess(
                next(i for i, event in enumerate(harness.events) if event[0] == "transcribe"),
                next(i for i, event in enumerate(harness.events) if event[0] == "load-aligner"),
            )

    def test_main_renders_one_sentence_across_two_reconciled_chunks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            args.language = "Chinese"
            args.chunk_duration = 2.0
            args.chunk_context = 1.0
            harness = WorkerHarness()
            events = harness.events
            transcriptions = iter(("它离呃上", "离呃上海。"))

            class MultiChunkASR:
                @classmethod
                def from_pretrained(cls, target: str, **kwargs: object) -> "MultiChunkASR":
                    events.append(("load-asr", (target, kwargs)))
                    return cls()

                def transcribe(self, **kwargs: object) -> list[SimpleNamespace]:
                    events.append(("transcribe", kwargs))
                    return [SimpleNamespace(text=next(transcriptions))]

            class MultiChunkAligner:
                @classmethod
                def from_pretrained(
                    cls, target: str, **kwargs: object
                ) -> "MultiChunkAligner":
                    events.append(("load-aligner", (target, kwargs)))
                    return cls()

                def align(self, **kwargs: object) -> list[list[SimpleNamespace]]:
                    events.append(("align", kwargs))
                    if kwargs["text"] == "它离呃上":
                        values = (
                            ("它", 0.5, 0.7),
                            ("离", 1.5, 1.7),
                            ("呃", 2.0, 2.2),
                            ("上", 2.4, 2.6),
                        )
                    else:
                        values = (
                            ("离", 0.5, 0.7),
                            ("呃", 1.0, 1.2),
                            ("上", 1.4, 1.6),
                            ("海", 2.0, 2.2),
                        )
                    return [
                        [
                            SimpleNamespace(text=text, start_time=start, end_time=end)
                            for text, start, end in values
                        ]
                    ]

            harness.asr_model = MultiChunkASR
            harness.aligner = MultiChunkAligner

            self.assertEqual(
                self.run_worker(args, harness, duration_seconds=4.0),
                0,
            )

            raw = read_json_strict(args.output)
            aligned = read_json_strict(args.aligned_output)
            self.assertEqual(raw["text"], "它离呃上海。")
            self.assertEqual(len(raw["boundary_reconciliation"]["seams"]), 1)
            self.assertGreaterEqual(
                raw["boundary_reconciliation"]["seams"][0][
                    "anchor_run_characters"
                ],
                3,
            )
            self.assertEqual(len(aligned["segments"]), 1)
            self.assertEqual(aligned["segments"][0]["text"], raw["text"])
            self.assertEqual(aligned["segments"][0]["source_chunk_id"], 0)

    def test_local_snapshots_enable_offline_mode_and_are_passed_directly(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            args.model_path = root / "model"
            args.aligner_path = root / "aligner"
            for model_path in (args.model_path, args.aligner_path):
                model_path.mkdir()
                (model_path / "config.json").write_text("{}", encoding="utf-8")
                (model_path / "model.safetensors").write_bytes(b"weights")
            harness = WorkerHarness()

            with patch.dict(
                cuda_worker.os.environ,
                {"HF_HUB_OFFLINE": "0", "TRANSFORMERS_OFFLINE": "0"},
                clear=True,
            ):
                self.assertEqual(self.run_worker(args, harness), 0)
                self.assertEqual(cuda_worker.os.environ["HF_HUB_OFFLINE"], "1")
                self.assertEqual(cuda_worker.os.environ["TRANSFORMERS_OFFLINE"], "1")

            load_asr = next(value for event, value in harness.events if event == "load-asr")
            load_aligner = next(
                value for event, value in harness.events if event == "load-aligner"
            )
            self.assertEqual(load_asr[0], args.model_path.resolve().as_posix())
            self.assertEqual(load_aligner[0], args.aligner_path.resolve().as_posix())

    def test_complete_resume_does_not_import_cuda_or_touch_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            self.assertEqual(self.run_worker(args, WorkerHarness()), 0)
            raw_bytes = args.output.read_bytes()
            aligned_bytes = args.aligned_output.read_bytes()

            with (
                patch.object(cuda_worker, "parse_args", return_value=args),
                patch.object(
                    cuda_worker,
                    "load_cuda_runtime",
                    side_effect=AssertionError("CUDA must not load"),
                ),
                contextlib.redirect_stdout(io.StringIO()),
            ):
                self.assertEqual(cuda_worker.main(), 0)

            self.assertEqual(args.output.read_bytes(), raw_bytes)
            self.assertEqual(args.aligned_output.read_bytes(), aligned_bytes)

    def test_align_only_skips_asr_model_and_reuses_valid_raw(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            self.assertEqual(self.run_worker(args, WorkerHarness()), 0)
            args.aligned_output.unlink()

            harness = WorkerHarness()

            class ForbiddenASR:
                @classmethod
                def from_pretrained(cls, *args: object, **kwargs: object) -> object:
                    raise AssertionError("ASR model must not load during align-only")

            harness.asr_model = ForbiddenASR
            self.assertEqual(self.run_worker(args, harness), 0)
            self.assertFalse(any(event == "load-asr" for event, _ in harness.events))
            self.assertTrue(any(event == "load-aligner" for event, _ in harness.events))

    def test_pending_raw_with_stale_aligned_self_heals_as_align_only(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            self.assertEqual(self.run_worker(args, WorkerHarness()), 0)

            raw = read_json_strict(args.output)
            raw["boundary_reconciliation"]["status"] = "pending"
            raw["boundary_reconciliation"]["seams"] = []
            for segment in raw["segments"]:
                segment["text"] = segment["decoded_text"]
                segment.pop("owned_item_start")
                segment.pop("owned_item_stop")
            raw["text"] = cuda_worker.join_transcript_chunks(
                [segment["text"] for segment in raw["segments"]],
                language=args.language,
            )
            write_json_atomically(args.output, raw)
            stale_aligned = args.aligned_output.read_bytes()

            harness = WorkerHarness()
            self.assertEqual(self.run_worker(args, harness), 0)

            self.assertFalse(any(event == "load-asr" for event, _ in harness.events))
            self.assertEqual(
                read_json_strict(args.output)["boundary_reconciliation"]["status"],
                "complete",
            )
            self.assertNotEqual(args.aligned_output.read_bytes(), stale_aligned)
            self.assertEqual(
                read_json_strict(args.aligned_output)["source"]["raw_asr_sha256"],
                sha256_file(args.output),
            )

    def test_pending_raw_modified_during_alignment_is_not_overwritten(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            self.assertEqual(self.run_worker(args, WorkerHarness()), 0)

            raw = read_json_strict(args.output)
            raw["boundary_reconciliation"]["status"] = "pending"
            raw["boundary_reconciliation"]["seams"] = []
            for segment in raw["segments"]:
                segment["text"] = segment["decoded_text"]
                segment.pop("owned_item_start")
                segment.pop("owned_item_stop")
            raw["text"] = cuda_worker.join_transcript_chunks(
                [segment["text"] for segment in raw["segments"]],
                language=args.language,
            )
            write_json_atomically(args.output, raw)
            stale_aligned = args.aligned_output.read_bytes()

            harness = WorkerHarness()
            base_aligner = harness.aligner

            class ConcurrentRawMutationAligner(base_aligner):
                def align(self, **kwargs: object) -> list[list[SimpleNamespace]]:
                    concurrently_changed = read_json_strict(args.output)
                    concurrently_changed["generated_at"] = "concurrent-change"
                    write_json_atomically(args.output, concurrently_changed)
                    return super().align(**kwargs)

            harness.aligner = ConcurrentRawMutationAligner
            with self.assertRaisesRegex(
                ValueError, "raw ASR changed while forced alignment was running"
            ):
                self.run_worker(args, harness)

            self.assertEqual(
                read_json_strict(args.output)["generated_at"],
                "concurrent-change",
            )
            self.assertEqual(args.aligned_output.read_bytes(), stale_aligned)

    def test_changed_audio_is_rejected_before_cuda_load(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            self.assertEqual(self.run_worker(args, WorkerHarness()), 0)
            args.input.write_bytes(b"evil-audio")

            with (
                patch.object(cuda_worker, "parse_args", return_value=args),
                patch.object(
                    cuda_worker,
                    "load_cuda_runtime",
                    side_effect=AssertionError("CUDA must not load"),
                ),
                contextlib.redirect_stdout(io.StringIO()),
            ):
                with self.assertRaisesRegex(ValueError, "SHA-256"):
                    cuda_worker.main()

    def test_resume_rejects_extra_backend_option_and_wrong_raw_path(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            self.assertEqual(self.run_worker(args, WorkerHarness()), 0)

            raw = read_json_strict(args.output)
            raw["options"]["untracked_semantic_option"] = True
            write_json_atomically(args.output, raw)
            with patch.object(cuda_worker, "parse_args", return_value=args):
                with self.assertRaisesRegex(ValueError, "do not match exactly"):
                    cuda_worker.main()

            raw["options"].pop("untracked_semantic_option")
            write_json_atomically(args.output, raw)
            aligned = read_json_strict(args.aligned_output)
            aligned["source"]["raw_asr_sha256"] = sha256_file(args.output)
            aligned["source"]["raw_asr_path"] = "other/raw.json"
            write_json_atomically(args.aligned_output, aligned)
            with patch.object(cuda_worker, "parse_args", return_value=args):
                with self.assertRaisesRegex(ValueError, "raw artifact path"):
                    cuda_worker.main()

    def test_tampered_decode_window_is_rejected_before_cuda_load(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            self.assertEqual(self.run_worker(args, WorkerHarness()), 0)

            raw = read_json_strict(args.output)
            raw["segments"][0]["decode_end"] = 999.0
            write_json_atomically(args.output, raw)
            with (
                patch.object(cuda_worker, "parse_args", return_value=args),
                patch.object(
                    cuda_worker,
                    "load_cuda_runtime",
                    side_effect=AssertionError("CUDA must not load"),
                ),
            ):
                with self.assertRaisesRegex(ValueError, "invalid ownership"):
                    cuda_worker.main()

    def test_negative_duration_owned_alignment_is_rejected_on_noop(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            self.assertEqual(self.run_worker(args, WorkerHarness()), 0)

            aligned = read_json_strict(args.aligned_output)
            aligned["chunks"][0]["alignment"][0]["end"] = 0.0
            write_json_atomically(args.aligned_output, aligned)
            with patch.object(cuda_worker, "parse_args", return_value=args):
                with self.assertRaisesRegex(ValueError, "invalid owned timestamps"):
                    cuda_worker.main()


if __name__ == "__main__":
    unittest.main()
