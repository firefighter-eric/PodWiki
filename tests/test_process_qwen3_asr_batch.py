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

import process_qwen3_asr_batch as batch  # noqa: E402
from process_qwen3_asr_batch import (  # noqa: E402
    decode_front_matter_scalar,
    parse_json_output,
    read_episode_identity,
    repository_argument,
    resolve_backend_settings,
    run_logged,
    transcript_filename,
    validate_local_model_path,
)


class FrontMatterTests(unittest.TestCase):
    def test_decodes_json_quoted_and_plain_scalars(self) -> None:
        self.assertEqual(decode_front_matter_scalar('"张小珺：访谈"'), "张小珺：访谈")
        self.assertEqual(decode_front_matter_scalar("zhangxiaojun:145"), "zhangxiaojun:145")

    def test_reads_episode_id_and_title(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            episode = Path(directory)
            (episode / "README.md").write_text(
                "---\nid: \"show:001\"\ntitle: \"第一集：测试\"\n---\n\n# 标题\n",
                encoding="utf-8",
            )

            self.assertEqual(
                read_episode_identity(episode),
                ("show:001", "第一集：测试"),
            )


class OutputParsingTests(unittest.TestCase):
    def test_parses_structured_worker_output(self) -> None:
        self.assertEqual(
            parse_json_output('{"status":"skipped-valid","chunks":2}\n'),
            {"status": "skipped-valid", "chunks": 2},
        )

    def test_returns_empty_for_unstructured_failure_output(self) -> None:
        self.assertEqual(parse_json_output("Traceback: failed"), {})

    def test_worker_stderr_is_logged_without_corrupting_json_stdout(self) -> None:
        completed = SimpleNamespace(
            returncode=0,
            stdout='{"status":"completed","chunks":1}\n',
            stderr="third-party CUDA diagnostic\n",
        )
        with tempfile.TemporaryDirectory() as directory:
            log_path = Path(directory) / "worker.log"
            with patch.object(batch.subprocess, "run", return_value=completed):
                returned, parsed = run_logged(
                    command=["python", "worker.py"],
                    environment={},
                    log_path=log_path,
                )

            self.assertIs(returned, completed)
            self.assertEqual(parsed, {"status": "completed", "chunks": 1})
            self.assertIn("third-party CUDA diagnostic", log_path.read_text("utf-8"))


class PathTests(unittest.TestCase):
    def test_uses_language_tag_in_transcript_filename(self) -> None:
        self.assertEqual(transcript_filename("zh-CN"), "transcript.zh-CN.md")
        self.assertEqual(transcript_filename("en"), "transcript.en.md")
        with self.assertRaisesRegex(ValueError, "invalid transcript language"):
            transcript_filename("../en")

    def test_repository_argument_is_relative_inside_repository(self) -> None:
        path = ROOT / "shows" / "example" / "episodes" / "001"
        self.assertEqual(
            repository_argument(path),
            "shows/example/episodes/001",
        )

    def test_local_model_preflight_fails_before_episode_loop(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(FileNotFoundError, "has no config.json"):
                validate_local_model_path(Path(directory), label="model")


class BackendTests(unittest.TestCase):
    def test_preserves_mlx_defaults_and_selects_official_cuda_models(self) -> None:
        mlx = resolve_backend_settings(
            "mlx",
            model=None,
            aligner=None,
            max_tokens=None,
            chunk_duration=None,
        )
        cuda = resolve_backend_settings(
            "cuda",
            model=None,
            aligner=None,
            max_tokens=None,
            chunk_duration=None,
        )

        self.assertEqual(mlx.worker_name, "transcribe_qwen3_asr.py")
        self.assertEqual(mlx.engine, "mlx-audio")
        self.assertEqual(mlx.max_tokens, 4096)
        self.assertEqual(mlx.chunk_duration, 240.0)
        self.assertEqual(cuda.worker_name, "transcribe_qwen3_asr_cuda.py")
        self.assertEqual(cuda.engine, "qwen-asr-transformers")
        self.assertEqual(cuda.model, "Qwen/Qwen3-ASR-1.7B")
        self.assertEqual(cuda.aligner, "Qwen/Qwen3-ForcedAligner-0.6B")
        self.assertEqual(cuda.max_tokens, 2048)
        self.assertEqual(cuda.chunk_duration, 120.0)

    def test_cuda_batch_invokes_cuda_worker_and_renders_matching_engine(self) -> None:
        args = argparse.Namespace(
            backend="cuda",
            episode=None,
            model=None,
            model_path=None,
            aligner=None,
            aligner_path=None,
            language="Chinese",
            transcript_language="zh-CN",
            max_tokens=None,
            chunk_duration=None,
            max_sentence_characters=160,
            device="cuda:0",
            dtype="bfloat16",
            attention_implementation="sdpa",
            skip_render=False,
            retranscribe=False,
            realign=False,
        )
        episode = ROOT / "shows" / "fake-show" / "episodes" / "fake-episode"
        with tempfile.TemporaryDirectory() as directory:
            audio = Path(directory) / "source.m4a"
            audio.write_bytes(b"audio")
            commands: list[list[str]] = []

            def fake_run_logged(**kwargs: object) -> tuple[SimpleNamespace, dict[str, object]]:
                command = kwargs["command"]
                if not isinstance(command, list):
                    raise AssertionError("command must be a list")
                commands.append(command)
                if "render_asr_transcript.py" in command[1]:
                    return SimpleNamespace(returncode=0), {"rendered_lines": 1}
                return SimpleNamespace(returncode=0), {
                    "status": "transcribed-and-aligned",
                    "chunks": 1,
                    "sentence_segments": 1,
                }

            with (
                patch.object(batch, "parse_args", return_value=args),
                patch.object(batch, "discover_episode_dirs", return_value=[episode]),
                patch.object(batch, "read_episode_identity", return_value=("id", "title")),
                patch.object(batch, "cached_audio_path", return_value=audio),
                patch.object(batch, "run_logged", side_effect=fake_run_logged),
                contextlib.redirect_stdout(io.StringIO()),
            ):
                self.assertEqual(batch.main(), 0)

        self.assertEqual(len(commands), 2)
        transcribe, render = commands
        self.assertTrue(transcribe[1].endswith("transcribe_qwen3_asr_cuda.py"))
        self.assertIn("--device", transcribe)
        self.assertEqual(transcribe[transcribe.index("--device") + 1], "cuda:0")
        self.assertEqual(transcribe[transcribe.index("--dtype") + 1], "bfloat16")
        self.assertEqual(
            transcribe[transcribe.index("--model") + 1],
            "Qwen/Qwen3-ASR-1.7B",
        )
        self.assertEqual(
            render[render.index("--engine") + 1],
            "qwen-asr-transformers",
        )


if __name__ == "__main__":
    unittest.main()
