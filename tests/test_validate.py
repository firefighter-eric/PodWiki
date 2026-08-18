from __future__ import annotations

import copy
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
    check_youtube_urls,
    check_xiaoyuzhou_urls,
    transcript_structure,
    validate_core_point_logic_table,
    validate_episode_catalog_keyword,
    validate_episode_metadata_contract,
    validate_episode_navigation_title,
    validate_episode_translations,
    validate_mlx_qwen_v2_raw_coverage,
    validate_participant_profiles,
    validate_qwen_chain,
    validate_summary_reader_contract,
    validate_show_metadata_contract,
    validate_source_schema,
    validate_wiki_indexes,
)


MLX_QWEN_MODEL = "mlx-community/Qwen3-ASR-1.7B-8bit"
MLX_QWEN_MODEL_REVISION = "a8379a2e2f9e313c9292cdf1af4055ab56d50d55"
MLX_QWEN_ALIGNER = "mlx-community/Qwen3-ForcedAligner-0.6B-8bit"
MLX_QWEN_ALIGNER_REVISION = "0e1a68e91d815300c7c9754b2a7639378b23db15"
CUDA_QWEN_MODEL = "Qwen/Qwen3-ASR-1.7B-hf"
CUDA_QWEN_MODEL_REVISION = "bcd2b5b7f32b480ab5790554cfa8347f246a14f3"
CUDA_QWEN_ALIGNER = "Qwen/Qwen3-ForcedAligner-0.6B-hf"
CUDA_QWEN_ALIGNER_REVISION = "c07281df297b9905d24a508279258cccf987a064"


