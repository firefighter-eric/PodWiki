---
schema_version: 1
kind: episode
id: "dwarkesh:youtube-6b4e73693558564454544d"
show_id: dwarkesh
episode_key: youtube-6b4e73693558564454544d
episode_number: null
slug: youtube-6b4e73693558564454544d-marc-andreessen
release_type: regular
numbering:
  status: not-in-publisher-feed
  checked_at: 2026-08-18
  source: publisher-rss
  url: https://api.substack.com/feed/podcast/69345.rss
  note: "官方 RSS 与节目页均未给出正式期号，不按 YouTube 播放列表顺序推断"
title: "Marc Andreessen — AI, crypto, 1000 Elon Musks, regrets, vulnerabilities, & managerial revolution"
navigation_title: "Marc Andreessen · AI、风投与管理革命"
catalog_keyword: "管理型资本主义"
published_at: "2023-02-01T16:00:00Z"
duration_ms: 4818000
language: en
participants:
  - id: marc-andreessen
    name: Marc Andreessen
    role: guest
  - id: dwarkesh-patel
    name: Dwarkesh Patel
    role: host
sources:
  - platform: youtube
    kind: video
    url: https://www.youtube.com/watch?v=kNsi5XVDTTM
    preferred: true
    identifiers:
      video_id: kNsi5XVDTTM
      channel_id: UCXl4i9dYBrFOabk0xGmbkRA
  - platform: rss
    kind: feed-item
    url: https://www.dwarkesh.com/p/marc-andreessen
    identifiers:
      guid: "substack:post:99489876"
      feed_url: https://api.substack.com/feed/podcast/69345.rss
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
    sha256: a60dd2cae3d74c629ee1dce6a1b7e801778c79f80462d62d353f55d29cc21166
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
  generated_at: "2026-08-18T08:33:35.526548Z"
  quality:
    source_events: 887
    translated_events: 887
    aligned_events: 887
    rendered_lines: 887
  translations:
    - language: zh-CN
      path: transcript.zh-CN.md
      source_language: en
      source_path: transcript.en.md
      alignment: segment
      status: machine
      generated_at: "2026-08-18T08:33:35.526548Z"
      source_sha256: a60dd2cae3d74c629ee1dce6a1b7e801778c79f80462d62d353f55d29cc21166
      sha256: 85e6c372220746e0dd5d1b9d78e639b2f718d7682cad8460ae50df82a552fcb4
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
    generated_at: "2026-08-18T08:33:35.526548Z"
    artifacts:
      raw: asr/youtube-subtitles/raw.json
      refined: asr/youtube-subtitles/refined.json
      transcript: asr/youtube-subtitles/transcript.en.md
    options:
      source_language: en
      translation_track: zh-Hans-en
      format: json3
    quality:
      source_events: 887
      translated_events: 887
      timestamp_alignment: exact
local_audio_cache: null
last_verified_at: 2026-08-18
---

# Marc Andreessen — AI, crypto, 1000 Elon Musks, regrets, vulnerabilities, & managerial revolution

> 本页依据官方 RSS、YouTube 元数据与完整发布者英文字幕整理；英文逐字稿和逐段简中机器译稿尚未人工校对。本批采用公开字幕路径，未下载音频。

## 单集信息

- 节目：Dwarkesh Podcast
- 主播：Dwarkesh Patel
- 嘉宾：Marc Andreessen
- 发布时间：2023-02-01 16:00:00（UTC，官方 RSS）
- 来源：[YouTube 正片](https://www.youtube.com/watch?v=kNsi5XVDTTM) · [官方节目页](https://www.dwarkesh.com/p/marc-andreessen)
- 逐字稿：[发布者英文字幕](./transcript.en.md) · [逐段简中机器译稿](./transcript.zh-CN.md)
- 总结：[基于完整英文稿的中文总结](./summary.zh-CN.md)

## 内容概览

Marc Andreessen 讨论 AI 软件、管理型资本主义、长期基金、基础研究、加密与 NFT、创始人、a16z 风险和大科技。

## 章节概览

官方十五个章节覆盖 AI、组织与风投理论、基础研究、加密、创始人、a16z 风险、Twitter 和大科技。

## 核心议题

- AI 如何改变软件构建与交互
- 管理型资本主义、创业者和风险资本
- 加密资产、长期基金与 a16z 自身脆弱性

## 待补充

- [x] 核对官方 YouTube video ID、channel ID、节目页与 RSS GUID
- [x] 保存发布者英文 JSON3 并生成逐事件对齐的简中机器译稿
- [x] 基于完整英文稿形成中文总结草稿
- [ ] 人工校对中英文稿、说话人归属、专有名词与数字
- [ ] 回听关键观点并独立核查高影响外部事实
