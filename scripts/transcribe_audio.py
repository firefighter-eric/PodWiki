#!/usr/bin/env python3
"""Transcribe a local audio file to engine-native MLX Whisper JSON."""

from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path
from typing import Any


DEFAULT_MODEL = "mlx-community/whisper-large-v3-turbo-q4"


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
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as stream:
            json.dump(
                document,
                stream,
                ensure_ascii=False,
                indent=2,
                allow_nan=True,
            )
            stream.write("\n")
            temporary_path = Path(stream.name)
        temporary_path.replace(path)
        temporary_path = None
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def main() -> int:
    args = parse_args()
    input_path = args.input.resolve()
    output_path = args.output.resolve()
    if not input_path.is_file():
        raise FileNotFoundError(f"audio file does not exist: {input_path}")

    try:
        import mlx_whisper
    except ImportError as error:
        raise SystemExit(
            "mlx-whisper is unavailable; run this script with `uv run --group asr`"
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
