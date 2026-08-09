#!/usr/bin/env python3
"""Transcribe a local audio file to engine-native MLX Whisper JSON."""

from __future__ import annotations

import argparse
import json
import os
import tempfile
from pathlib import Path
from typing import Any


DEFAULT_MODEL = "mlx-community/whisper-large-v3-turbo-q4"
PROJECT_ROOT = Path(__file__).resolve().parents[1]
BENCHMARK_ROOT = PROJECT_ROOT / ".cache" / "benchmarks"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run MLX Whisper locally and save its raw JSON result."
    )
    parser.add_argument("--input", required=True, type=Path, help="Local audio file")
    parser.add_argument("--output", required=True, type=Path, help="Raw ASR JSON")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--language", default="zh")
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument(
        "--clip-timestamps",
        default="0",
        help="Optional Whisper clip range, for example 0,30",
    )
    parser.add_argument(
        "--initial-prompt",
        help="Optional vocabulary prompt containing names and technical terms",
    )
    parser.add_argument(
        "--verbose",
        action=argparse.BooleanOptionalAction,
        default=True,
    )
    return parser.parse_args()


def write_json_atomically(path: Path, document: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
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
            temporary_path = Path(stream.name)
            json.dump(
                document,
                stream,
                ensure_ascii=False,
                indent=2,
                allow_nan=False,
            )
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        temporary_path.replace(path)
        temporary_path = None
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def validate_benchmark_output(path: Path) -> Path:
    resolved = path.resolve()
    try:
        relative = resolved.relative_to(BENCHMARK_ROOT.resolve())
    except ValueError as error:
        raise ValueError(
            "new MLX Whisper output must stay under .cache/benchmarks"
        ) from error
    if not relative.parts or resolved.suffix != ".json":
        raise ValueError("MLX Whisper output must be a JSON file under .cache/benchmarks")
    return resolved


def main() -> int:
    args = parse_args()
    input_path = args.input.resolve()
    output_path = validate_benchmark_output(args.output)
    if not input_path.is_file():
        raise FileNotFoundError(f"audio file does not exist: {input_path}")
    if input_path == output_path:
        raise ValueError("input audio and Whisper output paths must be distinct")

    try:
        import mlx_whisper
    except ImportError as error:
        raise SystemExit(
            "mlx-whisper is unavailable; install the project with `uv sync --extra asr`"
        ) from error

    result = mlx_whisper.transcribe(
        str(input_path),
        path_or_hf_repo=args.model,
        language=args.language,
        temperature=args.temperature,
        clip_timestamps=args.clip_timestamps,
        initial_prompt=args.initial_prompt,
        verbose=args.verbose,
    )
    if not isinstance(result, dict) or not isinstance(result.get("segments"), list):
        raise ValueError("mlx-whisper returned an unexpected result")
    try:
        json.dumps(result, allow_nan=False)
    except (TypeError, ValueError) as error:
        raise ValueError("mlx-whisper returned non-strict JSON data") from error

    write_json_atomically(output_path, result)
    print(
        json.dumps(
            {
                "input": input_path.as_posix(),
                "output": output_path.as_posix(),
                "model": args.model,
                "language": result.get("language"),
                "temperature": args.temperature,
                "segments": len(result["segments"]),
                "characters": len(result.get("text", "")),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
