---
schema_version: 1
kind: episode
id: xuhuazhe:bili-bv1jxue66emy
show_id: xuhuazhe
episode_key: bili-bv1jxue66emy
episode_number: null
slug: bili-bv1jxue66emy-mu-beipeng
release_type: regular
numbering:
  status: unknown
  checked_at: '2026-10-14'
  source: https://www.bilibili.com/video/BV1jxuE66EmY/
title: 老友记：MIT博士的机器人创业路
navigation_title: 穆北鹏 · 机器人创业与人生选择
catalog_keyword: 机器人创业
published_at: '2026-08-06T12:00:00Z'
duration_ms: 2609344
language: zh-CN
participants:
  - id: mubeipeng
    name: 穆北鹏
    aliases: []
    role: guest
    profile:
      headline: 小狸机器人创始人
      checked_at: '2026-10-14'
  - id: xuhuazhe
    name: 许华哲
    aliases: []
    role: host
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1jxuE66EmY/
    preferred: true
    title: 老友记：MIT博士的机器人创业路
    identifiers:
      bvid: BV1jxuE66EmY
      aid: '117046834627759'
      cid: '40647067190'
      page: 1
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
    sha256: 3827b0c1078aa6a6c94858851dceb4e8ca6d4d4fa671ee9af794b77ea34bfbcf
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
    planned_chunk_count: 11
    final_leaf_chunk_count: 11
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 45056
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: '2026-10-13T18:12:42.303551Z'
  quality:
    source_chunks: 11
    aligned_chunks: 11
    alignment_items: 13385
    sentence_segments: 404
    source_segments: 404
    refined_segments: 403
    rendered_blocks: 87
    rendered_lines: 403
  performance:
    model_load_seconds: 0.188
    transcription_seconds: 114.143
    prompt_tokens: 34120
    generation_tokens: 9385
    attempt_prompt_tokens: 34120
    attempt_generation_tokens: 9385
    generation_call_count: 11
    prompt_tokens_per_second: 298.924
    generation_tokens_per_second: 82.222
    aligner_load_seconds: 0.136
    alignment_seconds: 17.206
  access_context: anonymous
asr_runs:
  - id: qwen3-asr
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    generated_at: '2026-10-13T18:12:42.303551Z'
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/xuhuazhe/bili-bv1jxue66emy-mu-beipeng/source.m4a
  metadata_path: .cache/media/xuhuazhe/bili-bv1jxue66emy-mu-beipeng/source.metadata.json
  git_ignored: true
  size_bytes: 61635092
  duration_ms: 2609344
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  sha256: 0757628b293f8980c64018f2e2182ca872088e72f814533de5c13852dc28dcc0
  verified_at: '2026-10-13T17:13:46.303431Z'
  acquired_at: '2026-10-13T17:13:46.303431Z'
last_verified_at: '2026-10-14'
asr_artifacts:
  raw:
    path: asr/qwen3-asr/raw.json
    git_ignored: false
    format: podwiki-raw-asr-json-v1
    sha256: fd3a2a2d6150afd10f6f7c8193b0995148f42cc45d148d5ba70fd75737a842ce
  aligned:
    path: asr/qwen3-asr/aligned.json
    git_ignored: false
    format: podwiki-aligned-asr-json-v1
    sha256: 3701fd92d56a09ee002b0eba3c87af7eaacebf6e31892ee9904634f0b9a7e02b
  refined:
    path: asr/qwen3-asr/refined.json
    git_ignored: false
    format: podwiki-refined-asr-json-v1
    sha256: ff749c450ab6f013da1e4181afec15c9760cdb360ff72c8a075bf1f79b370069
  transcript:
    path: asr/qwen3-asr/transcript.zh-CN.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
    sha256: 3827b0c1078aa6a6c94858851dceb4e8ca6d4d4fa671ee9af794b77ea34bfbcf
  renderer: scripts/render_asr_transcript.py
---

# 老友记：MIT博士的机器人创业路

> 中文逐字稿由本地 Qwen3-ASR 与 ForcedAligner 生成，保持 machine 状态。

## 单集信息

- 来源：[BV1jxuE66EmY](https://www.bilibili.com/video/BV1jxuE66EmY/)

## 内容概览

已完成本地机器逐字稿；完整内容总结依据当前所选中文稿。

## 完整逐字稿

- [查看中文逐字稿](./transcript.zh-CN.md)

## 完整总结

- [查看中文总结](./summary.zh-CN.md)
