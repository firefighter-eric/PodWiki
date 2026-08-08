# ASR backend selection

## Qwen3-ASR with ForcedAligner

### Apple Silicon / MLX

- Worker entry point: `scripts/transcribe_qwen3_asr.py`; batch selection:
  `scripts/process_qwen3_asr_batch.py --backend mlx`.
- Engine value: `mlx-audio`.
- Selected models: `mlx-community/Qwen3-ASR-1.7B-8bit` and
  `mlx-community/Qwen3-ForcedAligner-0.6B-8bit`.
- The full WhynotTV #4 validation established alignment accounting, timestamp monotonicity,
  speed, memory feasibility, and renderer compatibility. See `docs/asr-benchmark.md`.

### Windows / NVIDIA CUDA

- Worker entry point: `scripts/transcribe_qwen3_asr_cuda.py`; batch selection:
  `scripts/process_qwen3_asr_batch.py --backend cuda`.
- The batch default remains `mlx`, so Windows runs must pass `--backend cuda` explicitly.
- Engine value: `qwen-asr-transformers`.
- Canonical official models: `Qwen/Qwen3-ASR-1.7B` and
  `Qwen/Qwen3-ForcedAligner-0.6B`. Keep these Hub IDs in tracked provenance even when local
  paths are used.
- The `asr-cuda` dependency group locks `qwen-asr==0.0.6` and the CUDA 12.8 build of
  PyTorch 2.11.0 on Windows AMD64; the worker rejects incompatible runtime versions.
- Stable ignored paths are `.cache/models/Qwen3-ASR-1.7B` and
  `.cache/models/Qwen3-ForcedAligner-0.6B`. Supplying both `--model-path` and
  `--aligner-path` forces both Hugging Face and Transformers offline modes; do not omit one
  path and claim a fully local run.
- Defaults are `cuda:0`, `bfloat16`, SDPA, 120-second ownership chunks, 5 seconds of
  acoustic context on each side, 2,048 generated tokens per chunk, and inference batch
  size 1. There is no CPU fallback. Use `--dtype float16` only when the selected CUDA
  device does not support bf16.
- CUDA chunk candidates overlap, but the canonical transcript never concatenates those
  candidates directly. ForcedAligner items are matched exactly under a one-second time
  gate; an anchor normally belongs to a contiguous match of at least three normalized
  characters. The only shorter fallback is one globally unique adjacent two-character match
  whose two alignment pairs both agree within 250 ms and whose confidence is recorded.
  One crossover owns each seam, and only the owned item slices reach canonical raw, aligned,
  refined, and Markdown artifacts. An aligned-gap fallback is accepted only when its entire
  gap passes the recorded acoustic silence guard; every other uncertain seam fails closed.
- The CUDA worker also rejects sparse or prematurely ended alignment when the uncovered
  region contains sustained active audio. This prevents a short decode from being accepted
  as a complete long chunk.
- Short final remainders are redistributed across the final two ownership chunks instead of
  creating a tiny outro chunk whose boundary cannot be reconciled reliably.
- The local RTX A2000 8GB Laptop GPU has been smoke-tested successfully with the official
  1.7B model and 0.6B aligner. The worker runs them in sequence and releases the ASR model
  before loading the aligner so both are never resident together.

### Shared Qwen artifact and recovery contract

- Produces raw chunk output and a forced-aligned sentence document under `asr/qwen3-asr/`.
- Raw stores the source audio size and SHA-256. Aligned stores the audio SHA-256, raw JSON
  SHA-256, and sentence-splitting options so resumability fails closed on identity drift.
- Refined stores the exact input-ASR SHA-256 (aligned for Qwen) and rendered Markdown
  SHA-256, so the readable transcript can be checked against its structured lineage.
- A CUDA raw overlap checkpoint records full candidate text plus non-overlapping ownership
  ranges. Its reconciliation status is `pending` until forced alignment has selected the
  owned slices; only `complete` raw may be referenced by aligned output. Existing valid raw
  resumes at alignment/reconciliation; existing valid complete raw and aligned artifacts
  are a no-op. Replacement requires `--retranscribe` or `--realign`.
- Use local model paths for workers while retaining canonical Hub IDs in tracked metadata.

## MLX Whisper

- Entry point: `scripts/transcribe_audio.py`.
- Engine value: `mlx-whisper`.
- Proven project baseline: `mlx-community/whisper-large-v3-turbo-q4`.
- Retain existing historical baselines. When explicitly requested for a new comparison, write
  it under `.cache/benchmarks/`; the current worker can emit non-strict JSON `NaN` values, so
  do not select, promote, or commit new output until that contract is fixed.
- Produces engine-native `raw.json` with timestamped segments accepted by the renderer.

## Backend contract

- Preserve engine-native raw output for traceability.
- Supply `segments` containing finite `start`, `end`, and non-empty `text` values to the
  deterministic refinement/rendering stage.
- Record engine, model, language, options, and generation time in the episode README and
  refined artifact.
- Execute a multi-episode batch serially with one worker subprocess per episode. A child
  process exit is the reliable Metal/unified-memory or CUDA-VRAM cleanup boundary.
- Do not silently fall back across engines. Local-to-remote fallback requires explicit user
  authorization because it can transfer source audio and incur cost.
