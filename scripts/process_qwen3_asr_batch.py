#!/usr/bin/env python3
"""Process multiple cached PodWiki episodes with Qwen3-ASR, one subprocess each."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODEL = "mlx-community/Qwen3-ASR-1.7B-8bit"
DEFAULT_ALIGNER = "mlx-community/Qwen3-ForcedAligner-0.6B-8bit"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run resumable Qwen3-ASR processing for cached PodWiki episodes."
    )
    parser.add_argument(
        "--episode",
        action="append",
        type=Path,
        help="Episode directory; repeat as needed. Defaults to every cached episode.",
    )
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--model-path", type=Path)
    parser.add_argument("--aligner", default=DEFAULT_ALIGNER)
    parser.add_argument("--aligner-path", type=Path)
    parser.add_argument("--language", default="Chinese")
    parser.add_argument("--max-tokens", type=int, default=4096)
    parser.add_argument("--chunk-duration", type=float, default=240.0)
    parser.add_argument("--max-sentence-characters", type=int, default=160)
    parser.add_argument("--skip-render", action="store_true")
    replacement = parser.add_mutually_exclusive_group()
    replacement.add_argument("--retranscribe", action="store_true")
    replacement.add_argument("--realign", action="store_true")
    return parser.parse_args()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def decode_front_matter_scalar(value: str) -> str:
    value = value.strip()
    if value.startswith('"'):
        parsed = json.loads(value)
        if not isinstance(parsed, str):
            raise ValueError(f"front matter value is not text: {value}")
        return parsed
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")
    return value


def read_episode_identity(episode_dir: Path) -> tuple[str, str]:
    readme = episode_dir / "README.md"
    if not readme.is_file():
        raise FileNotFoundError(f"episode README does not exist: {readme}")
    text = readme.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) != 3:
        raise ValueError(f"episode README has no YAML front matter: {readme}")
    values: dict[str, str] = {}
    for line in parts[1].splitlines():
        if line.startswith(("id:", "title:")):
            key, _, value = line.partition(":")
            values[key] = decode_front_matter_scalar(value)
    if not values.get("id") or not values.get("title"):
        raise ValueError(f"episode README is missing id or title: {readme}")
    return values["id"], values["title"]


def cached_audio_path(episode_dir: Path) -> Path:
    resolved = episode_dir.resolve()
    try:
        relative = resolved.relative_to((ROOT / "shows").resolve())
    except ValueError as error:
        raise ValueError(f"episode is outside the shows directory: {episode_dir}") from error
    if len(relative.parts) != 3 or relative.parts[1] != "episodes":
        raise ValueError(f"unexpected episode directory layout: {episode_dir}")
    show_id, _, episode_folder = relative.parts
    return ROOT / ".cache" / "media" / show_id / episode_folder / "source.m4a"


def repository_argument(path: Path) -> str:
    """Return a portable repository-relative CLI argument when possible."""
    resolved = path.resolve()
    try:
        return resolved.relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return resolved.as_posix()


def validate_local_model_path(path: Path, *, label: str) -> None:
    resolved = path if path.is_absolute() else ROOT / path
    resolved = resolved.resolve()
    if not resolved.is_dir():
        raise FileNotFoundError(f"local {label} directory does not exist: {resolved}")
    if not (resolved / "config.json").is_file():
        raise FileNotFoundError(f"local {label} has no config.json: {resolved}")
    if not any(resolved.glob("*.safetensors")):
        raise FileNotFoundError(f"local {label} has no safetensors weights: {resolved}")


def discover_episode_dirs(explicit: list[Path] | None) -> list[Path]:
    if explicit:
        return sorted({path.resolve() for path in explicit})
    discovered: list[Path] = []
    for episode_dir in sorted((ROOT / "shows").glob("*/episodes/*")):
        if episode_dir.is_dir() and cached_audio_path(episode_dir).is_file():
            discovered.append(episode_dir.resolve())
    return discovered


def parse_json_output(output: str) -> dict[str, Any]:
    stripped = output.strip()
    if not stripped:
        return {}
    try:
        document = json.loads(stripped)
    except json.JSONDecodeError:
        return {}
    return document if isinstance(document, dict) else {}


def run_logged(
    *, command: list[str], environment: dict[str, str], log_path: Path
) -> tuple[subprocess.CompletedProcess[str], dict[str, Any]]:
    completed = subprocess.run(
        command,
        cwd=ROOT,
        env=environment,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as stream:
        stream.write(f"\n[{utc_now()}] {' '.join(command)}\n")
        stream.write(completed.stdout)
        if completed.stdout and not completed.stdout.endswith("\n"):
            stream.write("\n")
        stream.write(f"exit_code={completed.returncode}\n")
    return completed, parse_json_output(completed.stdout)


def main() -> int:
    args = parse_args()
    episodes = discover_episode_dirs(args.episode)
    if not episodes:
        raise SystemExit("no cached episodes were found")

    environment = os.environ.copy()
    environment.setdefault("HF_ENDPOINT", "https://hf-mirror.com")
    if args.model_path is not None and args.aligner_path is not None:
        environment.setdefault("HF_HUB_OFFLINE", "1")
    environment.setdefault("UV_CACHE_DIR", str(ROOT / ".cache" / "uv"))

    if args.model_path is not None:
        validate_local_model_path(args.model_path, label="model")
    if args.aligner_path is not None:
        validate_local_model_path(args.aligner_path, label="aligner")

    results: list[dict[str, Any]] = []
    for index, episode_dir in enumerate(episodes, start=1):
        label = f"{episode_dir.parent.parent.name}/{episode_dir.name}"
        print(f"[{index}/{len(episodes)}] START {label}", flush=True)
        try:
            episode_id, title = read_episode_identity(episode_dir)
            audio_path = cached_audio_path(episode_dir)
            if not audio_path.is_file():
                raise FileNotFoundError(f"cached audio does not exist: {audio_path}")

            run_dir = episode_dir / "asr" / "qwen3-asr"
            raw_path = run_dir / "raw.json"
            aligned_path = run_dir / "aligned.json"
            refined_path = run_dir / "refined.json"
            transcript_path = run_dir / "transcript.zh-CN.md"
            log_path = (
                ROOT
                / ".cache"
                / "logs"
                / "qwen3-asr"
                / f"{episode_dir.parent.parent.name}--{episode_dir.name}.log"
            )

            transcribe_command = [
                sys.executable,
                str(ROOT / "scripts" / "transcribe_qwen3_asr.py"),
                "--input",
                repository_argument(audio_path),
                "--output",
                repository_argument(raw_path),
                "--aligned-output",
                repository_argument(aligned_path),
                "--model",
                args.model,
                "--aligner",
                args.aligner,
                "--language",
                args.language,
                "--max-tokens",
                str(args.max_tokens),
                "--chunk-duration",
                str(args.chunk_duration),
                "--max-sentence-characters",
                str(args.max_sentence_characters),
                "--no-verbose",
            ]
            if args.model_path is not None:
                transcribe_command.extend(
                    ["--model-path", repository_argument(args.model_path)]
                )
            if args.aligner_path is not None:
                transcribe_command.extend(
                    ["--aligner-path", repository_argument(args.aligner_path)]
                )
            if args.retranscribe:
                transcribe_command.append("--retranscribe")
            elif args.realign:
                transcribe_command.append("--realign")

            transcribe, transcribe_output = run_logged(
                command=transcribe_command,
                environment=environment,
                log_path=log_path,
            )
            if transcribe.returncode != 0:
                raise RuntimeError(
                    f"Qwen worker failed; inspect {log_path.relative_to(ROOT)}"
                )

            render_output: dict[str, Any] = {}
            if not args.skip_render:
                render_command = [
                    sys.executable,
                    str(ROOT / "scripts" / "render_asr_transcript.py"),
                    "--input",
                    repository_argument(aligned_path),
                    "--refined-output",
                    repository_argument(refined_path),
                    "--output",
                    repository_argument(transcript_path),
                    "--episode-id",
                    episode_id,
                    "--title",
                    title,
                    "--engine",
                    "mlx-audio",
                    "--model",
                    args.model,
                ]
                rendered, render_output = run_logged(
                    command=render_command,
                    environment=environment,
                    log_path=log_path,
                )
                if rendered.returncode != 0:
                    raise RuntimeError(
                        f"renderer failed; inspect {log_path.relative_to(ROOT)}"
                    )

            result = {
                "episode": label,
                "status": transcribe_output.get("status", "completed"),
                "chunks": transcribe_output.get("chunks"),
                "sentence_segments": transcribe_output.get("sentence_segments"),
                "rendered_lines": render_output.get("rendered_lines"),
                "log": str(log_path.relative_to(ROOT)),
            }
            results.append(result)
            print(f"[{index}/{len(episodes)}] DONE {label}", flush=True)
        except Exception as error:
            results.append(
                {
                    "episode": label,
                    "status": "failed",
                    "error": str(error),
                }
            )
            print(f"[{index}/{len(episodes)}] FAILED {label}: {error}", flush=True)

    print(json.dumps({"episodes": results}, ensure_ascii=False, indent=2))
    return 1 if any(result["status"] == "failed" for result in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
