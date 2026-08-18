#!/usr/bin/env python3
"""Validate PodWiki content, source URLs, and complete Qwen ASR chains."""

from __future__ import annotations

import hashlib
import json
import math
import re
import sys
from datetime import datetime
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import urlsplit

from qwen3_asr_transformers_adapter import (
    DEFAULT_ALIGNER as CUDA_QWEN_ALIGNER,
    DEFAULT_ALIGNER_REVISION as CUDA_QWEN_ALIGNER_REVISION,
    DEFAULT_MODEL as CUDA_QWEN_MODEL,
    DEFAULT_MODEL_REVISION as CUDA_QWEN_MODEL_REVISION,
    TORCH_PUBLIC_VERSION as CUDA_TORCH_VERSION,
    TRANSFORMERS_PACKAGE_VERSION as CUDA_TRANSFORMERS_VERSION,
)


ROOT = Path(__file__).resolve().parents[1]
SHOWS_ROOT = ROOT / "shows"
BILIBILI_URL_RE = re.compile(r"https://www\.bilibili\.com/video/[^\s)\]\"']+")
CANONICAL_BILIBILI_URL_RE = re.compile(r"https://www\.bilibili\.com/video/BV[A-Za-z0-9]+/")
CANONICAL_BILIBILI_VIDEO_RE = re.compile(
    r"https://www\.bilibili\.com/video/(?P<bvid>BV[A-Za-z0-9]+)/"
)
XIAOYUZHOU_URL_RE = re.compile(r"https://www\.xiaoyuzhoufm\.com/(?:episode|podcast)/[^\s)\]\"']+")
CANONICAL_XIAOYUZHOU_URL_RE = re.compile(
    r"https://www\.xiaoyuzhoufm\.com/(?:episode|podcast)/[0-9a-f]{24}"
)
CANONICAL_XIAOYUZHOU_EPISODE_RE = re.compile(
    r"https://www\.xiaoyuzhoufm\.com/episode/(?P<eid>[0-9a-f]{24})"
)
YOUTUBE_URL_RE = re.compile(r"https://www\.youtube\.com/(?:watch\?v=|playlist\?list=)[^\s)\]\"']+")
CANONICAL_YOUTUBE_VIDEO_RE = re.compile(
    r"https://www\.youtube\.com/watch\?v=(?P<video_id>[A-Za-z0-9_-]{11})"
)
CANONICAL_YOUTUBE_PLAYLIST_RE = re.compile(
    r"https://www\.youtube\.com/playlist\?list=(?P<playlist_id>[A-Za-z0-9_-]{10,64})"
)
TRACKING_PARAMETERS = ("spm_id_from", "vd_source")
QWEN_JSON_ARTIFACT_NAMES = (
    "raw.json",
    "aligned.json",
    "refined.json",
)
DEFAULT_QWEN_TRANSCRIPT_NAME = "transcript.zh-CN.md"
QWEN_TRANSCRIPT_NAME_RE = re.compile(r"transcript\.[A-Za-z]{2,3}(?:-[A-Za-z0-9]{2,8})*\.md")
SHA256_RE = re.compile(r"[0-9a-f]{64}")
SHOW_ID_RE = re.compile(r"[a-z0-9]+")
EPISODE_KEY_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
RFC3339_RE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})")
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
EPISODE_RELEASE_TYPES = {"regular", "special", "bonus"}
NUMBERING_STATUSES = {"verified", "not-in-publisher-feed", "unknown"}
PARTICIPANT_ROLES = {"guest", "participant", "host"}
PARTICIPANT_FIELDS = {"id", "name", "role", "aliases", "profile"}
SHOW_STATUSES = {"active", "inactive", "archived"}
SOURCE_PLATFORMS = {
    "apple-podcasts",
    "bilibili",
    "rss",
    "website",
    "xiaoyuzhou",
    "youtube",
}
SOURCE_KINDS = {
    "audio",
    "channel",
    "episode",
    "feed",
    "feed-item",
    "podcast",
    "playlist",
    "show",
    "video",
    "video-channel",
}
SOURCE_FIELDS = {
    "platform",
    "kind",
    "title",
    "external_id",
    "url",
    "preferred",
    "identifiers",
}
SOURCE_IDENTIFIER_FIELDS = {
    "aid",
    "apple_podcasts_id",
    "bvid",
    "cid",
    "channel_id",
    "eid",
    "episode_id",
    "episode_number",
    "feed_url",
    "guid",
    "media_id",
    "mid",
    "page",
    "page_id",
    "pid",
    "playlist_id",
    "rss_guid",
    "show_id",
    "video_id",
}
SHOW_FIELDS = {
    "schema_version",
    "kind",
    "id",
    "title",
    "aliases",
    "language",
    "status",
    "formats",
    "topics",
    "sources",
    "last_verified_at",
}
ASR_SELECTION_STATUSES = {"candidate", "selected", "superseded", "rejected"}
SUMMARY_SELECTION_STATUSES = {"selected", "superseded"}
SUMMARY_TIMESTAMP_RE = re.compile(r"\[(\d{2}:[0-5]\d:[0-5]\d)\]")
XIAOYUZHOU_MEDIA_ID_RE = re.compile(r"(?P<pid>[0-9a-f]{24})/[A-Za-z0-9_-]+\.m4a")
GIT_COMMIT_RE = re.compile(r"[0-9a-f]{40}")
MODEL_IDENTITY_REQUIRED_FILES = {"config.json"}
MLX_QWEN_ENGINE = "mlx-audio"
MLX_QWEN_MODEL = "mlx-community/Qwen3-ASR-1.7B-8bit"
MLX_QWEN_MODEL_REVISION = "a8379a2e2f9e313c9292cdf1af4055ab56d50d55"
MLX_QWEN_ALIGNER = "mlx-community/Qwen3-ForcedAligner-0.6B-8bit"
MLX_QWEN_ALIGNER_REVISION = "0e1a68e91d815300c7c9754b2a7639378b23db15"
MLX_SAMPLE_RATE_HZ = 16_000
MAX_SAFE_JSON_INTEGER = (1 << 53) - 1
MLX_MIN_AUDIO_DURATION_SECONDS = 0.001
MLX_MAX_AUDIO_DURATION_SECONDS = 359_999.999
MLX_MIN_CHUNK_DURATION_SECONDS = 1.0
MLX_MAX_CHUNK_DURATION_SECONDS = 300.0
MLX_MIN_AUDIO_SAMPLE_COUNT = math.ceil(MLX_MIN_AUDIO_DURATION_SECONDS * MLX_SAMPLE_RATE_HZ)
MLX_MAX_AUDIO_SAMPLE_COUNT = int(MLX_MAX_AUDIO_DURATION_SECONDS * MLX_SAMPLE_RATE_HZ)
MLX_MAX_PLANNED_CHUNK_COUNT = math.ceil(
    MLX_MAX_AUDIO_DURATION_SECONDS / MLX_MIN_CHUNK_DURATION_SECONDS
)
MLX_RAW_TIMESTAMP_ROUNDING_SECONDS = 0.001
MLX_RAW_FLOAT_COMPARISON_EPSILON_SECONDS = 1e-9
MLX_RAW_BOUNDARY_TOLERANCE_SECONDS = (
    MLX_RAW_TIMESTAMP_ROUNDING_SECONDS + MLX_RAW_FLOAT_COMPARISON_EPSILON_SECONDS
)
MLX_RAW_CUMULATIVE_BOUNDARY_TOLERANCE_SECONDS = (
    2 * MLX_RAW_TIMESTAMP_ROUNDING_SECONDS + MLX_RAW_FLOAT_COMPARISON_EPSILON_SECONDS
)
MLX_PER_CHUNK_TOKEN_BUDGET_SCOPE = "per-planned-chunk-v1"
MLX_LEGACY_ADAPTIVE_TOKEN_BUDGET_SCOPE = "adaptive-bisect-per-leaf-v1"
MLX_ADAPTIVE_TOKEN_BUDGET_SCOPE = "adaptive-bisect-per-leaf-v2"
MLX_ADAPTIVE_SPLIT_ALGORITHM = "adaptive-low-energy-bisect-v1"
MLX_ADAPTIVE_MIN_LEAF_SAMPLES = 20 * MLX_SAMPLE_RATE_HZ
MLX_LEGACY_ADAPTIVE_MAX_DEPTH = 3
MLX_ADAPTIVE_MAX_DEPTH = 4
MLX_ADAPTIVE_DEPTH_BY_SCOPE = {
    MLX_LEGACY_ADAPTIVE_TOKEN_BUDGET_SCOPE: MLX_LEGACY_ADAPTIVE_MAX_DEPTH,
    MLX_ADAPTIVE_TOKEN_BUDGET_SCOPE: MLX_ADAPTIVE_MAX_DEPTH,
}
MLX_ADAPTIVE_MAX_SPLIT_COUNT = 64
MLX_ADAPTIVE_ENERGY_WINDOW_SAMPLES = MLX_SAMPLE_RATE_HZ // 10
MLX_ADAPTIVE_QUANTIZATION = "pcm-s16-round-half-away-v1"
MLX_ADAPTIVE_TIE_BREAK = "energy-center-left-v1"
CUDA_QWEN_ENGINE = "qwen-asr-transformers"
CUDA_QWEN_BACKEND = "transformers-native"
LEGACY_CUDA_QWEN_MODEL = "Qwen/Qwen3-ASR-1.7B"
LEGACY_CUDA_QWEN_ALIGNER = "Qwen/Qwen3-ForcedAligner-0.6B"
LEGACY_CUDA_QWEN_BACKEND = "qwen-asr"


def bounded_json_number(
    value: Any,
    *,
    field: str,
    minimum: float,
    maximum: float,
    errors: list[str],
    maximum_exclusive: bool = False,
) -> float | None:
    """Validate an untrusted JSON number without leaking conversion errors."""

    if isinstance(value, bool) or not isinstance(value, (int, float)):
        errors.append(f"{field} must be a finite number in the supported range")
        return None
    try:
        number = float(value)
    except (OverflowError, TypeError, ValueError):
        errors.append(f"{field} must be a finite number in the supported range")
        return None
    if (
        not math.isfinite(number)
        or number < minimum
        or (number >= maximum if maximum_exclusive else number > maximum)
    ):
        upper_comparison = "<" if maximum_exclusive else "<="
        errors.append(
            f"{field} must be a finite number with {minimum} <= value {upper_comparison} {maximum}"
        )
        return None
    return number


def bounded_json_integer(
    value: Any,
    *,
    field: str,
    minimum: int,
    maximum: int,
    errors: list[str],
) -> int | None:
    """Validate an untrusted JSON integer, rejecting bool and arbitrary bignums."""

    if type(value) is not int or not minimum <= value <= maximum:
        errors.append(f"{field} must be an integer in [{minimum}, {maximum}]")
        return None
    return value


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
        errors.append(f"{display_path(path, repository_root)} is not strict JSON: {error}")
        return None

    if not isinstance(document, dict):
        errors.append(f"{display_path(path, repository_root)} JSON root must be an object")
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


def nested_front_matter_scalar(lines: list[str], section: str, key: str) -> str | None:
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


def decode_yaml_primitive(value: str) -> Any:
    """Decode the conservative scalar/list subset used by PodWiki front matter."""

    raw = value.strip()
    if raw == "[]":
        return []
    if raw.lower() in {"null", "~"}:
        return None
    if raw == "true":
        return True
    if raw == "false":
        return False
    if re.fullmatch(r"-?\d+", raw):
        return int(raw)
    return decode_yaml_scalar(raw)


def top_level_front_matter_value(lines: list[str], key: str) -> Any:
    raw = top_level_front_matter_raw_scalar(lines, key)
    return decode_yaml_primitive(raw) if raw is not None else None


def top_level_front_matter_keys(lines: list[str]) -> list[str]:
    return [
        line.split(":", 1)[0].strip()
        for line in lines
        if line and not line.startswith(" ") and ":" in line
    ]


def parse_top_level_scalar_list(lines: list[str], section: str) -> tuple[bool, list[Any]]:
    """Parse the block or empty scalar-list subset used by show metadata."""

    values: list[Any] = []
    present = False
    in_section = False
    for line in lines:
        stripped = line.strip()
        indent = len(line) - len(line.lstrip(" "))
        if not in_section:
            if indent == 0 and stripped.startswith(f"{section}:"):
                present = True
                inline = stripped.split(":", 1)[1].strip()
                if inline == "[]":
                    return True, []
                if inline:
                    return True, [decode_yaml_primitive(inline)]
                in_section = True
            continue
        if stripped and indent == 0:
            break
        if not stripped or stripped.startswith("#"):
            continue
        if indent == 2 and stripped.startswith("- "):
            values.append(decode_yaml_primitive(stripped[2:]))
    return present, values


def nested_front_matter_mapping(
    lines: list[str], section: str, nested: str | None = None
) -> dict[str, Any]:
    """Parse one small mapping at indent two, or a nested mapping at indent four."""

    result: dict[str, Any] = {}
    in_section = False
    in_nested = nested is None
    for line in lines:
        stripped = line.strip()
        indent = len(line) - len(line.lstrip(" "))
        if not in_section:
            if indent == 0 and stripped == f"{section}:":
                in_section = True
            continue
        if stripped and indent == 0:
            break
        if not stripped or stripped.startswith("#"):
            continue
        if nested is not None and indent == 2:
            in_nested = stripped == f"{nested}:"
            continue
        expected_indent = 4 if nested is not None else 2
        if in_nested and indent == expected_indent and ":" in stripped:
            key, value = stripped.split(":", 1)
            result[key.strip()] = decode_yaml_primitive(value)
    return result


