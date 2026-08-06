#!/usr/bin/env python3
"""Validate PodWiki content, source URLs, and complete Qwen ASR chains."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SHOWS_ROOT = ROOT / "shows"
BILIBILI_URL_RE = re.compile(
    r"https://www\.bilibili\.com/video/[^\s)\]\"']+"
)
CANONICAL_BILIBILI_URL_RE = re.compile(
    r"https://www\.bilibili\.com/video/BV[A-Za-z0-9]+/"
)
TRACKING_PARAMETERS = ("spm_id_from", "vd_source")
QWEN_ARTIFACT_NAMES = (
    "raw.json",
    "aligned.json",
    "refined.json",
    "transcript.zh-CN.md",
)
SHA256_RE = re.compile(r"[0-9a-f]{64}")
TRANSCRIPT_LINE_RE = re.compile(r"^\[\d{2,}:\d{2}:\d{2}\] \S.*  $")


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def display_path(path: Path, repository_root: Path) -> str:
    try:
        return path.relative_to(repository_root).as_posix()
    except ValueError:
        return str(path)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate object key {key!r}")
        result[key] = value
    return result


def reject_non_finite_number(value: str) -> None:
    raise ValueError(f"non-finite number {value}")


def read_json_strict(
    path: Path,
    *,
    repository_root: Path,
    errors: list[str],
) -> dict[str, Any] | None:
    try:
        text = path.read_text(encoding="utf-8")
        document = json.loads(
            text,
            object_pairs_hook=reject_duplicate_keys,
            parse_constant=reject_non_finite_number,
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as error:
        errors.append(
            f"{display_path(path, repository_root)} is not strict JSON: {error}"
        )
        return None

    if not isinstance(document, dict):
        errors.append(
            f"{display_path(path, repository_root)} JSON root must be an object"
        )
        return None
    return document


def extract_front_matter_lines(text: str) -> list[str]:
    if not text.startswith("---\n"):
        return []
    closing = text.find("\n---\n", 4)
    if closing < 0:
        return []
    return text[4:closing].splitlines()


def decode_yaml_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value.startswith('"') and value.endswith('"'):
        try:
            decoded = json.loads(value)
        except json.JSONDecodeError:
            return value
        return decoded if isinstance(decoded, str) else value
    if len(value) >= 2 and value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")
    return value


def nested_front_matter_scalar(
    lines: list[str], section: str, key: str
) -> str | None:
    in_section = False
    for line in lines:
        stripped = line.strip()
        indent = len(line) - len(line.lstrip(" "))
        if not in_section:
            if indent == 0 and stripped == f"{section}:":
                in_section = True
            continue
        if stripped and indent == 0:
            break
        if indent == 2 and stripped.startswith(f"{key}:"):
            return decode_yaml_scalar(stripped.split(":", 1)[1])
    return None


def parse_asr_runs(lines: list[str]) -> list[dict[str, Any]]:
    runs: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    nested_section: str | None = None
    in_runs = False

    for line in lines:
        stripped = line.strip()
        indent = len(line) - len(line.lstrip(" "))
        if not in_runs:
            if indent == 0 and stripped == "asr_runs:":
                in_runs = True
            continue
        if stripped and indent == 0:
            break
        if not stripped or stripped.startswith("#"):
            continue

        if indent == 2 and stripped.startswith("- "):
            current = {}
            runs.append(current)
            nested_section = None
            item = stripped[2:]
            if ":" in item:
                key, value = item.split(":", 1)
                current[key.strip()] = decode_yaml_scalar(value)
            continue
        if current is None:
            continue
        if indent == 4 and ":" in stripped:
            key, value = stripped.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value:
                current[key] = decode_yaml_scalar(value)
                nested_section = None
            else:
                current[key] = {}
                nested_section = key
            continue
        if indent == 6 and nested_section and ":" in stripped:
            key, value = stripped.split(":", 1)
            nested = current.get(nested_section)
            if isinstance(nested, dict):
                nested[key.strip()] = decode_yaml_scalar(value)

    return runs


def is_qwen_run(run: dict[str, Any]) -> bool:
    values: list[str] = []
    for key in ("id", "engine", "model", "aligner"):
        value = run.get(key)
        if isinstance(value, str):
            values.append(value)
    artifacts = run.get("artifacts")
    if isinstance(artifacts, dict):
        values.extend(value for value in artifacts.values() if isinstance(value, str))
    return any("qwen" in value.lower() for value in values)


def safe_recorded_path(
    value: Any,
    *,
    base: Path,
    repository_root: Path,
    field: str,
    errors: list[str],
) -> Path | None:
    if not isinstance(value, str) or not value:
        errors.append(f"{field} must be a non-empty relative path")
        return None
    if "\\" in value or re.match(r"^[A-Za-z]:", value):
        errors.append(f"{field} must use a repository-relative POSIX path: {value!r}")
        return None

    parts = value.split("/")
    pure = PurePosixPath(value)
    if pure.is_absolute() or any(part in ("", ".", "..") for part in parts):
        errors.append(f"{field} must use a repository-relative POSIX path: {value!r}")
        return None

    path = base.joinpath(*parts)
    try:
        path.resolve(strict=False).relative_to(repository_root.resolve())
    except ValueError:
        errors.append(f"{field} escapes the repository: {value!r}")
        return None
    return path


def check_recorded_path(
    value: Any,
    *,
    base: Path,
    expected: Path,
    repository_root: Path,
    field: str,
    errors: list[str],
) -> Path | None:
    path = safe_recorded_path(
        value,
        base=base,
        repository_root=repository_root,
        field=field,
        errors=errors,
    )
    if path is not None and path != expected:
        errors.append(
            f"{field} must point to {display_path(expected, repository_root)}, "
            f"not {value!r}"
        )
    return path


def mapping_value(
    document: dict[str, Any], mapping: str, key: str, *, field: str, errors: list[str]
) -> Any:
    value = document.get(mapping)
    if not isinstance(value, dict):
        errors.append(f"{field.rsplit('.', 1)[0]} must be an object")
        return None
    if key not in value:
        errors.append(f"{field} is missing")
        return None
    return value[key]


def valid_sha256(value: Any, *, field: str, errors: list[str]) -> str | None:
    if not isinstance(value, str) or SHA256_RE.fullmatch(value) is None:
        errors.append(f"{field} must be a lowercase SHA-256 digest")
        return None
    return value


def validate_qwen_chain(
    episode_dir: Path,
    *,
    repository_root: Path,
    readme_text: str,
    errors: list[str],
) -> bool:
    """Validate one complete chain; intentional raw/aligned checkpoints are skipped."""

    qwen_dir = episode_dir / "asr" / "qwen3-asr"
    paths = {name: qwen_dir / name for name in QWEN_ARTIFACT_NAMES}
    front_matter = extract_front_matter_lines(readme_text)
    qwen_runs = [run for run in parse_asr_runs(front_matter) if is_qwen_run(run)]
    selected_runs = [
        run
        for run in qwen_runs
        if str(run.get("selection_status", "")).lower() == "selected"
    ]
    missing = [name for name, path in paths.items() if not path.is_file()]
    if missing:
        if selected_runs:
            errors.append(
                f"{display_path(episode_dir, repository_root)} marks Qwen selected "
                f"but its artifact chain is incomplete: {', '.join(missing)}"
            )
        return False

    raw_path = paths["raw.json"]
    aligned_path = paths["aligned.json"]
    refined_path = paths["refined.json"]
    transcript_path = paths["transcript.zh-CN.md"]
    raw = read_json_strict(raw_path, repository_root=repository_root, errors=errors)
    aligned = read_json_strict(
        aligned_path, repository_root=repository_root, errors=errors
    )
    refined = read_json_strict(
        refined_path, repository_root=repository_root, errors=errors
    )
    if raw is None or aligned is None or refined is None:
        return True

    raw_sha = sha256_file(raw_path)
    aligned_sha = sha256_file(aligned_path)
    transcript_sha = sha256_file(transcript_path)
    transcript_text = transcript_path.read_text(encoding="utf-8")
    transcript_lines = transcript_text.splitlines()
    if (
        len(transcript_lines) < 2
        or not transcript_lines[0].startswith("# ")
        or transcript_lines[1] != ""
    ):
        errors.append("Qwen transcript must start with a level-one title and blank line")
    rendered_lines = transcript_lines[2:]
    for index, line in enumerate(rendered_lines, start=3):
        if TRANSCRIPT_LINE_RE.fullmatch(line) is None:
            errors.append(
                f"Qwen transcript line {index} must be one timestamped sentence "
                "with a Markdown hard break"
            )
            break
    statistics = refined.get("statistics")
    if not isinstance(statistics, dict):
        errors.append("refined.statistics must be an object")
    else:
        recorded_rendered_lines = statistics.get("rendered_lines")
        if (
            isinstance(recorded_rendered_lines, bool)
            or not isinstance(recorded_rendered_lines, int)
        ):
            errors.append("refined.statistics.rendered_lines must be an integer")
        elif recorded_rendered_lines != len(rendered_lines):
            errors.append(
                "refined.statistics.rendered_lines does not match Qwen transcript"
            )

    raw_recorded_path = mapping_value(
        aligned,
        "source",
        "raw_asr_path",
        field="aligned.source.raw_asr_path",
        errors=errors,
    )
    check_recorded_path(
        raw_recorded_path,
        base=repository_root,
        expected=raw_path,
        repository_root=repository_root,
        field="aligned.source.raw_asr_path",
        errors=errors,
    )
    aligned_raw_sha = valid_sha256(
        mapping_value(
            aligned,
            "source",
            "raw_asr_sha256",
            field="aligned.source.raw_asr_sha256",
            errors=errors,
        ),
        field="aligned.source.raw_asr_sha256",
        errors=errors,
    )
    if aligned_raw_sha is not None and aligned_raw_sha != raw_sha:
        errors.append("aligned.source.raw_asr_sha256 does not match raw.json")

    refined_input_path = mapping_value(
        refined,
        "source",
        "input_asr_path",
        field="refined.source.input_asr_path",
        errors=errors,
    )
    check_recorded_path(
        refined_input_path,
        base=repository_root,
        expected=aligned_path,
        repository_root=repository_root,
        field="refined.source.input_asr_path",
        errors=errors,
    )
    refined_aligned_sha = valid_sha256(
        mapping_value(
            refined,
            "source",
            "input_asr_sha256",
            field="refined.source.input_asr_sha256",
            errors=errors,
        ),
        field="refined.source.input_asr_sha256",
        errors=errors,
    )
    if refined_aligned_sha is not None and refined_aligned_sha != aligned_sha:
        errors.append("refined.source.input_asr_sha256 does not match aligned.json")

    rendered_path = mapping_value(
        refined,
        "rendered_transcript",
        "path",
        field="refined.rendered_transcript.path",
        errors=errors,
    )
    check_recorded_path(
        rendered_path,
        base=repository_root,
        expected=transcript_path,
        repository_root=repository_root,
        field="refined.rendered_transcript.path",
        errors=errors,
    )
    rendered_sha = valid_sha256(
        mapping_value(
            refined,
            "rendered_transcript",
            "sha256",
            field="refined.rendered_transcript.sha256",
            errors=errors,
        ),
        field="refined.rendered_transcript.sha256",
        errors=errors,
    )
    if rendered_sha is not None and rendered_sha != transcript_sha:
        errors.append(
            "refined.rendered_transcript.sha256 does not match transcript.zh-CN.md"
        )

    raw_audio_sha = valid_sha256(
        mapping_value(
            raw,
            "audio",
            "sha256",
            field="raw.audio.sha256",
            errors=errors,
        ),
        field="raw.audio.sha256",
        errors=errors,
    )
    aligned_audio_sha = valid_sha256(
        mapping_value(
            aligned,
            "source",
            "audio_sha256",
            field="aligned.source.audio_sha256",
            errors=errors,
        ),
        field="aligned.source.audio_sha256",
        errors=errors,
    )
    if (
        raw_audio_sha is not None
        and aligned_audio_sha is not None
        and raw_audio_sha != aligned_audio_sha
    ):
        errors.append("aligned.source.audio_sha256 does not match raw.audio.sha256")

    cache_value = nested_front_matter_scalar(
        front_matter, "local_audio_cache", "path"
    )
    cache_path: Path | None = None
    if cache_value is not None:
        cache_path = safe_recorded_path(
            cache_value,
            base=repository_root,
            repository_root=repository_root,
            field="local_audio_cache.path",
            errors=errors,
        )
    if cache_path is None:
        show_id = episode_dir.parent.parent.name
        cache_path = (
            repository_root
            / ".cache"
            / "media"
            / show_id
            / episode_dir.name
            / "source.m4a"
        )

    if cache_path.is_file():
        actual_audio_sha = sha256_file(cache_path)
        actual_audio_size = cache_path.stat().st_size
        raw_audio_size = mapping_value(
            raw,
            "audio",
            "size_bytes",
            field="raw.audio.size_bytes",
            errors=errors,
        )
        if isinstance(raw_audio_size, bool) or not isinstance(raw_audio_size, int):
            errors.append("raw.audio.size_bytes must be an integer")
        elif raw_audio_size != actual_audio_size:
            errors.append("raw.audio.size_bytes does not match cached audio")
        if raw_audio_sha is not None and raw_audio_sha != actual_audio_sha:
            errors.append("raw.audio.sha256 does not match cached audio")
        if aligned_audio_sha is not None and aligned_audio_sha != actual_audio_sha:
            errors.append("aligned.source.audio_sha256 does not match cached audio")

    if len(selected_runs) > 1:
        errors.append("episode README marks more than one Qwen ASR run as selected")

    expected_episode_paths = {
        "raw": raw_path,
        "aligned": aligned_path,
        "refined": refined_path,
        "transcript": transcript_path,
    }
    for index, run in enumerate(qwen_runs):
        artifacts = run.get("artifacts")
        if not isinstance(artifacts, dict):
            errors.append(f"asr_runs Qwen item {index} has no artifacts mapping")
            continue
        for name, expected in expected_episode_paths.items():
            check_recorded_path(
                artifacts.get(name),
                base=episode_dir,
                expected=expected,
                repository_root=repository_root,
                field=f"asr_runs[{index}].artifacts.{name}",
                errors=errors,
            )

    if selected_runs:
        root_value = nested_front_matter_scalar(front_matter, "transcript", "path")
        root_transcript = check_recorded_path(
            root_value,
            base=episode_dir,
            expected=episode_dir / transcript_path.name,
            repository_root=repository_root,
            field="transcript.path",
            errors=errors,
        )
        if root_transcript is not None:
            if not root_transcript.is_file():
                errors.append(
                    f"selected Qwen root transcript is missing: "
                    f"{display_path(root_transcript, repository_root)}"
                )
            elif root_transcript.read_bytes() != transcript_path.read_bytes():
                errors.append(
                    "selected Qwen root transcript is not byte-identical to "
                    "asr/qwen3-asr/transcript.zh-CN.md"
                )

    return True


def check_front_matter(path: Path, text: str, errors: list[str]) -> None:
    if not text.startswith("---\n"):
        errors.append(f"{relative(path)} must begin with YAML front matter")
        return

    if "\n---\n" not in text[4:]:
        errors.append(f"{relative(path)} has no closing front matter marker")


def check_bilibili_urls(path: Path, text: str, errors: list[str]) -> int:
    for parameter in TRACKING_PARAMETERS:
        if parameter in text:
            errors.append(
                f"{relative(path)} contains tracking parameter {parameter}"
            )

    count = 0
    for match in BILIBILI_URL_RE.finditer(text):
        count += 1
        url = match.group(0)
        if CANONICAL_BILIBILI_URL_RE.fullmatch(url) is None:
            errors.append(
                f"{relative(path)} contains non-canonical Bilibili URL: {url}"
            )
    return count


def main() -> int:
    errors: list[str] = []
    markdown_count = 0
    bilibili_url_count = 0
    qwen_chain_count = 0

    if not SHOWS_ROOT.is_dir():
        print("PodWiki validation failed:\n\n- shows directory is missing", file=sys.stderr)
        return 1

    for path in sorted(SHOWS_ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        markdown_count += 1
        if path.name == "README.md":
            check_front_matter(path, text, errors)
        elif path.name.startswith("transcript.") and text.startswith("---\n"):
            errors.append(
                f"{relative(path)} must keep metadata in its episode README"
            )
        bilibili_url_count += check_bilibili_urls(path, text, errors)

    for episode_dir in sorted(SHOWS_ROOT.glob("*/episodes/*")):
        if not episode_dir.is_dir():
            continue
        readme = episode_dir / "README.md"
        readme_text = readme.read_text(encoding="utf-8") if readme.is_file() else ""
        if validate_qwen_chain(
            episode_dir,
            repository_root=ROOT,
            readme_text=readme_text,
            errors=errors,
        ):
            qwen_chain_count += 1

    if errors:
        print("PodWiki validation failed:\n", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "PodWiki validation passed: "
        f"{markdown_count} Markdown files, "
        f"{bilibili_url_count} Bilibili URLs, "
        f"{qwen_chain_count} complete Qwen ASR chains."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
