---
schema_version: 1
kind: episode
id: "luoyonghao:bili-bv1ukm26zesf"
show_id: luoyonghao
episode_key: "bili-bv1ukm26zesf"
episode_number: null
slug: bili-bv1ukm26zesf-x-shiliyan
release_type: special
numbering:
  status: unknown
  checked_at: 2026-08-09
  source: publisher-rss-branch-and-season
  url: https://feed.xyzfm.space/wmnkvmrpwuww
  note: "发布者明确将其定义为《十字路口》分支系列《X字路口》的完整播客正片，但未提供正式期号；不根据发布日期或合集顺序推导"
title: "【正片】罗永浩的X字路口！我们能活到今天，多亏了祖传的势利眼"
navigation_title: "呼兰、小块、王继业、小镟 · 势利眼与道德困境"
catalog_keyword: "道德困境"
published_at: "2026-08-06T13:00:00+08:00"
duration_ms: 10730603
language: zh-CN
participants:
  - id: hu-lan
    name: "呼兰"
    aliases: []
    role: guest
  - id: xiao-kuai
    name: "小块"
    aliases: []
    role: guest
  - id: wang-jiye
    name: "王继业"
    aliases: []
    role: guest
  - id: xiao-xuan
    name: "小镟"
    aliases: []
    role: guest
sources:
  - platform: bilibili
    kind: video
    title: "【正片】罗永浩的X字路口！我们能活到今天，多亏了祖传的势利眼"
    url: https://www.bilibili.com/video/BV1ukM26zESF/
    preferred: true
    identifiers:
      bvid: BV1ukM26zESF
      aid: "117043311413663"
      cid: "40627144210"
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
    sha256: 8fc4bd7c5b973e95b0b4603baac9116555ef1f6136ebdc3b607810a9d88d4ca2
transcript:
  path: transcript.zh-CN.md
  platform_subtitle_access: no-anonymous-public-track
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
    planned_chunk_count: 45
    final_leaf_chunk_count: 45
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 184320
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: "2026-08-09T21:05:31.365120Z"
  quality:
    source_chunks: 45
    aligned_chunks: 45
    alignment_items: 55259
    sentence_segments: 3237
    refined_segments: 3217
    rendered_blocks: 345
    rendered_lines: 3217
  performance:
    model_load_seconds: 0.175
    transcription_seconds: 533.91
    prompt_tokens: 140318
    generation_tokens: 42323
    attempt_prompt_tokens: 140318
    attempt_generation_tokens: 42323
    generation_call_count: 45
    prompt_tokens_per_second: 262.812
    generation_tokens_per_second: 79.27
    aligner_load_seconds: 0.149
    alignment_seconds: 70.658
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
    generated_at: "2026-08-09T21:05:31.365120Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/luoyonghao/bili-bv1ukm26zesf-x-shiliyan/source.m4a
  metadata_path: .cache/media/luoyonghao/bili-bv1ukm26zesf-x-shiliyan/source.metadata.json
  git_ignored: true
  recovered_at: "2026-08-09T12:32:30.674224Z"
  verified_at: "2026-08-09T12:32:30.674224Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 159572028
  duration_ms: 10730603
  sha256: b448f8a2ef09c8ae2ea1ec604c9adb0c407174904385b5c01bbb0cb63d3d9209
last_verified_at: 2026-08-09
---

# 【正片】罗永浩的X字路口！我们能活到今天，多亏了祖传的势利眼

> 本页保留发布者材料形成的内容提纲，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 节目：罗永浩的十字路口
- 嘉宾：呼兰、小块、王继业、小镟
- 发布时间：2026-08-06 13:00:00（UTC+8）
- Bilibili 视频时长：02:58:51
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1ukM26zESF/)
- 来源状态：公开单 P；匿名访问未发现公开字幕轨；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 本地音频：AAC、48 kHz、双声道、159,572,028 字节
- 编号状态：《X字路口》为发布者确认的分支特别篇，但未提供正式 X 期号；保留 `episode_number: null`、`release_type: special`
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

发布者通过教育资源、救生选择、经营信息和职场机会等假设情境，让四位参与者讨论势利、诚实与现实利益之间的道德困境。

## 章节概览

- `[00:00:00]` 本期主题：势利
- `[00:13:35]` 如何正确押宝
- `[00:30:13]` 人类生存哲思问题
- `[00:57:55]` 小块面对势利眼
- `[01:27:20]` 权力的幻觉
- `[01:49:15]` 教育公平难题
- `[02:05:53]` 不诚实的领导
- `[02:46:12]` 情人节是骗局吗

## 核心议题

- 资源分配与选择困境
- 诚实、利益和现实判断
- 势利眼背后的生存逻辑

## 待补充

- [x] 核对 BVID、aid、cid、page、参与者、special 类型与期号缺失状态
- [x] 检查匿名访问可见的平台字幕轨并记录边界
- [x] 获取公开音轨并完成编码、时长、大小和哈希校验
- [x] 生成完整 Qwen3-ASR 机器逐字稿及 adaptive v2 产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 核听多人抢话片段、校对专有名词并核查进化、遗传、教育、劳动法律、商业经营、消费价格与其他高影响事实
