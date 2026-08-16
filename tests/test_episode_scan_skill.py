from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
INVENTORY_SCRIPT = (
    REPOSITORY_ROOT
    / ".agents/skills/podwiki-scan-episodes/scripts/build_episode_inventory.py"
)
VALIDATOR_SCRIPT = (
    REPOSITORY_ROOT
    / ".agents/skills/podwiki-scan-episodes/scripts/validate_scan_manifest.py"
)
KNOWN_BVID = "BV1Know00000"
NEW_BVID = "BV1New000000"


class EpisodeScanSkillTests(unittest.TestCase):
    def make_repository(self, root: Path) -> None:
        show = root / "shows/sv101"
        episode = show / "episodes/001-known"
        episode.mkdir(parents=True)
        (show / "README.md").write_text(
            """---
schema_version: 1
kind: show
id: sv101
title: 硅谷101
status: active
sources:
  - platform: bilibili
    kind: channel
    url: https://space.bilibili.com/508452265/
    preferred: true
    identifiers:
      mid: "508452265"
---

# 硅谷101
""",
            encoding="utf-8",
        )
        (episode / "README.md").write_text(
            f"""---
schema_version: 1
kind: episode
id: "sv101:001"
show_id: sv101
episode_key: "001"
episode_number: 1
title: Known episode
published_at: "2026-07-01T12:00:00+08:00"
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/{KNOWN_BVID}/
    preferred: true
    identifiers:
      bvid: {KNOWN_BVID}
---

# Known episode
""",
            encoding="utf-8",
        )

    def candidate(self, bvid: str = NEW_BVID, *, platform: str = "bilibili") -> dict[str, Any]:
        if platform == "bilibili":
            url = f"https://www.bilibili.com/video/{bvid}/"
            identifiers = {"bvid": bvid}
        else:
            url = "https://example.com/episode/new"
            identifiers = {"guid": "new-guid"}
        return {
            "decision": "eligible-new",
            "platform": platform,
            "canonical_url": url,
            "identifiers": identifiers,
            "title": "New complete dialogue",
            "published_at": "2026-08-15T12:00:00+08:00",
            "duration_seconds": 7200.25,
            "decision_reason": "Verified candidate absent from repository.",
            "evidence": [
                {
                    "type": "show-identity",
                    "url": "https://space.bilibili.com/508452265/",
                    "checked_at": "2026-08-16T00:05:00Z",
                    "note": "Official show publisher.",
                },
                {
                    "type": "complete-episode",
                    "url": url,
                    "checked_at": "2026-08-16T00:06:00Z",
                    "note": "Exact complete official episode.",
                },
                {
                    "type": "long-form-dialogue",
                    "url": url,
                    "checked_at": "2026-08-16T00:06:00Z",
                    "note": "Complete long-form dialogue.",
                },
            ],
            "matched_episode_id": None,
        }

    def manifest(self, candidate: dict[str, Any]) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "kind": "podwiki-episode-scan",
            "scan_id": "20260816T000000Z-sv101-test",
            "show_id": "sv101",
            "show_title": "硅谷101",
            "started_at": "2026-08-16T00:00:00Z",
            "completed_at": "2026-08-16T00:10:00Z",
            "status": "complete",
            "scope": {
                "mode": "incremental",
                "coverage_start": "2026-04-01T00:00:00Z",
                "coverage_end": "2026-08-16T00:10:00Z",
                "repository_commit": None,
                "required_platforms": ["bilibili"],
                "access_context": "anonymous",
            },
            "sources": [
                {
                    "platform": "bilibili",
                    "url": "https://space.bilibili.com/508452265/",
                    "role": "discovery",
                    "required": True,
                    "status": "verified",
                    "checked_at": "2026-08-16T00:09:00Z",
                    "coverage_complete": True,
                    "observed_item_urls": [candidate["canonical_url"]],
                    "evidence": "Official listing traversed through the declared start.",
                }
            ],
            "candidates": [candidate],
            "summary": {
                "eligible_new": 1,
                "already_present": 0,
                "excluded": 0,
                "needs_review": 0,
            },
        }

    def run_validator(self, root: Path, document: dict[str, Any]) -> subprocess.CompletedProcess[str]:
        manifest = root / "scan.json"
        manifest.write_text(
            json.dumps(document, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return subprocess.run(
            [
                sys.executable,
                str(VALIDATOR_SCRIPT),
                str(manifest),
                "--repository-root",
                str(root),
            ],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_inventory_extracts_stable_repository_identity(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            output = root / "inventory.json"
            result = subprocess.run(
                [
                    sys.executable,
                    str(INVENTORY_SCRIPT),
                    "--repository-root",
                    str(root),
                    "--show",
                    "sv101",
                    "--generated-at",
                    "2026-08-16T00:00:00Z",
                    "--output",
                    str(output),
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            inventory = json.loads(output.read_text(encoding="utf-8"))
            show = inventory["shows"][0]
            self.assertEqual(show["episode_count"], 1)
            self.assertEqual(show["episodes"][0]["id"], "sv101:001")
            self.assertEqual(show["recommended_incremental_coverage_start"], "2026-04-02T04:00:00Z")
            self.assertIn(f"bilibili:bvid:{KNOWN_BVID.lower()}", show["known_source_keys"])

    def test_validator_accepts_complete_new_strict_dialogue_candidate(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            result = self.run_validator(root, self.manifest(self.candidate()))
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_validator_rejects_known_episode_claimed_as_new(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            result = self.run_validator(root, self.manifest(self.candidate(KNOWN_BVID)))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("already exists in repository", result.stderr)

    def test_validator_rejects_false_complete_source_status(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            manifest = self.manifest(self.candidate())
            manifest["sources"][0]["status"] = "blocked"
            manifest["sources"][0]["coverage_complete"] = False
            result = self.run_validator(root, manifest)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("complete scans require every required source", result.stderr)

    def test_validator_rejects_narrow_incremental_window(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            manifest = self.manifest(self.candidate())
            manifest["scope"]["coverage_start"] = "2026-05-01T00:00:00Z"
            result = self.run_validator(root, manifest)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("narrower than the repository inventory", result.stderr)

    def test_validator_rejects_unclassified_discovery_item(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            manifest = self.manifest(self.candidate())
            manifest["sources"][0]["observed_item_urls"].append(
                "https://www.bilibili.com/video/BV1Miss00000/"
            )
            result = self.run_validator(root, manifest)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("observed discovery item is not classified", result.stderr)

    def test_validator_rejects_rss_only_candidate_for_strict_show(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            result = self.run_validator(root, self.manifest(self.candidate(platform="rss")))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("eligible-new must be on official Bilibili", result.stderr)


if __name__ == "__main__":
    unittest.main()
