# ASR backend selection

## Qwen3-ASR on Apple Silicon / MLX

- Worker: scripts/transcribe_qwen3_asr.py.
- Batch: scripts/process_qwen3_asr_batch.py --backend mlx.
- Engine: mlx-audio.
- Models: mlx-community/Qwen3-ASR-1.7B-8bit and
  mlx-community/Qwen3-ForcedAligner-0.6B-8bit.
- Stable ignored model paths are .cache/models/qwen3-asr-1.7b-8bit-pinned-v2 and
  .cache/models/qwen3-forced-aligner-0.6b-8bit-pinned-v2.
- The WhynotTV #4 validation established project feasibility; see docs/asr-benchmark.md.

## Qwen3-ASR on Windows / NVIDIA CUDA

- Worker: scripts/transcribe_qwen3_asr_cuda.py.
- Batch: scripts/process_qwen3_asr_batch.py --backend cuda. The batch default remains mlx, so pass
  cuda explicitly.
- Engine: qwen-asr-transformers.
- Models: Qwen/Qwen3-ASR-1.7B-hf and Qwen/Qwen3-ForcedAligner-0.6B-hf.
- Stable ignored model paths are .cache/models/Qwen3-ASR-1.7B-hf-pinned-v3 and
  .cache/models/Qwen3-ForcedAligner-0.6B-hf-pinned-v3.
- Supplying both local paths forces Hugging Face and Transformers offline modes. Never omit one and
  claim a fully local run.
- Defaults are cuda:0, bfloat16, SDPA, 120-second ownership chunks, five seconds of context on each
  internal boundary, 2,048 generated tokens, and batch size 1. There is no CPU fallback. Use
  float16 only when the device does not support bf16.
- Overlap reconciliation uses ForcedAligner exact text/time crossover, active-audio coverage, and
  aligned-gap silence guards. Do not concatenate overlapping candidate text or bypass a failed seam.
- Release the ASR model before loading the aligner. The native adapter has mocked contract coverage
  but still lacks the repository's RTX A2000 golden-output, peak-VRAM, and long-audio qualification.
  Do not claim hardware proof or promote newly generated native CUDA transcripts until it passes.

## Shared Qwen recovery contract

- Preserve raw.json, aligned.json, refined.json, and transcript.<language>.md under
  asr/qwen3-asr/.
- Raw binds audio size/SHA-256. Aligned binds audio and raw SHA-256. Refined binds aligned SHA-256
  and rendered Markdown SHA-256.
- Only a v2 raw is an alignable checkpoint. A valid v2 raw without aligned output resumes at
  alignment; a matching complete chain is a no-op.
- A complete markerless legacy raw/aligned chain is read-only. Markerless partials, pending CUDA
  reconciliation, or realignment require explicit --retranscribe; never backfill today's model
  cache identity into historical output.
- Both pinned model identities are required for align-only or --realign. Old qwen-asr CUDA output
  must not be mixed with the Transformers-native aligner.
- Run multiple episodes serially, one child process per episode. Child exit is the accelerator
  resource-recovery boundary.

## MLX Whisper baseline

- Worker: scripts/transcribe_audio.py.
- Engine: mlx-whisper.
- Retained model: mlx-community/whisper-large-v3-turbo-q4.
- Preserve existing historical baselines. New comparisons require an explicit request and must stay
  under .cache/benchmarks/; never select, promote, or commit them.

## Backend invariants

- Preserve engine-native raw output.
- Record actual engine, model, aligner, language, options, generation time, and artifact hashes.
- Never silently fall back across engines. Remote or paid processing requires explicit authorization
  for data transfer, credentials, and cost.
