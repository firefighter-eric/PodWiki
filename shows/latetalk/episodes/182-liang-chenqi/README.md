---
schema_version: 1
kind: episode
id: latetalk:182
show_id: latetalk
episode_key: '182'
episode_number: 182
slug: 182-liang-chenqi
release_type: regular
numbering:
  status: verified
  checked_at: '2026-10-02'
  source: https://podcast.latepost.com/182
title: 对话梁琛奇：抖音→猫箱→创业，他们都搞生产力，我想用 AI 创造开心【晚点聊LateTalk】
navigation_title: 梁琛奇 · AI娱乐与泛创作
catalog_keyword: AI娱乐
published_at: '2026-09-30T20:21:21+08:00'
duration_ms: 12119400
language: zh-CN
participants:
  - id: liang-chenqi
    name: 梁琛奇
    aliases: []
    role: guest
  - id: cheng-manqi
    name: 程曼祺
    aliases: []
    role: host
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1Vbao6aEYM/
    title: 对话梁琛奇：抖音→猫箱→创业，他们都搞生产力，我想用 AI 创造开心【晚点聊LateTalk】
    preferred: true
    identifiers:
      bvid: BV1Vbao6aEYM
      aid: '117359947813263'
      cid: '42341043024'
      page: 1
  - platform: website
    kind: episode
    url: https://podcast.latepost.com/182
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
    path: transcript.zh-CN.md
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    selection_status: selected
    sha256: bfaae7acb75984262717af2805446d887fcc7ce8981e86a2540d614939f9579b
transcript:
  path: transcript.zh-CN.md
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
    planned_chunk_count: 51
    final_leaf_chunk_count: 51
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 208896
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: '2026-10-02T15:16:40.287322Z'
  access_context: anonymous
  quality:
    source_chunks: 51
    aligned_chunks: 51
    alignment_items: 70986
    sentence_segments: 1989
    source_segments: 1989
    refined_segments: 1988
    rendered_blocks: 405
    rendered_lines: 1988
  performance:
    model_load_seconds: 0.455
    transcription_seconds: 605.116
    prompt_tokens: 158477
    generation_tokens: 47697
    attempt_prompt_tokens: 158477
    attempt_generation_tokens: 47697
    generation_call_count: 51
    prompt_tokens_per_second: 261.895
    generation_tokens_per_second: 78.823
    aligner_load_seconds: 0.323
    alignment_seconds: 94.432
  translations: []
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
    path: asr/qwen3-asr/transcript.zh-CN.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
  renderer: scripts/render_asr_transcript.py
asr_runs:
  - id: qwen3-asr
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    generated_at: '2026-10-02T15:16:40.287322Z'
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/latetalk/182-liang-chenqi/source.m4a
  metadata_path: .cache/media/latetalk/182-liang-chenqi/source.metadata.json
  git_ignored: true
  size_bytes: 117533940
  duration_ms: 12119400
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  sha256: e473878977e5dd06b9d6ba94b44f0c2a96d178213346708e7a68f873a2de41f9
  verified_at: '2026-10-02T15:01:13.691857Z'
  acquired_at: '2026-10-02T15:01:13.691857Z'
last_verified_at: '2026-10-02'
---

# 对话梁琛奇：抖音→猫箱→创业，他们都搞生产力，我想用 AI 创造开心【晚点聊LateTalk】

> 正式稿由本地固定版本 Qwen3-ASR 与 ForcedAligner 生成，为 `machine`；总结依据完整所选原文，为 `draft`，待人工审核。

## 单集信息

- 总结：[查看总结](./summary.zh-CN.md)
- 正式逐字稿：[查看中文逐字稿](./transcript.zh-CN.md)
- 原始节目：[发布者完整单集](https://www.bilibili.com/video/BV1Vbao6aEYM/)

## 待审核

- 回听核对人名、数字、否定词、说话人归属与时间戳。
- 核对总结的观点归属、论据与限制条件。
