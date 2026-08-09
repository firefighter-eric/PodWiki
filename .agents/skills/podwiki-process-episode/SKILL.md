---
name: podwiki-process-episode
description: Fully process PodWiki episodes from public Bilibili or Xiaoyuzhou sources, acquire public YouTube media, or resume existing local-media artifacts. Use when adding, downloading, resuming, retranscribing, regenerating, or validating an episode through source acquisition, ASR, transcript rendering, metadata updates, and repository checks.
---

# Process a PodWiki episode

Move one or more episodes through the requested machine-processing stages while
preserving source provenance, resumability, and the repository content standard.

## Establish scope

1. Read `docs/episode-processing.md`, `docs/content-standard.md`, and the relevant templates
   before editing. Treat the runbook as the canonical end-to-end order and this skill as its
   execution and safety policy.
2. Inspect the existing show, episode directory, cache, ASR artifacts, and Git changes.
3. Infer the requested stopping point:
   - Download or acquire: stop after verified local media and metadata.
   - Transcribe or retranscribe: stop after raw ASR unless rendering is also requested.
   - Process, add, or ingest: continue through rendered machine transcript and validation.
4. Never treat list order as an official episode number. Use a verified publisher number;
   otherwise use the documented source-ID key (for example, a lower-cased BVID key for
   Bilibili or the canonical `eid` key for Xiaoyuzhou).
5. Preserve existing artifacts. Reuse only when identity metadata and hashes match; require
   an explicit overwrite request to replace an existing source or raw ASR result.

## Process sources

1. Canonicalize the supplied URL and remove tracking parameters. When a Bilibili festival or
   campaign URL carries `bvid=<BVID>`, extract that identifier and form
   `https://www.bilibili.com/video/<BVID>/`; never pass the festival page to the acquisition
   script.
2. Read the matching source guide: `references/bilibili.md`, `references/youtube.md`, or
   `references/xiaoyuzhou.md`.
3. Run the metadata-only intake and check for a public subtitle track before downloading
   media. The repository does not yet provide a subtitle importer. If a public subtitle is
   present, stop and report that unsupported branch instead of silently falling through to
   audio ASR.
4. YouTube currently supports canonicalization, metadata intake, and public media acquisition
   only. Stop before tracked episode ingestion because the repository has not defined its
   source-identifiers contract or a stable key for unnumbered videos.
5. Do not bypass login, membership, payment, region, or other access controls. This workflow
   never uses browser cookies; even an authorized request requires a separate, explicitly
   documented source-handling workflow.
