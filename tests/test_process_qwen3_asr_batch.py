from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from process_qwen3_asr_batch import (  # noqa: E402
    decode_front_matter_scalar,
    parse_json_output,
    read_episode_identity,
    repository_argument,
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


class PathTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
