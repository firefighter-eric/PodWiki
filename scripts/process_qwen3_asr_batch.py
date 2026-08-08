#!/usr/bin/env python3
"""Process multiple cached PodWiki episodes with Qwen3-ASR, one subprocess each."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MLX_MODEL = "mlx-community/Qwen3-ASR-1.7B-8bit"
DEFAULT_MLX_ALIGNER = "mlx-community/Qwen3-ForcedAligner-0.6B-8bit"
DEFAULT_CUDA_MODEL = "Qwen/Qwen3-ASR-1.7B"
DEFAULT_CUDA_ALIGNER = "Qwen/Qwen3-ForcedAligner-0.6B"
TRANSCRIPT_LANGUAGE_RE = re.compile(r"^[A-Za-z]{2,3}(?:-[A-Za-z0-9]{2,8})*$")


@dataclass(frozen=True)
class BackendSettings:
    worker_name: str
    engine: str
    model: str
    aligner: str
    max_tokens: int
    chunk_duration: float


def resolve_backend_settings(
    backend: str,
    *,
    model: str | None,
    aligner: str | None,
    max_tokens: int | None,
    chunk_duration: float | None,
) -> BackendSettings:
    if backend == "mlx":
        return BackendSettings(
            worker_name="transcribe_qwen3_asr.py",
            engine="mlx-audio",
            model=model or DEFAULT_MLX_MODEL,
            aligner=aligner or DEFAULT_MLX_ALIGNER,
            max_tokens=max_tokens if max_tokens is not None else 4096,
            chunk_duration=(
                chunk_duration if chunk_duration is not None else 240.0
            ),
        )
    if backend == "cuda":
        return BackendSettings(
            worker_name="transcribe_qwen3_asr_cuda.py",
            engine="qwen-asr-transformers",
            model=model or DEFAULT_CUDA_MODEL,
            aligner=aligner or DEFAULT_CUDA_ALIGNER,
            max_tokens=max_tokens if max_tokens is not None else 2048,
            chunk_duration=(
                chunk_duration if chunk_duration is not None else 120.0
            ),
        )
    raise ValueError(f"unsupported ASR backend: {backend}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run resumable Qwen3-ASR processing for cached PodWiki episodes."
    )
    parser.add_argument(
        "--backend",
        choices=("mlx", "cuda"),
        default="mlx",
        help="Local inference backend; mlx remains the default",
    )
    parser.add_argument(
        "--episode",
        action="append",
        type=Path,
        help="Episode directory; repeat as needed. Defaults to every cached episode.",
    )
    parser.add_argument("--model")
    parser.add_argument("--model-path", type=Path)
    parser.add_argument("--aligner")
    parser.add_argument("--aligner-path", type=Path)
    parser.add_argument("--language", default="Chinese")
    parser.add_argument(
        "--transcript-language",
        default="zh-CN",
        help="BCP 47 language tag used in the rendered transcript filename",
    )
    parser.add_argument("--max-tokens", type=int)
    parser.add_argument("--chunk-duration", type=float)
    parser.add_argument("--max-sentence-characters", type=int, default=160)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument(
        "--dtype",
        choices=("float16", "bfloat16"),
        default="bfloat16",
    )
    parser.add_argument(
        "--attention-implementation",
        choices=("sdpa", "eager"),
        default="sdpa",
    )
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


def transcript_filename(language: str) -> str:
    if TRANSCRIPT_LANGUAGE_RE.fullmatch(language) is None:
        raise ValueError(f"invalid transcript language tag: {language!r}")
    return f"transcript.{language}.md"


def validate_local_model_path(path: Path, *, label: str) -> Path:
    resolved = path if path.is_absolute() else ROOT / path
    resolved = resolved.resolve()
    if not resolved.is_dir():
        raise FileNotFoundError(f"local {label} directory does not exist: {resolved}")
    if not (resolved / "config.json").is_file():
        raise FileNotFoundError(f"local {label} has no config.json: {resolved}")
    if not any(resolved.glob("*.safetensors")):
        raise FileNotFoundError(f"local {label} has no safetensors weights: {resolved}")
    return resolved


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
        stderr=subprocess.PIPE,
        check=False,
    )
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as stream:
        stream.write(f"\n[{utc_now()}] {' '.join(command)}\n")
        stream.write(completed.stdout)
        if completed.stdout and not completed.stdout.endswith("\n"):
            stream.write("\n")
        if completed.stderr:
            stream.write("[stderr]\n")
            stream.write(completed.stderr)
            if not completed.stderr.endswith("\n"):
                stream.write("\n")
        stream.write(f"exit_code={completed.returncode}\n")
    return completed, parse_json_output(completed.stdout)


def main() -> int:
    args = parse_args()
    backend = resolve_backend_settings(
        args.backend,
        model=args.model,
        aligner=args.aligner,
        max_tokens=args.max_tokens,
        chunk_duration=args.chunk_duration,
    )
    rendered_transcript_name = transcript_filename(args.transcript_language)
    episodes = discover_episode_dirs(args.episode)
    if not episodes:
        raise SystemExit("no cached episodes were found")

    environment = os.environ.copy()
    if args.backend == "mlx":
        environment.setdefault("HF_ENDPOINT", "https://hf-mirror.com")
    if args.model_path is not None and args.aligner_path is not None:
        environment["HF_HUB_OFFLINE"] = "1"
        environment["TRANSFORMERS_OFFLINE"] = "1"
    environment.setdefault("UV_CACHE_DIR", str(ROOT / ".cache" / "uv"))

    model_path = (
        validate_local_model_path(args.model_path, label="model")
        if args.model_path is not None
        else None
    )
    aligner_path = (
        validate_local_model_path(args.aligner_path, label="aligner")
        if args.aligner_path is not None
        else None
    )

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
            transcript_path = run_dir / rendered_transcript_name
            log_path = (
                ROOT
                / ".cache"
                / "logs"
                / "qwen3-asr"
                / f"{episode_dir.parent.parent.name}--{episode_dir.name}.log"
            )

            transcribe_command = [
                sys.executable,
                str(ROOT / "scripts" / backend.worker_name),
                "--input",
                repository_argument(audio_path),
                "--output",
                repository_argument(raw_path),
                "--aligned-output",
                repository_argument(aligned_path),
                "--model",
                backend.model,
                "--aligner",
                backend.aligner,
                "--language",
                args.language,
                "--max-tokens",
                str(backend.max_tokens),
                "--chunk-duration",
                str(backend.chunk_duration),
                "--max-sentence-characters",
                str(args.max_sentence_characters),
                "--no-verbose",
            ]
            if args.backend == "cuda":
                transcribe_command.extend(
                    [
                        "--device",
                        args.device,
                        "--dtype",
                        args.dtype,
                        "--attention-implementation",
                        args.attention_implementation,
                    ]
                )
            if model_path is not None:
                transcribe_command.extend(
                    ["--model-path", repository_argument(model_path)]
                )
            if aligner_path is not None:
                transcribe_command.extend(
                    ["--aligner-path", repository_argument(aligner_path)]
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
                    backend.engine,
                    "--model",
                    backend.model,
                    "--language",
                    args.transcript_language,
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

    print(json.dumps({"episodes": results}, ensure_ascii=True, indent=2))
    return 1 if any(result["status"] == "failed" for result in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