6. By default acquire only one video or podcast episode, never an account, channel,
   playlist, or entire podcast. A bounded whole-podcast exception is allowed only when the
   user explicitly authorizes one verified Xiaoyuzhou podcast. Before downloading, freeze a
   manifest containing that podcast PID and every canonical episode URL/eid in scope. Admit
   only anonymous `NORMAL`, `FREE`, non-private, explicitly `PUBLIC` episodes whose podcast
   identity matches; reject and report every other item. Process the frozen manifest
   sequentially with rate limiting and repeat the full identity validation for each episode.
   Never expand the manifest during the run or extend the authorization to another podcast.
   Whether invoked once or from such an authorized manifest, each acquisition command still
   receives exactly one canonical episode URL:

   ```bash
   env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/acquire_media.py \
     --url <canonical-url> \
     --output .cache/media/<show-id>/<episode-folder>/source.m4a
   ```

   On PowerShell, set `$env:UV_CACHE_DIR = ".cache/uv"` once, omit the leading POSIX
   `env UV_CACHE_DIR=...`, and either run each command on one line or replace `\` with the
   PowerShell backtick. These equivalents apply to every command in this skill.

7. Require the sidecar `source.metadata.json` and verify codec, duration, size, sample rate,
   channels, and SHA-256 before marking the source acquired.
8. Keep downloaded media and temporary files under `.cache/`; never add them to Git.

## Select and run ASR

Read `references/asr-backends.md` before choosing an engine.

Confirm the prerequisites and platform boundary in `docs/episode-processing.md`. The official
local Qwen paths are Apple Silicon/MLX and Windows x86-64/NVIDIA CUDA. Select the matching
backend explicitly; do not silently substitute a remote service on another platform.

The `asr` and `asr-cuda` extras are mutually exclusive. On macOS 14+ Apple Silicon, install
the media and MLX stacks together with `uv sync --locked --extra media --extra asr`, then use
`env UV_CACHE_DIR=.cache/uv uv run --no-sync` for every worker. On Windows, prepare the ignored
`.cache/venvs/qwen-cuda` environment with
`uv sync --active --locked --extra media --extra asr-cuda` and invoke its
`Scripts/python.exe` directly. Never sync dependencies while workers are running. For a cold
Apple Silicon/MLX cache, use the official Hugging Face endpoint by default and stable ignored
paths:

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync hf download \
  mlx-community/Qwen3-ASR-1.7B-8bit \
  --revision a8379a2e2f9e313c9292cdf1af4055ab56d50d55 \
  --local-dir .cache/models/qwen3-asr-1.7b-8bit-pinned-v2
env UV_CACHE_DIR=.cache/uv uv run --no-sync hf download \
  mlx-community/Qwen3-ForcedAligner-0.6B-8bit \
  --revision 0e1a68e91d815300c7c9754b2a7639378b23db15 \
  --local-dir .cache/models/qwen3-forced-aligner-0.6b-8bit-pinned-v2
```

For a cold Windows/CUDA cache, download the official models to their ignored local paths:

```powershell
& .cache/venvs/qwen-cuda/Scripts/hf.exe download Qwen/Qwen3-ASR-1.7B-hf `
  --revision bcd2b5b7f32b480ab5790554cfa8347f246a14f3 `
  --local-dir .cache/models/Qwen3-ASR-1.7B-hf-pinned-v3
& .cache/venvs/qwen-cuda/Scripts/hf.exe download Qwen/Qwen3-ForcedAligner-0.6B-hf `
  --revision c07281df297b9905d24a508279258cccf987a064 `
  --local-dir .cache/models/Qwen3-ForcedAligner-0.6B-hf-pinned-v3
```

Only when the official endpoint is unreachable on the current network may `HF_ENDPOINT` be
temporarily pointed at a mirror. A mirror is transport, not evidence of upstream authenticity.
The full commit pin, per-payload download metadata/ETag, and freshly computed SHA-256 values make
the acquired local snapshot reproducible; upstream trust still comes from the official Hugging
Face Hub. Keep the CUDA native `*-pinned-v3` directories separate from legacy snapshot/symlink
caches that do not contain download metadata for every payload file; MLX retains its independent
`*-pinned-v2` directories.

1. Use an explicitly requested engine and model when compatible.
2. Otherwise reuse the episode's recorded engine and model for reproducibility.
3. For Chinese episodes on Apple Silicon, use the project-selected Qwen3-ASR 1.7B 8-bit
   MLX model with its 8-bit ForcedAligner. On Windows/NVIDIA CUDA, use the official
   `Qwen/Qwen3-ASR-1.7B-hf` and `Qwen/Qwen3-ForcedAligner-0.6B-hf` models through native Transformers
   backend. Keep MLX Whisper only as a retained baseline when it already exists or when the
   user explicitly requests it.
4. Never silently switch to a paid or remote ASR service. Report credentials, data transfer,
   and cost implications before using one.
5. Preserve Qwen engine-native output under `asr/qwen3-asr/`: `raw.json`, `aligned.json`,
   `refined.json`, and `transcript.<language>.md` (`zh-CN` for Chinese, `en` for English).
   Copy the selected Markdown to the episode root only after all four artifacts validate.
