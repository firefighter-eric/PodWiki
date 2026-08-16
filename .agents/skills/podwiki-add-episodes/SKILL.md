---
name: podwiki-add-episodes
description: Add or continue exact approved PodWiki podcast episodes through metadata intake, media acquisition, local ASR, transcript rendering or translation, summary creation, index updates, and repository validation. Use when asked to add, ingest, download, transcribe, resume, retranscribe, realign, regenerate, or validate named episode URLs or eligible candidates from a podwiki-scan-episodes manifest.
---

# Add PodWiki episodes

Move exact approved episodes through the requested processing stage while preserving source
identity, resumability, provenance, and review status. Discovery is deliberately out of scope.

## Establish the exact input

1. Read AGENTS.md, docs/episode-processing.md, docs/content-standard.md, the relevant templates,
   and the selected show's README before editing.
2. Accept one of:
   - exact canonical episode URLs named by the user;
   - exact existing episode directories to resume; or
   - a validated $podwiki-scan-episodes manifest plus the exact approved eligible-new subset.
3. When consuming a scan manifest, validate it against the current repository:

~~~bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python \
  .agents/skills/podwiki-scan-episodes/scripts/validate_scan_manifest.py \
  <scan.json> --repository-root .
~~~

4. Do not enumerate channels, feeds, collections, or show pages; do not add URLs discovered during
   ingestion. If the user asks to find updates, invoke $podwiki-scan-episodes first.
5. A partial scan may hand off an exact individually verified candidate only when the user approves
   that URL. Never interpret a partial scan as authorization to add all updates.
6. For multiple episodes, freeze only the approved URLs and their scan evidence into
   .cache/intake/<show-id>/manifest.json. Record the source scan path and SHA-256. Do not change
   the list during the run.
7. Inspect git status -sb, existing episode/cache artifacts, and concurrent changes. Preserve all
   user work and existing outputs unless replacement was explicitly requested.

## Select the stopping point

- intake: verify source identity, access state, podcast eligibility, and subtitle availability.
- acquire: stop after verified ignored media and sidecar.
- transcribe: stop at the requested raw or aligned checkpoint.
- add, ingest, or process: continue through tracked transcript, summary, both indexes, and all
  completion gates.

Do not present a partial stage as a complete episode. Report each episode's reached state and
restart point separately.

## Revalidate every source

Read the matching source guide before running intake:

- [bilibili.md](references/bilibili.md)
- [xiaoyuzhou.md](references/xiaoyuzhou.md)
- [youtube.md](references/youtube.md)

Canonicalize the exact URL and remove tracking parameters. Run metadata-only intake in the same
authorized access context intended for acquisition:

~~~bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/acquire_media.py \
  --url <canonical-url> \
  --output .cache/intake/<source-id>/source.m4a \
  --metadata-only
~~~

Require affirmative publisher evidence that both the show is a verified podcast and the exact item
is a complete official episode under docs/content-standard.md. A prior scan decision is evidence,
not a bypass. Re-check uploader/show identity, stable identifiers, public-free access state, single
page, and subtitle tracks.

Stop without downloading or creating tracked files when:

- podcast or complete-episode evidence is absent, ambiguous, or conflicts with fresh metadata;
- the item is paid, membership-only, private, regional, or otherwise restricted;
- the authorized access context exposes a usable subtitle, because subtitle import is not yet
  implemented;
- the platform's tracked source/key contract is unsupported; YouTube currently stops at verified
  metadata or public media acquisition;
- source identity cannot be preserved without leaking credentials.

User-authorized login is an access context only. Keep cookies, tokens, and browser material under
ignored .cache/credentials/; never print or record secrets in logs, sidecars, Markdown, or Git.

## Create or resume the episode

1. Use only a publisher-confirmed formal number. Never infer one from order, date, scan position, or
   a title token.
2. Without a formal number, use the documented source key:
   - Bilibili: bili-<lowercase-bvid>;
   - Xiaoyuzhou: xiaoyuzhou-<eid>;
   - YouTube: stop before tracked ingestion.
