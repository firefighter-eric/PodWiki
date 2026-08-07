---
schema_version: 1
kind: episode
id: "zhangxiaojun:128"
show_id: zhangxiaojun
episode_key: "128"
episode_number: 128
slug: 128-ji-yichao
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-06
  source: publisher-rss
title: "Manus 决定出售前最后的访谈：啊，这奇幻的 2025 年漂流啊…"
navigation_title: "季逸超 · Manus 与产品驱动的通用 Agent"
catalog_keyword: "Manus"
published_at: "2025-12-30T10:41:23+08:00"
duration_ms: 12677000
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: ji-yichao
    name: 季逸超
    role: guest
sources:
  - platform: rss
    kind: feed-item
    url: https://www.xiaoyuzhoufm.com/episode/695331cb2db086f897b50ea9
    preferred: false
    identifiers:
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 695331cb2db086f897b50ea9
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1knvYBDEjs/
    preferred: true
    identifiers:
      bvid: BV1knvYBDEjs
      aid: "115807753406655"
      cid: "35217870603"
      page: 1
workflow:
  metadata: verified
  summary: draft
  transcript: machine
summary_basis:
  - publisher-description
  - complete-machine-transcript
summary:
  path: summary.zh-CN.md
  language: zh-CN
  source_transcript:
    path: transcript.zh-CN.md
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    selection_status: selected
    sha256: f26acc688571348956b96ae699f278b68803c318c2a643be42e049af672a32d0
transcript:
  path: transcript.zh-CN.md
  platform_subtitle_access: not-exposed-as-public-track
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
  generated_at: "2026-08-06T07:51:57.972822Z"
  quality:
    source_chunks: 53
    aligned_chunks: 53
    alignment_items: 78048
    sentence_segments: 2435
    refined_segments: 2433
    rendered_blocks: 449
    rendered_lines: 2433
  performance:
    transcription_seconds: 591.311
    alignment_seconds: 120.537
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
    generated_at: "2026-08-06T07:51:57.972822Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/128-ji-yichao/source.m4a
  metadata_path: .cache/media/zhangxiaojun/128-ji-yichao/source.metadata.json
  git_ignored: true
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 129667018
  duration_ms: 12660425
  sha256: 9089d7b7b1b0c90cac689048fe3093bde0567475f567a309a5bc079c2aab99ea
  acquired_at: "2026-08-06T06:52:25.143532Z"
  verified_at: "2026-08-06T06:52:25.143532Z"
last_verified_at: 2026-08-06
---

# Manus 决定出售前最后的访谈：啊，这奇幻的 2025 年漂流啊…

> 本页保留发布者简介与平台章节形成的概览；另有依据完整 Qwen3-ASR 机器逐字稿整理的总结草稿。机器稿与总结均尚未完成人工核听或独立事实核查。

## 单集信息

- 节目：张小珺商业访谈录（第 128 期）
- 主持人：张小珺
- 嘉宾：季逸超（Peak），Manus 联合创始人兼首席科学家
- 录制时间：2025-12-01；发布时间：2025-12-30 10:41（UTC+8）
- 官方 RSS 时长：03:31:17；Bilibili 视频时长：03:31:00
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/695331cb2db086f897b50ea9)、[Bilibili 视频](https://www.bilibili.com/video/BV1knvYBDEjs/)
- 字幕状态：匿名访问未发现公开字幕轨；播放器提示登录后可能存在字幕
- 本地音频：AAC、44.1 kHz、双声道、129,667,018 字节；sidecar 已记录 SHA-256 和来源身份
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[核心观点与 5 分钟版](./summary.zh-CN.md)

## 内容概览

访谈录制于 Meta 宣布收购 Manus 之前，发布时因交易已经公开而成为 Manus 出售前的最后一次长访谈。节目以季逸超和 Manus 在 2025 年的产品、组织与创业漂流为主线。

## 核心议题

- Manus 在 2025 年的产品演进与创业路径
- 季逸超在技术、产品和组织之间的角色
- Agent 产品的能力边界与商业化选择
- 收购发生前团队对公司未来的判断

## 待补充

- [x] 通过发布者 RSS GUID 核对官方期号
- [x] 核对 Bilibili 视频的 aid、cid 和 page
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取并验证本地独立音轨及来源 sidecar
- [x] 使用 Qwen3-ASR 与 ForcedAligner 生成机器逐字稿
- [ ] 校对专有名词、断句和识别错误
- [ ] 增加主持人与嘉宾的说话人区分
- [x] 基于完整机器逐字稿生成总结草稿
- [ ] 核听总结引用的关键片段并完成必要事实核查
