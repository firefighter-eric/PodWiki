---
schema_version: 1
kind: episode
id: "luoyonghao:015"
show_id: luoyonghao
episode_key: "015"
episode_number: 15
slug: 015-liu-jingkang
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-09
  source: publisher-rss-description
  url: https://feed.xyzfm.space/wmnkvmrpwuww
title: "【正片】影石Insta360 创始人刘靖康×罗永浩！比生存更重要的是那些微小的念头"
navigation_title: "刘靖康 · 影石、影像与创业念头"
catalog_keyword: "影石"
published_at: "2025-12-25T12:00:00+08:00"
duration_ms: 15690176
language: zh-CN
participants:
  - id: luo-yonghao
    name: "罗永浩"
    aliases: []
    role: host
  - id: liu-jingkang
    name: "刘靖康"
    aliases: []
    role: guest
sources:
  - platform: bilibili
    kind: video
    title: "【正片】影石Insta360 创始人刘靖康×罗永浩！比生存更重要的是那些微小的念头"
    url: https://www.bilibili.com/video/BV1yhBjBSEzn/
    preferred: true
    identifiers:
      bvid: BV1yhBjBSEzn
      aid: "115774802888711"
      cid: "34980235791"
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
    sha256: 7a2089d4c2d7fe3979741ed5fa06a1bd0603e4a4f66c187fb1e245b36ce3ebca
transcript:
  path: transcript.zh-CN.md
  platform_subtitle_access: no-anonymous-track-login-indicated
  platform_subtitle_languages: []
  automatic_caption_languages: []
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
    planned_chunk_count: 66
    effective_total_token_budget: 270336
    max_sentence_characters: 160
  generated_at: "2026-08-09T15:24:21.983044Z"
  quality:
    source_chunks: 66
    aligned_chunks: 66
    alignment_items: 79995
    sentence_segments: 2586
    refined_segments: 2586
    rendered_blocks: 526
    rendered_lines: 2586
  performance:
    model_load_seconds: 0.19
    transcription_seconds: 720.683
    prompt_tokens: 205165
    generation_tokens: 56333
    prompt_tokens_per_second: 284.679
    generation_tokens_per_second: 78.166
    aligner_load_seconds: 0.183
    alignment_seconds: 105.259
  translations: []
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
    generated_at: "2026-08-09T15:24:21.983044Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/luoyonghao/015-liu-jingkang/source.m4a
  metadata_path: .cache/media/luoyonghao/015-liu-jingkang/source.metadata.json
  git_ignored: true
  recovered_at: "2026-08-09T12:32:04.574324Z"
  verified_at: "2026-08-09T12:32:04.574324Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 244755521
  duration_ms: 15690176
  sha256: 8167e145ec5081cb879f322d9b931a48d0a8b5f20a11b2456d9afece5b7dea55
last_verified_at: 2026-08-09
---

# 【正片】影石Insta360 创始人刘靖康×罗永浩！比生存更重要的是那些微小的念头

> 本页保留发布者材料形成的内容提纲，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 节目：罗永浩的十字路口（第 15 期）
- 主持人：罗永浩
- 嘉宾：刘靖康
- 发布时间：2025-12-25 12:00:00（UTC+8）
- Bilibili 视频时长：04:21:30
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1yhBjBSEzn/)
- 来源状态：公开单 P；匿名访问未发现公开字幕轨；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 本地音频：AAC、48 kHz、双声道、244,755,521 字节
- 编号状态：发布者材料明确为第 15 期
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

发布者围绕刘靖康从技术兴趣和微小念头出发、不断创造产品并创立影石 Insta360 的经历，讨论技术、影像与创业选择。

## 章节概览

- `[00:00:00]` 童年环境
- `[00:48:06]` 大学创业
- `[01:08:40]` 实习经历
- `[01:25:04]` 全景相机
- `[02:10:01]` 爆款产品
- `[02:31:26]` 大赛风波
- `[03:07:35]` 重大决策
- `[03:22:13]` 成功上市
- `[03:43:48]` 发展趋势
- `[04:17:53]` 始于敢想

## 核心议题

- 技术兴趣与早期创造经历
- 影石 Insta360 的创业过程
- 产品念头、生存与长期选择

## 待补充

- [x] 核对 BVID、aid、cid、page、正式期号与参与者
- [x] 检查匿名访问可见的平台字幕轨并记录边界
- [x] 获取公开音轨并完成编码、时长、大小和哈希校验
- [x] 生成完整 Qwen3-ASR 机器逐字稿及 v2 产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 核听关键片段、校对专有名词并核查高影响事实
