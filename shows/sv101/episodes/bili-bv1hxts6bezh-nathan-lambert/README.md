---
schema_version: 1
kind: episode
id: "sv101:bili-bv1hxts6bezh"
show_id: sv101
episode_key: bili-bv1hxts6bezh
episode_number: null
slug: bili-bv1hxts6bezh-nathan-lambert
release_type: special
numbering:
  status: not-in-publisher-feed
  checked_at: 2026-08-07
  source: publisher-rss-checked
  url: https://feeds.fireside.fm/sv101/rss
  note: "硅谷101官方 RSS 未收录与该发布者视频对应的单集，无法核实或推导正式期号"
title: "美国AI研究员的中国之旅：年轻人，追赶者，算力焦虑与“AGI展示厅” ｜专访Nathan Lambert【101视频播客】"
navigation_title: "Nathan Lambert - 中国 AI 生态、开源模型与算力焦虑"
published_at: "2026-07-03T14:10:30+08:00"
duration_ms: 5225163
language: en
participants:
  - id: nathan-lambert
    name: Nathan Lambert
    role: guest
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1HXTs6bEzH/
    preferred: true
    identifiers:
      bvid: BV1HXTs6bEzH
      aid: "116854534184366"
      cid: "39628246380"
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
    path: transcript.en.md
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    selection_status: selected
    sha256: 1763e9c31545b747d157da73136eea35bec62a5982223072019f41b54744b4ab
transcript:
  path: transcript.en.md
  platform_subtitle_access: no-anonymous-track-login-indicated
  platform_subtitle_languages: []
  automatic_caption_languages: []
  translations:
    - language: zh-CN
      path: transcript.zh-CN.md
      source_language: en
      source_path: transcript.en.md
      alignment: segment
      status: edited
      generated_at: "2026-08-06T20:46:04Z"
      source_sha256: 1763e9c31545b747d157da73136eea35bec62a5982223072019f41b54744b4ab
      sha256: 6636adba493bd56c0ea0323ca95ab63442dae9d371ba36a87274eec5811e2770
  acquisition_method: audio-asr
  asr_script: scripts/transcribe_qwen3_asr.py
  engine: mlx-audio
  model: mlx-community/Qwen3-ASR-1.7B-8bit
  aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
  options:
    language: English
    temperature: 0.0
    max_tokens_per_chunk: 4096
    chunk_duration_seconds: 60.0
    max_sentence_characters: 160
  generated_at: "2026-08-06T20:32:07.814206Z"
  quality:
    source_chunks: 87
    aligned_chunks: 87
    alignment_items: 17530
    sentence_segments: 1136
    refined_segments: 1135
    rendered_blocks: 447
    rendered_lines: 1135
  performance:
    model_load_seconds: 2.557
    transcription_seconds: 187.88
    prompt_tokens: 69510
    generation_tokens: 20850
    prompt_tokens_per_second: 369.984
    generation_tokens_per_second: 110.979
    aligner_load_seconds: 0.218
    alignment_seconds: 22.3
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
    path: asr/qwen3-asr/transcript.en.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
  renderer: scripts/render_asr_transcript.py
asr_runs:
  - id: qwen3-asr-1.7b-8bit
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    generated_at: "2026-08-06T20:32:07.814206Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.en.md
local_audio_cache:
  path: .cache/media/sv101/bili-bv1hxts6bezh-nathan-lambert/source.m4a
  metadata_path: .cache/media/sv101/bili-bv1hxts6bezh-nathan-lambert/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-06T18:50:52.918456Z"
  verified_at: "2026-08-06T18:50:52.918456Z"
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 51002151
  duration_ms: 5225163
  sha256: 2dc196954d1038655a8c4786f5c38128115333523abb761d2cad590c64bbc4a1
last_verified_at: 2026-08-07
---

# Nathan Lambert - 中国 AI 生态、开源模型与算力焦虑

## 单集信息

- 节目：硅谷101（官方 RSS 未收录对应单集，正式期号未核实）
- 嘉宾：Nathan Lambert，艾伦人工智能研究所（Ai2）后训练负责人
- 发布时间：2026-07-03 14:10:30（UTC+8）
- 主要语言：英语
- 本地音频时长：01:27:05.163（AAC、44.1 kHz、双声道）
- 来源：[发布者视频](https://www.bilibili.com/video/BV1HXTs6bEzH/)
- 字幕状态：匿名访问未发现公开字幕轨；播放器提示登录后可能存在字幕
- 本地来源：独立音轨已下载，并通过媒体探测、时长、大小和 SHA-256 校验
- 英文逐字稿：[Qwen3-ASR 机器初稿](./transcript.en.md)
- 中文逐字稿：[逐段对齐的机器译稿](./transcript.zh-CN.md)（已做初步专名编辑，尚未逐段人工审核）
- 中文总结：[基于完整英文机器稿的总结草稿](./summary.zh-CN.md)
- 处理状态：英文机器逐字稿、经初步专名编辑的逐段中文机器译稿与中文总结草稿均已生成；音频尚未核听，英文识别和中文翻译均未完成逐段人工审核

## 内容概览

Nathan Lambert 回顾 2026 年 4 月访问中国 AI 团队的经历。行程覆盖阿里巴巴、月之暗面、智谱、清华、美团、小米、蚂蚁和零一万物；节目借这些现场观察讨论中国模型团队的组织方式、工程文化与产业生态。

对话把年轻人才、追赶者心态、开放模型、超级 App、算力约束、数据产业和产品闭环放在同一框架中比较。核心问题包括中美 AI 圈为何呈现不同的焦虑、中国公司为何普遍希望拥有自己的模型，以及开放模型如何成为中国 AI 进入全球开发者社区的重要路径。

基于完整英文机器稿的中文梳理、原文定位与事实边界见[总结草稿](./summary.zh-CN.md)。

## 发布者章节概览

- 00:00:00 — Nathan 的中国 AI 行
- 00:12:04 — Kimi
- 00:16:42 — 智谱
- 00:20:03 — 美团 / 小米
- 00:26:59 — 阿里 / 01.AI
- 00:38:47 — 开源模型之战
- 00:44:20 — 组织架构、追赶者
- 00:56:35 — 国产芯片与算力焦虑
- 01:11:35 — 数据弱点
- 01:16:21 — 全球 AI 竞赛

## 核心议题

- 中国 AI 实验室的组织、工程文化与年轻人才
- 月之暗面、智谱、美团、小米、阿里和零一万物的观察
- 开放模型与全球开发者生态的连接方式
- 中美 AI 团队不同的竞争压力与追赶者心态
- 国产芯片、算力约束和数据产业的现实边界
- 产品闭环、真实用户反馈与全球 AI 竞赛

## 待补充

- [x] 核对规范来源、发布账号、BVID、aid、cid 和 page
- [x] 核对硅谷101官方 RSS，确认未收录对应单集
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取并验证本地独立音轨及来源 sidecar
- [x] 使用 Qwen3-ASR 与 ForcedAligner 生成 1135 段英文机器逐字稿，并保留原始、对齐、精炼与渲染产物
- [x] 生成与英文稿 1135 个 segment 逐段对齐的中文机器译稿，并完成初步专名编辑
- [x] 基于完整英文机器逐字稿完善结构化中文总结并核验时间码
- [ ] 校对专有名词、断句和说话人区分
- [ ] 逐段人工审核中文机器译稿，不以当前译稿替代英文源稿
- [ ] 核听关键片段并核查高影响外部事实
