# ASR backend selection

## MLX Whisper

- Entry point: `scripts/transcribe_audio.py`.
- Engine value: `mlx-whisper`.
- Proven project baseline: `mlx-community/whisper-large-v3-turbo-q4`.
- Use for production processing on Apple Silicon while candidate engines remain unvalidated.
- Produces engine-native `raw.json` with timestamped segments accepted by the renderer.

## Qwen3-ASR with ForcedAligner

- Entry point: `scripts/transcribe_qwen3_asr.py`.
- Engine value: `mlx-audio`.
- Produces raw chunk output and a forced-aligned segment document.
- Treat it as a candidate until models are fully available and a representative real-audio
  end-to-end run validates alignment accounting, speed, memory use, and renderer output.
- Keep comparison artifacts under an engine-specific ASR subdirectory. Promote one to the
  episode root transcript only after an explicit quality decision.

## Backend contract

- Preserve engine-native raw output for traceability.
- Supply `segments` containing finite `start`, `end`, and non-empty `text` values to the
  deterministic refinement/rendering stage.
- Record engine, model, language, options, and generation time in the episode README and
  refined artifact.
- Do not silently fall back across engines. Local-to-remote fallback requires explicit user
  authorization because it can transfer source audio and incur cost.
