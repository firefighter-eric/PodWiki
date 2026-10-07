"""Create the ignored project link before downloading shared model weights."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def setup_shared_models(local: Path, shared: Path) -> Path:
    local = local.parent.resolve() / local.name
    shared = shared.expanduser().resolve()
    if shared == local or shared.is_relative_to(local):
        raise ValueError("Shared models must be outside the project model directory")
    if local.is_symlink() or local.is_junction():
        if local.exists() and local.samefile(shared):
            return shared
        raise ValueError("Existing model link points elsewhere; inspect it before changing it")
    if local.exists() and not local.is_dir():
        raise ValueError("Project model path is not a directory")
    local.parent.mkdir(parents=True, exist_ok=True)
    shared.parent.mkdir(parents=True, exist_ok=True)
    moved = False
    removed_empty = False
    if local.exists():
        if shared.exists():
            if not shared.is_dir() or any(local.iterdir()):
                raise ValueError("Both model locations exist; inspect and reconcile them without overwriting")
            local.rmdir()
            removed_empty = True
        else:
            # Same-filesystem rename preserves metadata and all internal links.
            # Cross-filesystem moves fail rather than copying/deleting weights.
            local.rename(shared)
            moved = True
    else:
        shared.mkdir(exist_ok=True)
    try:
        try:
            local.symlink_to(shared, target_is_directory=True)
        except OSError:
            if os.name != "nt":
                raise
            subprocess.run(
                ["cmd", "/c", "mklink", "/J", str(local), str(shared)],
                check=True,
                capture_output=True,
                text=True,
            )
        if not local.samefile(shared):
            raise RuntimeError("Model link verification failed")
    except Exception:
        if not local.exists() and not local.is_symlink() and not local.is_junction():
            if moved:
                shared.rename(local)
            elif removed_empty:
                local.mkdir()
        raise
    return shared


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--shared-root", type=Path, default=Path.home() / "Models" / "PodWiki")
    args = parser.parse_args()
    shared = setup_shared_models(ROOT / ".cache" / "models", args.shared_root)
    print(f"Shared model directory: {shared}")
    print(f"Project model link: {ROOT / '.cache' / 'models'}")


if __name__ == "__main__":
    main()
