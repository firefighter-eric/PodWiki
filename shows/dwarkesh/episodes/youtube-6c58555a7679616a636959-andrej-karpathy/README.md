---
schema_version: 1
kind: episode
id: "dwarkesh:youtube-6c58555a7679616a636959"
show_id: dwarkesh
episode_key: youtube-6c58555a7679616a636959
episode_number: null
slug: youtube-6c58555a7679616a636959-andrej-karpathy
release_type: regular
numbering:
  status: not-in-publisher-feed
  checked_at: 2026-08-18
  source: publisher-rss
  url: https://api.substack.com/feed/podcast/69345.rss
  note: "官方 RSS 与节目页均未给出正式期号，不按 YouTube 播放列表顺序推断"
title: "Andrej Karpathy — “We’re summoning ghosts, not building animals”"
navigation_title: "Andrej Karpathy · 代理、RL 与教育"
catalog_keyword: "认知架构"
published_at: "2025-10-17T16:54:33Z"
duration_ms: 8768000
language: en
participants:
  - id: andrej-karpathy
    name: Andrej Karpathy
    role: guest
    profile:
      headline: "AI 研究者与教育者，OpenAI 创始团队成员、前 Tesla AI 总监"
      bio: "曾在 OpenAI 从事研究，并于 Tesla 领导 Autopilot 计算机视觉团队；其后持续面向公众讲解神经网络、LLM 与 AI 工程。"
      affiliations:
        - organization: OpenAI
          title: "研究科学家、创始团队成员"
          status: former
        - organization: Tesla
          title: "AI 总监"
          status: former
      education:
        - institution: Stanford University
          credential: PhD
          field: "神经网络、计算机视觉与自然语言处理"
      checked_at: 2026-08-18
  - id: dwarkesh-patel
    name: Dwarkesh Patel
    role: host
sources:
  - platform: youtube
    kind: video
    url: https://www.youtube.com/watch?v=lXUZvyajciY
    preferred: true
    identifiers:
      video_id: lXUZvyajciY
      channel_id: UCXl4i9dYBrFOabk0xGmbkRA
  - platform: rss
    kind: feed-item
    url: https://www.dwarkesh.com/p/andrej-karpathy
    identifiers:
      guid: "substack:post:176425744"
      feed_url: https://api.substack.com/feed/podcast/69345.rss
  - platform: website
    kind: profile
    title: "Andrej Karpathy 官方个人简介"
    url: https://karpathy.ai/
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
    sha256: ce5c7cd9b51e3efe672e8c56b4369f7a8527a70a31cd49c99c05936df36904bd
transcript:
  path: transcript.en.md
  platform_subtitle_access: public
  platform_subtitle_languages:
    - en
    - es
  automatic_caption_languages:
    - zh-Hans-en
  acquisition_method: publisher-subtitle
  engine: youtube-subtitles
  model: publisher-caption-en
  options:
    source_language: en
    translation_track: zh-Hans-en
    format: json3
  generated_at: "2026-08-18T08:26:16.130712Z"
  quality:
    source_events: 1806
    translated_events: 1806
    aligned_events: 1806
    rendered_lines: 1806
  translations:
    - language: zh-CN
      path: transcript.zh-CN.md
      source_language: en
      source_path: transcript.en.md
      alignment: segment
      status: machine
      generated_at: "2026-08-18T08:26:16.130712Z"
      source_sha256: ce5c7cd9b51e3efe672e8c56b4369f7a8527a70a31cd49c99c05936df36904bd
      sha256: 0916e36a4b60ff151670f5ae8d47984df20ffe4aa82b8d5dd04fbae70336cf12
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
    generated_at: "2026-08-18T08:26:16.130712Z"
    artifacts:
      raw: asr/youtube-subtitles/raw.json
      refined: asr/youtube-subtitles/refined.json
      transcript: asr/youtube-subtitles/transcript.en.md
    options:
      source_language: en
      translation_track: zh-Hans-en
      format: json3
    quality:
      source_events: 1806
      translated_events: 1806
      timestamp_alignment: exact
local_audio_cache: null
last_verified_at: 2026-08-18
---

# Andrej Karpathy — “We’re summoning ghosts, not building animals”

> 本页依据官方 RSS、YouTube 元数据与完整发布者英文字幕整理；英文逐字稿和逐段简中机器译稿尚未人工校对。本批采用公开字幕路径，未下载音频。

## 单集信息

- 节目：Dwarkesh Podcast
- 主播：Dwarkesh Patel
- 嘉宾：Andrej Karpathy
- 发布时间：2025-10-17 16:54:33（UTC，官方 RSS）
- 来源：[YouTube 正片](https://www.youtube.com/watch?v=lXUZvyajciY) · [官方节目页](https://www.dwarkesh.com/p/andrej-karpathy)
- 逐字稿：[发布者英文字幕](./transcript.en.md) · [逐段简中机器译稿](./transcript.zh-CN.md)
- 总结：[基于完整英文稿的中文总结](./summary.zh-CN.md)

## 内容概览

Andrej Karpathy 讨论代理时间线、语言模型的认知缺陷、强化学习、经济增长、自动驾驶、演化与 AI 教育。

## 章节概览

官方九个章节从 AGI 时间线推进到认知缺陷、RL、经济影响、超级智能、演化、自动驾驶和教育。

## 核心议题

- 语言模型为何更像幽灵而不是动物
- 强化学习与真实部署的可靠性瓶颈
- 渐进自动化、GDP 与未来教育

## 待补充

- [x] 核对官方 YouTube video ID、channel ID、节目页与 RSS GUID
- [x] 保存发布者英文 JSON3 并生成逐事件对齐的简中机器译稿
- [x] 基于完整英文稿形成中文总结草稿
- [ ] 人工校对中英文稿、说话人归属、专有名词与数字
- [ ] 回听关键观点并独立核查高影响外部事实
