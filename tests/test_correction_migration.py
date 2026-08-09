from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from audit_correction_migration import audit_repository  # noqa: E402


class CorrectionMigrationTests(unittest.TestCase):
    def test_episode_maps_reproduce_tracked_selected_artifacts(self) -> None:
        report = audit_repository()

        self.assertEqual(report["legacy_migration_maps"], 14)
        self.assertEqual(report["legacy_migration_hits"], 56)
        self.assertTrue(report["artifacts_unchanged"])


if __name__ == "__main__":
    unittest.main()
