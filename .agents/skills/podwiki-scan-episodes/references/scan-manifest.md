# Scan manifest contract

Write strict UTF-8 JSON to `.cache/scans/<scan-id>/scan.json`. Keep all evidence ignored by Git.
The validator rejects duplicate keys, non-finite numbers, inconsistent counts, repository duplicates,
false `complete` states, and incremental windows narrower than the frozen inventory recommends.

## Top-level shape

```json
{
  "schema_version": 1,
  "kind": "podwiki-episode-scan",
  "scan_id": "20260816T090000Z-sv101",
  "show_id": "sv101",
  "show_title": "硅谷101",
  "started_at": "2026-08-16T09:00:00Z",
  "completed_at": "2026-08-16T09:08:00Z",
  "status": "complete",
  "scope": {
    "mode": "incremental",
    "coverage_start": "2026-05-01T00:00:00Z",
    "coverage_end": "2026-08-16T09:08:00Z",
    "repository_commit": "0123456789abcdef0123456789abcdef01234567",
    "required_platforms": ["bilibili"],
    "access_context": "anonymous"
  },
  "sources": [],
  "candidates": [],
  "summary": {
    "eligible_new": 0,
    "already_present": 0,
    "excluded": 0,
    "needs_review": 0
  }
}
```

Use `status: complete` only when every required discovery source is `verified` and has
`coverage_complete: true`. Use `partial` when useful evidence exists but any required coverage is
missing. Use `blocked` when required discovery cannot produce a trustworthy candidate listing.

## Source record

```json
{
  "platform": "bilibili",
  "url": "https://space.bilibili.com/508452265/",
  "role": "discovery",
  "required": true,
  "status": "verified",
  "checked_at": "2026-08-16T09:07:00Z",
  "coverage_complete": true,
  "observed_item_urls": [
    "https://www.bilibili.com/video/BV1Example00/"
  ],
  "evidence": "Rendered official upload listing traversed through the declared coverage start."
}
```

Source `status` is one of `verified`, `blocked`, `unreachable`, `incomplete`, or `not-checked`.
Record every exact item URL observed on a discovery source inside the coverage window in
`observed_item_urls`, including items later classified as present, excluded, or ambiguous. Every
discovery observation must have exactly one candidate classification, and every candidate must
come from a discovery observation. Use an empty array only when the listing truly exposed no item
or could not be observed; the source status and evidence distinguish those cases.
Do not store cookies, tokens, account identifiers, browser profile paths, signed media URLs, or raw
credential material.

Canonical YouTube watch and playlist URLs are the only query-bearing exceptions: they retain
exactly one `v=<video-id>` or `list=<playlist-id>` parameter. A YouTube candidate records all three
identifiers without altering case:

```json
{
  "platform": "youtube",
  "canonical_url": "https://www.youtube.com/watch?v=-RXD4bTuFTo",
  "identifiers": {
    "video_id": "-RXD4bTuFTo",
    "channel_id": "UCXl4i9dYBrFOabk0xGmbkRA",
    "playlist_id": "PLd7-bHaQwnthaNDpZ32TtYONGVk95-fhF"
  }
}
```

## Candidate record

```json
{
  "decision": "eligible-new",
  "platform": "bilibili",
  "canonical_url": "https://www.bilibili.com/video/BV1Example00/",
  "identifiers": {"bvid": "BV1Example00"},
  "title": "Publisher title",
  "published_at": "2026-08-15T12:00:00+08:00",
  "duration_seconds": 7200.25,
  "decision_reason": "Official complete long-form dialogue episode absent from repository.",
  "evidence": [
    {
      "type": "show-identity",
      "url": "https://space.bilibili.com/508452265/",
      "checked_at": "2026-08-16T09:07:00Z",
      "note": "Official publisher and verified podcast identity."
    },
    {
      "type": "complete-episode",
      "url": "https://www.bilibili.com/video/BV1Example00/",
      "checked_at": "2026-08-16T09:07:30Z",
      "note": "Publisher labels and presents the exact item as the complete episode."
    },
    {
      "type": "long-form-dialogue",
      "url": "https://www.bilibili.com/video/BV1Example00/",
      "checked_at": "2026-08-16T09:07:30Z",
      "note": "Long-form dialogue required by a strict show policy."
    }
  ],
  "matched_episode_id": null
}
```

Candidate `decision` is one of `eligible-new`, `already-present`, `excluded`, or `needs-review`.
All candidates need a non-empty `decision_reason` and evidence list. `eligible-new` requires both
`show-identity` and `complete-episode` evidence; `zhangxiaojun` and `sv101` additionally require
`long-form-dialogue`. `already-present` requires the exact `matched_episode_id`. Excluded and
ambiguous items keep their canonical identity so later scans do not oscillate silently.

`summary` counts must exactly match the candidate decisions. A valid manifest is evidence for the
scan; it is not ingestion authorization.
