---
schema_version: 1
kind: episode
id: svvector:bili-bv1dnjs66e44
show_id: svvector
episode_key: bili-bv1dnjs66e44
episode_number: null
slug: bili-bv1dnjs66e44-li-yanbing
release_type: regular
numbering:
  status: not-in-publisher-feed
  checked_at: '2026-10-23'
  source: publisher-page
title: '硅谷坐标 x Datadog首席产品官｜HYSTA主席李严冰: AI 落地进入 ROI 时代'
navigation_title: 李严冰 · AI运维、可观测性与ROI
catalog_keyword: 可观测性
published_at: '2026-10-16T07:33:04+08:00'
duration_ms: 974784
language: zh-CN
participants:
  - id: li-yanbing
    name: 李严冰
    aliases: []
    role: guest
  - id: cao-qingyun
    name: 曹卿云
    aliases: []
    role: host
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1DnJS66E44/
    preferred: true
    title: '硅谷坐标 x Datadog首席产品官｜HYSTA主席李严冰: AI 落地进入 ROI 时代'
    identifiers:
      bvid: BV1DnJS66E44
      aid: '117447524882337'
      cid: '42777775794'
      page: 1
  - platform: xiaoyuzhou
    kind: episode
    url: https://www.xiaoyuzhoufm.com/episode/6ad5a9820e4e410a05beffc3
    preferred: false
    title: AI 落地最大的障碍不是模型，是运维｜对话 Datadog 首席产品官李严冰
    identifiers:
      eid: 6ad5a9820e4e410a05beffc3
      pid: 69a4b82b27e15c06061cfc2d
      media_id: 69a4b82b27e15c06061cfc2d/lvZmw-7HBNJmW19FodFprwP-sNSy.m4a
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
    sha256: 0ed7466d44692b49912801ba01e99cc68eddd0d280c925192e293c67ef5a4718
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
    planned_chunk_count: 5
    final_leaf_chunk_count: 5
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 20480
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: '2026-10-23T15:20:48.145225Z'
  access_context: anonymous
  platform_subtitle_access:
    anonymous_tracks: []
    need_login: true
    authenticated_context: not-authorized-or-used
  quality:
    source_chunks: 5
    aligned_chunks: 5
    alignment_items: 4123
    sentence_segments: 94
    source_segments: 94
    refined_segments: 94
    rendered_blocks: 35
    rendered_lines: 94
  performance:
    model_load_seconds: 0.186
    transcription_seconds: 27.856
    prompt_tokens: 12764
    generation_tokens: 2596
    attempt_prompt_tokens: 12764
    attempt_generation_tokens: 2596
    generation_call_count: 5
    prompt_tokens_per_second: 458.22
    generation_tokens_per_second: 93.195
    aligner_load_seconds: 0.139
    alignment_seconds: 4.643
asr_runs:
  - id: qwen3-asr
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    generated_at: '2026-10-23T15:20:48.145225Z'
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 9117777
  duration_ms: 974784
  sha256: 6c56f7a88d1ea9b39981019c39d21b4b0bd71654369e21e3a0c9faa36fed771b
  path: .cache/media/svvector/bili-bv1dnjs66e44-li-yanbing/source.m4a
  metadata_path: .cache/media/svvector/bili-bv1dnjs66e44-li-yanbing/source.metadata.json
  git_ignored: true
  acquired_at: '2026-10-23T15:14:25.160167Z'
  verified_at: '2026-10-23T15:14:25.160167Z'
last_verified_at: '2026-10-23'
asr_artifacts:
  raw:
    path: asr/qwen3-asr/raw.json
    git_ignored: false
    format: podwiki-raw-asr-json-v1
    sha256: ad015f3f579e5d9f35f5fbc577026c0a3b35fece3483500dec94e0846fc2f75a
  aligned:
    path: asr/qwen3-asr/aligned.json
    git_ignored: false
    format: podwiki-aligned-asr-json-v1
    sha256: c81099575cd4f94e9bc730f69d9041096097e8b6da643b552ac08fbcd6c32e46
  refined:
    path: asr/qwen3-asr/refined.json
    git_ignored: false
    format: podwiki-refined-asr-json-v1
    sha256: d754d0eeb7f8bcc988556bb166bffa2308f99a0d91cf81fd2b62d4f97560d9e4
  transcript:
    path: asr/qwen3-asr/transcript.zh-CN.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
    sha256: 0ed7466d44692b49912801ba01e99cc68eddd0d280c925192e293c67ef5a4718
  renderer: scripts/render_asr_transcript.py
---

# 硅谷坐标 x Datadog首席产品官｜HYSTA主席李严冰: AI 落地进入 ROI 时代

> 逐字稿由本地固定版本Qwen3-ASR与ForcedAligner生成，状态为`machine`；全文总结为`draft`。尚未完成逐段人工核听。

## 单集信息

- 总结：[查看全文总结](./summary.zh-CN.md)
- 正式逐字稿：[查看中文逐字稿](./transcript.zh-CN.md)
- 原始节目：[发布者完整单集](https://www.bilibili.com/video/BV1DnJS66E44/)

## 来源核验

- 官方发布者、公开免费单P、BVID/aid/cid/page与本地音频大小、时长和SHA-256均已核实。
- 与官方播客发布的嘉宾、内容主题、章节和完整时长对应；小宇宙仅作身份和同集交叉核对。
- 本次匿名上下文未发现可用字幕；没有使用登录态，也未把匿名检查解释为所有上下文均无字幕。

## 待审核

- 逐段核听人名、公司与模型名、数字、否定词及说话人归属。
- 对总结中的关键引文和高影响事实做必要的回听及独立核查；当前不得标为reviewed。
