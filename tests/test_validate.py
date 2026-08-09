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
    check_xiaoyuzhou_urls,
    transcript_structure,
    validate_core_point_logic_table,
    validate_episode_catalog_keyword,
    validate_episode_metadata_contract,
    validate_episode_navigation_title,
    validate_episode_translations,
    validate_participant_profiles,
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


def write_episode_contract_fixture(
    root: Path,
    *,
    folder: str,
    episode_key: str,
    episode_id: str | None = None,
    episode_key_scalar: str | None = None,
    published_at: str = '"2026-08-08T12:00:00+08:00"',
    duration_ms: str = "60000",
    workflow: dict[str, str] | None = None,
    source_preferences: tuple[str, ...] = ("true",),
    language: str = "zh-CN",
    transcript_path: str = "transcript.zh-CN.md",
    create_summary: bool = True,
    create_transcript: bool = True,
) -> Path:
    episode = root / "shows" / "example" / "episodes" / folder
    episode.mkdir(parents=True)
    resolved_workflow = workflow or {
        "metadata": "verified",
        "summary": "draft",
        "transcript": "machine",
    }
    sources = "".join(
        "  - platform: website\n"
        "    kind: episode\n"
        f"    url: https://example.com/{folder}/{index}\n"
        f"    preferred: {preferred}\n"
        for index, preferred in enumerate(source_preferences, start=1)
    )
    readme = episode / "README.md"
    readme.write_text(
        f"""---
id: "{episode_id or f'example:{episode_key}'}"
show_id: example
episode_key: {episode_key_scalar or json.dumps(episode_key)}
published_at: {published_at}
duration_ms: {duration_ms}
language: {language}
sources:
{sources}workflow:
  metadata: {resolved_workflow['metadata']}
  summary: {resolved_workflow['summary']}
  transcript: {resolved_workflow['transcript']}
summary:
  path: summary.zh-CN.md
transcript:
  path: {transcript_path}
  translations: []
---

# 测试单集
""",
        encoding="utf-8",
    )
    if create_summary:
        (episode / "summary.zh-CN.md").write_text("# 测试总结\n", encoding="utf-8")
    if create_transcript:
        (episode / transcript_path).write_text(
            "# 测试逐字稿\n\n[00:00:00] 测试。  \n",
            encoding="utf-8",
        )
    return readme


class QwenChainFixture:
    def __init__(
        self,
        root: Path,
        *,
        selection_status: str = "selected",
        transcript_language: str = "zh-CN",
    ) -> None:
        self.root = root
        self.episode = root / "shows" / "example" / "episodes" / "001"
        self.qwen = self.episode / "asr" / "qwen3-asr"
        self.raw_path = self.qwen / "raw.json"
        self.aligned_path = self.qwen / "aligned.json"
        self.refined_path = self.qwen / "refined.json"
        self.transcript_name = f"transcript.{transcript_language}.md"
        self.candidate_path = self.qwen / self.transcript_name
        self.root_transcript_path = self.episode / self.transcript_name
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
            "language": transcript_language,
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
            f"""---
schema_version: 1
kind: episode
id: "example:001"
transcript:
  path: {self.transcript_name}
asr_runs:
  - id: qwen3-asr-1.7b-8bit
    selection_status: {selection_status}
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/{self.transcript_name}
local_audio_cache:
  path: .cache/media/example/001/source.m4a
---

# 测试单集
""",
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


