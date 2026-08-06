---
schema_version: 1
kind: episode
id: "whynottv:005"
show_id: whynottv
episode_key: "005"
episode_number: 5
slug: 005-xu-danfei
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-07
  source: publisher-rss
title: "Danfei Xu：人类数据，行为克隆，机器人GPT-3，全栈，EgoMimic，遥操作，UMI，斯坦福 | WhynotTV Podcast #5"
navigation_title: "徐丹飞 - 人类数据、行为克隆与机器人学习"
published_at: "2026-05-01T19:46:59+08:00"
duration_ms: 8243541
language: zh-CN
participants:
  - id: xu-danfei
    name: 徐丹飞
    role: guest
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1usRgBEESe/
    preferred: true
    identifiers:
      bvid: BV1usRgBEESe
      aid: "116499075303246"
      cid: "38008982505"
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
    sha256: f7c65735ed89679ed34bebf15d85165bd247cc6a1a719a14c17c7120f09ace93
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
    temperature: 0.0
    max_tokens_per_chunk: 4096
    chunk_duration_seconds: 240.0
    max_sentence_characters: 160
  generated_at: "2026-08-06T19:37:15.891968Z"
  quality:
    source_chunks: 35
    aligned_chunks: 35
    alignment_items: 37326
    sentence_segments: 1037
    refined_segments: 1037
    rendered_blocks: 302
    rendered_lines: 1037
  performance:
    model_load_seconds: 1.81
    transcription_seconds: 300.92
    prompt_tokens: 107800
    generation_tokens: 26954
    prompt_tokens_per_second: 358.24
    generation_tokens_per_second: 89.573
    aligner_load_seconds: 0.213
    alignment_seconds: 59.284
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
    generated_at: "2026-08-06T19:37:15.891968Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
    quality:
      source_chunks: 35
      aligned_chunks: 35
      alignment_items: 37326
      sentence_segments: 1037
      refined_segments: 1037
      rendered_blocks: 302
      rendered_lines: 1037
    performance:
      model_load_seconds: 1.81
      transcription_seconds: 300.92
      prompt_tokens: 107800
      generation_tokens: 26954
      prompt_tokens_per_second: 358.24
      generation_tokens_per_second: 89.573
      aligner_load_seconds: 0.213
      alignment_seconds: 59.284
local_audio_cache:
  path: .cache/media/whynottv/005-xu-danfei/source.m4a
  metadata_path: .cache/media/whynottv/005-xu-danfei/source.metadata.json
  git_ignored: true
  extractor: BiliBili
  acquired_at: "2026-08-06T18:46:01.935600Z"
  verified_at: "2026-08-06T18:46:01.935600Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 116795080
  duration_ms: 8243541
  sha256: 7185306d61873c103df65f5804e207558df6f0a4f917f4e1ffed754a53791c53
last_verified_at: 2026-08-07
---

# 徐丹飞 - 人类数据、行为克隆与机器人学习

## 单集信息

- 节目：WhynotTV Podcast（第 5 期）
- 嘉宾：徐丹飞（Danfei Xu），机器人学者
- 发布时间：2026-05-01 19:46:59（UTC+8）
- 时长：02:17:24
- 来源：[节目发布页](https://www.bilibili.com/video/BV1usRgBEESe/)
- 字幕状态：匿名访问未发现独立公开字幕轨；平台提示登录后可能存在字幕
- 本地来源：音轨及来源 sidecar 已获取，并通过时长、文件大小与 SHA-256 校验
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的结构化总结草稿](./summary.zh-CN.md)
- 处理状态：Qwen3-ASR 逐字稿与结构化总结草稿均已生成

## 内容概览

本期从徐丹飞的机器人学习经历切入，讨论人类在物理世界中的动作数据能否成为机器人学习的基础燃料。发布者简介串联了行为克隆、第一人称数据、EgoMimic、遥操作与 UMI 等技术路线，并延伸到触觉、灵巧手、人形机器人和全栈机器人系统的关系。

对话也回顾徐丹飞从早期动手机器人项目、斯坦福机器人学习研究到建立完整研究系统的过程，关注机器人智能如何从人的操作、身体运动和交互中学习，以及学术界如何建设开放的人类数据基础设施。

## 章节概览

发布页未提供独立章节。

## 核心议题

- 人类数据与机器人数据的边界及互补关系
- 行为克隆从模型方法走向完整系统时的关键难点
- 第一人称视频、遥操作、UMI 与 EgoMimic 的数据价值
- 触觉、灵巧手和人形机器人对数据迁移的影响
- 全栈机器人研究与开放数据基础设施

## 待补充

- [x] 核对发布者正式期号、规范来源和平台标识符
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取并验证本地独立音轨及来源 sidecar
- [x] 使用 Qwen3-ASR 与 ForcedAligner 生成机器逐字稿
- [x] 基于完整逐字稿形成独立总结
- [ ] 校对专有名词、断句和说话人区分
- [ ] 核听关键片段并完成必要事实核查
- [ ] 将逐字稿和总结推进到人工审核状态

## ASR 运行记录

- 当前选中逐字稿：[Qwen3-ASR 版本](./transcript.zh-CN.md)
- 可追溯运行产物：[Qwen3-ASR run](./asr/qwen3-asr/transcript.zh-CN.md)
- 模型：`mlx-community/Qwen3-ASR-1.7B-8bit`
- 对齐器：`mlx-community/Qwen3-ForcedAligner-0.6B-8bit`
