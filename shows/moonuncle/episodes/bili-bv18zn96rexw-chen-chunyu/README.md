---
schema_version: 1
kind: episode
id: moonuncle:bili-bv18zn96rexw
show_id: moonuncle
episode_key: bili-bv18zn96rexw
episode_number: null
slug: bili-bv18zn96rexw-chen-chunyu
release_type: regular
numbering:
  status: not-in-publisher-feed
  checked_at: '2026-11-08'
  source: https://www.bilibili.com/video/BV18Zn96REXW/
title: 陈春宇：清华，辍学，睡地板，精英的傲慢，硅谷，创业，情商，聊天软件，全球翻译，生物，爱自己
navigation_title: 陈春宇 · 辍学创业与真实用户
catalog_keyword: Intent
published_at: '2026-10-26T04:52:16+00:00'
duration_ms: 6824693
language: zh-CN
participants:
  - id: chen-chunyu
    name: 陈春宇
    aliases: []
    role: guest
  - id: moonuncle
    name: 月球大叔
    aliases: []
    role: host
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV18Zn96REXW/
    preferred: true
    title: 陈春宇：清华，辍学，睡地板，精英的傲慢，硅谷，创业，情商，聊天软件，全球翻译，生物，爱自己
    identifiers:
      bvid: BV18Zn96REXW
      aid: '117505406277466'
      cid: '43057087746'
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
    sha256: 5d5a2765958d97feedecfa7d3cf74ac8c47564b430f8d97659a15069b07caa8a
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
    planned_chunk_count: 29
    final_leaf_chunk_count: 29
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 118784
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: '2026-11-08T15:51:50.684358Z'
  access_context: authenticated-subtitle-check-public-audio
  platform_subtitle_access:
    anonymous_tracks: []
    need_login: false
    authenticated_context: checked-no-subtitle-control-or-track
  quality:
    source_chunks: 29
    aligned_chunks: 29
    alignment_items: 39341
    sentence_segments: 891
    source_segments: 891
    refined_segments: 891
    rendered_blocks: 230
    rendered_lines: 891
  performance:
    model_load_seconds: 0.191
    transcription_seconds: 263.012
    prompt_tokens: 89246
    generation_tokens: 25579
    attempt_prompt_tokens: 89246
    attempt_generation_tokens: 25579
    generation_call_count: 29
    prompt_tokens_per_second: 339.324
    generation_tokens_per_second: 97.254
    aligner_load_seconds: 0.211
    alignment_seconds: 39.855
asr_runs:
  - id: qwen3-asr
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    generated_at: '2026-11-08T15:51:50.684358Z'
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 94944941
  duration_ms: 6824693
  sha256: c9008d1441ee0968835f274a9b1b15c4b30abd5fa14680b6a04d831004b8126b
  path: .cache/media/moonuncle/bili-bv18zn96rexw-chen-chunyu/source.m4a
  metadata_path: .cache/media/moonuncle/bili-bv18zn96rexw-chen-chunyu/source.metadata.json
  git_ignored: true
  acquired_at: '2026-11-08T15:40:49.645980Z'
  verified_at: '2026-11-08T15:40:49.645980Z'
last_verified_at: '2026-11-08'
asr_artifacts:
  raw:
    path: asr/qwen3-asr/raw.json
    git_ignored: false
    format: podwiki-raw-asr-json-v1
    sha256: dc37e117c9d3b5ff7058449e6c05ed6f6adf5e26e3c927857a2c4753eeb0f0a2
  aligned:
    path: asr/qwen3-asr/aligned.json
    git_ignored: false
    format: podwiki-aligned-asr-json-v1
    sha256: 77c40be1c449468da1b29f32e57e3d983151a385150ae59f6ba0a0412ba9032c
  refined:
    path: asr/qwen3-asr/refined.json
    git_ignored: false
    format: podwiki-refined-asr-json-v1
    sha256: d3bbd7c1d7bc529011e16eaf112018498a317b3a5c58ddd867574ae05a4b5414
  transcript:
    path: asr/qwen3-asr/transcript.zh-CN.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
    sha256: 5d5a2765958d97feedecfa7d3cf74ac8c47564b430f8d97659a15069b07caa8a
  renderer: scripts/render_asr_transcript.py
---

# 陈春宇：清华，辍学，睡地板，精英的傲慢，硅谷，创业，情商，聊天软件，全球翻译，生物，爱自己

> 逐字稿由本地固定版本Qwen3-ASR与ForcedAligner生成，状态为`machine`；全文总结为`draft`。尚未完成逐段人工核听。

## 单集信息

- 总结：[查看全文总结](./summary.zh-CN.md)
- 正式逐字稿：[查看中文逐字稿](./transcript.zh-CN.md)
- 原始节目：[发布者完整单集](https://www.bilibili.com/video/BV18Zn96REXW/)

## 来源核验

- 官方发布者、公开免费单P、BVID/aid/cid/page与本地音频大小、时长和SHA-256均已核实。
- 播客完整性由官方RSS同集映射或官方播客正片合集核实；实际输入来自批准的B站正片。
- 本机已登录Chrome完整播放界面未提供可用字幕控件或轨道；随后使用匿名公开免费音轨进行本地ASR。

## 待审核

- 逐段核听人名、公司与模型名、数字、否定词及说话人归属。
- 对总结中的关键引文和高影响事实做必要的回听及独立核查；当前不得标为reviewed。
