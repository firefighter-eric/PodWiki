---
schema_version: 1
kind: episode
id: latetalk:183
show_id: latetalk
episode_key: '183'
episode_number: 183
slug: 183-henry-yin
release_type: regular
numbering:
  status: verified
  checked_at: '2026-10-14'
  source: https://podcast.latepost.com/183
title: AI 季报 26Q3：从 Meta 到 OpenAI，个人助理卷土重来【晚点聊 LateTalk】
navigation_title: Henry Yin · 个人助理与AI季报
catalog_keyword: 个人助理
published_at: '2026-10-08T10:59:52Z'
duration_ms: 7627871
language: zh-CN
participants:
  - id: henryyin
    name: Henry Yin
    aliases: []
    role: guest
    profile:
      headline: MoE Capital 创始合伙人
      checked_at: '2026-10-14'
  - id: chengmanqi
    name: 程曼祺
    aliases: []
    role: host
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1wqHD6qEqU/
    preferred: true
    title: AI 季报 26Q3：从 Meta 到 OpenAI，个人助理卷土重来【晚点聊 LateTalk】
    identifiers:
      bvid: BV1wqHD6qEqU
      aid: '117404910949380'
      cid: '42566878394'
      page: 1
  - platform: website
    kind: episode
    url: https://podcast.latepost.com/183
    preferred: false
    title: 与Henry的「AI季报26Q3」：Muse引爆个人助理、Astra进入机器人、OpenAI收入猛增
    identifiers:
      feed_url: https://podcast.latepost.com/rss
      guid: 47e78c2f-c36f-4894-9124-dad5dcffc972
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
    sha256: ba93faf86c33539371103c7915298a67316566b16156085b2d622238b171aa1b
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
    planned_chunk_count: 32
    final_leaf_chunk_count: 32
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 131072
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: '2026-10-13T17:34:09.737677Z'
  quality:
    source_chunks: 32
    aligned_chunks: 32
    alignment_items: 40362
    sentence_segments: 964
    source_segments: 964
    refined_segments: 964
    rendered_blocks: 262
    rendered_lines: 964
  performance:
    model_load_seconds: 0.213
    transcription_seconds: 279.65
    prompt_tokens: 99741
    generation_tokens: 27466
    attempt_prompt_tokens: 99741
    attempt_generation_tokens: 27466
    generation_call_count: 32
    prompt_tokens_per_second: 356.664
    generation_tokens_per_second: 98.216
    aligner_load_seconds: 0.22
    alignment_seconds: 43.37
  access_context: anonymous
asr_runs:
  - id: qwen3-asr
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    generated_at: '2026-10-13T17:34:09.737677Z'
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/latetalk/183-henry-yin/source.m4a
  metadata_path: .cache/media/latetalk/183-henry-yin/source.metadata.json
  git_ignored: true
  size_bytes: 94029187
  duration_ms: 7627871
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  sha256: 3c4f4f3c1d89ab072ef1da40e1a6b2d685382607c917ed353eebb3dbd62c91b9
  verified_at: '2026-10-13T17:13:08.473503Z'
  acquired_at: '2026-10-13T17:13:08.473503Z'
last_verified_at: '2026-10-14'
asr_artifacts:
  raw:
    path: asr/qwen3-asr/raw.json
    git_ignored: false
    format: podwiki-raw-asr-json-v1
    sha256: ccc7ee4593c41ae383925e5c2916d48abbf4bf30c0eea7ecc1c53a5a601dce87
  aligned:
    path: asr/qwen3-asr/aligned.json
    git_ignored: false
    format: podwiki-aligned-asr-json-v1
    sha256: 6c1165746e93ab6ccba64c2938fbf90d008d8eea553193bcab65c18c7bad6b2a
  refined:
    path: asr/qwen3-asr/refined.json
    git_ignored: false
    format: podwiki-refined-asr-json-v1
    sha256: c5ad7e796db66068c1116b5745ad6c40ace2f0163e4e0d139c36a496da7642ab
  transcript:
    path: asr/qwen3-asr/transcript.zh-CN.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
    sha256: ba93faf86c33539371103c7915298a67316566b16156085b2d622238b171aa1b
  renderer: scripts/render_asr_transcript.py
---

# AI 季报 26Q3：从 Meta 到 OpenAI，个人助理卷土重来【晚点聊 LateTalk】

> 中文逐字稿由本地 Qwen3-ASR 与 ForcedAligner 生成，保持 machine 状态。

## 单集信息

- 来源：[BV1wqHD6qEqU](https://www.bilibili.com/video/BV1wqHD6qEqU/)

## 内容概览

已完成本地机器逐字稿；完整内容总结依据当前所选中文稿。

## 完整逐字稿

- [查看中文逐字稿](./transcript.zh-CN.md)

## 完整总结

- [查看中文总结](./summary.zh-CN.md)
