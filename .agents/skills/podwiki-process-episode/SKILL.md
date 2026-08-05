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

Before starting parallel workers, run `uv sync --all-groups` once. Every worker must then
use `env UV_CACHE_DIR=.cache/uv uv run --no-sync` so concurrent dependency groups do not
mutate the shared `.venv`.

1. Use an explicitly requested engine and model when compatible.
2. Otherwise reuse the episode's recorded engine and model for reproducibility.
3. For a new Chinese episode on Apple Silicon, prefer the project-proven MLX Whisper
   baseline until another backend has passed an end-to-end real-audio validation.
4. Never silently switch to a paid or remote ASR service. Report credentials, data transfer,
   and cost implications before using one.
5. Preserve engine-native output as `asr/raw.json`. For Qwen3-ASR, also preserve
   `asr/qwen3-asr/aligned.json`; do not call a candidate transcript the official transcript.
6. Run only as many local model workers as unified memory can safely support. Parallelize
   metadata and downloads, but serialize or limit long ASR jobs when memory pressure rises.

For the MLX Whisper baseline:

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/transcribe_audio.py \
  --input .cache/media/<show-id>/<episode-folder>/source.m4a \
  --output shows/<show-id>/episodes/<episode-folder>/asr/raw.json \
  --model mlx-community/whisper-large-v3-turbo-q4 \
  --language zh
```

## Render and record provenance

1. Render `raw.json` into both `refined.json` and `transcript.<language>.md` in one run.
2. Pass the actual engine and model; never leave a misleading default provenance value.
3. Update the episode README with:
   - canonical source URL and verified identifiers;
   - local media metadata from the acquisition sidecar;
   - engine, model, options, generation timestamp, and artifact paths;
   - source/refined/rendered segment counts;
   - the exact workflow state reached.
4. Base an outline summary only on publisher material until the complete transcript exists.
   Do not mark summary or transcript as reviewed without the corresponding review work.

## Validate completion

1. Run the relevant unit tests.
2. Run `env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/validate.py`.
3. Run `git diff --check` and inspect `git status --short`.
4. Confirm media remains ignored and expected ASR/Markdown artifacts are tracked candidates.
5. Report each episode separately with its reached state, artifact paths, engine/model,
   validation result, and any remaining human review or access blocker.
