---
schema_version: 1
kind: episode
id: "dwarkesh:youtube-382d626f42735763723541"
show_id: dwarkesh
episode_key: youtube-382d626f42735763723541
episode_number: null
slug: youtube-382d626f42735763723541-satya-nadella-2025
release_type: regular
numbering:
  status: not-in-publisher-feed
  checked_at: 2026-08-18
  source: publisher-rss
  url: https://api.substack.com/feed/podcast/69345.rss
  note: "官方 RSS 与节目页均未给出正式期号，不按 YouTube 播放列表顺序推断"
title: "Satya Nadella – How Microsoft thinks about AGI"
navigation_title: "Satya Nadella · 微软全栈 AGI 战略"
catalog_keyword: "多模型云"
published_at: "2025-11-12T17:03:08Z"
duration_ms: 5321000
language: en
participants:
  - id: satya-nadella
    name: Satya Nadella
    role: guest
    profile:
      headline: "Microsoft 董事长兼首席执行官"
      bio: "1992 年加入 Microsoft，曾领导云与企业事业群；2014 年起任首席执行官，目前兼任董事长。"
      affiliations:
        - organization: Microsoft
          title: "董事长兼首席执行官"
          status: current
      education:
        - institution: Mangalore University
          credential: "学士"
          field: "电气工程"
        - institution: "University of Wisconsin–Milwaukee"
          credential: "硕士"
          field: "计算机科学"
        - institution: University of Chicago
          credential: MBA
      checked_at: 2026-08-18
  - id: dwarkesh-patel
    name: Dwarkesh Patel
    role: host
sources:
  - platform: youtube
    kind: video
    url: https://www.youtube.com/watch?v=8-boBsWcr5A
    preferred: true
    identifiers:
      video_id: 8-boBsWcr5A
      channel_id: UCXl4i9dYBrFOabk0xGmbkRA
  - platform: rss
    kind: feed-item
    url: https://www.dwarkesh.com/p/satya-nadella-2
    identifiers:
      guid: "substack:post:178688356"
      feed_url: https://api.substack.com/feed/podcast/69345.rss
  - platform: website
    kind: profile
    title: "Microsoft：Satya Nadella 官方人物介绍"
    url: https://news.microsoft.com/source/exec/satya-nadella/
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
    sha256: b87adc07449b2d2d828bff5157719f7bd87f374b3d6e18a1703b7e2529a9c67e
transcript:
  path: transcript.en.md
  platform_subtitle_access: public
  platform_subtitle_languages:
    - en
    - es
    - hi
    - zh
  automatic_caption_languages:
    - zh-Hans-en
  acquisition_method: publisher-subtitle
  engine: youtube-subtitles
  model: publisher-caption-en
  options:
    source_language: en
    translation_track: zh-Hans-en
    format: json3
  generated_at: "2026-08-18T08:26:16.080466Z"
  quality:
    source_events: 966
    translated_events: 966
    aligned_events: 966
    rendered_lines: 966
  translations:
    - language: zh-CN
      path: transcript.zh-CN.md
      source_language: en
      source_path: transcript.en.md
      alignment: segment
      status: machine
      generated_at: "2026-08-18T08:26:16.080466Z"
      source_sha256: b87adc07449b2d2d828bff5157719f7bd87f374b3d6e18a1703b7e2529a9c67e
      sha256: 38b5a52f70b98a7b65f738407322a8342ec9434b2a57eac6c67a90a925e9b48f
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
    generated_at: "2026-08-18T08:26:16.080466Z"
    artifacts:
      raw: asr/youtube-subtitles/raw.json
      refined: asr/youtube-subtitles/refined.json
      transcript: asr/youtube-subtitles/transcript.en.md
    options:
      source_language: en
      translation_track: zh-Hans-en
      format: json3
    quality:
      source_events: 966
      translated_events: 966
      timestamp_alignment: exact
local_audio_cache: null
last_verified_at: 2026-08-18
---

# Satya Nadella – How Microsoft thinks about AGI

> 本页依据官方 RSS、YouTube 元数据与完整发布者英文字幕整理；英文逐字稿和逐段简中机器译稿尚未人工校对。本批采用公开字幕路径，未下载音频。

## 单集信息

- 节目：Dwarkesh Podcast
- 主播：Dwarkesh Patel
- 嘉宾：Satya Nadella
- 发布时间：2025-11-12 17:03:08（UTC，官方 RSS）
- 来源：[YouTube 正片](https://www.youtube.com/watch?v=8-boBsWcr5A) · [官方节目页](https://www.dwarkesh.com/p/satya-nadella-2)
- 逐字稿：[发布者英文字幕](./transcript.en.md) · [逐段简中机器译稿](./transcript.zh-CN.md)
- 总结：[基于完整英文稿的中文总结](./summary.zh-CN.md)

## 内容概览

Satya Nadella 从 Fairwater 2 出发，解释微软在基础设施、多模型云、OpenAI、MAI、自研芯片、Copilot 与全球信任上的组合策略。

## 章节概览

官方九个章节覆盖 Fairwater、AGI 商业模式、Copilot、模型利润、MAI、超大云、自研芯片、资本开支和全球信任。

## 核心议题

- 跨芯片代际的数据中心设计
- 多模型云与应用层利润分配
- 自研芯片、合作伙伴和全球信任

## 待补充

- [x] 核对官方 YouTube video ID、channel ID、节目页与 RSS GUID
- [x] 保存发布者英文 JSON3 并生成逐事件对齐的简中机器译稿
- [x] 基于完整英文稿形成中文总结草稿
- [ ] 人工校对中英文稿、说话人归属、专有名词与数字
- [ ] 回听关键观点并独立核查高影响外部事实
