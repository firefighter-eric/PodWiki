from __future__ import annotations

import json
import hashlib
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from asr_lineage import (  # noqa: E402
    IDENTITY_CACHE_NAME,
    build_model_identity,
    pinned_revision,
    validate_model_identity,
)


REPOSITORY = "mlx-community/Qwen3-ASR-1.7B-8bit"
REVISION = "a8379a2e2f9e313c9292cdf1af4055ab56d50d55"


class ModelIdentityTests(unittest.TestCase):
    @staticmethod
    def git_blob_sha1(path: Path) -> str:
        content = path.read_bytes()
        return hashlib.sha1(
            f"blob {len(content)}\0".encode("ascii") + content
        ).hexdigest()

    @staticmethod
    def write_metadata(
        model: Path,
        logical_path: str,
        *,
        commit: str,
        etag: str,
    ) -> Path:
        metadata = (
            model
            / ".cache"
            / "huggingface"
            / "download"
            / f"{logical_path}.metadata"
        )
        metadata.parent.mkdir(parents=True, exist_ok=True)
        metadata.write_text(f"{commit}\n{etag}\n0\n", encoding="utf-8")
        return metadata

    def model_directory(self, root: Path, *, commit: str = REVISION) -> Path:
        model = root / "model"
        model.mkdir()
        (model / "config.json").write_text('{"model_type":"qwen3_asr"}\n')
        (model / "model.safetensors").write_bytes(b"pinned model weights")
        (model / "merges.txt").write_text("a b\n", encoding="utf-8")
        (model / "vocab.json").write_text('{"a":0}\n', encoding="utf-8")
        self.write_metadata(
            model,
            "config.json",
            commit=commit,
            etag=self.git_blob_sha1(model / "config.json"),
        )
        self.write_metadata(
            model,
            "model.safetensors",
            commit=commit,
            etag=hashlib.sha256((model / "model.safetensors").read_bytes()).hexdigest(),
        )
        for logical_path in ("merges.txt", "vocab.json"):
            self.write_metadata(
                model,
                logical_path,
                commit=commit,
                etag=self.git_blob_sha1(model / logical_path),
            )
        return model

    def test_builds_and_reuses_a_pinned_identity_cache(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            model = self.model_directory(Path(directory))
            identity = build_model_identity(
                repository=REPOSITORY,
                requested_revision=None,
                local_path=model,
            )
            self.assertEqual(identity["resolved_commit"], REVISION)
            self.assertEqual(
                sorted(identity["files_sha256"]),
                ["config.json", "merges.txt", "model.safetensors", "vocab.json"],
            )
            self.assertEqual(validate_model_identity(identity, label="test"), identity)

            cache = model / IDENTITY_CACHE_NAME
            first_cache = cache.read_text(encoding="utf-8")
            repeated = build_model_identity(
                repository=REPOSITORY,
                requested_revision=REVISION,
                local_path=model,
            )
            self.assertEqual(repeated, identity)
            self.assertEqual(cache.read_text(encoding="utf-8"), first_cache)

    def test_rejects_mismatched_hugging_face_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            model = self.model_directory(Path(directory), commit="b" * 40)
            with self.assertRaisesRegex(ValueError, "commit mismatch"):
                build_model_identity(
                    repository=REPOSITORY,
                    requested_revision=REVISION,
                    local_path=model,
                )

    def test_requires_metadata_for_every_critical_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            model = self.model_directory(Path(directory))
            (
                model
                / ".cache"
                / "huggingface"
                / "download"
                / "model.safetensors.metadata"
            ).unlink()

            with self.assertRaisesRegex(ValueError, "model.safetensors"):
                build_model_identity(
                    repository=REPOSITORY,
                    requested_revision=REVISION,
                    local_path=model,
                )

    def test_rejects_conflicting_weight_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            model = self.model_directory(Path(directory))
            self.write_metadata(
                model,
                "model.safetensors",
                commit="b" * 40,
                etag=hashlib.sha256(
                    (model / "model.safetensors").read_bytes()
                ).hexdigest(),
            )

            with self.assertRaisesRegex(ValueError, "commit mismatch"):
                build_model_identity(
                    repository=REPOSITORY,
                    requested_revision=REVISION,
                    local_path=model,
                )

    def test_same_size_restored_mtime_tamper_is_not_hidden_by_cache(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            model = self.model_directory(Path(directory))
            build_model_identity(
                repository=REPOSITORY,
                requested_revision=REVISION,
                local_path=model,
            )
            weight = model / "model.safetensors"
            original_stat = weight.stat()
            weight.write_bytes(b"x" * original_stat.st_size)
            os.utime(
                weight,
                ns=(original_stat.st_atime_ns, original_stat.st_mtime_ns),
            )

            with self.assertRaisesRegex(ValueError, "etag does not match"):
                build_model_identity(
                    repository=REPOSITORY,
                    requested_revision=REVISION,
                    local_path=model,
                )

    def test_accepts_hf_local_dir_symlinks_and_records_logical_paths(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            hf_home = root / "hf-home"
            blobs = hf_home / "hub" / "models--example" / "blobs"
            blobs.mkdir(parents=True)
            config_blob = blobs / "config-blob"
            weight_blob = blobs / "weight-blob"
            config_blob.write_text('{"model_type":"qwen3_asr"}\n', encoding="utf-8")
            weight_blob.write_bytes(b"trusted symlinked weights")
            model = root / "pinned-v2"
            model.mkdir()
            (model / "config.json").symlink_to(config_blob)
            (model / "model.safetensors").symlink_to(weight_blob)
            self.write_metadata(
                model,
                "config.json",
                commit=REVISION,
                etag=self.git_blob_sha1(config_blob),
            )
            self.write_metadata(
                model,
                "model.safetensors",
                commit=REVISION,
                etag=hashlib.sha256(weight_blob.read_bytes()).hexdigest(),
            )

            with patch.dict(os.environ, {"HF_HOME": str(hf_home)}):
                identity = build_model_identity(
                    repository=REPOSITORY,
                    requested_revision=REVISION,
                    local_path=model,
                )

            self.assertEqual(
                sorted(identity["files_sha256"]),
                ["config.json", "model.safetensors"],
            )

    def test_snapshot_symlink_without_local_dir_metadata_fails_as_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            hf_home = root / "hf-home"
            repository_cache = hf_home / "hub" / "models--example"
            blobs = repository_cache / "blobs"
            snapshot = repository_cache / "snapshots" / REVISION
            blobs.mkdir(parents=True)
            snapshot.mkdir(parents=True)
            config_blob = blobs / "config-blob"
            weight_blob = blobs / "weight-blob"
            config_blob.write_text("{}\n", encoding="utf-8")
            weight_blob.write_bytes(b"weights")
            (snapshot / "config.json").symlink_to(config_blob)
            (snapshot / "model.safetensors").symlink_to(weight_blob)
            model = root / "legacy-model"
            model.symlink_to(snapshot, target_is_directory=True)

            with patch.dict(os.environ, {"HF_HOME": str(hf_home)}), self.assertRaisesRegex(
                ValueError, "download metadata"
            ):
                build_model_identity(
                    repository=REPOSITORY,
                    requested_revision=REVISION,
                    local_path=model,
                )

    def test_accepts_hf_local_dir_hardlinks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            blobs = root / "hf-home" / "hub" / "models--example" / "blobs"
            blobs.mkdir(parents=True)
            config_blob = blobs / "config-blob"
            weight_blob = blobs / "weight-blob"
            config_blob.write_text("{}\n", encoding="utf-8")
            weight_blob.write_bytes(b"hardlinked weights")
            model = root / "pinned-v2"
            model.mkdir()
            try:
                os.link(config_blob, model / "config.json")
                os.link(weight_blob, model / "model.safetensors")
            except OSError as error:
                self.skipTest(f"hardlinks unavailable: {error}")
            self.write_metadata(
                model,
                "config.json",
                commit=REVISION,
                etag=self.git_blob_sha1(config_blob),
            )
            self.write_metadata(
                model,
                "model.safetensors",
                commit=REVISION,
                etag=hashlib.sha256(weight_blob.read_bytes()).hexdigest(),
            )

            identity = build_model_identity(
                repository=REPOSITORY,
                requested_revision=REVISION,
                local_path=model,
            )

            self.assertEqual(
                identity["files_sha256"]["model.safetensors"],
                hashlib.sha256(weight_blob.read_bytes()).hexdigest(),
            )

    def test_requires_download_metadata_and_weight_hashes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            model = root / "model"
            model.mkdir()
            (model / "config.json").write_text("{}\n", encoding="utf-8")
            (model / "model.safetensors").write_bytes(b"weights")
            with self.assertRaisesRegex(ValueError, "download metadata"):
                build_model_identity(
                    repository=REPOSITORY,
                    requested_revision=REVISION,
                    local_path=model,
                )

    def test_requires_full_commit_for_unknown_model(self) -> None:
        with self.assertRaisesRegex(ValueError, "no pinned revision"):
            pinned_revision("example/private-model", None)
        with self.assertRaisesRegex(ValueError, "full 40-character"):
            pinned_revision("example/private-model", "main")
        self.assertEqual(pinned_revision("example/private-model", "c" * 40), "c" * 40)

    def test_identity_json_is_strict(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            model = self.model_directory(Path(directory))
            identity = build_model_identity(
                repository=REPOSITORY,
                requested_revision=REVISION,
                local_path=model,
            )
            self.assertNotIn("NaN", json.dumps(identity, allow_nan=False))


if __name__ == "__main__":
    unittest.main()
