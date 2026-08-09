#!/usr/bin/env python3
"""Pinned model identities shared by the local Qwen ASR workers."""

from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
from pathlib import Path, PurePosixPath
from typing import Any


LINEAGE_SCHEMA_VERSION = 2
MODEL_IDENTITY_SCHEMA_VERSION = 1
FULL_COMMIT_RE = re.compile(r"[0-9a-f]{40}")
SHA256_RE = re.compile(r"[0-9a-f]{64}")
PINNED_MODEL_REVISIONS = {
    "mlx-community/Qwen3-ASR-1.7B-8bit": "a8379a2e2f9e313c9292cdf1af4055ab56d50d55",
    "mlx-community/Qwen3-ForcedAligner-0.6B-8bit": "0e1a68e91d815300c7c9754b2a7639378b23db15",
    "Qwen/Qwen3-ASR-1.7B": "7278e1e70fe206f11671096ffdd38061171dd6e5",
    "Qwen/Qwen3-ForcedAligner-0.6B": "c7cbfc2048c462b0d63a45797104fc9db3ad62b7",
}
IDENTITY_CACHE_NAME = ".podwiki-model-identity-v1.json"
def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def pinned_revision(repository: str, requested_revision: str | None) -> str:
    revision = requested_revision or PINNED_MODEL_REVISIONS.get(repository)
    if revision is None:
        raise ValueError(
            f"model {repository!r} has no pinned revision; pass a full 40-character commit"
        )
    revision = revision.lower()
    if FULL_COMMIT_RE.fullmatch(revision) is None:
        raise ValueError(
            f"model revision for {repository!r} must be a full 40-character commit"
        )
    return revision


def _read_huggingface_metadata(
    model_path: Path,
) -> dict[str, tuple[str, str]]:
    metadata_root = model_path / ".cache" / "huggingface" / "download"
    if not metadata_root.is_dir():
        return {}
    metadata: dict[str, tuple[str, str]] = {}
    for metadata_path in sorted(metadata_root.rglob("*.metadata")):
        try:
            lines = metadata_path.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeError, IndexError) as error:
            raise ValueError(f"invalid Hugging Face metadata: {metadata_path}") from error
        if len(lines) < 2:
            raise ValueError(f"invalid Hugging Face metadata: {metadata_path}")
        commit = lines[0].lower()
        if FULL_COMMIT_RE.fullmatch(commit) is None:
            raise ValueError(f"invalid Hugging Face commit in {metadata_path}: {commit!r}")
        etag = lines[1].strip().removeprefix('W/').strip('"').lower()
        if re.fullmatch(r"(?:[0-9a-f]{40}|[0-9a-f]{64})", etag) is None:
            raise ValueError(f"invalid Hugging Face etag in {metadata_path}: {etag!r}")
        metadata_relative = metadata_path.relative_to(metadata_root).as_posix()
        logical_path = metadata_relative.removesuffix(".metadata")
        if logical_path in metadata:
            raise ValueError(f"duplicate Hugging Face metadata for {logical_path}")
        metadata[logical_path] = (commit, etag)
    return metadata


def _strict_json(path: Path) -> dict[str, Any]:
    def reject_constant(value: str) -> None:
        raise ValueError(f"non-finite number {value}")

    document = json.loads(
        path.read_text(encoding="utf-8"),
        parse_constant=reject_constant,
    )
    if not isinstance(document, dict):
        raise ValueError(f"JSON root must be an object: {path}")
    return document


def _safe_logical_path(value: str) -> PurePosixPath:
    logical = PurePosixPath(value)
    if (
        logical.is_absolute()
        or not logical.parts
        or any(part in {"", ".", ".."} for part in logical.parts)
        or "\\" in value
        or re.match(r"^[A-Za-z]:", value) is not None
    ):
        raise ValueError(f"model file path must be repository-relative: {value!r}")
    return logical


