from __future__ import annotations

import argparse
import ast
import contextlib
import hashlib
import io
import sys
import tempfile
import types
import unittest
from importlib.metadata import PackageNotFoundError, distribution
from pathlib import Path
from unittest.mock import patch

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import transcribe_qwen3_asr as mlx_worker  # noqa: E402
from transcribe_qwen3_asr import (  # noqa: E402
    alignment_units,
    effective_total_token_budget,
    finite_document_number,
    generate_mlx_planned_chunks,
    plan_mlx_generation,
    read_json_strict,
    resume_mode,
    sentence_segments,
    sentence_texts,
    sha256_file,
    validate_aligned_document,
    validate_raw_document,
    write_json_atomically,
)
from render_asr_transcript import clean_text  # noqa: E402


class RefinementTests(unittest.TestCase):
    def test_does_not_apply_cross_episode_proper_noun_replacements(self) -> None:
        self.assertEqual(
            clean_text("翁嘉译在 WhyNot TV 介绍天授。"),
            "翁嘉译在 WhyNot TV 介绍天授。",
        )


class ArtifactWriterTests(unittest.TestCase):
    def test_json_artifacts_use_lf_bytes_on_every_platform(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "raw.json"
            write_json_atomically(output, {"kind": "raw-asr", "segments": []})

            self.assertNotIn(b"\r\n", output.read_bytes())


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


class TokenBudgetTests(unittest.TestCase):
    class FakeAudio:
        def __init__(self, sample_count: int) -> None:
            self.sample_count = sample_count

        def __len__(self) -> int:
            return self.sample_count

        def __getitem__(self, item: slice) -> TokenBudgetTests.FakeAudio:
            if not isinstance(item, slice):
                raise TypeError("FakeAudio only supports slices")
            start, stop, step = item.indices(self.sample_count)
            if step != 1:
                raise ValueError("FakeAudio only supports contiguous slices")
            return TokenBudgetTests.FakeAudio(max(0, stop - start))

    @staticmethod
    def nominal_splitter(
        audio: object, *, sr: int, chunk_duration: float
    ) -> list[tuple[FakeAudio, float]]:
        sample_count = len(audio)  # type: ignore[arg-type]
        chunk_samples = int(sr * chunk_duration)
        chunks: list[tuple[TokenBudgetTests.FakeAudio, float]] = []
        for start in range(0, sample_count, chunk_samples):
            source_samples = min(chunk_samples, sample_count - start)
            planned_samples = max(source_samples, sr)
            chunks.append((TokenBudgetTests.FakeAudio(planned_samples), start / sr))
        return chunks

    def test_expands_per_chunk_budget_from_exact_planned_chunk_count(self) -> None:
        self.assertEqual(
            effective_total_token_budget(
                per_chunk_budget=4096,
                planned_chunk_count=27,
            ),
            4096 * 27,
        )

    def test_plans_just_below_equal_and_just_above_chunk_boundary(self) -> None:
        boundary_samples = 240 * mlx_worker.SAMPLE_RATE
        cases = (
            (boundary_samples - 1, 1),
            (boundary_samples, 1),
            (boundary_samples + 1, 2),
        )
        for sample_count, expected_chunks in cases:
            with self.subTest(sample_count=sample_count):
                chunks, total_budget = plan_mlx_generation(
                    self.FakeAudio(sample_count),
                    sample_rate=mlx_worker.SAMPLE_RATE,
                    chunk_duration_seconds=240.0,
                    per_chunk_budget=4096,
                    split_audio_into_chunks=self.nominal_splitter,
                )
                self.assertEqual(len(chunks), expected_chunks)
                self.assertEqual(total_budget, 4096 * expected_chunks)

    def test_silence_aware_plan_can_exceed_nominal_duration_ceiling(self) -> None:
        audio = self.FakeAudio(480 * mlx_worker.SAMPLE_RATE)

        def early_silence_splitter(
            _audio: object, *, sr: int, chunk_duration: float
        ) -> list[tuple[TokenBudgetTests.FakeAudio, float]]:
            self.assertEqual(sr, mlx_worker.SAMPLE_RATE)
            self.assertEqual(chunk_duration, 240.0)
            return [
                (self.FakeAudio(235 * sr), 0.0),
                (self.FakeAudio(235 * sr), 235.0),
                (self.FakeAudio(10 * sr), 470.0),
            ]

        chunks, total_budget = plan_mlx_generation(
            audio,
            sample_rate=mlx_worker.SAMPLE_RATE,
            chunk_duration_seconds=240.0,
            per_chunk_budget=4096,
            split_audio_into_chunks=early_silence_splitter,
        )
        self.assertEqual(len(chunks), 3)
        self.assertEqual(total_budget, 3 * 4096)


class AdaptiveSplitSelectionTests(unittest.TestCase):
    def test_quantizes_pcm_with_half_away_from_zero_and_clipping(self) -> None:
        half = 0.5 / 32768
        samples = np.array([-2.0, -1.0, -half, 0.0, half, 1.0, 2.0])

        self.assertEqual(
            mlx_worker.quantize_pcm_s16(samples).tolist(),
            [-32768, -32768, -1, 0, 1, 32767, 32767],
        )

    def test_rejects_non_finite_pcm(self) -> None:
        for value in (np.nan, np.inf, -np.inf):
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, "finite mono PCM"):
                mlx_worker.quantize_pcm_s16(np.array([0.0, value]))

    def test_selects_global_low_energy_then_center_then_left(self) -> None:
        sample_count = 60 * mlx_worker.SAMPLE_RATE
        center = sample_count // 2
        far_quiet = 22 * mlx_worker.SAMPLE_RATE
        pcm = np.ones(sample_count, dtype=np.int16)
        half_window = mlx_worker.MLX_ADAPTIVE_ENERGY_WINDOW_SAMPLES // 2
        pcm[far_quiet - half_window : far_quiet + half_window] = 0
        split, energy = mlx_worker.select_adaptive_split_sample(
            pcm,
            parent_start_sample=0,
            parent_end_sample=sample_count,
        )
        self.assertEqual((split, energy), (far_quiet, 0))
        self.assertNotEqual(split, center)

        pcm[:] = 1
        for candidate in (25 * mlx_worker.SAMPLE_RATE, 35 * mlx_worker.SAMPLE_RATE):
            pcm[candidate - half_window : candidate + half_window] = 0
        split, _ = mlx_worker.select_adaptive_split_sample(
            pcm,
            parent_start_sample=0,
            parent_end_sample=sample_count,
        )
        self.assertEqual(split, 25 * mlx_worker.SAMPLE_RATE)

    def test_zero_energy_ties_use_integer_center_and_left_for_odd_length(self) -> None:
        sample_count = 60 * mlx_worker.SAMPLE_RATE + 1
        split, energy = mlx_worker.select_adaptive_split_sample(
            np.zeros(sample_count, dtype=np.int16),
            parent_start_sample=123,
            parent_end_sample=123 + sample_count,
        )

        self.assertEqual(split, 123 + sample_count // 2)
        self.assertEqual(energy, 0)

    def test_forty_seconds_has_exactly_one_legal_split(self) -> None:
        sample_count = 40 * mlx_worker.SAMPLE_RATE
        split, _ = mlx_worker.select_adaptive_split_sample(
            np.ones(sample_count, dtype=np.int16),
            parent_start_sample=500,
            parent_end_sample=500 + sample_count,
        )
        self.assertEqual(split, 500 + 20 * mlx_worker.SAMPLE_RATE)

        with self.assertRaisesRegex(ValueError, "20-second leaf minimum"):
            mlx_worker.select_adaptive_split_sample(
                np.ones(30 * mlx_worker.SAMPLE_RATE, dtype=np.int16),
                parent_start_sample=0,
                parent_end_sample=30 * mlx_worker.SAMPLE_RATE,
            )

    def test_45_second_parent_can_split_at_the_twenty_second_legal_boundary(self) -> None:
        sample_count = 45 * mlx_worker.SAMPLE_RATE + 2670
        split_sample = 20 * mlx_worker.SAMPLE_RATE
        pcm = np.ones(sample_count, dtype=np.int16)
        half_window = mlx_worker.MLX_ADAPTIVE_ENERGY_WINDOW_SAMPLES // 2
        pcm[split_sample - half_window : split_sample + half_window] = 0

        selected, energy = mlx_worker.select_adaptive_split_sample(
            pcm,
            parent_start_sample=0,
            parent_end_sample=sample_count,
        )

        self.assertEqual((selected, energy), (split_sample, 0))
        self.assertEqual(sample_count - selected, 25 * mlx_worker.SAMPLE_RATE + 2670)


class PlannedChunkGenerationTests(unittest.TestCase):
    @staticmethod
    def result(*, text: str, sample_count: int, generation_tokens: int) -> object:
        return types.SimpleNamespace(
            text=text,
            segments=[
                {
                    "start": 0.0,
                    "end": sample_count / mlx_worker.SAMPLE_RATE,
                    "text": text,
                }
            ],
            prompt_tokens=64,
            generation_tokens=generation_tokens,
        )

    def generate(
        self,
        results: list[object],
        *,
        planned_chunks: list[tuple[TokenBudgetTests.FakeAudio, float]] | None = None,
        audio_sample_count: int = 24_000,
    ) -> tuple[dict[str, object], list[dict[str, object]], list[None]]:
        calls: list[dict[str, object]] = []
        cache_clears: list[None] = []

        class FakeModel:
            def generate(self, audio: object, **kwargs: object) -> object:
                calls.append({"audio": audio, **kwargs})
                return results[len(calls) - 1]

        if planned_chunks is None:
            planned_chunks = [
                (TokenBudgetTests.FakeAudio(16_000), 0.0),
                (TokenBudgetTests.FakeAudio(16_000), 1.0),
            ]
        generated = generate_mlx_planned_chunks(
            FakeModel(),
            planned_chunks,
            audio_sample_count=audio_sample_count,
            sample_rate=mlx_worker.SAMPLE_RATE,
            per_chunk_budget=4096,
            temperature=0.0,
            language="Chinese",
            verbose=False,
            clear_cache=lambda: cache_clears.append(None),
            quantize_pcm=lambda audio: np.zeros(len(audio), dtype=np.int16),
        )
        return generated, calls, cache_clears

    def test_generates_each_planned_chunk_with_an_independent_budget(self) -> None:
        generated, calls, cache_clears = self.generate(
            [
                self.result(text="第一段。", sample_count=16_000, generation_tokens=80),
                self.result(text="第二段。", sample_count=16_000, generation_tokens=90),
            ]
        )

        self.assertEqual(len(calls), 2)
        self.assertTrue(all(call["max_tokens"] == 4096 for call in calls))
        self.assertTrue(all(call["chunk_duration"] == (16_000 + 1) / 16_000 for call in calls))
        self.assertEqual(len(cache_clears), 2)
        self.assertEqual(generated["text"], "第一段。 第二段。")
        self.assertEqual(generated["prompt_tokens"], 128)
        self.assertEqual(generated["generation_tokens"], 170)
        self.assertEqual(
            generated["segments"],
            [
                {
                    "id": 0,
                    "initial_chunk_id": 0,
                    "split_path": "",
                    "start_sample": 0,
                    "end_sample": 16_000,
                    "start": 0.0,
                    "end": 1.0,
                    "text": "第一段。",
                    "generation_tokens": 80,
                },
                {
                    "id": 1,
                    "initial_chunk_id": 1,
                    "split_path": "",
                    "start_sample": 16_000,
                    "end_sample": 24_000,
                    "start": 1.0,
                    "end": 1.5,
                    "text": "第二段。",
                    "generation_tokens": 90,
                },
            ],
        )

        self.assertEqual(generated["adaptive_split_count"], 0)
        self.assertEqual(generated["attempt_generation_tokens"], 170)
        self.assertEqual(generated["generation_call_count"], 2)

    def test_rejects_exhausted_chunk_below_the_leaf_minimum(self) -> None:
        with self.assertRaisesRegex(ValueError, "below the adaptive leaf minimum"):
            self.generate(
                [self.result(text="异常。", sample_count=16_000, generation_tokens=4096)],
                planned_chunks=[(TokenBudgetTests.FakeAudio(16_000), 0.0)],
                # The dependency padded this 1 ms source ownership to 1 second;
                # padding must never make it eligible for adaptive splitting.
                audio_sample_count=mlx_worker.MIN_AUDIO_SAMPLE_COUNT,
            )

    def test_rejects_exhausted_thirty_nine_second_chunk_without_a_legal_split(self) -> None:
        sample_count = 39 * mlx_worker.SAMPLE_RATE
        with (
            patch.object(mlx_worker, "select_adaptive_split_sample") as select_split,
            self.assertRaisesRegex(ValueError, "below the adaptive leaf minimum"),
        ):
            self.generate(
                [self.result(text="仍触顶。", sample_count=sample_count, generation_tokens=4096)],
                planned_chunks=[(TokenBudgetTests.FakeAudio(sample_count), 0.0)],
                audio_sample_count=sample_count,
            )
        select_split.assert_not_called()

    def test_retries_only_an_exhausted_chunk_as_two_low_energy_leaves(self) -> None:
        sample_count = 60 * mlx_worker.SAMPLE_RATE
        audio = np.zeros(sample_count, dtype=np.float32)
        generated, calls, cache_clears = self.generate(
            [
                self.result(text="丢弃父块。", sample_count=sample_count, generation_tokens=4096),
                self.result(text="左叶。", sample_count=sample_count // 2, generation_tokens=80),
                self.result(text="右叶。", sample_count=sample_count // 2, generation_tokens=90),
            ],
            planned_chunks=[(audio, 0.0)],
            audio_sample_count=sample_count,
        )

        self.assertEqual(len(calls), 3)
        self.assertEqual(len(cache_clears), 3)
        self.assertEqual(generated["text"], "左叶。 右叶。")
        self.assertNotIn("丢弃父块。", generated["text"])
        self.assertEqual(generated["generation_tokens"], 170)
        self.assertEqual(generated["attempt_generation_tokens"], 4266)
        self.assertEqual(generated["prompt_tokens"], 128)
        self.assertEqual(generated["attempt_prompt_tokens"], 192)
        self.assertEqual(generated["generation_call_count"], 3)
        self.assertEqual(generated["initial_chunk_count"], 1)
        self.assertEqual(generated["final_leaf_chunk_count"], 2)
        self.assertEqual(generated["adaptive_split_count"], 1)
        self.assertEqual(
            [
                (segment["split_path"], segment["start_sample"], segment["end_sample"])
                for segment in generated["segments"]
            ],
            [("L", 0, sample_count // 2), ("R", sample_count // 2, sample_count)],
        )
        event = generated["generation_plan"]["split_events"][0]
        self.assertEqual(event["split_path"], "")
        self.assertEqual(event["split_sample"], sample_count // 2)
        self.assertEqual(event["cut_energy_sum_squares"], 0)
        self.assertEqual(event["parent_prompt_tokens"], 64)
        self.assertEqual(event["parent_generation_tokens"], 4096)

    def test_preserves_an_unexhausted_neighbor_while_splitting_only_the_hit(self) -> None:
        chunk_samples = 60 * mlx_worker.SAMPLE_RATE
        first = np.zeros(chunk_samples, dtype=np.float32)
        second = np.zeros(chunk_samples, dtype=np.float32)
        generated, calls, _ = self.generate(
            [
                self.result(text="保持。", sample_count=chunk_samples, generation_tokens=80),
                self.result(text="丢弃。", sample_count=chunk_samples, generation_tokens=4096),
                self.result(text="左。", sample_count=chunk_samples // 2, generation_tokens=90),
                self.result(text="右。", sample_count=chunk_samples // 2, generation_tokens=100),
            ],
            planned_chunks=[(first, 0.0), (second, 60.0)],
            audio_sample_count=2 * chunk_samples,
        )

        self.assertEqual(len(calls), 4)
        self.assertIs(calls[0]["audio"], first)
        self.assertEqual(generated["text"], "保持。 左。 右。")
        self.assertEqual(
            [
                (segment["initial_chunk_id"], segment["split_path"])
                for segment in generated["segments"]
            ],
            [(0, ""), (1, "L"), (1, "R")],
        )

    def test_recursively_splits_an_exhausted_child_depth_first(self) -> None:
        sample_count = 80 * mlx_worker.SAMPLE_RATE
        audio = np.zeros(sample_count, dtype=np.float32)
        generated, calls, _ = self.generate(
            [
                self.result(text="父。", sample_count=sample_count, generation_tokens=4096),
                self.result(text="左父。", sample_count=sample_count // 2, generation_tokens=4096),
                self.result(text="左左。", sample_count=sample_count // 4, generation_tokens=70),
                self.result(text="左右。", sample_count=sample_count // 4, generation_tokens=71),
                self.result(text="右。", sample_count=sample_count // 2, generation_tokens=72),
            ],
            planned_chunks=[(audio, 0.0)],
            audio_sample_count=sample_count,
        )

        self.assertEqual(len(calls), 5)
        self.assertEqual(
            [segment["split_path"] for segment in generated["segments"]],
            ["LL", "LR", "R"],
        )
        self.assertEqual(
            [event["split_path"] for event in generated["generation_plan"]["split_events"]],
            ["", "L"],
        )
        self.assertEqual(generated["generation_tokens"], 213)
        self.assertEqual(generated["attempt_generation_tokens"], 213 + 2 * 4096)

    def test_depth_four_splits_a_45_second_terminal_parent_into_legal_leaves(self) -> None:
        sample_count = 160 * mlx_worker.SAMPLE_RATE
        target_parent_samples = 45 * mlx_worker.SAMPLE_RATE + 2670
        target_left_samples = 20 * mlx_worker.SAMPLE_RATE
        cuts = iter(
            (
                120 * mlx_worker.SAMPLE_RATE,
                80 * mlx_worker.SAMPLE_RATE,
                target_parent_samples,
                target_left_samples,
            )
        )
        results = [
            self.result(text="root", sample_count=sample_count, generation_tokens=4096),
            self.result(
                text="L", sample_count=120 * mlx_worker.SAMPLE_RATE, generation_tokens=4096
            ),
            self.result(
                text="LL", sample_count=80 * mlx_worker.SAMPLE_RATE, generation_tokens=4096
            ),
            self.result(text="LLL", sample_count=target_parent_samples, generation_tokens=4096),
            self.result(text="左叶。", sample_count=target_left_samples, generation_tokens=70),
            self.result(
                text="右叶。",
                sample_count=target_parent_samples - target_left_samples,
                generation_tokens=71,
            ),
            self.result(
                text="LLR。",
                sample_count=80 * mlx_worker.SAMPLE_RATE - target_parent_samples,
                generation_tokens=72,
            ),
            self.result(
                text="LR。", sample_count=40 * mlx_worker.SAMPLE_RATE, generation_tokens=73
            ),
            self.result(text="R。", sample_count=40 * mlx_worker.SAMPLE_RATE, generation_tokens=74),
        ]

        with patch.object(
            mlx_worker,
            "select_adaptive_split_sample",
            side_effect=lambda _pcm, **_kwargs: (next(cuts), 0),
        ):
            generated, calls, _ = self.generate(
                results,
                planned_chunks=[(TokenBudgetTests.FakeAudio(sample_count), 0.0)],
                audio_sample_count=sample_count,
            )

        self.assertEqual(len(calls), 9)
        self.assertEqual(generated["adaptive_split_count"], 4)
        self.assertEqual(generated["final_leaf_chunk_count"], 5)
        self.assertEqual(generated["generation_call_count"], 9)
        self.assertEqual(
            [segment["split_path"] for segment in generated["segments"]],
            ["LLLL", "LLLR", "LLR", "LR", "R"],
        )
        target_event = generated["generation_plan"]["split_events"][-1]
        self.assertEqual(target_event["split_path"], "LLL")
        self.assertEqual(target_event["depth"], 3)
        self.assertEqual(target_event["parent_end_sample"], target_parent_samples)
        self.assertEqual(target_event["split_sample"], target_left_samples)
        self.assertEqual(
            (
                generated["segments"][0]["end_sample"] - generated["segments"][0]["start_sample"],
                generated["segments"][1]["end_sample"] - generated["segments"][1]["start_sample"],
            ),
            (20 * mlx_worker.SAMPLE_RATE, 25 * mlx_worker.SAMPLE_RATE + 2670),
        )

    def test_depth_limit_fails_closed_when_a_leaf_still_exhausts(self) -> None:
        sample_count = 240 * mlx_worker.SAMPLE_RATE
        cuts = iter(sample_count - offset * mlx_worker.SAMPLE_RATE for offset in (40, 80, 120, 160))
        results = [
            self.result(text="hit", sample_count=count, generation_tokens=4096)
            for count in (
                sample_count,
                200 * mlx_worker.SAMPLE_RATE,
                160 * mlx_worker.SAMPLE_RATE,
                120 * mlx_worker.SAMPLE_RATE,
                80 * mlx_worker.SAMPLE_RATE,
            )
        ]
        with (
            patch.object(
                mlx_worker,
                "select_adaptive_split_sample",
                side_effect=lambda _pcm, **_kwargs: (next(cuts), 0),
            ),
            self.assertRaisesRegex(ValueError, "adaptive depth limit"),
        ):
            self.generate(
                results,
                planned_chunks=[(TokenBudgetTests.FakeAudio(sample_count), 0.0)],
                audio_sample_count=sample_count,
            )

    def test_global_split_limit_fails_before_a_sixty_fifth_retry(self) -> None:
        chunk_samples = 40 * mlx_worker.SAMPLE_RATE
        planned_chunks = [
            (TokenBudgetTests.FakeAudio(chunk_samples), index * 40.0) for index in range(65)
        ]
        results: list[object] = []
        for _ in range(64):
            results.extend(
                [
                    self.result(text="父", sample_count=chunk_samples, generation_tokens=4096),
                    self.result(text="左", sample_count=chunk_samples // 2, generation_tokens=10),
                    self.result(text="右", sample_count=chunk_samples // 2, generation_tokens=10),
                ]
            )
        results.append(
            self.result(text="第65父", sample_count=chunk_samples, generation_tokens=4096)
        )
        with (
            patch.object(
                mlx_worker,
                "quantize_pcm_s16",
                side_effect=lambda audio: TokenBudgetTests.FakeAudio(len(audio)),
            ),
            patch.object(
                mlx_worker,
                "select_adaptive_split_sample",
                side_effect=lambda _pcm, *, parent_start_sample, parent_end_sample: (
                    (parent_start_sample + parent_end_sample) // 2,
                    0,
                ),
            ),
            self.assertRaisesRegex(ValueError, "split-count limit"),
        ):
            self.generate(
                results,
                planned_chunks=planned_chunks,
                audio_sample_count=65 * chunk_samples,
            )

    def test_rejects_invalid_runtime_generation_token_types_and_overrun(self) -> None:
        for value in (True, -1, 1.0, 4097):
            with (
                self.subTest(value=value),
                self.assertRaisesRegex(ValueError, "generation token accounting"),
            ):
                self.generate(
                    [self.result(text="异常。", sample_count=16_000, generation_tokens=value)],
                    planned_chunks=[(TokenBudgetTests.FakeAudio(16_000), 0.0)],
                    audio_sample_count=16_000,
                )

    def test_rejects_boolean_adaptive_temperature_before_generation(self) -> None:
        model_calls: list[None] = []

        class FakeModel:
            def generate(self, _audio: object, **_kwargs: object) -> object:
                model_calls.append(None)
                raise AssertionError("generation must not start")

        with self.assertRaisesRegex(ValueError, "requires temperature=0.0"):
            generate_mlx_planned_chunks(
                FakeModel(),
                [(TokenBudgetTests.FakeAudio(16_000), 0.0)],
                audio_sample_count=16_000,
                sample_rate=mlx_worker.SAMPLE_RATE,
                per_chunk_budget=4096,
                temperature=False,
                language="Chinese",
                verbose=False,
                clear_cache=lambda: None,
            )
        self.assertEqual(model_calls, [])

    def test_rejects_multiple_segments_from_one_public_generate_call(self) -> None:
        result = self.result(text="第一段。 第二段。", sample_count=16_000, generation_tokens=4096)
        result.segments.append(  # type: ignore[attr-defined]
            {"start": 0.5, "end": 1.0, "text": "第二段。"}
        )
        with self.assertRaisesRegex(ValueError, "exactly one segment"):
            self.generate(
                [result],
                planned_chunks=[(TokenBudgetTests.FakeAudio(16_000), 0.0)],
                audio_sample_count=16_000,
            )

    def test_rejects_split_plan_offset_or_chunk_coverage_mismatch(self) -> None:
        with self.assertRaisesRegex(ValueError, "sample count does not match"):
            self.generate(
                [
                    self.result(text="第一段。", sample_count=16_000, generation_tokens=80),
                    self.result(text="第二段。", sample_count=16_000, generation_tokens=90),
                ],
                planned_chunks=[
                    (TokenBudgetTests.FakeAudio(16_000), 0.0),
                    (TokenBudgetTests.FakeAudio(16_000), 1.1),
                ],
                audio_sample_count=32_000,
            )

    def test_prevalidates_the_entire_plan_before_model_generation(self) -> None:
        model_calls: list[None] = []

        class FakeModel:
            def generate(self, _audio: object, **_kwargs: object) -> object:
                model_calls.append(None)
                raise AssertionError("model generation must not start")

        with self.assertRaisesRegex(ValueError, "sample count does not match"):
            generate_mlx_planned_chunks(
                FakeModel(),
                [
                    (TokenBudgetTests.FakeAudio(16_000), 0.0),
                    (TokenBudgetTests.FakeAudio(16_000), 1.1),
                ],
                audio_sample_count=32_000,
                sample_rate=mlx_worker.SAMPLE_RATE,
                per_chunk_budget=4096,
                temperature=0.0,
                language="Chinese",
                verbose=False,
                clear_cache=lambda: None,
            )

        self.assertEqual(model_calls, [])

    def test_rejects_nested_result_that_does_not_cover_its_chunk(self) -> None:
        result = self.result(text="异常。", sample_count=16_000, generation_tokens=4096)
        result.segments[0]["end"] = 0.9  # type: ignore[attr-defined,index]
        with self.assertRaisesRegex(ValueError, "did not cover its planned audio"):
            self.generate(
                [result],
                planned_chunks=[(TokenBudgetTests.FakeAudio(16_000), 0.0)],
                audio_sample_count=16_000,
            )

    def test_preserves_a_one_sample_padded_tail_boundary(self) -> None:
        generated, _, _ = self.generate(
            [
                self.result(text="第一段。", sample_count=16_000, generation_tokens=80),
                self.result(text="尾。", sample_count=16_000, generation_tokens=20),
            ],
            planned_chunks=[
                (TokenBudgetTests.FakeAudio(16_000), 0.0),
                (TokenBudgetTests.FakeAudio(16_000), 1.0),
            ],
            audio_sample_count=16_001,
        )

        tail = generated["segments"][1]  # type: ignore[index]
        self.assertEqual(tail["start"], 1.0)
        self.assertEqual(tail["end"], 16_001 / 16_000)
        self.assertGreater(tail["end"], tail["start"])
        self.assertEqual(
            generated["pcm_s16le_sha256"],
            hashlib.sha256(np.zeros(16_001, dtype="<i2").tobytes()).hexdigest(),
        )


class MainPreciseTokenBudgetTests(unittest.TestCase):
    def test_pinned_mlx_dependency_generate_calls_the_splitter_again(self) -> None:
        try:
            mlx_audio_distribution = distribution("mlx-audio")
        except PackageNotFoundError:
            self.skipTest("mlx-audio is platform-specific and is not installed")
        self.assertEqual(mlx_audio_distribution.version, "0.4.7")
        source_path = mlx_audio_distribution.locate_file(
            "mlx_audio/stt/models/qwen3_asr/qwen3_asr.py"
        )
        module = ast.parse(source_path.read_text(encoding="utf-8"))
        generate_methods = [
            item
            for node in module.body
            if isinstance(node, ast.ClassDef) and node.name == "Qwen3ASRModel"
            for item in node.body
            if isinstance(item, ast.FunctionDef) and item.name == "generate"
        ]
        self.assertEqual(len(generate_methods), 1)
        splitter_calls = [
            node
            for node in ast.walk(generate_methods[0])
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "split_audio_into_chunks"
        ]
        self.assertEqual(len(splitter_calls), 1)

    def test_main_passes_and_persists_the_exact_split_plan_budget(self) -> None:
        class StopAfterRawWrite(Exception):
            pass

        boundary_samples = 240 * mlx_worker.SAMPLE_RATE
        audio = np.zeros(boundary_samples + 7, dtype=np.float32)
        model_calls: list[dict[str, object]] = []
        split_calls: list[dict[str, object]] = []
        captured_raw: dict[str, object] = {}
        first_chunk = audio[: 235 * mlx_worker.SAMPLE_RATE]
        second_chunk = audio[235 * mlx_worker.SAMPLE_RATE :]

        class FakeModel:
            def generate(self, _audio: object, **kwargs: object) -> object:
                # The dependency's public API still runs its splitter, but the
                # one-sample epsilon keeps this already-planned input whole.
                fake_splitter(
                    _audio,
                    sr=mlx_worker.SAMPLE_RATE,
                    chunk_duration=float(kwargs["chunk_duration"]),
                )
                model_calls.append(kwargs)
                index = len(model_calls) - 1
                text = ("第一段。", "第二段。")[index]
                return types.SimpleNamespace(
                    text=text,
                    segments=[
                        {
                            "start": 0.0,
                            "end": len(_audio) / mlx_worker.SAMPLE_RATE,  # type: ignore[arg-type]
                            "text": text,
                        }
                    ],
                    prompt_tokens=64,
                    generation_tokens=100 + index,
                )

        def fake_splitter(
            received_audio: object, *, sr: int, chunk_duration: float
        ) -> list[tuple[object, float]]:
            split_calls.append(
                {
                    "audio": received_audio,
                    "sr": sr,
                    "chunk_duration": chunk_duration,
                }
            )
            if received_audio is audio:
                return [(first_chunk, 0.0), (second_chunk, 235.0)]
            return [(received_audio, 0.0)]

        mlx_package = types.ModuleType("mlx")
        mlx_package.__path__ = []  # type: ignore[attr-defined]
        mlx_core = types.ModuleType("mlx.core")
        mlx_core.clear_cache = lambda: None  # type: ignore[attr-defined]
        mlx_package.core = mlx_core  # type: ignore[attr-defined]
        numpy_module = types.ModuleType("numpy")
        numpy_module.__dict__.update(np.__dict__)
        numpy_module.array = lambda value: value  # type: ignore[attr-defined]
        mlx_audio_package = types.ModuleType("mlx_audio")
        mlx_audio_package.__path__ = []  # type: ignore[attr-defined]
        stt_package = types.ModuleType("mlx_audio.stt")
        stt_package.__path__ = []  # type: ignore[attr-defined]
        stt_package.load = lambda _target: FakeModel()  # type: ignore[attr-defined]
        models_package = types.ModuleType("mlx_audio.stt.models")
        models_package.__path__ = []  # type: ignore[attr-defined]
        qwen_package = types.ModuleType("mlx_audio.stt.models.qwen3_asr")
        qwen_package.__path__ = []  # type: ignore[attr-defined]
        qwen_module = types.ModuleType("mlx_audio.stt.models.qwen3_asr.qwen3_asr")
        qwen_module.split_audio_into_chunks = fake_splitter  # type: ignore[attr-defined]
        utils_module = types.ModuleType("mlx_audio.stt.utils")
        utils_module.load_audio = lambda _path: audio  # type: ignore[attr-defined]
        fake_modules = {
            "mlx": mlx_package,
            "mlx.core": mlx_core,
            "numpy": numpy_module,
            "mlx_audio": mlx_audio_package,
            "mlx_audio.stt": stt_package,
            "mlx_audio.stt.models": models_package,
            "mlx_audio.stt.models.qwen3_asr": qwen_package,
            "mlx_audio.stt.models.qwen3_asr.qwen3_asr": qwen_module,
            "mlx_audio.stt.utils": utils_module,
        }

        def fake_identity(
            *, repository: str, requested_revision: str, local_path: Path
        ) -> dict[str, object]:
            self.assertIsInstance(local_path, Path)
            return {
                "schema_version": 1,
                "repository": repository,
                "requested_revision": requested_revision,
                "resolved_commit": requested_revision,
                "files_sha256": {
                    "config.json": "1" * 64,
                    "model.safetensors": "2" * 64,
                },
            }

        def capture_raw(_path: Path, document: dict[str, object]) -> None:
            captured_raw.update(document)
            raise StopAfterRawWrite

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            input_path = root / "source.m4a"
            input_path.write_bytes(b"fake-audio")
            args = argparse.Namespace(
                input=input_path,
                output=root / "raw.json",
                aligned_output=root / "aligned.json",
                model=mlx_worker.DEFAULT_MODEL,
                model_revision=None,
                model_path=root / "model",
                aligner=mlx_worker.DEFAULT_ALIGNER,
                aligner_revision=None,
                aligner_path=root / "aligner",
                language="Chinese",
                temperature=0.0,
                max_tokens=4096,
                chunk_duration=240.0,
                max_sentence_characters=160,
                verbose=False,
                retranscribe=False,
                realign=False,
            )
            with (
                patch.object(mlx_worker, "parse_args", return_value=args),
                patch.object(
                    mlx_worker,
                    "local_model_target",
                    side_effect=lambda _path, *, label, fallback: f"{label}:{fallback}",
                ),
                patch.object(mlx_worker, "build_model_identity", side_effect=fake_identity),
                patch.object(mlx_worker, "write_json_atomically", side_effect=capture_raw),
                patch.dict(sys.modules, fake_modules),
                self.assertRaises(StopAfterRawWrite),
            ):
                mlx_worker.main()

        self.assertEqual(len(split_calls), 3)
        self.assertIs(split_calls[0]["audio"], audio)
        self.assertIs(split_calls[1]["audio"], first_chunk)
        self.assertIs(split_calls[2]["audio"], second_chunk)
        self.assertTrue(all(call["sr"] == mlx_worker.SAMPLE_RATE for call in split_calls))
        self.assertEqual(split_calls[0]["chunk_duration"], 240.0)
        self.assertEqual(len(model_calls), 2)
        self.assertTrue(all(call["max_tokens"] == 4096 for call in model_calls))
        self.assertEqual(captured_raw["audio"]["sample_count"], len(audio))  # type: ignore[index]
        self.assertEqual(captured_raw["audio"]["duration_seconds"], 240.0)  # type: ignore[index]
        self.assertEqual(captured_raw["options"]["max_tokens_per_chunk"], 4096)  # type: ignore[index]
        self.assertEqual(captured_raw["options"]["planned_chunk_count"], 2)  # type: ignore[index]
        self.assertEqual(
            captured_raw["options"]["effective_total_token_budget"],  # type: ignore[index]
            8192,
        )
        self.assertEqual(
            captured_raw["options"]["token_budget_scope"],  # type: ignore[index]
            mlx_worker.MLX_ADAPTIVE_TOKEN_BUDGET_SCOPE,
        )
        self.assertEqual(captured_raw["options"]["final_leaf_chunk_count"], 2)  # type: ignore[index]
        self.assertEqual(captured_raw["options"]["adaptive_split_count"], 0)  # type: ignore[index]
        self.assertEqual(
            captured_raw["options"]["adaptive_min_leaf_samples"],  # type: ignore[index]
            20 * mlx_worker.SAMPLE_RATE,
        )
        self.assertEqual(
            [
                segment["generation_tokens"]
                for segment in captured_raw["segments"]  # type: ignore[union-attr]
            ],
            [100, 101],
        )
        self.assertEqual(captured_raw["performance"]["generation_tokens"], 201)  # type: ignore[index]
        self.assertEqual(
            captured_raw["performance"]["attempt_generation_tokens"],  # type: ignore[index]
            201,
        )
        self.assertEqual(captured_raw["performance"]["generation_call_count"], 2)  # type: ignore[index]
        self.assertEqual(
            captured_raw["generation_plan"]["initial_chunk_boundaries_samples"],  # type: ignore[index]
            [0, 235 * mlx_worker.SAMPLE_RATE, len(audio)],
        )
        self.assertEqual(captured_raw["generation_plan"]["split_events"], [])  # type: ignore[index]
        self.assertEqual(
            captured_raw["generation_plan"]["pcm_s16le_sha256"],  # type: ignore[index]
            hashlib.sha256(np.zeros(len(audio), dtype="<i2").tobytes()).hexdigest(),
        )


class MainLegacyLineageTests(unittest.TestCase):
    def write_chain(self, root: Path) -> tuple[argparse.Namespace, bytes, bytes]:
        input_path = root / "source.m4a"
        raw_path = root / "raw.json"
        aligned_path = root / "aligned.json"
        input_path.write_bytes(b"fake-audio")
        audio_sha256 = sha256_file(input_path)
        raw = {
            "schema_version": 1,
            "kind": "raw-asr",
            "engine": "mlx-audio",
            "model": mlx_worker.DEFAULT_MODEL,
            "language": "Chinese",
            "audio": {
                "duration_seconds": 2.0,
                "sample_rate_hz": 16000,
                "size_bytes": input_path.stat().st_size,
                "sha256": audio_sha256,
            },
            "options": {
                "temperature": 0.0,
                "max_tokens_per_chunk": 4096,
                "chunk_duration_seconds": 240.0,
            },
            "text": "测试。",
            "segments": [{"id": 0, "start": 0.0, "end": 2.0, "text": "测试。"}],
        }
        write_json_atomically(raw_path, raw)
        aligned = {
            "schema_version": 1,
            "kind": "aligned-asr",
            "language": "Chinese",
            "source": {
                "engine": "mlx-audio",
                "model": mlx_worker.DEFAULT_MODEL,
                "aligner": mlx_worker.DEFAULT_ALIGNER,
                "audio_sha256": audio_sha256,
                "raw_asr_sha256": sha256_file(raw_path),
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
        write_json_atomically(aligned_path, aligned)
        args = argparse.Namespace(
            input=input_path,
            output=raw_path,
            aligned_output=aligned_path,
            model=mlx_worker.DEFAULT_MODEL,
            model_revision=None,
            model_path=None,
            aligner=mlx_worker.DEFAULT_ALIGNER,
            aligner_revision=None,
            aligner_path=None,
            language="Chinese",
            temperature=0.0,
            max_tokens=4096,
            chunk_duration=240.0,
            max_sentence_characters=160,
            verbose=False,
            retranscribe=False,
            realign=False,
        )
        return args, raw_path.read_bytes(), aligned_path.read_bytes()

    def test_markerless_align_only_requires_retranscription(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            args, raw_bytes, aligned_bytes = self.write_chain(Path(directory))
            args.aligned_output.unlink()
            with (
                patch.object(mlx_worker, "parse_args", return_value=args),
                self.assertRaisesRegex(ValueError, "pass --retranscribe"),
            ):
                mlx_worker.main()
            self.assertEqual(args.output.read_bytes(), raw_bytes)
            self.assertFalse(args.aligned_output.exists())

            args.aligned_output.write_bytes(aligned_bytes)
            args.realign = True
            with (
                patch.object(mlx_worker, "parse_args", return_value=args),
                self.assertRaisesRegex(ValueError, "pass --retranscribe"),
            ):
                mlx_worker.main()
            self.assertEqual(args.output.read_bytes(), raw_bytes)
            self.assertEqual(args.aligned_output.read_bytes(), aligned_bytes)

    def test_complete_markerless_chain_remains_read_only(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            args, raw_bytes, aligned_bytes = self.write_chain(Path(directory))
            with (
                patch.object(mlx_worker, "parse_args", return_value=args),
                contextlib.redirect_stdout(io.StringIO()),
            ):
                self.assertEqual(mlx_worker.main(), 0)
            self.assertEqual(args.output.read_bytes(), raw_bytes)
            self.assertEqual(args.aligned_output.read_bytes(), aligned_bytes)


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
            "segments": [{"id": 0, "start": 0.0, "end": 2.0, "text": "测试。"}],
        }

    def mark_v2(self) -> None:
        revision = "a" * 40
        self.raw["lineage_schema_version"] = 2
        self.raw["model_identity"] = {
            "schema_version": 1,
            "repository": self.raw["model"],
            "requested_revision": revision,
            "resolved_commit": revision,
            "files_sha256": {
                "config.json": "b" * 64,
                "model.safetensors": "c" * 64,
            },
        }

    def validate_raw(self, *, adaptive_pcm_s16le_sha256: str | None = None) -> dict[str, object]:
        return validate_raw_document(
            self.raw,
            model="model-id",
            language="Chinese",
            temperature=0.0,
            max_tokens=4096,
            chunk_duration=240.0,
            audio_size_bytes=123,
            audio_sha256="audio-sha",
            adaptive_pcm_s16le_sha256=adaptive_pcm_s16le_sha256,
        )

    def configure_precise_v2(
        self, *, duration_seconds: float, segments: list[dict[str, object]]
    ) -> None:
        self.mark_v2()
        self.raw["audio"].update(
            {
                "duration_seconds": duration_seconds,
                "sample_count": round(duration_seconds * mlx_worker.SAMPLE_RATE),
            }
        )
        self.raw["options"].update(
            {
                "planned_chunk_count": len(segments),
                "effective_total_token_budget": 4096 * len(segments),
            }
        )
        self.raw["performance"] = {"generation_tokens": 1}
        self.raw["segments"] = segments

    def configure_per_chunk_v2(self) -> None:
        self.configure_precise_v2(
            duration_seconds=2.0,
            segments=[
                {
                    "id": 0,
                    "start": 0.0,
                    "end": 1.0,
                    "text": "第一段。",
                    "generation_tokens": 80,
                },
                {
                    "id": 1,
                    "start": 1.0,
                    "end": 2.0,
                    "text": "第二段。",
                    "generation_tokens": 90,
                },
            ],
        )
        self.raw["options"]["token_budget_scope"] = mlx_worker.MLX_PER_CHUNK_TOKEN_BUDGET_SCOPE
        self.raw["performance"] = {"generation_tokens": 170}
        self.raw["text"] = "第一段。 第二段。"

    def configure_adaptive_v2(self) -> None:
        self.mark_v2()
        sample_count = 60 * mlx_worker.SAMPLE_RATE
        split_sample = sample_count // 2
        self.raw["audio"].update({"duration_seconds": 60.0, "sample_count": sample_count})
        self.raw["options"].update(
            {
                "planned_chunk_count": 1,
                "final_leaf_chunk_count": 2,
                "adaptive_split_count": 1,
                "adaptive_split_algorithm": mlx_worker.MLX_ADAPTIVE_SPLIT_ALGORITHM,
                "adaptive_min_leaf_samples": mlx_worker.MLX_ADAPTIVE_MIN_LEAF_SAMPLES,
                "adaptive_max_depth": mlx_worker.MLX_ADAPTIVE_MAX_DEPTH,
                "adaptive_max_split_count": mlx_worker.MLX_ADAPTIVE_MAX_SPLIT_COUNT,
                "adaptive_energy_window_samples": (mlx_worker.MLX_ADAPTIVE_ENERGY_WINDOW_SAMPLES),
                "adaptive_quantization": mlx_worker.MLX_ADAPTIVE_QUANTIZATION,
                "adaptive_tie_break": mlx_worker.MLX_ADAPTIVE_TIE_BREAK,
                "effective_total_token_budget": 8192,
                "token_budget_scope": mlx_worker.MLX_ADAPTIVE_TOKEN_BUDGET_SCOPE,
            }
        )
        self.raw["performance"] = {
            "prompt_tokens": 128,
            "generation_tokens": 170,
            "attempt_prompt_tokens": 192,
            "attempt_generation_tokens": 4266,
            "generation_call_count": 3,
        }
        self.raw["text"] = "左叶。 右叶。"
        self.raw["segments"] = [
            {
                "id": 0,
                "initial_chunk_id": 0,
                "split_path": "L",
                "start_sample": 0,
                "end_sample": split_sample,
                "start": 0.0,
                "end": 30.0,
                "text": "左叶。",
                "generation_tokens": 80,
            },
            {
                "id": 1,
                "initial_chunk_id": 0,
                "split_path": "R",
                "start_sample": split_sample,
                "end_sample": sample_count,
                "start": 30.0,
                "end": 60.0,
                "text": "右叶。",
                "generation_tokens": 90,
            },
        ]
        self.raw["generation_plan"] = {
            "schema_version": 1,
            "pcm_s16le_sha256": "0" * 64,
            "initial_chunk_boundaries_samples": [0, sample_count],
            "split_events": [
                {
                    "initial_chunk_id": 0,
                    "split_path": "",
                    "depth": 0,
                    "parent_start_sample": 0,
                    "parent_end_sample": sample_count,
                    "legal_start_sample": mlx_worker.MLX_ADAPTIVE_MIN_LEAF_SAMPLES,
                    "legal_end_sample": (sample_count - mlx_worker.MLX_ADAPTIVE_MIN_LEAF_SAMPLES),
                    "split_sample": split_sample,
                    "cut_energy_sum_squares": 0,
                    "parent_prompt_tokens": 64,
                    "parent_generation_tokens": 4096,
                }
            ],
        }

    def test_markerless_mlx_accepts_missing_performance(self) -> None:
        self.assertIs(self.validate_raw(), self.raw)

    def test_v2_mlx_rejects_missing_performance(self) -> None:
        self.mark_v2()

        with self.assertRaisesRegex(ValueError, "invalid performance data"):
            self.validate_raw()

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

    def test_rejects_raw_that_exhausts_the_effective_token_budget(self) -> None:
        self.raw["performance"] = {"generation_tokens": 4096}

        with self.assertRaisesRegex(ValueError, "exhausted"):
            self.validate_raw()

    def test_accepts_precise_budget_above_a_rounded_chunk_boundary(self) -> None:
        self.mark_v2()
        self.raw["audio"].update(
            {
                "duration_seconds": 240.0,
                "sample_count": 240 * mlx_worker.SAMPLE_RATE + 7,
            }
        )
        self.raw["options"].update(
            {
                "planned_chunk_count": 2,
                "effective_total_token_budget": 8192,
            }
        )
        self.raw["performance"] = {"generation_tokens": 4096}
        self.raw["segments"] = [
            {"id": 0, "start": 0.0, "end": 235.0, "text": "第一段。"},
            {"id": 1, "start": 235.0, "end": 240.0, "text": "第二段。"},
        ]

        self.assertIs(self.validate_raw(), self.raw)

    def test_accepts_per_chunk_token_accounting(self) -> None:
        self.configure_per_chunk_v2()

        self.assertIs(self.validate_raw(), self.raw)

    def test_accepts_adaptive_split_tree_and_final_leaf_budget(self) -> None:
        self.configure_adaptive_v2()

        self.assertIs(self.validate_raw(adaptive_pcm_s16le_sha256="0" * 64), self.raw)

        with self.assertRaisesRegex(ValueError, "does not match generated PCM"):
            self.validate_raw(adaptive_pcm_s16le_sha256="1" * 64)

    def test_accepts_legacy_depth_three_adaptive_scope(self) -> None:
        self.configure_adaptive_v2()
        self.raw["options"].update(
            {
                "token_budget_scope": mlx_worker.MLX_LEGACY_ADAPTIVE_TOKEN_BUDGET_SCOPE,
                "adaptive_max_depth": mlx_worker.MLX_LEGACY_ADAPTIVE_MAX_DEPTH,
            }
        )

        self.assertIs(self.validate_raw(), self.raw)

    def test_rejects_adaptive_scope_depth_crossovers(self) -> None:
        cases = (
            (
                mlx_worker.MLX_ADAPTIVE_TOKEN_BUDGET_SCOPE,
                mlx_worker.MLX_LEGACY_ADAPTIVE_MAX_DEPTH,
            ),
            (
                mlx_worker.MLX_LEGACY_ADAPTIVE_TOKEN_BUDGET_SCOPE,
                mlx_worker.MLX_ADAPTIVE_MAX_DEPTH,
            ),
        )
        for scope, depth in cases:
            with self.subTest(scope=scope, depth=depth):
                self.configure_adaptive_v2()
                self.raw["options"].update(
                    {"token_budget_scope": scope, "adaptive_max_depth": depth}
                )
                with self.assertRaisesRegex(ValueError, "adaptive_max_depth mismatch"):
                    self.validate_raw()

    def test_rejects_adaptive_tree_or_cost_tampering(self) -> None:
        cases = (
            (
                "PCM commitment",
                lambda: self.raw["generation_plan"].update({"pcm_s16le_sha256": "G" * 64}),
            ),
            ("leaf sample", lambda: self.raw["segments"][1].update({"start_sample": 1})),
            (
                "split sample",
                lambda: self.raw["generation_plan"]["split_events"][0].update({"split_sample": 1}),
            ),
            (
                "parent token",
                lambda: self.raw["generation_plan"]["split_events"][0].update(
                    {"parent_generation_tokens": 4095}
                ),
            ),
            (
                "attempt tokens",
                lambda: self.raw["performance"].update({"attempt_generation_tokens": 170}),
            ),
            (
                "call count",
                lambda: self.raw["performance"].update({"generation_call_count": 2}),
            ),
        )
        for label, mutate in cases:
            with self.subTest(label=label):
                self.configure_adaptive_v2()
                mutate()
                with self.assertRaises(ValueError):
                    self.validate_raw()
                self.setUp()

    def test_accepts_exact_one_sample_final_ownership(self) -> None:
        self.configure_per_chunk_v2()
        self.raw["audio"].update({"duration_seconds": 1.0, "sample_count": 16_001})
        self.raw["segments"][0]["end"] = 1.0
        self.raw["segments"][1].update({"start": 1.0, "end": 16_001 / 16_000})

        self.assertIs(self.validate_raw(), self.raw)

    def test_rejects_per_chunk_budget_exhaustion(self) -> None:
        self.configure_per_chunk_v2()
        self.raw["segments"][1]["generation_tokens"] = 4096
        self.raw["performance"]["generation_tokens"] = 4176

        with self.assertRaisesRegex(ValueError, "segment 1 generation token"):
            self.validate_raw()

    def test_rejects_per_chunk_token_accounting_sum_mismatch(self) -> None:
        self.configure_per_chunk_v2()
        self.raw["performance"]["generation_tokens"] = 169

        with self.assertRaisesRegex(ValueError, "do not match performance"):
            self.validate_raw()

    def test_rejects_missing_per_chunk_token_accounting(self) -> None:
        self.configure_per_chunk_v2()
        del self.raw["segments"][1]["generation_tokens"]

        with self.assertRaisesRegex(ValueError, "segment 1 generation token"):
            self.validate_raw()

    def test_rejects_non_integer_or_negative_per_chunk_token_accounting(self) -> None:
        for value in (True, -1, 1.0):
            with self.subTest(value=value):
                self.configure_per_chunk_v2()
                self.raw["segments"][1]["generation_tokens"] = value
                with self.assertRaisesRegex(ValueError, "segment 1 generation token"):
                    self.validate_raw()
                self.setUp()

    def test_rejects_unknown_token_budget_scope(self) -> None:
        self.configure_per_chunk_v2()
        self.raw["options"]["token_budget_scope"] = "future-scope"

        with self.assertRaisesRegex(ValueError, "unsupported MLX token budget scope"):
            self.validate_raw()

    def test_rejects_per_chunk_scope_without_v2_lineage(self) -> None:
        self.configure_per_chunk_v2()
        del self.raw["lineage_schema_version"]
        del self.raw["model_identity"]

        with self.assertRaisesRegex(ValueError, "requires v2 lineage"):
            self.validate_raw()

    def test_rejects_per_chunk_text_merge_mismatch(self) -> None:
        self.configure_per_chunk_v2()
        self.raw["text"] = "被篡改的整集文本。"

        with self.assertRaisesRegex(ValueError, "does not match"):
            self.validate_raw()

    def test_rejects_exhaustion_against_the_recorded_precise_budget(self) -> None:
        self.mark_v2()
        self.raw["audio"]["sample_count"] = 2 * mlx_worker.SAMPLE_RATE
        self.raw["options"].update(
            {
                "planned_chunk_count": 1,
                "effective_total_token_budget": 4096,
            }
        )
        self.raw["performance"] = {"generation_tokens": 4096}

        with self.assertRaisesRegex(ValueError, "exhausted"):
            self.validate_raw()

    def test_rejects_inconsistent_precise_budget_metadata(self) -> None:
        self.mark_v2()
        self.raw["audio"]["sample_count"] = 2 * mlx_worker.SAMPLE_RATE
        self.raw["options"].update(
            {
                "planned_chunk_count": 2,
                "effective_total_token_budget": 8192,
            }
        )
        self.raw["performance"] = {"generation_tokens": 1}

        with self.assertRaisesRegex(ValueError, "segment count"):
            self.validate_raw()

    def test_rejects_mismatched_effective_total_token_budget(self) -> None:
        self.mark_v2()
        self.raw["audio"]["sample_count"] = 2 * mlx_worker.SAMPLE_RATE
        self.raw["options"].update(
            {
                "planned_chunk_count": 1,
                "effective_total_token_budget": 8192,
            }
        )
        self.raw["performance"] = {"generation_tokens": 1}

        with self.assertRaisesRegex(ValueError, "effective total"):
            self.validate_raw()

    def test_rejects_each_incomplete_precise_marker_set(self) -> None:
        fields = (
            ("audio", "sample_count"),
            ("options", "planned_chunk_count"),
            ("options", "effective_total_token_budget"),
        )
        for container, key in fields:
            with self.subTest(field=f"{container}.{key}"):
                self.configure_precise_v2(
                    duration_seconds=2.0,
                    segments=[
                        {
                            "id": 0,
                            "start": 0.0,
                            "end": 2.0,
                            "text": "测试。",
                        }
                    ],
                )
                del self.raw[container][key]  # type: ignore[index]
                with self.assertRaisesRegex(ValueError, "incomplete precise"):
                    self.validate_raw()
                self.setUp()

    def test_rejects_unbounded_raw_numbers_without_overflowing(self) -> None:
        cases = {
            "duration": ("audio", "duration_seconds", 10**1000, "audio duration"),
            "tiny-duration": ("audio", "duration_seconds", 5e-324, "audio duration"),
            "segment": ("segments", 0, 10**1000, "segment 0 start"),
        }
        for label, (container, key, value, message) in cases.items():
            with self.subTest(label=label):
                if container == "segments":
                    self.raw["segments"][key]["start"] = value  # type: ignore[index]
                else:
                    self.raw[container][key] = value  # type: ignore[index]
                with self.assertRaisesRegex(ValueError, message):
                    self.validate_raw()
                self.setUp()

    def test_rejects_unbounded_precise_sample_and_token_counts(self) -> None:
        cases = {
            "sample-count": ("audio", "sample_count", "sample count"),
            "effective-budget": (
                "options",
                "effective_total_token_budget",
                "effective total token budget",
            ),
            "generation-tokens": (
                "performance",
                "generation_tokens",
                "generation token accounting",
            ),
        }
        for label, (container, key, message) in cases.items():
            with self.subTest(label=label):
                self.configure_precise_v2(
                    duration_seconds=2.0,
                    segments=[
                        {
                            "id": 0,
                            "start": 0.0,
                            "end": 2.0,
                            "text": "测试。",
                        }
                    ],
                )
                self.raw[container][key] = 10**1000  # type: ignore[index]
                with self.assertRaisesRegex(ValueError, message):
                    self.validate_raw()
                self.setUp()

    def test_rejects_subnormal_chunk_duration_before_budget_math(self) -> None:
        self.raw["options"]["chunk_duration_seconds"] = 5e-324

        with self.assertRaisesRegex(ValueError, "requested chunk duration"):
            validate_raw_document(
                self.raw,
                model="model-id",
                language="Chinese",
                temperature=0.0,
                max_tokens=4096,
                chunk_duration=5e-324,
                audio_size_bytes=123,
                audio_sha256="audio-sha",
            )

    def test_rejects_raw_that_stops_before_the_audio_ends(self) -> None:
        self.raw["audio"]["duration_seconds"] = 480.0
        self.raw["segments"] = [
            {"id": 0, "start": 0.0, "end": 240.0, "text": "第一段。"},
        ]

        with self.assertRaisesRegex(ValueError, "through its end"):
            self.validate_raw()

    def test_rejects_raw_with_a_gap_between_chunks(self) -> None:
        self.raw["audio"]["duration_seconds"] = 480.0
        self.raw["segments"] = [
            {"id": 0, "start": 0.0, "end": 240.0, "text": "第一段。"},
            {"id": 1, "start": 241.0, "end": 480.0, "text": "第二段。"},
        ]

        with self.assertRaisesRegex(ValueError, "continuously cover"):
            self.validate_raw()

    def test_rejects_raw_that_does_not_start_at_zero(self) -> None:
        self.raw["segments"][0]["start"] = 0.5

        with self.assertRaisesRegex(ValueError, "continuously cover"):
            self.validate_raw()

    def test_v2_mlx_rejects_99ms_start_and_gap(self) -> None:
        cases = {
            "start": [
                {"id": 0, "start": 0.099, "end": 1.0, "text": "第一段。"},
                {"id": 1, "start": 1.0, "end": 2.0, "text": "第二段。"},
            ],
            "gap": [
                {"id": 0, "start": 0.0, "end": 1.0, "text": "第一段。"},
                {"id": 1, "start": 1.099, "end": 2.0, "text": "第二段。"},
            ],
        }
        for label, segments in cases.items():
            with self.subTest(label=label):
                self.configure_precise_v2(duration_seconds=2.0, segments=segments)
                with self.assertRaisesRegex(ValueError, "continuously cover"):
                    self.validate_raw()
                self.setUp()

    def test_v2_mlx_accepts_one_millisecond_boundary_rounding(self) -> None:
        self.configure_precise_v2(
            duration_seconds=2.0,
            segments=[
                {"id": 0, "start": 0.0, "end": 1.0, "text": "第一段。"},
                {"id": 1, "start": 1.001, "end": 2.0, "text": "第二段。"},
            ],
        )

        self.assertIs(self.validate_raw(), self.raw)

    def test_v2_mlx_rejects_cumulative_gaps_despite_compensating_overlap(
        self,
    ) -> None:
        self.configure_precise_v2(
            duration_seconds=5.0,
            segments=[
                {"id": 0, "start": 0.0, "end": 1.0, "text": "一。"},
                {"id": 1, "start": 1.001, "end": 2.0, "text": "二。"},
                {"id": 2, "start": 1.999, "end": 3.0, "text": "三。"},
                {"id": 3, "start": 3.001, "end": 4.0, "text": "四。"},
                {"id": 4, "start": 4.001, "end": 5.0, "text": "五。"},
            ],
        )

        with self.assertRaisesRegex(ValueError, "cumulative chunk-boundary gaps"):
            self.validate_raw()

    def test_v2_mlx_rejects_cumulative_overlaps_despite_compensating_gap(
        self,
    ) -> None:
        self.configure_precise_v2(
            duration_seconds=5.0,
            segments=[
                {"id": 0, "start": 0.0, "end": 1.0, "text": "一。"},
                {"id": 1, "start": 0.999, "end": 2.0, "text": "二。"},
                {"id": 2, "start": 2.001, "end": 3.0, "text": "三。"},
                {"id": 3, "start": 2.999, "end": 4.0, "text": "四。"},
                {"id": 4, "start": 3.999, "end": 5.0, "text": "五。"},
            ],
        )

        with self.assertRaisesRegex(ValueError, "cumulative chunk-boundary overlaps"):
            self.validate_raw()

    def test_markerless_mlx_retains_legacy_boundary_tolerance(self) -> None:
        self.raw["segments"][0]["start"] = 0.05

        self.assertIs(self.validate_raw(), self.raw)

    def test_v2_cuda_raw_defers_token_and_full_coverage_checks(self) -> None:
        self.raw["engine"] = "qwen-asr-transformers"
        self.raw["model"] = "cuda-model-id"
        self.mark_v2()
        self.raw["performance"] = {
            "transcription_seconds": 1.0,
            "cuda_peak_memory_bytes": 1024,
        }
        self.raw["segments"][0]["start"] = 0.5

        self.assertIs(
            validate_raw_document(
                self.raw,
                engine="qwen-asr-transformers",
                model="cuda-model-id",
                language="Chinese",
                temperature=0.0,
                max_tokens=4096,
                chunk_duration=240.0,
                audio_size_bytes=123,
                audio_sha256="audio-sha",
            ),
            self.raw,
        )

    def test_rejects_boolean_timestamp(self) -> None:
        with self.assertRaisesRegex(ValueError, "invalid timestamp"):
            finite_document_number(True, field="timestamp")

    def test_rejects_boolean_raw_segment_id(self) -> None:
        self.raw["segments"][0]["id"] = False

        with self.assertRaisesRegex(ValueError, "non-contiguous id"):
            self.validate_raw()

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
