---
schema_version: 1
kind: episode
id: "dwarkesh:youtube-7259586551625475566c30"
show_id: dwarkesh
episode_key: youtube-7259586551625475566c30
episode_number: null
slug: youtube-7259586551625475566c30-mark-zuckerberg-2025
release_type: regular
numbering:
  status: not-in-publisher-feed
  checked_at: 2026-08-18
  source: publisher-rss
  url: https://api.substack.com/feed/podcast/69345.rss
  note: "官方 RSS 与节目页均未给出正式期号，不按 YouTube 播放列表顺序推断"
title: "Mark Zuckerberg — AI will write most Meta code in 18 months"
navigation_title: "Mark Zuckerberg · Llama 4 与代码代理"
catalog_keyword: "开放模型"
published_at: "2025-04-29T15:46:54Z"
duration_ms: 4549000
language: en
participants:
  - id: mark-zuckerberg
    name: Mark Zuckerberg
    role: guest
  - id: dwarkesh-patel
    name: Dwarkesh Patel
    role: host
sources:
  - platform: youtube
    kind: video
    url: https://www.youtube.com/watch?v=rYXeQbTuVl0
    preferred: true
    identifiers:
      video_id: rYXeQbTuVl0
      channel_id: UCXl4i9dYBrFOabk0xGmbkRA
  - platform: rss
    kind: feed-item
    url: https://www.dwarkesh.com/p/mark-zuckerberg-2
    identifiers:
      guid: "substack:post:162392947"
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
    sha256: b9c5e92c98b6ede6f262799e685b146bbbe242a3deba20575b9b391fe9525e29
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
  generated_at: "2026-08-18T08:26:16.211240Z"
  quality:
    source_events: 675
    translated_events: 675
    aligned_events: 675
    rendered_lines: 675
  translations:
    - language: zh-CN
      path: transcript.zh-CN.md
      source_language: en
      source_path: transcript.en.md
      alignment: segment
      status: machine
      generated_at: "2026-08-18T08:26:16.211240Z"
      source_sha256: b9c5e92c98b6ede6f262799e685b146bbbe242a3deba20575b9b391fe9525e29
      sha256: b7fd7c481177d8249f475496f4a720a69ccc61e8fd82601b5b25a2664b83e161
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
    generated_at: "2026-08-18T08:26:16.211240Z"
    artifacts:
      raw: asr/youtube-subtitles/raw.json
      refined: asr/youtube-subtitles/refined.json
      transcript: asr/youtube-subtitles/transcript.en.md
    options:
      source_language: en
      translation_track: zh-Hans-en
      format: json3
    quality:
      source_events: 675
      translated_events: 675
      timestamp_alignment: exact
local_audio_cache: null
last_verified_at: 2026-08-18
---

# Mark Zuckerberg — AI will write most Meta code in 18 months

> 本页依据官方 RSS、YouTube 元数据与完整发布者英文字幕整理；英文逐字稿和逐段简中机器译稿尚未人工校对。本批采用公开字幕路径，未下载音频。

## 单集信息

- 节目：Dwarkesh Podcast
- 主播：Dwarkesh Patel
- 嘉宾：Mark Zuckerberg
- 发布时间：2025-04-29 15:46:54（UTC，官方 RSS）
- 来源：[YouTube 正片](https://www.youtube.com/watch?v=rYXeQbTuVl0) · [官方节目页](https://www.dwarkesh.com/p/mark-zuckerberg-2)
- 逐字稿：[发布者英文字幕](./transcript.en.md) · [逐段简中机器译稿](./transcript.zh-CN.md)
- 总结：[基于完整英文稿的中文总结](./summary.zh-CN.md)

## 内容概览

Mark Zuckerberg 讨论 Llama 4 评估、代码代理、AI 关系产品、DeepSeek、开放模型、商业化和 Meta 的管理方式。

## 章节概览

官方九个章节覆盖 Llama 4、智能爆炸、AI 关系、中国、开放模型、商业化、CEO、政府关系和生产率。

## 核心议题

- 产品价值与公开模型基准的冲突
- 代码代理和 AI 关系产品的机会与风险
- 开放模型、许可与中美竞争

## 待补充

- [x] 核对官方 YouTube video ID、channel ID、节目页与 RSS GUID
- [x] 保存发布者英文 JSON3 并生成逐事件对齐的简中机器译稿
- [x] 基于完整英文稿形成中文总结草稿
- [ ] 人工校对中英文稿、说话人归属、专有名词与数字
- [ ] 回听关键观点并独立核查高影响外部事实