def parse_front_matter_list(lines: list[str], section: str) -> tuple[bool, list[dict[str, Any]]]:
    """Parse the list-of-mappings subset used by sources and participants."""

    items: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    nested_field: str | None = None
    present = False
    in_section = False

    for line in lines:
        stripped = line.strip()
        indent = len(line) - len(line.lstrip(" "))
        if not in_section:
            if indent == 0 and stripped.startswith(f"{section}:"):
                present = True
                in_section = True
                inline = stripped.split(":", 1)[1].strip()
                if inline == "[]":
                    return True, []
            continue
        if stripped and indent == 0:
            break
        if not stripped or stripped.startswith("#"):
            continue

        if indent == 2 and (stripped == "-" or stripped.startswith("- ")):
            current = {}
            items.append(current)
            nested_field = None
            inline = stripped[1:].strip()
            if inline and ":" in inline:
                key, value = inline.split(":", 1)
                current[key.strip()] = decode_yaml_primitive(value)
            continue
        if current is None:
            continue
        if indent == 4 and ":" in stripped:
            key, value = stripped.split(":", 1)
            key = key.strip()
            raw_value = value.strip()
            if raw_value:
                current[key] = decode_yaml_primitive(raw_value)
                nested_field = None
            else:
                current[key] = {}
                nested_field = key
            continue
        if indent == 6 and nested_field is not None:
            nested_value = current.get(nested_field)
            if stripped == "-" or stripped.startswith("- "):
                if not isinstance(nested_value, list):
                    nested_value = []
                    current[nested_field] = nested_value
                nested_value.append(decode_yaml_primitive(stripped[1:]))
            elif ":" in stripped:
                if not isinstance(nested_value, dict):
                    continue
                key, value = stripped.split(":", 1)
                nested_value[key.strip()] = decode_yaml_primitive(value)

    return present, items


def is_calendar_date(value: Any) -> bool:
    if not isinstance(value, str) or CALENDAR_DATE_RE.fullmatch(value) is None:
        return False
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        return False
    return True


def is_absolute_url(value: Any, *, scheme: str | None = None) -> bool:
    if not isinstance(value, str) or not value:
        return False
    try:
        parsed = urlsplit(value)
    except ValueError:
        return False
    return bool(parsed.scheme and parsed.netloc) and (scheme is None or parsed.scheme == scheme)


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
                    errors.append("transcript.translations items must be YAML mappings")
                    continue
                key, value = item.split(":", 1)
                current[key.strip()] = decode_yaml_scalar(value)
            continue
        if indent == 6 and current is not None and ":" in stripped:
            key, value = stripped.split(":", 1)
            key = key.strip()
            if key in current:
                errors.append(f"transcript.translations item has duplicate field {key!r}")
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
            errors.append(f"{field_prefix} profile must be attached to a participants list item")
            return
        if profile_seen:
            errors.append(f"{profile_field(participant_index)} has a duplicate profile field")
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
            else:
                errors.append(f"{base_field} contains unsupported field {key!r}")
            continue

        if indent == 8 and current_list_name is not None:
            state = lists[current_list_name]
            if not (stripped == "-" or stripped.startswith("- ")):
                state["mode"] = "invalid"
                errors.append(f"{base_field}.{current_list_name} must be a YAML list")
                current_list_item = None
                continue
            item: dict[str, str | None] = {}
            state["items"].append(item)
            current_list_item = item
            inline = stripped[1:].strip()
            if not inline:
                continue
            if ":" not in inline:
                errors.append(f"{base_field}.{current_list_name} items must be YAML mappings")
                continue
            key, raw_value = inline.split(":", 1)
            item[key.strip()] = decode_non_empty_yaml_scalar(raw_value)
            continue

        if indent == 10 and current_list_name is not None and current_list_item is not None:
            if ":" not in stripped:
                errors.append(f"{base_field}.{current_list_name} items must be YAML mappings")
                continue
            key, raw_value = stripped.split(":", 1)
            key = key.strip()
            if key in current_list_item:
                errors.append(f"{base_field}.{current_list_name} item has duplicate field {key!r}")
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
            isinstance(checked_at, str) and CALENDAR_DATE_RE.fullmatch(checked_at) is not None
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
                allowed = (
                    {"organization", "title", "status"}
                    if list_name == "affiliations"
                    else {"institution", "credential", "field"}
                )
                unknown = set(item).difference(allowed)
                if unknown:
                    errors.append(
                        f"{item_field} contains unsupported fields: {', '.join(sorted(unknown))}"
                    )
                required = (
                    ("organization", "status") if list_name == "affiliations" else ("institution",)
                )
                for key in required:
                    if item.get(key) is None:
                        errors.append(f"{item_field}.{key} must be a non-empty string")
                optional = ("title",) if list_name == "affiliations" else ("credential", "field")
                for key in optional:
                    if key in item and item[key] is None:
                        errors.append(f"{item_field}.{key} must be a non-empty string when present")
                if list_name == "affiliations" and item.get("status") not in {
                    "current",
                    "former",
                    None,
                }:
                    errors.append(f"{item_field}.status must be one of current, former")


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
            f"{field} must point to {display_path(expected, repository_root)}, not {value!r}"
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


def validate_model_identity(value: Any, *, field: str, errors: list[str]) -> dict[str, Any] | None:
    if not isinstance(value, dict):
        errors.append(f"{field} must be an object")
        return None
    expected_fields = {
        "schema_version",
        "repository",
        "requested_revision",
        "resolved_commit",
        "files_sha256",
    }
    if set(value) != expected_fields:
        errors.append(f"{field} fields must exactly match model identity schema version 1")
    if type(value.get("schema_version")) is not int or value.get("schema_version") != 1:
        errors.append(f"{field}.schema_version must be the strict integer 1")
    for key in expected_fields:
        if key not in value:
            errors.append(f"{field}.{key} is missing")
    for key in ("repository",):
        if not isinstance(value.get(key), str) or not value.get(key):
            errors.append(f"{field}.{key} must be non-empty")
    requested = value.get("requested_revision")
    resolved = value.get("resolved_commit")
    if not isinstance(requested, str) or GIT_COMMIT_RE.fullmatch(requested) is None:
        errors.append(f"{field}.requested_revision must be a 40-character commit")
    if not isinstance(resolved, str) or GIT_COMMIT_RE.fullmatch(resolved) is None:
        errors.append(f"{field}.resolved_commit must be a 40-character commit")
    if requested != resolved:
        errors.append(f"{field}.requested_revision must equal resolved_commit")
    files = value.get("files_sha256")
    if (
        not isinstance(files, dict)
        or "config.json" not in files
        or not any(
            isinstance(path, str) and path.endswith(".safetensors")
            for path in files
            if isinstance(files, dict)
        )
    ):
        errors.append(f"{field}.files_sha256 must include config.json and safetensors")
    elif isinstance(files, dict):
        for path, digest in files.items():
            valid_path = isinstance(path, str) and bool(path) and "\\" not in path
            if valid_path:
                pure = PurePosixPath(path)
                valid_path = (
                    not pure.is_absolute()
                    and re.match(r"^[A-Za-z]:", path) is None
                    and all(part not in {"", ".", ".."} for part in pure.parts)
                )
            if not valid_path:
                errors.append(f"{field}.files_sha256 keys must be normalized relative POSIX paths")
                break
            if not isinstance(digest, str) or SHA256_RE.fullmatch(digest) is None:
                errors.append(f"{field}.files_sha256 values must be lowercase SHA-256 digests")
                break
    return value


def validate_pinned_qwen_identity(
    identity: dict[str, Any] | None,
    *,
    field: str,
    repository: str,
    revision: str,
    errors: list[str],
) -> None:
    if identity is None:
        return
    if identity.get("repository") != repository:
        errors.append(f"{field}.repository must equal {repository!r}")
    if identity.get("requested_revision") != revision:
        errors.append(f"{field}.requested_revision must equal {revision!r}")
    if identity.get("resolved_commit") != revision:
        errors.append(f"{field}.resolved_commit must equal {revision!r}")


