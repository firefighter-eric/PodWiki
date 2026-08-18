---
schema_version: 1
kind: episode
id: "dwarkesh:youtube-5966316f3054517a727938"
show_id: dwarkesh
episode_key: youtube-5966316f3054517a727938
episode_number: null
slug: youtube-5966316f3054517a727938-ilya-sutskever-2023
release_type: regular
numbering:
  status: not-in-publisher-feed
  checked_at: 2026-08-18
  source: publisher-rss
  url: https://api.substack.com/feed/podcast/69345.rss
  note: "官方 RSS 与节目页均未给出正式期号，不按 YouTube 播放列表顺序推断"
title: "Ilya Sutskever (OpenAI Chief Scientist) — Why next-token prediction could surpass human intelligence"
navigation_title: "Ilya Sutskever · 下一词预测与 AGI"
catalog_keyword: "下一词预测"
published_at: "2023-03-27T13:57:39Z"
duration_ms: 2861000
language: en
participants:
  - id: ilya-sutskever
    name: Ilya Sutskever
    role: guest
    profile:
      headline: "Safe Superintelligence Inc. 首席执行官、OpenAI 联合创始人兼前首席科学家"
      bio: "AI 研究者，曾在 OpenAI 领导超级智能对齐研究；离开 OpenAI 后转向以安全超级智能为唯一目标的 SSI。"
      affiliations:
        - organization: "Safe Superintelligence Inc. (SSI)"
          title: "首席执行官"
          status: current
        - organization: OpenAI
          title: "联合创始人、首席科学家"
          status: former
      checked_at: 2026-08-18
  - id: dwarkesh-patel
    name: Dwarkesh Patel
    role: host
sources:
  - platform: youtube
    kind: video
    url: https://www.youtube.com/watch?v=Yf1o0TQzry8
    preferred: true
    identifiers:
      video_id: Yf1o0TQzry8
      channel_id: UCXl4i9dYBrFOabk0xGmbkRA
  - platform: rss
    kind: feed-item
    url: https://www.dwarkesh.com/p/ilya-sutskever
    identifiers:
      guid: "substack:post:106731655"
      feed_url: https://api.substack.com/feed/podcast/69345.rss
  - platform: website
    kind: profile
    title: "SSI：Ilya Sutskever 官方职务更新"
    url: https://ssi.inc/updates
  - platform: website
    kind: profile
    title: "OpenAI：Ilya Sutskever 联合创始人与首席科学家资料"
    url: https://openai.com/index/introducing-superalignment/
  - platform: website
    kind: profile
    title: "OpenAI：Ilya Sutskever 离任公告"
    url: https://openai.com/index/jakub-pachocki-announced-as-chief-scientist/
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
    sha256: c42c16187a773274d504273343137d8b1e8632a51a74a5a58578e3bd23d53744
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
  generated_at: "2026-08-18T08:33:35.482123Z"
  quality:
    source_events: 501
    translated_events: 501
    aligned_events: 501
    rendered_lines: 501
  translations:
    - language: zh-CN
      path: transcript.zh-CN.md
      source_language: en
      source_path: transcript.en.md
      alignment: segment
      status: machine
      generated_at: "2026-08-18T08:33:35.482123Z"
      source_sha256: c42c16187a773274d504273343137d8b1e8632a51a74a5a58578e3bd23d53744
      sha256: b0b79fdec2c935a39c9ff93fd67f981a5f9c1c18a910434fda332dae3ef80f15
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
    generated_at: "2026-08-18T08:33:35.482123Z"
    artifacts:
      raw: asr/youtube-subtitles/raw.json
      refined: asr/youtube-subtitles/refined.json
      transcript: asr/youtube-subtitles/transcript.en.md
    options:
      source_language: en
      translation_track: zh-Hans-en
      format: json3
    quality:
      source_events: 501
      translated_events: 501
      timestamp_alignment: exact
local_audio_cache: null
last_verified_at: 2026-08-18
---

# Ilya Sutskever (OpenAI Chief Scientist) — Why next-token prediction could surpass human intelligence

> 本页依据官方 RSS、YouTube 元数据与完整发布者英文字幕整理；英文逐字稿和逐段简中机器译稿尚未人工校对。本批采用公开字幕路径，未下载音频。

## 单集信息

- 节目：Dwarkesh Podcast
- 主播：Dwarkesh Patel
- 嘉宾：Ilya Sutskever
- 发布时间：2023-03-27 13:57:39（UTC，官方 RSS）
- 来源：[YouTube 正片](https://www.youtube.com/watch?v=Yf1o0TQzry8) · [官方节目页](https://www.dwarkesh.com/p/ilya-sutskever)
- 逐字稿：[发布者英文字幕](./transcript.en.md) · [逐段简中机器译稿](./transcript.zh-CN.md)
- 总结：[基于完整英文稿的中文总结](./summary.zh-CN.md)

## 内容概览

Ilya Sutskever 解释下一词预测为何可能超越浅层模仿，并讨论 AGI 时间线、能力外推、多层对齐和 post-AGI 未来。

## 章节概览

官方八个章节覆盖 AGI 时间线、生成模型、数据与研究、对齐、post-AGI、竞争、进步必然性和未来突破。

## 核心议题

- 下一词预测目标是否包含深层世界理解
- 平滑损失如何映射到具体能力
- 多层对齐与 post-AGI 制度选择

## 待补充

- [x] 核对官方 YouTube video ID、channel ID、节目页与 RSS GUID
- [x] 保存发布者英文 JSON3 并生成逐事件对齐的简中机器译稿
- [x] 基于完整英文稿形成中文总结草稿
- [ ] 人工校对中英文稿、说话人归属、专有名词与数字
- [ ] 回听关键观点并独立核查高影响外部事实
