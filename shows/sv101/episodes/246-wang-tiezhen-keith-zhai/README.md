---
schema_version: 1
kind: episode
id: sv101:246
show_id: sv101
episode_key: '246'
episode_number: 246
slug: 246-wang-tiezhen-keith-zhai
release_type: regular
numbering:
  status: verified
  checked_at: '2026-10-14'
  source: https://sv101.fireside.fm/259
title: 何谓蒸馏？聊聊硅谷如何看中国开放模型逼近前沿【硅谷101播客】
navigation_title: 王铁震、Keith Zhai · 蒸馏与开放模型
catalog_keyword: 蒸馏
published_at: '2026-08-01T00:00:00Z'
duration_ms: 4055979
language: zh-CN
participants:
  - id: yiwen
    name: Yiwen
    aliases: []
    role: host
  - id: wangtiezhen
    name: 王铁震
    aliases: []
    role: guest
  - id: keithzhai
    name: Keith Zhai
    aliases: []
    role: guest
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1AoGN6XESP/
    preferred: true
    title: 何谓蒸馏？聊聊硅谷如何看中国开放模型逼近前沿【硅谷101播客】
    identifiers:
      bvid: BV1AoGN6XESP
      aid: '117015914222979'
      cid: '40483227727'
      page: 1
  - platform: website
    kind: episode
    url: https://sv101.fireside.fm/259
    preferred: false
    title: E246｜何谓蒸馏？聊聊硅谷如何看中国开放模型逼近前沿
    identifiers:
      feed_url: https://feeds.fireside.fm/sv101/rss
      guid: 5fd236d7-9a72-4b15-9e84-e83ceadd1b41
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
    sha256: 473f8aa8ad529b212a5a33715b08bcfd91ca91887214775f40437a305692bbe4
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
    planned_chunk_count: 17
    final_leaf_chunk_count: 17
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 69632
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: '2026-10-13T17:50:46.438856Z'
  quality:
    source_chunks: 17
    aligned_chunks: 17
    alignment_items: 22419
    sentence_segments: 574
    source_segments: 574
    refined_segments: 574
    rendered_blocks: 135
    rendered_lines: 574
  performance:
    model_load_seconds: 0.183
    transcription_seconds: 179.094
    prompt_tokens: 53037
    generation_tokens: 14689
    attempt_prompt_tokens: 53037
    attempt_generation_tokens: 14689
    generation_call_count: 17
    prompt_tokens_per_second: 296.141
    generation_tokens_per_second: 82.019
    aligner_load_seconds: 0.304
    alignment_seconds: 28.163
  access_context: anonymous
asr_runs:
  - id: qwen3-asr
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    generated_at: '2026-10-13T17:50:46.438856Z'
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/sv101/246-wang-tiezhen-keith-zhai/source.m4a
  metadata_path: .cache/media/sv101/246-wang-tiezhen-keith-zhai/source.metadata.json
  git_ignored: true
  size_bytes: 57075716
  duration_ms: 4055979
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  sha256: 4076f98b19cf66c699c60b6c414dadf8e1660674a78c336ade5507f395e377cb
  verified_at: '2026-10-13T17:14:09.645828Z'
  acquired_at: '2026-10-13T17:14:09.645828Z'
last_verified_at: '2026-10-14'
asr_artifacts:
  raw:
    path: asr/qwen3-asr/raw.json
    git_ignored: false
    format: podwiki-raw-asr-json-v1
    sha256: 614a84b141e457c0821acc313d5ee6a65edb242534df5036d6aaabcd4bfab182
  aligned:
    path: asr/qwen3-asr/aligned.json
    git_ignored: false
    format: podwiki-aligned-asr-json-v1
    sha256: 28f0caf90146d34e7efcd1c0dfd82f5a414045d30599ec55dcc912e09a820d62
  refined:
    path: asr/qwen3-asr/refined.json
    git_ignored: false
    format: podwiki-refined-asr-json-v1
    sha256: 07e9c78ac56cc548575bf2ed4952c0ef4ece3bc82bdb7806b31bb223042aeef1
  transcript:
    path: asr/qwen3-asr/transcript.zh-CN.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
    sha256: 473f8aa8ad529b212a5a33715b08bcfd91ca91887214775f40437a305692bbe4
  renderer: scripts/render_asr_transcript.py
---

# 何谓蒸馏？聊聊硅谷如何看中国开放模型逼近前沿【硅谷101播客】

> 中文逐字稿由本地 Qwen3-ASR 与 ForcedAligner 生成，保持 machine 状态。

## 单集信息

- 来源：[BV1AoGN6XESP](https://www.bilibili.com/video/BV1AoGN6XESP/)

## 内容概览

已完成本地机器逐字稿；完整内容总结依据当前所选中文稿。

## 完整逐字稿

- [查看中文逐字稿](./transcript.zh-CN.md)

## 完整总结

- [查看中文总结](./summary.zh-CN.md)
