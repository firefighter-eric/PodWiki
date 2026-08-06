---
schema_version: 1
kind: episode
id: "luoyonghao:013"
show_id: luoyonghao
episode_key: "013"
episode_number: 13
slug: 013-yan-junjie
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-06
  source: publisher-description
title: "MiniMax 创始人闫俊杰 × 罗永浩：大山并非无法翻越"
navigation_title: "闫俊杰 - MiniMax、多模态与全球化"
published_at: "2025-12-10T14:31:12+08:00"
duration_ms: 13889642
language: zh-CN
participants:
  - id: luo-yonghao
    name: 罗永浩
    role: host
  - id: yan-junjie
    name: 闫俊杰
    role: guest
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV11NmtBzE36/
    preferred: true
    identifiers:
      bvid: BV11NmtBzE36
      aid: "115693685049646"
      cid: "34631649758"
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
    sha256: f671bbb5021044f7773c43c6d40d34abe24722f411e71ca093c41c231b57e780
transcript:
  path: transcript.zh-CN.md
  platform_subtitle_access: not-exposed-as-public-track
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
  generated_at: "2026-08-06T08:32:38.969175Z"
  quality:
    source_chunks: 58
    aligned_chunks: 58
    alignment_items: 75115
    sentence_segments: 2566
    refined_segments: 2563
    rendered_blocks: 455
    rendered_lines: 2563
  performance:
    model_load_seconds: 2.095
    transcription_seconds: 564.721
    prompt_tokens: 181621
    generation_tokens: 50059
    prompt_tokens_per_second: 321.676
    generation_tokens_per_second: 88.661
    aligner_load_seconds: 0.234
    alignment_seconds: 119.339
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
    generated_at: "2026-08-06T08:32:38.969175Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/luoyonghao/013-yan-junjie/source.m4a
  metadata_path: .cache/media/luoyonghao/013-yan-junjie/source.metadata.json
  git_ignored: true
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 225278109
  duration_ms: 13889642
  sha256: cb79683b003f117983533cf5c1bbde5644d00b5f5f6c7d0e4dff25e85d478aa7
  acquired_at: "2026-08-06T06:49:07.131519Z"
  verified_at: "2026-08-06T06:49:07.131519Z"
last_verified_at: 2026-08-06
---

# MiniMax 创始人闫俊杰 × 罗永浩：大山并非无法翻越

> 本页保留发布者简介形成的概览；完整 Qwen3-ASR 机器逐字稿和基于全文的总结草稿已生成，关键片段尚未核听，也未完成独立事实核查。

## 单集信息

- 节目：罗永浩的十字路口（第 13 期）
- 主持人：罗永浩
- 嘉宾：闫俊杰，MiniMax 创始人
- 发布时间：2025-12-10 14:31（UTC+8）
- Bilibili 视频时长：03:51:30
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV11NmtBzE36/)
- 字幕状态：匿名访问未发现公开字幕轨；播放器提示登录后可能存在字幕

## 内容概览

发布者简介以闫俊杰从小县城、清华求学、商汤工作到创立 MiniMax 的经历为主线，讨论他如何判断 AI 革命的窗口、为何离开成熟组织创业，以及希望让 AI 从少数精英工具变成普惠生产力的长期目标。

## 核心议题

- 闫俊杰的教育、研究与产业经历
- 从商汤到创立 MiniMax 的关键选择
- 中国大模型公司的全球竞争与产品普惠
- 创业者如何面对技术浪潮中的风险、野心与长期主义

## 待补充

- [x] 核对发布者正式期号、BVID、aid、cid 和 page
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取并验证本地独立音轨及来源 sidecar
- [x] 使用 Qwen3-ASR 与 ForcedAligner 生成机器逐字稿
- [x] 基于完整机器逐字稿生成总结草稿
- [ ] 核听总结引用的关键片段并完成必要事实核查
