#!/usr/bin/env python3
"""Refine structured ASR output and render a readable Markdown transcript."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import os
import re
import tempfile
import unicodedata
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
LEGACY_CORRECTION_MIGRATION_VERSION = "legacy-global-v1-migration"
CORRECTION_RULE_ID_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
TRAILING_PUNCTUATION_RE = re.compile(r"[，。！？；：、,.!?;:]$")
LEADING_PUNCTUATION_RE = re.compile(r"^[，。！？；：、,.!?;:]")
MAX_REVERSED_TIMESTAMP_JITTER_SECONDS = 0.250


@dataclass(frozen=True)
class CorrectionRule:
    rule_id: str
    match: str
    replacement: str
    reason: str
    case_sensitive: bool
    expected_hits: int


@dataclass(frozen=True)
class CorrectionMap:
    path: Path
    sha256: str
    schema_version: int
    version: str | int
    episode_id: str
    input_asr_sha256: str
    rules: tuple[CorrectionRule, ...]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Preserve a refined JSON artifact and render it as transcript Markdown."
        )
    )
    parser.add_argument(
        "--input", required=True, type=Path, help="Raw or aligned ASR JSON"
    )
    parser.add_argument(
        "--refined-output", required=True, type=Path, help="Refined ASR JSON"
    )
    parser.add_argument(
        "--output", required=True, type=Path, help="Rendered transcript Markdown"
    )
    parser.add_argument("--episode-id", required=True)
    parser.add_argument("--title", required=True, help="Episode title")
    parser.add_argument("--engine", default="mlx-whisper")
    parser.add_argument("--model", required=True)
    parser.add_argument("--language", default="zh-CN")
    parser.add_argument(
        "--correction-map",
        type=Path,
        help="Episode-scoped, audited literal correction rules",
    )
    parser.add_argument(
        "--rerender",
        action="store_true",
        help="Explicitly replace an existing valid artifact pair",
    )
    return parser.parse_args()


def clean_text(
    value: Any,
    *,
    correction_rules: tuple[CorrectionRule, ...] = (),
    correction_hits: dict[str, int] | None = None,
) -> str:
    text = re.sub(r"\uFFFDN?", "", str(value or ""))
    text = re.sub(r"\s+", " ", text).strip()

    for rule in correction_rules:
        if rule.case_sensitive:
            count = text.count(rule.match)
            text = text.replace(rule.match, rule.replacement)
        else:
            text, count = re.subn(
                re.escape(rule.match),
                lambda _match: rule.replacement,
                text,
                flags=re.IGNORECASE,
            )
        if correction_hits is not None and count:
            correction_hits[rule.rule_id] += count

    text = re.sub(r"\s+([，。！？；：、])", r"\1", text)
    text = re.sub(r"([，。！？；：、])\s+", r"\1", text)
    return text.strip()


def normalized(text: str) -> str:
    return "".join(
        character.lower()
        for character in text
        if not character.isspace()
        and unicodedata.category(character)[0] not in {"P", "S"}
    )


def contains_lexical_content(text: str) -> bool:
    return any(unicodedata.category(character)[0] in {"L", "N"} for character in text)


def append_text(left: str, right: str) -> str:
    if not left:
        return right
    if not right:
        return left
    if TRAILING_PUNCTUATION_RE.search(left) or LEADING_PUNCTUATION_RE.search(right):
        return f"{left}{right}"
    if left[-1].isascii() and left[-1].isalnum() and right[0].isascii() and right[0].isalnum():
        return f"{left} {right}"
    return f"{left}{right}"


def finite_number(value: Any, *, field: str, segment_index: int) -> float:
    if not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(
            f"segment {segment_index} has invalid {field}: {value!r}"
        )
    return float(value)


def normalize_timestamp_bounds(
    *, start: Any, end: Any, segment_index: int
) -> tuple[float, float]:
    normalized_start = finite_number(
        start, field="start", segment_index=segment_index
    )
    normalized_end = finite_number(end, field="end", segment_index=segment_index)

    if normalized_start < 0 or normalized_end < 0:
        raise ValueError(
            f"segment {segment_index} has negative timestamp bounds: "
            f"start={normalized_start!r}, end={normalized_end!r}"
        )

    reversed_by = normalized_start - normalized_end
    if reversed_by > MAX_REVERSED_TIMESTAMP_JITTER_SECONDS:
        raise ValueError(
            f"segment {segment_index} end precedes start by "
            f"{reversed_by:.3f}s, exceeding the "
            f"{MAX_REVERSED_TIMESTAMP_JITTER_SECONDS:.3f}s tolerance"
        )
    if reversed_by > 0:
        normalized_end = normalized_start

    return normalized_start, normalized_end


def refine_segments(
    raw_segments: list[dict[str, Any]],
    *,
    correction_rules: tuple[CorrectionRule, ...] = (),
    correction_hits: dict[str, int] | None = None,
) -> list[dict[str, Any]]:
    refined: list[dict[str, Any]] = []
    previous_start: float | None = None

    for source_index, segment in enumerate(raw_segments):
        text = clean_text(
            segment.get("text"),
            correction_rules=correction_rules,
            correction_hits=correction_hits,
        )
        if not text or not contains_lexical_content(text):
            continue

        start, end = normalize_timestamp_bounds(
            start=segment.get("start"),
            end=segment.get("end"),
            segment_index=source_index,
        )
        if previous_start is not None:
            reversed_by = previous_start - start
            if reversed_by > MAX_REVERSED_TIMESTAMP_JITTER_SECONDS:
                raise ValueError(
                    f"segment {source_index} start precedes the previous "
                    f"segment start by {reversed_by:.3f}s, exceeding the "
                    f"{MAX_REVERSED_TIMESTAMP_JITTER_SECONDS:.3f}s tolerance"
                )
            if reversed_by > 0:
                start = previous_start
                end = max(end, start)
        previous_start = start
        source_id = segment.get("id", source_index)

        if refined and normalized(text) == normalized(refined[-1]["text"]):
            refined[-1]["source_segment_indexes"].append(source_index)
            refined[-1]["source_segment_ids"].append(source_id)
            continue

        refined.append(
            {
                "start": start,
                "end": end,
                "text": text,
                "source_segment_indexes": [source_index],
                "source_segment_ids": [source_id],
            }
        )

    return refined


def merge_blocks(refined_segments: list[dict[str, Any]]) -> list[dict[str, Any]]:
    blocks: list[dict[str, Any]] = []

    for refined_index, segment in enumerate(refined_segments):
        if blocks:
            current = blocks[-1]
            gap = segment["start"] - current["end"]
            merged_text = append_text(current["text"], segment["text"])
            can_merge = (
                gap <= 2.5
                and segment["end"] - current["start"] <= 35
                and len(merged_text) <= 260
            )
        else:
            current = None
            merged_text = segment["text"]
            can_merge = False

        if current is not None and can_merge:
            current["end"] = max(current["end"], segment["end"])
            current["text"] = merged_text
            current["refined_segment_indexes"].append(refined_index)
        else:
            blocks.append(
                {
                    "start": segment["start"],
                    "end": segment["end"],
                    "text": segment["text"],
                    "refined_segment_indexes": [refined_index],
                }
            )

    return blocks


def format_timestamp(seconds: float) -> str:
    total_seconds = max(0, math.floor(seconds))
    hours, remainder = divmod(total_seconds, 3600)
    minutes, remaining_seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{remaining_seconds:02d}"


def render_markdown(
    *,
    refined_segments: list[dict[str, Any]],
    title: str,
) -> str:
    body = "\n".join(
        f'[{format_timestamp(segment["start"])}] {segment["text"]}  '
        for segment in refined_segments
    )
    return f"""# {title}

