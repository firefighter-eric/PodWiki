---
schema_version: 1
kind: episode
id: "luoyonghao:007"
show_id: luoyonghao
episode_key: "007"
episode_number: 7
slug: 007-song-fangjin
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-09
  source: publisher-bilibili-description
  url: https://www.bilibili.com/video/BV1ogWqzCEQu/
  note: "发布者 Bilibili 简介明确写明《罗永浩的十字路口》第 7 期"
title: "【正片】宋方金×罗永浩！故事必须有人讲下去"
navigation_title: "宋方金 · 故事、创作与影视行业"
catalog_keyword: "影视创作"
published_at: "2025-10-17T12:00:00+08:00"
duration_ms: 19402773
language: zh-CN
participants:
  - id: luo-yonghao
    name: "罗永浩"
    aliases: []
    role: host
  - id: song-fangjin
    name: "宋方金"
    aliases: []
    role: guest
sources:
  - platform: bilibili
    kind: video
    title: "【正片】宋方金×罗永浩！故事必须有人讲下去"
    url: https://www.bilibili.com/video/BV1ogWqzCEQu/
    preferred: true
    identifiers:
      bvid: BV1ogWqzCEQu
      aid: "115383960865362"
      cid: "33129955684"
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
    sha256: f24bd1d458f7563693ffd8aafa99243f8556f36d66461a73aa5a89ca65b162e4
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
    max_sentence_characters: 160
  generated_at: "2026-08-09T13:59:33.079323Z"
  quality:
    source_chunks: 81
    aligned_chunks: 81
    alignment_items: 94254
    sentence_segments: 2646
    refined_segments: 2645
    rendered_blocks: 661
    rendered_lines: 2645
  performance:
    model_load_seconds: 2.19
    transcription_seconds: 1941.232
    prompt_tokens: 253710
    generation_tokens: 66417
    prompt_tokens_per_second: 130.705
    generation_tokens_per_second: 34.216
    aligner_load_seconds: 0.956
    alignment_seconds: 216.066
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
    generated_at: "2026-08-09T13:59:33.079323Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/luoyonghao/007-song-fangjin/source.m4a
  metadata_path: .cache/media/luoyonghao/007-song-fangjin/source.metadata.json
  git_ignored: true
  recovered_at: "2026-08-09T12:31:55.443829Z"
  verified_at: "2026-08-09T12:31:55.443829Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 291081751
  duration_ms: 19402773
  sha256: 205f76add2e5058a125352218fb447b82cb22fca3baea49c23f78ccff1bafaa5
last_verified_at: 2026-08-09
---

# 【正片】宋方金×罗永浩！故事必须有人讲下去

> 本页保留发布者材料形成的内容提纲，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 节目：罗永浩的十字路口（第 7 期）
- 主持人：罗永浩
- 嘉宾：宋方金
- 发布时间：2025-10-17 12:00:00（UTC+8）
- Bilibili 视频时长：05:23:23
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1ogWqzCEQu/)
- 来源状态：公开单 P；匿名访问未发现公开字幕轨；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 本地音频：AAC、48 kHz、双声道、291,081,751 字节
- 编号状态：发布者材料明确为第 7 期
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

发布者以宋方金的编剧与讲述经验为核心，围绕故事创作、电影和影视行业展开长谈，并突出他对行业问题的直接观察。

## 章节概览

- `[00:00:00]` 拜访莫言
- `[01:36:00]` 罗永浩打脸表情包
- `[02:07:25]` 张艺谋见外星人
- `[03:28:25]` 作家网红化
- `[05:02:59]` 编剧方法论
- `[05:07:01]` 电影行业未来

## 核心议题

- 故事与编剧创作方法
- 电影和影视行业观察
- 讲述者的责任与表达边界

## 待补充

- [x] 核对 BVID、aid、cid、page、正式期号与参与者
- [x] 检查匿名访问可见的平台字幕轨并记录边界
- [x] 获取公开音轨并完成编码、时长、大小和哈希校验
- [x] 生成完整 Qwen3-ASR 机器逐字稿及 v2 产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 核听关键片段、校对专有名词并核查高影响事实