6. Run long local ASR jobs serially, one episode per subprocess. The process boundary is the
   reliable Metal/unified-memory or CUDA-VRAM cleanup boundary; do not call either worker
   `main()` repeatedly in one Python process.
7. Treat only a v2 raw as an alignable stage checkpoint. A valid v2 raw with no aligned artifact
   resumes at alignment; a valid complete pair is a no-op. A markerless legacy pair may only be
   validated and skipped read-only. If markerless raw lacks aligned output, has pending CUDA
   reconciliation, or is passed with `--realign`, fail before loading a model and require explicit
   `--retranscribe`; never backfill today's cache identity into a historical raw. Only a v2 raw may
   use align-only/`--realign`, with both pinned local model and aligner paths verified.
8. On Windows/CUDA, use 120-second nominal ownership chunks with five seconds of decode
   context on each side of every internal boundary. Reconcile overlaps only through the
   ForcedAligner's exact text-and-time crossover, retain every boundary phrase exactly once,
   and require the active-audio coverage guard to pass before raw and aligned artifacts become
   complete. An exact crossover normally belongs to a contiguous match of at least three
   characters. A unique two-character run is accepted only when both forced alignments agree
   within 250 ms for the entire run and record that stricter confidence evidence; an
   alignment-gap fallback additionally requires the whole gap to pass the recorded acoustic
   silence guard. A pending CUDA raw is a resume checkpoint, never a downstream source.

For the MLX Whisper baseline:

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/transcribe_audio.py \
  --input .cache/media/<show-id>/<episode-folder>/source.m4a \
  --output .cache/benchmarks/<show-id>/<episode-folder>/whisper/raw.json \
  --model mlx-community/whisper-large-v3-turbo-q4 \
  --language zh
```

The Whisper worker rejects non-finite values and writes strict JSON atomically. Keep every new
comparison under `.cache/benchmarks/`; do not select, promote, or commit benchmark output.
The two tracked historical baselines have been normalized from non-standard `NaN` tokens to
JSON `null` without changing text or timestamps.

For one Qwen episode on Apple Silicon/MLX with already cached local models:

```bash
env HF_HUB_OFFLINE=1 \
  UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/transcribe_qwen3_asr.py \
  --input .cache/media/<show-id>/<episode-folder>/source.m4a \
  --output shows/<show-id>/episodes/<episode-folder>/asr/qwen3-asr/raw.json \
  --aligned-output shows/<show-id>/episodes/<episode-folder>/asr/qwen3-asr/aligned.json \
  --model mlx-community/Qwen3-ASR-1.7B-8bit \
  --model-path .cache/models/qwen3-asr-1.7b-8bit-pinned-v2 \
  --aligner mlx-community/Qwen3-ForcedAligner-0.6B-8bit \
  --aligner-path .cache/models/qwen3-forced-aligner-0.6b-8bit-pinned-v2 \
  --language Chinese --no-verbose
```

For one or more Windows/CUDA episodes, use the batch entry point even for a one-item run:

```powershell
& .cache/venvs/qwen-cuda/Scripts/python.exe scripts/process_qwen3_asr_batch.py `
  --backend cuda `
  --episode shows/<show-id>/episodes/<episode-folder> `
  --model-path .cache/models/Qwen3-ASR-1.7B-hf-pinned-v3 `
  --aligner-path .cache/models/Qwen3-ForcedAligner-0.6B-hf-pinned-v3 `
  --chunk-context 5
```

Providing both local paths forces `HF_HUB_OFFLINE=1` and `TRANSFORMERS_OFFLINE=1`; the worker
must not retrieve either model from the network. CUDA defaults are `cuda:0`, `bfloat16`, SDPA,
120-second nominal ownership chunks, five seconds of context on both sides of internal
boundaries, and batch size 1. The context, exact-time ForcedAligner crossover, active-audio
coverage guard, and aligned-gap acoustic guard are part of the recorded reproducibility
contract. The worker releases the ASR model before loading the aligner. The native adapter has
mocked API and contract coverage, but has not completed the repository's Windows RTX A2000
golden-output, peak-VRAM, and long-audio qualification. Do not claim hardware proof or promote
new native CUDA transcripts until that qualification passes. Use `--dtype float16` only when
the selected CUDA device does not support bf16.