def cuda_native_options() -> dict[str, str]:
    return {
        "backend": "transformers-native",
        "transformers_version": "5.14.1",
        "torch_version": "2.13.0",
    }


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
    summary_text = "# 测试总结\n"
    transcript_text = "# 测试逐字稿\n\n[00:00:00] 测试。  \n"
    if create_summary:
        (episode / "summary.zh-CN.md").write_text(summary_text, encoding="utf-8")
    if create_transcript:
        (episode / transcript_path).write_text(transcript_text, encoding="utf-8")
    transcript_sha = sha256_bytes(transcript_text.encode())
    readme = episode / "README.md"
    readme.write_text(
        f"""---
schema_version: 1
kind: episode
id: "{episode_id or f"example:{episode_key}"}"
show_id: example
episode_key: {episode_key_scalar or json.dumps(episode_key)}
episode_number: null
slug: {folder}
release_type: regular
numbering:
  status: unknown
  checked_at: 2026-08-08
  source: test-fixture
title: 测试单集
navigation_title: "测试嘉宾 · 测试主题"
published_at: {published_at}
duration_ms: {duration_ms}
language: {language}
participants:
  - id: test-guest
    name: 测试嘉宾
    aliases: []
    role: guest
sources:
{sources}workflow:
  metadata: {resolved_workflow["metadata"]}
  summary: {resolved_workflow["summary"]}
  transcript: {resolved_workflow["transcript"]}
summary:
  path: summary.zh-CN.md
  source_transcript:
    path: {transcript_path}
    engine: fixture-engine
    model: fixture-model
    selection_status: selected
    sha256: {transcript_sha}
transcript:
  path: {transcript_path}
  acquisition_method: audio-asr
  engine: fixture-engine
  model: fixture-model
  translations: []
asr_runs:
  - id: fixture-run
    selection_status: selected
    engine: fixture-engine
    model: fixture-model
    artifacts:
      raw: asr/fixture/raw.json
      refined: asr/fixture/refined.json
      transcript: asr/fixture/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/example/{folder}/source.m4a
  metadata_path: .cache/media/example/{folder}/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-08T12:00:00Z"
  verified_at: "2026-08-08T12:00:00Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 100
  duration_ms: {duration_ms}
  sha256: "{"0" * 64}"
---

# 测试单集
""",
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
        refined["source"]["input_asr_sha256"] = sha256_bytes(self.aligned_path.read_bytes())
        write_json(self.refined_path, refined)

    def rewrite_raw(self, mutate: Callable[[dict[str, Any]], None]) -> None:
        raw = json.loads(self.raw_path.read_text(encoding="utf-8"))
        mutate(raw)
        write_json(self.raw_path, raw)
        self.rewrite_aligned(
            lambda document: document["source"].__setitem__(
                "raw_asr_sha256", sha256_bytes(self.raw_path.read_bytes())
            )
        )

    def upgrade_to_v2(
        self,
        *,
        engine: str = "mlx-audio",
        model: str = MLX_QWEN_MODEL,
        model_revision: str = MLX_QWEN_MODEL_REVISION,
        aligner: str = MLX_QWEN_ALIGNER,
        aligner_revision: str = MLX_QWEN_ALIGNER_REVISION,
        raw_options: dict[str, Any] | None = None,
        aligned_options: dict[str, Any] | None = None,
    ) -> None:
        model_identity = {
            "schema_version": 1,
            "repository": model,
            "requested_revision": model_revision,
            "resolved_commit": model_revision,
            "files_sha256": {
                "config.json": "1" * 64,
                "model.safetensors": "2" * 64,
            },
        }
        aligner_identity = {
            "schema_version": 1,
            "repository": aligner,
            "requested_revision": aligner_revision,
            "resolved_commit": aligner_revision,
            "files_sha256": {
                "config.json": "3" * 64,
                "model.safetensors": "4" * 64,
            },
        }
        raw = json.loads(self.raw_path.read_text(encoding="utf-8"))
        raw.update(
            {
                "lineage_schema_version": 2,
                "engine": engine,
                "model": model,
                "model_identity": copy.deepcopy(model_identity),
            }
        )
        if engine == "mlx-audio":
            raw["audio"]["duration_seconds"] = 480.0
            raw["options"] = {
                "temperature": 0.0,
                "max_tokens_per_chunk": 4096,
                "chunk_duration_seconds": 240.0,
            }
            raw["performance"] = {"generation_tokens": 4096}
            raw["text"] = "第一段。第二段。"
            raw["segments"] = [
                {"id": 0, "start": 0.0, "end": 240.0, "text": "第一段。"},
                {"id": 1, "start": 240.0, "end": 480.0, "text": "第二段。"},
            ]
        if raw_options is not None:
            raw["options"] = copy.deepcopy(raw_options)
        write_json(self.raw_path, raw)
        aligned = json.loads(self.aligned_path.read_text(encoding="utf-8"))
        aligned["lineage_schema_version"] = 2
        aligned["source"].update(
            {
                "raw_asr_sha256": sha256_bytes(self.raw_path.read_bytes()),
                "engine": engine,
                "model": model,
                "aligner": aligner,
                "model_identity": copy.deepcopy(model_identity),
                "aligner_identity": copy.deepcopy(aligner_identity),
            }
        )
        if aligned_options is not None:
            aligned["options"] = copy.deepcopy(aligned_options)
        write_json(self.aligned_path, aligned)
        refined = json.loads(self.refined_path.read_text(encoding="utf-8"))
        refined["lineage_schema_version"] = 2
        refined["source"].update(
            {
                "input_asr_sha256": sha256_bytes(self.aligned_path.read_bytes()),
                "engine": engine,
                "model": model,
                "aligner": aligner,
                "model_identity": copy.deepcopy(model_identity),
                "aligner_identity": copy.deepcopy(aligner_identity),
            }
        )
        write_json(self.refined_path, refined)
        readme = self.readme_path.read_text(encoding="utf-8")
        readme = readme.replace(
            "    model: mlx-community/Qwen3-ASR-1.7B-8bit\n",
            f"    engine: {engine}\n    model: {model}\n    aligner: {aligner}\n",
        )
        self.readme_path.write_text(readme, encoding="utf-8")

    def configure_web_ready_qwen_provenance(self, *, precise_budget: bool) -> None:
        canonical_generated_at = "2026-08-09T12:02:00Z"

        def update_raw(document: dict[str, Any]) -> None:
            document["generated_at"] = "2026-08-09T12:00:00Z"
            if precise_budget:
                document["audio"].update(
                    {
                        "sample_count": 480 * 16000,
                        "sample_rate_hz": 16000,
                    }
                )
                document["options"].update(
                    {
                        "planned_chunk_count": 2,
                        "effective_total_token_budget": 8192,
                    }
                )

        self.rewrite_raw(update_raw)
        refined = json.loads(self.refined_path.read_text(encoding="utf-8"))
        refined["generated_at"] = canonical_generated_at
        write_json(self.refined_path, refined)

        readme = self.readme_path.read_text(encoding="utf-8")
        options = ""
        if precise_budget:
            options = (
                "  options:\n    planned_chunk_count: 2\n    effective_total_token_budget: 8192\n"
            )
        readme = readme.replace(
            f"transcript:\n  path: {self.transcript_name}\n",
            "workflow:\n"
            "  metadata: verified\n"
            "  summary: draft\n"
            "  transcript: machine\n"
            "transcript:\n"
            f"  path: {self.transcript_name}\n"
            f'  generated_at: "{canonical_generated_at}"\n'
            f"{options}",
        )
        aligner = "    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit\n"
        if aligner in readme:
            readme = readme.replace(
                aligner,
                aligner + f'    generated_at: "{canonical_generated_at}"\n',
            )
        else:
            model = "    model: mlx-community/Qwen3-ASR-1.7B-8bit\n"
            readme = readme.replace(
                model,
                model + f'    generated_at: "{canonical_generated_at}"\n',
            )
        self.readme_path.write_text(readme, encoding="utf-8")

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
            "# Shared title\n\n[00:00:00] Hello.  \n[00:00:04] World.  \n",
            encoding="utf-8",
        )
        self.translation_path.write_text(
            "# Shared title\n\n[00:00:00] 你好。  \n[00:00:04] 世界。  \n",
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
            translations += "".join(f"      {key}: {value}\n" for key, value in fields[1:])
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
    @staticmethod
    def precise_boundary_raw(*, generation_tokens: int = 4096) -> dict[str, Any]:
        return {
            "audio": {
                "duration_seconds": 240.0,
                "sample_count": 240 * 16000 + 7,
                "sample_rate_hz": 16000,
            },
            "options": {
                "max_tokens_per_chunk": 4096,
                "chunk_duration_seconds": 240.0,
                "planned_chunk_count": 2,
                "effective_total_token_budget": 8192,
            },
            "performance": {"generation_tokens": generation_tokens},
            "segments": [
                {"id": 0, "start": 0.0, "end": 235.0, "text": "第一段。"},
                {"id": 1, "start": 235.0, "end": 240.0, "text": "第二段。"},
            ],
        }

    @classmethod
    def per_chunk_boundary_raw(cls) -> dict[str, Any]:
        raw = cls.precise_boundary_raw(generation_tokens=170)
        raw["lineage_schema_version"] = 2
        raw["options"]["token_budget_scope"] = "per-planned-chunk-v1"
        raw["segments"][0]["generation_tokens"] = 80
        raw["segments"][1]["generation_tokens"] = 90
        raw["text"] = "第一段。 第二段。"
        return raw

    @staticmethod
    def adaptive_boundary_raw(*, split: bool) -> dict[str, Any]:
        sample_count = 60 * 16_000
        split_sample = 30 * 16_000
        generation_tokens = 170 if split else 80
        split_count = 1 if split else 0
        segments = (
            [
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
            if split
            else [
                {
                    "id": 0,
                    "initial_chunk_id": 0,
                    "split_path": "",
                    "start_sample": 0,
                    "end_sample": sample_count,
                    "start": 0.0,
                    "end": 60.0,
                    "text": "完整叶。",
                    "generation_tokens": 80,
                }
            ]
        )
        split_events = (
            [
                {
                    "initial_chunk_id": 0,
                    "split_path": "",
                    "depth": 0,
                    "parent_start_sample": 0,
                    "parent_end_sample": sample_count,
                    "legal_start_sample": 20 * 16_000,
                    "legal_end_sample": 40 * 16_000,
                    "split_sample": split_sample,
                    "cut_energy_sum_squares": 123,
                    "parent_prompt_tokens": 20,
                    "parent_generation_tokens": 4096,
                }
            ]
            if split
            else []
        )
        final_leaf_count = len(segments)
        return {
            "lineage_schema_version": 2,
            "audio": {
                "duration_seconds": 60.0,
                "sample_count": sample_count,
                "sample_rate_hz": 16_000,
            },
            "options": {
                "max_tokens_per_chunk": 4096,
                "chunk_duration_seconds": 60.0,
                "planned_chunk_count": 1,
                "effective_total_token_budget": 4096 * final_leaf_count,
                "token_budget_scope": "adaptive-bisect-per-leaf-v1",
                "temperature": 0.0,
                "adaptive_split_algorithm": "adaptive-low-energy-bisect-v1",
                "adaptive_min_leaf_samples": 20 * 16_000,
                "adaptive_max_depth": 3,
                "adaptive_max_split_count": 64,
                "adaptive_energy_window_samples": 1600,
                "adaptive_quantization": "pcm-s16-round-half-away-v1",
                "adaptive_tie_break": "energy-center-left-v1",
                "final_leaf_chunk_count": final_leaf_count,
                "adaptive_split_count": split_count,
            },
            "performance": {
                "prompt_tokens": 20,
                "generation_tokens": generation_tokens,
                "attempt_prompt_tokens": 40 if split else 20,
                "attempt_generation_tokens": generation_tokens + split_count * 4096,
                "generation_call_count": 1 + 2 * split_count,
            },
            "generation_plan": {
                "schema_version": 1,
                "pcm_s16le_sha256": "0" * 64,
                "initial_chunk_boundaries_samples": [0, sample_count],
                "split_events": split_events,
            },
            "segments": segments,
            "text": " ".join(segment["text"] for segment in segments),
        }

    @staticmethod
    def adaptive_depth_four_raw() -> dict[str, Any]:
        sample_rate = 16_000
        sample_count = 160 * sample_rate
        target_parent_end = 45 * sample_rate + 2670
        cuts = (120 * sample_rate, 80 * sample_rate, target_parent_end, 20 * sample_rate)
        leaves = (
            ("LLLL", 0, cuts[3], "左叶。", 10),
            ("LLLR", cuts[3], cuts[2], "右叶。", 11),
            ("LLR", cuts[2], cuts[1], "三。", 12),
            ("LR", cuts[1], cuts[0], "四。", 13),
            ("R", cuts[0], sample_count, "五。", 14),
        )
        segments = [
            {
                "id": index,
                "initial_chunk_id": 0,
                "split_path": path,
                "start_sample": start,
                "end_sample": end,
                "start": start / sample_rate,
                "end": end / sample_rate,
                "text": text,
                "generation_tokens": tokens,
            }
            for index, (path, start, end, text, tokens) in enumerate(leaves)
        ]
        parent_ends = (sample_count, cuts[0], cuts[1], cuts[2])
        split_paths = ("", "L", "LL", "LLL")
        split_events = [
            {
                "initial_chunk_id": 0,
                "split_path": path,
                "depth": depth,
                "parent_start_sample": 0,
                "parent_end_sample": parent_end,
                "legal_start_sample": 20 * sample_rate,
                "legal_end_sample": parent_end - 20 * sample_rate,
                "split_sample": cuts[depth],
                "cut_energy_sum_squares": 0,
                "parent_prompt_tokens": 20,
                "parent_generation_tokens": 4096,
            }
            for depth, (path, parent_end) in enumerate(zip(split_paths, parent_ends))
        ]
        generation_tokens = sum(segment["generation_tokens"] for segment in segments)
        prompt_tokens = 20 * len(segments)
        split_count = len(split_events)
        return {
            "lineage_schema_version": 2,
            "audio": {
                "duration_seconds": 160.0,
                "sample_count": sample_count,
                "sample_rate_hz": sample_rate,
            },
            "options": {
                "max_tokens_per_chunk": 4096,
                "chunk_duration_seconds": 240.0,
                "planned_chunk_count": 1,
                "effective_total_token_budget": 4096 * len(segments),
                "token_budget_scope": "adaptive-bisect-per-leaf-v2",
                "temperature": 0.0,
                "adaptive_split_algorithm": "adaptive-low-energy-bisect-v1",
                "adaptive_min_leaf_samples": 20 * sample_rate,
                "adaptive_max_depth": 4,
                "adaptive_max_split_count": 64,
                "adaptive_energy_window_samples": 1600,
                "adaptive_quantization": "pcm-s16-round-half-away-v1",
                "adaptive_tie_break": "energy-center-left-v1",
                "final_leaf_chunk_count": len(segments),
                "adaptive_split_count": split_count,
            },
            "performance": {
                "prompt_tokens": prompt_tokens,
                "generation_tokens": generation_tokens,
                "attempt_prompt_tokens": prompt_tokens + 20 * split_count,
                "attempt_generation_tokens": generation_tokens + 4096 * split_count,
                "generation_call_count": 1 + 2 * split_count,
            },
            "generation_plan": {
                "schema_version": 1,
                "pcm_s16le_sha256": "0" * 64,
                "initial_chunk_boundaries_samples": [0, sample_count],
                "split_events": split_events,
            },
            "segments": segments,
            "text": " ".join(segment["text"] for segment in segments),
        }

    def test_central_validator_accepts_precise_rounded_boundary_budget(self) -> None:
        errors: list[str] = []

        validate_mlx_qwen_v2_raw_coverage(self.precise_boundary_raw(), errors=errors)

        self.assertEqual(errors, [])

    def test_central_validator_accepts_per_chunk_token_accounting(self) -> None:
        errors: list[str] = []

        validate_mlx_qwen_v2_raw_coverage(self.per_chunk_boundary_raw(), errors=errors)

        self.assertEqual(errors, [])

    def test_central_validator_accepts_adaptive_no_split(self) -> None:
        errors: list[str] = []

        validate_mlx_qwen_v2_raw_coverage(self.adaptive_boundary_raw(split=False), errors=errors)

        self.assertEqual(errors, [])

    def test_central_validator_accepts_adaptive_single_split(self) -> None:
        errors: list[str] = []

        validate_mlx_qwen_v2_raw_coverage(self.adaptive_boundary_raw(split=True), errors=errors)

        self.assertEqual(errors, [])

    def test_central_validator_accepts_depth_four_adaptive_tree(self) -> None:
        errors: list[str] = []

        validate_mlx_qwen_v2_raw_coverage(self.adaptive_depth_four_raw(), errors=errors)

        self.assertEqual(errors, [])

    def test_central_validator_preserves_legacy_depth_three_scope(self) -> None:
        raw = self.adaptive_boundary_raw(split=True)
        errors: list[str] = []

        validate_mlx_qwen_v2_raw_coverage(raw, errors=errors)

        self.assertEqual(errors, [])

    def test_central_validator_rejects_adaptive_scope_depth_crossovers(self) -> None:
        cases = (
            (self.adaptive_depth_four_raw(), 3),
            (self.adaptive_boundary_raw(split=True), 4),
        )
        for raw, wrong_depth in cases:
            with self.subTest(scope=raw["options"]["token_budget_scope"]):
                raw["options"]["adaptive_max_depth"] = wrong_depth
                errors: list[str] = []

                validate_mlx_qwen_v2_raw_coverage(raw, errors=errors)

                self.assertTrue(any("adaptive_max_depth" in error for error in errors), errors)

    def test_central_validator_rejects_a_depth_four_split_event(self) -> None:
        raw = self.adaptive_depth_four_raw()
        raw["generation_plan"]["split_events"][-1].update({"split_path": "LLLL", "depth": 4})
        errors: list[str] = []

        validate_mlx_qwen_v2_raw_coverage(raw, errors=errors)

        self.assertTrue(any("split_path is invalid" in error for error in errors), errors)

    def test_central_validator_rejects_adaptive_exhausted_leaf(self) -> None:
        raw = self.adaptive_boundary_raw(split=True)
        raw["segments"][1]["generation_tokens"] = 4096
        raw["performance"]["generation_tokens"] = 4176
        raw["performance"]["attempt_generation_tokens"] = 8272
        errors: list[str] = []

        validate_mlx_qwen_v2_raw_coverage(raw, errors=errors)

        self.assertTrue(
            any("segments[1].generation_tokens" in error for error in errors),
            errors,
        )

    def test_central_validator_rejects_adaptive_accounting_tampering(self) -> None:
        cases: tuple[tuple[str, Callable[[dict[str, Any]], None], str], ...] = (
            (
                "accepted-token sum",
                lambda raw: (
                    raw["performance"].__setitem__("generation_tokens", 169),
                    raw["performance"].__setitem__("attempt_generation_tokens", 4265),
                ),
                "must sum to raw.performance.generation_tokens",
            ),
            (
                "attempt generation tokens",
                lambda raw: raw["performance"].__setitem__("attempt_generation_tokens", 4265),
                "attempt_generation_tokens must include every discarded exhausted parent",
            ),
            (
                "attempt prompt tokens",
                lambda raw: raw["performance"].__setitem__("attempt_prompt_tokens", 19),
                "attempt_prompt_tokens must include every discarded parent",
            ),
            (
                "generation call count",
                lambda raw: raw["performance"].__setitem__("generation_call_count", 2),
                "generation_call_count must equal planned chunks + 2 * splits",
            ),
        )
        for label, mutate, expected in cases:
            with self.subTest(label=label):
                raw = self.adaptive_boundary_raw(split=True)
                mutate(raw)
                errors: list[str] = []

                validate_mlx_qwen_v2_raw_coverage(raw, errors=errors)

                self.assertTrue(any(expected in error for error in errors), errors)

    def test_central_validator_rejects_adaptive_plan_tampering(self) -> None:
        maximum_window_energy = 1600 * 32768**2
        cases: tuple[tuple[str, Callable[[dict[str, Any]], None], str], ...] = (
            (
                "PCM commitment",
                lambda raw: raw["generation_plan"].__setitem__("pcm_s16le_sha256", "G" * 64),
                "pcm_s16le_sha256",
            ),
            (
                "boolean temperature",
                lambda raw: raw["options"].__setitem__("temperature", False),
                "requires temperature=0.0",
            ),
            (
                "parent prompt count",
                lambda raw: raw["generation_plan"]["split_events"][0].__setitem__(
                    "parent_prompt_tokens", True
                ),
                "parent_prompt_tokens",
            ),
            (
                "parent token count",
                lambda raw: raw["generation_plan"]["split_events"][0].__setitem__(
                    "parent_generation_tokens", 4095
                ),
                "parent_generation_tokens",
            ),
            (
                "split path",
                lambda raw: raw["generation_plan"]["split_events"][0].__setitem__(
                    "split_path", "X"
                ),
                "split_path is invalid",
            ),
            (
                "cut sample",
                lambda raw: raw["generation_plan"]["split_events"][0].__setitem__(
                    "split_sample", 20 * 16_000 - 1
                ),
                "split_sample",
            ),
            (
                "parent boundary",
                lambda raw: raw["generation_plan"]["split_events"][0].__setitem__(
                    "parent_end_sample", 60 * 16_000 - 1
                ),
                "parent_end_sample",
            ),
            (
                "legal boundary",
                lambda raw: raw["generation_plan"]["split_events"][0].__setitem__(
                    "legal_start_sample", 20 * 16_000 + 1
                ),
                "legal_start_sample",
            ),
            (
                "cut energy",
                lambda raw: raw["generation_plan"]["split_events"][0].__setitem__(
                    "cut_energy_sum_squares", maximum_window_energy + 1
                ),
                "cut_energy_sum_squares",
            ),
            (
                "event count",
                lambda raw: raw["generation_plan"]["split_events"].append(
                    copy.deepcopy(raw["generation_plan"]["split_events"][0])
                ),
                "split_events must match adaptive_split_count",
            ),
            (
                "final leaf count",
                lambda raw: raw["options"].__setitem__("final_leaf_chunk_count", 3),
                "final_leaf_chunk_count must equal the raw segment count",
            ),
            (
                "split count",
                lambda raw: raw["options"].__setitem__("adaptive_split_count", 0),
                "split_events must match adaptive_split_count",
            ),
            (
                "effective budget",
                lambda raw: raw["options"].__setitem__("effective_total_token_budget", 4096),
                "effective_total_token_budget must equal max_tokens_per_chunk",
            ),
        )
        for label, mutate, expected in cases:
            with self.subTest(label=label):
                raw = self.adaptive_boundary_raw(split=True)
                mutate(raw)
                errors: list[str] = []

                validate_mlx_qwen_v2_raw_coverage(raw, errors=errors)

                self.assertTrue(any(expected in error for error in errors), errors)

    def test_central_validator_accepts_exact_one_sample_final_ownership(
        self,
    ) -> None:
        raw = self.per_chunk_boundary_raw()
        raw["audio"].update({"duration_seconds": 1.0, "sample_count": 16_001})
        raw["segments"][0]["end"] = 1.0
        raw["segments"][1].update({"start": 1.0, "end": 16_001 / 16_000})
        errors: list[str] = []

        validate_mlx_qwen_v2_raw_coverage(raw, errors=errors)

        self.assertEqual(errors, [])

    def test_central_validator_rejects_per_chunk_budget_exhaustion(self) -> None:
        raw = self.per_chunk_boundary_raw()
        raw["segments"][1]["generation_tokens"] = 4096
        raw["performance"]["generation_tokens"] = 4176
        errors: list[str] = []

        validate_mlx_qwen_v2_raw_coverage(raw, errors=errors)

        self.assertTrue(
            any("segments[1].generation_tokens" in error for error in errors),
            errors,
        )

    def test_central_validator_rejects_per_chunk_token_sum_mismatch(self) -> None:
        raw = self.per_chunk_boundary_raw()
        raw["performance"]["generation_tokens"] = 169
        errors: list[str] = []

        validate_mlx_qwen_v2_raw_coverage(raw, errors=errors)

        self.assertTrue(any("must sum to raw.performance" in error for error in errors), errors)

    def test_central_validator_rejects_invalid_chunk_tokens(self) -> None:
        for label, value in (
            ("missing", None),
            ("boolean", True),
            ("negative", -1),
            ("float", 1.0),
        ):
            with self.subTest(label=label):
                raw = self.per_chunk_boundary_raw()
                if value is None:
                    del raw["segments"][1]["generation_tokens"]
                else:
                    raw["segments"][1]["generation_tokens"] = value
                errors: list[str] = []

                validate_mlx_qwen_v2_raw_coverage(raw, errors=errors)

                self.assertTrue(
                    any("segments[1].generation_tokens" in error for error in errors),
                    errors,
                )

    def test_central_validator_rejects_unknown_token_budget_scope(self) -> None:
        raw = self.per_chunk_boundary_raw()
        raw["options"]["token_budget_scope"] = "future-scope"
        errors: list[str] = []

        validate_mlx_qwen_v2_raw_coverage(raw, errors=errors)

        self.assertTrue(any("token_budget_scope" in error for error in errors), errors)

    def test_central_validator_rejects_per_chunk_text_merge_mismatch(self) -> None:
        raw = self.per_chunk_boundary_raw()
        raw["text"] = "被篡改的整集文本。"
        errors: list[str] = []

        validate_mlx_qwen_v2_raw_coverage(raw, errors=errors)

        self.assertTrue(
            any("ordered per-chunk segment text" in error for error in errors),
            errors,
        )

    def test_central_validator_rejects_precise_budget_exhaustion(self) -> None:
        errors: list[str] = []

        validate_mlx_qwen_v2_raw_coverage(
            self.precise_boundary_raw(generation_tokens=8192), errors=errors
        )

        self.assertTrue(
            any("effective full-audio token budget" in error for error in errors),
            errors,
        )

    def test_central_validator_rejects_inconsistent_precise_budget(self) -> None:
        raw = self.precise_boundary_raw()
        raw["options"]["planned_chunk_count"] = 1
        errors: list[str] = []

        validate_mlx_qwen_v2_raw_coverage(raw, errors=errors)

        self.assertTrue(
            any("planned_chunk_count" in error for error in errors),
            errors,
        )

    def test_central_validator_rejects_mismatched_effective_budget(self) -> None:
        raw = self.precise_boundary_raw()
        raw["options"]["effective_total_token_budget"] = 4096
        errors: list[str] = []

        validate_mlx_qwen_v2_raw_coverage(raw, errors=errors)

        self.assertTrue(
            any("max_tokens_per_chunk * planned_chunk_count" in error for error in errors),
            errors,
        )

    def test_central_validator_rejects_unbounded_numbers_without_crashing(
        self,
    ) -> None:
        cases = {
            "duration": (
                "audio",
                "duration_seconds",
                10**1000,
                "raw.audio.duration_seconds",
            ),
            "tiny-duration": (
                "audio",
                "duration_seconds",
                5e-324,
                "raw.audio.duration_seconds",
            ),
            "sample-count": (
                "audio",
                "sample_count",
                10**1000,
                "raw.audio.sample_count",
            ),
            "max-tokens": (
                "options",
                "max_tokens_per_chunk",
                10**1000,
                "raw.options.max_tokens_per_chunk",
            ),
            "planned-count": (
                "options",
                "planned_chunk_count",
                10**1000,
                "raw.options.planned_chunk_count",
            ),
            "effective-budget": (
                "options",
                "effective_total_token_budget",
                10**1000,
                "raw.options.effective_total_token_budget",
            ),
            "generation-tokens": (
                "performance",
                "generation_tokens",
                10**1000,
                "raw.performance.generation_tokens",
            ),
            "boolean-budget": (
                "options",
                "max_tokens_per_chunk",
                True,
                "raw.options.max_tokens_per_chunk",
            ),
        }
        for label, (container, key, value, expected_field) in cases.items():
            with self.subTest(label=label):
                raw = self.precise_boundary_raw()
                raw[container][key] = value
                errors: list[str] = []

                validate_mlx_qwen_v2_raw_coverage(raw, errors=errors)

                self.assertTrue(
                    any(
                        expected_field in error
                        and (
                            "supported range" in error
                            or "finite number with" in error
                            or "integer in" in error
                        )
                        for error in errors
                    ),
                    errors,
                )

    def test_central_validator_rejects_each_incomplete_precise_marker_set(
        self,
    ) -> None:
        fields = (
            ("audio", "sample_count"),
            ("options", "planned_chunk_count"),
            ("options", "effective_total_token_budget"),
        )
        for container, key in fields:
            with self.subTest(field=f"{container}.{key}"):
                raw = self.precise_boundary_raw()
                del raw[container][key]
                errors: list[str] = []

                validate_mlx_qwen_v2_raw_coverage(raw, errors=errors)

                self.assertTrue(
                    any("precise token budget metadata must include" in error for error in errors),
                    errors,
                )

    def test_central_validator_rejects_unbounded_segment_boundary(self) -> None:
        raw = self.precise_boundary_raw()
        raw["segments"][0]["start"] = 10**1000
        errors: list[str] = []

        validate_mlx_qwen_v2_raw_coverage(raw, errors=errors)

        self.assertTrue(any("segments[0].start" in error for error in errors), errors)

    def test_central_validator_rejects_boolean_segment_id(self) -> None:
        raw = self.precise_boundary_raw()
        raw["segments"][0]["id"] = False
        errors: list[str] = []

        validate_mlx_qwen_v2_raw_coverage(raw, errors=errors)

        self.assertTrue(any("segments[0].id" in error for error in errors), errors)

    def test_central_validator_rejects_subnormal_legacy_chunk_duration(
        self,
    ) -> None:
        raw = self.precise_boundary_raw()
        del raw["audio"]["sample_count"]
        del raw["options"]["planned_chunk_count"]
        del raw["options"]["effective_total_token_budget"]
        raw["options"]["chunk_duration_seconds"] = 5e-324
        errors: list[str] = []

        validate_mlx_qwen_v2_raw_coverage(raw, errors=errors)

        self.assertTrue(any("chunk_duration_seconds" in error for error in errors), errors)

    def test_central_validator_rejects_99ms_start_and_gap(self) -> None:
        cases = {"start": (0, 0.099), "gap": (1, 235.099)}
        for label, (segment_index, start) in cases.items():
            with self.subTest(label=label):
                raw = self.precise_boundary_raw()
                raw["segments"][segment_index]["start"] = start
                errors: list[str] = []

                validate_mlx_qwen_v2_raw_coverage(raw, errors=errors)

                self.assertTrue(
                    any("must continuously cover the audio" in error for error in errors),
                    errors,
                )

    def test_central_validator_accepts_one_millisecond_boundary_rounding(
        self,
    ) -> None:
        raw = self.precise_boundary_raw()
        raw["segments"][1]["start"] = 235.001
        errors: list[str] = []

        validate_mlx_qwen_v2_raw_coverage(raw, errors=errors)

        self.assertEqual(errors, [])

    def test_central_validator_rejects_cumulative_gaps_despite_overlap(
        self,
    ) -> None:
        raw = self.precise_boundary_raw()
        raw["audio"].update({"duration_seconds": 5.0, "sample_count": 5 * 16000})
        raw["options"].update({"planned_chunk_count": 5, "effective_total_token_budget": 20480})
        raw["segments"] = [
            {"id": 0, "start": 0.0, "end": 1.0, "text": "一。"},
            {"id": 1, "start": 1.001, "end": 2.0, "text": "二。"},
            {"id": 2, "start": 1.999, "end": 3.0, "text": "三。"},
            {"id": 3, "start": 3.001, "end": 4.0, "text": "四。"},
            {"id": 4, "start": 4.001, "end": 5.0, "text": "五。"},
        ]
        errors: list[str] = []

        validate_mlx_qwen_v2_raw_coverage(raw, errors=errors)

        self.assertTrue(
            any("cumulative chunk-boundary gaps" in error for error in errors),
            errors,
        )

    def test_central_validator_rejects_cumulative_overlaps_despite_gap(
        self,
    ) -> None:
        raw = self.precise_boundary_raw()
        raw["audio"].update({"duration_seconds": 5.0, "sample_count": 5 * 16000})
        raw["options"].update({"planned_chunk_count": 5, "effective_total_token_budget": 20480})
        raw["segments"] = [
            {"id": 0, "start": 0.0, "end": 1.0, "text": "一。"},
            {"id": 1, "start": 0.999, "end": 2.0, "text": "二。"},
            {"id": 2, "start": 2.001, "end": 3.0, "text": "三。"},
            {"id": 3, "start": 2.999, "end": 4.0, "text": "四。"},
            {"id": 4, "start": 3.999, "end": 5.0, "text": "五。"},
        ]
        errors: list[str] = []

        validate_mlx_qwen_v2_raw_coverage(raw, errors=errors)

        self.assertTrue(
            any("cumulative chunk-boundary overlaps" in error for error in errors),
            errors,
        )

    def test_accepts_strict_v2_mlx_model_identity_chain(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = QwenChainFixture(Path(directory))
            fixture.upgrade_to_v2()

            self.assertEqual(fixture.validate(), (True, []))

    def test_selected_web_qwen_v2_accepts_canonical_provenance(self) -> None:
        for precise_budget in (False, True):
            with (
                self.subTest(precise_budget=precise_budget),
                tempfile.TemporaryDirectory() as directory,
            ):
                fixture = QwenChainFixture(Path(directory))
                fixture.upgrade_to_v2()
                fixture.configure_web_ready_qwen_provenance(precise_budget=precise_budget)

                self.assertEqual(fixture.validate(), (True, []))

    def test_selected_web_legacy_qwen_binds_time_without_budget_markers(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = QwenChainFixture(Path(directory))
            fixture.configure_web_ready_qwen_provenance(precise_budget=False)

            self.assertEqual(fixture.validate(), (True, []))

        with tempfile.TemporaryDirectory() as directory:
            fixture = QwenChainFixture(Path(directory))
            fixture.configure_web_ready_qwen_provenance(precise_budget=False)
            readme = fixture.readme_path.read_text(encoding="utf-8")
            fixture.readme_path.write_text(
                readme.replace(
                    '    generated_at: "2026-08-09T12:02:00Z"\n',
                    '    generated_at: "2026-08-09T12:01:00Z"\n',
                    1,
                ),
                encoding="utf-8",
            )

            _, errors = fixture.validate()

            self.assertTrue(any("asr_runs.generated_at" in error for error in errors), errors)

    def test_selected_web_qwen_v2_rejects_missing_or_wrong_generated_at(
        self,
    ) -> None:
        canonical = "2026-08-09T12:02:00Z"
        cases = (
            (
                "missing transcript timestamp",
                f'  generated_at: "{canonical}"\n',
                "",
                "transcript.generated_at",
            ),
            (
                "wrong transcript timestamp",
                f'  generated_at: "{canonical}"\n',
                '  generated_at: "2026-08-09T12:01:00Z"\n',
                "transcript.generated_at",
            ),
            (
                "missing run timestamp",
                f'    generated_at: "{canonical}"\n',
                "",
                "asr_runs.generated_at",
            ),
            (
                "wrong run timestamp",
                f'    generated_at: "{canonical}"\n',
                '    generated_at: "2026-08-09T12:01:00Z"\n',
                "asr_runs.generated_at",
            ),
        )
        for label, old, new, expected in cases:
            with (
                self.subTest(label=label),
                tempfile.TemporaryDirectory() as directory,
            ):
                fixture = QwenChainFixture(Path(directory))
                fixture.upgrade_to_v2()
                fixture.configure_web_ready_qwen_provenance(precise_budget=False)
                readme = fixture.readme_path.read_text(encoding="utf-8")
                self.assertIn(old, readme)
                fixture.readme_path.write_text(readme.replace(old, new, 1), encoding="utf-8")

                _, errors = fixture.validate()

                self.assertTrue(any(expected in error for error in errors), errors)

    def test_selected_web_qwen_v2_rejects_missing_or_wrong_precise_budget(
        self,
    ) -> None:
        cases = (
            (
                "missing planned count",
                "    planned_chunk_count: 2\n",
                "",
                "transcript.options.planned_chunk_count",
            ),
            (
                "wrong planned count",
                "    planned_chunk_count: 2\n",
                "    planned_chunk_count: 1\n",
                "transcript.options.planned_chunk_count",
            ),
            (
                "missing effective budget",
                "    effective_total_token_budget: 8192\n",
                "",
                "transcript.options.effective_total_token_budget",
            ),
            (
                "wrong effective budget",
                "    effective_total_token_budget: 8192\n",
                "    effective_total_token_budget: 4096\n",
                "transcript.options.effective_total_token_budget",
            ),
        )
        for label, old, new, expected in cases:
            with (
                self.subTest(label=label),
                tempfile.TemporaryDirectory() as directory,
            ):
                fixture = QwenChainFixture(Path(directory))
                fixture.upgrade_to_v2()
                fixture.configure_web_ready_qwen_provenance(precise_budget=True)
                readme = fixture.readme_path.read_text(encoding="utf-8")
                self.assertIn(old, readme)
                fixture.readme_path.write_text(readme.replace(old, new, 1), encoding="utf-8")

                _, errors = fixture.validate()

                self.assertTrue(any(expected in error for error in errors), errors)

    def test_chain_reports_unbounded_mlx_duration_instead_of_crashing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = QwenChainFixture(Path(directory))
            fixture.upgrade_to_v2()
            fixture.rewrite_raw(
                lambda document: document["audio"].__setitem__("duration_seconds", 10**1000)
            )

            complete, errors = fixture.validate()

            self.assertTrue(complete)
            self.assertTrue(
                any("raw.audio.duration_seconds" in error for error in errors),
                errors,
            )

    def test_rejects_mlx_v2_raw_that_stops_before_audio_end(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = QwenChainFixture(Path(directory))
            fixture.upgrade_to_v2()
            fixture.rewrite_raw(lambda document: document["segments"].pop())

            _, errors = fixture.validate()

            self.assertTrue(
                any("must cover the audio through its end" in error for error in errors),
                errors,
            )

    def test_rejects_mlx_v2_raw_gap_and_nonzero_start(self) -> None:
        cases = ((0, 0.2), (1, 241.0))
        for segment_index, start in cases:
            with (
                self.subTest(segment_index=segment_index),
                tempfile.TemporaryDirectory() as directory,
            ):
                fixture = QwenChainFixture(Path(directory))
                fixture.upgrade_to_v2()
                fixture.rewrite_raw(
                    lambda document: document["segments"][segment_index].__setitem__("start", start)
                )

                _, errors = fixture.validate()

                self.assertTrue(
                    any("must continuously cover the audio" in error for error in errors),
                    errors,
                )

    def test_rejects_mlx_v2_raw_that_exhausts_effective_token_budget(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = QwenChainFixture(Path(directory))
            fixture.upgrade_to_v2()
            fixture.rewrite_raw(
                lambda document: document["performance"].__setitem__("generation_tokens", 8192)
            )

            _, errors = fixture.validate()

            self.assertTrue(
                any("effective full-audio token budget" in error for error in errors),
                errors,
            )

    def test_accepts_strict_v2_cuda_native_chain(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = QwenChainFixture(Path(directory))
            fixture.upgrade_to_v2(
                engine="qwen-asr-transformers",
                model=CUDA_QWEN_MODEL,
                model_revision=CUDA_QWEN_MODEL_REVISION,
                aligner=CUDA_QWEN_ALIGNER,
                aligner_revision=CUDA_QWEN_ALIGNER_REVISION,
                raw_options=cuda_native_options(),
                aligned_options=cuda_native_options(),
            )

            self.assertEqual(fixture.validate(), (True, []))

    def test_rejects_legacy_qwen_asr_cuda_v2_chain(self) -> None:
        legacy_options = {
            "backend": "qwen-asr",
            "qwen_asr_version": "0.0.6",
            "torch_version": "2.11.0",
        }
        with tempfile.TemporaryDirectory() as directory:
            fixture = QwenChainFixture(Path(directory))
            fixture.upgrade_to_v2(
                engine="qwen-asr-transformers",
                model="Qwen/Qwen3-ASR-1.7B",
                model_revision="7278e1e70fe206f11671096ffdd38061171dd6e5",
                aligner="Qwen/Qwen3-ForcedAligner-0.6B",
                aligner_revision="c7cbfc2048c462b0d63a45797104fc9db3ad62b7",
                raw_options=legacy_options,
                aligned_options=legacy_options,
            )

            complete, errors = fixture.validate()

            self.assertTrue(complete)
            self.assertTrue(any("Qwen CUDA v2 raw.model must equal" in e for e in errors))
            self.assertTrue(any("must not record qwen_asr_version" in e for e in errors))

    def test_rejects_cuda_v2_wrong_model_aligner_and_revisions(self) -> None:
        cases = (
            (
                "model",
                {"model": "Qwen/Qwen3-ASR-1.7B"},
                "Qwen CUDA v2 raw.model must equal",
            ),
            (
                "aligner",
                {"aligner": "Qwen/Qwen3-ForcedAligner-0.6B"},
                "Qwen CUDA v2 aligned.source.aligner must equal",
            ),
            (
                "model revision",
                {"model_revision": "a" * 40},
                "Qwen CUDA v2 raw.model_identity.requested_revision must equal",
            ),
            (
                "aligner revision",
                {"aligner_revision": "b" * 40},
                "Qwen CUDA v2 aligned.source.aligner_identity.requested_revision must equal",
            ),
        )
        for label, overrides, expected in cases:
            with self.subTest(label=label), tempfile.TemporaryDirectory() as directory:
                fixture = QwenChainFixture(Path(directory))
                values = {
                    "engine": "qwen-asr-transformers",
                    "model": CUDA_QWEN_MODEL,
                    "model_revision": CUDA_QWEN_MODEL_REVISION,
                    "aligner": CUDA_QWEN_ALIGNER,
                    "aligner_revision": CUDA_QWEN_ALIGNER_REVISION,
                    "raw_options": cuda_native_options(),
                    "aligned_options": cuda_native_options(),
                    **overrides,
                }
                fixture.upgrade_to_v2(**values)

                _, errors = fixture.validate()

                self.assertTrue(any(expected in error for error in errors), errors)

    def test_rejects_cuda_v2_wrong_backend_package_versions_on_both_stages(
        self,
    ) -> None:
        cases = (
            ("backend", "qwen-asr"),
            ("transformers_version", "5.13.0"),
            ("torch_version", "2.12.0"),
        )
        for stage in ("raw", "aligned"):
            for key, value in cases:
                with (
                    self.subTest(stage=stage, key=key),
                    tempfile.TemporaryDirectory() as directory,
                ):
                    raw_options = cuda_native_options()
                    aligned_options = cuda_native_options()
                    selected_options = raw_options if stage == "raw" else aligned_options
                    selected_options[key] = value
                    fixture = QwenChainFixture(Path(directory))
                    fixture.upgrade_to_v2(
                        engine="qwen-asr-transformers",
                        model=CUDA_QWEN_MODEL,
                        model_revision=CUDA_QWEN_MODEL_REVISION,
                        aligner=CUDA_QWEN_ALIGNER,
                        aligner_revision=CUDA_QWEN_ALIGNER_REVISION,
                        raw_options=raw_options,
                        aligned_options=aligned_options,
                    )

                    _, errors = fixture.validate()

                    expected = f"Qwen CUDA v2 {stage}.options.{key} must equal"
                    self.assertTrue(any(expected in error for error in errors), errors)

    def test_rejects_missing_unknown_and_string_identity_schema_versions(self) -> None:
        for schema_version in (None, 2, "1"):
            with (
                self.subTest(schema_version=schema_version),
                tempfile.TemporaryDirectory() as directory,
            ):
                fixture = QwenChainFixture(Path(directory))
                fixture.upgrade_to_v2()
                raw = json.loads(fixture.raw_path.read_text(encoding="utf-8"))
                if schema_version is None:
                    del raw["model_identity"]["schema_version"]
                else:
                    raw["model_identity"]["schema_version"] = schema_version
                write_json(fixture.raw_path, raw)
                fixture.rewrite_aligned(
                    lambda document: document["source"].__setitem__(
                        "raw_asr_sha256", sha256_bytes(fixture.raw_path.read_bytes())
                    )
                )

                _, errors = fixture.validate()

                self.assertTrue(
                    any("model_identity.schema_version" in error for error in errors),
                    errors,
                )

    def test_rejects_identity_unknown_fields_and_unsafe_file_paths(self) -> None:
        cases = {
            "unknown": lambda identity: identity.__setitem__("unexpected", True),
            "absolute": lambda identity: identity["files_sha256"].__setitem__(
                "/weights.safetensors", "5" * 64
            ),
            "traversal": lambda identity: identity["files_sha256"].__setitem__(
                "../weights.safetensors", "5" * 64
            ),
        }
        for label, mutate in cases.items():
            with self.subTest(label=label), tempfile.TemporaryDirectory() as directory:
                fixture = QwenChainFixture(Path(directory))
                fixture.upgrade_to_v2()
                raw = json.loads(fixture.raw_path.read_text(encoding="utf-8"))
                mutate(raw["model_identity"])
                write_json(fixture.raw_path, raw)
                fixture.rewrite_aligned(
                    lambda document: document["source"].__setitem__(
                        "raw_asr_sha256", sha256_bytes(fixture.raw_path.read_bytes())
                    )
                )

                _, errors = fixture.validate()

                self.assertTrue(
                    any(
                        "model identity schema" in error
                        or "normalized relative POSIX paths" in error
                        for error in errors
                    ),
                    errors,
                )

    def test_rejects_cross_stage_identity_for_another_repository(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = QwenChainFixture(Path(directory))
            fixture.upgrade_to_v2()
            raw = json.loads(fixture.raw_path.read_text(encoding="utf-8"))
            raw["model_identity"]["repository"] = "other/model"
            write_json(fixture.raw_path, raw)
            aligned = json.loads(fixture.aligned_path.read_text(encoding="utf-8"))
            aligned["source"]["raw_asr_sha256"] = sha256_bytes(fixture.raw_path.read_bytes())
            aligned["source"]["model_identity"]["repository"] = "other/model"
            write_json(fixture.aligned_path, aligned)
            refined = json.loads(fixture.refined_path.read_text(encoding="utf-8"))
            refined["source"]["input_asr_sha256"] = sha256_bytes(fixture.aligned_path.read_bytes())
            refined["source"]["model_identity"]["repository"] = "other/model"
            write_json(fixture.refined_path, refined)

            _, errors = fixture.validate()

            self.assertTrue(
                any("model_identity.repository must equal raw.model" in error for error in errors),
                errors,
            )

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
                '{"audio":{"sha256":"%s"},"audio":{}}\n' % ("0" * 64),
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

    def test_rejects_unknown_mixed_and_non_integer_lineage_markers(self) -> None:
        cases = (
            (1, 1, 1),
            (3, 3, 3),
            ("2", "2", "2"),
            (True, True, True),
            (2, None, 2),
        )
        for markers in cases:
            with self.subTest(markers=markers), tempfile.TemporaryDirectory() as directory:
                fixture = QwenChainFixture(Path(directory))
                raw = json.loads(fixture.raw_path.read_text(encoding="utf-8"))
                raw["lineage_schema_version"] = markers[0]
                write_json(fixture.raw_path, raw)
                aligned = json.loads(fixture.aligned_path.read_text(encoding="utf-8"))
                if markers[1] is not None:
                    aligned["lineage_schema_version"] = markers[1]
                aligned["source"]["raw_asr_sha256"] = sha256_bytes(fixture.raw_path.read_bytes())
                write_json(fixture.aligned_path, aligned)
                refined = json.loads(fixture.refined_path.read_text(encoding="utf-8"))
                refined["lineage_schema_version"] = markers[2]
                refined["source"]["input_asr_sha256"] = sha256_bytes(
                    fixture.aligned_path.read_bytes()
                )
                write_json(fixture.refined_path, refined)

                _, errors = fixture.validate()

                self.assertTrue(
                    any("lineage_schema_version must be absent" in error for error in errors),
                    errors,
                )

    def test_rejects_non_repository_and_incorrect_recorded_paths(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = QwenChainFixture(Path(directory))
            fixture.rewrite_aligned(
                lambda document: document["source"].__setitem__("raw_asr_path", "../raw.json")
            )

            _, errors = fixture.validate()

            self.assertTrue(
                any(
                    "aligned.source.raw_asr_path must use a repository-relative" in error
                    for error in errors
                )
            )

    def test_rejects_raw_to_aligned_and_aligned_to_refined_hash_mismatches(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = QwenChainFixture(Path(directory))
            fixture.rewrite_aligned(
                lambda document: document["source"].__setitem__("raw_asr_sha256", "0" * 64)
            )
            refined = json.loads(fixture.refined_path.read_text(encoding="utf-8"))
            refined["source"]["input_asr_sha256"] = "1" * 64
            write_json(fixture.refined_path, refined)

            _, errors = fixture.validate()

            self.assertIn("aligned.source.raw_asr_sha256 does not match raw.json", errors)
            self.assertIn("refined.source.input_asr_sha256 does not match aligned.json", errors)

    def test_rejects_rendered_transcript_hash_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = QwenChainFixture(Path(directory))
            refined = json.loads(fixture.refined_path.read_text(encoding="utf-8"))
            refined["rendered_transcript"]["sha256"] = "0" * 64
            write_json(fixture.refined_path, refined)

            _, errors = fixture.validate()

            self.assertIn(
                "refined.rendered_transcript.sha256 does not match transcript.zh-CN.md",
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
            self.assertIn("aligned.source.audio_sha256 does not match cached audio", errors)

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

            self.assertTrue(any("requires exactly one zh-CN item" in error for error in errors))

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
                "# Shared title\n\n[00:00:00] 你好。  \n[00:00:05] 世界。  \n",
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
                "transcript.translations[0].source_sha256 does not match transcript.en.md",
                errors,
            )
            self.assertIn(
                "transcript.translations[0].sha256 does not match transcript.zh-CN.md",
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

            self.assertIn("transcript.translations[0].language must be 'zh-CN'", errors)
            self.assertTrue(
                any("transcript.translations[0].path must point to" in error for error in errors)
            )
            self.assertIn("transcript.translations[0].source_language must be 'en'", errors)
            self.assertTrue(
                any(
                    "transcript.translations[0].source_path must point to" in error
                    for error in errors
                )
            )
            self.assertIn("transcript.translations[0].alignment must be 'segment'", errors)
            self.assertIn(
                "transcript.translations[0].status must be one of machine, edited, reviewed",
                errors,
            )
            self.assertIn(
                "transcript.translations[0].generated_at must be an RFC 3339 timestamp",
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


class ShowMetadataContractTests(unittest.TestCase):
    def validate(self, root: Path, text: str) -> list[str]:
        readme = root / "shows" / "example" / "README.md"
        readme.parent.mkdir(parents=True)
        readme.write_text(text, encoding="utf-8")
        errors: list[str] = []
        validate_show_metadata_contract(
            readme,
            text,
            repository_root=root,
            show_ids={},
            errors=errors,
        )
        return errors

    def test_show_template_is_valid_after_filling_its_date_placeholder(self) -> None:
        template = (
            (ROOT / "templates" / "show" / "README.md")
            .read_text(encoding="utf-8")
            .replace("id: showid", "id: example")
            .replace("YYYY-MM-DD", "2026-08-09")
        )
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(self.validate(Path(directory), template), [])

    def test_rejects_fields_that_the_web_show_schema_rejects(self) -> None:
        template = (
            (ROOT / "templates" / "show" / "README.md")
            .read_text(encoding="utf-8")
            .replace("id: showid", "id: example")
            .replace("YYYY-MM-DD", "2026-08-09")
        )
        cases = {
            "status": template.replace("status: active", "status: unknown"),
            "formats": template.replace("formats:\n  - interview", "formats: []"),
            "topics": template.replace("topics:\n  - technology", "topics: []"),
            "platform": template.replace("platform: website", "platform: publisher-platform"),
            "source URL": template.replace(
                "https://publisher.example/show", "http://publisher.example/show"
            ),
            "malformed source URL": template.replace("https://publisher.example/show", "https://"),
            "source field": template.replace(
                "    preferred: true", "    preferred: true\n    invented: value"
            ),
            "verified date": template.replace(
                "last_verified_at: 2026-08-09", "last_verified_at: someday"
            ),
        }
        for label, text in cases.items():
            with self.subTest(label=label), tempfile.TemporaryDirectory() as directory:
                self.assertTrue(self.validate(Path(directory), text))


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

    def test_rejects_trailer_as_an_episode_release_type(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            readme = write_episode_contract_fixture(root, folder="001-trailer", episode_key="001")
            readme.write_text(
                readme.read_text(encoding="utf-8").replace(
                    "release_type: regular", "release_type: trailer"
                ),
                encoding="utf-8",
            )

            _, errors = self.validate(root, readme)

            self.assertTrue(any("release_type must be one of" in error for error in errors))

    def test_publishable_episode_requires_one_selected_run(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            readme = write_episode_contract_fixture(
                root, folder="001-no-selected", episode_key="001"
            )
            readme.write_text(
                readme.read_text(encoding="utf-8").replace(
                    "selection_status: selected", "selection_status: candidate"
                ),
                encoding="utf-8",
            )
            _, errors = self.validate(root, readme)
            self.assertTrue(any("exactly one selected ASR run" in error for error in errors))

    def test_numbering_requires_a_source_matching_the_web_schema(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            readme = write_episode_contract_fixture(
                root, folder="001-numbering-source", episode_key="001"
            )
            readme.write_text(
                readme.read_text(encoding="utf-8").replace("  source: test-fixture\n", ""),
                encoding="utf-8",
            )
            _, errors = self.validate(root, readme)
            self.assertTrue(
                any("numbering.source must be a non-empty string" in error for error in errors)
            )

    def test_summary_provenance_rejects_unknown_timestamp(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            readme = write_episode_contract_fixture(
                root, folder="001-bad-timecode", episode_key="001"
            )
            (readme.parent / "summary.zh-CN.md").write_text(
                "# 测试总结\n\n错误引用 [00:59:59]\n", encoding="utf-8"
            )
            _, errors = self.validate(root, readme)
            self.assertTrue(
                any("does not exist in summary.source_transcript" in error for error in errors)
            )

    def test_xiaoyuzhou_source_requires_complete_identity(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            readme = write_episode_contract_fixture(root, folder="001-xiaoyu", episode_key="001")
            text = readme.read_text(encoding="utf-8").replace(
                "platform: website\n    kind: episode\n    url: https://example.com/001-xiaoyu/1",
                "platform: xiaoyuzhou\n    kind: episode\n    url: https://www.xiaoyuzhoufm.com/episode/0123456789abcdef01234567",
            )
            readme.write_text(text, encoding="utf-8")
            _, errors = self.validate(root, readme)
            self.assertTrue(any("identifiers.eid is required" in error for error in errors))

    def test_website_profile_source_is_supported(self) -> None:
        errors: list[str] = []

        validate_source_schema(
            [
                {
                    "platform": "website",
                    "kind": "profile",
                    "url": "https://example.com/people/test-person",
                }
            ],
            field_prefix="episode test",
            errors=errors,
        )

        self.assertEqual([], errors)

    def test_xiaoyuzhou_source_requires_episode_platform_and_kind(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            readme = write_episode_contract_fixture(
                root, folder="001-xiaoyu-kind", episode_key="001"
            )
            source = (
                "platform: xiaoyuzhou\n"
                "    kind: audio\n"
                "    url: https://www.xiaoyuzhoufm.com/episode/0123456789abcdef01234567\n"
                "    identifiers:\n"
                "      eid: 0123456789abcdef01234567\n"
                "      pid: fedcba987654321001234567\n"
                "      media_id: fedcba987654321001234567/example.m4a"
            )
            readme.write_text(
                readme.read_text(encoding="utf-8").replace(
                    "platform: website\n"
                    "    kind: episode\n"
                    "    url: https://example.com/001-xiaoyu-kind/1",
                    source,
                ),
                encoding="utf-8",
            )

            _, errors = self.validate(root, readme)

            self.assertTrue(
                any("must use platform xiaoyuzhou and kind episode" in error for error in errors)
            )

    def test_youtube_video_source_requires_exact_identity(self) -> None:
        errors: list[str] = []
        validate_source_schema(
            [
                {
                    "platform": "youtube",
                    "kind": "video",
                    "url": "https://www.youtube.com/watch?v=-RXD4bTuFTo",
                    "preferred": True,
                    "identifiers": {
                        "video_id": "-RXD4bTuFTo",
                        "channel_id": "UCXl4i9dYBrFOabk0xGmbkRA",
                    },
                }
            ],
            field_prefix="episode",
            errors=errors,
        )
        self.assertEqual(errors, [])

    def test_youtube_video_source_rejects_case_drift(self) -> None:
        errors: list[str] = []
        validate_source_schema(
            [
                {
                    "platform": "youtube",
                    "kind": "video",
                    "url": "https://www.youtube.com/watch?v=-RXD4bTuFTo",
                    "preferred": True,
                    "identifiers": {
                        "video_id": "-rxd4btufTo",
                        "channel_id": "UCXl4i9dYBrFOabk0xGmbkRA",
                    },
                }
            ],
            field_prefix="episode",
            errors=errors,
        )
        self.assertTrue(any("video_id must match" in error for error in errors))

    def test_youtube_url_checker_accepts_only_canonical_video_and_playlist(self) -> None:
        errors: list[str] = []
        count = check_youtube_urls(
            Path("shows/example/README.md"),
            "\n".join(
                [
                    "https://www.youtube.com/watch?v=-RXD4bTuFTo",
                    (
                        "https://www.youtube.com/playlist?list="
                        "PLd7-bHaQwnthaNDpZ32TtYONGVk95-fhF"
                    ),
                ]
            ),
            errors,
        )
        self.assertEqual(count, 2)
        self.assertEqual(errors, [])

    def test_episode_may_register_a_bilibili_channel_as_a_secondary_source(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            readme = write_episode_contract_fixture(root, folder="001-channel", episode_key="001")
            readme.write_text(
                readme.read_text(encoding="utf-8").replace(
                    "platform: website\n"
                    "    kind: episode\n"
                    "    url: https://example.com/001-channel/1",
                    "platform: bilibili\n"
                    "    kind: channel\n"
                    "    url: https://space.bilibili.com/12345/",
                ),
                encoding="utf-8",
            )

            _, errors = self.validate(root, readme)

            self.assertEqual(errors, [])

    def test_audio_asr_duration_must_equal_local_cache(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            readme = write_episode_contract_fixture(root, folder="001-duration", episode_key="001")
            readme.write_text(
                readme.read_text(encoding="utf-8").replace(
                    "  duration_ms: 60000", "  duration_ms: 59999", 1
                ),
                encoding="utf-8",
            )

            _, errors = self.validate(root, readme)

            self.assertTrue(
                any("must equal local_audio_cache.duration_ms" in error for error in errors)
            )

    def test_non_audio_transcript_may_omit_local_audio_cache(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            readme = write_episode_contract_fixture(
                root, folder="001-publisher-text", episode_key="001"
            )
            text = readme.read_text(encoding="utf-8").replace(
                "acquisition_method: audio-asr",
                "acquisition_method: publisher-transcript",
            )
            cache_start = text.index("local_audio_cache:\n")
            cache_end = text.index("---\n", cache_start)
            readme.write_text(
                text[:cache_start] + "local_audio_cache: null\n" + text[cache_end:],
                encoding="utf-8",
            )

            _, errors = self.validate(root, readme)

            self.assertFalse(any("local_audio_cache" in error for error in errors), errors)

    def test_participant_profile_validation_is_part_of_metadata_contract(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            readme = write_episode_contract_fixture(
                root,
                folder="001-profile",
                episode_key="001-profile",
            )
            text = readme.read_text(encoding="utf-8").replace(
                "    role: guest\nsources:\n",
                "    role: guest\n"
                "    profile:\n"
                '      headline: ""\n'
                "      checked_at: 2026-08-09\n"
                "sources:\n",
                1,
            )
            readme.write_text(text, encoding="utf-8")

            _, errors = self.validate(root, readme)

            self.assertTrue(any("profile.headline must be a non-empty string" in e for e in errors))

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

            self.assertTrue(
                any("summary.path escapes the episode directory" in error for error in errors)
            )

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


class WikiIndexContractTests(unittest.TestCase):
    ROOT_TRANSLATION_LINK = "[中文译稿](./shows/example/episodes/001-test/transcript.zh-CN.md)"
    SHOW_TRANSLATION_LINK = "[中文译稿](./episodes/001-test/transcript.zh-CN.md)"
    ROOT_EPISODE_ROW = (
        "| [Canonical \\| Title](https://publisher.example/episode) | Test Guest | "
        "[Example Show](./shows/example/) | 2026-08-08 | "
        "[总结](./shows/example/episodes/001-test/summary.zh-CN.md) | "
        "[逐字稿](./shows/example/episodes/001-test/transcript.zh-CN.md) |"
    )
    SHOW_EPISODE_ROW = (
        "| [Canonical \\| Title](https://publisher.example/episode) | Example Show | "
        "2026-08-08 | [总结](./episodes/001-test/summary.zh-CN.md) | "
        "[逐字稿](./episodes/001-test/transcript.zh-CN.md) |"
    )
    ROOT_BILINGUAL_EPISODE_ROW = (
        "| [Canonical \\| Title](https://publisher.example/episode) | Test Guest | "
        "[Example Show](./shows/example/) | 2026-08-08 | "
        "[总结](./shows/example/episodes/001-test/summary.zh-CN.md) | "
        "[英文逐字稿](./shows/example/episodes/001-test/transcript.en.md) · "
        f"{ROOT_TRANSLATION_LINK} |"
    )
    SHOW_BILINGUAL_EPISODE_ROW = (
        "| [Canonical \\| Title](https://publisher.example/episode) | Example Show | "
        "2026-08-08 | [总结](./episodes/001-test/summary.zh-CN.md) | "
        "[英文逐字稿](./episodes/001-test/transcript.en.md) · "
        f"{SHOW_TRANSLATION_LINK} |"
    )

    @classmethod
    def write_fixture(
        cls,
        root: Path,
        *,
        root_episode_rows: list[str] | None = None,
        show_episode_rows: list[str] | None = None,
        bilingual: bool = False,
    ) -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
        default_root_row = cls.ROOT_BILINGUAL_EPISODE_ROW if bilingual else cls.ROOT_EPISODE_ROW
        default_show_row = cls.SHOW_BILINGUAL_EPISODE_ROW if bilingual else cls.SHOW_EPISODE_ROW
        root_rows = root_episode_rows or [default_root_row]
        show_rows = show_episode_rows or [default_show_row]
        (root / "README.md").write_text(
            "# Test\n\n"
            "## 收录播客\n\n"
            "| 播客 | 简介 | 节目页 |\n"
            "| --- | --- | --- |\n"
            "| [Example Show](https://publisher.example/show) | Intro | "
            "[README](./shows/example/) |\n\n"
            "## 单集索引\n\n"
            "| 标题 | 访谈人物 | 播客名称 | 日期 | 总结 | 逐字稿 |\n"
            "| --- | --- | --- | --- | --- | --- |\n" + "\n".join(root_rows) + "\n",
            encoding="utf-8",
        )
        show_dir = root / "shows" / "example"
        show_dir.mkdir(parents=True)
        (show_dir / "README.md").write_text(
            "# Example Show\n\n"
            "## 单集\n\n"
            "| 标题 | 播客名称 | 日期 | 总结链接 | 逐字稿链接 |\n"
            "| --- | --- | --- | --- | --- |\n" + "\n".join(show_rows) + "\n",
            encoding="utf-8",
        )
        shows = {
            "example": {
                "id": "example",
                "title": "Example Show",
                "preferred": {"url": "https://publisher.example/show"},
            }
        }
        episodes = [
            {
                "show_id": "example",
                "show_title": "Example Show",
                "title": "Canonical | Title",
                "date": "2026-08-08",
                "guests": "Test Guest",
                "preferred_url": "https://publisher.example/episode",
                "root_show_link": "./shows/example/",
                "root_summary_link": "./shows/example/episodes/001-test/summary.zh-CN.md",
                "root_transcript_link": "./shows/example/episodes/001-test/transcript.zh-CN.md",
                "show_summary_link": "./episodes/001-test/summary.zh-CN.md",
                "show_transcript_link": "./episodes/001-test/transcript.zh-CN.md",
            }
        ]
        if bilingual:
            episodes[0].update(
                {
                    "root_transcript_link": ("./shows/example/episodes/001-test/transcript.en.md"),
                    "root_translation_link": (
                        "./shows/example/episodes/001-test/transcript.zh-CN.md"
                    ),
                    "show_transcript_link": "./episodes/001-test/transcript.en.md",
                    "show_translation_link": ("./episodes/001-test/transcript.zh-CN.md"),
                }
            )
        return shows, episodes

    def validate(
        self,
        root: Path,
        *,
        root_episode_rows: list[str] | None = None,
        show_episode_rows: list[str] | None = None,
        bilingual: bool = False,
    ) -> list[str]:
        shows, episodes = self.write_fixture(
            root,
            root_episode_rows=root_episode_rows,
            show_episode_rows=show_episode_rows,
            bilingual=bilingual,
        )
        errors: list[str] = []
        validate_wiki_indexes(
            repository_root=root,
            shows=shows,
            episodes=episodes,
            errors=errors,
        )
        return errors

    def test_accepts_exact_index_contract_and_escaped_title_pipe(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(self.validate(Path(directory)), [])

    def test_accepts_bilingual_transcript_links(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(self.validate(Path(directory), bilingual=True), [])

    def test_rejects_missing_zh_cn_translation_link(self) -> None:
        cases = {
            "root": {
                "root_episode_rows": [
                    self.ROOT_BILINGUAL_EPISODE_ROW.replace(f" · {self.ROOT_TRANSLATION_LINK}", "")
                ]
            },
            "show": {
                "show_episode_rows": [
                    self.SHOW_BILINGUAL_EPISODE_ROW.replace(f" · {self.SHOW_TRANSLATION_LINK}", "")
                ]
            },
        }
        for label, values in cases.items():
            with self.subTest(label=label), tempfile.TemporaryDirectory() as directory:
                errors = self.validate(Path(directory), bilingual=True, **values)
                self.assertTrue(
                    any("must link the zh-CN transcript translation" in error for error in errors),
                    errors,
                )

    def test_rejects_duplicate_summary_rows(self) -> None:
        cases = {
            "root": {"root_episode_rows": [self.ROOT_EPISODE_ROW, self.ROOT_EPISODE_ROW]},
            "show": {"show_episode_rows": [self.SHOW_EPISODE_ROW, self.SHOW_EPISODE_ROW]},
        }
        for label, values in cases.items():
            with self.subTest(label=label), tempfile.TemporaryDirectory() as directory:
                errors = self.validate(Path(directory), **values)
                self.assertTrue(any("duplicates summary link" in error for error in errors))

    def test_rejects_tampered_title_and_show_columns(self) -> None:
        cases = {
            "root title": {
                "root_episode_rows": [
                    self.ROOT_EPISODE_ROW.replace("Canonical \\| Title", "Wrong Title")
                ],
                "expected": "title must equal metadata",
            },
            "root show": {
                "root_episode_rows": [
                    self.ROOT_EPISODE_ROW.replace(
                        "[Example Show](./shows/example/)",
                        "[Wrong Show](./shows/wrong/)",
                    )
                ],
                "expected": "podcast must equal and link its show",
            },
            "show title": {
                "show_episode_rows": [
                    self.SHOW_EPISODE_ROW.replace("Canonical \\| Title", "Wrong Title")
                ],
                "expected": "title must equal metadata",
            },
            "show name": {
                "show_episode_rows": [
                    self.SHOW_EPISODE_ROW.replace("| Example Show |", "| Wrong Show |")
                ],
                "expected": "podcast name must equal show title",
            },
        }
        for label, values in cases.items():
            expected = values.pop("expected")
            with self.subTest(label=label), tempfile.TemporaryDirectory() as directory:
                errors = self.validate(Path(directory), **values)
                self.assertTrue(any(expected in error for error in errors), errors)


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
    def test_summary_reader_contract_requires_explicit_order_and_hides_editor_copy(
        self,
    ) -> None:
        path = ROOT / "shows" / "example" / "episodes" / "001" / "summary.zh-CN.md"
        valid = """# 测试

## 一句话总结

摘要。

## 为什么值得听

- 理由。

## 核心观点

| 主题 | 判断 |
| --- | --- |
| 示例 | 内容 |

## 5 分钟读完

内容。

## 主题导航

- [00:00:00] 开场

## 阅读边界

- ASR—LLM—TTS 是节目讨论的真实主题。

## 编辑记录（不对读者展示）

- 本稿仍需回听校对。
"""

        valid_errors: list[str] = []
        validate_summary_reader_contract(path, valid, valid_errors)
        self.assertEqual(valid_errors, [])

        order_errors: list[str] = []
        validate_summary_reader_contract(
            path,
            valid.replace("## 阅读边界", "## 事实边界与待核实"),
            order_errors,
        )
        self.assertTrue(any("missing or out of order" in error for error in order_errors))

        copy_errors: list[str] = []
        validate_summary_reader_contract(
            path,
            valid.replace(
                "- ASR—LLM—TTS 是节目讨论的真实主题。", "- 状态为 draft，仍是草稿，待审核。"
            ),
            copy_errors,
        )
        self.assertTrue(any("editor-only copy" in error for error in copy_errors))

    def test_core_point_logic_table_requires_semantic_columns_and_rows(self) -> None:
        path = ROOT / "shows" / "example" / "episodes" / "001" / "summary.zh-CN.md"

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
            '---\ncatalog_keyword: "SGLang"\n---\n',
            valid_errors,
        )
        self.assertEqual(valid_errors, [])

        invalid_errors: list[str] = []
        validate_episode_catalog_keyword(
            path,
            '---\ncatalog_keyword: "特别"\n---\n',
            invalid_errors,
        )
        self.assertTrue(any("release labels" in error for error in invalid_errors))

        missing_errors: list[str] = []
        validate_episode_catalog_keyword(path, "---\ntitle: example\n---\n", missing_errors)
        self.assertTrue(any("missing catalog_keyword" in error for error in missing_errors))

        duplicate_errors: list[str] = []
        validate_episode_catalog_keyword(
            path,
            '---\nnavigation_title: "盛颖 · SGLang 与开源"\ncatalog_keyword: "盛颖"\n---\n',
            duplicate_errors,
        )
        self.assertTrue(any("must not duplicate" in error for error in duplicate_errors))

    def test_episode_navigation_title_uses_person_topic_format(self) -> None:
        path = ROOT / "shows" / "example" / "episodes" / "001" / "README.md"

        valid_errors: list[str] = []
        validate_episode_navigation_title(
            path,
            '---\nnavigation_title: "盛颖 · SGLang 与开源"\n---\n',
            valid_errors,
        )
        self.assertEqual(valid_errors, [])

        invalid_errors: list[str] = []
        validate_episode_navigation_title(
            path,
            '---\nnavigation_title: "#247 盛颖 - SGLang"\n---\n',
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
            "https://www.xiaoyuzhoufm.com/podcast/6697cbecf103d7b06d18488b/?utm_source=test",
            errors,
        )

        self.assertEqual(count, 1)
        self.assertTrue(any("non-canonical Xiaoyuzhou URL" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
