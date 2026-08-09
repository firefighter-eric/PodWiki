---
schema_version: 1
kind: episode
id: "zhangxiaojun:146"
show_id: zhangxiaojun
episode_key: "146"
episode_number: 146
slug: 146-ke-liyiming
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-05
  source: publisher-rss
title: "对Physical Intelligence柯丽一鸣4小时访谈：Pi的开源模型研究，机器人的江湖、族谱与主角"
navigation_title: "柯丽一鸣 · 通用机器人、Pi 模型与强化学习"
catalog_keyword: "Pi"
published_at: "2026-07-16T08:30:00+08:00"
duration_ms: 13684000
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: ke-liyiming
    name: 柯丽一鸣
    aliases:
      - Kay Ke
    role: guest
    profile:
      headline: "Physical Intelligence 研究员"
      bio: "从事强化学习研究，也是 Physical Intelligence 核心论文作者之一；科研之外从事小说写作。"
      affiliations:
        - organization: "Physical Intelligence"
          title: "研究员"
          status: current
      checked_at: "2026-08-06"
sources:
  - platform: rss
    kind: feed-item
    url: https://www.xiaoyuzhoufm.com/episode/6a57a05da4972c496dfc67f1
    preferred: false
    identifiers:
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 6a57a05da4972c496dfc67f1
  - platform: apple-podcasts
    kind: episode
    url: https://podcasts.apple.com/podcast/id1634356920?i=1000776989957
    preferred: false
    identifiers:
      show_id: "1634356920"
      episode_id: "1000776989957"
      rss_guid: 6a57a05da4972c496dfc67f1
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV12bNB6vEtt/
    preferred: true
    identifiers:
      bvid: BV12bNB6vEtt
      aid: "116924612676518"
      cid: "39961037462"
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
    sha256: 27675ca1815e07fdb15f6be3f51524f45d8a712faa6ffae986fbf2b49ab6b3ac
transcript:
  path: transcript.zh-CN.md
  platform_subtitle_access: not-exposed-as-track
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
  generated_at: "2026-08-06T04:12:54.445737Z"
  quality:
    source_chunks: 57
    aligned_chunks: 57
    alignment_items: 72433
    sentence_segments: 1833
    refined_segments: 1832
    rendered_blocks: 456
    rendered_lines: 1832
  performance:
    transcription_seconds: 489.043
    alignment_seconds: 105.025
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
    generated_at: "2026-08-06T04:12:54.445737Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/146-ke-liyiming/source.m4a
  metadata_path: .cache/media/zhangxiaojun/146-ke-liyiming/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-05T12:00:53.532323Z"
  verified_at: "2026-08-05T12:00:53.532323Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 188616174
  duration_ms: 13572224
  sha256: d22317ea1ad994b7f699e9115e5636eb9b9c4aa550eda9f31bf4ca627e1a9f65
last_verified_at: 2026-08-06
---

# 对 Physical Intelligence 柯丽一鸣 4 小时访谈

> 本页保留发布者简介与章节形成的结构化概览；另有依据完整机器逐字稿整理的总结草稿，尚未完成关键片段核听和独立事实核查。

## 单集信息

- 节目：张小珺商业访谈录 #146
- 主持人：张小珺
- 嘉宾：柯丽一鸣（Kay Ke），Physical Intelligence 研究员
- 发布时间：2026-07-16 08:30（UTC+8）
- 官方 RSS 音频时长：03:48:04
- 本地 Bilibili 音轨：03:46:12（AAC、48 kHz、双声道）
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/6a57a05da4972c496dfc67f1)、[Apple Podcasts](https://podcasts.apple.com/podcast/id1634356920?i=1000776989957)、[Bilibili 视频](https://www.bilibili.com/video/BV12bNB6vEtt/)
- 字幕状态：匿名访问未发现独立平台字幕轨
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[核心观点与 5 分钟版](./summary.zh-CN.md)

## 内容概览

本期嘉宾柯丽一鸣主要在机器人公司 Physical Intelligence（Pi）从事强化学习研究，也是 Pi 核心论文作者之一。发布者简介将 Pi 描述为专注机器人“大脑”的创业公司，并提到柯丽一鸣在科研之外也从事小说写作。

访谈从个人经历、武侠和文学表达谈起，继而梳理机器人领域的团队谱系、硅谷创业图谱，以及 Pi 从 π0、π0.5 到 π*0.6 的研究思路与技术细节。由于录制时间较早，节目没有覆盖当时更新的 π0.7；发布者在简介中补充了其统一模型、架构与数据设计方向。

## 章节概览

> 以下采用发布者 RSS 音频的时间码。Bilibili 视频总时长短约 1 分 52 秒，其发布者章节时间码相对 RSS 版本约提前 1 分钟。

- 00:02:11 — 机器人与小说家
- 00:17:26 — 武侠、板寸、背包客
- 00:36:33 — 草蛇灰线
- 00:53:56 — 机器人江湖、族谱、主角
- 01:27:18 — 硅谷创业图谱
- 01:54:43 — Pi 的研究：π0、π0.5、π*0.6
- 02:26:01 — Pi 的组织与文化
- 02:34:52 — 放弃剑桥教职
- 02:46:49 — 巴甫洛夫的狗
- 03:04:53 — 前沿展望
- 03:16:14 — 中国
- 03:25:02 — 机器人“种族”
- 03:31:19 — 没有写完的故事

## 核心议题

- 机器人领域的团队谱系、技术路线与主要参与者
- Physical Intelligence 的通用机器人模型研究与开源工作
- π0、π0.5、π*0.6 的演进，以及发布者补充的 π0.7 方向
- 硅谷机器人创业公司的组织、文化与人才流动
- 科研工作、人文表达与个人选择之间的关系

## 待补充

- [x] 通过发布者 RSS GUID 核对官方期号
- [x] 核对 Bilibili 视频的 aid、cid 和 page
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取并验证本地独立音轨
- [x] 使用 Qwen3-ASR 与 ForcedAligner 生成机器逐字稿
- [ ] 校对专有名词、断句和识别错误
- [ ] 增加主持人与嘉宾的说话人区分
- [x] 基于完整机器逐字稿生成总结草稿
- [ ] 核听总结引用的关键片段并完成必要事实核查