3. Reuse an existing directory only after its show/episode/source identity matches. Do not copy a
   template over an existing episode.
4. For a new episode, copy templates/episode/README.md and fill only verified values. Do not leave
   placeholders or guess participants, language, numbering, profiles, navigation title, or catalog
   keyword.
5. Keep workflow.transcript: not-started until media exists. Publisher material supports only
   workflow.summary: outline.

## Acquire and verify media

~~~bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/acquire_media.py \
  --url <canonical-url> \
  --output .cache/media/<show-id>/<episode-folder>/source.m4a
~~~

Require both media and source.metadata.json. Verify canonical identity, codec, duration, byte size,
sample rate, channels, and SHA-256 before recording local_audio_cache or setting source-acquired.
Reuse only an identity/hash-matching cache. Use --overwrite, --repair-metadata, or an expected
SHA-256 only under the explicit recovery/overwrite conditions in docs/episode-processing.md.

Media, model files, credentials, logs, and temporary checkpoints remain under ignored .cache/.

## Run local ASR serially

Read [asr-backends.md](references/asr-backends.md) before selecting a backend.

1. Respect an explicitly requested compatible engine/model; otherwise reuse recorded provenance or
   use the project Qwen default for the current supported platform.
2. Never silently fall back to a remote or paid service.
3. Run one episode per child process and one accelerator worker at a time. Metadata preparation can
   be parallelized when safe; MLX or CUDA ASR cannot.
4. Use scripts/process_qwen3_asr_batch.py with every intended episode passed explicitly. Group
   batches by language. Never combine cache autodiscovery with replacement flags.
5. Preserve raw.json -> aligned.json -> refined.json -> transcript.<language>.md. Valid v2 raw can
   resume at alignment; markerless historical partials or realignment require explicit
   --retranscribe. Never backfill current model identity into historical artifacts.
6. Keep prior ASR runs. Replacement requires explicit --retranscribe, --realign, or rerender
   authorization as defined by the runbook.

The batch script stops at run-directory artifacts. It does not promote the root transcript, update
metadata, translate English, write the summary, or update indexes.

## Promote, translate, and summarize

1. Validate the selected run, then copy its Markdown to the root only if no conflicting root file
   exists or replacement was explicitly approved. The root file must be byte-identical to the
   selected run artifact.
2. Record actual engine, model, aligner, options, timestamps, counts, paths, and SHA-256 values in the
   episode README. Mark exactly one ASR run selected; preserve older runs as candidate or
   superseded.
3. For an English selected transcript, keep transcript.en.md selected and create a one-to-one,
   timestamp-preserving root transcript.zh-CN.md translation with the complete hashes and status
   contract from the runbook.
4. Generate summary.zh-CN.md only from the selected complete transcript. Validate every summary
   timestamp against that transcript's exact timestamp set.
5. Machine output remains workflow.transcript: machine, workflow.summary: draft, and translation
   status: machine until the corresponding human review is actually complete.

## Synchronize indexes and validate

Add a Web-publishable episode to both the root six-column index and the show five-column index in
date-descending order. Update the root show table only when show identity or metadata changes.
Never index an intake, outline, or source-acquired record.

Run the repository completion gate from the root:

~~~bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python -m unittest discover -s tests -v
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/validate.py
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/audit_correction_migration.py
npm --prefix apps/web audit --audit-level=high
npm --prefix apps/web run check
git diff --check
git status --short
~~~

Also run the lock, lint, type, compile, and supply-chain gates from CONTRIBUTING.md when Python,
dependencies, or CI changed. Confirm cache media remains ignored and expected Markdown/ASR files
are trackable.

Report every episode with canonical URL, stable ID, reached state, artifacts, engine/model, test
results, and remaining listening, terminology, translation, or fact review. Publishing, committing,
opening a PR, or merging requires the user's separate authorization.
