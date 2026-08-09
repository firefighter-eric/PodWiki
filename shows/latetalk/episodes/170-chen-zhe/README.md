---
schema_version: 1
kind: episode
id: "latetalk:170"
show_id: latetalk
episode_key: "170"
episode_number: 170
slug: 170-chen-zhe
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-07
  source: publisher-website
  note: "晚点聊官网与官方 RSS 明确标为 170 期"
title: "具身季报 26Q2：世界模型大风不停，和不想被贴标签的人【晚点聊LateTalk】"
navigation_title: "陈哲 · 具身季报、世界模型与路线选择"
catalog_keyword: "具身季报"
published_at: "2026-07-28T13:01:47+08:00"
duration_ms: 6831000
language: zh-CN
participants:
  - id: cheng-manqi
    name: 程曼祺
    role: host
    aliases:
      - 曼祺
  - id: chen-zhe
    name: 陈哲
    role: guest
    profile:
      headline: "Alphaist Partners 创始合伙人"
      affiliations:
        - organization: "Alphaist Partners"
          title: "创始合伙人"
          status: current
      checked_at: "2026-08-07"
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1Eb3Y6QEMs/
    preferred: true
    identifiers:
      bvid: BV1Eb3Y6QEMs
      aid: "116995831894171"
      cid: "40365068028"
      page: 1
  - platform: website
    kind: episode
    url: https://podcast.latepost.com/170
    identifiers:
      episode_number: "170"
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
    sha256: 684d86cd47692bf245f65d5baf56dbb2606c0a83718c1a140fa057f7e0d503aa
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
  generated_at: "2026-08-07T09:54:27.867548Z"
  quality:
    source_chunks: 29
    aligned_chunks: 29
    alignment_items: 34671
    sentence_segments: 819
    refined_segments: 819
    rendered_blocks: 230
    rendered_lines: 819
  performance:
    model_load_seconds: 2.067
    transcription_seconds: 262.748
    prompt_tokens: 89325
    generation_tokens: 22575
    prompt_tokens_per_second: 339.968
    generation_tokens_per_second: 85.92
    aligner_load_seconds: 0.238
    alignment_seconds: 60.085
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
    generated_at: "2026-08-07T09:54:27.867548Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/latetalk/170-chen-zhe/source.m4a
  metadata_path: .cache/media/latetalk/170-chen-zhe/source.metadata.json
  git_ignored: true
  extractor: BiliBili
  acquired_at: "2026-08-07T09:40:04.113737Z"
  verified_at: "2026-08-07T09:40:04.113737Z"
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 87391942
  duration_ms: 6830753
  sha256: aa8ca416d3ac4f202034a4d955d1b468d7e954fc12c2ffba875eb7e32961998a
last_verified_at: 2026-08-07
---

# 具身季报 26Q2：世界模型大风不停，和不想被贴标签的人【晚点聊LateTalk】

> 本页保留发布者简介形成的内容提纲，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 节目：晚点聊 LateTalk #170
- 主持人：程曼祺
- 嘉宾：陈哲，Alphaist Partners 创始合伙人
- Bilibili 发布时间：2026-07-28 13:01:47（UTC+8）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1Eb3Y6QEMs/) · [官方节目页](https://podcast.latepost.com/170)
- 字幕状态：未发现匿名公开字幕轨；平台提示字幕查询需要登录，未使用 cookies 或登录态
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

发布者简介称，本期以第二季度五项具身智能进展为线索，讨论人形机器人马拉松、Figure 的物流直播、灵巧手、英伟达 Cosmos 3 与世界模型投资热，以及 Gen-1、π0.7 等具身模型路线。

## 章节概览

官方节目页按 Q2 总览、人形马拉松、Figure、灵巧操作、世界模型和具身模型提供时间线；最终总结将以完整正式逐字稿中的实际时间码为准。

## 核心议题

- 人形机器人展示与真实部署之间的差距
- 灵巧手、遥操作和数据采集范式
- 世界模型的路线分类与投资热度
- 通用具身模型、产业落地和推进智能的取舍

## 待补充

- [x] 核对 BVID、aid、cid、page、正式期号与参与者
- [x] 检查匿名访问可见的平台字幕轨并记录边界
- [x] 获取公开音轨并完成编码、时长、大小和哈希校验
- [x] 生成 Qwen3-ASR 机器逐字稿及完整 lineage
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 核听关键片段、校对专有名词并核查高影响事实
