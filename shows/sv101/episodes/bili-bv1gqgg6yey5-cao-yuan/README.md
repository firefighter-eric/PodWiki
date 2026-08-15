---
schema_version: 1
kind: episode
id: "sv101:bili-bv1gqgg6yey5"
show_id: sv101
episode_key: bili-bv1gqgg6yey5
episode_number: null
slug: bili-bv1gqgg6yey5-cao-yuan
release_type: special
numbering:
  status: not-in-publisher-feed
  checked_at: 2026-08-15
  source: publisher-bilibili-video
  note: "发布者在 Bilibili 将该视频标为 101视频播客；未依据标题推断硅谷101官方 RSS 的正式期号，因此保留 episode_number: null"
title: "对话前DeepMind曹原：AI for Science爆发，一个新时代到来了【101视频播客】"
navigation_title: "曹原 · AI for Science 与科学发现"
catalog_keyword: "AI for Science"
published_at: "2026-08-15T11:53:42+08:00"
duration_ms: 6561173
language: zh-CN
participants:
  - id: cao-yuan
    name: 曹原
    role: guest
    profile:
      headline: "前 Google DeepMind 资深研究科学家"
      affiliations:
        - organization: "Google DeepMind"
          title: "资深研究科学家"
          status: former
      checked_at: 2026-08-15
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1GQgg6yEy5/
    preferred: true
    identifiers:
      bvid: BV1GQgg6yEy5
      aid: "117097485113167"
      cid: "40925595176"
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
    sha256: cb9e784c8069575cb582e66cf2f7637410172a23f0d1c0daff30d208b8fd4209
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
    planned_chunk_count: 28
    effective_total_token_budget: 114688
    max_sentence_characters: 160
  generated_at: "2026-08-15T09:55:27.605992Z"
  quality:
    source_chunks: 28
    aligned_chunks: 28
    alignment_items: 39276
    sentence_segments: 941
    refined_segments: 941
    rendered_blocks: 222
    rendered_lines: 941
  performance:
    model_load_seconds: 0.327
    transcription_seconds: 280.678
    prompt_tokens: 85801
    generation_tokens: 25758
    prompt_tokens_per_second: 305.692
    generation_tokens_per_second: 91.771
    aligner_load_seconds: 0.224
    alignment_seconds: 42.218
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
    generated_at: "2026-08-15T09:55:27.605992Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/sv101/bili-bv1gqgg6yey5-cao-yuan/source.m4a
  metadata_path: .cache/media/sv101/bili-bv1gqgg6yey5-cao-yuan/source.metadata.json
  git_ignored: true
  extractor: BiliBili
  acquired_at: "2026-08-15T09:46:57.665501Z"
  verified_at: "2026-08-15T09:46:57.665501Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 101790602
  duration_ms: 6561173
  sha256: f46cdefbfb6264c992b8cd42d82d0d10921cf4e47fd95e28ac535f90f24120a4
last_verified_at: 2026-08-15
---

# 对话前DeepMind曹原：AI for Science爆发，一个新时代到来了【101视频播客】

> 本页保留硅谷101的 Bilibili 发布者简介与平台章节，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；专有名词、数字、引文与嘉宾归属均须人工核听后才能提升状态。

## 单集信息

- 节目：硅谷101，101视频播客
- 嘉宾：曹原；发布者介绍为前 Google DeepMind 资深研究科学家
- 发布时间：2026-08-15 11:53:42（UTC+8）
- Bilibili 标示时长：01:49:22
- 本地 Bilibili 音轨：01:49:21.173（AAC、48 kHz、双声道）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1GQgg6yEy5/)
- 编号状态：Bilibili 以“101视频播客”标识该完整对话；未从该标识推断硅谷101官方 RSS 的期号，因此保留 `episode_number: null`
- 字幕状态：匿名元数据没有列出公开字幕轨，且提示字幕查询需要登录；处理未使用 cookies 或登录态
- 本地来源：音轨已通过媒体探测、时长、文件大小和 SHA-256 校验
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 处理状态：机器逐字稿与总结草稿均已生成，尚未核听或完成人工审核

## 内容概览

发布者将本期定位为一场关于 AI for Science 的对话：围绕 Jeff Dean 离开 Google 创办 Discovery Loop 的背景，讨论 AI for Science、AI for AI 与 RSI 的关系，以及从数学、代码、生物、材料到物理的科研闭环。节目中的机构动态、产品能力和时间判断均按主持人与嘉宾陈述保留；基于完整机器稿的独立梳理、原文定位与事实边界见[总结草稿](./summary.zh-CN.md)。

## 章节概览

> 以下时间范围与标题来自 Bilibili 发布者章节。

- 00:00:00–00:15:02 — 出走谷歌
- 00:15:02–00:24:58 — AI4S爆发
- 00:24:58–00:30:59 — 问题定义
- 00:30:59–00:42:59 — AI做科研
- 00:42:59–00:52:22 — “真正发现”
- 00:52:22–01:04:03 — 符号主义
- 01:04:03–01:11:17 — 巨头押注
- 01:11:17–01:32:05 — “数学边界”
- 01:32:05–01:38:45 — 物理
- 01:38:45–01:49:21 — 商业化与哲学

## 核心议题

- Jeff Dean 离开 Google 与 AI for Science 的组织背景
- AI for Science、AI for AI 与 RSI 的关系
- 科学发现、实验验证与反馈速度
- 符号主义与连接主义的结合
- AI 在数学、代码、生物、材料与物理中的边界
