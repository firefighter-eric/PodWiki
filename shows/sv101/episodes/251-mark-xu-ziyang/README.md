---
schema_version: 1
kind: episode
id: sv101:251
show_id: sv101
episode_key: '251'
episode_number: 251
slug: 251-mark-xu-ziyang
release_type: regular
numbering:
  status: verified
  checked_at: '2026-10-14'
  source: https://sv101.fireside.fm/264
title: 推理芯片之战：聊聊Groq、Cerebras与OpenAI三大路径与Bill Dally的设计哲学【硅谷101播客】
navigation_title: Mark、徐子扬 · 推理芯片架构与设计
catalog_keyword: 推理芯片
published_at: '2026-09-16T00:00:00Z'
duration_ms: 5509333
language: zh-CN
participants:
  - id: hongjun
    name: 泓君
    aliases: []
    role: host
  - id: mark
    name: Mark
    aliases: []
    role: guest
  - id: xuziyang
    name: 徐子扬
    aliases: []
    role: guest
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1bqex6kEhT/
    preferred: true
    title: 推理芯片之战：聊聊Groq、Cerebras与OpenAI三大路径与Bill Dally的设计哲学【硅谷101播客】
    identifiers:
      bvid: BV1bqex6kEhT
      aid: '117277303250704'
      cid: '41929476525'
      page: 1
  - platform: website
    kind: episode
    url: https://sv101.fireside.fm/264
    preferred: false
    title: E251｜推理芯片之战：聊聊Groq、Cerebras与OpenAI三大路径与Bill Dally的设计哲学
    identifiers:
      feed_url: https://feeds.fireside.fm/sv101/rss
      guid: 786d63c4-d46c-4ff3-80f8-fc895b2a57f0
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
    sha256: b2cf9666dbdabaadcb8aee6ce3931293cb1264f738e6d500bf574034e5ea5876
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
    planned_chunk_count: 24
    final_leaf_chunk_count: 24
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 98304
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: '2026-10-13T17:55:33.151979Z'
  quality:
    source_chunks: 24
    aligned_chunks: 24
    alignment_items: 29786
    sentence_segments: 750
    source_segments: 750
    refined_segments: 750
    rendered_blocks: 186
    rendered_lines: 750
  performance:
    model_load_seconds: 0.208
    transcription_seconds: 240.375
    prompt_tokens: 72053
    generation_tokens: 19616
    attempt_prompt_tokens: 72053
    attempt_generation_tokens: 19616
    generation_call_count: 24
    prompt_tokens_per_second: 299.753
    generation_tokens_per_second: 81.606
    aligner_load_seconds: 0.152
    alignment_seconds: 37.083
  access_context: anonymous
asr_runs:
  - id: qwen3-asr
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    generated_at: '2026-10-13T17:55:33.151979Z'
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/sv101/251-mark-xu-ziyang/source.m4a
  metadata_path: .cache/media/sv101/251-mark-xu-ziyang/source.metadata.json
  git_ignored: true
  size_bytes: 82950361
  duration_ms: 5509333
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  sha256: cbc50311b8c38a05df75caa667e462dfd39b3bf00b31cd826d43f00204bef610
  verified_at: '2026-10-13T17:14:05.906109Z'
  acquired_at: '2026-10-13T17:14:05.906109Z'
last_verified_at: '2026-10-14'
asr_artifacts:
  raw:
    path: asr/qwen3-asr/raw.json
    git_ignored: false
    format: podwiki-raw-asr-json-v1
    sha256: 54acedfaccb8c8e643e9465d1dbf11ff67403a471220689a952fd335fa2e1da2
  aligned:
    path: asr/qwen3-asr/aligned.json
    git_ignored: false
    format: podwiki-aligned-asr-json-v1
    sha256: 6aa79c1e337387052df23b19fa028a1027c2c4416c5a8831de4ad37841ad2057
  refined:
    path: asr/qwen3-asr/refined.json
    git_ignored: false
    format: podwiki-refined-asr-json-v1
    sha256: 146cd60a1fe488f9c98616045c4d8bf71cc9d8420f85f14bd517660d976d366a
  transcript:
    path: asr/qwen3-asr/transcript.zh-CN.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
    sha256: b2cf9666dbdabaadcb8aee6ce3931293cb1264f738e6d500bf574034e5ea5876
  renderer: scripts/render_asr_transcript.py
---

# 推理芯片之战：聊聊Groq、Cerebras与OpenAI三大路径与Bill Dally的设计哲学【硅谷101播客】

> 中文逐字稿由本地 Qwen3-ASR 与 ForcedAligner 生成，保持 machine 状态。

## 单集信息

- 来源：[BV1bqex6kEhT](https://www.bilibili.com/video/BV1bqex6kEhT/)

## 内容概览

已完成本地机器逐字稿；完整内容总结依据当前所选中文稿。

## 完整逐字稿

- [查看中文逐字稿](./transcript.zh-CN.md)

## 完整总结

- [查看中文总结](./summary.zh-CN.md)
