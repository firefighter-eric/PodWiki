from __future__ import annotations

import argparse
import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import transcribe_audio  # noqa: E402


class WhisperOutputTests(unittest.TestCase):
    def arguments(self, *, input_path: Path, output_path: Path) -> argparse.Namespace:
        return argparse.Namespace(
            input=input_path,
            output=output_path,
            model=transcribe_audio.DEFAULT_MODEL,
            language="zh",
            temperature=0.0,
            clip_timestamps="0",
            initial_prompt=None,
            verbose=False,
        )

    def test_rejects_output_outside_cache_benchmarks_before_model_load(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            input_path = root / "source.m4a"
            input_path.write_bytes(b"audio")
            arguments = self.arguments(
                input_path=input_path,
                output_path=root / "tracked" / "raw.json",
            )
            with patch.object(
                transcribe_audio, "BENCHMARK_ROOT", root / ".cache" / "benchmarks"
            ), patch.object(
                transcribe_audio, "parse_args", return_value=arguments
            ), self.assertRaisesRegex(ValueError, r"\.cache/benchmarks"):
                transcribe_audio.main()

    def test_rejects_non_finite_model_result_without_creating_output(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            benchmark_root = root / ".cache" / "benchmarks"
            input_path = root / "source.m4a"
            output_path = benchmark_root / "show" / "episode" / "raw.json"
            input_path.write_bytes(b"audio")
            arguments = self.arguments(
                input_path=input_path,
                output_path=output_path,
            )
            fake_whisper = SimpleNamespace(
                transcribe=lambda *_args, **_kwargs: {
                    "language": "zh",
                    "text": "invalid",
                    "segments": [{"start": float("nan"), "text": "invalid"}],
                }
            )
            with patch.object(
                transcribe_audio, "BENCHMARK_ROOT", benchmark_root
            ), patch.object(
                transcribe_audio, "parse_args", return_value=arguments
            ), patch.dict(sys.modules, {"mlx_whisper": fake_whisper}), self.assertRaisesRegex(
                ValueError, "non-strict JSON"
            ):
                transcribe_audio.main()

            self.assertFalse(output_path.exists())

    def test_writes_strict_json_inside_benchmark_cache(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            benchmark_root = root / ".cache" / "benchmarks"
            input_path = root / "source.m4a"
            output_path = benchmark_root / "show" / "episode" / "raw.json"
            input_path.write_bytes(b"audio")
            arguments = self.arguments(
                input_path=input_path,
                output_path=output_path,
            )
            result = {
                "language": "zh",
                "text": "内容",
                "segments": [{"start": 0.0, "end": 1.0, "text": "内容"}],
            }
            fake_whisper = SimpleNamespace(
                transcribe=lambda *_args, **_kwargs: result
            )
            with patch.object(
                transcribe_audio, "BENCHMARK_ROOT", benchmark_root
            ), patch.object(
                transcribe_audio, "parse_args", return_value=arguments
            ), patch.dict(sys.modules, {"mlx_whisper": fake_whisper}), contextlib.redirect_stdout(
                io.StringIO()
            ):
                self.assertEqual(transcribe_audio.main(), 0)

            self.assertEqual(json.loads(output_path.read_text("utf-8")), result)
            self.assertNotIn(b"\r\n", output_path.read_bytes())

    def test_atomic_writer_preserves_existing_file_on_nan(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "raw.json"
            output.write_text('{"stable":true}\n', encoding="utf-8")
            with self.assertRaises(ValueError):
                transcribe_audio.write_json_atomically(
                    output,
                    {"value": float("nan")},
                )
            self.assertEqual(output.read_text("utf-8"), '{"stable":true}\n')
            self.assertEqual(list(output.parent.glob(".*.tmp")), [])

    def test_tracked_whisper_raw_artifacts_are_strict_json(self) -> None:
        paths = sorted(ROOT.glob("shows/*/episodes/*/asr/whisper/raw.json"))
        self.assertTrue(paths)

        def reject_constant(value: str) -> None:
            raise ValueError(f"non-finite JSON number: {value}")

        for path in paths:
            with self.subTest(path=path):
                document = json.loads(
                    path.read_text(encoding="utf-8"),
                    parse_constant=reject_constant,
                )
                self.assertIsInstance(document, dict)


if __name__ == "__main__":
    unittest.main()
