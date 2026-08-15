---
schema_version: 1
kind: episode
id: "moonuncle:bili-bv1x2eq6be1g"
show_id: moonuncle
episode_key: bili-bv1x2eq6be1g
episode_number: null
slug: bili-bv1x2eq6be1g-jiang-junchen
release_type: regular
numbering:
  status: unknown
  checked_at: 2026-08-09
  source: publisher-season
  note: "官方播客合集仅标注为正片，标题与简介未提供正式期号；不根据合集顺序推导"
title: "江鋆晨: 大模型记忆，KV Cache，清华姚班，CMU，教授，开源，视频流媒体"
navigation_title: "江鋆晨 · 大模型记忆与 KV Cache"
catalog_keyword: "LMCache"
published_at: "2026-06-10T12:56:47+08:00"
duration_ms: 8726152
language: zh-CN
participants:
  - id: yueqiu-dashu
    name: 月球大叔
    aliases: []
    role: host
  - id: jiang-junchen
    name: 江鋆晨
    aliases:
      - Jiang Junchen
    role: guest
sources:
  - platform: bilibili
    kind: video
    title: "江鋆晨: 大模型记忆，KV Cache，清华姚班，CMU，教授，开源，视频流媒体"
    url: https://www.bilibili.com/video/BV1x2EQ6BE1g/
    preferred: true
    identifiers:
      bvid: BV1x2EQ6BE1g
      aid: "116723990796165"
      cid: "39000870046"
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
    sha256: 46e46a58c2e59c32fd896cf5b258050fa1140cb0ee61b451703888e374d4aeb7
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
  generated_at: "2026-08-09T12:42:39.243883Z"
  quality:
    source_chunks: 37
    aligned_chunks: 37
    alignment_items: 43398
    sentence_segments: 1014
    refined_segments: 1014
    rendered_blocks: 302
    rendered_lines: 1014
  performance:
    model_load_seconds: 1.814
    transcription_seconds: 344.939
    prompt_tokens: 114107
    generation_tokens: 30039
    prompt_tokens_per_second: 330.803
    generation_tokens_per_second: 87.085
    aligner_load_seconds: 0.277
    alignment_seconds: 53.008
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
    options:
      language: Chinese
      temperature: 0
      max_tokens_per_chunk: 4096
      chunk_duration_seconds: 240
      max_sentence_characters: 160
    generated_at: "2026-08-09T12:42:39.243883Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
    quality:
      source_chunks: 37
      aligned_chunks: 37
      alignment_items: 43398
      sentence_segments: 1014
      refined_segments: 1014
      rendered_blocks: 302
      rendered_lines: 1014
    performance:
      model_load_seconds: 1.814
      transcription_seconds: 344.939
      prompt_tokens: 114107
      generation_tokens: 30039
      prompt_tokens_per_second: 330.803
      generation_tokens_per_second: 87.085
      aligner_load_seconds: 0.277
      alignment_seconds: 53.008
local_audio_cache:
  path: .cache/media/moonuncle/bili-bv1x2eq6be1g-jiang-junchen/source.m4a
  metadata_path: .cache/media/moonuncle/bili-bv1x2eq6be1g-jiang-junchen/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-09T11:58:27.105984Z"
  verified_at: "2026-08-09T11:58:27.105984Z"
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 124620264
  duration_ms: 8726152
  sha256: 487daf7592168fc532f1b3e4b68aa0ae25fc32f4a9fdfc50e095798978e2cc79
last_verified_at: 2026-08-09
---

# 江鋆晨: 大模型记忆，KV Cache，清华姚班，CMU，教授，开源，视频流媒体

> 本页保留发布者简介形成的概览；另有依据完整机器逐字稿整理的总结草稿，尚未完成关键片段核听和独立事实核查。

## 单集信息

- 节目：月球大叔的硅谷播客
- 主持人：月球大叔
- 嘉宾：江鋆晨（Jiang Junchen）
- 发布时间：2026-06-10 12:56:47（UTC+8）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1x2EQ6BE1g/)
- 编号状态：发布者未提供正式期号，保留 `episode_number: null`
- 本地来源：公开音轨已获取，并通过媒体探测、大小与 SHA-256 校验
- 字幕状态：匿名访问未发现公开字幕轨；平台元数据提示字幕接口需要登录，处理过程未使用 cookies 或登录态
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[核心观点与 5 分钟版](./summary.zh-CN.md)

## 内容概览

发布者从江鋆晨在清华姚班、CMU 和视频流媒体领域的经历切入，延伸至 LMCache、KV Cache、大模型记忆、工业界实践、创业与职业选择。

## 章节概览

- `[00:00:00]` 清华姚班
- `[00:15:00]` CMU、Hui Zhang 与 Ion Stoica
- `[00:26:00]` 视频流媒体与大数据
- `[00:37:00]` KV Cache
- `[00:44:00]` 融入工业界
- `[00:55:00]` 高价值问题
- `[01:21:00]` 详解 KV Cache
- `[01:40:00]` Agent 与记忆
- `[01:50:00]` 创业、融资与进化
- `[02:03:00]` 未来基础设施与职业建议

## 核心议题

- 网络多媒体到大模型基础设施的研究路径
- KV Cache、LMCache 与大模型记忆
- 学术、工业界和创业之间的选择

## 待补充

- [x] 获取并验证本地独立音轨及来源 sidecar
- [x] 使用 Qwen3-ASR 与 ForcedAligner 生成完整机器逐字稿
- [x] 基于完整机器逐字稿生成总结草稿
- [ ] 校对专有名词、断句和识别错误
- [ ] 增加主持人与嘉宾的说话人区分
- [ ] 核听总结引用的关键片段并完成必要事实核查
