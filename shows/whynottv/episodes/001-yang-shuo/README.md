---
schema_version: 1
kind: episode
id: "whynottv:001"
show_id: whynottv
episode_key: "001"
episode_number: 1
slug: 001-yang-shuo
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-07
  source: publisher-rss
title: "杨硕：妙动科技，特斯拉Optimus，CMU，大疆，无人机，人形机器人｜WhynotTV Podcast #1"
navigation_title: "杨硕 - 妙动科技、Optimus 与人形机器人"
published_at: "2025-07-05T17:10:58+08:00"
duration_ms: 5381294
language: zh-CN
participants:
  - id: yang-shuo
    name: 杨硕
    role: guest
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1em3XznEFx/
    preferred: true
    identifiers:
      bvid: BV1em3XznEFx
      aid: "114799811757702"
      cid: "30864574379"
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
    sha256: 2f816ba886dc2fc0fc6c8f818e1d124286578d6db7d488effb21bed2d8387783
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
    max_sentence_characters: 160
  generated_at: "2026-08-06T19:16:13.106153Z"
  quality:
    source_chunks: 23
    aligned_chunks: 23
    alignment_items: 22998
    sentence_segments: 629
    refined_segments: 628
    rendered_blocks: 182
    rendered_lines: 628
  performance:
    model_load_seconds: 1.738
    transcription_seconds: 171.491
    prompt_tokens: 70369
    generation_tokens: 15244
    prompt_tokens_per_second: 410.349
    generation_tokens_per_second: 88.894
    aligner_load_seconds: 0.216
    alignment_seconds: 36.99
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
      temperature: 0
      max_tokens_per_chunk: 4096
      chunk_duration_seconds: 240
      max_sentence_characters: 160
    generated_at: "2026-08-06T19:16:13.106153Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
    quality:
      source_chunks: 23
      aligned_chunks: 23
      alignment_items: 22998
      sentence_segments: 629
      refined_segments: 628
      rendered_blocks: 182
      rendered_lines: 628
    performance:
      model_load_seconds: 1.738
      transcription_seconds: 171.491
      prompt_tokens: 70369
      generation_tokens: 15244
      prompt_tokens_per_second: 410.349
      generation_tokens_per_second: 88.894
      aligner_load_seconds: 0.216
      alignment_seconds: 36.99
    benchmark: docs/asr-benchmark.md
local_audio_cache:
  path: .cache/media/whynottv/001-yang-shuo/source.m4a
  metadata_path: .cache/media/whynottv/001-yang-shuo/source.metadata.json
  git_ignored: true
  extractor: BiliBili
  acquired_at: "2026-08-06T18:47:06.652457Z"
  verified_at: "2026-08-06T18:47:06.652457Z"
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 114561018
  duration_ms: 5381294
  sha256: 3c3efc127494f3ec8a2305f544f944283ac96a6bf3335bbc5d763a42b3c9c184
last_verified_at: 2026-08-07
---

# 杨硕 - 妙动科技、Optimus 与人形机器人

> 本页概览根据发布者公开简介整理；基于完整机器逐字稿生成的总结初稿单独保存在 [`summary.zh-CN.md`](./summary.zh-CN.md)。

## 单集信息

- 节目：WhynotTV Podcast（第 1 期）
- 嘉宾：杨硕，妙动科技创始人
- 发布时间：2025-07-05 17:10:58（UTC+8）
- 时长：01:29:42
- 来源：[节目发布页](https://www.bilibili.com/video/BV1em3XznEFx/)
- 总结：[查看结构化总结初稿](./summary.zh-CN.md)
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 字幕状态：匿名访问未发现独立公开字幕轨；平台提示登录后可能存在字幕
- 本地来源：音轨及来源 sidecar 已获取，并通过时长、文件大小与 SHA-256 校验
- 处理状态：Qwen3-ASR 逐字稿与结构化总结初稿已生成，尚待人工核听和校对

## 内容概览

本期回顾杨硕从无人机飞控到足式机器人和人形机器人的技术经历。发布者简介串联了他在香港科技大学参与大疆飞控系统研发、前往 CMU 攻读机器人博士，以及加入特斯拉 Optimus 团队从事人形机器人工作的职业路径。

对话也聚焦他离开特斯拉创立妙动科技的选择，讨论机器人状态估计与控制、消费级机器人产品的工程目标，以及长期一线研发经验如何影响对人形机器人产业机会的判断。

## 章节概览

发布页未提供独立章节。

## 核心议题

- 无人机飞控研发与机器人控制经验
- CMU 足式机器人研究及状态估计问题
- 特斯拉 Optimus 团队的人形机器人实践
- 从大型工程团队走向机器人创业的选择
- 消费级机器人产品的技术与落地路径

## 待补充

- [x] 核对发布者正式期号、规范来源和平台标识符
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取并验证本地独立音轨及来源 sidecar
- [x] 使用 Qwen3-ASR 与 ForcedAligner 生成机器逐字稿
- [x] 基于完整逐字稿形成独立总结初稿
- [ ] 校对专有名词、断句和说话人区分
- [ ] 核听总结引用的关键片段并完成必要事实核查
- [ ] 将逐字稿和总结推进到人工审核状态

## ASR 运行记录

- 当前选中逐字稿：[Qwen3-ASR 版本](./transcript.zh-CN.md)
- 可追溯运行产物：[Qwen3-ASR run](./asr/qwen3-asr/transcript.zh-CN.md)
- 模型：`mlx-community/Qwen3-ASR-1.7B-8bit`
- 对齐器：`mlx-community/Qwen3-ForcedAligner-0.6B-8bit`
