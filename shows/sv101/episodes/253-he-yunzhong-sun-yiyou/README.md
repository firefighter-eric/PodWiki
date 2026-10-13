---
schema_version: 1
kind: episode
id: sv101:253
show_id: sv101
episode_key: '253'
episode_number: 253
slug: 253-he-yunzhong-sun-yiyou
release_type: regular
numbering:
  status: verified
  checked_at: '2026-10-14'
  source: https://sv101.fireside.fm/267
title: 谁在给大模型出题、卖题、判卷？聊聊AI数据行业的野蛮生长【硅谷101播客】
navigation_title: 何允中、孙一铀 · AI数据行业与模型评测
catalog_keyword: AI数据
published_at: '2026-09-28T02:30:00Z'
duration_ms: 3480469
language: zh-CN
participants:
  - id: yiwen
    name: Yiwen
    aliases: []
    role: host
  - id: heyunzhong
    name: 何允中
    aliases: []
    role: guest
  - id: sunyiyou
    name: 孙一铀
    aliases: []
    role: guest
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1imaq6mEof/
    preferred: true
    title: 谁在给大模型出题、卖题、判卷？聊聊AI数据行业的野蛮生长【硅谷101播客】
    identifiers:
      bvid: BV1imaq6mEof
      aid: '117346106675376'
      cid: '42261414770'
      page: 1
  - platform: website
    kind: episode
    url: https://sv101.fireside.fm/267
    preferred: false
    title: E253｜谁在给大模型出题、卖题、判卷？聊聊AI数据行业的野蛮生长
    identifiers:
      feed_url: https://feeds.fireside.fm/sv101/rss
      guid: 0a1dd0c4-a1f7-4f7c-b334-bd807ca72a5d
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
    sha256: 3606f18fcf16c98a6386ddfd2ac25557b4a85b2872ebb213a1804342b61060c6
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
    planned_chunk_count: 15
    final_leaf_chunk_count: 15
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 61440
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: '2026-10-13T17:58:42.896220Z'
  quality:
    source_chunks: 15
    aligned_chunks: 15
    alignment_items: 20097
    sentence_segments: 496
    source_segments: 496
    refined_segments: 496
    rendered_blocks: 121
    rendered_lines: 496
  performance:
    model_load_seconds: 0.183
    transcription_seconds: 158.136
    prompt_tokens: 45520
    generation_tokens: 13079
    attempt_prompt_tokens: 45520
    attempt_generation_tokens: 13079
    generation_call_count: 15
    prompt_tokens_per_second: 287.854
    generation_tokens_per_second: 82.707
    aligner_load_seconds: 0.316
    alignment_seconds: 24.671
  access_context: anonymous
asr_runs:
  - id: qwen3-asr
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    generated_at: '2026-10-13T17:58:42.896220Z'
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/sv101/253-he-yunzhong-sun-yiyou/source.m4a
  metadata_path: .cache/media/sv101/253-he-yunzhong-sun-yiyou/source.metadata.json
  git_ignored: true
  size_bytes: 56874740
  duration_ms: 3480469
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  sha256: e5778a6112f72734a7003f5098dc08f3ce2eb4c8cc00e4a94fa98c57c92c91f6
  verified_at: '2026-10-13T17:14:02.007726Z'
  acquired_at: '2026-10-13T17:14:02.007726Z'
last_verified_at: '2026-10-14'
asr_artifacts:
  raw:
    path: asr/qwen3-asr/raw.json
    git_ignored: false
    format: podwiki-raw-asr-json-v1
    sha256: ada8afc3233e594d360e600f7c23006a72922b52e821332815f685d7349ace0c
  aligned:
    path: asr/qwen3-asr/aligned.json
    git_ignored: false
    format: podwiki-aligned-asr-json-v1
    sha256: d6695c9dbbabe4dfc93975afcd7215f3b50e74836bebb1901533843f790539aa
  refined:
    path: asr/qwen3-asr/refined.json
    git_ignored: false
    format: podwiki-refined-asr-json-v1
    sha256: f3c115671abfe75624c0222c857da29250e586e2f0026d1f718441ed945669e7
  transcript:
    path: asr/qwen3-asr/transcript.zh-CN.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
    sha256: 3606f18fcf16c98a6386ddfd2ac25557b4a85b2872ebb213a1804342b61060c6
  renderer: scripts/render_asr_transcript.py
---

# 谁在给大模型出题、卖题、判卷？聊聊AI数据行业的野蛮生长【硅谷101播客】

> 中文逐字稿由本地 Qwen3-ASR 与 ForcedAligner 生成，保持 machine 状态。

## 单集信息

- 来源：[BV1imaq6mEof](https://www.bilibili.com/video/BV1imaq6mEof/)

## 内容概览

已完成本地机器逐字稿；完整内容总结依据当前所选中文稿。

## 完整逐字稿

- [查看中文逐字稿](./transcript.zh-CN.md)

## 完整总结

- [查看中文总结](./summary.zh-CN.md)