For multiple episodes, use `scripts/process_qwen3_asr_batch.py`. It discovers cached audio
or accepts repeated `--episode` paths, launches one worker subprocess at a time, writes a
per-episode log under `.cache/logs/qwen3-asr/`, continues after individual failures, renders
successful aligned artifacts, and returns non-zero after the full batch if any item failed.
Local model paths are preflighted before the first episode, and tracked JSON paths are stored
repository-relative even when discovery returns absolute filesystem paths.

The batch language options apply to every selected episode and default to Chinese. Group work
by language and always pass each intended episode explicitly with repeated `--episode` flags.
Never use cache autodiscovery in a mixed-language repository, especially with `--retranscribe`
or `--realign`. Do not rerun completed batches merely to verify them; use the repository
validator so the renderer does not create unnecessary artifact churn.

## Render and record provenance

1. Render Qwen `aligned.json` into both `refined.json` and `transcript.<language>.md` in one
   run. The renderer writes temporary files first and records the generic input-ASR SHA-256
   (raw for Whisper, aligned for Qwen) plus the rendered transcript SHA-256.
2. Remember that the batch script stops at run-directory ASR artifacts. It does not promote
   the root transcript, update front matter, translate English, write the summary, or update
   either Wiki index; complete those stages explicitly before reporting ingestion complete.
3. Pass the actual engine and model; never leave a misleading default provenance value.
4. Update the episode README with:
   - canonical source URL and verified identifiers;
   - verified participants and any optional `participants[].profile` metadata;
   - `navigation_title` and `catalog_keyword` set and validated against
     `docs/content-standard.md`;
   - local media metadata from the acquisition sidecar;
   - engine, model, options, generation timestamp, and artifact paths;
   - source/refined/rendered segment counts;
   - the exact workflow state reached.
   For `navigation_title`, use verified guests first, otherwise verified `participant`
   records, otherwise the hosts who actually appear. Never relabel a participant or host as
   a guest merely to satisfy navigation. The root `访谈人物` index column remains guest-only
   and uses `—` when the episode has no verified guest.
5. When adding `participants[].profile`, require `headline` and `checked_at: YYYY-MM-DD`.
   `bio` is optional. In `affiliations`, require `organization`, allow optional `title`, and use
   only `current` or `former` for `status`; in `education`, require `institution` and allow
   optional `credential` and `field`. Lists may be omitted or empty when facts are unavailable.
   Every profile fact must come from a source registered in the episode's `sources` or from an
   explicit guest self-statement verified against the audio or a human-checked transcript.
   Never infer profile facts from a publisher title or machine ASR. Treat `status: current` as
   current only as of `checked_at`; omit the entire profile instead of keeping placeholders or
   guessing missing facts.
6. Base an outline summary only on publisher material until the complete transcript exists.
   Do not mark summary or transcript as reviewed without the corresponding review work.
7. When selecting Qwen as the official transcript, preserve any existing Whisper raw,
   refined, and Markdown artifacts under `asr/whisper/`; never delete the previous baseline.
   Then copy the validated Qwen Markdown to the episode root and update the `transcript` and
   `asr_artifacts` metadata to point at Qwen.

## Translate selected English transcripts

When the episode language is `en`, or the selected `transcript.path` ends in `.en.md`, keep
`transcript.en.md` as the selected original and also provide a segment-aligned root
`transcript.zh-CN.md` translation.

For a long transcript, follow the ordered chunking, checkpoint, terminology, SHA-256, and
structural QA procedure in `docs/episode-processing.md`; never ask a model to rewrite the
entire file without preserving a resumable segment mapping.