def _critical_model_files(model_path: Path) -> list[tuple[str, Path]]:
    config_path = model_path / "config.json"
    if not config_path.is_file():
        raise FileNotFoundError(f"local model has no config.json: {model_path}")

    files: dict[str, Path] = {}
    for path in sorted(model_path.rglob("*")):
        relative = path.relative_to(model_path)
        if not relative.parts or relative.parts[0] == ".cache":
            continue
        if relative.name.startswith(".podwiki-model-identity"):
            continue
        if path.is_file():
            logical_name = PurePosixPath(*relative.parts).as_posix()
            _safe_logical_path(logical_name)
            files[logical_name] = path
    index_path = model_path / "model.safetensors.index.json"
    if index_path.is_file():
        index = _strict_json(index_path)
        weight_map = index.get("weight_map")
        if not isinstance(weight_map, dict) or not weight_map:
            raise ValueError(f"model weight index has no weight_map: {index_path}")
        for filename in weight_map.values():
            if not isinstance(filename, str) or not filename.endswith(".safetensors"):
                raise ValueError(f"model weight index has an invalid filename: {filename!r}")
            logical = _safe_logical_path(filename)
            logical_name = logical.as_posix()
            weight_path = model_path.joinpath(*logical.parts)
            if not weight_path.is_file():
                raise FileNotFoundError(f"model weight is missing: {weight_path}")
            if logical_name not in files:
                raise ValueError(
                    f"model weight is outside the downloaded payload: {logical_name}"
                )
            files[logical_name] = weight_path
    else:
        weights = sorted(
            path for logical_name, path in files.items()
            if logical_name.endswith(".safetensors")
        )
        if not weights:
            raise FileNotFoundError(f"local model has no safetensors weights: {model_path}")
    return sorted(files.items())


def _is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def _trusted_huggingface_roots(model_path: Path) -> tuple[Path, ...]:
    roots = {model_path.resolve()}
    hf_hub_cache = os.environ.get("HF_HUB_CACHE")
    if hf_hub_cache:
        roots.add(Path(hf_hub_cache).expanduser().resolve())
    hf_home = Path(
        os.environ.get("HF_HOME", Path.home() / ".cache" / "huggingface")
    ).expanduser()
    roots.add((hf_home / "hub").resolve())
    return tuple(sorted(roots, key=lambda path: path.as_posix()))


def _validate_file_target(*, logical_path: str, path: Path, model_path: Path) -> None:
    if not path.is_symlink():
        return
    try:
        target = path.resolve(strict=True)
    except OSError as error:
        raise ValueError(f"broken model symlink for {logical_path}: {path}") from error
    if not any(
        _is_within(target, root)
        for root in _trusted_huggingface_roots(model_path)
    ):
        raise ValueError(
            f"model symlink for {logical_path} targets an untrusted path: {target}"
        )


def _file_digests(path: Path) -> tuple[str, str]:
    size = path.stat().st_size
    sha256 = hashlib.sha256()
    git_sha1 = hashlib.sha1()
    git_sha1.update(f"blob {size}\0".encode("ascii"))
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            sha256.update(chunk)
            git_sha1.update(chunk)
    return sha256.hexdigest(), git_sha1.hexdigest()


