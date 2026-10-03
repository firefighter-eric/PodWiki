---
schema_version: 1
kind: episode
id: sv101:252
show_id: sv101
episode_key: '252'
episode_number: 252
slug: 252-eight-sleep
release_type: regular
numbering:
  status: verified
  checked_at: '2026-10-02'
  source: https://sv101.fireside.fm/266
title: 硅谷睡眠外挂：富人的玩具，还是预防医疗的入口？｜对话Eight Sleep创始人【硅谷101视频播客】
navigation_title: Matteo Franceschetti、Alex Zatarain · 睡眠科技与硬件创业
catalog_keyword: 睡眠科技
published_at: '2026-09-24T08:00:00+08:00'
duration_ms: 2695445
language: en
participants:
  - id: matteo-franceschetti
    name: Matteo Franceschetti
    aliases: []
    role: guest
  - id: alex-zatarain
    name: Alex Zatarain
    aliases: []
    role: guest
  - id: yiwen
    name: Yiwen
    aliases: []
    role: host
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1Chhb6YENK/
    title: 硅谷睡眠外挂：富人的玩具，还是预防医疗的入口？｜对话Eight Sleep创始人【硅谷101视频播客】
    preferred: true
    identifiers:
      bvid: BV1Chhb6YENK
      aid: '117321226065579'
      cid: '42143387389'
      page: 1
  - platform: website
    kind: episode
    url: https://sv101.fireside.fm/266
    preferred: false
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
    path: transcript.en.md
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    selection_status: selected
    sha256: 73c845462c59db0549285076ed177a9bd72aceecc87ff9d8617f6ac90fb2cddc
transcript:
  path: transcript.en.md
  acquisition_method: audio-asr
  asr_script: scripts/transcribe_qwen3_asr.py
  engine: mlx-audio
  model: mlx-community/Qwen3-ASR-1.7B-8bit
  aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
  options:
    language: English
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
  generated_at: '2026-10-02T15:19:23.538910Z'
  access_context: anonymous
  quality:
    source_chunks: 12
    aligned_chunks: 12
    alignment_items: 10512
    sentence_segments: 574
    source_segments: 574
    refined_segments: 574
    rendered_blocks: 225
    rendered_lines: 574
  performance:
    model_load_seconds: 0.212
    transcription_seconds: 138.403
    prompt_tokens: 35258
    generation_tokens: 10968
    attempt_prompt_tokens: 35258
    attempt_generation_tokens: 10968
    generation_call_count: 12
    prompt_tokens_per_second: 254.748
    generation_tokens_per_second: 79.247
    aligner_load_seconds: 0.294
    alignment_seconds: 17.344
  translations:
    - language: zh-CN
      path: transcript.zh-CN.md
      source_language: en
      source_path: transcript.en.md
      alignment: segment
      status: machine
      generated_at: '2026-10-02T15:51:04.769948Z'
      source_sha256: 73c845462c59db0549285076ed177a9bd72aceecc87ff9d8617f6ac90fb2cddc
      sha256: a113233beac06a2db9ca6128f3ffff0257a2e51514527438cbf189fa4aca2b1b
asr_artifacts:
  raw:
    path: asr/qwen3-asr/raw.json
    git_ignored: false
    format: podwiki-raw-asr-json-v1
  aligned:
    path: asr/qwen3-asr/aligned.json
    git_ignored: false
    format: podwiki-aligned-asr-json-v1
  refined:
    path: asr/qwen3-asr/refined.json
    git_ignored: false
    format: podwiki-refined-asr-json-v1
  transcript:
    path: asr/qwen3-asr/transcript.en.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
  renderer: scripts/render_asr_transcript.py
asr_runs:
  - id: qwen3-asr
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    generated_at: '2026-10-02T15:19:23.538910Z'
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.en.md
local_audio_cache:
  path: .cache/media/sv101/252-eight-sleep/source.m4a
  metadata_path: .cache/media/sv101/252-eight-sleep/source.metadata.json
  git_ignored: true
  size_bytes: 42095060
  duration_ms: 2695445
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  sha256: cdd7c28fdc2121264947b23e023c08d0c1287c4b9b10f6c336490f1fcd2ac8d9
  verified_at: '2026-10-02T15:01:12.892597Z'
  acquired_at: '2026-10-02T15:01:12.892597Z'
last_verified_at: '2026-10-02'
---

# 硅谷睡眠外挂：富人的玩具，还是预防医疗的入口？｜对话Eight Sleep创始人【硅谷101视频播客】

> 正式稿由本地固定版本 Qwen3-ASR 与 ForcedAligner 生成，为 `machine`；逐段中文译稿来自本地固定版本 Qwen3.6，为 `machine`；总结依据完整所选原文，为 `draft`，待人工审核。主体为英文访谈，保留中文导语与尾声；译稿中的原有中文段落保持原样。

## 单集信息

- 总结：[查看总结](./summary.zh-CN.md)
- 正式逐字稿：[查看英文逐字稿](./transcript.en.md)
- 中文译稿：[查看逐段中文译稿](./transcript.zh-CN.md)
- 翻译来源：[固定模型与逐段载荷](./translation.zh-CN.json)
- 原始节目：[发布者完整单集](https://www.bilibili.com/video/BV1Chhb6YENK/)

## 待审核

- 回听核对人名、数字、否定词、说话人归属与时间戳。
- 核对总结的观点归属、论据与限制条件。
- 逐段核对机器译稿中的术语、跨字幕句子、语气与省略。
