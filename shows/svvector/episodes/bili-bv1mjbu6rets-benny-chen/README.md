---
schema_version: 1
kind: episode
id: "svvector:bili-bv1mjbu6rets"
show_id: svvector
episode_key: bili-bv1mjbu6rets
episode_number: null
slug: bili-bv1mjbu6rets-benny-chen
release_type: regular
numbering:
  status: unknown
  checked_at: 2026-08-16
  source: publisher-feed
  url: https://www.xiaoyuzhoufm.com/episode/6a80b9d136641f136d88c76b
  note: "发布者官方小宇宙节目页收录对应单集，但未给出正式期号；不按列表位置推导"
title: "【视频播客】硅谷坐标 x Fireworks 联创Benny Chen：开源模型、token增速、推理优化和模型定制"
navigation_title: "Benny Chen · 开源模型与推理平台"
catalog_keyword: "Fireworks"
published_at: "2026-08-16T03:41:53+08:00"
duration_ms: 2705152
language: zh-CN
participants:
  - id: cao-qingyun
    name: 曹卿云
    aliases: []
    role: host
  - id: benny-chen
    name: Benny Chen
    aliases:
      - 陈宇飞
    role: guest
    profile:
      headline: "Fireworks AI 联合创始人，前 Meta 广告基础设施负责人"
      affiliations:
        - organization: "Fireworks AI"
          title: "联合创始人"
          status: current
        - organization: "Meta"
          title: "广告基础设施负责人"
          status: former
      education:
        - institution: "UCLA"
      checked_at: 2026-08-16
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1mJbU6REts/
    preferred: true
    identifiers:
      bvid: BV1mJbU6REts
      aid: "117101209654493"
      cid: "40948794048"
      page: 1
  - platform: xiaoyuzhou
    kind: episode
    url: https://www.xiaoyuzhoufm.com/episode/6a80b9d136641f136d88c76b
    identifiers:
      eid: 6a80b9d136641f136d88c76b
      pid: 69a4b82b27e15c06061cfc2d
      media_id: 69a4b82b27e15c06061cfc2d/llroDDKiS2gbxQZCASbPtoDFS78p.m4a
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
    sha256: fba7e981b326039511e3741da09f29c74d8d6e94d833a001c1af2a1bc501cb0b
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
    planned_chunk_count: 12
    effective_total_token_budget: 49152
    max_sentence_characters: 160
  generated_at: "2026-08-16T04:43:45.167349Z"
  quality:
    source_chunks: 12
    aligned_chunks: 12
    alignment_items: 13883
    sentence_segments: 385
    refined_segments: 385
    rendered_blocks: 94
    rendered_lines: 385
  performance:
    model_load_seconds: 0.201
    transcription_seconds: 104.737
    prompt_tokens: 35381
    generation_tokens: 9594
    prompt_tokens_per_second: 337.81
    generation_tokens_per_second: 91.601
    aligner_load_seconds: 0.144
    alignment_seconds: 15.82
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
    generated_at: "2026-08-16T04:43:45.167349Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/svvector/bili-bv1mjbu6rets-benny-chen/source.m4a
  metadata_path: .cache/media/svvector/bili-bv1mjbu6rets-benny-chen/source.metadata.json
  git_ignored: true
  extractor: BiliBili
  acquired_at: "2026-08-16T04:13:59.466575Z"
  verified_at: "2026-08-16T04:13:59.466575Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 28585650
  duration_ms: 2705152
  sha256: 0cf34ca5bf4841e68e10b5e59e37b12160639b461b390748a25071ed7e538666
last_verified_at: 2026-08-16
---

# 【视频播客】硅谷坐标 x Fireworks 联创Benny Chen：开源模型、token增速、推理优化和模型定制

> 本页保留 Bilibili 与小宇宙发布者材料形成的内容提纲，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 节目：硅谷坐标 SV-Vector
- 主持人：曹卿云
- 嘉宾：Benny Chen（陈宇飞），Fireworks AI 联合创始人（身份来自发布者简介）
- 发布时间：2026-08-16 03:41:53（UTC+8）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1mJbU6REts/) · [小宇宙单集](https://www.xiaoyuzhoufm.com/episode/6a80b9d136641f136d88c76b)
- 编号状态：发布者没有给出正式期号，保留 `episode_number: null`
- 字幕状态：未发现匿名公开字幕轨；平台提示字幕查询需要登录，未使用登录态
- 转载边界：Bilibili 公开元数据标记 `no_reprint: 1`
- 本地音轨：00:45:05.152（AAC、48 kHz、双声道）
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

曹卿云与 Fireworks AI 联合创始人 Benny Chen 讨论开源与闭源模型的产业格局、企业 token 流向、推理优化和定制模型两类业务，以及 Fireworks 与大型云厂商之间的竞合关系。

## 章节概览

> 以下时间码来自发布者简介，并非平台独立章节轨。

- 01:23 — 开源与闭源模型的产业格局
- 03:00 — 蒸馏与非蒸馏路线
- 10:18 — Fireworks 平台的 token 增长来源
- 17:35 — Coding 渗透率与市场空间
- 22:11 — 企业如何权衡开源、闭源、本地与云端部署
- 27:00 — 推理优化与定制模型两类业务
- 36:20 — Fireworks 与云厂商的竞合
- 40:29 — RSI 自动化后的核心竞争力
- 41:39 — 大厂 CapEx 与开源模型的投入回报

## 核心议题

- 开源模型与闭源前沿模型的长期分工
- 企业 AI 应用的 token 流向与成本结构
- 推理优化、模型定制与评估体系
- Fireworks 与 AWS、Azure、GCP 的竞合
- 大厂资本开支与基础设施平台的机会

## 待补充

- [x] 核对 BVID、aid、cid、page、节目 PID 与单集 EID
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取公开音轨并完成媒体校验
- [x] 生成 Qwen3-ASR 机器逐字稿及可复现产物链
- [x] 基于完整逐字稿形成独立总结草稿
- [ ] 回听并校对专有名词与高影响事实
