---
schema_version: 1
kind: episode
id: "latetalk:174"
show_id: latetalk
episode_key: "174"
episode_number: 174
slug: 174-yuan-xin
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-07
  source: publisher-website
  note: "晚点聊官网与官方 RSS 明确标为 174 期"
title: "AI 冲击企业软件巨头？与SAP原欣聊大模型 to B 的颠覆与边界【晚点聊LateTalk】"
navigation_title: "原欣 · 企业软件的 AI 颠覆与边界"
catalog_keyword: "SAP"
published_at: "2026-07-28T21:55:19+08:00"
duration_ms: 5505000
language: zh-CN
participants:
  - id: cheng-manqi
    name: 程曼祺
    role: host
    aliases:
      - 曼祺
  - id: yuan-xin
    name: 原欣
    role: guest
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1zQ3i6YErP/
    preferred: true
    identifiers:
      bvid: BV1zQ3i6YErP
      aid: "116997912272759"
      cid: "40381450847"
      page: 1
  - platform: website
    kind: episode
    url: https://podcast.latepost.com/174
    identifiers:
      episode_number: "174"
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
    sha256: 474ad69c1897b80c35e59389f974efd0a864cac00661bc52c953212732eb1e84
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
  generated_at: "2026-08-07T10:20:51.189585Z"
  quality:
    source_chunks: 23
    aligned_chunks: 23
    alignment_items: 24863
    sentence_segments: 595
    refined_segments: 594
    rendered_blocks: 194
    rendered_lines: 594
  performance:
    model_load_seconds: 1.576
    transcription_seconds: 215.056
    prompt_tokens: 71970
    generation_tokens: 16545
    prompt_tokens_per_second: 334.703
    generation_tokens_per_second: 76.944
    aligner_load_seconds: 0.236
    alignment_seconds: 44.578
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
    generated_at: "2026-08-07T10:20:51.189585Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/latetalk/174-yuan-xin/source.m4a
  metadata_path: .cache/media/latetalk/174-yuan-xin/source.metadata.json
  git_ignored: true
  extractor: BiliBili
  acquired_at: "2026-08-07T09:39:26.584283Z"
  verified_at: "2026-08-07T09:39:26.584283Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 70565898
  duration_ms: 5504107
  sha256: ac0ec5e48d2777cec861c3e16695e3d0aa229b22f57d465cc06781464826c071
last_verified_at: 2026-08-07
---

# AI 冲击企业软件巨头？与SAP原欣聊大模型 to B 的颠覆与边界【晚点聊LateTalk】

> 本页保留发布者简介形成的内容提纲，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 节目：晚点聊 LateTalk #174
- 主持人：程曼祺
- 嘉宾：原欣，SAP 大中华地区总裁
- Bilibili 发布时间：2026-07-28 21:55:19（UTC+8）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1zQ3i6YErP/) · [官方节目页](https://podcast.latepost.com/174)
- 字幕状态：未发现匿名公开字幕轨；平台提示字幕查询需要登录，未使用 cookies 或登录态
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

发布者简介称，本期讨论大模型与 AI coding 对企业软件的冲击，SAP 的数据、流程和行业经验是否仍构成壁垒，以及自主运营企业、FDE、计费方式与组织变革的演进边界。本期由 SAP 支持播出，相关业务数据与判断尚未独立核查。

## 章节概览

官方节目页按企业软件壁垒、自主运营企业、FDE 与中国企业采用 AI 四组议题提供时间线；最终总结将以完整正式逐字稿中的实际时间码为准。

## 核心议题

- AI coding 对传统企业软件形态的影响
- 数据治理、流程和业务理解是否仍是长期壁垒
- Agent 与 human in the loop 的现实边界
- FDE、商业模式和企业组织变革

## 待补充

- [x] 核对 BVID、aid、cid、page、正式期号与参与者
- [x] 检查匿名访问可见的平台字幕轨并记录边界
- [x] 获取公开音轨并完成编码、时长、大小和哈希校验
- [x] 生成 Qwen3-ASR 机器逐字稿及完整 lineage
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 核听关键片段、校对专有名词并核查高影响事实
