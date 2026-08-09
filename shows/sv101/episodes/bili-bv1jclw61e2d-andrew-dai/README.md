---
schema_version: 1
kind: episode
id: "sv101:bili-bv1jclw61e2d"
show_id: sv101
episode_key: bili-bv1jclw61e2d
episode_number: null
slug: bili-bv1jclw61e2d-andrew-dai
release_type: special
numbering:
  status: not-in-publisher-feed
  checked_at: 2026-08-06
  source: publisher-rss
  note: "硅谷101官方 RSS 未收录与该 Bilibili 视频对应的单集；发布者称其为 Neolabs 特辑第一期，但不能据此推导硅谷101全节目正式期号"
title: "“谷歌太慢了”：与Andrew Dai聊Gemini的翻身之战，出走与视觉理解模型【硅谷101视频播客】"
navigation_title: "Andrew Dai · Gemini 追赶与视觉推理创业"
catalog_keyword: "Gemini"
published_at: "2026-05-19T11:00:00+08:00"
duration_ms: 3816512
language: zh-CN
participants:
  - id: andrew-dai
    name: Andrew Dai
    role: guest
    profile:
      headline: "Elorian AI 联合创始人兼 CEO、前 Google DeepMind 研究总监"
      affiliations:
        - organization: "Elorian AI"
          title: "联合创始人兼 CEO"
          status: current
        - organization: "Google DeepMind"
          title: "研究总监"
          status: former
      checked_at: "2026-08-07"
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1JCLw61E2d/
    preferred: true
    identifiers:
      bvid: BV1JCLw61E2d
      aid: "116594923540687"
      cid: "38436406094"
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
    sha256: f4b6b99e2987c1b9db59b87cd11533cbbff960f008db8127030f4d2ae6e88545
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
  generated_at: "2026-08-06T16:13:47.033092Z"
  quality:
    source_chunks: 16
    aligned_chunks: 16
    alignment_items: 18160
    sentence_segments: 548
    refined_segments: 548
    rendered_blocks: 131
    rendered_lines: 548
  performance:
    model_load_seconds: 1.645
    transcription_seconds: 136.404
    prompt_tokens: 49904
    generation_tokens: 12989
    prompt_tokens_per_second: 365.863
    generation_tokens_per_second: 95.227
    aligner_load_seconds: 0.168
    alignment_seconds: 25.458
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
    generated_at: "2026-08-06T16:13:47.033092Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/sv101/bili-bv1jclw61e2d-andrew-dai/source.m4a
  metadata_path: .cache/media/sv101/bili-bv1jclw61e2d-andrew-dai/source.metadata.json
  git_ignored: true
  extractor: BiliBili
  acquired_at: "2026-08-06T15:40:12.023144Z"
  verified_at: "2026-08-06T15:40:12.023144Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 67488631
  duration_ms: 3816512
  sha256: 692b36e77e20670375ad99fc9bbc1f79a4ba8a917813a64082e45c5ea08dc2ee
last_verified_at: 2026-08-07
---

# “谷歌太慢了”：与Andrew Dai聊Gemini的翻身之战，出走与视觉理解模型【硅谷101视频播客】

> 本页保留 Bilibili 发布者简介与平台章节，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；关键片段尚未核听，专有名词、数字、说话人归属与外部事实也尚未完成人工校对或独立核查。

## 单集信息

- 节目：硅谷101，Neolabs 特辑
- 嘉宾：Andrew Dai，发布者介绍为 Elorian AI 联合创始人兼 CEO、前 Google DeepMind 研究总监
- 发布时间：2026-05-19 11:00:00（UTC+8）
- Bilibili 标示时长：01:03:37
- 本地 Bilibili 音轨：01:03:36.512（AAC、48 kHz、双声道）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1JCLw61E2d/)
- 编号状态：截至 2026-08-06，硅谷101官方 RSS 未收录与该 Bilibili 视频对应的单集；发布者称其为 Neolabs 特辑第一期，但不能据此推导全节目正式期号，因此保留 `episode_number: null`
- 字幕状态：匿名访问未发现独立公开字幕轨；平台字幕检查提示登录后可能存在字幕，处理过程中未使用 cookies 或登录态
- 本地来源：音轨已获取，并通过独立 ffprobe、文件大小和 SHA-256 校验
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 处理状态：机器逐字稿与总结草稿均已生成，尚未核听或完成人工审核

## 内容概览

发布者简介以 Andrew Dai 在 Google 的十四年经历为主线，回顾他参与 Google Brain 与 DeepMind 研究项目期间接触的序列学习、文本生成、对抗训练、MoE、PaLM、Flan、Gemini、多模态和长上下文等方向。简介将这段经历放入 Google 在生成式 AI 浪潮中错过、追赶并重新建立竞争力的过程里讨论。

发布者还介绍了 Andrew Dai 离开 Google 后创办 Elorian AI 的选择，并把他关注的语言与视觉推理结合路线置于 Neolabs 特辑的背景中。融资规模、合作人物及其他外部事实目前均只作为发布者陈述记录，尚未独立核查。基于完整机器稿的独立梳理、原文定位与事实边界见[总结草稿](./summary.zh-CN.md)。

## 章节概览

> 以下时间范围和标题来自 Bilibili 发布者章节。

- 00:00:00–00:05:35 — 一位谷歌AI核心科学家的14年
- 00:05:35–00:09:34 — 从伦敦到硅谷
- 00:09:34–00:15:54 — 谷歌错过的“GPT时刻”
- 00:15:54–00:18:05 — 谷歌健康
- 00:18:05–00:25:55 — MoE架构
- 00:25:55–00:29:02 — 拉响红色警报
- 00:29:02–00:37:51 — Gemini 1.0-3.0
- 00:37:51–00:52:27 — Neolab爆发
- 00:52:27–00:58:06 — “最重要的资源是时间”
- 00:58:06–01:03:37 — 彩蛋：office tour

## 核心议题

- Andrew Dai 在 Google Brain 与 DeepMind 的研究经历
- Google 在生成式 AI 与 Gemini 演进中的组织和技术转折
- 序列学习、MoE、多模态与长上下文等技术方向
- 大型科技公司与新型前沿 AI 实验室的路线差异
- 语言模型、视觉理解和视觉推理之间的关系
- 科研人员离开大公司创业时对时间与研究路径的取舍

## 待补充

- [x] 核对 Bilibili 视频的规范 URL、BVID、aid、cid 和 page
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取并独立验证本地音轨、来源 sidecar、大小和 SHA-256
- [x] 核对发布者官方 RSS，确认未收录对应视频，无法推导正式期号
- [x] 生成完整 Qwen3-ASR 机器逐字稿并保留原始、对齐、精炼与渲染产物
- [x] 基于完整机器逐字稿撰写独立总结草稿并核验时间码存在性
- [ ] 校对专有名词、断句及主持人与嘉宾的说话人区分
- [ ] 核听关键片段并核查高影响外部事实
