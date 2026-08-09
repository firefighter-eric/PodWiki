# Contributing to PodWiki

PodWiki treats source identity, generated-artifact lineage, and reader-facing content as one
contract. Keep a pull request narrow, preserve existing media and ASR outputs by default, and
state which checks were actually run.

## Set up the repository

Install the pinned `uv` version and Python 3.12, then prepare the common development and media
environment:

```bash
uv sync --locked --group dev --extra media
npm --prefix apps/web ci
```

Apple Silicon contributors who run MLX ASR add the mutually exclusive `asr` extra:

```bash
uv sync --locked --group dev --extra media --extra asr
```

Windows/NVIDIA contributors should keep CUDA dependencies in the ignored environment described
in [the episode runbook](docs/episode-processing.md). Never install `asr` and `asr-cuda`
together or synchronize an environment while an ASR worker is running.

## Make a change

- Read `AGENTS.md` and the relevant contract in `docs/` before editing an episode or script.
- Do not infer episode numbers, people, review status, or profile facts from file order or
  machine output.
- Keep downloads, models, logs, benchmarks, and temporary transaction files under `.cache/` or
  another ignored path.
- Preserve existing artifacts. Replacement modes require an explicit episode allowlist.
- Put auditable text corrections in that episode's `asr/corrections.json`; never add a global
  replacement rule. The renderer records the map hash, version, rule details, and hit counts.
- Pin model downloads to the documented full commit and retain Hugging Face download metadata so
  new raw, aligned, and refined artifacts can record the resolved identity and critical hashes.

## Run the same gates as CI

```bash
env UV_CACHE_DIR=.cache/uv uv lock --check
env UV_CACHE_DIR=.cache/uv uv run --no-sync ruff check scripts tests
env UV_CACHE_DIR=.cache/uv uv run --no-sync mypy \
  scripts/acquire_media.py scripts/audit_correction_migration.py scripts/asr_lineage.py \
  scripts/process_qwen3_asr_batch.py scripts/render_asr_transcript.py \
  scripts/transcribe_audio.py scripts/transcribe_qwen3_asr.py \
  scripts/transcribe_qwen3_asr_cuda.py
env UV_CACHE_DIR=.cache/uv uv run --no-sync python -m compileall -q scripts tests
env UV_CACHE_DIR=.cache/uv uv run --no-sync python -m unittest discover -s tests -v
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/validate.py
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/audit_correction_migration.py
env UV_CACHE_DIR=.cache/uv uv run --no-sync pip-audit --local --strict --progress-spinner off
npm --prefix apps/web audit --audit-level=high
npm --prefix apps/web exec -- playwright install --with-deps chromium
npm --prefix apps/web run check
git diff --check
git status --short
```

If your platform cannot run a hardware-specific gate, say so in the pull request and include the
locked resolution or CI job that covers it. Do not describe an unrun check as passing.

## Review and release

The CODEOWNERS review covers repository contracts and release gates. In the pull request,
describe compatibility with existing episodes, provide exact test evidence, and list any
remaining listening, factual, accessibility, security, or platform review. A green build does
not upgrade machine transcripts or summaries to `reviewed`.