def validate_mlx_adaptive_generation_plan(
    raw: dict[str, Any],
    *,
    segments: list[Any],
    sample_count: int,
    max_tokens_per_chunk: int,
    initial_chunk_count: int,
    generation_tokens: int,
    errors: list[str],
) -> int | None:
    """Replay adaptive split geometry and validate its leaf/cost evidence."""

    options = raw.get("options")
    performance = raw.get("performance")
    if not isinstance(options, dict) or not isinstance(performance, dict):
        return None
    adaptive_scope = options.get("token_budget_scope")
    adaptive_max_depth = MLX_ADAPTIVE_DEPTH_BY_SCOPE.get(adaptive_scope)
    if adaptive_max_depth is None:
        errors.append("Qwen MLX adaptive raw has an unsupported token budget scope")
        return None
    expected_options = {
        "adaptive_split_algorithm": MLX_ADAPTIVE_SPLIT_ALGORITHM,
        "adaptive_min_leaf_samples": MLX_ADAPTIVE_MIN_LEAF_SAMPLES,
        "adaptive_max_depth": adaptive_max_depth,
        "adaptive_max_split_count": MLX_ADAPTIVE_MAX_SPLIT_COUNT,
        "adaptive_energy_window_samples": MLX_ADAPTIVE_ENERGY_WINDOW_SAMPLES,
        "adaptive_quantization": MLX_ADAPTIVE_QUANTIZATION,
        "adaptive_tie_break": MLX_ADAPTIVE_TIE_BREAK,
    }
    for field, expected in expected_options.items():
        actual = options.get(field)
        if actual != expected or type(actual) is not type(expected):
            errors.append(f"Qwen MLX adaptive raw.options.{field} must equal {expected!r}")

    final_leaf_count = bounded_json_integer(
        options.get("final_leaf_chunk_count"),
        field="Qwen MLX adaptive raw.options.final_leaf_chunk_count",
        minimum=1,
        maximum=MLX_MAX_PLANNED_CHUNK_COUNT + MLX_ADAPTIVE_MAX_SPLIT_COUNT,
        errors=errors,
    )
    split_count = bounded_json_integer(
        options.get("adaptive_split_count"),
        field="Qwen MLX adaptive raw.options.adaptive_split_count",
        minimum=0,
        maximum=MLX_ADAPTIVE_MAX_SPLIT_COUNT,
        errors=errors,
    )
    if final_leaf_count is not None and final_leaf_count != len(segments):
        errors.append("Qwen MLX adaptive final_leaf_chunk_count must equal the raw segment count")
    if (
        final_leaf_count is not None
        and split_count is not None
        and final_leaf_count != initial_chunk_count + split_count
    ):
        errors.append(
            "Qwen MLX adaptive final leaf count must equal planned_chunk_count + "
            "adaptive_split_count"
        )

    prompt_tokens = bounded_json_integer(
        performance.get("prompt_tokens"),
        field="Qwen MLX adaptive raw.performance.prompt_tokens",
        minimum=0,
        maximum=MAX_SAFE_JSON_INTEGER,
        errors=errors,
    )
    attempt_prompt_tokens = bounded_json_integer(
        performance.get("attempt_prompt_tokens"),
        field="Qwen MLX adaptive raw.performance.attempt_prompt_tokens",
        minimum=0,
        maximum=MAX_SAFE_JSON_INTEGER,
        errors=errors,
    )
    attempt_generation_tokens = bounded_json_integer(
        performance.get("attempt_generation_tokens"),
        field="Qwen MLX adaptive raw.performance.attempt_generation_tokens",
        minimum=0,
        maximum=MAX_SAFE_JSON_INTEGER,
        errors=errors,
    )
    if split_count is not None and attempt_generation_tokens is not None:
        expected_attempt_tokens = generation_tokens + split_count * max_tokens_per_chunk
        if attempt_generation_tokens != expected_attempt_tokens:
            errors.append(
                "Qwen MLX adaptive attempt_generation_tokens must include every "
                "discarded exhausted parent"
            )
    generation_call_count = bounded_json_integer(
        performance.get("generation_call_count"),
        field="Qwen MLX adaptive raw.performance.generation_call_count",
        minimum=1,
        maximum=MLX_MAX_PLANNED_CHUNK_COUNT + 2 * MLX_ADAPTIVE_MAX_SPLIT_COUNT,
        errors=errors,
    )
    if (
        split_count is not None
        and generation_call_count is not None
        and generation_call_count != initial_chunk_count + 2 * split_count
    ):
        errors.append(
            "Qwen MLX adaptive generation_call_count must equal planned chunks + 2 * splits"
        )

    plan = raw.get("generation_plan")
    expected_plan_fields = {
        "schema_version",
        "pcm_s16le_sha256",
        "initial_chunk_boundaries_samples",
        "split_events",
    }
    if not isinstance(plan, dict) or set(plan) != expected_plan_fields:
        errors.append("Qwen MLX adaptive raw.generation_plan has invalid fields")
        return final_leaf_count
    if type(plan.get("schema_version")) is not int or plan.get("schema_version") != 1:
        errors.append("Qwen MLX adaptive raw.generation_plan.schema_version must equal 1")
    valid_sha256(
        plan.get("pcm_s16le_sha256"),
        field="Qwen MLX adaptive raw.generation_plan.pcm_s16le_sha256",
        errors=errors,
    )

    boundaries = plan.get("initial_chunk_boundaries_samples")
    if not isinstance(boundaries, list) or len(boundaries) != initial_chunk_count + 1:
        errors.append(
            "Qwen MLX adaptive initial_chunk_boundaries_samples must match planned chunks"
        )
        return final_leaf_count
    validated_boundaries: list[int] = []
    for index, boundary in enumerate(boundaries):
        value = bounded_json_integer(
            boundary,
            field=(
                f"Qwen MLX adaptive raw.generation_plan.initial_chunk_boundaries_samples[{index}]"
            ),
            minimum=0,
            maximum=sample_count,
            errors=errors,
        )
        if value is None:
            return final_leaf_count
        validated_boundaries.append(value)
    if (
        validated_boundaries[0] != 0
        or validated_boundaries[-1] != sample_count
        or any(right <= left for left, right in zip(validated_boundaries, validated_boundaries[1:]))
    ):
        errors.append("Qwen MLX adaptive initial boundaries must continuously cover the audio")
        return final_leaf_count

    split_events = plan.get("split_events")
    if not isinstance(split_events, list):
        errors.append("Qwen MLX adaptive raw.generation_plan.split_events must be a list")
        return final_leaf_count
    if split_count is None or len(split_events) != split_count:
        errors.append("Qwen MLX adaptive split_events must match adaptive_split_count")
        return final_leaf_count

    active_nodes: dict[tuple[int, str], tuple[int, int]] = {
        (index, ""): (validated_boundaries[index], validated_boundaries[index + 1])
        for index in range(initial_chunk_count)
    }
    event_fields = {
        "initial_chunk_id",
        "split_path",
        "depth",
        "parent_start_sample",
        "parent_end_sample",
        "legal_start_sample",
        "legal_end_sample",
        "split_sample",
        "cut_energy_sum_squares",
        "parent_prompt_tokens",
        "parent_generation_tokens",
    }
    maximum_window_energy = MLX_ADAPTIVE_ENERGY_WINDOW_SAMPLES * 32768**2
    discarded_prompt_tokens = 0
    for index, event in enumerate(split_events):
        field_prefix = f"Qwen MLX adaptive raw.generation_plan.split_events[{index}]"
        if not isinstance(event, dict) or set(event) != event_fields:
            errors.append(f"{field_prefix} has invalid fields")
            return final_leaf_count
        initial_chunk_id = bounded_json_integer(
            event.get("initial_chunk_id"),
            field=f"{field_prefix}.initial_chunk_id",
            minimum=0,
            maximum=initial_chunk_count - 1,
            errors=errors,
        )
        split_path = event.get("split_path")
        if (
            not isinstance(split_path, str)
            or len(split_path) >= adaptive_max_depth
            or any(step not in "LR" for step in split_path)
        ):
            errors.append(f"{field_prefix}.split_path is invalid")
            return final_leaf_count
        depth = bounded_json_integer(
            event.get("depth"),
            field=f"{field_prefix}.depth",
            minimum=0,
            maximum=adaptive_max_depth - 1,
            errors=errors,
        )
        if initial_chunk_id is None or depth is None:
            return final_leaf_count
        if depth != len(split_path):
            errors.append(f"{field_prefix}.depth must equal the split path length")
            return final_leaf_count
        key = (initial_chunk_id, split_path)
        if key not in active_nodes:
            errors.append(f"{field_prefix} must name a currently active tree node")
            return final_leaf_count
        parent_start, parent_end = active_nodes[key]
        legal_start = parent_start + MLX_ADAPTIVE_MIN_LEAF_SAMPLES
        legal_end = parent_end - MLX_ADAPTIVE_MIN_LEAF_SAMPLES
        if legal_start > legal_end:
            errors.append(f"{field_prefix} cannot preserve the adaptive leaf minimum")
            return final_leaf_count
        expected_event_values = {
            "parent_start_sample": parent_start,
            "parent_end_sample": parent_end,
            "legal_start_sample": legal_start,
            "legal_end_sample": legal_end,
            "parent_generation_tokens": max_tokens_per_chunk,
        }
        for field, expected in expected_event_values.items():
            actual = event.get(field)
            if type(actual) is not int or actual != expected:
                errors.append(f"{field_prefix}.{field} must equal {expected}")
                return final_leaf_count
        split_sample = bounded_json_integer(
            event.get("split_sample"),
            field=f"{field_prefix}.split_sample",
            minimum=legal_start,
            maximum=legal_end,
            errors=errors,
        )
        bounded_json_integer(
            event.get("cut_energy_sum_squares"),
            field=f"{field_prefix}.cut_energy_sum_squares",
            minimum=0,
            maximum=maximum_window_energy,
            errors=errors,
        )
        parent_prompt_tokens = bounded_json_integer(
            event.get("parent_prompt_tokens"),
            field=f"{field_prefix}.parent_prompt_tokens",
            minimum=0,
            maximum=MAX_SAFE_JSON_INTEGER,
            errors=errors,
        )
        if parent_prompt_tokens is None:
            return final_leaf_count
        if discarded_prompt_tokens > MAX_SAFE_JSON_INTEGER - parent_prompt_tokens:
            errors.append(
                "Qwen MLX adaptive discarded parent prompt-token sum exceeds the "
                "JSON safe-integer limit"
            )
            return final_leaf_count
        discarded_prompt_tokens += parent_prompt_tokens
        if split_sample is None:
            return final_leaf_count
        del active_nodes[key]
        active_nodes[(initial_chunk_id, f"{split_path}L")] = (parent_start, split_sample)
        active_nodes[(initial_chunk_id, f"{split_path}R")] = (split_sample, parent_end)

    if (
        prompt_tokens is not None
        and attempt_prompt_tokens is not None
        and attempt_prompt_tokens != prompt_tokens + discarded_prompt_tokens
    ):
        errors.append("Qwen MLX adaptive attempt_prompt_tokens must include every discarded parent")

    ordered_leaves = sorted(
        (
            (start, end, initial_chunk_id, split_path)
            for (initial_chunk_id, split_path), (start, end) in active_nodes.items()
        ),
        key=lambda leaf: (leaf[0], leaf[1]),
    )
    if final_leaf_count is not None and len(ordered_leaves) != final_leaf_count:
        errors.append("Qwen MLX adaptive split tree does not yield final_leaf_chunk_count")
        return final_leaf_count
    segment_fields = {
        "id",
        "initial_chunk_id",
        "split_path",
        "start_sample",
        "end_sample",
        "start",
        "end",
        "text",
        "generation_tokens",
    }
    for index, (segment, leaf) in enumerate(zip(segments, ordered_leaves)):
        field_prefix = f"Qwen MLX adaptive raw.segments[{index}]"
        if not isinstance(segment, dict) or set(segment) != segment_fields:
            errors.append(f"{field_prefix} has invalid adaptive leaf fields")
            continue
        start, end, initial_chunk_id, split_path = leaf
        expected_values = {
            "initial_chunk_id": initial_chunk_id,
            "split_path": split_path,
            "start_sample": start,
            "end_sample": end,
        }
        for field, expected in expected_values.items():
            actual = segment.get(field)
            if actual != expected or type(actual) is not type(expected):
                errors.append(f"{field_prefix}.{field} must equal {expected!r}")
        start_seconds = bounded_json_number(
            segment.get("start"),
            field=f"{field_prefix}.start",
            minimum=0.0,
            maximum=MLX_MAX_AUDIO_DURATION_SECONDS,
            errors=errors,
        )
        end_seconds = bounded_json_number(
            segment.get("end"),
            field=f"{field_prefix}.end",
            minimum=0.0,
            maximum=MLX_MAX_AUDIO_DURATION_SECONDS,
            errors=errors,
        )
        if start_seconds is not None and not math.isclose(
            start_seconds,
            start / MLX_SAMPLE_RATE_HZ,
            rel_tol=0.0,
            abs_tol=MLX_RAW_FLOAT_COMPARISON_EPSILON_SECONDS,
        ):
            errors.append(f"{field_prefix}.start must exactly match start_sample")
        if end_seconds is not None and not math.isclose(
            end_seconds,
            end / MLX_SAMPLE_RATE_HZ,
            rel_tol=0.0,
            abs_tol=MLX_RAW_FLOAT_COMPARISON_EPSILON_SECONDS,
        ):
            errors.append(f"{field_prefix}.end must exactly match end_sample")
    return final_leaf_count