{body}
"""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def repository_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return resolved.as_posix()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_json_strict(path: Path) -> dict[str, Any]:
    def reject_constant(value: str) -> None:
        raise ValueError(f"non-finite JSON number {value} in {path}")

    def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        document: dict[str, Any] = {}
        for key, value in pairs:
            if key in document:
                raise ValueError(f"duplicate JSON key {key!r} in {path}")
            document[key] = value
        return document

    document = json.loads(
        path.read_text(encoding="utf-8"),
        parse_constant=reject_constant,
        object_pairs_hook=reject_duplicates,
    )
    if not isinstance(document, dict):
        raise ValueError(f"JSON root must be an object: {path}")
    return document


def load_correction_map(path: Path, *, episode_id: str) -> CorrectionMap:
    resolved = path.resolve()
    document = read_json_strict(resolved)
    if document.get("schema_version") != 1:
        raise ValueError("correction map schema_version must be 1")
    if document.get("episode_id") != episode_id:
        raise ValueError("correction map episode_id does not match --episode-id")
    version = document.get("version")
    if isinstance(version, bool) or not isinstance(version, (str, int)) or version == "":
        raise ValueError("correction map version must be a non-empty string or integer")
    input_asr_sha256 = document.get("input_asr_sha256")
    if not isinstance(input_asr_sha256, str) or re.fullmatch(
        r"[0-9a-f]{64}", input_asr_sha256
    ) is None:
        raise ValueError("correction map input_asr_sha256 must be lowercase SHA-256")
    raw_rules = document.get("rules")
    if not isinstance(raw_rules, list):
        raise ValueError("correction map rules must be a list")

    rules: list[CorrectionRule] = []
    seen_ids: set[str] = set()
    for index, raw_rule in enumerate(raw_rules):
        if not isinstance(raw_rule, dict):
            raise ValueError(f"correction rule {index} must be an object")
        unknown_fields = set(raw_rule) - {
            "id",
            "match",
            "replacement",
            "reason",
            "case_sensitive",
            "expected_hits",
        }
        if unknown_fields:
            raise ValueError(
                f"correction rule {index} has unknown fields: "
                f"{', '.join(sorted(unknown_fields))}"
            )
        rule_id = raw_rule.get("id")
        if not isinstance(rule_id, str) or CORRECTION_RULE_ID_RE.fullmatch(
            rule_id
        ) is None:
            raise ValueError(f"correction rule {index} has an invalid id")
        if rule_id in seen_ids:
            raise ValueError(f"duplicate correction rule id: {rule_id}")
        seen_ids.add(rule_id)
        match = raw_rule.get("match")
        replacement = raw_rule.get("replacement")
        reason = raw_rule.get("reason")
        case_sensitive = raw_rule.get("case_sensitive", True)
        expected_hits = raw_rule.get("expected_hits")
        if not isinstance(match, str) or not match:
            raise ValueError(f"correction rule {rule_id} has no match text")
        if not isinstance(replacement, str):
            raise ValueError(f"correction rule {rule_id} has no replacement text")
        if not isinstance(reason, str) or not reason.strip():
            raise ValueError(f"correction rule {rule_id} has no audit reason")
        if not isinstance(case_sensitive, bool):
            raise ValueError(f"correction rule {rule_id} case_sensitive is not boolean")
        if (
            isinstance(expected_hits, bool)
            or not isinstance(expected_hits, int)
            or expected_hits < 1
        ):
            raise ValueError(
                f"correction rule {rule_id} expected_hits must be a positive integer"
            )
        rules.append(
            CorrectionRule(
                rule_id=rule_id,
                match=match,
                replacement=replacement,
                reason=reason,
                case_sensitive=case_sensitive,
                expected_hits=expected_hits,
            )
        )
    return CorrectionMap(
        path=resolved,
        sha256=sha256_file(resolved),
        schema_version=1,
        version=version,
        episode_id=episode_id,
        input_asr_sha256=input_asr_sha256,
        rules=tuple(rules),
    )


def correction_provenance(
    correction_map: CorrectionMap | None,
    *,
    hits: dict[str, int],
) -> dict[str, Any]:
    if correction_map is None:
        return {
            "status": "none",
            "rules": [],
            "total_hits": 0,
        }
    rules = [
        {
            "id": rule.rule_id,
            "match": rule.match,
            "replacement": rule.replacement,
            "reason": rule.reason,
            "case_sensitive": rule.case_sensitive,
            "expected_hits": rule.expected_hits,
            "hits": hits[rule.rule_id],
        }
        for rule in correction_map.rules
    ]
    return {
        "status": "applied",
        "map_path": repository_path(correction_map.path),
        "map_sha256": correction_map.sha256,
        "schema_version": correction_map.schema_version,
        "version": correction_map.version,
        "input_asr_sha256": correction_map.input_asr_sha256,
        "rules": rules,
        "total_hits": sum(hits.values()),
    }


def validate_correction_hits(
    correction_map: CorrectionMap | None,
    *,
    hits: dict[str, int],
) -> None:
    if correction_map is None:
        return
    mismatches = [
        f"{rule.rule_id}: expected={rule.expected_hits}, actual={hits[rule.rule_id]}"
        for rule in correction_map.rules
        if hits[rule.rule_id] != rule.expected_hits
    ]
    if mismatches:
        raise ValueError(
            "correction map hit counts changed; review the aligned input or map: "
            + "; ".join(mismatches)
        )


def render_transaction_path(*, refined_path: Path, transcript_path: Path) -> Path:
    identity = "\0".join(
        sorted((refined_path.resolve().as_posix(), transcript_path.resolve().as_posix()))
    )
    suffix = hashlib.sha256(identity.encode("utf-8")).hexdigest()[:16]
    return refined_path.resolve().parent / f".podwiki-render-{suffix}.transaction.json"


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


def promote_transaction_artifact(temporary_path: Path, target_path: Path) -> None:
    temporary_path.replace(target_path)


def validate_render_temporary_path(
    *, label: str, temporary: Path, target: Path
) -> None:
    expected_prefix = f".podwiki-{target.name}."
    if temporary == target:
        raise ValueError(f"render transaction {label} temporary path equals its target")
    if temporary.parent != target.parent:
        raise ValueError(
            f"render transaction {label} temporary path is outside the target directory"
        )
    if not (
        temporary.name.startswith(expected_prefix)
        and temporary.name.endswith(".tmp")
    ):
        raise ValueError(f"render transaction {label} temporary filename is invalid")


def recover_artifact_pair_transaction(
    *, refined_path: Path, transcript_path: Path
) -> bool:
    transaction_path = render_transaction_path(
        refined_path=refined_path,
        transcript_path=transcript_path,
    )
    if not transaction_path.is_file():
        return False
    transaction = read_json_strict(transaction_path)
    if transaction.get("schema_version") != 1 or transaction.get("kind") != (
        "podwiki-render-transaction"
    ):
        raise ValueError(f"invalid render transaction journal: {transaction_path}")
    artifacts = transaction.get("artifacts")
    if not isinstance(artifacts, dict) or set(artifacts) != {"refined", "transcript"}:
        raise ValueError(f"invalid render transaction artifacts: {transaction_path}")
    expected_targets = {
        "refined": refined_path.resolve(),
        "transcript": transcript_path.resolve(),
    }
    validated_artifacts: list[tuple[str, Path, Path, str]] = []
    for label in ("transcript", "refined"):
        entry = artifacts.get(label)
        if not isinstance(entry, dict):
            raise ValueError(f"invalid {label} render transaction entry")
        target = Path(str(entry.get("target"))).resolve()
        temporary = Path(str(entry.get("temporary"))).resolve()
        expected_sha256 = entry.get("sha256")
        if target != expected_targets[label]:
            raise ValueError(f"render transaction {label} target changed")
        if not isinstance(expected_sha256, str) or re.fullmatch(
            r"[0-9a-f]{64}", expected_sha256
        ) is None:
            raise ValueError(f"render transaction {label} hash is invalid")
        validate_render_temporary_path(
            label=label,
            temporary=temporary,
            target=target,
        )
        validated_artifacts.append((label, temporary, target, expected_sha256))

    for label, temporary, target, expected_sha256 in validated_artifacts:
        if target.is_file() and sha256_file(target) == expected_sha256:
            temporary.unlink(missing_ok=True)
            continue
        if not temporary.is_file() or sha256_file(temporary) != expected_sha256:
            raise ValueError(
                f"cannot recover {label} from render transaction: {transaction_path}"
            )
        promote_transaction_artifact(temporary, target)
        target.chmod(0o644)
    transaction_path.unlink()
    return True


def write_artifact_pair_atomically(
    *, refined_path: Path, refined_text: str, transcript_path: Path, transcript_text: str
) -> None:
    if refined_path.resolve() == transcript_path.resolve():
        raise ValueError("refined JSON and transcript paths must be distinct")
    recover_artifact_pair_transaction(
        refined_path=refined_path,
        transcript_path=transcript_path,
    )
    temporary_paths: dict[str, Path] = {}
    transaction_path = render_transaction_path(
        refined_path=refined_path,
        transcript_path=transcript_path,
    )
    transaction_written = False
    try:
        for label, path, text in (
            ("refined", refined_path, refined_text),
            ("transcript", transcript_path, transcript_text),
        ):
            path.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(
                mode="w",
                encoding="utf-8",
                newline="\n",
                dir=path.parent,
                prefix=f".podwiki-{path.name}.",
                suffix=".tmp",
                delete=False,
            ) as stream:
                stream.write(text)
                stream.flush()
                os.fsync(stream.fileno())
                temporary_paths[label] = Path(stream.name)

        write_json_atomically(
            transaction_path,
            {
                "schema_version": 1,
                "kind": "podwiki-render-transaction",
                "artifacts": {
                    "refined": {
                        "target": refined_path.resolve().as_posix(),
                        "temporary": temporary_paths["refined"].resolve().as_posix(),
                        "sha256": sha256_text(refined_text),
                    },
                    "transcript": {
                        "target": transcript_path.resolve().as_posix(),
                        "temporary": temporary_paths["transcript"].resolve().as_posix(),
                        "sha256": sha256_text(transcript_text),
                    },
                },
            },
        )
        transaction_written = True
        promote_transaction_artifact(temporary_paths["transcript"], transcript_path)
        transcript_path.chmod(0o644)
        temporary_paths.pop("transcript")
        promote_transaction_artifact(temporary_paths["refined"], refined_path)
        refined_path.chmod(0o644)
        temporary_paths.pop("refined")
        transaction_path.unlink()
        transaction_written = False
    finally:
        if not transaction_written:
            for temporary_path in temporary_paths.values():
                temporary_path.unlink(missing_ok=True)


def artifact_pair_is_current(
    *,
    refined_path: Path,
    transcript_path: Path,
    input_path: Path,
    episode_id: str,
    language: str,
    engine: str,
    model: str,
    correction_map: CorrectionMap | None,
) -> bool:
    if not refined_path.is_file() or not transcript_path.is_file():
        return False
    refined = read_json_strict(refined_path)
    source = refined.get("source")
    rendered = refined.get("rendered_transcript")
    if not isinstance(source, dict) or not isinstance(rendered, dict):
        raise ValueError("existing refined artifact has incomplete pair lineage")
    if rendered.get("sha256") != sha256_file(transcript_path):
        raise ValueError("existing refined/transcript pair hash does not match")
    if (
        refined.get("episode_id") != episode_id
        or refined.get("language") != language
        or source.get("input_asr_path") != repository_path(input_path)
        or source.get("input_asr_sha256") != sha256_file(input_path)
        or source.get("engine") != engine
        or source.get("model") != model
        or rendered.get("path") != repository_path(transcript_path)
    ):
        return False
    corrections = refined.get("corrections")
    if correction_map is None:
        return corrections is None or (
            isinstance(corrections, dict) and corrections.get("status") == "none"
        )
    if (
        correction_map.version == LEGACY_CORRECTION_MIGRATION_VERSION
        and (
            corrections is None
            or (
                isinstance(corrections, dict)
                and corrections.get("status") == "none"
            )
        )
    ):
        return legacy_correction_map_reproduces_pair(
            refined=refined,
            input_path=input_path,
            transcript_path=transcript_path,
            correction_map=correction_map,
        )
    return bool(
        isinstance(corrections, dict)
        and corrections.get("status") == "applied"
        and corrections.get("map_path") == repository_path(correction_map.path)
        and corrections.get("map_sha256") == correction_map.sha256
        and corrections.get("version") == correction_map.version
    )


def legacy_correction_map_reproduces_pair(
    *,
    refined: dict[str, Any],
    input_path: Path,
    transcript_path: Path,
    correction_map: CorrectionMap,
) -> bool:
    if correction_map.input_asr_sha256 != sha256_file(input_path):
        return False
    raw = read_json_strict(input_path)
    raw_segments = raw.get("segments")
    if not isinstance(raw_segments, list):
        raise ValueError("legacy correction input has no segment list")
    hits = {rule.rule_id: 0 for rule in correction_map.rules}
    reproduced_segments = refine_segments(
        raw_segments,
        correction_rules=correction_map.rules,
        correction_hits=hits,
    )
    validate_correction_hits(correction_map, hits=hits)
    if reproduced_segments != refined.get("segments"):
        return False
    if merge_blocks(reproduced_segments) != refined.get("blocks"):
        return False
    transcript_bytes = transcript_path.read_bytes()
    try:
        transcript = transcript_bytes.decode("utf-8")
    except UnicodeDecodeError as error:
        raise ValueError("legacy correction transcript is not UTF-8") from error
    first_line = transcript.splitlines()[0] if transcript else ""
    if not first_line.startswith("# "):
        return False
    reproduced_markdown = render_markdown(
        refined_segments=reproduced_segments,
        title=first_line.removeprefix("# "),
    ).encode("utf-8")
    return reproduced_markdown == transcript_bytes


def main() -> int:
    args = parse_args()
    if len(
        {
            args.input.resolve(),
            args.refined_output.resolve(),
            args.output.resolve(),
        }
    ) != 3:
        raise ValueError("input, refined output, and transcript paths must be distinct")
    recover_artifact_pair_transaction(
        refined_path=args.refined_output,
        transcript_path=args.output,
    )
    raw = read_json_strict(args.input)
    raw_segments = raw.get("segments", [])
    if not isinstance(raw_segments, list):
        raise ValueError("input JSON field 'segments' must be a list")
    correction_map = (
        load_correction_map(args.correction_map, episode_id=args.episode_id)
        if getattr(args, "correction_map", None) is not None
        else None
    )
    if (
        correction_map is not None
        and correction_map.input_asr_sha256 != sha256_file(args.input)
    ):
        raise ValueError(
            "correction map input_asr_sha256 does not match the selected ASR input"
        )
    if artifact_pair_is_current(
        refined_path=args.refined_output,
        transcript_path=args.output,
        input_path=args.input,
        episode_id=args.episode_id,
        language=args.language,
        engine=args.engine,
        model=args.model,
        correction_map=correction_map,
    ) and not getattr(args, "rerender", False):
        print(
            json.dumps(
                {
                    "status": "skipped-valid",
                    "input": args.input.as_posix(),
                    "refined_output": args.refined_output.as_posix(),
                    "output": args.output.as_posix(),
                },
                ensure_ascii=False,
                indent=2,
                allow_nan=False,
            )
        )
        return 0
    if (
        args.refined_output.exists() or args.output.exists()
    ) and not getattr(args, "rerender", False):
        raise FileExistsError(
            "existing render artifacts do not match the requested lineage; "
            "inspect them and pass --rerender to replace the pair"
        )

    correction_hits = {
        rule.rule_id: 0 for rule in correction_map.rules
    } if correction_map is not None else {}
    refined_segments = refine_segments(
        raw_segments,
        correction_rules=correction_map.rules if correction_map is not None else (),
        correction_hits=correction_hits,
    )
    validate_correction_hits(correction_map, hits=correction_hits)
    blocks = merge_blocks(refined_segments)
    generated_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    markdown = render_markdown(
        refined_segments=refined_segments,
        title=args.title,
    )

    refined_document = {
        "schema_version": 1,
        "kind": "refined-asr",
        "episode_id": args.episode_id,
        "language": args.language,
        "source": {
            "input_asr_path": repository_path(args.input),
            "input_asr_sha256": sha256_file(args.input),
            "engine": args.engine,
            "model": args.model,
        },
        "rendered_transcript": {
            "path": repository_path(args.output),
            "sha256": sha256_text(markdown),
        },
        "generated_at": generated_at,
        "corrections": correction_provenance(
            correction_map,
            hits=correction_hits,
        ),
        "statistics": {
            "source_segments": len(raw_segments),
            "refined_segments": len(refined_segments),
            "rendered_blocks": len(blocks),
            "rendered_lines": len(refined_segments),
        },
        "segments": refined_segments,
        "blocks": blocks,
    }
    lineage_schema_version = raw.get("lineage_schema_version")
    if lineage_schema_version is not None and (
        type(lineage_schema_version) is not int or lineage_schema_version != 2
    ):
        raise ValueError(
            "input lineage_schema_version must be absent for legacy artifacts "
            "or the strict integer 2"
        )
    if lineage_schema_version == 2:
        raw_source = raw.get("source")
        if not isinstance(raw_source, dict):
            raise ValueError("lineage-v2 aligned input has no source object")
        model_identity = raw_source.get("model_identity")
        aligner_identity = raw_source.get("aligner_identity")
        if not isinstance(model_identity, dict) or not isinstance(
            aligner_identity, dict
        ):
            raise ValueError("lineage-v2 aligned input has incomplete model identities")
        refined_document["lineage_schema_version"] = 2
        aligner_repository = raw_source.get("aligner")
        if not isinstance(aligner_repository, str) or not aligner_repository:
            raise ValueError("lineage-v2 aligned input has no aligner repository")
        refined_document["source"]["aligner"] = aligner_repository
        refined_document["source"]["model_identity"] = copy.deepcopy(model_identity)
        refined_document["source"]["aligner_identity"] = copy.deepcopy(
            aligner_identity
        )

    refined_text = (
        json.dumps(
            refined_document,
            ensure_ascii=False,
            indent=2,
            allow_nan=False,
        )
        + "\n"
    )
    write_artifact_pair_atomically(
        refined_path=args.refined_output,
        refined_text=refined_text,
        transcript_path=args.output,
        transcript_text=markdown,
    )

    print(
        json.dumps(
            {
                "input": args.input.as_posix(),
                "refined_output": args.refined_output.as_posix(),
                "output": args.output.as_posix(),
                "source_segments": len(raw_segments),
                "refined_segments": len(refined_segments),
                "rendered_blocks": len(blocks),
                "rendered_lines": len(refined_segments),
                "generated_at": generated_at,
                "markdown_characters": len(markdown),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
