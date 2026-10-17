---
schema_version: 1
kind: episode
id: zhangxiaojun:154
show_id: zhangxiaojun
episode_key: '154'
episode_number: 154
slug: 154-lindon-gao
release_type: regular
numbering:
  status: verified
  checked_at: '2026-10-17'
  source: https://feed.xyzfm.space/dk4yh3pkpjp3
title: 对Dyna创始人Lindon Gao的3小时访谈：机器人世界的迷雾、分歧与抉择，修心、《沉思录》与王阳明
navigation_title: Lindon Gao · 机器人产品路线与创业修心
catalog_keyword: Dyna
published_at: '2026-10-15T00:00:00+00:00'
duration_ms: 10278272
language: zh-CN
participants:
  - id: lindongao
    name: Lindon Gao
    aliases: []
    role: guest
    profile:
      headline: Dyna Robotics 创始人兼 CEO
      checked_at: '2026-10-17'
  - id: zhangxiaojun
    name: 张小珺
    aliases: []
    role: host
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1wgpy69Ekz/
    preferred: true
    title: 对Dyna创始人Lindon Gao的3小时访谈：机器人世界的迷雾、分歧与抉择，修心、《沉思录》与王阳明
    identifiers:
      bvid: BV1wgpy69Ekz
      aid: '117437575987587'
      cid: '42728557483'
      page: 1
  - platform: rss
    kind: feed
    url: https://feed.xyzfm.space/dk4yh3pkpjp3
    preferred: false
    title: 154. 对Dyna创始人Lindon的3小时访谈：机器人世界的迷雾、分歧与抉择，修心、《沉思录》与王阳明
    identifiers:
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 6acf81f0195d838e2af1e281
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
    sha256: b5a1bfb247db2ae04804f95bdc3b5fc74e23608952795fa418507c4ad35a9e1d
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
    planned_chunk_count: 43
    final_leaf_chunk_count: 43
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 176128
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: '2026-10-17T15:25:02.791623Z'
  access_context: anonymous
  quality:
    source_chunks: 43
    aligned_chunks: 43
    alignment_items: 47035
    sentence_segments: 1666
    source_segments: 1666
    refined_segments: 1662
    rendered_blocks: 349
    rendered_lines: 1662
  performance:
    model_load_seconds: 0.341
    transcription_seconds: 340.286
    prompt_tokens: 134398
    generation_tokens: 31026
    attempt_prompt_tokens: 134398
    attempt_generation_tokens: 31026
    generation_call_count: 43
    prompt_tokens_per_second: 394.956
    generation_tokens_per_second: 91.176
    aligner_load_seconds: 0.224
    alignment_seconds: 54.319
asr_artifacts:
  raw:
    path: asr/qwen3-asr/raw.json
    git_ignored: false
    format: podwiki-raw-asr-json-v1
    sha256: a0dd3af0c33bb7af8a68af9738209a6f3293671af0bc2c108facfd8851d59a17
  aligned:
    path: asr/qwen3-asr/aligned.json
    git_ignored: false
    format: podwiki-aligned-asr-json-v1
    sha256: 3457a60e628df2fff9349e99f90d310a9f9ea869e27df9dc1c4e29a0e3dd4c51
  refined:
    path: asr/qwen3-asr/refined.json
    git_ignored: false
    format: podwiki-refined-asr-json-v1
    sha256: 913b6ab36f02b34a7ebeeef0496cef425403d526c386e3ddf2db2fff38710d85
  transcript:
    path: asr/qwen3-asr/transcript.zh-CN.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
    sha256: b5a1bfb247db2ae04804f95bdc3b5fc74e23608952795fa418507c4ad35a9e1d
  renderer: scripts/render_asr_transcript.py
asr_runs:
  - id: qwen3-asr
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    generated_at: '2026-10-17T15:25:02.791623Z'
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/154-lindon-gao/source.m4a
  metadata_path: .cache/media/zhangxiaojun/154-lindon-gao/source.metadata.json
  git_ignored: true
  acquired_at: '2026-10-17T15:14:51.704847Z'
  verified_at: '2026-10-17T15:14:51.704847Z'
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 173702754
  duration_ms: 10278272
  sha256: 3759db7246ec69e2c5dd780aa22e37b9b73d2d0fe88203775389fcdfc0e51e86
last_verified_at: '2026-10-17'
---

# 对Dyna创始人Lindon Gao的3小时访谈：机器人世界的迷雾、分歧与抉择，修心、《沉思录》与王阳明

> 正式稿由本地固定版本 Qwen3-ASR 与 ForcedAligner 生成，状态为 `machine`。全文总结为 `draft`；尚未人工核听。

## 单集信息

- 正式逐字稿：[查看中文逐字稿](./transcript.zh-CN.md)
- 总结：[查看全文总结](./summary.zh-CN.md)
- 原始节目：[发布者完整单集](https://www.bilibili.com/video/BV1wgpy69Ekz/)

## 来源核验

- 官方B站发布者、单P、BVID/aid/cid/page与免费访问状态已核实。
- 官方 RSS 以第154期发布同一嘉宾、简介与章节；B站展示时长与RSS相差1秒。正式稿绑定本地已核验音频的实际时长。
- 本次匿名访问未发现可用字幕；没有使用登录态、导出凭据或将匿名检查解释为所有访问上下文都无字幕。

## 待审核

- 核听人名、数字、否定词、说话人归属与关键引文。
- 校对总结观点归属和限制条件，对商业经历与产品能力等高影响事实做独立核查。
