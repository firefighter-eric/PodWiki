---
name: podwiki-scan-episodes
description: Discover, verify, and diff PodWiki podcast episodes without downloading media or creating episode content. Use when asked to scan shows or channels, check for episode updates, find new/recent/missing episodes, audit discovery completeness, or prepare a verified candidate manifest for the add-episodes workflow.
---

# Scan PodWiki episodes

Find candidate episodes, prove the scope of the scan, and stop before ingestion. Treat discovery
as an evidence and coverage task rather than a search-results task.

## Keep the boundary hard

- Read `AGENTS.md`, `docs/content-standard.md`, and every selected show README before scanning.
- Do not download media, create episode directories, run ASR, edit indexes, or change tracked
  episode content. Metadata-only requests and ignored `.cache/scans/` evidence are allowed.
- Do not treat a scan request as permission to add episodes. Invoke `$podwiki-add-episodes` only
  when the user also asks to add/process the exact candidates.
- Do not enumerate another show, account, or platform beyond the requested or inferred active-show
  scope. Authentication changes access context, not authorization or podcast eligibility.
- Never report `no updates` when a required discovery surface is blocked, unreachable, stale, or
  only partially traversed. Report `partial` or `blocked` and name the missing coverage.

## Load the focused references

1. Read [show-policies.md](references/show-policies.md) for the selected show's eligibility and
   source-role overrides.
2. Read [platform-strategies.md](references/platform-strategies.md) only for the platforms present
   in that show's README.
3. Read [scan-manifest.md](references/scan-manifest.md) before writing the result.

The show README remains the source of truth for show identity and source URLs. The reference files
define scanning behavior and exceptions; they do not replace tracked show metadata.

## Establish scope and coverage

1. Interpret a named show literally. If the user says to scan all shows, select all show READMEs
   whose `status` is `active`. Do not silently add a new show.
2. Select one mode per show:
   - `incremental`: find updates in a declared time window.
   - `full`: exhaust the publisher's eligible history.
3. For an incremental scan, use the inventory's
   `recommended_incremental_coverage_start`. It is computed as the earlier of:
   - 90 days before the newest stored episode publication time; or
   - the publication time of the third-newest stored episode.
   If the show has fewer than three stored episodes, the overlap point is the earliest stored
   publication time. If no stored episode has a valid publication time, use `full` mode or report
   the missing baseline; do not invent an incremental start.
4. Set `coverage_end` to the scan completion time. Enumerate every item on each required publisher
   surface inside that closed window. Continue past the newest known item until the coverage start
   is crossed and the current page or result batch is complete.
5. A full scan is complete only after all pages or collection entries are exhausted. If the
   publisher does not expose a verifiable end, record `partial`; do not imply full-history coverage.

The window makes a negative result precise. It does not claim that older, backfilled publisher
items outside the window do not exist.

## Freeze the repository baseline

Create an ignored scan directory and generate a deterministic repository inventory before network
discovery. Use UTC in directory names.

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python \
  .agents/skills/podwiki-scan-episodes/scripts/build_episode_inventory.py \
  --repository-root . \
  --show <show-id> \
  --output .cache/scans/<scan-id>/inventory.json
```

Record the inventory Git commit in the scan manifest. If the worktree changes during a long scan,
regenerate the inventory before final classification and record the new commit.

## Build and execute the source plan

1. Classify each show source as:
   - `discovery`: authoritative for whether an update exists under project policy;
   - `identity`: proves the show is a podcast;
   - `cross-check`: helps map titles, numbers, GUIDs, dates, or duration but cannot create a
     candidate by itself.
2. Mark every policy-required discovery source with `required: true` in the manifest.
3. Retrieve sources freshly. Record the final canonical URL, access context (`anonymous` or the
   user-authorized non-sensitive alias), check time, response status, and coverage result.
4. Search engines and cached snippets are leads only. They may find a URL but can never prove
   enumeration completeness or a negative result.
5. Record every exact item URL observed on a discovery surface inside the window in that source's
   `observed_item_urls`. The manifest validator requires a one-to-one classification for those
   observations; do not omit known, excluded, or ambiguous items to make the result look clean.
6. When Bilibili returns a CAPTCHA, HTTP 412/352, an empty application shell, or an extractor block,
   record the source as blocked. Do not bypass access controls, reuse credentials without explicit
   authorization, or substitute RSS/another platform for a Bilibili-required update policy.
7. For each plausible exact episode URL, run metadata-only intake when supported. Keep its output
   inside the scan directory; do not use the media cache and do not download bytes.

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/acquire_media.py \
  --url <canonical-episode-url> \
  --output .cache/scans/<scan-id>/intake/<source-id>/source.m4a \
  --metadata-only
```

If the actual authorized access context exposes a subtitle, record that fact for the add workflow;
the scan still does not import it or start ASR.

## Classify every discovered item

Apply both gates independently:

1. **Show gate:** affirmative publisher evidence identifies the source as the selected podcast.
2. **Episode gate:** affirmative publisher evidence identifies the exact item as a complete official
   episode allowed by the show policy.

Long duration, interview appearance, an `EP` token, channel ownership, tags, or audio suitability
are not sufficient evidence. Apply the most restrictive rule from `docs/content-standard.md`, the
show README, and `show-policies.md`.

Assign exactly one decision to every item in the covered publisher listing:

- `eligible-new`: passes both gates and is absent from the frozen repository inventory;
- `already-present`: passes both gates and matches a stored episode;
- `excluded`: conclusively fails a gate, with a stable reason;
- `needs-review`: evidence is ambiguous, conflicting, or unavailable.

Deduplicate in this order:

1. exact platform stable identifier (`bvid`, `eid`, publisher GUID, or documented equivalent);
2. canonical source URL;
3. verified publisher episode number within the same show;
4. explicit publisher cross-platform mapping.

Never deduplicate or declare identity from fuzzy title similarity alone. Guest, title, duration,
description, chapters, and publication time are corroborating evidence; record disagreements.

## Validate and report

Write one `scan.json` per show under `.cache/scans/<scan-id>/`, then run:

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python \
  .agents/skills/podwiki-scan-episodes/scripts/validate_scan_manifest.py \
  .cache/scans/<scan-id>/scan.json \
  --repository-root .
```

Fix all validation errors before reporting. Report each show separately with:

- scan status (`complete`, `partial`, or `blocked`) and exact covered window;
- required sources, access context, and source-level coverage;
- counts for all four candidate decisions;
- each `eligible-new` and `needs-review` item with canonical URL and reason;
- stable exclusion counts/reasons and repository matches;
- the manifest and inventory paths.

Use the phrase `no updates` only when status is `complete`, the manifest validates, and
`eligible_new` is zero. Otherwise say that the result is incomplete or unverified.

## Hand off to adding

When the same user request also authorizes adding, pass the validated scan manifest and the exact
`eligible-new` candidate URLs or identifiers to `$podwiki-add-episodes`. The add workflow must
revalidate source identity and access state, freeze only the approved subset, and must not resume
discovery or expand the list.
