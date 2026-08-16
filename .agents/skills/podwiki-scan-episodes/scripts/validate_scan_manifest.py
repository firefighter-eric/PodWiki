#!/usr/bin/env python3
"""Validate a PodWiki episode scan manifest against the current repository."""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

import build_episode_inventory as inventory


DECISIONS = {"eligible-new", "already-present", "excluded", "needs-review"}
SCAN_STATUSES = {"complete", "partial", "blocked"}
SOURCE_STATUSES = {"verified", "blocked", "unreachable", "incomplete", "not-checked"}
SOURCE_ROLES = {"discovery", "identity", "cross-check"}
STRICT_DIALOGUE_SHOWS = {"zhangxiaojun", "sv101"}
BVID_RE = re.compile(r"BV[0-9A-Za-z]{10}")
EID_RE = re.compile(r"[0-9a-f]{24}")
GIT_SHA_RE = re.compile(r"[0-9a-f]{40}")


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate object key {key!r}")
        result[key] = value
    return result


def reject_non_finite(value: str) -> None:
    raise ValueError(f"non-finite number {value}")


def read_json_strict(path: Path) -> dict[str, Any]:
    document = json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=reject_duplicate_keys,
        parse_constant=reject_non_finite,
    )
    if not isinstance(document, dict):
        raise ValueError("JSON root must be an object")
    return document


def is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def parse_rfc3339(value: Any) -> datetime | None:
    if not is_non_empty_string(value):
        return None
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def validate_https_url(value: Any, field: str, errors: list[str]) -> str | None:
    if not is_non_empty_string(value):
        errors.append(f"{field} must be a non-empty HTTPS URL")
        return None
    try:
        parsed = urlsplit(str(value))
    except ValueError:
        errors.append(f"{field} must be a valid HTTPS URL")
        return None
    if (
        parsed.scheme != "https"
        or not parsed.netloc
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
    ):
        errors.append(f"{field} must be canonical HTTPS without credentials, query, or fragment")
        return None
    return str(value)


def require_mapping(value: Any, field: str, errors: list[str]) -> dict[str, Any]:
    if not isinstance(value, dict):
        errors.append(f"{field} must be an object")
        return {}
    return value


def require_list(value: Any, field: str, errors: list[str]) -> list[Any]:
    if not isinstance(value, list):
        errors.append(f"{field} must be an array")
        return []
    return value


def validate_candidate_identity(
    candidate: dict[str, Any],
    index: int,
    errors: list[str],
) -> list[str]:
    field = f"candidates[{index}]"
    platform = candidate.get("platform")
    url = validate_https_url(candidate.get("canonical_url"), f"{field}.canonical_url", errors)
    identifiers = require_mapping(candidate.get("identifiers"), f"{field}.identifiers", errors)
    if not is_non_empty_string(platform):
        errors.append(f"{field}.platform must be a non-empty string")
        return []
    if not identifiers:
        errors.append(f"{field}.identifiers must not be empty")
    if url is None:
        return []

    if platform == "bilibili":
        bvid = identifiers.get("bvid")
        if not isinstance(bvid, str) or BVID_RE.fullmatch(bvid) is None:
            errors.append(f"{field}.identifiers.bvid must be a canonical BVID")
        expected = f"https://www.bilibili.com/video/{bvid}/"
        if isinstance(bvid, str) and url != expected:
            errors.append(f"{field}.canonical_url must equal {expected}")
    elif platform == "xiaoyuzhou":
        eid = identifiers.get("eid")
        if not isinstance(eid, str) or EID_RE.fullmatch(eid) is None:
            errors.append(f"{field}.identifiers.eid must be 24 lowercase hex characters")
        expected = f"https://www.xiaoyuzhoufm.com/episode/{eid}"
        if isinstance(eid, str) and url != expected:
            errors.append(f"{field}.canonical_url must equal {expected}")
    elif platform == "rss" and not any(
        is_non_empty_string(identifiers.get(key)) for key in ("guid", "rss_guid", "episode_guid")
    ):
        errors.append(f"{field}.identifiers must include a publisher GUID for RSS")
    return inventory.source_keys(
        {"platform": platform, "url": url, "identifiers": identifiers}
    )


