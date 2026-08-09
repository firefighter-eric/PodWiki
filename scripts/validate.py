#!/usr/bin/env python3
"""Validate PodWiki content, source URLs, and complete Qwen ASR chains."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime
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
XIAOYUZHOU_URL_RE = re.compile(
    r"https://www\.xiaoyuzhoufm\.com/(?:episode|podcast)/[^\s)\]\"']+"
)
CANONICAL_XIAOYUZHOU_URL_RE = re.compile(
    r"https://www\.xiaoyuzhoufm\.com/(?:episode|podcast)/[0-9a-f]{24}"
)
TRACKING_PARAMETERS = ("spm_id_from", "vd_source")
QWEN_JSON_ARTIFACT_NAMES = (
    "raw.json",
    "aligned.json",
    "refined.json",
)
DEFAULT_QWEN_TRANSCRIPT_NAME = "transcript.zh-CN.md"
QWEN_TRANSCRIPT_NAME_RE = re.compile(
    r"transcript\.[A-Za-z]{2,3}(?:-[A-Za-z0-9]{2,8})*\.md"
)
SHA256_RE = re.compile(r"[0-9a-f]{64}")
SHOW_ID_RE = re.compile(r"[a-z0-9]+")
EPISODE_KEY_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
RFC3339_RE = re.compile(
    r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})"
)
CALENDAR_DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
TRANSCRIPT_LINE_RE = re.compile(r"^\[\d{2}:[0-5]\d:[0-5]\d\] \S.*  $")
TRANSCRIPT_TIMESTAMP_RE = re.compile(r"^(\[\d{2}:[0-5]\d:[0-5]\d\]) ")
TRANSLATION_STATUSES = {"machine", "edited", "reviewed"}
WORKFLOW_METADATA_STATUSES = {"draft", "verified"}
WORKFLOW_SUMMARY_STATUSES = {"empty", "outline", "draft", "reviewed"}
WORKFLOW_TRANSCRIPT_STATUSES = {
    "not-started",
    "source-acquired",
    "machine",
    "edited",
    "reviewed",
    "blocked",
}
WEB_SUMMARY_STATUSES = {"draft", "reviewed"}
WEB_TRANSCRIPT_STATUSES = {"machine", "edited", "reviewed"}


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


def top_level_front_matter_scalar(lines: list[str], key: str) -> str | None:
    for line in lines:
        stripped = line.strip()
        indent = len(line) - len(line.lstrip(" "))
        if indent == 0 and stripped.startswith(f"{key}:"):
            return decode_yaml_scalar(stripped.split(":", 1)[1])
    return None


def top_level_front_matter_raw_scalar(lines: list[str], key: str) -> str | None:
    for line in lines:
        stripped = line.strip()
        indent = len(line) - len(line.lstrip(" "))
        if indent == 0 and stripped.startswith(f"{key}:"):
            return stripped.split(":", 1)[1].strip()
    return None


def parse_transcript_translations(
    lines: list[str], *, errors: list[str]
) -> tuple[bool, list[dict[str, Any]]]:
    translations: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    in_transcript = False
    in_translations = False
    translations_present = False

    for line in lines:
        stripped = line.strip()
        indent = len(line) - len(line.lstrip(" "))
        if not in_transcript:
            if indent == 0 and stripped == "transcript:":
                in_transcript = True
            continue
        if stripped and indent == 0:
            break
        if not stripped or stripped.startswith("#"):
            continue

        if indent == 2 and stripped.startswith("translations:"):
            translations_present = True
            in_translations = True
            current = None
            inline = stripped.split(":", 1)[1].strip()
            if inline == "[]":
                in_translations = False
            elif inline:
                errors.append("transcript.translations must be a YAML list")
                in_translations = False
            continue
        if not in_translations:
            continue
        if indent <= 2:
            in_translations = False
            current = None
            continue
        if indent == 4 and (stripped == "-" or stripped.startswith("- ")):
            current = {}
            translations.append(current)
            item = stripped[1:].strip()
            if item:
                if ":" not in item:
                    errors.append(
                        "transcript.translations items must be YAML mappings"
                    )
                    continue
                key, value = item.split(":", 1)
                current[key.strip()] = decode_yaml_scalar(value)
            continue
        if indent == 6 and current is not None and ":" in stripped:
            key, value = stripped.split(":", 1)
            key = key.strip()
            if key in current:
                errors.append(
                    f"transcript.translations item has duplicate field {key!r}"
                )
            current[key] = decode_yaml_scalar(value)
            continue
        errors.append("transcript.translations items must be YAML mappings")

    return translations_present, translations


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


def decode_non_empty_yaml_scalar(value: str) -> str | None:
    """Decode the small scalar subset used by profile front matter."""

    raw = value.strip()
    if not raw:
        return None
    quoted = len(raw) >= 2 and raw[0] in {'"', "'"} and raw[-1] == raw[0]
    if not quoted and (raw == "~" or raw.lower() == "null"):
        return None
    decoded = decode_yaml_scalar(raw)
    return decoded if decoded.strip() else None


def validate_participant_profiles(
    lines: list[str], *, field_prefix: str, errors: list[str]
) -> None:
    """Validate optional profiles nested directly in ``participants[]``."""

    profiles: list[dict[str, Any]] = []
    in_participants = False
    participant_index = -1
    profile_seen = False
    current_profile: dict[str, Any] | None = None
    current_list_name: str | None = None
    current_list_item: dict[str, str | None] | None = None
    scalar_fields = {"headline", "bio", "checked_at"}
    list_fields = {"affiliations", "education"}

    def profile_field(index: int) -> str:
        return f"{field_prefix} participants[{index}].profile"

    def start_profile(raw_value: str) -> None:
        nonlocal current_profile, current_list_name, current_list_item, profile_seen
        if participant_index < 0:
            errors.append(
                f"{field_prefix} profile must be attached to a participants list item"
            )
            return
        if profile_seen:
            errors.append(
                f"{profile_field(participant_index)} has a duplicate profile field"
            )
            return
        profile_seen = True
        current_list_name = None
        current_list_item = None
        if raw_value.strip():
            errors.append(f"{profile_field(participant_index)} must be a YAML mapping")
            current_profile = None
            return
        current_profile = {
            "participant_index": participant_index,
            "fields": {},
            "seen_fields": set(),
            "lists": {},
        }
        profiles.append(current_profile)

    for line in lines:
        stripped = line.strip()
        indent = len(line) - len(line.lstrip(" "))
        if not in_participants:
            if indent == 0 and stripped == "participants:":
                in_participants = True
            continue
        if stripped and indent == 0:
            break
        if not stripped or stripped.startswith("#"):
            continue

        if indent == 2 and (stripped == "-" or stripped.startswith("- ")):
            participant_index += 1
            profile_seen = False
            current_profile = None
            current_list_name = None
            current_list_item = None
            item = stripped[1:].strip()
            if item.startswith("profile:"):
                start_profile(item.split(":", 1)[1])
            continue

        if indent == 4:
            current_profile = None
            current_list_name = None
            current_list_item = None
            if stripped.startswith("profile:"):
                start_profile(stripped.split(":", 1)[1])
            continue

        if current_profile is None:
            continue
        index = current_profile["participant_index"]
        fields = current_profile["fields"]
        seen_fields = current_profile["seen_fields"]
        lists = current_profile["lists"]
        base_field = profile_field(index)

        if indent == 6:
            current_list_name = None
            current_list_item = None
            if ":" not in stripped:
                errors.append(f"{base_field} must be a YAML mapping")
                continue
            key, raw_value = stripped.split(":", 1)
            key = key.strip()
            raw_value = raw_value.strip()
            if key in seen_fields:
                errors.append(f"{base_field} has duplicate field {key!r}")
                continue
            seen_fields.add(key)
            if key in scalar_fields:
                fields[key] = decode_non_empty_yaml_scalar(raw_value)
            elif key in list_fields:
                state = {"mode": "block", "items": []}
                lists[key] = state
                if raw_value == "[]":
                    state["mode"] = "empty"
                elif raw_value:
                    state["mode"] = "invalid"
                    errors.append(f"{base_field}.{key} must be a YAML list")
                else:
                    current_list_name = key
            continue

        if indent == 8 and current_list_name is not None:
            state = lists[current_list_name]
            if not (stripped == "-" or stripped.startswith("- ")):
                state["mode"] = "invalid"
                errors.append(
                    f"{base_field}.{current_list_name} must be a YAML list"
                )
                current_list_item = None
                continue
            item: dict[str, str | None] = {}
            state["items"].append(item)
            current_list_item = item
            inline = stripped[1:].strip()
            if not inline:
                continue
            if ":" not in inline:
                errors.append(
                    f"{base_field}.{current_list_name} items must be YAML mappings"
                )
                continue
            key, raw_value = inline.split(":", 1)
            item[key.strip()] = decode_non_empty_yaml_scalar(raw_value)
            continue

        if (
            indent == 10
            and current_list_name is not None
            and current_list_item is not None
        ):
            if ":" not in stripped:
                errors.append(
                    f"{base_field}.{current_list_name} items must be YAML mappings"
                )
                continue
            key, raw_value = stripped.split(":", 1)
            key = key.strip()
            if key in current_list_item:
                errors.append(
                    f"{base_field}.{current_list_name} item has duplicate field "
                    f"{key!r}"
                )
                continue
            current_list_item[key] = decode_non_empty_yaml_scalar(raw_value)

    for profile in profiles:
        index = profile["participant_index"]
        base_field = profile_field(index)
        fields = profile["fields"]
        if fields.get("headline") is None:
            errors.append(f"{base_field}.headline must be a non-empty string")
        if "bio" in fields and fields["bio"] is None:
            errors.append(f"{base_field}.bio must be a non-empty string when present")

        checked_at = fields.get("checked_at")
        valid_checked_at = (
            isinstance(checked_at, str)
            and CALENDAR_DATE_RE.fullmatch(checked_at) is not None
        )
        if valid_checked_at:
            try:
                datetime.strptime(checked_at, "%Y-%m-%d")
            except ValueError:
                valid_checked_at = False
        if not valid_checked_at:
            errors.append(f"{base_field}.checked_at must be a valid YYYY-MM-DD date")

        for list_name, state in profile["lists"].items():
            if state["mode"] == "block" and not state["items"]:
                errors.append(f"{base_field}.{list_name} must be a YAML list")
            for item_index, item in enumerate(state["items"]):
                item_field = f"{base_field}.{list_name}[{item_index}]"
                required = (
                    ("organization", "status")
                    if list_name == "affiliations"
                    else ("institution",)
                )
                for key in required:
                    if item.get(key) is None:
                        errors.append(f"{item_field}.{key} must be a non-empty string")
                optional = (
                    ("title",) if list_name == "affiliations" else ("credential", "field")
                )
                for key in optional:
                    if key in item and item[key] is None:
                        errors.append(
                            f"{item_field}.{key} must be a non-empty string when present"
                        )
                if list_name == "affiliations" and item.get("status") not in {
                    "current",
                    "former",
                    None,
                }:
                    errors.append(
                        f"{item_field}.status must be one of current, former"
                    )


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
    containment_label: str = "repository",
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
        errors.append(f"{field} escapes the {containment_label}: {value!r}")
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


def is_rfc3339_timestamp(value: Any) -> bool:
    if not isinstance(value, str) or RFC3339_RE.fullmatch(value) is None:
        return False
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed.tzinfo is not None


def is_episode_web_publishable(workflow: dict[str, str | None]) -> bool:
    return (
        workflow.get("metadata") == "verified"
        and workflow.get("summary") in WEB_SUMMARY_STATUSES
        and workflow.get("transcript") in WEB_TRANSCRIPT_STATUSES
    )


def validate_source_preferences(
    lines: list[str], *, field_prefix: str, errors: list[str]
) -> None:
    in_sources = False
    sources_present = False
    source_count = 0
    preferred_count = 0
    current_has_preferred = False

    def record_preferred(raw_value: str) -> None:
        nonlocal preferred_count, current_has_preferred
        if current_has_preferred:
            errors.append(f"{field_prefix} source has duplicate preferred fields")
            return
        current_has_preferred = True
        value = raw_value.strip()
        if value not in {"true", "false"}:
            errors.append(
                f"{field_prefix} sources[].preferred must be a YAML boolean"
            )
        elif value == "true":
            preferred_count += 1

    for line in lines:
        stripped = line.strip()
        indent = len(line) - len(line.lstrip(" "))
        if not in_sources:
            if indent == 0 and stripped.startswith("sources:"):
                in_sources = True
                sources_present = True
            continue
        if stripped and indent == 0:
            break
        if not stripped or stripped.startswith("#"):
            continue
        if indent == 2 and (stripped == "-" or stripped.startswith("- ")):
            source_count += 1
            current_has_preferred = False
            inline = stripped[1:].strip()
            if inline.startswith("preferred:"):
                record_preferred(inline.split(":", 1)[1])
            continue
        if indent == 4 and stripped.startswith("preferred:"):
            if source_count == 0:
                errors.append(f"{field_prefix} sources must be a YAML list")
                continue
            record_preferred(stripped.split(":", 1)[1])

    if not sources_present or source_count == 0:
        errors.append(f"{field_prefix} sources must contain at least one source")
    if preferred_count != 1:
        errors.append(
            f"{field_prefix} sources must contain exactly one preferred source"
        )


def validate_episode_metadata_contract(
    readme_path: Path,
    readme_text: str,
    *,
    repository_root: Path,
    episode_ids: dict[str, Path],
    errors: list[str],
) -> bool:
    """Validate metadata shared by the repository gate and the web catalog."""

    front_matter = extract_front_matter_lines(readme_text)
    label = display_path(readme_path, repository_root)
    episode_dir = readme_path.parent
    episode_id = top_level_front_matter_scalar(front_matter, "id")
    show_id = top_level_front_matter_scalar(front_matter, "show_id")
    episode_key = top_level_front_matter_scalar(front_matter, "episode_key")
    published_at = top_level_front_matter_scalar(front_matter, "published_at")
    episode_key_raw = top_level_front_matter_raw_scalar(front_matter, "episode_key")
    published_at_raw = top_level_front_matter_raw_scalar(front_matter, "published_at")
    duration_ms_raw = top_level_front_matter_raw_scalar(front_matter, "duration_ms")

    if not episode_id:
        errors.append(f"{label} is missing id")
    else:
        previous = episode_ids.get(episode_id)
        if previous is not None:
            errors.append(
                f"{label} duplicates episode id {episode_id!r} from "
                f"{display_path(previous, repository_root)}"
            )
        else:
            episode_ids[episode_id] = readme_path

    if not show_id or SHOW_ID_RE.fullmatch(show_id) is None:
        errors.append(f"{label} show_id must contain only lowercase letters and digits")
    elif len(readme_path.parents) >= 3 and readme_path.parents[2].name != show_id:
        errors.append(
            f"{label} show_id {show_id!r} does not match its show directory "
            f"{readme_path.parents[2].name!r}"
        )

    if not episode_key or EPISODE_KEY_RE.fullmatch(episode_key) is None:
        errors.append(f"{label} episode_key has an invalid stable-key format")
    elif episode_key.isdigit() and episode_key_raw == episode_key:
        errors.append(f"{label} numeric episode_key must be a quoted YAML string")

    if episode_id and show_id and episode_key:
        expected_id = f"{show_id}:{episode_key}"
        if episode_id != expected_id:
            errors.append(f"{label} id must equal {expected_id!r}")

    if (
        not is_rfc3339_timestamp(published_at)
        or published_at_raw is None
        or len(published_at_raw) < 2
        or published_at_raw[0] not in {'"', "'"}
        or published_at_raw[-1] != published_at_raw[0]
    ):
        errors.append(f"{label} published_at must be an RFC 3339 timestamp with offset")

    if duration_ms_raw is None or re.fullmatch(r"[1-9]\d*", duration_ms_raw) is None:
        errors.append(f"{label} duration_ms must be a positive integer")

    workflow = {
        "metadata": nested_front_matter_scalar(front_matter, "workflow", "metadata"),
        "summary": nested_front_matter_scalar(front_matter, "workflow", "summary"),
        "transcript": nested_front_matter_scalar(
            front_matter, "workflow", "transcript"
        ),
    }
    workflow_contracts = {
        "metadata": WORKFLOW_METADATA_STATUSES,
        "summary": WORKFLOW_SUMMARY_STATUSES,
        "transcript": WORKFLOW_TRANSCRIPT_STATUSES,
    }
    for field, allowed in workflow_contracts.items():
        if workflow[field] not in allowed:
            errors.append(
                f"{label} workflow.{field} must be one of {', '.join(sorted(allowed))}"
            )

    validate_source_preferences(front_matter, field_prefix=label, errors=errors)
    validate_participant_profiles(front_matter, field_prefix=label, errors=errors)
    publishable = is_episode_web_publishable(workflow)

    for section in ("summary", "transcript"):
        value = nested_front_matter_scalar(front_matter, section, "path")
        asset_path = safe_recorded_path(
            value,
            base=episode_dir,
            repository_root=episode_dir,
            field=f"{label} {section}.path",
            errors=errors,
            containment_label="episode directory",
        )
        if publishable and asset_path is not None and not asset_path.is_file():
            errors.append(
                f"{label} is web-publishable but {section}.path is missing: {value!r}"
            )

    return publishable


def transcript_structure(
    path: Path,
    *,
    repository_root: Path,
    field: str,
    errors: list[str],
) -> tuple[str, list[str], list[str | None]] | None:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as error:
        errors.append(
            f"{field} cannot be read at "
            f"{display_path(path, repository_root)}: {error}"
        )
        return None

    if len(lines) < 3 or not lines[0].startswith("# ") or lines[1] != "":
        errors.append(
            f"{field} must start with a level-one title, a blank line, "
            "and at least one segment"
        )
        return None

    body = lines[2:]
    timestamps: list[str | None] = []
    for index, line in enumerate(body, start=3):
        if TRANSCRIPT_LINE_RE.fullmatch(line) is None:
            errors.append(
                f"{field} line {index} must be one timestamped sentence "
                "with a Markdown hard break"
            )
            timestamps.append(None)
            continue
        match = TRANSCRIPT_TIMESTAMP_RE.match(line)
        timestamps.append(match.group(1) if match is not None else None)
    return lines[0], body, timestamps


def validate_episode_translations(
    episode_dir: Path,
    *,
    repository_root: Path,
    readme_text: str,
    errors: list[str],
    require_complete: bool = True,
) -> None:
    """Validate required segment-aligned Chinese translations of English roots."""

    front_matter = extract_front_matter_lines(readme_text)
    episode_language = top_level_front_matter_scalar(front_matter, "language")
    selected_value = nested_front_matter_scalar(front_matter, "transcript", "path")
    selected_is_english = isinstance(selected_value, str) and selected_value.endswith(
        ".en.md"
    )
    required = episode_language == "en" or selected_is_english
    translations_present, translations = parse_transcript_translations(
        front_matter, errors=errors
    )

    if not required:
        if translations:
            errors.append(
                "transcript.translations is only valid when the selected transcript "
                "is English"
            )
        return

    expected_source = episode_dir / "transcript.en.md"
    source_path = check_recorded_path(
        selected_value,
        base=episode_dir,
        expected=expected_source,
        repository_root=repository_root,
        field="transcript.path",
        errors=errors,
    )
    translation_claimed = bool(translations)
    if (
        (require_complete or translation_claimed)
        and source_path is not None
        and not source_path.is_file()
    ):
        errors.append(
            "selected English transcript is missing: "
            f"{display_path(source_path, repository_root)}"
        )

    chinese_items = [
        item for item in translations if item.get("language") == "zh-CN"
    ]
    if (require_complete or translation_claimed) and (
        not translations_present or len(chinese_items) != 1
    ):
        errors.append(
            "English selected transcript requires exactly one zh-CN item in "
            "transcript.translations"
        )

    source_structure = (
        transcript_structure(
            source_path,
            repository_root=repository_root,
            field="selected English transcript",
            errors=errors,
        )
        if source_path is not None and source_path.is_file()
        else None
    )

    for index, translation in enumerate(translations):
        field = f"transcript.translations[{index}]"
        language = translation.get("language")
        if language != "zh-CN":
            errors.append(f"{field}.language must be 'zh-CN'")
        if translation.get("source_language") != "en":
            errors.append(f"{field}.source_language must be 'en'")
        if translation.get("alignment") != "segment":
            errors.append(f"{field}.alignment must be 'segment'")
        status = translation.get("status")
        if status not in TRANSLATION_STATUSES:
            errors.append(
                f"{field}.status must be one of machine, edited, reviewed"
            )
        generated_at = translation.get("generated_at")
        if not is_rfc3339_timestamp(generated_at):
            errors.append(f"{field}.generated_at must be an RFC 3339 timestamp")

        translation_path = check_recorded_path(
            translation.get("path"),
            base=episode_dir,
            expected=episode_dir / "transcript.zh-CN.md",
            repository_root=repository_root,
            field=f"{field}.path",
            errors=errors,
        )
        translation_source_path = check_recorded_path(
            translation.get("source_path"),
            base=episode_dir,
            expected=expected_source,
            repository_root=repository_root,
            field=f"{field}.source_path",
            errors=errors,
        )

        source_sha = valid_sha256(
            translation.get("source_sha256"),
            field=f"{field}.source_sha256",
            errors=errors,
        )
        translation_sha = valid_sha256(
            translation.get("sha256"),
            field=f"{field}.sha256",
            errors=errors,
        )
        if source_path is not None and source_path.is_file() and source_sha is not None:
            if source_sha != sha256_file(source_path):
                errors.append(
                    f"{field}.source_sha256 does not match transcript.en.md"
                )
        if (
            translation_source_path is not None
            and source_path is not None
            and translation_source_path != source_path
        ):
            errors.append(f"{field}.source_path must match transcript.path")

        if translation_path is None:
            continue
        if not translation_path.is_file():
            errors.append(
                "Chinese transcript translation is missing: "
                f"{display_path(translation_path, repository_root)}"
            )
            continue
        if translation_sha is not None and translation_sha != sha256_file(
            translation_path
        ):
            errors.append(f"{field}.sha256 does not match transcript.zh-CN.md")

        translation_structure = transcript_structure(
            translation_path,
            repository_root=repository_root,
            field="Chinese transcript translation",
            errors=errors,
        )
        if source_structure is None or translation_structure is None:
            continue
        source_title, source_body, source_timestamps = source_structure
        translation_title, translation_body, translation_timestamps = (
            translation_structure
        )
        if translation_title != source_title:
            errors.append(
                "transcript.en.md and transcript.zh-CN.md must have the same title"
            )
        if len(translation_body) != len(source_body):
            errors.append(
                "transcript.en.md and transcript.zh-CN.md must have the same "
                "number of segment lines"
            )
        for line_number, (source_timestamp, translation_timestamp) in enumerate(
            zip(source_timestamps, translation_timestamps), start=1
        ):
            if (
                source_timestamp is not None
                and translation_timestamp is not None
                and source_timestamp != translation_timestamp
            ):
                errors.append(
                    "transcript.zh-CN.md segment "
                    f"{line_number} timestamp {translation_timestamp} does not "
                    f"match transcript.en.md {source_timestamp}"
                )


def qwen_transcript_name(
    *,
    qwen_dir: Path,
    front_matter: list[str],
    qwen_runs: list[dict[str, Any]],
    errors: list[str],
) -> str:
    """Discover the rendered language even before a run is recorded in README."""

    names: set[str] = set()
    for run in qwen_runs:
        artifacts = run.get("artifacts")
        value = artifacts.get("transcript") if isinstance(artifacts, dict) else None
        if isinstance(value, str):
            names.add(PurePosixPath(value).name)

    root_transcript = nested_front_matter_scalar(
        front_matter, "transcript", "path"
    )
    if isinstance(root_transcript, str) and root_transcript:
        names.add(PurePosixPath(root_transcript).name)

    if qwen_dir.is_dir():
        names.update(
            path.name
            for path in qwen_dir.glob("transcript.*.md")
            if path.is_file()
        )

    invalid_names = sorted(
        name for name in names if QWEN_TRANSCRIPT_NAME_RE.fullmatch(name) is None
    )
    for name in invalid_names:
        errors.append(
            "Qwen transcript artifact must use transcript.<language>.md naming: "
            f"{name!r}"
        )
    valid_names = sorted(names.difference(invalid_names))
    if len(valid_names) > 1:
        errors.append(
            "episode records multiple Qwen transcript languages: "
            + ", ".join(valid_names)
        )
    return valid_names[0] if valid_names else DEFAULT_QWEN_TRANSCRIPT_NAME


def validate_qwen_chain(
    episode_dir: Path,
    *,
    repository_root: Path,
    readme_text: str,
    errors: list[str],
) -> bool:
    """Validate one complete chain; intentional raw/aligned checkpoints are skipped."""

    front_matter = extract_front_matter_lines(readme_text)
    qwen_runs = [run for run in parse_asr_runs(front_matter) if is_qwen_run(run)]
    selected_runs = [
        run
        for run in qwen_runs
        if str(run.get("selection_status", "")).lower() == "selected"
    ]
    qwen_dir = episode_dir / "asr" / "qwen3-asr"
    transcript_name = qwen_transcript_name(
        qwen_dir=qwen_dir,
        front_matter=front_matter,
        qwen_runs=qwen_runs,
        errors=errors,
    )
    paths = {name: qwen_dir / name for name in QWEN_JSON_ARTIFACT_NAMES}
    paths[transcript_name] = qwen_dir / transcript_name
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
    transcript_path = paths[transcript_name]
    raw = read_json_strict(raw_path, repository_root=repository_root, errors=errors)
    aligned = read_json_strict(
        aligned_path, repository_root=repository_root, errors=errors
    )
    refined = read_json_strict(
        refined_path, repository_root=repository_root, errors=errors
    )
    if raw is None or aligned is None or refined is None:
        return True

    transcript_language = transcript_name.removeprefix("transcript.").removesuffix(
        ".md"
    )
    if refined.get("language") != transcript_language:
        errors.append(
            "refined.language must match the Qwen transcript filename: "
            f"expected={transcript_language!r} actual={refined.get('language')!r}"
        )

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
            f"refined.rendered_transcript.sha256 does not match {transcript_name}"
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
                    f"asr/qwen3-asr/{transcript_name}"
                )

    return True


def check_front_matter(path: Path, text: str, errors: list[str]) -> None:
    if not text.startswith("---\n"):
        errors.append(f"{relative(path)} must begin with YAML front matter")
        return

    if "\n---\n" not in text[4:]:
        errors.append(f"{relative(path)} has no closing front matter marker")


def validate_episode_catalog_keyword(
    path: Path,
    text: str,
    errors: list[str],
) -> None:
    lines = extract_front_matter_lines(text)
    value = top_level_front_matter_scalar(lines, "catalog_keyword")
    if value is None:
        errors.append(f"{relative(path)} is missing catalog_keyword")
        return
    if value != value.strip():
        errors.append(f"{relative(path)} catalog_keyword has surrounding whitespace")
    if not 1 <= len(value) <= 20:
        errors.append(f"{relative(path)} catalog_keyword must be 1-20 characters")
    if re.match(r"^(?:#|第\s*\d+|特访|特别)", value):
        errors.append(
            f"{relative(path)} catalog_keyword must not contain episode numbering or release labels"
        )
    navigation_title = top_level_front_matter_scalar(lines, "navigation_title")
    if navigation_title is not None:
        person = navigation_title.split(" · ", 1)[0]
        if value in {person, navigation_title}:
            errors.append(
                f"{relative(path)} catalog_keyword must not duplicate the person or full navigation title"
            )


def validate_episode_navigation_title(
    path: Path,
    text: str,
    errors: list[str],
) -> None:
    lines = extract_front_matter_lines(text)
    value = top_level_front_matter_scalar(lines, "navigation_title")
    if value is None:
        errors.append(f"{relative(path)} is missing navigation_title")
        return
    parts = value.split(" · ")
    if len(parts) != 2 or not all(parts):
        errors.append(
            f"{relative(path)} navigation_title must use 'person · topic' format"
        )
    if len(value) > 40:
        errors.append(f"{relative(path)} navigation_title must be at most 40 characters")
    if re.match(r"^(?:#|第\s*\d+|特访|特别)", value):
        errors.append(
            f"{relative(path)} navigation_title must not contain episode numbering or release labels"
        )


def parse_markdown_table_row(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return []
    return [cell.strip() for cell in stripped[1:-1].split("|")]


def validate_core_point_logic_table(
    path: Path,
    text: str,
    errors: list[str],
) -> None:
    section = re.search(
        r"^## 核心观点[ \t]*\n(?P<body>.*?)(?=^###\s|\Z)",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )
    if section is None:
        errors.append(f"{relative(path)} is missing the 核心观点 section")
        return

    lines = [line for line in section.group("body").splitlines() if line.strip()]
    if len(lines) < 3:
        errors.append(f"{relative(path)} 核心观点 must begin with a logic table")
        return

    columns = parse_markdown_table_row(lines[0])
    separator = parse_markdown_table_row(lines[1])
    rows = [parse_markdown_table_row(line) for line in lines[2:]]
    if not 2 <= len(columns) <= 4 or any(not column for column in columns):
        errors.append(
            f"{relative(path)} 核心观点 logic table must have 2-4 named columns"
        )
        return
    if len(separator) != len(columns) or any(
        re.fullmatch(r":?-{3,}:?", cell) is None for cell in separator
    ):
        errors.append(f"{relative(path)} 核心观点 logic table has an invalid separator")
        return
    if len(rows) < 3:
        errors.append(f"{relative(path)} 核心观点 logic table must have at least 3 rows")
    if any(len(row) != len(columns) or any(not cell for cell in row) for row in rows):
        errors.append(
            f"{relative(path)} 核心观点 logic table rows must match its named columns"
        )

    decorative_number = re.compile(r"^(?:0?\d+|第\s*\d+)$")
    if any(decorative_number.fullmatch(column) for column in columns) or any(
        decorative_number.fullmatch(cell) for row in rows for cell in row
    ):
        errors.append(
            f"{relative(path)} 核心观点 logic table must not use decorative numbering"
        )


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


def check_xiaoyuzhou_urls(path: Path, text: str, errors: list[str]) -> int:
    count = 0
    for match in XIAOYUZHOU_URL_RE.finditer(text):
        count += 1
        url = match.group(0)
        if CANONICAL_XIAOYUZHOU_URL_RE.fullmatch(url) is None:
            errors.append(
                f"{relative(path)} contains non-canonical Xiaoyuzhou URL: {url}"
            )
    return count


def main() -> int:
    errors: list[str] = []
    markdown_count = 0
    bilibili_url_count = 0
    xiaoyuzhou_url_count = 0
    qwen_chain_count = 0
    episode_ids: dict[str, Path] = {}

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
        elif path.name.startswith("summary."):
            validate_core_point_logic_table(path, text, errors)
        bilibili_url_count += check_bilibili_urls(path, text, errors)
        xiaoyuzhou_url_count += check_xiaoyuzhou_urls(path, text, errors)

    for episode_dir in sorted(SHOWS_ROOT.glob("*/episodes/*")):
        if not episode_dir.is_dir():
            continue
        readme = episode_dir / "README.md"
        readme_text = readme.read_text(encoding="utf-8") if readme.is_file() else ""
        publishable = validate_episode_metadata_contract(
            readme,
            readme_text,
            repository_root=ROOT,
            episode_ids=episode_ids,
            errors=errors,
        )
        validate_episode_catalog_keyword(readme, readme_text, errors)
        validate_episode_navigation_title(readme, readme_text, errors)
        validate_episode_translations(
            episode_dir,
            repository_root=ROOT,
            readme_text=readme_text,
            errors=errors,
            require_complete=publishable,
        )
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
        f"{xiaoyuzhou_url_count} Xiaoyuzhou URLs, "
        f"{qwen_chain_count} complete Qwen ASR chains."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
