---
schema_version: 1
kind: episode
id: "luoyonghao:016"
show_id: luoyonghao
episode_key: "016"
episode_number: 16
slug: 016-chen-mian
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-09
  source: publisher-rss-description
  url: https://feed.xyzfm.space/wmnkvmrpwuww
title: "【正片】Lovart 创始人陈冕×罗永浩！且让我大闹一场，然后悄然离去"
navigation_title: "陈冕 · Lovart 与连续创业"
catalog_keyword: "Lovart"
published_at: "2026-01-09T13:37:58+08:00"
duration_ms: 13472362
language: zh-CN
participants:
  - id: luo-yonghao
    name: "罗永浩"
    aliases: []
    role: host
  - id: chen-mian
    name: "陈冕"
    aliases: []
    role: guest
sources:
  - platform: bilibili
    kind: video
    title: "【正片】Lovart 创始人陈冕×罗永浩！且让我大闹一场，然后悄然离去"
    url: https://www.bilibili.com/video/BV14eiQBmEbN/
    preferred: true
    identifiers:
      bvid: BV14eiQBmEbN
      aid: "115858454086686"
      cid: "35275474874"
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
    sha256: 28bccd9c58dba10f81789421c12e6c873dd7dfb3d2587c2ae1f28d68df6bb68a
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
    planned_chunk_count: 57
    effective_total_token_budget: 233472
    max_sentence_characters: 160
  generated_at: "2026-08-09T15:36:07.175067Z"
  quality:
    source_chunks: 57
    aligned_chunks: 57
    alignment_items: 68263
    sentence_segments: 2166
    refined_segments: 2166
    rendered_blocks: 451
    rendered_lines: 2166
  performance:
    model_load_seconds: 0.2
    transcription_seconds: 600.317
    prompt_tokens: 176173
    generation_tokens: 47944
    prompt_tokens_per_second: 293.464
    generation_tokens_per_second: 79.864
    aligner_load_seconds: 0.168
    alignment_seconds: 90.564
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
    generated_at: "2026-08-09T15:36:07.175067Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/luoyonghao/016-chen-mian/source.m4a
  metadata_path: .cache/media/luoyonghao/016-chen-mian/source.metadata.json
  git_ignored: true
  recovered_at: "2026-08-09T12:32:05.998116Z"
  verified_at: "2026-08-09T12:32:05.998116Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 198166390
  duration_ms: 13472362
  sha256: 1bd849b5c59ba2f4013195ef85f0b2ed60c3cf8e5010b44fc050a538b044228b
last_verified_at: 2026-08-09
---

# 【正片】Lovart 创始人陈冕×罗永浩！且让我大闹一场，然后悄然离去

> 本页保留发布者材料形成的内容提纲，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 节目：罗永浩的十字路口（第 16 期）
- 主持人：罗永浩
- 嘉宾：陈冕
- 发布时间：2026-01-09 13:37:58（UTC+8）
- Bilibili 视频时长：03:44:32
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV14eiQBmEbN/)
- 来源状态：公开单 P；匿名访问未发现公开字幕轨；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 本地音频：AAC、48 kHz、双声道、198,166,390 字节
- 编号状态：发布者材料明确为第 16 期
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

发布者把陈冕在多家互联网公司的经历视为创业准备，围绕他创立 Lovart 前后的观察、积累与行动展开。

## 章节概览

- `[00:00:00]` 生于重庆
- `[00:19:06]` 大学经历
- `[00:37:47]` 游遍大厂
- `[01:00:28]` 转战字节
- `[01:18:40]` 残酷竞争
- `[01:33:41]` 准备创业
- `[02:46:24]` 同行观察
- `[03:04:38]` 展望未来
- `[03:33:53]` 终极风险

## 核心议题

- 互联网公司经历与能力积累
- Lovart 的创业起点
- 连续尝试、判断与行动

## 待补充

- [x] 核对 BVID、aid、cid、page、正式期号与参与者
- [x] 检查匿名访问可见的平台字幕轨并记录边界
- [x] 获取公开音轨并完成编码、时长、大小和哈希校验
- [x] 生成完整 Qwen3-ASR 机器逐字稿及 v2 产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 核听关键片段、校对专有名词并核查高影响事实