def validate_mlx_qwen_v2_raw_coverage(raw: dict[str, Any], *, errors: list[str]) -> None:
    """Fail closed when a strict MLX v2 raw artifact does not cover its audio."""

    audio = raw.get("audio")
    duration_seconds: float | None = None
    sample_count: Any = None
    sample_count_recorded = False
    if not isinstance(audio, dict):
        errors.append("Qwen MLX v2 raw.audio must be an object")
    else:
        sample_count_recorded = "sample_count" in audio
        sample_count = audio.get("sample_count")
        duration_seconds = bounded_json_number(
            audio.get("duration_seconds"),
            field="Qwen MLX v2 raw.audio.duration_seconds",
            minimum=MLX_MIN_AUDIO_DURATION_SECONDS,
            maximum=MLX_MAX_AUDIO_DURATION_SECONDS,
            errors=errors,
        )

    options = raw.get("options")
    max_tokens_per_chunk: int | None = None
    chunk_duration_seconds: float | None = None
    planned_chunk_count: Any = None
    effective_total_token_budget: Any = None
    planned_chunk_count_recorded = False
    effective_total_token_budget_recorded = False
    per_chunk_token_budget = False
    adaptive_token_budget = False
    if not isinstance(options, dict):
        errors.append("Qwen MLX v2 raw.options must be an object")
    else:
        planned_chunk_count_recorded = "planned_chunk_count" in options
        planned_chunk_count = options.get("planned_chunk_count")
        effective_total_token_budget_recorded = "effective_total_token_budget" in options
        effective_total_token_budget = options.get("effective_total_token_budget")
        if "token_budget_scope" in options:
            token_budget_scope = options.get("token_budget_scope")
            if token_budget_scope not in {
                MLX_PER_CHUNK_TOKEN_BUDGET_SCOPE,
                MLX_LEGACY_ADAPTIVE_TOKEN_BUDGET_SCOPE,
                MLX_ADAPTIVE_TOKEN_BUDGET_SCOPE,
            }:
                errors.append("Qwen MLX v2 raw.options.token_budget_scope has an unsupported value")
            else:
                per_chunk_token_budget = True
                adaptive_token_budget = token_budget_scope in MLX_ADAPTIVE_DEPTH_BY_SCOPE
                if raw.get("lineage_schema_version") != 2:
                    errors.append("Qwen MLX per-chunk token budget scope requires v2 lineage")
                if adaptive_token_budget and (
                    isinstance(options.get("temperature"), bool)
                    or not isinstance(options.get("temperature"), (int, float))
                    or options.get("temperature") != 0.0
                ):
                    errors.append("Qwen MLX adaptive token budget scope requires temperature=0.0")
        max_tokens_per_chunk = bounded_json_integer(
            options.get("max_tokens_per_chunk"),
            field="Qwen MLX v2 raw.options.max_tokens_per_chunk",
            minimum=1,
            maximum=MAX_SAFE_JSON_INTEGER,
            errors=errors,
        )
        chunk_duration_seconds = bounded_json_number(
            options.get("chunk_duration_seconds"),
            field="Qwen MLX v2 raw.options.chunk_duration_seconds",
            minimum=MLX_MIN_CHUNK_DURATION_SECONDS,
            maximum=MLX_MAX_CHUNK_DURATION_SECONDS,
            maximum_exclusive=True,
            errors=errors,
        )

    performance = raw.get("performance")
    generation_tokens: int | None = None
    if not isinstance(performance, dict):
        errors.append("Qwen MLX v2 raw.performance must be an object")
    else:
        generation_tokens = bounded_json_integer(
            performance.get("generation_tokens"),
            field="Qwen MLX v2 raw.performance.generation_tokens",
            minimum=0,
            maximum=MAX_SAFE_JSON_INTEGER,
            errors=errors,
        )

    segments = raw.get("segments")
    if not isinstance(segments, list) or not segments:
        errors.append("Qwen MLX v2 raw.segments must be a non-empty list")
        return

    previous_start = -1.0
    previous_end = 0.0
    cumulative_gap_seconds = 0.0
    cumulative_overlap_seconds = 0.0
    segment_generation_tokens = 0
    segment_generation_tokens_valid = True
    for index, segment in enumerate(segments):
        if not isinstance(segment, dict):
            errors.append(f"Qwen MLX v2 raw.segments[{index}] must be an object")
            continue
        if type(segment.get("id")) is not int or segment.get("id") != index:
            errors.append(f"Qwen MLX v2 raw.segments[{index}].id must equal {index}")
        if per_chunk_token_budget:
            chunk_generation_tokens = bounded_json_integer(
                segment.get("generation_tokens"),
                field=(f"Qwen MLX v2 raw.segments[{index}].generation_tokens"),
                minimum=0,
                maximum=(
                    max_tokens_per_chunk - 1
                    if max_tokens_per_chunk is not None
                    else MAX_SAFE_JSON_INTEGER
                ),
                errors=errors,
            )
            if chunk_generation_tokens is None:
                segment_generation_tokens_valid = False
            elif segment_generation_tokens > MAX_SAFE_JSON_INTEGER - chunk_generation_tokens:
                errors.append(
                    "Qwen MLX v2 raw segment generation-token sum exceeds "
                    "the JSON safe-integer limit"
                )
                segment_generation_tokens_valid = False
            else:
                segment_generation_tokens += chunk_generation_tokens
        start_seconds = bounded_json_number(
            segment.get("start"),
            field=f"Qwen MLX v2 raw.segments[{index}].start",
            minimum=-MLX_RAW_BOUNDARY_TOLERANCE_SECONDS,
            maximum=(MLX_MAX_AUDIO_DURATION_SECONDS + MLX_RAW_BOUNDARY_TOLERANCE_SECONDS),
            errors=errors,
        )
        end_seconds = bounded_json_number(
            segment.get("end"),
            field=f"Qwen MLX v2 raw.segments[{index}].end",
            minimum=-MLX_RAW_BOUNDARY_TOLERANCE_SECONDS,
            maximum=(MLX_MAX_AUDIO_DURATION_SECONDS + MLX_RAW_BOUNDARY_TOLERANCE_SECONDS),
            errors=errors,
        )
        if start_seconds is None or end_seconds is None:
            continue
        if (
            start_seconds < previous_start
            or start_seconds < -MLX_RAW_BOUNDARY_TOLERANCE_SECONDS
            or end_seconds <= start_seconds
            or (
                duration_seconds is not None
                and end_seconds > duration_seconds + MLX_RAW_BOUNDARY_TOLERANCE_SECONDS
            )
        ):
            errors.append(f"Qwen MLX v2 raw.segments[{index}] has invalid timestamp bounds")
        boundary_delta = start_seconds - previous_end
        if not math.isclose(
            start_seconds,
            previous_end,
            rel_tol=0.0,
            abs_tol=MLX_RAW_BOUNDARY_TOLERANCE_SECONDS,
        ):
            errors.append(
                "Qwen MLX v2 raw.segments must continuously cover the audio "
                f"from zero; gap before segment {index}"
            )
        if boundary_delta > 0:
            cumulative_gap_seconds += boundary_delta
        else:
            cumulative_overlap_seconds -= boundary_delta
        previous_start = start_seconds
        previous_end = end_seconds

    if duration_seconds is not None:
        tail_delta = duration_seconds - previous_end
        if not math.isclose(
            previous_end,
            duration_seconds,
            rel_tol=0.0,
            abs_tol=MLX_RAW_BOUNDARY_TOLERANCE_SECONDS,
        ):
            errors.append(
                "Qwen MLX v2 raw.segments must cover the audio through its end: "
                f"last_end={previous_end} duration={duration_seconds}"
            )
        if tail_delta > 0:
            cumulative_gap_seconds += tail_delta
        else:
            cumulative_overlap_seconds -= tail_delta
    if cumulative_gap_seconds > MLX_RAW_CUMULATIVE_BOUNDARY_TOLERANCE_SECONDS:
        errors.append("Qwen MLX v2 raw.segments have excessive cumulative chunk-boundary gaps")
    if cumulative_overlap_seconds > MLX_RAW_CUMULATIVE_BOUNDARY_TOLERANCE_SECONDS:
        errors.append("Qwen MLX v2 raw.segments have excessive cumulative chunk-boundary overlaps")
    if per_chunk_token_budget:
        raw_text = raw.get("text")
        segment_texts = [segment.get("text") for segment in segments if isinstance(segment, dict)]
        if (
            not isinstance(raw_text, str)
            or len(segment_texts) != len(segments)
            or any(not isinstance(text, str) for text in segment_texts)
            or raw_text != " ".join(segment_texts)
        ):
            errors.append("Qwen MLX v2 raw.text must equal the ordered per-chunk segment text")

    precise_budget_markers = (
        sample_count_recorded,
        planned_chunk_count_recorded,
        effective_total_token_budget_recorded,
    )
    effective_budget: int | None = None
    if per_chunk_token_budget and not all(precise_budget_markers):
        errors.append(
            "Qwen MLX v2 raw per-chunk token budget scope requires precise token budget metadata"
        )
    if any(precise_budget_markers):
        if not all(precise_budget_markers):
            errors.append(
                "Qwen MLX v2 raw precise token budget metadata must include "
                "audio.sample_count, options.planned_chunk_count, and "
                "options.effective_total_token_budget"
            )
        else:
            sample_rate_hz = audio.get("sample_rate_hz") if isinstance(audio, dict) else None
            precise_metadata_valid = True
            validated_sample_count = bounded_json_integer(
                sample_count,
                field="Qwen MLX v2 raw.audio.sample_count",
                minimum=MLX_MIN_AUDIO_SAMPLE_COUNT,
                maximum=MLX_MAX_AUDIO_SAMPLE_COUNT,
                errors=errors,
            )
            if validated_sample_count is None:
                precise_metadata_valid = False
            if type(sample_rate_hz) is not int or sample_rate_hz != MLX_SAMPLE_RATE_HZ:
                errors.append(
                    f"Qwen MLX v2 raw.audio.sample_rate_hz must equal {MLX_SAMPLE_RATE_HZ}"
                )
                precise_metadata_valid = False
            validated_planned_chunk_count = bounded_json_integer(
                planned_chunk_count,
                field="Qwen MLX v2 raw.options.planned_chunk_count",
                minimum=1,
                maximum=MLX_MAX_PLANNED_CHUNK_COUNT,
                errors=errors,
            )
            if validated_planned_chunk_count is None:
                precise_metadata_valid = False
            elif not adaptive_token_budget and validated_planned_chunk_count != len(segments):
                errors.append(
                    "Qwen MLX v2 raw.options.planned_chunk_count must equal the raw segment count"
                )
                precise_metadata_valid = False
            validated_total_token_budget = bounded_json_integer(
                effective_total_token_budget,
                field=("Qwen MLX v2 raw.options.effective_total_token_budget"),
                minimum=1,
                maximum=MAX_SAFE_JSON_INTEGER,
                errors=errors,
            )
            if validated_total_token_budget is None:
                precise_metadata_valid = False
            if (
                validated_sample_count is not None
                and sample_rate_hz == MLX_SAMPLE_RATE_HZ
                and duration_seconds is not None
                and not math.isclose(
                    duration_seconds,
                    round(validated_sample_count / MLX_SAMPLE_RATE_HZ, 3),
                    rel_tol=0.0,
                    abs_tol=1e-9,
                )
            ):
                errors.append(
                    "Qwen MLX v2 raw.audio.duration_seconds must match its "
                    "sample_count and sample_rate_hz"
                )
                precise_metadata_valid = False
            budget_chunk_count = validated_planned_chunk_count
            if (
                adaptive_token_budget
                and validated_sample_count is not None
                and max_tokens_per_chunk is not None
                and validated_planned_chunk_count is not None
                and generation_tokens is not None
            ):
                adaptive_error_count = len(errors)
                budget_chunk_count = validate_mlx_adaptive_generation_plan(
                    raw,
                    segments=segments,
                    sample_count=validated_sample_count,
                    max_tokens_per_chunk=max_tokens_per_chunk,
                    initial_chunk_count=validated_planned_chunk_count,
                    generation_tokens=generation_tokens,
                    errors=errors,
                )
                if budget_chunk_count is None or len(errors) != adaptive_error_count:
                    precise_metadata_valid = False
            elif adaptive_token_budget:
                precise_metadata_valid = False
            if max_tokens_per_chunk is not None and budget_chunk_count is not None:
                expected_budget: int | None = None
                if max_tokens_per_chunk > MAX_SAFE_JSON_INTEGER // budget_chunk_count:
                    errors.append(
                        "Qwen MLX v2 raw effective token budget product exceeds "
                        "the JSON safe-integer limit"
                    )
                    precise_metadata_valid = False
                else:
                    expected_budget = max_tokens_per_chunk * budget_chunk_count
                if expected_budget is not None and validated_total_token_budget != expected_budget:
                    budget_count_field = (
                        "final_leaf_chunk_count" if adaptive_token_budget else "planned_chunk_count"
                    )
                    errors.append(
                        "Qwen MLX v2 raw.options.effective_total_token_budget "
                        f"must equal max_tokens_per_chunk * {budget_count_field}"
                    )
                    precise_metadata_valid = False
            else:
                precise_metadata_valid = False
            if precise_metadata_valid:
                effective_budget = validated_total_token_budget
    elif (
        duration_seconds is not None
        and max_tokens_per_chunk is not None
        and chunk_duration_seconds is not None
    ):
        # Old MLX v2 artifacts did not record the exact silence-aware split
        # plan. Keep their nominal-duration reconstruction fail-closed.
        nominal_chunk_count = math.ceil(duration_seconds / chunk_duration_seconds)
        if max_tokens_per_chunk > MAX_SAFE_JSON_INTEGER // nominal_chunk_count:
            errors.append(
                "Qwen MLX v2 raw reconstructed token budget exceeds the JSON safe-integer limit"
            )
        else:
            effective_budget = max_tokens_per_chunk * nominal_chunk_count

    if (
        generation_tokens is not None
        and effective_budget is not None
        and generation_tokens >= effective_budget
    ):
        errors.append(
            "Qwen MLX v2 raw.performance.generation_tokens exhausted its "
            f"effective full-audio token budget ({generation_tokens} >= "
            f"{effective_budget})"
        )
    if (
        per_chunk_token_budget
        and generation_tokens is not None
        and segment_generation_tokens_valid
        and generation_tokens != segment_generation_tokens
    ):
        errors.append(
            "Qwen MLX v2 raw segment generation_tokens must sum to "
            "raw.performance.generation_tokens"
        )


def validate_qwen_v2_backend_contract(
    raw: dict[str, Any],
    aligned: dict[str, Any],
    refined: dict[str, Any],
    *,
    raw_model_identity: dict[str, Any] | None,
    aligned_aligner_identity: dict[str, Any] | None,
    errors: list[str],
) -> None:
    """Require one of the two supported, pinned Qwen v2 backends."""

    aligned_source = aligned.get("source") if isinstance(aligned.get("source"), dict) else {}
    refined_source = refined.get("source") if isinstance(refined.get("source"), dict) else {}
    raw_engine = raw.get("engine")
    raw_model = raw.get("model")
    raw_options = raw.get("options")
    aligned_options = aligned.get("options")

    if raw_engine == MLX_QWEN_ENGINE:
        validate_mlx_qwen_v2_raw_coverage(raw, errors=errors)

    if raw_engine == MLX_QWEN_ENGINE and raw_model == MLX_QWEN_MODEL:
        expected_values = (
            ("raw.engine", raw_engine, MLX_QWEN_ENGINE),
            ("raw.model", raw_model, MLX_QWEN_MODEL),
            ("aligned.source.engine", aligned_source.get("engine"), MLX_QWEN_ENGINE),
            ("aligned.source.model", aligned_source.get("model"), MLX_QWEN_MODEL),
            (
                "aligned.source.aligner",
                aligned_source.get("aligner"),
                MLX_QWEN_ALIGNER,
            ),
            ("refined.source.engine", refined_source.get("engine"), MLX_QWEN_ENGINE),
            ("refined.source.model", refined_source.get("model"), MLX_QWEN_MODEL),
            (
                "refined.source.aligner",
                refined_source.get("aligner"),
                MLX_QWEN_ALIGNER,
            ),
        )
        for field, actual, expected in expected_values:
            if actual != expected:
                errors.append(f"Qwen MLX v2 {field} must equal {expected!r}")
        validate_pinned_qwen_identity(
            raw_model_identity,
            field="Qwen MLX v2 raw.model_identity",
            repository=MLX_QWEN_MODEL,
            revision=MLX_QWEN_MODEL_REVISION,
            errors=errors,
        )
        validate_pinned_qwen_identity(
            aligned_aligner_identity,
            field="Qwen MLX v2 aligned.source.aligner_identity",
            repository=MLX_QWEN_ALIGNER,
            revision=MLX_QWEN_ALIGNER_REVISION,
            errors=errors,
        )
        return

    raw_backend = raw_options.get("backend") if isinstance(raw_options, dict) else None
    aligned_backend = aligned_options.get("backend") if isinstance(aligned_options, dict) else None
    cuda_indicators = (
        raw_engine == CUDA_QWEN_ENGINE
        or aligned_source.get("engine") == CUDA_QWEN_ENGINE
        or refined_source.get("engine") == CUDA_QWEN_ENGINE
        or raw_model in {CUDA_QWEN_MODEL, LEGACY_CUDA_QWEN_MODEL}
        or aligned_source.get("model") in {CUDA_QWEN_MODEL, LEGACY_CUDA_QWEN_MODEL}
        or raw_backend in {CUDA_QWEN_BACKEND, LEGACY_CUDA_QWEN_BACKEND}
        or aligned_backend in {CUDA_QWEN_BACKEND, LEGACY_CUDA_QWEN_BACKEND}
    )
    if not cuda_indicators:
        errors.append("Qwen v2 lineage must use the supported pinned MLX or CUDA backend")
        return

    expected_values = (
        ("raw.engine", raw_engine, CUDA_QWEN_ENGINE),
        ("raw.model", raw_model, CUDA_QWEN_MODEL),
        ("aligned.source.engine", aligned_source.get("engine"), CUDA_QWEN_ENGINE),
        ("aligned.source.model", aligned_source.get("model"), CUDA_QWEN_MODEL),
        (
            "aligned.source.aligner",
            aligned_source.get("aligner"),
            CUDA_QWEN_ALIGNER,
        ),
        ("refined.source.engine", refined_source.get("engine"), CUDA_QWEN_ENGINE),
        ("refined.source.model", refined_source.get("model"), CUDA_QWEN_MODEL),
        (
            "refined.source.aligner",
            refined_source.get("aligner"),
            CUDA_QWEN_ALIGNER,
        ),
    )
    for field, actual, expected in expected_values:
        if actual != expected:
            errors.append(f"Qwen CUDA v2 {field} must equal {expected!r}")

    validate_pinned_qwen_identity(
        raw_model_identity,
        field="Qwen CUDA v2 raw.model_identity",
        repository=CUDA_QWEN_MODEL,
        revision=CUDA_QWEN_MODEL_REVISION,
        errors=errors,
    )
    validate_pinned_qwen_identity(
        aligned_aligner_identity,
        field="Qwen CUDA v2 aligned.source.aligner_identity",
        repository=CUDA_QWEN_ALIGNER,
        revision=CUDA_QWEN_ALIGNER_REVISION,
        errors=errors,
    )

    for stage, options in (("raw", raw_options), ("aligned", aligned_options)):
        if not isinstance(options, dict):
            errors.append(f"Qwen CUDA v2 {stage}.options must be an object")
            continue
        required_options = {
            "backend": CUDA_QWEN_BACKEND,
            "transformers_version": CUDA_TRANSFORMERS_VERSION,
            "torch_version": CUDA_TORCH_VERSION,
        }
        for key, expected in required_options.items():
            if options.get(key) != expected:
                errors.append(f"Qwen CUDA v2 {stage}.options.{key} must equal {expected!r}")
        if "qwen_asr_version" in options:
            errors.append(f"Qwen CUDA v2 {stage}.options must not record qwen_asr_version")


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


