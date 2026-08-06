# ASR backend selection

## MLX Whisper

- Entry point: `scripts/transcribe_audio.py`.
- Engine value: `mlx-whisper`.
- Proven project baseline: `mlx-community/whisper-large-v3-turbo-q4`.
- Retain as a fast baseline or use when explicitly requested.
- Produces engine-native `raw.json` with timestamped segments accepted by the renderer.

## Qwen3-ASR with ForcedAligner

- Entry point: `scripts/transcribe_qwen3_asr.py`.
- Engine value: `mlx-audio`.
- Selected Chinese transcription backend: `mlx-community/Qwen3-ASR-1.7B-8bit` with
  `mlx-community/Qwen3-ForcedAligner-0.6B-8bit`.
- Produces raw chunk output and a forced-aligned sentence document under `asr/qwen3-asr/`.
- The full WhynotTV #4 validation established alignment accounting, timestamp monotonicity,
  speed, memory feasibility, and renderer compatibility. See `docs/asr-benchmark.md`.
- Raw stores the source audio size and SHA-256. Aligned stores the audio SHA-256, raw JSON
  SHA-256, and sentence-splitting options so resumability fails closed on identity drift.
- Refined stores the exact input-ASR SHA-256 (aligned for Qwen) and rendered Markdown
  SHA-256, so the readable transcript can be checked against its structured lineage.
- Existing valid raw resumes at alignment; existing valid raw and aligned artifacts are a
  no-op. Replacement requires `--retranscribe` or `--realign`.
- Use local model paths for workers while retaining canonical Hub IDs in tracked metadata.

## Backend contract

- Preserve engine-native raw output for traceability.
- Supply `segments` containing finite `start`, `end`, and non-empty `text` values to the
  deterministic refinement/rendering stage.
- Record engine, model, language, options, and generation time in the episode README and
  refined artifact.
- Execute a multi-episode batch serially with one worker subprocess per episode. A child
  process exit is the reliable Metal and unified-memory cleanup boundary.
- Do not silently fall back across engines. Local-to-remote fallback requires explicit user
  authorization because it can transfer source audio and incur cost.
