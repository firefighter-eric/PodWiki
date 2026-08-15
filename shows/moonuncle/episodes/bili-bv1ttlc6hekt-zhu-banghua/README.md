---
schema_version: 1
kind: episode
id: "moonuncle:bili-bv1ttlc6hekt"
show_id: moonuncle
episode_key: bili-bv1ttlc6hekt
episode_number: null
slug: bili-bv1ttlc6hekt-zhu-banghua
release_type: regular
numbering:
  status: unknown
  checked_at: 2026-08-09
  source: publisher-season
  note: "官方播客合集仅标注为正片，标题与简介未提供正式期号；不根据合集顺序推导"
title: "朱邦华: SGLang，强化学习，英伟达收购，二次创业，清华，伯克利，LMSYS，Chatbot Arena，勇于放弃"
navigation_title: "朱邦华 · SGLang 与强化学习创业"
catalog_keyword: "SGLang"
published_at: "2026-05-18T13:12:30+08:00"
duration_ms: 6411238
language: zh-CN
participants:
  - id: yueqiu-dashu
    name: 月球大叔
    aliases: []
    role: host
  - id: zhu-banghua
    name: 朱邦华
    aliases: []
    role: guest
sources:
  - platform: bilibili
    kind: video
    title: "朱邦华: SGLang，强化学习，英伟达收购，二次创业，清华，伯克利，LMSYS，Chatbot Arena，勇于放弃"
    url: https://www.bilibili.com/video/BV1TTLc6HEKT/
    preferred: true
    identifiers:
      bvid: BV1TTLc6HEKT
      aid: "116593833021484"
      cid: "38416092709"
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
    sha256: 6a39d96c02b4700e34dd5b0db6dba3f85b644d2ee3c34bbd9b6488d5bda53313
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
  generated_at: "2026-08-09T12:35:50.593309Z"
  quality:
    source_chunks: 27
    aligned_chunks: 27
    alignment_items: 32540
    sentence_segments: 794
    refined_segments: 794
    rendered_blocks: 227
    rendered_lines: 794
  performance:
    model_load_seconds: 1.405
    transcription_seconds: 247.844
    prompt_tokens: 83836
    generation_tokens: 21941
    prompt_tokens_per_second: 338.261
    generation_tokens_per_second: 88.527
    aligner_load_seconds: 0.408
    alignment_seconds: 41.14
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
    generated_at: "2026-08-09T12:35:50.593309Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
    quality:
      source_chunks: 27
      aligned_chunks: 27
      alignment_items: 32540
      sentence_segments: 794
      refined_segments: 794
      rendered_blocks: 227
      rendered_lines: 794
    performance:
      model_load_seconds: 1.405
      transcription_seconds: 247.844
      prompt_tokens: 83836
      generation_tokens: 21941
      prompt_tokens_per_second: 338.261
      generation_tokens_per_second: 88.527
      aligner_load_seconds: 0.408
      alignment_seconds: 41.14
local_audio_cache:
  path: .cache/media/moonuncle/bili-bv1ttlc6hekt-zhu-banghua/source.m4a
  metadata_path: .cache/media/moonuncle/bili-bv1ttlc6hekt-zhu-banghua/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-09T11:58:15.355633Z"
  verified_at: "2026-08-09T11:58:15.355633Z"
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 101449930
  duration_ms: 6411238
  sha256: a5452ccc80580bbb6c64a9ccf21dee504b5cefe5768836c00757b2854cd02213
last_verified_at: 2026-08-09
---

# 朱邦华: SGLang，强化学习，英伟达收购，二次创业，清华，伯克利，LMSYS，Chatbot Arena，勇于放弃

> 本页保留发布者简介形成的概览；另有依据完整机器逐字稿整理的总结草稿，尚未完成关键片段核听和独立事实核查。

## 单集信息

- 节目：月球大叔的硅谷播客
- 主持人：月球大叔
- 嘉宾：朱邦华
- 发布时间：2026-05-18 13:12:30（UTC+8）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1TTLc6HEKT/)
- 编号状态：发布者未提供正式期号，保留 `episode_number: null`
- 本地来源：公开音轨已获取，并通过媒体探测、大小与 SHA-256 校验
- 字幕状态：匿名访问未发现公开字幕轨；平台元数据提示字幕接口需要登录，处理过程未使用 cookies 或登录态
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[核心观点与 5 分钟版](./summary.zh-CN.md)

## 内容概览

发布者以朱邦华从清华、伯克利到两次创业的经历为主线，介绍其参与开源强化学习、第一次创业公司被英伟达收购，以及以 SGLang 为基础再次创业的故事。

## 章节概览

发布者简介未提供带时间点的章节。

## 核心议题

- 从学术研究进入开源与创业
- PPO、SGLang 与大模型强化学习
- 公司被收购后的再次创业选择

## 待补充

- [x] 获取并验证本地独立音轨及来源 sidecar
- [x] 使用 Qwen3-ASR 与 ForcedAligner 生成完整机器逐字稿
- [x] 基于完整机器逐字稿生成总结草稿
- [ ] 校对专有名词、断句和识别错误
- [ ] 增加主持人与嘉宾的说话人区分
- [ ] 核听总结引用的关键片段并完成必要事实核查
