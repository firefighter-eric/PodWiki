---
schema_version: 1
kind: episode
id: "luoyonghao:bili-bv1h67b63eye"
show_id: luoyonghao
episode_key: "bili-bv1h67b63eye"
episode_number: null
slug: bili-bv1h67b63eye-x-jieqian
release_type: special
numbering:
  status: unknown
  checked_at: 2026-08-09
  source: publisher-rss-branch-and-season
  url: https://feed.xyzfm.space/wmnkvmrpwuww
  note: "发布者明确将其定义为《十字路口》分支系列《X字路口》的完整播客正片，但未提供正式期号；不根据发布日期或合集顺序推导"
title: "【正片】罗永浩的X字路口！不借钱给朋友，就会失去朋友失去钱！"
navigation_title: "小镟、贤鱼、王继业、小四爷 · 朋友借钱"
catalog_keyword: "朋友借钱"
published_at: "2026-06-26T12:00:00+08:00"
duration_ms: 9702251
language: zh-CN
participants:
  - id: xiao-xuan
    name: "小镟"
    aliases: []
    role: guest
  - id: xian-yu
    name: "贤鱼"
    aliases: []
    role: guest
  - id: wang-jiye
    name: "王继业"
    aliases: []
    role: guest
  - id: xiao-siye
    name: "小四爷"
    aliases: []
    role: guest
sources:
  - platform: bilibili
    kind: video
    title: "【正片】罗永浩的X字路口！不借钱给朋友，就会失去朋友失去钱！"
    url: https://www.bilibili.com/video/BV1h67B63EyE/
    preferred: true
    identifiers:
      bvid: BV1h67B63EyE
      aid: "116813681724363"
      cid: "39411516434"
      page: 1
workflow:
  metadata: verified
  summary: draft
  transcript: machine
summary_basis:
  - publisher-description
  - publisher-chapters
  - complete-machine-transcript
summary:
  path: summary.zh-CN.md
  language: zh-CN
  source_transcript:
    path: transcript.zh-CN.md
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    selection_status: selected
    sha256: 42ea3e06fdf7f7110ce1064f18007b4f16553aa44f8477f7828d097a29c86079
transcript:
  path: transcript.zh-CN.md
  platform_subtitle_access: no-anonymous-track-login-indicated
  platform_subtitle_languages: []
  automatic_caption_languages: []
  acquisition_method: audio-asr
  asr_script: scripts/transcribe_qwen3_asr.py
  engine: mlx-audio
  model: mlx-community/Qwen3-ASR-1.7B-8bit
  aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
  options:
    language: Chinese
    temperature: 0
    max_tokens_per_chunk: 4096
    chunk_duration_seconds: 240
    planned_chunk_count: 41
    final_leaf_chunk_count: 48
    adaptive_split_count: 7
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 196608
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: "2026-08-09T20:55:15.494400Z"
  quality:
    source_chunks: 48
    aligned_chunks: 48
    alignment_items: 46137
    sentence_segments: 3073
    refined_segments: 3049
    rendered_blocks: 319
    rendered_lines: 3049
  performance:
    model_load_seconds: 0.176
    transcription_seconds: 855.445
    prompt_tokens: 127003
    generation_tokens: 36637
    attempt_prompt_tokens: 144384
    attempt_generation_tokens: 65309
    generation_call_count: 55
    prompt_tokens_per_second: 148.464
    generation_tokens_per_second: 42.828
    aligner_load_seconds: 0.172
    alignment_seconds: 64.383
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
  - id: qwen3-asr-1.7b-8bit
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    generated_at: "2026-08-09T20:55:15.494400Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/luoyonghao/bili-bv1h67b63eye-x-jieqian/source.m4a
  metadata_path: .cache/media/luoyonghao/bili-bv1h67b63eye-x-jieqian/source.metadata.json
  git_ignored: true
  recovered_at: "2026-08-09T12:32:29.235833Z"
  verified_at: "2026-08-09T12:32:29.235833Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 143811162
  duration_ms: 9702251
  sha256: a212afeb1c0f45ed47e36f022b0886564e9666c2957e333f9f04aea5929820b6
last_verified_at: 2026-08-09
---

# 【正片】罗永浩的X字路口！不借钱给朋友，就会失去朋友失去钱！

> 本页保留发布者材料形成的内容提纲，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 节目：罗永浩的十字路口
- 嘉宾：小镟、贤鱼、王继业、小四爷
- 发布时间：2026-06-26 12:00:00（UTC+8）
- Bilibili 视频时长：02:41:42
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1h67B63EyE/)
- 来源状态：公开单 P；匿名访问未发现公开字幕轨；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 本地音频：AAC、48 kHz、双声道、143,811,162 字节
- 编号状态：《X字路口》为发布者确认的分支特别篇，但未提供正式 X 期号；保留 `episode_number: null`、`release_type: special`
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

发布者将本集定义为《X字路口》与肆笑喜剧的首次联动，以朋友借钱、债务和人情关系为入口展开多人讨论。

## 章节概览

- `[00:00:00]` 聊聊跟风
- `[00:17:25]` 追星经历
- `[00:41:19]` 警惕连环校园贷
- `[01:10:20]` 险些欠债三百万
- `[01:44:05]` 脱口秀大局观
- `[02:02:05]` 穷人乍富
- `[02:12:37]` 消费观念
- `[02:25:47]` 放心借钱的秘技
- `[02:31:38]` 讨债人的一天
- `[02:40:05]` 结尾上价值

## 核心议题

- 朋友借钱与人情边界
- 债务经历和风险判断
- 《X字路口》与肆笑喜剧联动

## 待补充

- [x] 核对 BVID、aid、cid、page、参与者、special 类型与期号缺失状态
- [x] 检查匿名访问可见的平台字幕轨并记录边界
- [x] 获取公开音轨并完成编码、时长、大小和哈希校验
- [x] 生成完整 Qwen3-ASR 机器逐字稿及 adaptive v2 产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 核听多人抢话片段、校对专有名词并核查金融、法律、数字与高影响事实
