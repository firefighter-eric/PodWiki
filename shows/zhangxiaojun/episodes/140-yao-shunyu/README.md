---
schema_version: 1
kind: episode
id: "zhangxiaojun:140"
show_id: zhangxiaojun
episode_key: "140"
episode_number: 140
slug: 140-yao-shunyu
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-05
  source: publisher-rss
title: "对姚顺宇的4小时访谈：请允许我小疯一下！在Anthropic和Gemini训模型、技术预测、英雄主义已过去"
published_at: "2026-05-11T08:00:00+08:00"
duration_ms: 13835000
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: yao-shunyu
    name: 姚顺宇
    aliases:
      - Shunyu Yao
    role: guest
sources:
  - platform: rss
    kind: feed-item
    url: https://www.xiaoyuzhoufm.com/episode/6a00aa051b7bd50295dfe41d
    preferred: false
    identifiers:
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 6a00aa051b7bd50295dfe41d
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1YR5E6EE9o/
    preferred: true
    identifiers:
      bvid: BV1YR5E6EE9o
      aid: "116551235669764"
      cid: "38242946885"
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
    sha256: e03d99a5c268b71c5749c7263e90eded038d35c2972b7e23d653028c87f0e9e4
transcript:
  path: transcript.zh-CN.md
  platform_subtitle_access: no-anonymous-track-login-indicated
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
  generated_at: "2026-08-06T04:02:32.189252Z"
  quality:
    source_chunks: 58
    aligned_chunks: 58
    alignment_items: 63545
    sentence_segments: 2067
    refined_segments: 2061
    rendered_blocks: 479
    rendered_lines: 2061
  performance:
    transcription_seconds: 495.064
    alignment_seconds: 97.538
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
    generated_at: "2026-08-06T04:02:32.189252Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/140-yao-shunyu/source.m4a
  metadata_path: .cache/media/zhangxiaojun/140-yao-shunyu/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-05T12:04:38.457056Z"
  verified_at: "2026-08-05T12:04:38.457056Z"
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 115870716
  duration_ms: 13680686
  sha256: 4cd0ade2bfe69491c29f8c979de99ecefa920c6e62a301cbbe931fa947f6a0ca
last_verified_at: 2026-08-06
---

# 对姚顺宇的 4 小时访谈：请允许我小疯一下

> 本页保留发布者简介与章节形成的结构化概览；另有依据完整机器逐字稿整理的总结草稿，尚未完成关键片段核听和独立事实核查。

## 单集信息

- 节目：张小珺商业访谈录 #140
- 主持人：张小珺
- 嘉宾：姚顺宇（Shunyu Yao），发布者介绍他先后在 Anthropic 与 Google DeepMind 担任研究科学家
- Bilibili 发布时间：2026-05-11 08:00（UTC+8）
- 官方 RSS 音频时长：03:50:35
- Bilibili 视频时长：03:48:01
- 本地 Bilibili 音轨：03:48:00.686（AAC、44.1 kHz、双声道），比 RSS 版本短约 2 分 34 秒
- RSS GUID：`6a00aa051b7bd50295dfe41d`
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/6a00aa051b7bd50295dfe41d)、[Bilibili 视频](https://www.bilibili.com/video/BV1YR5E6EE9o/)
- 字幕状态：匿名访问未发现公开独立字幕轨；平台 API 标记需要登录才能进一步检查，未使用 cookies 或登录态
- 本地来源：独立音轨已下载，并通过媒体探测、时长和 SHA-256 校验
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[核心观点与 5 分钟版](./summary.zh-CN.md)

## 内容概览

发布者介绍称，姚顺宇毕业于清华大学和斯坦福大学，早期研究理论物理，后来转向 AI，并在 Anthropic 与 Google DeepMind 参与模型研发。访谈从同名带来的话题、个人竞争观与研究转向谈起，逐步延伸到预训练、Coding、模型蒸馏和机器人等技术话题。

后半段按发布者章节梳理姚顺宇从非厄米系统、量子物理与高能物理转向 AI 的经历，以及在 Anthropic 和 Google DeepMind 的研发思考。访谈最后讨论技术预测、组织搭建，以及发布者所概括的“个人英雄主义时代已经过去”。

## 章节概览

> 以下时间码来自发布者 Bilibili 简介。

- 00:01:26 — 两个 Shunyu Yao
- 00:07:15 — 竞争与逃逸
- 00:25:22 — “Pre-train 没有到头”
- 00:35:08 — Coding 的爆发
- 00:50:10 — Seedance
- 00:54:30 — “硬蒸”和“软蒸”
- 01:04:07 — 机器人
- 01:08:45 — 在 Underdog 之地赌一把
- 01:19:44 — 非厄米系统与量子物理
- 01:36:27 — 高能物理
- 01:43:09 — 物理与 AI
- 01:52:32 — 在 Anthropic 训练 Claude 3.7 和 4.5
- 02:35:03 — “AI 本质是简单的”
- 02:41:10 — 在 Google DeepMind 训练 Gemini 3
- 03:01:28 — 技术预测和组织搭建
- 03:23:33 — 集体主义胜利

## 核心议题

- 从理论物理转向 AI 研究的经历与方法
- 预训练、Coding、蒸馏和机器人方向的判断
- Anthropic 与 Google DeepMind 模型研发经历
- AI 技术预测与研发组织搭建
- 个人英雄主义与集体协作在大模型研发中的关系

## 待补充

- [x] 通过发布者 RSS GUID 核对官方期号
- [x] 核对 Bilibili 视频的 aid、cid 和 page
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取独立音轨并完成编码、时长、大小和哈希校验
- [x] 使用 Qwen3-ASR 与 ForcedAligner 生成机器逐字稿
- [ ] 校对专有名词、断句和识别错误
- [ ] 增加主持人与嘉宾的说话人区分
- [x] 基于完整机器逐字稿生成总结草稿
- [ ] 核听总结引用的关键片段并完成必要事实核查
