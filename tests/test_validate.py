from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate import (  # noqa: E402
    check_bilibili_urls,
    check_front_matter,
    validate_qwen_chain,
)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def write_json(path: Path, document: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(document, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


class QwenChainFixture:
    def __init__(self, root: Path, *, selection_status: str = "selected") -> None:
        self.root = root
        self.episode = root / "shows" / "example" / "episodes" / "001"
        self.qwen = self.episode / "asr" / "qwen3-asr"
        self.raw_path = self.qwen / "raw.json"
        self.aligned_path = self.qwen / "aligned.json"
        self.refined_path = self.qwen / "refined.json"
        self.candidate_path = self.qwen / "transcript.zh-CN.md"
        self.root_transcript_path = self.episode / "transcript.zh-CN.md"
        self.readme_path = self.episode / "README.md"
        self.audio_path = root / ".cache" / "media" / "example" / "001" / "source.m4a"

        audio = b"fixture-audio\x00\x01"
        audio_sha = sha256_bytes(audio)
        self.audio_path.parent.mkdir(parents=True, exist_ok=True)
        self.audio_path.write_bytes(audio)

        raw = {
            "schema_version": 1,
            "kind": "raw-asr",
            "audio": {
                "size_bytes": len(audio),
                "sha256": audio_sha,
            },
        }
        write_json(self.raw_path, raw)

        aligned = {
            "schema_version": 1,
            "kind": "aligned-asr",
            "source": {
                "raw_asr_path": self.raw_path.relative_to(root).as_posix(),
                "raw_asr_sha256": sha256_bytes(self.raw_path.read_bytes()),
                "audio_sha256": audio_sha,
            },
        }
        write_json(self.aligned_path, aligned)

        transcript = "# 测试逐字稿\n\n[00:00:00] 第一句。  \n"
        self.candidate_path.write_text(transcript, encoding="utf-8")
        self.root_transcript_path.write_text(transcript, encoding="utf-8")
        refined = {
            "schema_version": 1,
            "kind": "refined-asr",
            "source": {
                "input_asr_path": self.aligned_path.relative_to(root).as_posix(),
                "input_asr_sha256": sha256_bytes(self.aligned_path.read_bytes()),
            },
            "rendered_transcript": {
                "path": self.candidate_path.relative_to(root).as_posix(),
                "sha256": sha256_bytes(self.candidate_path.read_bytes()),
            },
            "statistics": {"rendered_lines": 1},
        }
        write_json(self.refined_path, refined)
        self.write_readme(selection_status)

    def write_readme(self, selection_status: str) -> None:
        self.readme_path.write_text(
            """---
schema_version: 1
kind: episode
id: "example:001"
transcript:
  path: transcript.zh-CN.md
asr_runs:
  - id: qwen3-asr-1.7b-8bit
    selection_status: %s
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/example/001/source.m4a
---

# 测试单集
"""
            % selection_status,
            encoding="utf-8",
        )

    def rewrite_aligned(self, mutate: Callable[[dict[str, Any]], None]) -> None:
        aligned = json.loads(self.aligned_path.read_text(encoding="utf-8"))
        mutate(aligned)
        write_json(self.aligned_path, aligned)
        refined = json.loads(self.refined_path.read_text(encoding="utf-8"))
        refined["source"]["input_asr_sha256"] = sha256_bytes(
            self.aligned_path.read_bytes()
        )
        write_json(self.refined_path, refined)

    def validate(self) -> tuple[bool, list[str]]:
        errors: list[str] = []
        complete = validate_qwen_chain(
            self.episode,
            repository_root=self.root,
            readme_text=self.readme_path.read_text(encoding="utf-8"),
            errors=errors,
        )
        return complete, errors


class QwenArtifactChainTests(unittest.TestCase):
    def test_accepts_complete_selected_chain_with_matching_cached_audio(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = QwenChainFixture(Path(directory))

            self.assertEqual(fixture.validate(), (True, []))

    def test_rejects_duplicate_json_keys(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = QwenChainFixture(Path(directory))
            fixture.raw_path.write_text(
                '{"audio":{"sha256":"%s"},"audio":{}}\n'
                % ("0" * 64),
                encoding="utf-8",
            )

            _, errors = fixture.validate()

            self.assertTrue(any("not strict JSON" in error for error in errors))
            self.assertTrue(any("duplicate object key 'audio'" in error for error in errors))

    def test_rejects_non_finite_json_numbers(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = QwenChainFixture(Path(directory))
            fixture.raw_path.write_text(
                '{"audio":{"sha256":"%s"},"score":NaN}\n' % ("0" * 64),
                encoding="utf-8",
            )

            _, errors = fixture.validate()

            self.assertTrue(any("not strict JSON" in error for error in errors))
            self.assertTrue(any("non-finite number NaN" in error for error in errors))

    def test_rejects_non_repository_and_incorrect_recorded_paths(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = QwenChainFixture(Path(directory))
            fixture.rewrite_aligned(
                lambda document: document["source"].__setitem__(
                    "raw_asr_path", "../raw.json"
                )
            )

            _, errors = fixture.validate()

            self.assertTrue(
                any(
                    "aligned.source.raw_asr_path must use a repository-relative"
                    in error
                    for error in errors
                )
            )

    def test_rejects_raw_to_aligned_and_aligned_to_refined_hash_mismatches(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = QwenChainFixture(Path(directory))
            fixture.rewrite_aligned(
                lambda document: document["source"].__setitem__(
                    "raw_asr_sha256", "0" * 64
                )
            )
            refined = json.loads(fixture.refined_path.read_text(encoding="utf-8"))
            refined["source"]["input_asr_sha256"] = "1" * 64
            write_json(fixture.refined_path, refined)

            _, errors = fixture.validate()

            self.assertIn(
                "aligned.source.raw_asr_sha256 does not match raw.json", errors
            )
            self.assertIn(
                "refined.source.input_asr_sha256 does not match aligned.json", errors
            )

    def test_rejects_rendered_transcript_hash_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = QwenChainFixture(Path(directory))
            refined = json.loads(fixture.refined_path.read_text(encoding="utf-8"))
            refined["rendered_transcript"]["sha256"] = "0" * 64
            write_json(fixture.refined_path, refined)

            _, errors = fixture.validate()

            self.assertIn(
                "refined.rendered_transcript.sha256 does not match "
                "transcript.zh-CN.md",
                errors,
            )

    def test_rejects_non_line_oriented_transcript(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = QwenChainFixture(Path(directory))
            fixture.candidate_path.write_text(
                "# 测试逐字稿\n\n没有时间戳或硬换行\n", encoding="utf-8"
            )
            refined = json.loads(fixture.refined_path.read_text(encoding="utf-8"))
            refined["rendered_transcript"]["sha256"] = sha256_bytes(
                fixture.candidate_path.read_bytes()
            )
            write_json(fixture.refined_path, refined)

            _, errors = fixture.validate()

            self.assertTrue(any("one timestamped sentence" in error for error in errors))

    def test_checks_root_bytes_only_when_qwen_is_selected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = QwenChainFixture(Path(directory), selection_status="candidate")
            fixture.root_transcript_path.write_text("旧逐字稿\n", encoding="utf-8")

            self.assertEqual(fixture.validate(), (True, []))

            fixture.write_readme("selected")
            _, errors = fixture.validate()
            self.assertIn(
                "selected Qwen root transcript is not byte-identical to "
                "asr/qwen3-asr/transcript.zh-CN.md",
                errors,
            )

    def test_cached_audio_is_optional_but_validated_when_present(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = QwenChainFixture(Path(directory))
            fixture.audio_path.unlink()
            self.assertEqual(fixture.validate(), (True, []))

            fixture.audio_path.write_bytes(b"different")
            _, errors = fixture.validate()
            self.assertIn("raw.audio.size_bytes does not match cached audio", errors)
            self.assertIn("raw.audio.sha256 does not match cached audio", errors)
            self.assertIn(
                "aligned.source.audio_sha256 does not match cached audio", errors
            )

    def test_skips_intentional_incomplete_checkpoint(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            episode = root / "shows" / "example" / "episodes" / "001"
            raw = episode / "asr" / "qwen3-asr" / "raw.json"
            write_json(raw, {"kind": "raw-asr"})
            errors: list[str] = []

            complete = validate_qwen_chain(
                episode,
                repository_root=root,
                readme_text="",
                errors=errors,
            )

            self.assertFalse(complete)
            self.assertEqual(errors, [])

    def test_rejects_incomplete_chain_marked_selected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            episode = root / "shows" / "example" / "episodes" / "001"
            raw = episode / "asr" / "qwen3-asr" / "raw.json"
            write_json(raw, {"kind": "raw-asr"})
            readme = """---
asr_runs:
  - id: qwen3-asr-1.7b-8bit
    selection_status: selected
---
"""
            errors: list[str] = []

            complete = validate_qwen_chain(
                episode,
                repository_root=root,
                readme_text=readme,
                errors=errors,
            )

            self.assertFalse(complete)
            self.assertEqual(len(errors), 1)
            self.assertIn("marks Qwen selected", errors[0])
            self.assertIn("aligned.json", errors[0])


class ExistingMarkdownValidationTests(unittest.TestCase):
    def test_front_matter_checks_remain_active(self) -> None:
        path = ROOT / "shows" / "example" / "README.md"
        errors: list[str] = []

        check_front_matter(path, "# 缺少元数据\n", errors)

        self.assertEqual(
            errors,
            ["shows/example/README.md must begin with YAML front matter"],
        )

    def test_bilibili_url_checks_remain_active(self) -> None:
        path = ROOT / "shows" / "example" / "README.md"
        errors: list[str] = []

        count = check_bilibili_urls(
            path,
            "https://www.bilibili.com/video/BV1abc123/?vd_source=tracker",
            errors,
        )

        self.assertEqual(count, 1)
        self.assertTrue(any("tracking parameter vd_source" in error for error in errors))
        self.assertTrue(any("non-canonical Bilibili URL" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
