---
schema_version: 1
kind: episode
id: "latetalk:177"
show_id: latetalk
episode_key: "177"
episode_number: 177
slug: 177-zhao-chenyang-zeng-zhiyuan
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-07
  source: publisher-website
  note: "晚点聊官网与小宇宙均明确标为 177 期"
title: "详解 Kimi K3：强到冲击 Anthropic 估值的模型什么样？【晚点聊LateTalk】"
navigation_title: "赵晨阳、曾致远 · Kimi K3 架构与开源争议"
catalog_keyword: "Kimi K3"
published_at: "2026-08-06T12:00:00+08:00"
duration_ms: 6918997
language: zh-CN
participants:
  - id: cheng-manqi
    name: 程曼祺
    role: host
    aliases:
      - 曼祺
  - id: zhao-chenyang
    name: 赵晨阳
    role: guest
    profile:
      headline: "RadixArk 创始成员、SGLang 核心开发者"
      affiliations:
        - organization: "RadixArk"
          title: "创始成员、SGLang 核心开发者"
          status: current
      checked_at: "2026-08-07"
  - id: zeng-zhiyuan
    name: 曾致远
    role: guest
    profile:
      headline: "华盛顿大学博士生"
      education:
        - institution: "华盛顿大学"
          credential: "博士在读"
      checked_at: "2026-08-07"
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1nWM26QEu5/
    preferred: true
    identifiers:
      bvid: BV1nWM26QEu5
      aid: "117043512743699"
      cid: "40627798779"
      page: 1
  - platform: website
    kind: episode
    url: https://podcast.latepost.com/177
    identifiers:
      episode_number: "177"
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
    sha256: e6f65eb50a8cfbcea0ee565019f03d51f99779e7df24dbf1202669189c7bdc66
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
  generated_at: "2026-08-07T08:35:52.533892Z"
  quality:
    source_chunks: 29
    aligned_chunks: 29
    alignment_items: 35989
    sentence_segments: 932
    refined_segments: 932
    rendered_blocks: 235
    rendered_lines: 932
  performance:
    model_load_seconds: 2.043
    transcription_seconds: 280.983
    prompt_tokens: 90474
    generation_tokens: 24774
    prompt_tokens_per_second: 321.993
    generation_tokens_per_second: 88.169
    aligner_load_seconds: 0.252
    alignment_seconds: 57.225
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
    generated_at: "2026-08-07T08:35:52.533892Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/latetalk/177-zhao-chenyang-zeng-zhiyuan/source.m4a
  metadata_path: .cache/media/latetalk/177-zhao-chenyang-zeng-zhiyuan/source.metadata.json
  git_ignored: true
  extractor: BiliBili
  acquired_at: "2026-08-07T08:22:31.600649Z"
  verified_at: "2026-08-07T08:22:31.600649Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 84572666
  duration_ms: 6918997
  sha256: 8510e3a078c9ed3e1166da7e06e0a1d70036dda7593f7a87d25ac8749b0f6031
last_verified_at: 2026-08-07
---

# 详解 Kimi K3：强到冲击 Anthropic 估值的模型什么样？【晚点聊LateTalk】

> 本页保留发布者简介形成的内容提纲，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 节目：晚点聊 LateTalk #177
- 主持人：程曼祺
- 嘉宾：赵晨阳（RadixArk 创始成员、SGLang 核心开发者）、曾致远（华盛顿大学博士生）；身份来自发布者简介
- 发布时间：2026-08-06 12:00:00（UTC+8）
- Bilibili 平台时长：01:55:19
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1nWM26QEu5/) · [官方节目页](https://podcast.latepost.com/177)
- 字幕状态：未发现匿名公开字幕轨；平台同时提示字幕查询需要登录，未使用 cookies 或登录态
- 本地 Bilibili 音轨：01:55:18.997（AAC、48 kHz、双声道）
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

发布者简介称，本期从推理系统与算法两条线拆解 Kimi K3，讨论其 2.8T 总参数、104B 激活参数、原生多模态与百万上下文等公开技术信息，并延伸到 K3 在美国 AI 圈和投资市场引起的关注，以及与该模型相关的开源争论。技术数字与市场影响均为发布者材料中的说法，尚未独立核查。

## 章节概览

Bilibili 匿名元数据未提供平台章节。

## 核心议题

- Kimi K3 的模型架构、推理方式与训练重点
- 大规模稀疏模型在性能与部署成本之间的权衡
- 原生多模态、百万上下文和 Agent 能力的实际含义
- 开放权重对研究、产业竞争和估值叙事的影响

## 待补充

- [x] 核对 BVID、aid、cid、page、正式期号与参与者
- [x] 检查匿名访问可见的平台字幕轨并记录边界
- [x] 获取公开音轨并完成编码、时长、大小和哈希校验
- [x] 生成 Qwen3-ASR 机器逐字稿及旧版产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 核听关键片段、校对专有名词并核查高影响事实
