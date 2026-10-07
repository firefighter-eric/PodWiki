from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from setup_shared_models import setup_shared_models  # noqa: E402


class SharedModelSetupTests(unittest.TestCase):
    def test_fresh_checkout_reuses_shared_files_and_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            base = Path(d)
            local, shared = base / "project/.cache/models", base / "shared"
            shared.mkdir()
            (shared / "weight.bin").write_bytes(b"weights")
            setup_shared_models(local, shared)
            setup_shared_models(local, shared)
            self.assertEqual((local / "weight.bin").read_bytes(), b"weights")
            self.assertTrue(local.samefile(shared))

    def test_migrates_existing_weights_with_metadata_and_links(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            base = Path(d)
            local, shared = base / "project/.cache/models", base / "shared"
            local.mkdir(parents=True)
            weight = local / "weight.bin"
            weight.write_bytes(b"existing weights")
            inode = weight.stat().st_ino
            (local / "alias.bin").symlink_to("weight.bin")
            setup_shared_models(local, shared)
            self.assertEqual((local / "weight.bin").stat().st_ino, inode)
            self.assertEqual((shared / "alias.bin").read_bytes(), b"existing weights")

    def test_existing_directory_conflict_preserves_both(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            base = Path(d)
            local, shared = base / "project/.cache/models", base / "shared"
            local.mkdir(parents=True)
            shared.mkdir()
            (local / "weight.bin").write_bytes(b"local")
            (shared / "weight.bin").write_bytes(b"shared")
            with self.assertRaises(ValueError):
                setup_shared_models(local, shared)
            self.assertEqual((local / "weight.bin").read_bytes(), b"local")
            self.assertEqual((shared / "weight.bin").read_bytes(), b"shared")

    def test_rejects_nested_target(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            local = Path(d) / "models"
            with self.assertRaises(ValueError):
                setup_shared_models(local, local / "nested")


if __name__ == "__main__":
    unittest.main()
