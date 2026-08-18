---
schema_version: 1
kind: episode
id: "dwarkesh:youtube-487262713636587174436f"
show_id: dwarkesh
episode_key: youtube-487262713636587174436f
episode_number: null
slug: youtube-487262713636587174436f-jensen-huang
release_type: regular
numbering:
  status: not-in-publisher-feed
  checked_at: 2026-08-18
  source: publisher-rss
  url: https://api.substack.com/feed/podcast/69345.rss
  note: "官方 RSS 与节目页均未给出正式期号，不按 YouTube 播放列表顺序推断"
title: "Jensen Huang – Will Nvidia’s moat persist?"
navigation_title: "Jensen Huang · Nvidia 护城河"
catalog_keyword: "供应链"
published_at: "2026-04-15T15:45:23Z"
duration_ms: 6192000
language: en
participants:
  - id: jensen-huang
    name: Jensen Huang
    role: guest
  - id: dwarkesh-patel
    name: Dwarkesh Patel
    role: host
sources:
  - platform: youtube
    kind: video
    url: https://www.youtube.com/watch?v=Hrbq66XqtCo
    preferred: true
    identifiers:
      video_id: Hrbq66XqtCo
      channel_id: UCXl4i9dYBrFOabk0xGmbkRA
  - platform: rss
    kind: feed-item
    url: https://www.dwarkesh.com/p/jensen-huang
    identifiers:
      guid: "substack:post:194289889"
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
    sha256: 1db6d16308d7766e3e33aa49efd4cdb4462f053f8ab2ea966f49e79435445e7e
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
  generated_at: "2026-08-18T08:09:03.019257Z"
  quality:
    source_events: 1104
    translated_events: 1104
    aligned_events: 1104
    rendered_lines: 1104
  translations:
    - language: zh-CN
      path: transcript.zh-CN.md
      source_language: en
      source_path: transcript.en.md
      alignment: segment
      status: machine
      generated_at: "2026-08-18T08:09:03.019257Z"
      source_sha256: 1db6d16308d7766e3e33aa49efd4cdb4462f053f8ab2ea966f49e79435445e7e
      sha256: c8b7342402565fb2ca1b5a1a5670e9428204ac29e4a2370942703f1786d512e9
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
    generated_at: "2026-08-18T08:09:03.019257Z"
    artifacts:
      raw: asr/youtube-subtitles/raw.json
      refined: asr/youtube-subtitles/refined.json
      transcript: asr/youtube-subtitles/transcript.en.md
    options:
      source_language: en
      translation_track: zh-Hans-en
      format: json3
    quality:
      source_events: 1104
      translated_events: 1104
      timestamp_alignment: exact
local_audio_cache: null
last_verified_at: 2026-08-18
---

# Jensen Huang – Will Nvidia’s moat persist?

> 本页依据官方 RSS、YouTube 元数据与完整发布者英文字幕整理；英文逐字稿和逐段简中机器译稿尚未人工校对。本批采用公开字幕路径，未下载音频。

## 单集信息

- 节目：Dwarkesh Podcast
- 主播：Dwarkesh Patel
- 嘉宾：Jensen Huang
- 发布时间：2026-04-15 15:45:23（UTC，官方 RSS）
- 来源：[YouTube 正片](https://www.youtube.com/watch?v=Hrbq66XqtCo) · [官方节目页](https://www.dwarkesh.com/p/jensen-huang)
- 逐字稿：[发布者英文字幕](./transcript.en.md) · [逐段简中机器译稿](./transcript.zh-CN.md)
- 总结：[基于完整英文稿的中文总结](./summary.zh-CN.md)

## 内容概览

黄仁勋与 Dwarkesh Patel 讨论 Nvidia 的供应链、可编程计算生态、TPU 竞争、云业务边界、对华芯片政策与多架构取舍。

## 章节概览

官方五个章节依次讨论稀缺供应链、TPU、云业务边界、对华芯片销售和多架构选择。

## 核心议题

- 供应链规模与 CUDA 生态如何共同形成护城河
- TPU 专用效率与 GPU 可编程性的竞争
- 云业务边界和对华芯片政策的收益风险

## 待补充

- [x] 核对官方 YouTube video ID、channel ID、节目页与 RSS GUID
- [x] 保存发布者英文 JSON3 并生成逐事件对齐的简中机器译稿
- [x] 基于完整英文稿形成中文总结草稿
- [ ] 人工校对中英文稿、说话人归属、专有名词与数字
- [ ] 回听关键观点并独立核查高影响外部事实