def validate_selected_qwen_readme_provenance(
    front_matter: list[str],
    *,
    selected_run: dict[str, Any],
    raw: dict[str, Any],
    refined: dict[str, Any],
    errors: list[str],
) -> None:
    """Bind publishable selected-Qwen metadata to the rendered artifact."""

    canonical_generated_at = refined.get("generated_at")
    if not is_rfc3339_timestamp(canonical_generated_at):
        errors.append(
            "refined.generated_at must be an RFC 3339 timestamp for a "
            "web-publishable selected Qwen run"
        )
    else:
        transcript_generated_at = nested_front_matter_scalar(
            front_matter, "transcript", "generated_at"
        )
        if transcript_generated_at != canonical_generated_at:
            errors.append(
                "transcript.generated_at must equal selected "
                "refined.generated_at: "
                f"expected={canonical_generated_at!r} "
                f"actual={transcript_generated_at!r}"
            )
        run_generated_at = selected_run.get("generated_at")
        if run_generated_at != canonical_generated_at:
            errors.append(
                "selected Qwen asr_runs.generated_at must equal selected "
                "refined.generated_at: "
                f"expected={canonical_generated_at!r} actual={run_generated_at!r}"
            )

    raw_audio = raw.get("audio")
    raw_options = raw.get("options")
    if not isinstance(raw_audio, dict) or not isinstance(raw_options, dict):
        return
    precise_markers = (
        "sample_count" in raw_audio,
        "planned_chunk_count" in raw_options,
        "effective_total_token_budget" in raw_options,
    )
    if not all(precise_markers):
        # Markerless artifacts retain the legacy nominal-budget contract.
        return

    readme_options = nested_front_matter_mapping(front_matter, "transcript", "options")
    for field in ("planned_chunk_count", "effective_total_token_budget"):
        expected = raw_options.get(field)
        actual = readme_options.get(field)
        if actual != expected:
            errors.append(
                f"transcript.options.{field} must equal selected "
                f"raw.options.{field}: expected={expected!r} actual={actual!r}"
            )


def validate_source_preferences(
    lines: list[str], *, field_prefix: str, errors: list[str]
) -> list[dict[str, Any]]:
    sources_present, sources = parse_front_matter_list(lines, "sources")
    if not sources_present or not sources:
        errors.append(f"{field_prefix} sources must contain at least one source")
    preferred_count = 0
    for index, source in enumerate(sources):
        if "preferred" in source and not isinstance(source["preferred"], bool):
            errors.append(f"{field_prefix} sources[{index}].preferred must be a YAML boolean")
        if source.get("preferred") is True:
            preferred_count += 1
    if preferred_count != 1:
        errors.append(f"{field_prefix} sources must contain exactly one preferred source")
    return sources


def validate_source_schema(
    sources: list[dict[str, Any]], *, field_prefix: str, errors: list[str]
) -> None:
    """Mirror the Web source schema for fields shared by shows and episodes."""

    positive_id_fields = {"aid", "cid", "mid"}
    non_empty_string_fields = {
        "apple_podcasts_id",
        "channel_id",
        "episode_id",
        "episode_number",
        "guid",
        "page_id",
        "playlist_id",
        "rss_guid",
        "show_id",
        "video_id",
    }
    for index, source in enumerate(sources):
        field = f"{field_prefix} sources[{index}]"
        unknown_fields = set(source).difference(SOURCE_FIELDS)
        if unknown_fields:
            errors.append(
                f"{field} contains unsupported fields: {', '.join(sorted(unknown_fields))}"
            )

        platform = source.get("platform")
        kind = source.get("kind")
        url = source.get("url")
        if platform not in SOURCE_PLATFORMS:
            errors.append(f"{field}.platform must be one of {', '.join(sorted(SOURCE_PLATFORMS))}")
        if kind not in SOURCE_KINDS:
            errors.append(f"{field}.kind must be one of {', '.join(sorted(SOURCE_KINDS))}")
        if not is_absolute_url(url, scheme="https"):
            errors.append(f"{field}.url must be an HTTPS URL")
        if "title" in source and (not isinstance(source["title"], str) or not source["title"]):
            errors.append(f"{field}.title must be a non-empty string")
        external_id = source.get("external_id")
        if "external_id" in source and (
            isinstance(external_id, bool)
            or not isinstance(external_id, (str, int))
            or external_id == ""
        ):
            errors.append(f"{field}.external_id must be a non-empty string or number")
        if "preferred" in source and not isinstance(source["preferred"], bool):
            errors.append(f"{field}.preferred must be a YAML boolean")

        identifiers_value = source.get("identifiers")
        identifiers = identifiers_value if isinstance(identifiers_value, dict) else {}
        if identifiers_value is not None and not isinstance(identifiers_value, dict):
            errors.append(f"{field}.identifiers must be a mapping")
        if isinstance(identifiers_value, dict):
            unknown_identifiers = set(identifiers).difference(SOURCE_IDENTIFIER_FIELDS)
            if unknown_identifiers:
                errors.append(
                    f"{field}.identifiers contains unsupported fields: "
                    f"{', '.join(sorted(unknown_identifiers))}"
                )
            for key in positive_id_fields:
                value = identifiers.get(key)
                if key in identifiers and (
                    not isinstance(value, str) or re.fullmatch(r"[1-9]\d*", value) is None
                ):
                    errors.append(f"{field}.identifiers.{key} must be a positive ID string")
            for key in non_empty_string_fields:
                value = identifiers.get(key)
                if key in identifiers and (not isinstance(value, str) or not value):
                    errors.append(f"{field}.identifiers.{key} must be a non-empty string")
            bvid = identifiers.get("bvid")
            if "bvid" in identifiers and (
                not isinstance(bvid, str) or re.fullmatch(r"BV[0-9A-Za-z]+", bvid) is None
            ):
                errors.append(f"{field}.identifiers.bvid has an invalid BVID")
            for key in ("eid", "pid"):
                value = identifiers.get(key)
                if key in identifiers and (
                    not isinstance(value, str) or re.fullmatch(r"[0-9a-f]{24}", value) is None
                ):
                    errors.append(f"{field}.identifiers.{key} must be a lowercase 24-character ID")
            media_id = identifiers.get("media_id")
            if "media_id" in identifiers and (
                not isinstance(media_id, str)
                or re.fullmatch(r"[0-9a-f]{24}/[^/]+\.m4a", media_id) is None
            ):
                errors.append(f"{field}.identifiers.media_id has an invalid media identity")
            page = identifiers.get("page")
            if "page" in identifiers and (
                isinstance(page, bool) or not isinstance(page, int) or page <= 0
            ):
                errors.append(f"{field}.identifiers.page must be a positive integer")
            feed_url = identifiers.get("feed_url")
            if "feed_url" in identifiers and not is_absolute_url(feed_url):
                errors.append(f"{field}.identifiers.feed_url must be a URL")
            video_id = identifiers.get("video_id")
            if "video_id" in identifiers and (
                not isinstance(video_id, str)
                or re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id) is None
            ):
                errors.append(f"{field}.identifiers.video_id has an invalid YouTube video ID")
            channel_id = identifiers.get("channel_id")
            if "channel_id" in identifiers and (
                not isinstance(channel_id, str)
                or re.fullmatch(r"UC[A-Za-z0-9_-]{22}", channel_id) is None
            ):
                errors.append(f"{field}.identifiers.channel_id has an invalid YouTube channel ID")
            playlist_id = identifiers.get("playlist_id")
            if "playlist_id" in identifiers and (
                not isinstance(playlist_id, str)
                or re.fullmatch(r"[A-Za-z0-9_-]{10,64}", playlist_id) is None
            ):
                errors.append(f"{field}.identifiers.playlist_id has an invalid YouTube playlist ID")

        bilibili_match = CANONICAL_BILIBILI_VIDEO_RE.fullmatch(url or "")
        if platform == "bilibili" and kind == "video" and bilibili_match is None:
            errors.append(f"{field}.url must be the canonical Bilibili video URL")
        if bilibili_match is not None:
            if platform != "bilibili" or kind != "video":
                errors.append(
                    f"{field} Bilibili video URL must use platform bilibili and kind video"
                )
            for key in ("bvid", "aid", "cid", "page"):
                if key not in identifiers:
                    errors.append(f"{field}.identifiers.{key} is required")
            if identifiers.get("bvid") != bilibili_match.group("bvid"):
                errors.append(f"{field}.identifiers.bvid must match the source URL")

        xiaoyuzhou_match = CANONICAL_XIAOYUZHOU_EPISODE_RE.fullmatch(url or "")
        if platform == "xiaoyuzhou" and kind == "episode" and xiaoyuzhou_match is None:
            errors.append(f"{field}.url must be the canonical Xiaoyuzhou episode URL")
        if xiaoyuzhou_match is not None:
            if platform != "xiaoyuzhou" or kind != "episode":
                errors.append(
                    f"{field} Xiaoyuzhou episode URL must use platform xiaoyuzhou and kind episode"
                )
            for key in ("eid", "pid", "media_id"):
                if key not in identifiers:
                    errors.append(f"{field}.identifiers.{key} is required")
            if identifiers.get("eid") != xiaoyuzhou_match.group("eid"):
                errors.append(f"{field}.identifiers.eid must match the source URL")
            media_id = identifiers.get("media_id")
            pid = identifiers.get("pid")
            if (
                isinstance(media_id, str)
                and isinstance(pid, str)
                and not media_id.startswith(f"{pid}/")
            ):
                errors.append(f"{field}.identifiers.media_id must begin with its pid")

        youtube_video_match = CANONICAL_YOUTUBE_VIDEO_RE.fullmatch(url or "")
        if platform == "youtube" and kind == "video" and youtube_video_match is None:
            errors.append(f"{field}.url must be the canonical YouTube video URL")
        if youtube_video_match is not None:
            if platform != "youtube" or kind != "video":
                errors.append(
                    f"{field} YouTube video URL must use platform youtube and kind video"
                )
            for key in ("video_id", "channel_id"):
                if key not in identifiers:
                    errors.append(f"{field}.identifiers.{key} is required")
            if identifiers.get("video_id") != youtube_video_match.group("video_id"):
                errors.append(f"{field}.identifiers.video_id must match the source URL")

        youtube_playlist_match = CANONICAL_YOUTUBE_PLAYLIST_RE.fullmatch(url or "")
        if platform == "youtube" and kind == "playlist" and youtube_playlist_match is None:
            errors.append(f"{field}.url must be the canonical YouTube playlist URL")
        if youtube_playlist_match is not None:
            if platform != "youtube" or kind != "playlist":
                errors.append(
                    f"{field} YouTube playlist URL must use platform youtube and kind playlist"
                )
            for key in ("playlist_id", "channel_id"):
                if key not in identifiers:
                    errors.append(f"{field}.identifiers.{key} is required")
            if identifiers.get("playlist_id") != youtube_playlist_match.group("playlist_id"):
                errors.append(f"{field}.identifiers.playlist_id must match the source URL")


def validate_episode_sources(
    sources: list[dict[str, Any]], *, field_prefix: str, errors: list[str]
) -> None:
    validate_source_schema(sources, field_prefix=field_prefix, errors=errors)


def validate_participants_contract(
    lines: list[str], *, field_prefix: str, errors: list[str]
) -> list[dict[str, Any]]:
    present, participants = parse_front_matter_list(lines, "participants")
    if not present or not participants:
        errors.append(f"{field_prefix} participants must contain at least one person")
        return participants

    seen_ids: set[str] = set()
    for index, participant in enumerate(participants):
        field = f"{field_prefix} participants[{index}]"
        unknown_fields = set(participant).difference(PARTICIPANT_FIELDS)
        if unknown_fields:
            errors.append(
                f"{field} contains unsupported fields: {', '.join(sorted(unknown_fields))}"
            )
        participant_id = participant.get("id")
        name = participant.get("name")
        role = participant.get("role")
        aliases = participant.get("aliases", [])
        if not isinstance(participant_id, str) or EPISODE_KEY_RE.fullmatch(participant_id) is None:
            errors.append(f"{field}.id has an invalid stable ID format")
        elif participant_id in seen_ids:
            errors.append(f"{field}.id duplicates {participant_id!r}")
        else:
            seen_ids.add(participant_id)
        if not isinstance(name, str) or not name.strip():
            errors.append(f"{field}.name must be a non-empty string")
        if role not in PARTICIPANT_ROLES:
            errors.append(f"{field}.role must be one of {', '.join(sorted(PARTICIPANT_ROLES))}")
        if not isinstance(aliases, list) or any(
            not isinstance(alias, str) or not alias.strip() for alias in aliases
        ):
            errors.append(f"{field}.aliases must be a list of non-empty strings")
    return participants


def expected_navigation_person(participants: list[dict[str, Any]]) -> str | None:
    for role in ("guest", "participant", "host"):
        names = [
            participant.get("name")
            for participant in participants
            if participant.get("role") == role
            and isinstance(participant.get("name"), str)
            and participant.get("name")
        ]
        if names:
            return "、".join(names)
    return None


