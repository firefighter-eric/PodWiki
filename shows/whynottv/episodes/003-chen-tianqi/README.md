---
schema_version: 1
kind: episode
id: "whynottv:003"
show_id: whynottv
episode_key: "003"
episode_number: 3
slug: 003-chen-tianqi
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-07
  source: publisher-rss
title: "陈天奇：机器学习系统，长期主义，初心，XGBoost，MXNet，TVM，MLC LLM，OctoML｜WhynotTV Podcast #3"
navigation_title: "陈天奇 · XGBoost、TVM 与机器学习系统"
catalog_keyword: "XGBoost"
published_at: "2025-09-12T22:11:25+08:00"
duration_ms: 9610346
language: zh-CN
participants:
  - id: he-tairan
    name: 何泰然
    role: host
  - id: chen-tianqi
    name: 陈天奇
    role: guest
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1s6pgzLE3y/
    preferred: true
    identifiers:
      bvid: BV1s6pgzLE3y
      aid: "115191610083914"
      cid: "32337169816"
      page: 1
workflow:
  metadata: verified
  summary: draft
  transcript: machine
summary_basis:
  - publisher-description
  - complete-machine-transcript
summary:
  path: summary.zh-CN.md
  language: zh-CN
  source_transcript:
    path: transcript.zh-CN.md
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    selection_status: selected
    sha256: faa71039a20ff377e6ca58924bd3ef20d5535f0da0ef3f20c22d32feb56521d1
transcript:
  path: transcript.zh-CN.md
  platform_subtitle_access: no-anonymous-track
  platform_subtitle_languages: []
  automatic_caption_languages: []
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
    max_sentence_characters: 160
  generated_at: "2026-08-06T19:30:59.482180Z"
  quality:
    source_chunks: 40
    aligned_chunks: 40
    alignment_items: 43435
    sentence_segments: 1158
    refined_segments: 1158
    rendered_blocks: 335
    rendered_lines: 1158
  performance:
    model_load_seconds: 1.804
    transcription_seconds: 326.152
    prompt_tokens: 125664
    generation_tokens: 28909
    prompt_tokens_per_second: 385.298
    generation_tokens_per_second: 88.638
    aligner_load_seconds: 0.242
    alignment_seconds: 69.871
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
    options:
      language: Chinese
      temperature: 0.0
      max_tokens_per_chunk: 4096
      chunk_duration_seconds: 240.0
      max_sentence_characters: 160
    generated_at: "2026-08-06T19:30:59.482180Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
    quality:
      source_chunks: 40
      aligned_chunks: 40
      alignment_items: 43435
      sentence_segments: 1158
      refined_segments: 1158
      rendered_blocks: 335
      rendered_lines: 1158
    performance:
      model_load_seconds: 1.804
      transcription_seconds: 326.152
      prompt_tokens: 125664
      generation_tokens: 28909
      prompt_tokens_per_second: 385.298
      generation_tokens_per_second: 88.638
      aligner_load_seconds: 0.242
      alignment_seconds: 69.871
local_audio_cache:
  path: .cache/media/whynottv/003-chen-tianqi/source.m4a
  metadata_path: .cache/media/whynottv/003-chen-tianqi/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-06T18:45:41.531825Z"
  verified_at: "2026-08-06T18:45:41.531825Z"
  extractor: BiliBili
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 188061042
  duration_ms: 9610346
  sha256: 8300b2b010882f85b6e8dbbdd213c68f55b89dc5a58f2d293e6752e0e045e9d8
last_verified_at: 2026-08-07
---

# 陈天奇 - XGBoost、TVM 与机器学习系统

## 单集信息

- 节目：WhynotTV Podcast（第 3 期）
- 主持人：何泰然
- 嘉宾：陈天奇，机器学习系统研究者、卡内基梅隆大学助理教授
- 发布时间：2025-09-12 22:11:25（UTC+8）
- 本地音频时长：02:40:10.346（AAC、48 kHz、双声道）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1s6pgzLE3y/)
- 字幕状态：匿名访问未发现公开字幕轨，播放器未提示需要登录
- 本地来源：独立音轨已下载，并通过媒体探测、时长、大小和 SHA-256 校验
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的结构化总结草稿](./summary.zh-CN.md)
- 处理状态：Qwen3-ASR 逐字稿与结构化总结草稿均已生成

## 内容概览

陈天奇沿着近二十年的机器学习系统研究经历，回顾 XGBoost、MXNet、TVM 和 MLC LLM 等项目为什么出现、如何发展，以及开源社区、研究判断和系统工程在这些项目中的作用。

访谈也讨论他从上海交大 ACM 班到华盛顿大学博士阶段的成长经历、创办 OctoML 的经验、回到学术界任教的选择，以及在快速变化的 AI 研究环境中如何坚持长期主义、问题导向和亲手写代码的工作方式。

## 发布者章节概览

发布者未提供平台章节标记。

## 核心议题

- XGBoost、MXNet、TVM 与 MLC LLM 的技术演进
- 机器学习系统研究的方法、工程约束与未来方向
- 开源项目的社区建设、专注与长期维护
- 从研究项目到 OctoML 创业的经验与反思
- 学术研究、产业实践和教授角色之间的选择
- 长期主义、失败经验与保持初心

## 待补充

- [x] 通过发布者 RSS 与标题核对正式期号
- [x] 核对 BVID、aid、cid 和 page
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取并验证本地独立音轨及来源 sidecar
- [x] 使用 Qwen3-ASR 与 ForcedAligner 生成机器逐字稿
- [x] 基于完整逐字稿完善结构化总结
- [ ] 校对专有名词、断句和说话人区分
- [ ] 核听关键片段并完成必要事实核查
- [ ] 将逐字稿和总结推进到人工审核状态

## ASR 运行记录

- 当前选中逐字稿：[Qwen3-ASR 版本](./transcript.zh-CN.md)
- 可追溯运行产物：[Qwen3-ASR run](./asr/qwen3-asr/transcript.zh-CN.md)
- 模型：`mlx-community/Qwen3-ASR-1.7B-8bit`
- 对齐器：`mlx-community/Qwen3-ForcedAligner-0.6B-8bit`
