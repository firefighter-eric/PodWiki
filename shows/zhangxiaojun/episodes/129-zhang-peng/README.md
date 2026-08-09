---
schema_version: 1
kind: episode
id: "zhangxiaojun:129"
show_id: zhangxiaojun
episode_key: "129"
episode_number: 129
slug: 129-zhang-peng
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-06
  source: publisher-rss
title: "全球大模型第一股的上市访谈，和智谱 CEO 张鹏聊：敢问路在何方？"
navigation_title: "张鹏 · 智谱上市、GLM 与 AGI 商业化"
catalog_keyword: "GLM"
published_at: "2026-01-08T09:09:14+08:00"
duration_ms: 8799000
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: zhang-peng
    name: 张鹏
    role: guest
    profile:
      headline: "智谱 CEO"
      affiliations:
        - organization: "智谱"
          title: "CEO"
          status: current
      checked_at: "2026-08-06"
sources:
  - platform: rss
    kind: feed-item
    url: https://www.xiaoyuzhoufm.com/episode/695f008dc1e012a7abf0be09
    preferred: false
    identifiers:
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 695f008dc1e012a7abf0be09
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1awiDBDEWS/
    preferred: true
    identifiers:
      bvid: BV1awiDBDEWS
      aid: "115857313300913"
      cid: "35254307482"
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
    sha256: e2992a775ba792dd707359bf4aca79d738615b14e3ab0dabc7b6e5588a29bbdd
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
  generated_at: "2026-08-06T07:35:39.507312Z"
  quality:
    source_chunks: 37
    aligned_chunks: 37
    alignment_items: 47199
    sentence_segments: 1711
    refined_segments: 1709
    rendered_blocks: 286
    rendered_lines: 1709
  performance:
    model_load_seconds: 2.264
    transcription_seconds: 378.535
    prompt_tokens: 113447
    generation_tokens: 32161
    prompt_tokens_per_second: 299.704
    generation_tokens_per_second: 84.963
    aligner_load_seconds: 0.219
    alignment_seconds: 72.65
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
    generated_at: "2026-08-06T07:35:39.507312Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/129-zhang-peng/source.m4a
  metadata_path: .cache/media/zhangxiaojun/129-zhang-peng/source.metadata.json
  git_ignored: true
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 116413550
  duration_ms: 8675161
  sha256: 82bebc68a2b342cc37d2efaec34a82f1aef647ace6c25dd780871e489d2e67b5
  acquired_at: "2026-08-06T06:57:52.961494Z"
  verified_at: "2026-08-06T06:57:52.961494Z"
last_verified_at: 2026-08-06
---

# 全球大模型第一股的上市访谈，和智谱 CEO 张鹏聊：敢问路在何方？

> 本页保留发布者简介形成的概览；完整 Qwen3-ASR 机器逐字稿和基于全文的总结草稿已生成，关键片段尚未核听，也未完成独立事实核查。

## 单集信息

- 节目：张小珺商业访谈录（第 129 期）
- 主持人：张小珺
- 嘉宾：张鹏，智谱 CEO
- 发布时间：2026-01-08 09:09（UTC+8）
- 官方 RSS 时长：02:26:39；Bilibili 视频时长：02:24:35
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/695f008dc1e012a7abf0be09)、[Bilibili 视频](https://www.bilibili.com/video/BV1awiDBDEWS/)
- 字幕状态：匿名访问未发现公开字幕轨

## 内容概览

访谈发生在智谱上市前夕，围绕公司成为“全球大模型第一股”的意义、商业化与研发路线，以及张鹏希望智谱在未来 AI 历史中扮演怎样的角色展开。

## 核心议题

- 大模型公司的上市与资本市场检验
- 智谱的模型、产品与商业化路线
- 中国大模型公司之间的竞争格局
- “AGI 先行者”定位及其组织含义

## 待补充

- [x] 通过发布者 RSS GUID 核对官方期号
- [x] 核对 Bilibili 视频的 aid、cid 和 page
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取并验证本地独立音轨及来源 sidecar
- [x] 使用 Qwen3-ASR 与 ForcedAligner 生成机器逐字稿
- [x] 基于完整机器逐字稿生成总结草稿
- [ ] 核听总结引用的关键片段并完成必要事实核查
