---
schema_version: 1
kind: episode
id: "zhangxiaojun:bili-bv1nb3u6teru"
show_id: zhangxiaojun
episode_key: bili-bv1nb3u6teru
episode_number: null
slug: bili-bv1nb3u6teru-liao-heng
release_type: special
numbering:
  status: not-in-publisher-feed
  checked_at: 2026-08-05
  source: publisher-rss
  note: "截至核验日期未出现在发布者 RSS/feed 中，且无 RSS GUID；不推导正式期号"
title: "对华为半导体首席科学家廖恒的5小时访谈：一部昇腾史、18层宝塔与全球芯片恢弘30年史诗| B站 x WAIC AI会客厅"
navigation_title: "廖恒 · 芯片产业周期与昇腾工程史"
catalog_keyword: "昇腾"
published_at: "2026-07-25T21:19:38+08:00"
duration_ms: 16671403
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: liao-heng
    name: 廖恒
    role: guest
    profile:
      headline: "华为 Fellow、半导体首席科学家"
      affiliations:
        - organization: "华为"
          title: "Fellow、半导体首席科学家"
          status: current
      checked_at: "2026-08-06"
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1nB3u6tERu/
    preferred: true
    identifiers:
      bvid: BV1nB3u6tERu
      aid: "116980698843032"
      cid: "40282095854"
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
    sha256: 1eb7a8b999074813d680df2e8334de200771205a9b714dd5b706858457a98f94
transcript:
  path: transcript.zh-CN.md
  platform_subtitle_access: no-anonymous-track
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
  generated_at: "2026-08-06T04:31:08.151452Z"
  quality:
    source_chunks: 70
    aligned_chunks: 70
    alignment_items: 64382
    sentence_segments: 1910
    refined_segments: 1910
    rendered_blocks: 573
    rendered_lines: 1910
  performance:
    transcription_seconds: 471.928
    alignment_seconds: 100.569
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
    generated_at: "2026-08-06T04:31:08.151452Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/bili-bv1nb3u6teru-liao-heng/source.m4a
  metadata_path: .cache/media/zhangxiaojun/bili-bv1nb3u6teru-liao-heng/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-05T12:06:25.508889Z"
  verified_at: "2026-08-05T12:06:25.508889Z"
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 201246502
  duration_ms: 16671403
  sha256: e6c8982621c5587ca867e0417bb695b4658b59b6b7d9473613c2f3e48bcb3b7b
last_verified_at: 2026-08-06
---

# 对华为半导体首席科学家廖恒的访谈：昇腾史与全球芯片产业

> 本页保留发布者简介与章节形成的结构化概览；另有依据完整机器逐字稿整理的总结草稿，尚未完成关键片段核听和独立事实核查。

## 单集信息

- 节目：张小珺商业访谈录特别访谈（无正式期号）
- 主持人：张小珺
- 嘉宾：廖恒，华为 Fellow、半导体首席科学家
- 发布时间：2026-07-25 21:19:38（UTC+8）
- Bilibili 标示时长：04:37:52
- 本地 Bilibili 音轨：04:37:51.403（AAC、44.1 kHz、双声道）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1nB3u6tERu/)
- 编号状态：截至 2026-08-05，该内容未出现在发布者 RSS/feed 中，也没有 RSS GUID；因此保留 `episode_number: null`，不根据相邻单集推导为 #147
- 合作标记：Bilibili 公开元数据的 `is_cooperation` 为 `1`
- 字幕状态：匿名访问未发现独立公开字幕轨；处理过程中未使用 cookies 或登录态
- 本地来源：独立音轨已下载，并通过媒体探测、时长、大小和 SHA-256 校验
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[核心观点与 5 分钟版](./summary.zh-CN.md)

## 内容概览

发布者介绍称，本期嘉宾廖恒是华为 Fellow、半导体首席科学家。访谈从华为在 2020 年之后经历的挑战谈起，回顾昇腾芯片从低谷逐步走出的工程历程，并把这段经历放入中国半导体产业选择与发展的背景中观察。

节目也从更长时间尺度梳理全球半导体与芯片产业的历史、规律和整体格局，讨论摩尔定律、芯片产业的分层结构、人才与算力，以及 AI 与芯片的技术前沿。发布者将完整版定位为 Bilibili 与世界人工智能大会（WAIC）合作内容；页面同时说明节目不构成投资建议。

## 章节概览

> 以下时间码和标题来自 Bilibili 发布者简介。

- 00:02:08 — 芯片史：垄断之下漫长的日落
- 01:17:32 — 摩尔定律
- 01:31:45 — 18 层宝塔
- 01:58:18 — 华为昇腾史与中国道路
- 03:21:29 — 人才与算力
- 03:39:23 — AI 与芯片的科技前沿
- 04:16:45 — 工程师故事

## 核心议题

- 全球半导体产业的历史、竞争格局与长期规律
- 摩尔定律及芯片产业的多层结构
- 华为昇腾芯片在 2020 年之后的工程与产业历程
- 中国半导体产业的技术路线与现实选择
- 人才、算力和组织能力之间的关系
- AI 与芯片协同演进的技术前沿
- 工程师视角下的个人经历与产业变迁

## 待补充

- [x] 核对发布者 RSS/feed，确认截至 2026-08-05 没有正式期号或 RSS GUID
- [x] 核对 Bilibili 视频的 BVID、aid、cid 和 page
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取独立音轨并完成编码、时长、大小和哈希校验
- [x] 使用 Qwen3-ASR 与 ForcedAligner 生成机器逐字稿
- [ ] 校对专有名词、断句和识别错误
- [ ] 增加主持人与嘉宾的说话人区分
- [x] 基于完整机器逐字稿生成总结草稿
- [ ] 核听总结引用的关键片段并完成必要事实核查