def validate_manifest(document: dict[str, Any], repository_root: Path) -> list[str]:
    errors: list[str] = []
    if document.get("schema_version") != 1:
        errors.append("schema_version must equal 1")
    if document.get("kind") != "podwiki-episode-scan":
        errors.append("kind must equal 'podwiki-episode-scan'")
    if not is_non_empty_string(document.get("scan_id")):
        errors.append("scan_id must be a non-empty string")

    show_id = document.get("show_id")
    if not is_non_empty_string(show_id):
        errors.append("show_id must be a non-empty string")
        show_id = ""
    try:
        current_inventory = inventory.build_inventory(
            repository_root,
            selected_show_ids={str(show_id)} if show_id else None,
        )
    except (OSError, UnicodeError, ValueError) as error:
        errors.append(f"repository inventory failed: {error}")
        return errors
    shows = current_inventory["shows"]
    if len(shows) != 1:
        errors.append("show_id must select exactly one repository show")
        return errors
    show = shows[0]
    if document.get("show_title") != show.get("title"):
        errors.append("show_title must match the selected show README")

    started = parse_rfc3339(document.get("started_at"))
    completed = parse_rfc3339(document.get("completed_at"))
    if started is None:
        errors.append("started_at must be timezone-aware RFC 3339")
    if completed is None:
        errors.append("completed_at must be timezone-aware RFC 3339")
    if started is not None and completed is not None and completed < started:
        errors.append("completed_at must not precede started_at")
    status = document.get("status")
    if status not in SCAN_STATUSES:
        errors.append(f"status must be one of {sorted(SCAN_STATUSES)}")

    scope = require_mapping(document.get("scope"), "scope", errors)
    if scope.get("mode") not in {"incremental", "full"}:
        errors.append("scope.mode must be 'incremental' or 'full'")
    coverage_start = parse_rfc3339(scope.get("coverage_start"))
    coverage_end = parse_rfc3339(scope.get("coverage_end"))
    if coverage_start is None or coverage_end is None:
        errors.append("scope coverage_start and coverage_end must be timezone-aware RFC 3339")
    elif coverage_end < coverage_start:
        errors.append("scope.coverage_end must not precede coverage_start")
    recommended_start = parse_rfc3339(show.get("recommended_incremental_coverage_start"))
    if (
        scope.get("mode") == "incremental"
        and recommended_start is not None
        and coverage_start is not None
        and coverage_start > recommended_start
    ):
        errors.append(
            "scope.coverage_start is narrower than the repository inventory recommendation "
            f"{show['recommended_incremental_coverage_start']}"
        )
    if completed is not None and coverage_end is not None and coverage_end > completed:
        errors.append("scope.coverage_end must not follow completed_at")
    commit = scope.get("repository_commit")
    if commit is not None and (not isinstance(commit, str) or GIT_SHA_RE.fullmatch(commit) is None):
        errors.append("scope.repository_commit must be null or a 40-character lowercase Git SHA")
    current_commit = current_inventory.get("repository_commit")
    if commit is not None and current_commit is not None and commit != current_commit:
        errors.append("scope.repository_commit does not match the current repository inventory")
    required_platforms = require_list(scope.get("required_platforms"), "scope.required_platforms", errors)
    if not required_platforms or not all(is_non_empty_string(value) for value in required_platforms):
        errors.append("scope.required_platforms must contain non-empty platform strings")
    if len(set(required_platforms)) != len(required_platforms):
        errors.append("scope.required_platforms must not contain duplicates")
    if not is_non_empty_string(scope.get("access_context")):
        errors.append("scope.access_context must be a non-sensitive access label")

    sources = require_list(document.get("sources"), "sources", errors)
    required_discovery_platforms: set[str] = set()
    required_sources: list[dict[str, Any]] = []
    observed_discovery_urls: set[tuple[str, str]] = set()
    for index, raw_source in enumerate(sources):
        source = require_mapping(raw_source, f"sources[{index}]", errors)
        platform = source.get("platform")
        if not is_non_empty_string(platform):
            errors.append(f"sources[{index}].platform must be a non-empty string")
        validate_https_url(source.get("url"), f"sources[{index}].url", errors)
        if source.get("role") not in SOURCE_ROLES:
            errors.append(f"sources[{index}].role must be one of {sorted(SOURCE_ROLES)}")
        if not isinstance(source.get("required"), bool):
            errors.append(f"sources[{index}].required must be boolean")
        if source.get("status") not in SOURCE_STATUSES:
            errors.append(f"sources[{index}].status must be one of {sorted(SOURCE_STATUSES)}")
        if parse_rfc3339(source.get("checked_at")) is None:
            errors.append(f"sources[{index}].checked_at must be timezone-aware RFC 3339")
        if not isinstance(source.get("coverage_complete"), bool):
            errors.append(f"sources[{index}].coverage_complete must be boolean")
        if not is_non_empty_string(source.get("evidence")):
            errors.append(f"sources[{index}].evidence must be non-empty")
        observed_urls = require_list(
            source.get("observed_item_urls"),
            f"sources[{index}].observed_item_urls",
            errors,
        )
        source_observed: set[str] = set()
        for observed_index, observed_url in enumerate(observed_urls):
            normalized_url = validate_https_url(
                observed_url,
                f"sources[{index}].observed_item_urls[{observed_index}]",
                errors,
            )
            if normalized_url is None:
                continue
            if normalized_url in source_observed:
                errors.append(f"sources[{index}].observed_item_urls must not contain duplicates")
            source_observed.add(normalized_url)
            if source.get("role") == "discovery" and isinstance(platform, str):
                observed_discovery_urls.add((platform, normalized_url))
        if source.get("required") is True:
            required_sources.append(source)
            if source.get("role") == "discovery" and isinstance(platform, str):
                required_discovery_platforms.add(platform)
    missing_required = sorted(set(required_platforms) - required_discovery_platforms)
    if missing_required:
        errors.append(
            "required discovery source missing for platform(s): " + ", ".join(missing_required)
        )
    if status == "complete" and any(
        source.get("status") != "verified" or source.get("coverage_complete") is not True
        for source in required_sources
    ):
        errors.append("complete scans require every required source to be verified and complete")
    if status == "blocked" and required_sources and all(
        source.get("status") == "verified" and source.get("coverage_complete") is True
        for source in required_sources
    ):
        errors.append("blocked scans must identify incomplete required coverage")

    episodes_by_id = {episode["id"]: episode for episode in show["episodes"]}
    known_keys = set(show["known_source_keys"])
    seen_urls: set[str] = set()
    seen_keys: set[str] = set()
    classified_discovery_urls: set[tuple[str, str]] = set()
    counts: Counter[str] = Counter()
    candidates = require_list(document.get("candidates"), "candidates", errors)
    for index, raw_candidate in enumerate(candidates):
        candidate = require_mapping(raw_candidate, f"candidates[{index}]", errors)
        decision = candidate.get("decision")
        if decision not in DECISIONS:
            errors.append(f"candidates[{index}].decision must be one of {sorted(DECISIONS)}")
        else:
            counts[decision] += 1
        keys = validate_candidate_identity(candidate, index, errors)
        url = candidate.get("canonical_url")
        if isinstance(url, str):
            if url in seen_urls:
                errors.append(f"candidates[{index}].canonical_url duplicates another candidate")
            seen_urls.add(url)
            platform = candidate.get("platform")
            if isinstance(platform, str):
                classified_discovery_urls.add((platform, url))
        duplicate_keys = sorted(set(keys) & seen_keys)
        if duplicate_keys:
            errors.append(f"candidates[{index}] duplicates candidate identity {duplicate_keys[0]}")
        seen_keys.update(keys)
        if not is_non_empty_string(candidate.get("title")):
            errors.append(f"candidates[{index}].title must be non-empty")
        published = candidate.get("published_at")
        if published is not None and parse_rfc3339(published) is None:
            errors.append(f"candidates[{index}].published_at must be null or RFC 3339")
        if decision in {"eligible-new", "already-present"} and parse_rfc3339(published) is None:
            errors.append(f"candidates[{index}].published_at is required for {decision}")
        duration = candidate.get("duration_seconds")
        if duration is not None and (
            not isinstance(duration, (int, float))
            or isinstance(duration, bool)
            or not math.isfinite(float(duration))
            or duration <= 0
        ):
            errors.append(f"candidates[{index}].duration_seconds must be null or positive finite")
        if not is_non_empty_string(candidate.get("decision_reason")):
            errors.append(f"candidates[{index}].decision_reason must be non-empty")

        evidence = require_list(candidate.get("evidence"), f"candidates[{index}].evidence", errors)
        evidence_types: set[str] = set()
        for evidence_index, raw_evidence in enumerate(evidence):
            item = require_mapping(
                raw_evidence,
                f"candidates[{index}].evidence[{evidence_index}]",
                errors,
            )
            evidence_type = item.get("type")
            if not is_non_empty_string(evidence_type):
                errors.append(
                    f"candidates[{index}].evidence[{evidence_index}].type must be non-empty"
                )
            else:
                evidence_types.add(str(evidence_type))
            validate_https_url(
                item.get("url"),
                f"candidates[{index}].evidence[{evidence_index}].url",
                errors,
            )
            if parse_rfc3339(item.get("checked_at")) is None:
                errors.append(
                    f"candidates[{index}].evidence[{evidence_index}].checked_at must be RFC 3339"
                )
            if not is_non_empty_string(item.get("note")):
                errors.append(
                    f"candidates[{index}].evidence[{evidence_index}].note must be non-empty"
                )
        if not evidence:
            errors.append(f"candidates[{index}].evidence must not be empty")
        if decision == "eligible-new":
            missing = {"show-identity", "complete-episode"} - evidence_types
            if missing:
                errors.append(
                    f"candidates[{index}] eligible-new evidence missing {sorted(missing)}"
                )
            if show_id in STRICT_DIALOGUE_SHOWS:
                if candidate.get("platform") != "bilibili":
                    errors.append(
                        f"candidates[{index}] {show_id} eligible-new must be on official Bilibili"
                    )
                if "long-form-dialogue" not in evidence_types:
                    errors.append(
                        f"candidates[{index}] {show_id} requires long-form-dialogue evidence"
                    )
            overlap = sorted(set(keys) & known_keys)
            if overlap:
                errors.append(
                    f"candidates[{index}] eligible-new already exists in repository as {overlap[0]}"
                )
        matched_id = candidate.get("matched_episode_id")
        if decision == "already-present":
            if matched_id not in episodes_by_id:
                errors.append(
                    f"candidates[{index}].matched_episode_id must name a repository episode"
                )
            else:
                matched_keys = set(episodes_by_id[matched_id]["source_keys"])
                if not (set(keys) & matched_keys):
                    errors.append(
                        f"candidates[{index}] does not share an exact identity with {matched_id}"
                    )
        elif matched_id is not None:
            errors.append(
                f"candidates[{index}].matched_episode_id must be null outside already-present"
            )

    expected_summary = {
        "eligible_new": counts["eligible-new"],
        "already_present": counts["already-present"],
        "excluded": counts["excluded"],
        "needs_review": counts["needs-review"],
    }
    summary = require_mapping(document.get("summary"), "summary", errors)
    if summary != expected_summary:
        errors.append(f"summary must exactly equal {expected_summary}")
    if status == "blocked" and counts["eligible-new"]:
        errors.append("blocked scans must not claim eligible-new candidates")
    missing_classifications = sorted(observed_discovery_urls - classified_discovery_urls)
    if missing_classifications:
        platform, url = missing_classifications[0]
        errors.append(f"observed discovery item is not classified: {platform} {url}")
    orphan_classifications = sorted(classified_discovery_urls - observed_discovery_urls)
    if orphan_classifications:
        platform, url = orphan_classifications[0]
        errors.append(f"candidate is absent from discovery observations: {platform} {url}")
    return errors


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--repository-root", type=Path, default=Path.cwd())
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    try:
        document = read_json_strict(args.manifest)
        errors = validate_manifest(document, args.repository_root)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as load_error:
        print(f"scan manifest error: {load_error}", file=sys.stderr)
        return 1
    if errors:
        for message in errors:
            print(f"ERROR: {message}", file=sys.stderr)
        return 1
    print(f"validated scan manifest: {args.manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
