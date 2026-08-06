---
name: podwiki-process-episode
description: Process PodWiki podcast episodes from Bilibili, YouTube, or local media. Use when adding, downloading, resuming, retranscribing, regenerating, or validating an episode through source acquisition, ASR, transcript rendering, metadata updates, and repository checks.
---

# Process a PodWiki episode

Move one or more episodes through the requested machine-processing stages while
preserving source provenance, resumability, and the repository content standard.

## Establish scope

1. Read `docs/content-standard.md` and the relevant templates before editing.
2. Inspect the existing show, episode directory, cache, ASR artifacts, and Git changes.
3. Infer the requested stopping point:
   - Download or acquire: stop after verified local media and metadata.
   - Transcribe or retranscribe: stop after raw ASR unless rendering is also requested.
   - Process, add, or ingest: continue through rendered machine transcript and validation.
4. Never treat list order as an official episode number. Use a verified publisher number;
   otherwise use the documented source-ID key (for example, a lower-cased BVID key for
   Bilibili).
5. Preserve existing artifacts. Reuse only when identity metadata and hashes match; require
   an explicit overwrite request to replace an existing source or raw ASR result.

## Process sources

1. Canonicalize the supplied URL and remove tracking parameters.
2. Read `references/bilibili.md` for Bilibili or `references/youtube.md` for YouTube.
3. Check for a public subtitle track before downloading media.
4. Do not bypass login, membership, payment, region, or other access controls. Do not use
   browser cookies unless the user explicitly authorizes that source and access method.
5. Acquire only one video, never an account or playlist, with:

   ```bash
   env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/acquire_media.py \
     --url <canonical-url> \
     --output .cache/media/<show-id>/<episode-folder>/source.m4a
   ```

6. Require the sidecar `source.metadata.json` and verify codec, duration, size, sample rate,
   channels, and SHA-256 before marking the source acquired.
7. Keep downloaded media and temporary files under `.cache/`; never add them to Git.

## Select and run ASR

Read `references/asr-backends.md` before choosing an engine.

Before starting workers, run `uv sync --all-groups` once. Every worker must then use
`env UV_CACHE_DIR=.cache/uv uv run --no-sync` so dependency groups do not mutate the
shared `.venv`. Before any `hf download`, export the configured mirror:

```bash
export HF_ENDPOINT=https://hf-mirror.com
```

For a cold local cache, download only after that export and use stable ignored paths:

```bash
hf download mlx-community/Qwen3-ASR-1.7B-8bit \
  --local-dir .cache/models/qwen3-asr-1.7b-8bit
hf download mlx-community/Qwen3-ForcedAligner-0.6B-8bit \
  --local-dir .cache/models/qwen3-forced-aligner-0.6b-8bit
```

1. Use an explicitly requested engine and model when compatible.
2. Otherwise reuse the episode's recorded engine and model for reproducibility.
3. For Chinese episodes on Apple Silicon, use the project-selected Qwen3-ASR 1.7B 8-bit
   model with Qwen3 ForcedAligner. Keep MLX Whisper only as a retained baseline when it
   already exists or when the user explicitly requests it.
4. Never silently switch to a paid or remote ASR service. Report credentials, data transfer,
   and cost implications before using one.
5. Preserve Qwen engine-native output under `asr/qwen3-asr/`: `raw.json`, `aligned.json`,
   `refined.json`, and `transcript.zh-CN.md`. Copy the selected Markdown to the episode root
   only after all four artifacts validate.
6. Run long local ASR jobs serially, one episode per subprocess. The process boundary is the
   reliable Metal/unified-memory cleanup boundary; do not call the worker `main()` repeatedly
   in one Python process.
7. Treat raw as the stage checkpoint. A valid raw with no aligned artifact resumes at
   alignment; two valid artifacts are a no-op. Existing invalid or mismatched artifacts fail
   closed. Only `--retranscribe` or `--realign` may replace a corresponding artifact.

