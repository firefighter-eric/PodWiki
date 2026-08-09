#!/usr/bin/env python3
"""Prove episode correction maps reproduce the tracked selected artifacts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from render_asr_transcript import (
    load_correction_map,
    merge_blocks,
    read_json_strict,
    refine_segments,
    render_markdown,
    sha256_file,
    validate_correction_hits,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
LEGACY_MIGRATION_VERSION = "legacy-global-v1-migration"
EXPECTED_LEGACY_MAPS = 14
EXPECTED_LEGACY_HITS = 56


def _repository_path(path: Path) -> str:
    return path.resolve().relative_to(PROJECT_ROOT).as_posix()


def _require_mapping(value: Any, *, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be an object")
    return value


def audit_map(map_path: Path) -> dict[str, Any]:
    run_directory = map_path.parent / "qwen3-asr"
    aligned_path = run_directory / "aligned.json"
    refined_path = run_directory / "refined.json"
    transcript_path = run_directory / "transcript.zh-CN.md"
    for path in (aligned_path, refined_path, transcript_path):
        if not path.is_file():
            raise FileNotFoundError(f"correction map has no selected artifact: {path}")

    aligned = read_json_strict(aligned_path)
    refined = read_json_strict(refined_path)
    episode_id = refined.get("episode_id")
    if not isinstance(episode_id, str) or not episode_id:
        raise ValueError(f"refined artifact has no episode_id: {refined_path}")
    correction_map = load_correction_map(map_path, episode_id=episode_id)
    aligned_sha256 = sha256_file(aligned_path)
    if correction_map.input_asr_sha256 != aligned_sha256:
        raise ValueError(f"correction map input hash drifted: {map_path}")

    raw_segments = aligned.get("segments")
    if not isinstance(raw_segments, list):
        raise ValueError(f"aligned artifact has no segment list: {aligned_path}")
    hits = {rule.rule_id: 0 for rule in correction_map.rules}
    reproduced_segments = refine_segments(
        raw_segments,
        correction_rules=correction_map.rules,
        correction_hits=hits,
    )
    validate_correction_hits(correction_map, hits=hits)
    reproduced_blocks = merge_blocks(reproduced_segments)
    if reproduced_segments != refined.get("segments"):
        raise ValueError(f"correction map does not reproduce refined segments: {map_path}")
    if reproduced_blocks != refined.get("blocks"):
        raise ValueError(f"correction map does not reproduce refined blocks: {map_path}")

    transcript_bytes = transcript_path.read_bytes()
    try:
        transcript_text = transcript_bytes.decode("utf-8")
    except UnicodeDecodeError as error:
        raise ValueError(f"transcript is not UTF-8: {transcript_path}") from error
    first_line = transcript_text.splitlines()[0] if transcript_text else ""
    if not first_line.startswith("# "):
        raise ValueError(f"transcript has no title heading: {transcript_path}")
    reproduced_markdown = render_markdown(
        refined_segments=reproduced_segments,
        title=first_line.removeprefix("# "),
    ).encode("utf-8")
    if reproduced_markdown != transcript_bytes:
        raise ValueError(f"correction map does not reproduce transcript bytes: {map_path}")

    source = _require_mapping(refined.get("source"), label="refined source")
    rendered = _require_mapping(
        refined.get("rendered_transcript"), label="rendered transcript lineage"
    )
    if source.get("input_asr_sha256") != aligned_sha256:
        raise ValueError(f"legacy refined input hash drifted: {refined_path}")
    transcript_sha256 = sha256_file(transcript_path)
    if rendered.get("sha256") != transcript_sha256:
        raise ValueError(f"legacy refined transcript hash drifted: {refined_path}")

    return {
        "episode_id": episode_id,
        "map_path": _repository_path(map_path),
        "map_sha256": sha256_file(map_path),
        "version": correction_map.version,
        "input_asr_sha256": aligned_sha256,
        "refined_sha256": sha256_file(refined_path),
        "transcript_sha256": transcript_sha256,
        "rules": len(correction_map.rules),
        "hits": sum(hits.values()),
        "segments_equal": True,
        "blocks_equal": True,
        "transcript_bytes_equal": True,
    }


def audit_repository() -> dict[str, Any]:
    map_paths = sorted(
        PROJECT_ROOT.glob("shows/*/episodes/*/asr/corrections.json")
    )
    results = [audit_map(path) for path in map_paths]
    legacy_results = [
        result for result in results if result["version"] == LEGACY_MIGRATION_VERSION
    ]
    legacy_hits = sum(int(result["hits"]) for result in legacy_results)
    if len(legacy_results) != EXPECTED_LEGACY_MAPS or legacy_hits != EXPECTED_LEGACY_HITS:
        raise ValueError(
            "legacy correction migration coverage drifted: "
            f"expected maps/hits={EXPECTED_LEGACY_MAPS}/{EXPECTED_LEGACY_HITS}, "
            f"actual={len(legacy_results)}/{legacy_hits}"
        )
    return {
        "status": "ok",
        "maps": len(results),
        "legacy_migration_maps": len(legacy_results),
        "legacy_migration_hits": legacy_hits,
        "artifacts_unchanged": True,
        "results": results,
    }


def main() -> int:
    print(
        json.dumps(
            audit_repository(),
            ensure_ascii=False,
            indent=2,
            allow_nan=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
