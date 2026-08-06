---
schema_version: 1
kind: episode
id: "sv101:bili-bv1dy7c6newm"
show_id: sv101
episode_key: bili-bv1dy7c6newm
episode_number: null
slug: bili-bv1dy7c6newm-tian-yuandong
release_type: special
numbering:
  status: not-in-publisher-feed
  checked_at: 2026-08-06
  source: publisher-rss
  note: "截至 2026-08-06，发布者官方 RSS 未收录这条 2026 年 Bilibili 新视频；RSS 中 2024 年的 E145 是另一场更早的田渊栋访谈，不能为本集复用该编号"
title: "再访田渊栋：46.5亿美金估值的RSI，与AI自进化｜Neolabs特辑【101视频播客】"
published_at: "2026-06-05T17:03:28+08:00"
duration_ms: 5545366
language: zh-CN
participants:
  - id: tian-yuandong
    name: 田渊栋
    role: guest
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1DY7C6nEWM/
    preferred: true
    identifiers:
      bvid: BV1DY7C6nEWM
      aid: "116696660579481"
      cid: "38876350988"
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
    sha256: 92f612a7a568307c9f242f08ace1f8238b181560b30fe43f0fd4f515c8b2b368
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
  generated_at: "2026-08-06T16:04:32.011652Z"
  quality:
    source_chunks: 24
    aligned_chunks: 24
    alignment_items: 30536
    sentence_segments: 843
    refined_segments: 843
    rendered_blocks: 190
    rendered_lines: 843
  performance:
    model_load_seconds: 1.95
    transcription_seconds: 216.583
    prompt_tokens: 72527
    generation_tokens: 20798
    prompt_tokens_per_second: 334.876
    generation_tokens_per_second: 96.03
    aligner_load_seconds: 0.217
    alignment_seconds: 41.158
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
    generated_at: "2026-08-06T16:04:32.011652Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/sv101/bili-bv1dy7c6newm-tian-yuandong/source.m4a
  metadata_path: .cache/media/sv101/bili-bv1dy7c6newm-tian-yuandong/source.metadata.json
  git_ignored: true
  extractor: BiliBili
  acquired_at: "2026-08-06T15:40:08.895834Z"
  verified_at: "2026-08-06T15:40:08.895834Z"
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 70582412
  duration_ms: 5545366
  sha256: c7215e750f6fde1956e13fc91e1a747ec85bfcf2b07f1fad587538b708a5585a
last_verified_at: 2026-08-07
---

# 再访田渊栋：46.5亿美金估值的RSI，与AI自进化｜Neolabs特辑【101视频播客】

> 本页保留 Bilibili 发布者简介与平台章节，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；音频和总结均未完成人工审核，简介中的机构、估值与行业判断也尚未独立核查。

## 单集信息

- 节目：硅谷101（Neolabs 特辑）
- 嘉宾：田渊栋，Recursive Superintelligence 联合创始人、前 Meta 基础 AI 研究（FAIR）团队研究总监（身份来自发布者简介）
- 发布时间：2026-06-05 17:03:28（UTC+8）
- Bilibili 平台整秒时长：01:32:26
- 本地 Bilibili 音轨：01:32:25.366（AAC、44.1 kHz、双声道）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1DY7C6nEWM/)
- 编号状态：截至 2026-08-06，发布者官方 RSS 未收录这条 2026 年新视频；RSS 中 2024 年的 E145 是另一场更早的田渊栋访谈，不能为本集复用该编号，因此保留 `episode_number: null`
- 字幕状态：匿名 view/player 元数据未列出公开字幕轨；sidecar 同时标记字幕查询需要登录。这里只能确认“未发现匿名公开字幕轨”，不能据此排除登录可见字幕或画面硬字幕
- 获取方式：项目脚本使用 yt-dlp 的 BiliBili extractor 获取公开音轨；未使用 cookies 或登录态
- 本地来源：音轨已通过媒体探测、时长、大小和 SHA-256 校验
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，尚未核听或完成人工审核

## 内容概览

发布者简介以 Recursive Self-Improvement（递归自我改进）为背景，称这一方向关注 AI 系统在较少人类干预下设计和改进自身的能力，并把 Recursive Superintelligence（RSI）描述为押注这一方向的新实验室。标题和简介中的估值、机构定位及相关行业判断均为发布者表述，尚未独立核查。

本期是发布者与田渊栋相隔约半年的再次对话。简介称，讨论从他加入 RSI 的选择出发，延伸至递归自我改进、可解释性、研究路线与商业化，以及前沿模型竞争中模型、数据和组织效率各自扮演的角色。

后半部分也涉及 Neolab 生态与 AI 时代的职业处境。发布者用“大厂之间跳动的鱼缸”与“四维生物”等比喻概括节目关于组织变化、个人适应和意义感的讨论。本节保留发布者简介与章节所覆盖的议题轮廓；基于完整机器稿的独立梳理、原文定位和事实边界见[总结草稿](./summary.zh-CN.md)。

## 章节概览

> 以下章节标题和边界来自 Bilibili 平台章节。

- 00:00:00–00:05:45 — 加入RSI
- 00:05:45–00:14:03 — 8位联创
- 00:14:03–00:19:38 — 递归
- 00:19:38–00:25:32 — 可解释性
- 00:25:32–00:38:04 — 研究路线与商业化
- 00:38:04–00:42:36 — RSI最好的时机
- 00:42:36–00:57:22 — Neolab生态现状
- 00:57:22–01:18:38 — 前沿模型竞争与下一步
- 01:18:38–01:29:28 — 员工蒸馏
- 01:29:28–01:32:25 — 彩蛋

## 核心议题

- 田渊栋加入 RSI 的选择与八位联合创始人的组织背景
- Recursive Self-Improvement 的研究目标与技术路径
- 可解释性在递归改进系统中的作用
- 研究路线、商业化与实验室成立时机
- Neolab 生态及前沿 AI 实验室的竞争格局
- 模型、数据、研究能力和组织效率之间的关系
- “员工蒸馏”背景下个人职业位置与适应方式
- AI 时代如何理解个人意义与长期选择

## 待补充

- [x] 核对 Bilibili 视频的 BVID、aid、cid 和 page
- [x] 检查匿名访问可见的平台字幕轨并记录边界
- [x] 获取独立音轨并完成编码、时长、大小和哈希校验
- [x] 生成 Qwen3-ASR 机器逐字稿并保留原始、对齐、精炼与渲染产物
- [x] 基于完整机器逐字稿形成独立总结草稿并核验时间码存在性
- [ ] 核听总结引用的关键片段并完成人工内容审核
- [ ] 校对专有名词、断句及主持人与嘉宾的说话人区分
- [ ] 独立核查 RSI 估值、机构背景及简介提及的外部事实
