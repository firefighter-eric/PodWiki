---
schema_version: 1
kind: episode
id: "luoyonghao:019"
show_id: luoyonghao
episode_key: "019"
episode_number: 19
slug: 019-zhang-weiwei
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-09
  source: publisher-rss-description
  url: https://feed.xyzfm.space/wmnkvmrpwuww
title: "【正片】音乐人张玮玮×罗永浩！我们都是那个“混乱又伟大”的 90 年代的幸存者"
navigation_title: "张玮玮 · 九十年代与独立音乐"
catalog_keyword: "独立音乐"
published_at: "2026-02-11T12:00:00+08:00"
duration_ms: 20389525
language: zh-CN
participants:
  - id: luo-yonghao
    name: "罗永浩"
    aliases: []
    role: host
  - id: zhang-weiwei
    name: "张玮玮"
    aliases: []
    role: guest
sources:
  - platform: bilibili
    kind: video
    title: "【正片】音乐人张玮玮×罗永浩！我们都是那个“混乱又伟大”的 90 年代的幸存者"
    url: https://www.bilibili.com/video/BV1MXFdzsEn2/
    preferred: true
    identifiers:
      bvid: BV1MXFdzsEn2
      aid: "116049697570910"
      cid: "36008559751"
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
    sha256: e4f91c7350812c6f6458590a6378d6a4b0ba472f9ac6ee06b230cf6322d08c2e
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
    planned_chunk_count: 86
    effective_total_token_budget: 352256
    max_sentence_characters: 160
  generated_at: "2026-08-09T16:16:25.404062Z"
  quality:
    source_chunks: 86
    aligned_chunks: 86
    alignment_items: 85751
    sentence_segments: 3012
    refined_segments: 3010
    rendered_blocks: 682
    rendered_lines: 3010
  performance:
    model_load_seconds: 0.187
    transcription_seconds: 908.667
    prompt_tokens: 266617
    generation_tokens: 65107
    prompt_tokens_per_second: 293.413
    generation_tokens_per_second: 71.651
    aligner_load_seconds: 0.262
    alignment_seconds: 127.1
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
    generated_at: "2026-08-09T16:16:25.404062Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/luoyonghao/019-zhang-weiwei/source.m4a
  metadata_path: .cache/media/luoyonghao/019-zhang-weiwei/source.metadata.json
  git_ignored: true
  recovered_at: "2026-08-09T12:32:10.249962Z"
  verified_at: "2026-08-09T12:32:10.249962Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 305782570
  duration_ms: 20389525
  sha256: be5d6327a4678540f97adc83d055a6c6bfe644bf36926799ec5d5c282feee9a5
last_verified_at: 2026-08-09
---

# 【正片】音乐人张玮玮×罗永浩！我们都是那个“混乱又伟大”的 90 年代的幸存者

> 本页保留发布者材料形成的内容提纲，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 节目：罗永浩的十字路口（第 19 期）
- 主持人：罗永浩
- 嘉宾：张玮玮
- 发布时间：2026-02-11 12:00:00（UTC+8）
- Bilibili 视频时长：05:39:50
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1MXFdzsEn2/)
- 来源状态：公开单 P；匿名访问未发现公开字幕轨；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 本地音频：AAC、48 kHz、双声道、305,782,570 字节
- 编号状态：发布者材料明确为第 19 期
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

发布者沿着张玮玮从甘肃白银、广州到北京和大理的经历，回看九十年代的独立音乐环境、流动生活与个人创作。

## 章节概览

- `[00:00:00]` 来自白银
- `[00:01:58]` 厂矿子弟
- `[00:56:04]` 正向反馈
- `[01:29:11]` 组建乐队
- `[02:11:48]` 玩玩朋克
- `[02:54:42]` 河酒吧往事
- `[03:25:53]` 人生困境
- `[04:49:49]` 关于《米店》
- `[05:26:09]` 中年危机
- `[05:36:53]` 嘉宾推荐

## 核心议题

- 九十年代的社会与音乐环境
- 独立音乐人的流动经历
- 创作、生活与自我放逐

## 待补充

- [x] 核对 BVID、aid、cid、page、正式期号与参与者
- [x] 检查匿名访问可见的平台字幕轨并记录边界
- [x] 获取公开音轨并完成编码、时长、大小和哈希校验
- [x] 生成完整 Qwen3-ASR 机器逐字稿及 v2 产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 核听关键片段、校对专有名词并核查高影响事实
