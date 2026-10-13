---
schema_version: 1
kind: episode
id: sv101:241
show_id: sv101
episode_key: '241'
episode_number: 241
slug: 241-gai-de
release_type: regular
numbering:
  status: verified
  checked_at: '2026-10-14'
  source: https://sv101.fireside.fm/254
title: 跑鞋技术迭代史：马拉松跑进2小时，靠人还是靠鞋？【硅谷101播客】
navigation_title: 盖德 · 跑鞋技术与品牌竞争
catalog_keyword: 跑鞋
published_at: '2026-06-26T00:00:00Z'
duration_ms: 3658048
language: zh-CN
participants:
  - id: gaide
    name: 盖德
    aliases: []
    role: guest
    profile:
      headline: 《迪谈盖论》主播
      checked_at: '2026-10-14'
  - id: mahua
    name: 麻花
    aliases: []
    role: host
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1ga7a6pEvq/
    preferred: true
    title: 跑鞋技术迭代史：马拉松跑进2小时，靠人还是靠鞋？【硅谷101播客】
    identifiers:
      bvid: BV1ga7a6pEvq
      aid: '116811265744667'
      cid: '39403654766'
      page: 1
  - platform: website
    kind: episode
    url: https://sv101.fireside.fm/254
    preferred: false
    title: E241｜跑鞋技术迭代史：马拉松跑进2小时，靠人还是靠鞋？
    identifiers:
      feed_url: https://feeds.fireside.fm/sv101/rss
      guid: c38d5df5-2eb3-46d3-8437-892593599d29
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
    sha256: 04ff8b550d554a26ee38dffe0d78ba00878679ef4bc555762bcc38993d9ae893
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
    planned_chunk_count: 16
    final_leaf_chunk_count: 16
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 65536
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: '2026-10-13T17:43:10.917045Z'
  quality:
    source_chunks: 16
    aligned_chunks: 16
    alignment_items: 20314
    sentence_segments: 500
    source_segments: 500
    refined_segments: 500
    rendered_blocks: 122
    rendered_lines: 500
  performance:
    model_load_seconds: 0.185
    transcription_seconds: 168.683
    prompt_tokens: 47844
    generation_tokens: 13962
    attempt_prompt_tokens: 47844
    attempt_generation_tokens: 13962
    generation_call_count: 16
    prompt_tokens_per_second: 283.633
    generation_tokens_per_second: 82.771
    aligner_load_seconds: 0.135
    alignment_seconds: 25.029
  access_context: anonymous
asr_runs:
  - id: qwen3-asr
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    generated_at: '2026-10-13T17:43:10.917045Z'
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/sv101/241-gai-de/source.m4a
  metadata_path: .cache/media/sv101/241-gai-de/source.metadata.json
  git_ignored: true
  size_bytes: 53788249
  duration_ms: 3658048
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  sha256: 2a3c88af17f4abf67612edb1359d64994df3b0608630a2f74bbd8aab4a40aacb
  verified_at: '2026-10-13T17:13:56.869685Z'
  acquired_at: '2026-10-13T17:13:56.869685Z'
last_verified_at: '2026-10-14'
asr_artifacts:
  raw:
    path: asr/qwen3-asr/raw.json
    git_ignored: false
    format: podwiki-raw-asr-json-v1
    sha256: 5edc7209ede805d1cec5a1fe4da2e999e375195fce1b75b319f8d070e5841fff
  aligned:
    path: asr/qwen3-asr/aligned.json
    git_ignored: false
    format: podwiki-aligned-asr-json-v1
    sha256: 016ffb7cad9e5d4d9f5fb89c5cf1df5455671a9bbe56c192052c5a72dcfa57ce
  refined:
    path: asr/qwen3-asr/refined.json
    git_ignored: false
    format: podwiki-refined-asr-json-v1
    sha256: c85c4d7aac810327c8b464953875466c6614005c7afc8ff3c85e5c15b1d443ee
  transcript:
    path: asr/qwen3-asr/transcript.zh-CN.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
    sha256: 04ff8b550d554a26ee38dffe0d78ba00878679ef4bc555762bcc38993d9ae893
  renderer: scripts/render_asr_transcript.py
---

# 跑鞋技术迭代史：马拉松跑进2小时，靠人还是靠鞋？【硅谷101播客】

> 中文逐字稿由本地 Qwen3-ASR 与 ForcedAligner 生成，保持 machine 状态。

## 单集信息

- 来源：[BV1ga7a6pEvq](https://www.bilibili.com/video/BV1ga7a6pEvq/)

## 内容概览

已完成本地机器逐字稿；完整内容总结依据当前所选中文稿。

## 完整逐字稿

- [查看中文逐字稿](./transcript.zh-CN.md)

## 完整总结

- [查看中文总结](./summary.zh-CN.md)
