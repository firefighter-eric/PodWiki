---
schema_version: 1
kind: episode
id: sv101:255
show_id: sv101
episode_key: '255'
episode_number: 255
slug: 255-zhang-kuo
release_type: regular
numbering:
  status: verified
  checked_at: '2026-10-14'
  source: https://sv101.fireside.fm/269
title: 模型越来越强，为什么用户没感觉？再访阿里国际站总裁张阔【硅谷101播客】
navigation_title: 张阔 · 模型评测与商家Agent交付
catalog_keyword: Accio Work
published_at: '2026-10-09T00:00:00Z'
duration_ms: 2775765
language: zh-CN
participants:
  - id: zhangkuo
    name: 张阔
    aliases: []
    role: guest
    profile:
      headline: 阿里国际站总裁
      checked_at: '2026-10-14'
  - id: yiwen
    name: Yiwen
    aliases: []
    role: host
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV186pW6kEzU/
    preferred: true
    title: 模型越来越强，为什么用户没感觉？再访阿里国际站总裁张阔【硅谷101播客】
    identifiers:
      bvid: BV186pW6kEzU
      aid: '117407695771340'
      cid: '42579463730'
      page: 1
  - platform: website
    kind: episode
    url: https://sv101.fireside.fm/269
    preferred: false
    title: E255｜模型越来越强，为什么用户没感觉？再访阿里国际站总裁张阔
    identifiers:
      feed_url: https://feeds.fireside.fm/sv101/rss
      guid: 8fa0b58e-8359-4609-8e84-30c9a632df50
workflow:
  metadata: verified
  summary: draft
  transcript: machine
summary_basis:
  - complete-machine-transcript
summary:
  path: summary.zh-CN.md
  language: zh-CN
  source_transcript:
    path: transcript.zh-CN.md
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    selection_status: selected
    sha256: 9264e96de5f8db49a0505ac01941d22baf518406594785e09a84b504ceb65b9d
transcript:
  path: transcript.zh-CN.md
  translations: []
  acquisition_method: audio-asr
  asr_script: scripts/transcribe_qwen3_asr.py
  engine: mlx-audio
  model: mlx-community/Qwen3-ASR-1.7B-8bit
  aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
  options:
    language: Chinese
    temperature: 0.0
    max_tokens_per_chunk: 4096
    chunk_duration_seconds: 240.0
    planned_chunk_count: 12
    final_leaf_chunk_count: 12
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 49152
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: '2026-10-13T18:04:06.538973Z'
  quality:
    source_chunks: 12
    aligned_chunks: 12
    alignment_items: 15538
    sentence_segments: 375
    source_segments: 375
    refined_segments: 375
    rendered_blocks: 92
    rendered_lines: 375
  performance:
    model_load_seconds: 0.207
    transcription_seconds: 120.725
    prompt_tokens: 36302
    generation_tokens: 10042
    attempt_prompt_tokens: 36302
    attempt_generation_tokens: 10042
    generation_call_count: 12
    prompt_tokens_per_second: 300.699
    generation_tokens_per_second: 83.181
    aligner_load_seconds: 0.149
    alignment_seconds: 19.178
  access_context: anonymous
asr_runs:
  - id: qwen3-asr
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    generated_at: '2026-10-13T18:04:06.538973Z'
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/sv101/255-zhang-kuo/source.m4a
  metadata_path: .cache/media/sv101/255-zhang-kuo/source.metadata.json
  git_ignored: true
  size_bytes: 39859038
  duration_ms: 2775765
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  sha256: cd1e43df20d909e919b985a77d03a4ef0796d389cf1ba9ec9b8649287ebcd716
  verified_at: '2026-10-13T17:13:04.246872Z'
  acquired_at: '2026-10-13T17:13:04.246872Z'
last_verified_at: '2026-10-14'
asr_artifacts:
  raw:
    path: asr/qwen3-asr/raw.json
    git_ignored: false
    format: podwiki-raw-asr-json-v1
    sha256: c01a07ecd2051545fd9bc309496b54b34a50a0541e267280c0f6d2000328a616
  aligned:
    path: asr/qwen3-asr/aligned.json
    git_ignored: false
    format: podwiki-aligned-asr-json-v1
    sha256: 4dfc1dbd5e32097b09f8c2834ef65d72117ee2bd9cab5de153ae100739bccb26
  refined:
    path: asr/qwen3-asr/refined.json
    git_ignored: false
    format: podwiki-refined-asr-json-v1
    sha256: bbdb56c8d07618e5a11e461324cce37d39605e24574b01bb9c3978a35f914ce1
  transcript:
    path: asr/qwen3-asr/transcript.zh-CN.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
    sha256: 9264e96de5f8db49a0505ac01941d22baf518406594785e09a84b504ceb65b9d
  renderer: scripts/render_asr_transcript.py
---

# 模型越来越强，为什么用户没感觉？再访阿里国际站总裁张阔【硅谷101播客】

> 中文逐字稿由本地 Qwen3-ASR 与 ForcedAligner 生成，保持 machine 状态。

## 单集信息

- 来源：[BV186pW6kEzU](https://www.bilibili.com/video/BV186pW6kEzU/)

## 内容概览

已完成本地机器逐字稿；完整内容总结依据当前所选中文稿。

## 完整逐字稿

- [查看中文逐字稿](./transcript.zh-CN.md)

## 完整总结

- [查看中文总结](./summary.zh-CN.md)