def validate_local_audio_cache_contract(
    lines: list[str],
    *,
    field_prefix: str,
    duration_ms: int | None,
    publishable: bool,
    errors: list[str],
) -> None:
    raw_cache = top_level_front_matter_raw_scalar(lines, "local_audio_cache")
    cache = nested_front_matter_mapping(lines, "local_audio_cache")
    transcript = nested_front_matter_mapping(lines, "transcript")
    audio_asr = transcript.get("acquisition_method") == "audio-asr"
    if raw_cache is not None and decode_yaml_primitive(raw_cache) is None:
        if publishable and audio_asr:
            errors.append(
                f"{field_prefix} audio-ASR transcript requires local_audio_cache provenance"
            )
        return
    if not cache:
        if publishable and audio_asr:
            errors.append(
                f"{field_prefix} audio-ASR transcript requires local_audio_cache provenance"
            )
        return

    required = {
        "path",
        "metadata_path",
        "git_ignored",
        "verified_at",
        "codec",
        "sample_rate_hz",
        "channels",
        "size_bytes",
        "duration_ms",
        "sha256",
    }
    for key in sorted(required.difference(cache)):
        errors.append(f"{field_prefix} local_audio_cache.{key} is missing")
    if "acquired_at" not in cache and "recovered_at" not in cache:
        errors.append(f"{field_prefix} local_audio_cache requires acquired_at or recovered_at")
    for key in ("path", "metadata_path", "codec"):
        if key in cache and (not isinstance(cache[key], str) or not cache[key]):
            errors.append(f"{field_prefix} local_audio_cache.{key} must be non-empty")
    if cache.get("git_ignored") is not True:
        errors.append(f"{field_prefix} local_audio_cache.git_ignored must be true")
    for key in ("acquired_at", "recovered_at", "verified_at"):
        if key in cache and not is_rfc3339_timestamp(cache[key]):
            errors.append(f"{field_prefix} local_audio_cache.{key} must be RFC 3339")
    for key in ("sample_rate_hz", "channels", "size_bytes", "duration_ms"):
        value = cache.get(key)
        if key in cache and (isinstance(value, bool) or not isinstance(value, int) or value <= 0):
            errors.append(f"{field_prefix} local_audio_cache.{key} must be positive")
    if "sha256" in cache and (
        not isinstance(cache["sha256"], str) or SHA256_RE.fullmatch(cache["sha256"]) is None
    ):
        errors.append(f"{field_prefix} local_audio_cache.sha256 must be a lowercase SHA-256")
    cached_duration = cache.get("duration_ms")
    if (
        audio_asr
        and duration_ms is not None
        and isinstance(cached_duration, int)
        and duration_ms != cached_duration
    ):
        errors.append(
            f"{field_prefix} duration_ms must equal local_audio_cache.duration_ms "
            "for the selected ASR input"
        )


def validate_summary_provenance(
    lines: list[str],
    *,
    episode_dir: Path,
    repository_root: Path,
    label: str,
    summary_path: Path | None,
    transcript_path_value: str | None,
    errors: list[str],
) -> None:
    source = nested_front_matter_mapping(lines, "summary", "source_transcript")
    required = {"path", "engine", "model", "selection_status", "sha256"}
    for key in sorted(required.difference(source)):
        errors.append(f"{label} summary.source_transcript.{key} is missing")
    for key in ("path", "engine", "model"):
        if key in source and (not isinstance(source[key], str) or not source[key]):
            errors.append(f"{label} summary.source_transcript.{key} must be non-empty")
    selection_status = source.get("selection_status")
    if selection_status not in SUMMARY_SELECTION_STATUSES:
        errors.append(
            f"{label} summary.source_transcript.selection_status must be selected or superseded"
        )
    source_sha = source.get("sha256")
    if not isinstance(source_sha, str) or SHA256_RE.fullmatch(source_sha) is None:
        errors.append(f"{label} summary.source_transcript.sha256 must be a lowercase SHA-256")

    source_path = safe_recorded_path(
        source.get("path"),
        base=episode_dir,
        repository_root=episode_dir,
        field=f"{label} summary.source_transcript.path",
        errors=errors,
        containment_label="episode directory",
    )
    if source_path is None:
        return
    if not source_path.is_file():
        errors.append(f"{label} summary.source_transcript.path is missing: {source.get('path')!r}")
        return
    if isinstance(source_sha, str) and SHA256_RE.fullmatch(source_sha):
        if sha256_file(source_path) != source_sha:
            errors.append(f"{label} summary.source_transcript.sha256 does not match its file")
    if selection_status == "selected" and source.get("path") != transcript_path_value:
        errors.append(f"{label} selected summary source must equal transcript.path")

    runs = parse_asr_runs(lines)
    matching_runs = [
        run
        for run in runs
        if run.get("engine") == source.get("engine")
        and run.get("model") == source.get("model")
        and run.get("selection_status") == selection_status
    ]
    if len(matching_runs) != 1:
        errors.append(f"{label} summary.source_transcript must match exactly one ASR run")
    elif selection_status == "superseded":
        artifacts = matching_runs[0].get("artifacts")
        if not isinstance(artifacts, dict) or artifacts.get("transcript") != source.get("path"):
            errors.append(
                f"{label} superseded summary source must match its ASR run transcript artifact"
            )

    if summary_path is None or not summary_path.is_file():
        return
    source_timestamps: set[str] = set()
    try:
        for line in source_path.read_text(encoding="utf-8").splitlines():
            match = TRANSCRIPT_TIMESTAMP_RE.match(line)
            if match is not None:
                source_timestamps.add(match.group(1))
        summary_lines = summary_path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as error:
        errors.append(f"{label} summary provenance files cannot be read: {error}")
        return
    for line_number, line in enumerate(summary_lines, start=1):
        for match in SUMMARY_TIMESTAMP_RE.finditer(line):
            timestamp = f"[{match.group(1)}]"
            if timestamp not in source_timestamps:
                errors.append(
                    f"{label} summary timestamp {timestamp} at line {line_number} "
                    "does not exist in summary.source_transcript"
                )