1. Translate exactly one source segment into exactly one target segment. Keep the same
   level-one title, body-line count, line order, and per-line timestamps; never merge, split,
   omit, or invent segments.
2. Keep `transcript.path: transcript.en.md`. The Chinese derivative is not an ASR artifact:
   never add it to `asr/`, `asr_artifacts`, or `asr_runs`, and never use it to replace the
   selected English source.
3. Register the derivative under `transcript.translations` with this complete contract:

   ```yaml
   translations:
     - language: zh-CN
       path: transcript.zh-CN.md
       source_language: en
       source_path: transcript.en.md
       alignment: segment
       status: machine
       generated_at: "YYYY-MM-DDTHH:MM:SSZ"
       source_sha256: "<transcript.en.md SHA-256>"
       sha256: "<transcript.zh-CN.md SHA-256>"
   ```

4. Use only `machine`, `edited`, or `reviewed` for the translation status. Record the actual
   RFC 3339 generation time and exact file hashes; when the English source changes, regenerate
   or re-review the translation and update both hashes.
5. Do not complete an English episode until both Markdown files validate with identical
   titles, segment counts, and timestamp sequences.

## Keep Wiki indexes and usage docs current

1. The root `README.md` contains a `收录播客` table with columns `播客`、`简介`、`节目页`.
   Link each podcast name to its verified preferred publisher URL from show metadata, and
   link `节目页` to its local show README. Add or update this row whenever a show is added or
   its identity, source, or description changes.
2. The root `README.md` contains the canonical `单集索引` table. Its columns must remain,
   in this order: `标题`、`访谈人物`、`播客名称`、`日期`、`总结`、`逐字稿`.
   Show-level tables keep five columns in this order: `标题`、`播客名称`、`日期`、
   `总结链接`、`逐字稿链接`.
3. After every episode addition or update, update its row in both the root `README.md` and
   `shows/<show-id>/README.md`. Link the episode title to the canonical URL of its preferred
   publisher source, such as Bilibili, YouTube, or Xiaoyuzhou. In the root table only,
   populate `访谈人物`
   from front-matter participants whose role is `guest`; join multiple guests with `、` and
   never infer an unverified guest. Keep the verified episode number in `episode_number`; do
   not prefix the displayed title with `#<number>`. Link the summary and transcript columns
   directly to their local Markdown files. Completing episode work while either table is stale
   is incomplete.
4. Keep the root `README.md` focused on introducing PodWiki and navigating the podcast Wiki.
   Do not add Python command blocks or operational runbooks there.
5. Record Python script usage in `docs/python-scripts.md`. Whenever a script's CLI or the
   recommended workflow changes, update that document in the same change.

## Validate completion

1. Run the relevant unit tests.
2. Run `env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/validate.py` (PowerShell:
   after setting `$env:UV_CACHE_DIR`, run `uv run --no-sync python scripts/validate.py`).
3. Run `env UV_CACHE_DIR=.cache/uv uv run --no-sync python
   scripts/audit_correction_migration.py` to bind legacy correction recipes to selected output.
4. After the locked npm install, run `npm exec -- playwright install --with-deps chromium`,
   `npm audit --audit-level=high`, and `npm run check` from `apps/web` so the strict content
   loader, browser tests, and production
   build all consume the final repository content.
5. Run `git diff --check` and inspect `git status --short`.
6. Confirm media remains ignored and expected ASR/Markdown artifacts are trackable. For an
   English selected transcript, also confirm the required root Chinese translation and its
   `transcript.translations` hashes and segment alignment.
7. Confirm the root show table has three columns and links every podcast name to its verified
   preferred publisher page and every `节目页` to its local README. Confirm the root episode table uses
   the required six columns, the relevant show table keeps the required five columns, and both
   match the final metadata and paths.
8. Report each episode separately with its reached state, artifact paths, engine/model,
   validation result, and any remaining human review or access blocker.
