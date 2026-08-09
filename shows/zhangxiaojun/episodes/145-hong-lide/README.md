---
schema_version: 1
kind: episode
id: "zhangxiaojun:145"
show_id: zhangxiaojun
episode_key: "145"
episode_number: 145
slug: 145-hong-lide
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-05
  source: publisher-rss
title: "口述SpaceX开发史：和前高管洪力德聊，马斯克用人观、最大IPO、太空与AI、人类文明扩张前奏？"
navigation_title: "洪力德 · SpaceX 开发史与工程组织"
catalog_keyword: "SpaceX"
published_at: "2026-06-12T20:52:25+08:00"
duration_ms: 10886000
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: hong-lide
    name: 洪力德
    aliases:
      - Lewis Hong
    role: guest
    profile:
      headline: "SpaceX 前火箭首席制造工程师"
      affiliations:
        - organization: "SpaceX"
          title: "火箭首席制造工程师"
          status: former
      checked_at: "2026-08-06"
sources:
  - platform: rss
    kind: feed-item
    url: https://www.xiaoyuzhoufm.com/episode/6a2be5da43a22a695582ad20
    preferred: false
    identifiers:
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 6a2be5da43a22a695582ad20
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1HfEy6jEUx/
    preferred: true
    identifiers:
      bvid: BV1HfEy6jEUx
      aid: "116737110510456"
      cid: "39103430670"
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
    path: asr/whisper/transcript.zh-CN.md
    engine: mlx-whisper
    model: mlx-community/whisper-large-v3-turbo-q4
    selection_status: superseded
    sha256: 8f144e97ae70c2e4d8bd754a5cb614ba18fa1cef50bf2ecf3e6deecc89ca657a
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
  generated_at: "2026-08-06T03:51:49.182609Z"
  quality:
    source_chunks: 45
    aligned_chunks: 45
    alignment_items: 48094
    sentence_segments: 1590
    refined_segments: 1587
    rendered_blocks: 368
    rendered_lines: 1587
  performance:
    transcription_seconds: 382.777
    alignment_seconds: 81.902
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
    generated_at: "2026-08-06T03:51:49.182609Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
  - id: whisper-large-v3-turbo-q4
    selection_status: superseded
    engine: mlx-whisper
    model: mlx-community/whisper-large-v3-turbo-q4
    artifacts:
      raw: asr/whisper/raw.json
      refined: asr/whisper/refined.json
      transcript: asr/whisper/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/145-hong-lide/source.m4a
  metadata_path: .cache/media/zhangxiaojun/145-hong-lide/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-05T12:00:03.597514Z"
  verified_at: "2026-08-05T12:00:03.597514Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 183554521
  duration_ms: 10803605
  sha256: 265c9fd3feda67252160fefc67ecfd56f6fd8d3c63439c1ca5793ae2b0edcd1a
last_verified_at: 2026-08-06
---

# 口述 SpaceX 开发史：和前高管洪力德聊

> 本页概览根据发布者 RSS 与 Bilibili 简介、章节整理；基于完整机器逐字稿生成的总结初稿单独保存在 [`summary.zh-CN.md`](./summary.zh-CN.md)。

## 单集信息

- 节目：张小珺商业访谈录 #145
- 主持人：张小珺
- 嘉宾：洪力德（Lewis Hong），SpaceX 前火箭首席制造工程师
- 发布者 RSS 时间：2026-06-12 19:18:46（UTC+8）
- Bilibili 发布时间：2026-06-12 20:52:25（UTC+8）
- 官方 RSS 音频时长：03:01:26
- Bilibili 本地音频时长：03:00:03.605
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/6a2be5da43a22a695582ad20)、[Bilibili 视频](https://www.bilibili.com/video/BV1HfEy6jEUx/)
- 字幕状态：匿名访问未发现公开独立字幕轨；平台 API 标记需要登录才能进一步检查，未使用 cookies 或登录态
- 本地来源：独立音轨已下载并通过媒体探测、时长和 SHA-256 校验
- 总结：[查看结构化总结初稿](./summary.zh-CN.md)
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)；尚未完成人工校对、说话人识别和事实核查

## 内容概览

发布者把本期定位为 SpaceX IPO 历史节点上的一集加更。张小珺邀请 SpaceX 前火箭首席制造工程师洪力德，从亲历者视角回顾 SpaceX 的开发史，并讨论 SpaceX 对 x.AI 的收购整合、IPO、太空与 AI 的融合，以及这些变化是否可能成为人类文明扩张的前奏。

访谈也涉及马斯克的性格与用人方式、SpaceX 内部的工作情况、人员去留、Falcon 9 的成败过程，以及航天产业中的参与者、产业格局与权力关系。

## 章节概览

> 以下时间码来自发布者 RSS 与 Bilibili 简介。

- 00:01:24 — SpaceX 的 IPO 与对 x.AI 的收购
- 00:31:30 — 极端内向的马斯克和用人观
- 01:03:42 — SpaceX 内部的真实情况
- 01:30:51 — “那我接受你的辞呈”
- 01:56:35 — SpaceX 开发史、Falcon 9 成与败
- 02:11:19 — 航天产业的地图与权力

## 核心议题

- SpaceX IPO 与整合 x.AI 的背景及可能影响
- 马斯克的性格、人才判断与组织管理方式
- SpaceX 内部研发和制造工作的真实情况
- Falcon 9 开发过程中的成功、失败与工程经验
- 航天产业的参与者、产业版图与权力结构
- 太空技术与 AI 融合对人类文明扩张的长期意义

## 待补充

- [x] 通过发布者 RSS GUID 核对官方期号
- [x] 核对 Bilibili 视频的 aid、cid 和 page
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取独立音轨并完成编码、时长、大小和哈希校验
- [x] 使用 Qwen3-ASR 与 ForcedAligner 生成机器逐字稿
- [ ] 校对专有名词、断句和识别错误
- [ ] 增加主持人与嘉宾的说话人区分
- [x] 基于完整机器逐字稿生成结构化总结初稿
- [ ] 核听总结引用的关键片段并校对专有名词
- [ ] 完成事实核查并将总结标记为 `reviewed`