class EnglishTranslationFixture:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.episode = root / "shows" / "example" / "episodes" / "english"
        self.episode.mkdir(parents=True)
        self.source_path = self.episode / "transcript.en.md"
        self.translation_path = self.episode / "transcript.zh-CN.md"
        self.readme_path = self.episode / "README.md"
        self.source_path.write_text(
            "# Shared title\n\n"
            "[00:00:00] Hello.  \n"
            "[00:00:04] World.  \n",
            encoding="utf-8",
        )
        self.translation_path.write_text(
            "# Shared title\n\n"
            "[00:00:00] 你好。  \n"
            "[00:00:04] 世界。  \n",
            encoding="utf-8",
        )
        self.write_readme()

    def write_readme(
        self,
        *,
        include_translation: bool = True,
        episode_language: str = "en",
        metadata_overrides: dict[str, str] | None = None,
    ) -> None:
        metadata = {
            "language": "zh-CN",
            "path": "transcript.zh-CN.md",
            "source_language": "en",
            "source_path": "transcript.en.md",
            "alignment": "segment",
            "status": "machine",
            "generated_at": '"2026-08-07T12:00:00Z"',
            "source_sha256": sha256_bytes(self.source_path.read_bytes()),
            "sha256": sha256_bytes(self.translation_path.read_bytes()),
        }
        if metadata_overrides:
            metadata.update(metadata_overrides)
        translations = ""
        if include_translation:
            fields = list(metadata.items())
            first_key, first_value = fields[0]
            translations = f"  translations:\n    - {first_key}: {first_value}\n"
            translations += "".join(
                f"      {key}: {value}\n" for key, value in fields[1:]
            )
        self.readme_path.write_text(
            f"""---
schema_version: 1
kind: episode
id: example:english
language: {episode_language}
transcript:
  path: transcript.en.md
{translations}---

# Shared title
""",
            encoding="utf-8",
        )

    def validate(self) -> list[str]:
        errors: list[str] = []
        validate_episode_translations(
            self.episode,
            repository_root=self.root,
            readme_text=self.readme_path.read_text(encoding="utf-8"),
            errors=errors,
        )
        return errors


