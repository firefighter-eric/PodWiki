---
schema_version: 1
kind: episode
id: "latetalk:164"
show_id: latetalk
episode_key: "164"
episode_number: 164
slug: 164-wu-minghui
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-16
  source: publisher-website
  note: "晚点聊官方节目页与 RSS 标题明确标为 164 期"
title: "当AI杀死SaaS，明略吴明辉聊多Agent网络、软件转型、AI新组织"
navigation_title: "吴明辉 · 多 Agent 网络与软件转型"
catalog_keyword: "Agent 网络"
published_at: "2026-05-14T20:06:24+08:00"
duration_ms: 8938197
language: zh-CN
participants:
  - id: wu-minghui
    name: 吴明辉
    aliases: []
    role: guest
    profile:
      headline: "明略科技创始人"
      affiliations:
        - organization: "明略科技"
          title: "创始人"
          status: current
      checked_at: 2026-08-16
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1ma5X6wEwb/
    preferred: true
    identifiers:
      bvid: BV1ma5X6wEwb
      aid: "116572777616627"
      cid: "38330501899"
      page: 1
  - platform: website
    kind: episode
    url: https://podcast.latepost.com/164
    identifiers:
      episode_number: "164"
      rss_guid: ca5acce8-68a5-4ae0-b58c-bc9af6e572d7
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
    sha256: 769293a21ea63a78e8ac7008291a8e29f0fbe3a4b39441b0b05a3aabba545e2d
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
    planned_chunk_count: 38
    effective_total_token_budget: 155648
    max_sentence_characters: 160
  generated_at: "2026-08-16T04:25:53.924498Z"
  quality:
    source_chunks: 38
    aligned_chunks: 38
    alignment_items: 56050
    sentence_segments: 1687
    refined_segments: 1687
    rendered_blocks: 295
    rendered_lines: 1687
  performance:
    model_load_seconds: 0.201
    transcription_seconds: 398.866
    prompt_tokens: 116885
    generation_tokens: 37876
    prompt_tokens_per_second: 293.044
    generation_tokens_per_second: 94.959
    aligner_load_seconds: 0.139
    alignment_seconds: 58.24
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
    generated_at: "2026-08-16T04:25:53.924498Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/latetalk/164-wu-minghui/source.m4a
  metadata_path: .cache/media/latetalk/164-wu-minghui/source.metadata.json
  git_ignored: true
  extractor: BiliBili
  acquired_at: "2026-08-16T04:13:43.636794Z"
  verified_at: "2026-08-16T04:13:43.636794Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 102730997
  duration_ms: 8938197
  sha256: 497ddaea6ad9084c4098b65d5ad5f0db72603fec9d2300f9b22c1b029444a679
last_verified_at: 2026-08-16
---

# 当AI杀死SaaS，明略吴明辉聊多Agent网络、软件转型、AI新组织

> 本页保留发布者简介形成的内容提纲，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 节目：晚点聊 LateTalk #164
- 嘉宾：吴明辉，明略科技创始人（身份来自发布者简介）
- 发布时间：2026-05-14 20:06:24（UTC+8）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1ma5X6wEwb/) · [官方节目页](https://podcast.latepost.com/164)
- 字幕状态：未发现匿名公开字幕轨；平台提示字幕查询需要登录，未使用登录态
- 本地音轨：02:28:58.197（AAC、48 kHz、双声道）
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

发布者简介以明略过去的 AI 组织实践为背景，讨论大模型和 Agent 如何改变 SaaS、软件公司与既有组织，并介绍明略计划开源的多 Agent 协同网络“章鱼”。

## 章节概览

Bilibili 匿名元数据未提供平台章节。

## 核心议题

- AI 对 SaaS 和传统软件的冲击
- 明略历次 AI 组织实践的经验
- 多 Agent 协同网络“章鱼”
- 既有公司如何完成 AI 驱动的组织转型

## 待补充

- [x] 核对 BVID、aid、cid、page、正式期号与嘉宾
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取公开音轨并完成媒体校验
- [x] 生成 Qwen3-ASR 机器逐字稿及可复现产物链
- [x] 基于完整逐字稿形成独立总结草稿
- [ ] 回听并校对专有名词与高影响事实
