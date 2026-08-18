---
schema_version: 1
kind: episode
id: "dwarkesh:youtube-71546f674e555633434149"
show_id: dwarkesh
episode_key: youtube-71546f674e555633434149
episode_number: null
slug: youtube-71546f674e555633434149-demis-hassabis
release_type: regular
numbering:
  status: not-in-publisher-feed
  checked_at: 2026-08-18
  source: publisher-rss
  url: https://api.substack.com/feed/podcast/69345.rss
  note: "官方 RSS 与节目页均未给出正式期号，不按 YouTube 播放列表顺序推断"
title: "Demis Hassabis — Scaling, superhuman AIs, AlphaZero atop LLMs, AlphaFold"
navigation_title: "Demis Hassabis · Scaling 与超级智能"
catalog_keyword: "搜索规划"
published_at: "2024-02-28T15:49:28Z"
duration_ms: 3694000
language: en
participants:
  - id: demis-hassabis
    name: Demis Hassabis
    role: guest
    profile:
      headline: "Google DeepMind 联合创始人兼首席执行官"
      bio: "AI 研究者与科学创业者，领导 Google DeepMind 研发通用 AI，并推动 AI 在科学发现等领域的应用。"
      affiliations:
        - organization: Google DeepMind
          title: "联合创始人兼首席执行官"
          status: current
      checked_at: 2026-08-18
  - id: dwarkesh-patel
    name: Dwarkesh Patel
    role: host
sources:
  - platform: youtube
    kind: video
    url: https://www.youtube.com/watch?v=qTogNUV3CAI
    preferred: true
    identifiers:
      video_id: qTogNUV3CAI
      channel_id: UCXl4i9dYBrFOabk0xGmbkRA
  - platform: rss
    kind: feed-item
    url: https://www.dwarkesh.com/p/demis-hassabis
    identifiers:
      guid: "substack:post:142112869"
      feed_url: https://api.substack.com/feed/podcast/69345.rss
  - platform: website
    kind: profile
    title: "Google DeepMind：Demis Hassabis 官方人物介绍"
    url: https://deepmind.google/about/
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
    engine: youtube-subtitles
    model: publisher-caption-en
    selection_status: selected
    sha256: ec2a3bd500772122ee0d71f49988ad0b6d53599e57898d7d2168ac7b25ade4fc
transcript:
  path: transcript.en.md
  platform_subtitle_access: public
  platform_subtitle_languages:
    - en
  automatic_caption_languages:
    - zh-Hans-en
  acquisition_method: publisher-subtitle
  engine: youtube-subtitles
  model: publisher-caption-en
  options:
    source_language: en
    translation_track: zh-Hans-en
    format: json3
  generated_at: "2026-08-18T08:26:16.354504Z"
  quality:
    source_events: 640
    translated_events: 640
    aligned_events: 640
    rendered_lines: 640
  translations:
    - language: zh-CN
      path: transcript.zh-CN.md
      source_language: en
      source_path: transcript.en.md
      alignment: segment
      status: machine
      generated_at: "2026-08-18T08:26:16.354504Z"
      source_sha256: ec2a3bd500772122ee0d71f49988ad0b6d53599e57898d7d2168ac7b25ade4fc
      sha256: c58ed123319aadb8ef11dbcda94bb0e0d894a1f4ba11cac9f134936886e25550
asr_artifacts:
  raw:
    path: asr/youtube-subtitles/raw.json
    git_ignored: false
    format: podwiki-youtube-subtitle-raw-v1
  refined:
    path: asr/youtube-subtitles/refined.json
    git_ignored: false
    format: podwiki-youtube-subtitle-refined-v1
  transcript:
    path: asr/youtube-subtitles/transcript.en.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
  renderer: scripts/import_youtube_captions.py
asr_runs:
  - id: youtube-subtitles
    selection_status: selected
    engine: youtube-subtitles
    model: publisher-caption-en
    generated_at: "2026-08-18T08:26:16.354504Z"
    artifacts:
      raw: asr/youtube-subtitles/raw.json
      refined: asr/youtube-subtitles/refined.json
      transcript: asr/youtube-subtitles/transcript.en.md
    options:
      source_language: en
      translation_track: zh-Hans-en
      format: json3
    quality:
      source_events: 640
      translated_events: 640
      timestamp_alignment: exact
local_audio_cache: null
last_verified_at: 2026-08-18
---

# Demis Hassabis — Scaling, superhuman AIs, AlphaZero atop LLMs, AlphaFold

> 本页依据官方 RSS、YouTube 元数据与完整发布者英文字幕整理；英文逐字稿和逐段简中机器译稿尚未人工校对。本批采用公开字幕路径，未下载音频。

## 单集信息

- 节目：Dwarkesh Podcast
- 主播：Dwarkesh Patel
- 嘉宾：Demis Hassabis
- 发布时间：2024-02-28 15:49:28（UTC，官方 RSS）
- 来源：[YouTube 正片](https://www.youtube.com/watch?v=qTogNUV3CAI) · [官方节目页](https://www.dwarkesh.com/p/demis-hassabis)
- 逐字稿：[发布者英文字幕](./transcript.en.md) · [逐段简中机器译稿](./transcript.zh-CN.md)
- 总结：[基于完整英文稿的中文总结](./summary.zh-CN.md)

## 内容概览

Demis Hassabis 讨论 scaling、AlphaZero 式搜索、多模态、Gemini、超级智能治理、开放科学与权重安全。

## 章节概览

官方九个章节覆盖智能、搜索规划、scaling、时间线、Gemini、治理、权重安全、多模态与 DeepMind。

## 核心议题

- LLM 先验与搜索规划如何互补
- 规模工程和新算法的并行路线
- 超人系统治理、开放与权重保护

## 待补充

- [x] 核对官方 YouTube video ID、channel ID、节目页与 RSS GUID
- [x] 保存发布者英文 JSON3 并生成逐事件对齐的简中机器译稿
- [x] 基于完整英文稿形成中文总结草稿
- [ ] 人工校对中英文稿、说话人归属、专有名词与数字
- [ ] 回听关键观点并独立核查高影响外部事实