class QwenArtifactChainTests(unittest.TestCase):
    def test_accepts_complete_selected_chain_with_matching_cached_audio(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = QwenChainFixture(Path(directory))

            self.assertEqual(fixture.validate(), (True, []))

    def test_accepts_language_specific_qwen_transcript(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = QwenChainFixture(Path(directory), transcript_language="en")

            self.assertEqual(fixture.validate(), (True, []))

    def test_discovers_english_chain_before_readme_run_is_registered(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = QwenChainFixture(Path(directory), transcript_language="en")
            fixture.readme_path.write_text(
                """---
transcript:
  path: transcript.en.md
asr_runs: []
---
""",
                encoding="utf-8",
            )
            fixture.refined_path.write_text("{bad json\n", encoding="utf-8")

            complete, errors = fixture.validate()

            self.assertTrue(complete)
            self.assertTrue(any("refined.json is not strict JSON" in e for e in errors))

    def test_rejects_transcript_filename_language_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = QwenChainFixture(Path(directory), transcript_language="en")
            refined = json.loads(fixture.refined_path.read_text(encoding="utf-8"))
            refined["language"] = "zh-CN"
            write_json(fixture.refined_path, refined)

            _, errors = fixture.validate()

            self.assertTrue(any("refined.language must match" in e for e in errors))

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


class EnglishTranscriptTranslationTests(unittest.TestCase):
    def test_accepts_segment_aligned_chinese_translation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = EnglishTranslationFixture(Path(directory))

            self.assertEqual(fixture.validate(), [])

    def test_requires_translation_for_english_episode(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = EnglishTranslationFixture(Path(directory))
            fixture.write_readme(include_translation=False)

            errors = fixture.validate()

            self.assertIn(
                "English selected transcript requires exactly one zh-CN item in "
                "transcript.translations",
                errors,
            )

    def test_incomplete_workflow_still_validates_a_declared_translation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = EnglishTranslationFixture(Path(directory))
            fixture.source_path.unlink()
            errors: list[str] = []

            validate_episode_translations(
                fixture.episode,
                repository_root=fixture.root,
                readme_text=fixture.readme_path.read_text(encoding="utf-8"),
                errors=errors,
                require_complete=False,
            )

            self.assertTrue(
                any("selected English transcript is missing" in error for error in errors)
            )

    def test_english_selected_path_triggers_rule_even_if_episode_language_differs(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = EnglishTranslationFixture(Path(directory))
            fixture.write_readme(
                include_translation=False,
                episode_language="zh-CN",
            )

            errors = fixture.validate()

            self.assertTrue(
                any("requires exactly one zh-CN item" in error for error in errors)
            )

    def test_rejects_translation_title_and_segment_count_mismatches(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = EnglishTranslationFixture(Path(directory))
            fixture.translation_path.write_text(
                "# 不同标题\n\n[00:00:00] 合并后的译文。  \n",
                encoding="utf-8",
            )
            fixture.write_readme()

            errors = fixture.validate()

            self.assertIn(
                "transcript.en.md and transcript.zh-CN.md must have the same title",
                errors,
            )
            self.assertIn(
                "transcript.en.md and transcript.zh-CN.md must have the same "
                "number of segment lines",
                errors,
            )

    def test_rejects_per_segment_timestamp_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = EnglishTranslationFixture(Path(directory))
            fixture.translation_path.write_text(
                "# Shared title\n\n"
                "[00:00:00] 你好。  \n"
                "[00:00:05] 世界。  \n",
                encoding="utf-8",
            )
            fixture.write_readme()

            errors = fixture.validate()

            self.assertTrue(
                any(
                    "segment 2 timestamp [00:00:05] does not match "
                    "transcript.en.md [00:00:04]" in error
                    for error in errors
                )
            )

    def test_rejects_translation_hash_mismatches(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = EnglishTranslationFixture(Path(directory))
            fixture.write_readme(
                metadata_overrides={
                    "source_sha256": "0" * 64,
                    "sha256": "1" * 64,
                }
            )

            errors = fixture.validate()

            self.assertIn(
                "transcript.translations[0].source_sha256 does not match "
                "transcript.en.md",
                errors,
            )
            self.assertIn(
                "transcript.translations[0].sha256 does not match "
                "transcript.zh-CN.md",
                errors,
            )

    def test_rejects_invalid_translation_contract_values(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = EnglishTranslationFixture(Path(directory))
            fixture.write_readme(
                metadata_overrides={
                    "language": "zh",
                    "path": "translation.zh-CN.md",
                    "source_language": "zh-CN",
                    "source_path": "source.en.md",
                    "alignment": "paragraph",
                    "status": "draft",
                    "generated_at": '"2026-13-07T12:00:00Z"',
                }
            )

            errors = fixture.validate()

            self.assertIn(
                "transcript.translations[0].language must be 'zh-CN'", errors
            )
            self.assertTrue(
                any(
                    "transcript.translations[0].path must point to" in error
                    for error in errors
                )
            )
            self.assertIn(
                "transcript.translations[0].source_language must be 'en'", errors
            )
            self.assertTrue(
                any(
                    "transcript.translations[0].source_path must point to" in error
                    for error in errors
                )
            )
            self.assertIn(
                "transcript.translations[0].alignment must be 'segment'", errors
            )
            self.assertIn(
                "transcript.translations[0].status must be one of machine, "
                "edited, reviewed",
                errors,
            )
            self.assertIn(
                "transcript.translations[0].generated_at must be an RFC 3339 "
                "timestamp",
                errors,
            )

    def test_does_not_require_translation_for_non_english_episode(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            episode = root / "shows" / "example" / "episodes" / "chinese"
            errors: list[str] = []

            validate_episode_translations(
                episode,
                repository_root=root,
                readme_text="""---
language: zh-CN
transcript:
  path: transcript.zh-CN.md
  translations: []
---
""",
                errors=errors,
            )

            self.assertEqual(errors, [])


class EpisodeMetadataContractTests(unittest.TestCase):
    @staticmethod
    def validate(
        root: Path,
        readme: Path,
        episode_ids: dict[str, Path] | None = None,
    ) -> tuple[bool, list[str]]:
        errors: list[str] = []
        publishable = validate_episode_metadata_contract(
            readme,
            readme.read_text(encoding="utf-8"),
            repository_root=root,
            episode_ids=episode_ids if episode_ids is not None else {},
            errors=errors,
        )
        return publishable, errors

    def test_accepts_publishable_and_unfinished_workflow_states(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            episode_ids: dict[str, Path] = {}
            published = write_episode_contract_fixture(
                root,
                folder="001-published",
                episode_key="001",
            )
            unfinished = write_episode_contract_fixture(
                root,
                folder="002-unfinished",
                episode_key="002",
                workflow={
                    "metadata": "verified",
                    "summary": "outline",
                    "transcript": "not-started",
                },
                create_summary=False,
                create_transcript=False,
            )

            self.assertEqual(
                self.validate(root, published, episode_ids),
                (True, []),
            )
            self.assertEqual(
                self.validate(root, unfinished, episode_ids),
                (False, []),
            )

    def test_publishable_episode_requires_both_web_assets(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            readme = write_episode_contract_fixture(
                root,
                folder="001-missing-summary",
                episode_key="001",
                create_summary=False,
            )

            publishable, errors = self.validate(root, readme)

            self.assertTrue(publishable)
            self.assertTrue(any("summary.path is missing" in error for error in errors))

    def test_participant_profile_validation_is_part_of_metadata_contract(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            readme = write_episode_contract_fixture(
                root,
                folder="001-profile",
                episode_key="001-profile",
            )
            text = readme.read_text(encoding="utf-8").replace(
                "sources:\n",
                "participants:\n"
                "  - id: guest\n"
                "    profile:\n"
                "      headline: \"\"\n"
                "      checked_at: 2026-08-09\n"
                "sources:\n",
                1,
            )
            readme.write_text(text, encoding="utf-8")

            _, errors = self.validate(root, readme)

            self.assertTrue(
                any("profile.headline must be a non-empty string" in e for e in errors)
            )

    def test_unfinished_english_episode_may_lack_transcript_and_translation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            readme = write_episode_contract_fixture(
                root,
                folder="english-unfinished",
                episode_key="english-unfinished",
                language="en",
                transcript_path="transcript.en.md",
                workflow={
                    "metadata": "verified",
                    "summary": "outline",
                    "transcript": "not-started",
                },
                create_summary=False,
                create_transcript=False,
            )

            publishable, errors = self.validate(root, readme)
            validate_episode_translations(
                readme.parent,
                repository_root=root,
                readme_text=readme.read_text(encoding="utf-8"),
                errors=errors,
                require_complete=publishable,
            )

            self.assertFalse(publishable)
            self.assertEqual(errors, [])

    def test_rejects_invalid_metadata_and_source_preference_contracts(self) -> None:
        cases: list[tuple[str, dict[str, Any], str]] = [
            (
                "publication timestamp",
                {"published_at": '"2026-08-08"'},
                "published_at must be an RFC 3339 timestamp with offset",
            ),
            (
                "positive duration",
                {"duration_ms": "0"},
                "duration_ms must be a positive integer",
            ),
            (
                "stable id",
                {"episode_id": "example:other"},
                "id must equal 'example:001'",
            ),
            (
                "workflow enum",
                {
                    "workflow": {
                        "metadata": "verified",
                        "summary": "published",
                        "transcript": "machine",
                    }
                },
                "workflow.summary must be one of",
            ),
            (
                "one preferred source",
                {"source_preferences": ("true", "true")},
                "sources must contain exactly one preferred source",
            ),
            (
                "a preferred source is required",
                {"source_preferences": ()},
                "sources must contain exactly one preferred source",
            ),
            (
                "numeric key is a string",
                {"episode_key_scalar": "001"},
                "numeric episode_key must be a quoted YAML string",
            ),
            (
                "integer duration is not quoted",
                {"duration_ms": '"60000"'},
                "duration_ms must be a positive integer",
            ),
        ]

        for label, overrides, expected in cases:
            with self.subTest(label=label), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                readme = write_episode_contract_fixture(
                    root,
                    folder="001-invalid",
                    episode_key="001",
                    **overrides,
                )

                _, errors = self.validate(root, readme)

                self.assertTrue(
                    any(expected in error for error in errors),
                    f"expected {expected!r} in {errors!r}",
                )

    def test_rejects_duplicate_episode_ids(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            episode_ids: dict[str, Path] = {}
            first = write_episode_contract_fixture(
                root,
                folder="first",
                episode_key="001",
            )
            second = write_episode_contract_fixture(
                root,
                folder="second",
                episode_key="001",
            )

            self.assertEqual(self.validate(root, first, episode_ids), (True, []))
            _, errors = self.validate(root, second, episode_ids)

            self.assertTrue(any("duplicates episode id 'example:001'" in error for error in errors))

    def test_rejects_episode_asset_symlink_escape(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            readme = write_episode_contract_fixture(
                root,
                folder="001-symlink",
                episode_key="001",
                create_summary=False,
            )
            outside = root / "outside-summary.md"
            outside.write_text("# Outside\n", encoding="utf-8")
            try:
                (readme.parent / "summary.zh-CN.md").symlink_to(outside)
            except OSError as error:
                if getattr(error, "winerror", None) == 1314:
                    self.skipTest("Windows symlink creation requires extra privileges")
                raise

            _, errors = self.validate(root, readme)

            self.assertTrue(any("summary.path escapes the episode directory" in error for error in errors))

    def test_timestamp_contract_keeps_two_digit_hours_and_bounded_clock_fields(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            transcript = root / "transcript.zh-CN.md"
            transcript.write_text(
                "# 测试逐字稿\n\n[99:59:59] 合法边界。  \n",
                encoding="utf-8",
            )
            errors: list[str] = []

            transcript_structure(
                transcript,
                repository_root=root,
                field="transcript",
                errors=errors,
            )

            self.assertEqual(errors, [])

            for timestamp in ("100:00:00", "00:60:00", "00:00:60"):
                with self.subTest(timestamp=timestamp):
                    transcript.write_text(
                        f"# 测试逐字稿\n\n[{timestamp}] 非法时间戳。  \n",
                        encoding="utf-8",
                    )
                    invalid_errors: list[str] = []
                    transcript_structure(
                        transcript,
                        repository_root=root,
                        field="transcript",
                        errors=invalid_errors,
                    )
                    self.assertTrue(
                        any("one timestamped sentence" in error for error in invalid_errors)
                    )


class ParticipantProfileValidationTests(unittest.TestCase):
    @staticmethod
    def validate(front_matter: str) -> list[str]:
        errors: list[str] = []
        validate_participant_profiles(
            front_matter.splitlines(),
            field_prefix="episode",
            errors=errors,
        )
        return errors

    def test_accepts_absent_minimal_full_and_empty_list_profiles(self) -> None:
        errors = self.validate(
            """participants:
  - id: host
    name: Host
  - id: minimal-guest
    profile:
      headline: Researcher
      checked_at: 2026-08-09
  - id: full-guest
    profile:
      headline: Robotics researcher
      bio: Works on general-purpose robots.
      affiliations:
        - organization: Physical Intelligence
          title: Researcher
          status: current
        - organization: Example Lab
          status: former
      education:
        - institution: Example University
          credential: PhD
          field: Computer Science
      checked_at: 2024-02-29
  - id: empty-lists
    profile:
      headline: Founder
      affiliations: []
      education: []
      checked_at: 2026-08-09
"""
        )

        self.assertEqual(errors, [])

    def test_rejects_missing_and_empty_profile_scalars(self) -> None:
        errors = self.validate(
            """participants:
  - id: guest
    profile:
      headline: ""
      bio: null
      checked_at: 2026-02-30
"""
        )

        self.assertIn(
            "episode participants[0].profile.headline must be a non-empty string",
            errors,
        )
        self.assertIn(
            "episode participants[0].profile.bio must be a non-empty string when present",
            errors,
        )
        self.assertIn(
            "episode participants[0].profile.checked_at must be a valid YYYY-MM-DD date",
            errors,
        )

    def test_requires_profile_headline_and_checked_date(self) -> None:
        errors = self.validate(
            """participants:
  - id: guest
    profile:
      affiliations: []
"""
        )

        self.assertTrue(any("profile.headline" in error for error in errors))
        self.assertTrue(any("profile.checked_at" in error for error in errors))

    def test_rejects_non_list_profile_collections(self) -> None:
        errors = self.validate(
            """participants:
  - id: guest
    profile:
      headline: Researcher
      affiliations:
        organization: Example Lab
      education: {}
      checked_at: 2026-08-09
"""
        )

        self.assertEqual(
            sum("profile.affiliations must be a YAML list" in e for e in errors),
            1,
        )
        self.assertTrue(any("profile.education must be a YAML list" in e for e in errors))

    def test_rejects_invalid_affiliation_and_education_items(self) -> None:
        errors = self.validate(
            """participants:
  - id: guest
    profile:
      headline: Researcher
      affiliations:
        - organization: ""
          status: active
        - organization: Former Company
      education:
        - credential: PhD
        - institution: Example University
          field: ""
      checked_at: 2026-08-09
"""
        )

        self.assertTrue(any("affiliations[0].organization" in e for e in errors))
        self.assertTrue(any("affiliations[0].status must be one of" in e for e in errors))
        self.assertTrue(any("affiliations[1].status" in e for e in errors))
        self.assertTrue(any("education[0].institution" in e for e in errors))
        self.assertTrue(any("education[1].field" in e for e in errors))

    def test_rejects_profile_not_attached_to_participant_item(self) -> None:
        errors = self.validate(
            """participants:
    profile:
      headline: Researcher
      checked_at: 2026-08-09
"""
        )

        self.assertEqual(
            errors,
            ["episode profile must be attached to a participants list item"],
        )


class ExistingMarkdownValidationTests(unittest.TestCase):
    def test_core_point_logic_table_requires_semantic_columns_and_rows(self) -> None:
        path = (
            ROOT
            / "shows"
            / "example"
            / "episodes"
            / "001"
            / "summary.zh-CN.md"
        )

        valid_errors: list[str] = []
        validate_core_point_logic_table(
            path,
            """## 核心观点

| 产业层级 | 关键变化 | 工程含义 |
| --- | --- | --- |
| 需求周期 | AI 打开计算需求 | 应按真实负载校正产品 |
| 全球分工 | 供应前提发生变化 | 需要重建跨层能力 |
| 产品工程 | 原型不等于产品 | 可靠性依赖组织流程 |

### 1. 完整展开
""",
            valid_errors,
        )
        self.assertEqual(valid_errors, [])

        numeric_errors: list[str] = []
        validate_core_point_logic_table(
            path,
            """## 核心观点

| 序号 | 观点 |
| --- | --- |
| 01 | 第一条 |
| 02 | 第二条 |
| 03 | 第三条 |

### 1. 完整展开
""",
            numeric_errors,
        )
        self.assertTrue(any("decorative numbering" in error for error in numeric_errors))

        malformed_errors: list[str] = []
        validate_core_point_logic_table(
            path,
            """## 核心观点

| 问题 | 机制 | 边界 |
| --- | --- | --- |
| 一个问题 | 一个机制 |

### 1. 完整展开
""",
            malformed_errors,
        )
        self.assertTrue(any("at least 3 rows" in error for error in malformed_errors))
        self.assertTrue(any("match its named columns" in error for error in malformed_errors))

        missing_errors: list[str] = []
        validate_core_point_logic_table(path, "## 核心观点\n\n- 普通列表\n", missing_errors)
        self.assertTrue(any("must begin with a logic table" in error for error in missing_errors))

    def test_episode_catalog_keyword_is_required_and_bounded(self) -> None:
        path = ROOT / "shows" / "example" / "episodes" / "001" / "README.md"

        valid_errors: list[str] = []
        validate_episode_catalog_keyword(
            path,
            "---\ncatalog_keyword: \"SGLang\"\n---\n",
            valid_errors,
        )
        self.assertEqual(valid_errors, [])

        invalid_errors: list[str] = []
        validate_episode_catalog_keyword(
            path,
            "---\ncatalog_keyword: \"特别\"\n---\n",
            invalid_errors,
        )
        self.assertTrue(any("release labels" in error for error in invalid_errors))

        missing_errors: list[str] = []
        validate_episode_catalog_keyword(path, "---\ntitle: example\n---\n", missing_errors)
        self.assertTrue(any("missing catalog_keyword" in error for error in missing_errors))

        duplicate_errors: list[str] = []
        validate_episode_catalog_keyword(
            path,
            "---\nnavigation_title: \"盛颖 · SGLang 与开源\"\n"
            "catalog_keyword: \"盛颖\"\n---\n",
            duplicate_errors,
        )
        self.assertTrue(any("must not duplicate" in error for error in duplicate_errors))

    def test_episode_navigation_title_uses_person_topic_format(self) -> None:
        path = ROOT / "shows" / "example" / "episodes" / "001" / "README.md"

        valid_errors: list[str] = []
        validate_episode_navigation_title(
            path,
            "---\nnavigation_title: \"盛颖 · SGLang 与开源\"\n---\n",
            valid_errors,
        )
        self.assertEqual(valid_errors, [])

        invalid_errors: list[str] = []
        validate_episode_navigation_title(
            path,
            "---\nnavigation_title: \"#247 盛颖 - SGLang\"\n---\n",
            invalid_errors,
        )
        self.assertTrue(any("person · topic" in error for error in invalid_errors))
        self.assertTrue(any("release labels" in error for error in invalid_errors))

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

    def test_xiaoyuzhou_urls_require_canonical_public_pages(self) -> None:
        path = ROOT / "shows" / "example" / "README.md"
        errors: list[str] = []

        count = check_xiaoyuzhou_urls(
            path,
            "https://www.xiaoyuzhoufm.com/podcast/6697cbecf103d7b06d18488b/"
            "?utm_source=test",
            errors,
        )

        self.assertEqual(count, 1)
        self.assertTrue(
            any("non-canonical Xiaoyuzhou URL" in error for error in errors)
        )


if __name__ == "__main__":
    unittest.main()