def _write_json_atomically(path: Path, document: dict[str, Any]) -> None:
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="\n",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as stream:
            json.dump(document, stream, ensure_ascii=False, indent=2, allow_nan=False)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
            temporary_path = Path(stream.name)
        temporary_path.replace(path)
        temporary_path = None
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def build_model_identity(
    *, repository: str, requested_revision: str | None, local_path: Path
) -> dict[str, Any]:
    revision = pinned_revision(repository, requested_revision)
    model_path = local_path.expanduser().absolute()
    if not model_path.is_dir():
        raise FileNotFoundError(f"local model directory does not exist: {model_path}")

    critical_files = _critical_model_files(model_path)
    metadata = _read_huggingface_metadata(model_path)
    if not metadata:
        raise ValueError(
            f"local model has no Hugging Face download metadata: {model_path}; "
            "download it with `hf download --revision <full-commit> --local-dir ...`"
        )
    metadata_commits = {commit for commit, _etag in metadata.values()}
    if metadata_commits != {revision}:
        raise ValueError(
            f"local model commit mismatch for {repository!r}: "
            f"expected={revision}, metadata={sorted(metadata_commits)}"
        )
    missing_metadata = [
        logical_path
        for logical_path, _path in critical_files
        if logical_path not in metadata
    ]
    if missing_metadata:
        raise ValueError(
            "critical model files have no Hugging Face download metadata: "
            + ", ".join(missing_metadata)
        )

    files_sha256: dict[str, str] = {}
    cache_entries: dict[str, dict[str, Any]] = {}
    for logical_path, path in critical_files:
        _validate_file_target(
            logical_path=logical_path,
            path=path,
            model_path=model_path,
        )
        digest, git_digest = _file_digests(path)
        _commit, etag = metadata[logical_path]
        expected_etag = digest if len(etag) == 64 else git_digest
        if etag != expected_etag:
            raise ValueError(
                f"Hugging Face etag does not match critical model file {logical_path}"
            )
        files_sha256[logical_path] = digest
        cache_entries[logical_path] = {
            "size_bytes": path.stat().st_size,
            "etag": etag,
            "sha256": digest,
        }

    cache_path = model_path / IDENTITY_CACHE_NAME
    cache_document = {
        "schema_version": MODEL_IDENTITY_SCHEMA_VERSION,
        "repository": repository,
        "resolved_commit": revision,
        "files": cache_entries,
    }
    cached: dict[str, Any] | None = None
    if cache_path.is_file():
        try:
            cached = _strict_json(cache_path)
        except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
            cached = None
    if cached != cache_document:
        _write_json_atomically(
            cache_path,
            cache_document,
        )

    return {
        "schema_version": MODEL_IDENTITY_SCHEMA_VERSION,
        "repository": repository,
        "requested_revision": revision,
        "resolved_commit": revision,
        "files_sha256": files_sha256,
    }


def validate_model_identity(identity: Any, *, label: str) -> dict[str, Any]:
    if not isinstance(identity, dict):
        raise ValueError(f"{label} has no valid model identity")
    expected_fields = {
        "schema_version",
        "repository",
        "requested_revision",
        "resolved_commit",
        "files_sha256",
    }
    if set(identity) != expected_fields:
        raise ValueError(f"{label} model identity fields do not match schema version 1")
    if type(identity.get("schema_version")) is not int or identity["schema_version"] != 1:
        raise ValueError(f"{label} has no valid model identity schema_version")
    for field in ("requested_revision", "resolved_commit"):
        if FULL_COMMIT_RE.fullmatch(str(identity.get(field, ""))) is None:
            raise ValueError(f"{label} model identity has invalid {field}")
    if identity["requested_revision"] != identity["resolved_commit"]:
        raise ValueError(f"{label} requested and resolved model revisions differ")
    if not isinstance(identity.get("repository"), str) or not identity["repository"]:
        raise ValueError(f"{label} model identity has no repository")
    files = identity.get("files_sha256")
    if not isinstance(files, dict) or not files or "config.json" not in files:
        raise ValueError(f"{label} model identity has no critical file hashes")
    if not any(str(path).endswith(".safetensors") for path in files):
        raise ValueError(f"{label} model identity has no weight hash")
    for path, digest in files.items():
        if not isinstance(path, str):
            raise ValueError(f"{label} model identity has an invalid file path")
        try:
            _safe_logical_path(path)
        except ValueError as error:
            raise ValueError(
                f"{label} model identity has an invalid file path"
            ) from error
        if not isinstance(digest, str) or SHA256_RE.fullmatch(digest) is None:
            raise ValueError(f"{label} model identity has an invalid file hash")
    return identity


def require_requested_identity(
    identity: Any, *, repository: str, requested_revision: str | None, label: str
) -> dict[str, Any]:
    validated = validate_model_identity(identity, label=label)
    revision = pinned_revision(repository, requested_revision)
    if validated["repository"] != repository:
        raise ValueError(f"{label} repository does not match the requested model")
    if validated["requested_revision"] != revision:
        raise ValueError(f"{label} revision does not match the pinned revision")
    return validated