def validate_show_metadata_contract(
    readme_path: Path,
    readme_text: str,
    *,
    repository_root: Path,
    show_ids: dict[str, Path],
    errors: list[str],
) -> dict[str, Any]:
    lines = extract_front_matter_lines(readme_text)
    label = display_path(readme_path, repository_root)
    schema_version = top_level_front_matter_value(lines, "schema_version")
    kind = top_level_front_matter_scalar(lines, "kind")
    show_id = top_level_front_matter_scalar(lines, "id")
    title = top_level_front_matter_scalar(lines, "title")
    language = top_level_front_matter_scalar(lines, "language")
    status = top_level_front_matter_scalar(lines, "status")
    last_verified_at = top_level_front_matter_value(lines, "last_verified_at")
    top_level_keys = top_level_front_matter_keys(lines)
    unknown_fields = set(top_level_keys).difference(SHOW_FIELDS)
    if unknown_fields:
        errors.append(
            f"{label} contains unsupported show fields: {', '.join(sorted(unknown_fields))}"
        )
    duplicate_fields = sorted(key for key in set(top_level_keys) if top_level_keys.count(key) > 1)
    if duplicate_fields:
        errors.append(f"{label} duplicates show fields: {', '.join(duplicate_fields)}")
    if schema_version != 1:
        errors.append(f"{label} schema_version must equal 1")
    if kind != "show":
        errors.append(f"{label} kind must equal 'show'")
    if not show_id or SHOW_ID_RE.fullmatch(show_id) is None:
        errors.append(f"{label} id must contain only lowercase letters and digits")
    elif show_id != readme_path.parent.name:
        errors.append(f"{label} id must match its show directory")
    elif show_id in show_ids:
        errors.append(f"{label} duplicates show id {show_id!r}")
    else:
        show_ids[show_id] = readme_path
    if not title:
        errors.append(f"{label} title must be a non-empty string")
    aliases_present, aliases = parse_top_level_scalar_list(lines, "aliases")
    if not aliases_present or any(not isinstance(alias, str) or not alias for alias in aliases):
        errors.append(f"{label} aliases must be a list of non-empty strings")
    if not isinstance(language, str) or not language:
        errors.append(f"{label} language must be a non-empty string")
    if status not in SHOW_STATUSES:
        errors.append(f"{label} status must be one of {', '.join(sorted(SHOW_STATUSES))}")
    for field in ("formats", "topics"):
        present, values = parse_top_level_scalar_list(lines, field)
        if (
            not present
            or not values
            or any(not isinstance(value, str) or not value for value in values)
        ):
            errors.append(f"{label} {field} must be a non-empty list of strings")
    sources = validate_source_preferences(lines, field_prefix=label, errors=errors)
    validate_source_schema(sources, field_prefix=label, errors=errors)
    if not is_calendar_date(last_verified_at):
        errors.append(f"{label} last_verified_at must be a valid YYYY-MM-DD date")
    preferred = next((source for source in sources if source.get("preferred") is True), None)
    return {"id": show_id, "title": title, "preferred": preferred}


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
    schema_version = top_level_front_matter_value(front_matter, "schema_version")
    kind = top_level_front_matter_scalar(front_matter, "kind")
    episode_id = top_level_front_matter_scalar(front_matter, "id")
    show_id = top_level_front_matter_scalar(front_matter, "show_id")
    episode_key = top_level_front_matter_scalar(front_matter, "episode_key")
    episode_number = top_level_front_matter_value(front_matter, "episode_number")
    slug = top_level_front_matter_scalar(front_matter, "slug")
    release_type = top_level_front_matter_scalar(front_matter, "release_type")
    title = top_level_front_matter_scalar(front_matter, "title")
    navigation_title = top_level_front_matter_scalar(front_matter, "navigation_title")
    published_at = top_level_front_matter_scalar(front_matter, "published_at")
    language = top_level_front_matter_scalar(front_matter, "language")
    episode_key_raw = top_level_front_matter_raw_scalar(front_matter, "episode_key")
    published_at_raw = top_level_front_matter_raw_scalar(front_matter, "published_at")
    duration_ms_raw = top_level_front_matter_raw_scalar(front_matter, "duration_ms")
    duration_ms = top_level_front_matter_value(front_matter, "duration_ms")

    if schema_version != 1:
        errors.append(f"{label} schema_version must equal 1")
    if kind != "episode":
        errors.append(f"{label} kind must equal 'episode'")

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

    if slug != episode_dir.name:
        errors.append(f"{label} slug must equal its episode directory name")
    if release_type not in EPISODE_RELEASE_TYPES:
        errors.append(
            f"{label} release_type must be one of {', '.join(sorted(EPISODE_RELEASE_TYPES))}"
        )
    if not isinstance(title, str) or not title.strip():
        errors.append(f"{label} title must be a non-empty string")
    elif re.search(r"(?:^|\s)#\d+\s*$", title):
        errors.append(f"{label} title must not include an episode-number suffix")
    numbering = nested_front_matter_mapping(front_matter, "numbering")
    numbering_status = numbering.get("status")
    if numbering_status not in NUMBERING_STATUSES:
        errors.append(
            f"{label} numbering.status must be one of {', '.join(sorted(NUMBERING_STATUSES))}"
        )
    if not is_calendar_date(numbering.get("checked_at")):
        errors.append(f"{label} numbering.checked_at must be a valid YYYY-MM-DD date")
    if not isinstance(numbering.get("source"), str) or not numbering.get("source"):
        errors.append(f"{label} numbering.source must be a non-empty string")
    numbering_url = numbering.get("url")
    if "url" in numbering and not is_absolute_url(numbering_url):
        errors.append(f"{label} numbering.url must be a URL")
    if episode_number is None:
        if numbering_status == "verified":
            errors.append(f"{label} numbering.status cannot be verified without episode_number")
    elif (
        isinstance(episode_number, bool)
        or not isinstance(episode_number, int)
        or episode_number <= 0
    ):
        errors.append(f"{label} episode_number must be null or a positive integer")
    elif numbering_status != "verified":
        errors.append(f"{label} episode_number requires numbering.status verified")

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
    if not isinstance(language, str) or not language:
        errors.append(f"{label} language must be a non-empty string")

    workflow = {
        "metadata": nested_front_matter_scalar(front_matter, "workflow", "metadata"),
        "summary": nested_front_matter_scalar(front_matter, "workflow", "summary"),
        "transcript": nested_front_matter_scalar(front_matter, "workflow", "transcript"),
    }
    workflow_contracts = {
        "metadata": WORKFLOW_METADATA_STATUSES,
        "summary": WORKFLOW_SUMMARY_STATUSES,
        "transcript": WORKFLOW_TRANSCRIPT_STATUSES,
    }
    for field, allowed in workflow_contracts.items():
        if workflow[field] not in allowed:
            errors.append(f"{label} workflow.{field} must be one of {', '.join(sorted(allowed))}")

    sources = validate_source_preferences(front_matter, field_prefix=label, errors=errors)
    validate_episode_sources(sources, field_prefix=label, errors=errors)
    youtube_video_sources = [
        source
        for source in sources
        if source.get("platform") == "youtube" and source.get("kind") == "video"
    ]
    if episode_number is None and youtube_video_sources:
        youtube_identifiers = youtube_video_sources[0].get("identifiers")
        video_id = (
            youtube_identifiers.get("video_id")
            if isinstance(youtube_identifiers, dict)
            else None
        )
        if isinstance(video_id, str) and re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
            expected_key = f"youtube-{video_id.encode('ascii').hex()}"
            if episode_key != expected_key:
                errors.append(
                    f"{label} unnumbered YouTube episode_key must equal {expected_key!r}"
                )
    elif isinstance(episode_key, str) and episode_key.startswith("youtube-"):
        errors.append(f"{label} YouTube episode_key requires a YouTube video source")
    participants = validate_participants_contract(front_matter, field_prefix=label, errors=errors)
    validate_participant_profiles(front_matter, field_prefix=label, errors=errors)
    publishable = is_episode_web_publishable(workflow)

    expected_person = expected_navigation_person(participants)
    if (
        expected_person is not None
        and isinstance(navigation_title, str)
        and navigation_title.split(" · ", 1)[0] != expected_person
    ):
        errors.append(f"{label} navigation_title person must equal {expected_person!r}")

    runs = parse_asr_runs(front_matter)
    for index, run in enumerate(runs):
        if run.get("selection_status") not in ASR_SELECTION_STATUSES:
            errors.append(f"{label} asr_runs[{index}].selection_status has an invalid value")
    selected_runs = [run for run in runs if run.get("selection_status") == "selected"]
    if publishable and len(selected_runs) != 1:
        errors.append(f"{label} web-publishable transcript must bind exactly one selected ASR run")
    if selected_runs:
        selected_run = selected_runs[0]
        for key in ("id", "engine", "model"):
            if not isinstance(selected_run.get(key), str) or not selected_run.get(key):
                errors.append(f"{label} selected ASR run {key} must be non-empty")
        if not isinstance(selected_run.get("artifacts"), dict):
            errors.append(f"{label} selected ASR run must contain an artifacts mapping")
        transcript_metadata = nested_front_matter_mapping(front_matter, "transcript")
        for key in ("engine", "model"):
            if transcript_metadata.get(key) != selected_run.get(key):
                errors.append(f"{label} transcript.{key} must equal the selected ASR run {key}")
        acquisition_method = transcript_metadata.get("acquisition_method")
        if publishable and (not isinstance(acquisition_method, str) or not acquisition_method):
            errors.append(f"{label} publishable transcript.acquisition_method must be non-empty")
        if is_qwen_run(selected_run) and acquisition_method != "audio-asr":
            errors.append(f"{label} selected Qwen run requires acquisition_method audio-asr")

    validate_local_audio_cache_contract(
        front_matter,
        field_prefix=label,
        duration_ms=duration_ms if isinstance(duration_ms, int) else None,
        publishable=publishable,
        errors=errors,
    )

    asset_paths: dict[str, Path | None] = {}
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
        asset_paths[section] = asset_path
        if publishable and asset_path is not None and not asset_path.is_file():
            errors.append(f"{label} is web-publishable but {section}.path is missing: {value!r}")

    if publishable:
        validate_summary_provenance(
            front_matter,
            episode_dir=episode_dir,
            repository_root=repository_root,
            label=label,
            summary_path=asset_paths.get("summary"),
            transcript_path_value=nested_front_matter_scalar(front_matter, "transcript", "path"),
            errors=errors,
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
        errors.append(f"{field} cannot be read at {display_path(path, repository_root)}: {error}")
        return None

    if len(lines) < 3 or not lines[0].startswith("# ") or lines[1] != "":
        errors.append(
            f"{field} must start with a level-one title, a blank line, and at least one segment"
        )
        return None

    body = lines[2:]
    timestamps: list[str | None] = []
    for index, line in enumerate(body, start=3):
        if TRANSCRIPT_LINE_RE.fullmatch(line) is None:
            errors.append(
                f"{field} line {index} must be one timestamped sentence with a Markdown hard break"
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
    selected_is_english = isinstance(selected_value, str) and selected_value.endswith(".en.md")
    required = episode_language == "en" or selected_is_english
    translations_present, translations = parse_transcript_translations(front_matter, errors=errors)

    if not required:
        if translations:
            errors.append(
                "transcript.translations is only valid when the selected transcript is English"
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
            f"selected English transcript is missing: {display_path(source_path, repository_root)}"
        )

    chinese_items = [item for item in translations if item.get("language") == "zh-CN"]
    if (require_complete or translation_claimed) and (
        not translations_present or len(chinese_items) != 1
    ):
        errors.append(
            "English selected transcript requires exactly one zh-CN item in transcript.translations"
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
            errors.append(f"{field}.status must be one of machine, edited, reviewed")
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
                errors.append(f"{field}.source_sha256 does not match transcript.en.md")
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
        if translation_sha is not None and translation_sha != sha256_file(translation_path):
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
        translation_title, translation_body, translation_timestamps = translation_structure
        if translation_title != source_title:
            errors.append("transcript.en.md and transcript.zh-CN.md must have the same title")
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

    root_transcript = nested_front_matter_scalar(front_matter, "transcript", "path")
    if isinstance(root_transcript, str) and root_transcript:
        names.add(PurePosixPath(root_transcript).name)

    if qwen_dir.is_dir():
        names.update(path.name for path in qwen_dir.glob("transcript.*.md") if path.is_file())

    invalid_names = sorted(
        name for name in names if QWEN_TRANSCRIPT_NAME_RE.fullmatch(name) is None
    )
    for name in invalid_names:
        errors.append(
            f"Qwen transcript artifact must use transcript.<language>.md naming: {name!r}"
        )
    valid_names = sorted(names.difference(invalid_names))
    if len(valid_names) > 1:
        errors.append(
            "episode records multiple Qwen transcript languages: " + ", ".join(valid_names)
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
        run for run in qwen_runs if str(run.get("selection_status", "")).lower() == "selected"
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
    aligned = read_json_strict(aligned_path, repository_root=repository_root, errors=errors)
    refined = read_json_strict(refined_path, repository_root=repository_root, errors=errors)
    if raw is None or aligned is None or refined is None:
        return True

    lineage_versions = [
        document.get("lineage_schema_version") for document in (raw, aligned, refined)
    ]
    legacy_lineage = all(version is None for version in lineage_versions)
    v2_lineage = all(type(version) is int and version == 2 for version in lineage_versions)
    if not legacy_lineage and not v2_lineage:
        errors.append(
            "Qwen lineage_schema_version must be absent on all three legacy artifacts "
            "or the strict integer 2 on raw, aligned, and refined"
        )
    if v2_lineage:
        aligned_source = aligned.get("source") if isinstance(aligned.get("source"), dict) else {}
        refined_source = refined.get("source") if isinstance(refined.get("source"), dict) else {}
        raw_model = validate_model_identity(
            raw.get("model_identity"), field="raw.model_identity", errors=errors
        )
        aligned_model = validate_model_identity(
            aligned_source.get("model_identity"),
            field="aligned.source.model_identity",
            errors=errors,
        )
        aligned_aligner = validate_model_identity(
            aligned_source.get("aligner_identity"),
            field="aligned.source.aligner_identity",
            errors=errors,
        )
        refined_model = validate_model_identity(
            refined_source.get("model_identity"),
            field="refined.source.model_identity",
            errors=errors,
        )
        refined_aligner = validate_model_identity(
            refined_source.get("aligner_identity"),
            field="refined.source.aligner_identity",
            errors=errors,
        )
        if raw_model != aligned_model or aligned_model != refined_model:
            errors.append("Qwen model_identity must remain identical across the artifact chain")
        if aligned_aligner != refined_aligner:
            errors.append("Qwen aligner_identity must remain identical across the artifact chain")
        model_repositories = (
            raw.get("model"),
            aligned_source.get("model"),
            refined_source.get("model"),
        )
        if raw_model is None or any(
            not isinstance(repository, str) or repository != raw_model.get("repository")
            for repository in model_repositories
        ):
            errors.append(
                "Qwen model_identity.repository must equal raw.model, "
                "aligned.source.model, and refined.source.model"
            )
        aligner_repositories = (
            aligned_source.get("aligner"),
            refined_source.get("aligner"),
        )
        if aligned_aligner is None or any(
            not isinstance(repository, str) or repository != aligned_aligner.get("repository")
            for repository in aligner_repositories
        ):
            errors.append(
                "Qwen aligner_identity.repository must equal aligned.source.aligner "
                "and refined.source.aligner"
            )
        validate_qwen_v2_backend_contract(
            raw,
            aligned,
            refined,
            raw_model_identity=raw_model,
            aligned_aligner_identity=aligned_aligner,
            errors=errors,
        )

    workflow = {
        "metadata": nested_front_matter_scalar(front_matter, "workflow", "metadata"),
        "summary": nested_front_matter_scalar(front_matter, "workflow", "summary"),
        "transcript": nested_front_matter_scalar(front_matter, "workflow", "transcript"),
    }
    if len(selected_runs) == 1 and is_episode_web_publishable(workflow):
        validate_selected_qwen_readme_provenance(
            front_matter,
            selected_run=selected_runs[0],
            raw=raw,
            refined=refined,
            errors=errors,
        )

    transcript_language = transcript_name.removeprefix("transcript.").removesuffix(".md")
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
        if isinstance(recorded_rendered_lines, bool) or not isinstance(
            recorded_rendered_lines, int
        ):
            errors.append("refined.statistics.rendered_lines must be an integer")
        elif recorded_rendered_lines != len(rendered_lines):
            errors.append("refined.statistics.rendered_lines does not match Qwen transcript")

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
        errors.append(f"refined.rendered_transcript.sha256 does not match {transcript_name}")

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

    cache_value = nested_front_matter_scalar(front_matter, "local_audio_cache", "path")
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
            repository_root / ".cache" / "media" / show_id / episode_dir.name / "source.m4a"
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


def validate_selected_run_contract(
    episode_dir: Path,
    *,
    repository_root: Path,
    readme_text: str,
    publishable: bool,
    qwen_complete: bool,
    errors: list[str],
) -> None:
    if not publishable:
        return
    lines = extract_front_matter_lines(readme_text)
    selected = [run for run in parse_asr_runs(lines) if run.get("selection_status") == "selected"]
    if len(selected) != 1:
        return
    run = selected[0]
    if is_qwen_run(run):
        if not qwen_complete:
            errors.append(
                f"{display_path(episode_dir, repository_root)} selected Qwen run must have a complete artifact chain"
            )
        return
    artifacts = run.get("artifacts")
    if not isinstance(artifacts, dict):
        return
    required = {"raw", "refined", "transcript"}
    for name in sorted(required):
        path = safe_recorded_path(
            artifacts.get(name),
            base=episode_dir,
            repository_root=episode_dir,
            field=f"selected asr_runs.artifacts.{name}",
            errors=errors,
            containment_label="episode directory",
        )
        if path is not None and not path.is_file():
            errors.append(f"selected asr_runs.artifacts.{name} is missing")
    run_transcript = safe_recorded_path(
        artifacts.get("transcript"),
        base=episode_dir,
        repository_root=episode_dir,
        field="selected asr_runs.artifacts.transcript",
        errors=[],
        containment_label="episode directory",
    )
    root_value = nested_front_matter_scalar(lines, "transcript", "path")
    root_transcript = safe_recorded_path(
        root_value,
        base=episode_dir,
        repository_root=episode_dir,
        field="transcript.path",
        errors=[],
        containment_label="episode directory",
    )
    if (
        run_transcript is not None
        and root_transcript is not None
        and run_transcript.is_file()
        and root_transcript.is_file()
        and run_transcript.read_bytes() != root_transcript.read_bytes()
    ):
        errors.append(
            "selected non-Qwen root transcript must be byte-identical to its run artifact"
        )


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
        errors.append(f"{relative(path)} navigation_title must use 'person · topic' format")
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
    return [cell.strip() for cell in re.split(r"(?<!\\)\|", stripped[1:-1])]


def markdown_link_targets(cell: str) -> list[str]:
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", cell)


def markdown_links(cell: str) -> list[tuple[str, str]]:
    return [
        (label.replace(r"\|", "|"), target)
        for label, target in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", cell)
    ]


def markdown_table_after_heading(
    text: str, heading: str, *, label: str, errors: list[str]
) -> tuple[list[str], list[list[str]]]:
    lines = text.splitlines()
    try:
        start = lines.index(heading) + 1
    except ValueError:
        errors.append(f"{label} is missing {heading}")
        return [], []
    table_lines: list[str] = []
    for line in lines[start:]:
        if not table_lines and not line.strip():
            continue
        if not line.startswith("|"):
            break
        table_lines.append(line)
    if len(table_lines) < 2:
        errors.append(f"{label} {heading} must contain a Markdown table")
        return [], []
    return parse_markdown_table_row(table_lines[0]), [
        parse_markdown_table_row(line) for line in table_lines[2:]
    ]


def validate_wiki_indexes(
    *,
    repository_root: Path,
    shows: dict[str, dict[str, Any]],
    episodes: list[dict[str, Any]],
    errors: list[str],
) -> None:
    root_readme = repository_root / "README.md"
    root_text = root_readme.read_text(encoding="utf-8")
    show_columns, show_rows = markdown_table_after_heading(
        root_text, "## 收录播客", label="README.md", errors=errors
    )
    if show_columns != ["播客", "简介", "节目页"]:
        errors.append("README.md 收录播客 columns must be 播客、简介、节目页")
    seen_shows: set[str] = set()
    for row in show_rows:
        if len(row) != 3:
            errors.append("README.md 收录播客 row must contain 3 columns")
            continue
        local_targets = markdown_link_targets(row[2])
        match = re.fullmatch(r"\./shows/([a-z0-9]+)/?", local_targets[0]) if local_targets else None
        if match is None or match.group(1) not in shows:
            errors.append("README.md 收录播客 row has an invalid local show link")
            continue
        show_id = match.group(1)
        if show_id in seen_shows:
            errors.append(f"README.md 收录播客 duplicates show {show_id}")
            continue
        seen_shows.add(show_id)
        title_links = markdown_links(row[0])
        preferred = shows[show_id].get("preferred")
        preferred_url = preferred.get("url") if isinstance(preferred, dict) else None
        if title_links != [(shows[show_id]["title"], preferred_url)]:
            errors.append(f"README.md show {show_id} must link its preferred source")
    if seen_shows != set(shows):
        errors.append("README.md 收录播客 rows must exactly match show metadata")

    episode_columns, root_rows = markdown_table_after_heading(
        root_text, "## 单集索引", label="README.md", errors=errors
    )
    if episode_columns != ["标题", "访谈人物", "播客名称", "日期", "总结", "逐字稿"]:
        errors.append("README.md 单集索引 columns must match the six-column contract")
    expected_root = {episode["root_summary_link"]: episode for episode in episodes}
    seen_root: set[str] = set()
    root_dates: list[str] = []
    for row in root_rows:
        if len(row) != 6:
            errors.append("README.md 单集索引 row must contain 6 columns")
            continue
        summary_targets = markdown_link_targets(row[4])
        key = summary_targets[0] if summary_targets else ""
        episode = expected_root.get(key)
        if episode is None:
            errors.append(f"README.md 单集索引 has an unknown summary link: {key!r}")
            continue
        if key in seen_root:
            errors.append(f"README.md 单集索引 duplicates summary link: {key!r}")
            continue
        seen_root.add(key)
        root_dates.append(row[3])
        if markdown_links(row[0]) != [(episode["title"], episode["preferred_url"])]:
            errors.append(
                f"README.md row {key} title must equal metadata and link the preferred source"
            )
        if markdown_links(row[2]) != [(episode["show_title"], episode["root_show_link"])]:
            errors.append(f"README.md row {key} podcast must equal and link its show")
        root_transcript_targets = markdown_link_targets(row[5])
        if episode["root_transcript_link"] not in root_transcript_targets:
            errors.append(f"README.md row {key} must link the selected transcript")
        root_translation_link = episode.get("root_translation_link")
        if (
            isinstance(root_translation_link, str)
            and root_translation_link not in root_transcript_targets
        ):
            errors.append(f"README.md row {key} must link the zh-CN transcript translation")
        if row[3] != episode["date"]:
            errors.append(f"README.md row {key} has the wrong publication date")
        if row[1] != episode["guests"]:
            errors.append(f"README.md row {key} has the wrong verified guest list")
    if seen_root != set(expected_root):
        errors.append("README.md 单集索引 rows must exactly match publishable episodes")
    if root_dates != sorted(root_dates, reverse=True):
        errors.append("README.md 单集索引 must be sorted by date descending")

    for show_id in shows:
        show_readme = repository_root / "shows" / show_id / "README.md"
        columns, rows = markdown_table_after_heading(
            show_readme.read_text(encoding="utf-8"),
            "## 单集",
            label=display_path(show_readme, repository_root),
            errors=errors,
        )
        if columns != ["标题", "播客名称", "日期", "总结链接", "逐字稿链接"]:
            errors.append(
                f"shows/{show_id}/README.md 单集 columns must match the five-column contract"
            )
        show_episodes = [episode for episode in episodes if episode["show_id"] == show_id]
        expected = {episode["show_summary_link"]: episode for episode in show_episodes}
        seen: set[str] = set()
        dates: list[str] = []
        for row in rows:
            if len(row) != 5:
                errors.append(f"shows/{show_id}/README.md 单集 row must contain 5 columns")
                continue
            targets = markdown_link_targets(row[3])
            key = targets[0] if targets else ""
            episode = expected.get(key)
            if episode is None:
                errors.append(f"shows/{show_id}/README.md has an unknown summary link: {key!r}")
                continue
            if key in seen:
                errors.append(f"shows/{show_id}/README.md duplicates summary link: {key!r}")
                continue
            seen.add(key)
            dates.append(row[2])
            if markdown_links(row[0]) != [(episode["title"], episode["preferred_url"])]:
                errors.append(
                    f"shows/{show_id}/README.md row {key} title must equal metadata "
                    "and link the preferred source"
                )
            if row[1] != episode["show_title"]:
                errors.append(
                    f"shows/{show_id}/README.md row {key} podcast name must equal show title"
                )
            show_transcript_targets = markdown_link_targets(row[4])
            if episode["show_transcript_link"] not in show_transcript_targets:
                errors.append(
                    f"shows/{show_id}/README.md row {key} must link the selected transcript"
                )
            show_translation_link = episode.get("show_translation_link")
            if (
                isinstance(show_translation_link, str)
                and show_translation_link not in show_transcript_targets
            ):
                errors.append(
                    f"shows/{show_id}/README.md row {key} must link the zh-CN "
                    "transcript translation"
                )
            if row[2] != episode["date"]:
                errors.append(f"shows/{show_id}/README.md row {key} has the wrong publication date")
        if seen != set(expected):
            errors.append(f"shows/{show_id}/README.md rows must exactly match publishable episodes")
        if dates != sorted(dates, reverse=True):
            errors.append(f"shows/{show_id}/README.md 单集 must be sorted by date descending")

    for episode in episodes:
        if episode["show_id"] not in shows:
            errors.append(f"episode index record references unknown show {episode['show_id']!r}")


SUMMARY_HEADINGS = (
    "一句话总结",
    "为什么值得听",
    "核心观点",
    ("5 分钟读完", "整体总结"),
    "主题导航",
    "阅读边界",
    "编辑记录（不对读者展示）",
)
SUMMARY_EDITOR_COPY = (
    re.compile(
        r"(?:状态\s*(?:为|：)|当前为|仍是).{0,12}"
        r"(?:draft|reviewed|machine|草稿|未审核|待审核)",
        flags=re.IGNORECASE,
    ),
    re.compile(
        r"(?:\b(?:source_transcript|selection_status|lineage)\b|"
        r"SHA-256|[a-f\d]{64})",
        flags=re.IGNORECASE,
    ),
    re.compile(
        r"(?:qwen-asr-transformers|mlx-audio|transcript\.(?:zh-CN|en)\.md|"
        r"README(?:\.md)?)",
        flags=re.IGNORECASE,
    ),
    re.compile(r"(?:PodWiki|本稿|逐字稿|正式稿|\bASR\b)", flags=re.IGNORECASE),
    re.compile(r"机器(?:逐字稿|稿|初稿|转写|识别|翻译)"),
    re.compile(
        r"(?:草稿|未审核|待审核|待校对|待回听|待核听|人工(?:审核|复核)|"
        r"正式(?:审核|复核)|回听|核听|校对)"
    ),
    re.compile(r"`(?:draft|reviewed|machine|selected)`", flags=re.IGNORECASE),
    re.compile(r"frozen publisher metadata", flags=re.IGNORECASE),
)


def validate_summary_reader_contract(
    path: Path,
    text: str,
    errors: list[str],
) -> None:
    headings = re.findall(r"^##[ \t]+(.+?)[ \t]*$", text, flags=re.MULTILINE)
    structure_is_valid = len(headings) == len(SUMMARY_HEADINGS) and all(
        actual == expected if isinstance(expected, str) else actual in expected
        for actual, expected in zip(headings, SUMMARY_HEADINGS, strict=True)
    )
    if not structure_is_valid:
        actual = " → ".join(headings) or "无二级标题"
        errors.append(
            f"{relative(path)} summary reader sections are missing or out of order: {actual}"
        )
        return

    reader_start = text.index("## 一句话总结")
    editor_start = text.index("## 编辑记录（不对读者展示）")
    reader_text = text[reader_start:editor_start].replace("ASR—LLM—TTS", "")
    for pattern in SUMMARY_EDITOR_COPY:
        match = pattern.search(reader_text)
        if match is not None:
            errors.append(
                f"{relative(path)} reader content contains editor-only copy: {match.group(0)!r}"
            )
            break


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
        errors.append(f"{relative(path)} 核心观点 logic table must have 2-4 named columns")
        return
    if len(separator) != len(columns) or any(
        re.fullmatch(r":?-{3,}:?", cell) is None for cell in separator
    ):
        errors.append(f"{relative(path)} 核心观点 logic table has an invalid separator")
        return
    if len(rows) < 3:
        errors.append(f"{relative(path)} 核心观点 logic table must have at least 3 rows")
    if any(len(row) != len(columns) or any(not cell for cell in row) for row in rows):
        errors.append(f"{relative(path)} 核心观点 logic table rows must match its named columns")

    decorative_number = re.compile(r"^(?:0?\d+|第\s*\d+)$")
    if any(decorative_number.fullmatch(column) for column in columns) or any(
        decorative_number.fullmatch(cell) for row in rows for cell in row
    ):
        errors.append(f"{relative(path)} 核心观点 logic table must not use decorative numbering")


def check_bilibili_urls(path: Path, text: str, errors: list[str]) -> int:
    for parameter in TRACKING_PARAMETERS:
        if parameter in text:
            errors.append(f"{relative(path)} contains tracking parameter {parameter}")

    count = 0
    for match in BILIBILI_URL_RE.finditer(text):
        count += 1
        url = match.group(0)
        if CANONICAL_BILIBILI_URL_RE.fullmatch(url) is None:
            errors.append(f"{relative(path)} contains non-canonical Bilibili URL: {url}")
    return count


def check_xiaoyuzhou_urls(path: Path, text: str, errors: list[str]) -> int:
    count = 0
    for match in XIAOYUZHOU_URL_RE.finditer(text):
        count += 1
        url = match.group(0)
        if CANONICAL_XIAOYUZHOU_URL_RE.fullmatch(url) is None:
            errors.append(f"{relative(path)} contains non-canonical Xiaoyuzhou URL: {url}")
    return count


def check_youtube_urls(path: Path, text: str, errors: list[str]) -> int:
    count = 0
    for match in YOUTUBE_URL_RE.finditer(text):
        count += 1
        url = match.group(0)
        if (
            CANONICAL_YOUTUBE_VIDEO_RE.fullmatch(url) is None
            and CANONICAL_YOUTUBE_PLAYLIST_RE.fullmatch(url) is None
        ):
            errors.append(f"{relative(path)} contains non-canonical YouTube URL: {url}")
    return count


def main() -> int:
    errors: list[str] = []
    markdown_count = 0
    bilibili_url_count = 0
    xiaoyuzhou_url_count = 0
    youtube_url_count = 0
    qwen_chain_count = 0
    episode_ids: dict[str, Path] = {}
    show_ids: dict[str, Path] = {}
    show_records: dict[str, dict[str, Any]] = {}
    episode_records: list[dict[str, Any]] = []

    if not SHOWS_ROOT.is_dir():
        print("PodWiki validation failed:\n\n- shows directory is missing", file=sys.stderr)
        return 1

    for show_readme in sorted(SHOWS_ROOT.glob("*/README.md")):
        record = validate_show_metadata_contract(
            show_readme,
            show_readme.read_text(encoding="utf-8"),
            repository_root=ROOT,
            show_ids=show_ids,
            errors=errors,
        )
        if isinstance(record.get("id"), str):
            show_records[record["id"]] = record

    for path in sorted(SHOWS_ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        markdown_count += 1
        if path.name == "README.md":
            check_front_matter(path, text, errors)
        elif path.name.startswith("transcript.") and text.startswith("---\n"):
            errors.append(f"{relative(path)} must keep metadata in its episode README")
        elif path.name.startswith("summary."):
            validate_summary_reader_contract(path, text, errors)
            validate_core_point_logic_table(path, text, errors)
        bilibili_url_count += check_bilibili_urls(path, text, errors)
        xiaoyuzhou_url_count += check_xiaoyuzhou_urls(path, text, errors)
        youtube_url_count += check_youtube_urls(path, text, errors)

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
        if publishable:
            front_matter = extract_front_matter_lines(readme_text)
            sources = parse_front_matter_list(front_matter, "sources")[1]
            preferred = next((source for source in sources if source.get("preferred") is True), {})
            participants = parse_front_matter_list(front_matter, "participants")[1]
            guests = (
                "、".join(
                    str(person.get("name"))
                    for person in participants
                    if person.get("role") == "guest"
                )
                or "—"
            )
            show_id = top_level_front_matter_scalar(front_matter, "show_id") or ""
            show = show_records.get(show_id, {})
            summary_name = nested_front_matter_scalar(front_matter, "summary", "path") or ""
            transcript_name = nested_front_matter_scalar(front_matter, "transcript", "path") or ""
            episode_language = top_level_front_matter_scalar(front_matter, "language")
            translation_name: str | None = None
            if episode_language == "en" or transcript_name.endswith(".en.md"):
                translation_parse_errors: list[str] = []
                translations = parse_transcript_translations(
                    front_matter, errors=translation_parse_errors
                )[1]
                for translation in translations:
                    path = translation.get("path")
                    if translation.get("language") == "zh-CN" and isinstance(path, str) and path:
                        translation_name = path
                        break
            relative_episode = episode_dir.relative_to(ROOT).as_posix()
            episode_record = {
                "show_id": show_id,
                "show_title": show.get("title"),
                "title": top_level_front_matter_scalar(front_matter, "title"),
                "date": (top_level_front_matter_scalar(front_matter, "published_at") or "")[:10],
                "guests": guests,
                "preferred_url": preferred.get("url"),
                "root_show_link": f"./shows/{show_id}/",
                "root_summary_link": f"./{relative_episode}/{summary_name}",
                "root_transcript_link": f"./{relative_episode}/{transcript_name}",
                "show_summary_link": f"./episodes/{episode_dir.name}/{summary_name}",
                "show_transcript_link": f"./episodes/{episode_dir.name}/{transcript_name}",
            }
            if translation_name is not None:
                episode_record.update(
                    {
                        "root_translation_link": (f"./{relative_episode}/{translation_name}"),
                        "show_translation_link": (
                            f"./episodes/{episode_dir.name}/{translation_name}"
                        ),
                    }
                )
            episode_records.append(episode_record)
        validate_episode_catalog_keyword(readme, readme_text, errors)
        validate_episode_navigation_title(readme, readme_text, errors)
        validate_episode_translations(
            episode_dir,
            repository_root=ROOT,
            readme_text=readme_text,
            errors=errors,
            require_complete=publishable,
        )
        qwen_complete = validate_qwen_chain(
            episode_dir,
            repository_root=ROOT,
            readme_text=readme_text,
            errors=errors,
        )
        validate_selected_run_contract(
            episode_dir,
            repository_root=ROOT,
            readme_text=readme_text,
            publishable=publishable,
            qwen_complete=qwen_complete,
            errors=errors,
        )
        if qwen_complete:
            qwen_chain_count += 1

    validate_wiki_indexes(
        repository_root=ROOT,
        shows=show_records,
        episodes=episode_records,
        errors=errors,
    )

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
        f"{youtube_url_count} YouTube URLs, "
        f"{qwen_chain_count} complete Qwen ASR chains."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
