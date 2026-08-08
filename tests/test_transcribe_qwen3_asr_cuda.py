from __future__ import annotations

import argparse
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
        self.assertEqual(cuda_worker.MAX_INFERENCE_BATCH_SIZE, 1)

    def test_chunks_audio_without_crossing_requested_bound(self) -> None:
        self.assertEqual(
            list(cuda_worker.audio_chunk_ranges(250.0, chunk_duration=120.0)),
            [(0.0, 120.0), (120.0, 240.0), (240.0, 250.0)],
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
            args.chunk_duration = 181.0
            with self.assertRaisesRegex(ValueError, "at most 180"):
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
    ) -> int:
        with (
            patch.object(cuda_worker, "parse_args", return_value=args),
            patch.object(cuda_worker.shutil, "which", side_effect=lambda name: name),
            patch.object(cuda_worker, "probe_audio_duration", return_value=2.0),
            patch.object(cuda_worker, "decode_audio_chunk", return_value=FakeAudio()),
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


if __name__ == "__main__":
    unittest.main()