For the MLX Whisper baseline:

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/transcribe_audio.py \
  --input .cache/media/<show-id>/<episode-folder>/source.m4a \
  --output shows/<show-id>/episodes/<episode-folder>/asr/whisper/raw.json \
  --model mlx-community/whisper-large-v3-turbo-q4 \
  --language zh
```

For one Qwen episode with already cached local models:

```bash
env HF_ENDPOINT=https://hf-mirror.com HF_HUB_OFFLINE=1 \
  UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/transcribe_qwen3_asr.py \
  --input .cache/media/<show-id>/<episode-folder>/source.m4a \
  --output shows/<show-id>/episodes/<episode-folder>/asr/qwen3-asr/raw.json \
  --aligned-output shows/<show-id>/episodes/<episode-folder>/asr/qwen3-asr/aligned.json \
  --model mlx-community/Qwen3-ASR-1.7B-8bit \
  --model-path .cache/models/qwen3-asr-1.7b-8bit \
  --aligner mlx-community/Qwen3-ForcedAligner-0.6B-8bit \
  --aligner-path .cache/models/qwen3-forced-aligner-0.6b-8bit \
  --language Chinese --no-verbose
```

For multiple episodes, use `scripts/process_qwen3_asr_batch.py`. It discovers cached audio
or accepts repeated `--episode` paths, launches one worker subprocess at a time, writes a
per-episode log under `.cache/logs/qwen3-asr/`, continues after individual failures, renders
successful aligned artifacts, and returns non-zero after the full batch if any item failed.
Local model paths are preflighted before the first episode, and tracked JSON paths are stored
repository-relative even when discovery returns absolute filesystem paths.

## Render and record provenance

1. Render Qwen `aligned.json` into both `refined.json` and `transcript.<language>.md` in one
   run. The renderer writes temporary files first and records the generic input-ASR SHA-256
   (raw for Whisper, aligned for Qwen) plus the rendered transcript SHA-256.
2. Pass the actual engine and model; never leave a misleading default provenance value.
3. Update the episode README with:
   - canonical source URL and verified identifiers;
   - local media metadata from the acquisition sidecar;
   - engine, model, options, generation timestamp, and artifact paths;
   - source/refined/rendered segment counts;
   - the exact workflow state reached.
4. Base an outline summary only on publisher material until the complete transcript exists.
   Do not mark summary or transcript as reviewed without the corresponding review work.
5. When selecting Qwen as the official transcript, preserve any existing Whisper raw,
   refined, and Markdown artifacts under `asr/whisper/`; never delete the previous baseline.
   Then copy the validated Qwen Markdown to the episode root and update the `transcript` and
   `asr_artifacts` metadata to point at Qwen.

## Keep Wiki indexes and usage docs current

1. The root `README.md` contains a `收录播客` table with columns `播客`、`简介`、`节目页`.
   Link each podcast name to the verified Bilibili channel/space URL from show metadata, and
   link `节目页` to its local show README. Add or update this row whenever a show is added or
   its identity, source, or description changes.
2. The root `README.md` contains the canonical `单集索引` table. Its columns must remain,
   in this order: `标题`、`访谈人物`、`播客名称`、`日期`、`总结`、`逐字稿`.
   Show-level tables keep five columns in this order: `标题`、`播客名称`、`日期`、
   `总结链接`、`逐字稿链接`.
3. After every episode addition or update, update its row in both the root `README.md` and
   `shows/<show-id>/README.md`. Link the episode title to the canonical URL of its preferred
   publisher source, such as Bilibili or YouTube. In the root table only, populate `访谈人物`
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
2. Run `env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/validate.py`.
3. Run `git diff --check` and inspect `git status --short`.
4. Confirm media remains ignored and expected ASR/Markdown artifacts are trackable.
5. Confirm the root show table has three columns and links every podcast name to its verified
   Bilibili space and every `节目页` to its local README. Confirm the root episode table uses
   the required six columns, the relevant show table keeps the required five columns, and both
   match the final metadata and paths.
6. Report each episode separately with its reached state, artifact paths, engine/model,
   validation result, and any remaining human review or access blocker.
