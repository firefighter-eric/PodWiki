---
schema_version: 1
kind: episode
id: "luoyonghao:005"
show_id: luoyonghao
episode_key: "005"
episode_number: 5
slug: 005-zhou-hongyi
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-07
  source: publisher-description
title: "【正片】周鸿祎×罗永浩！近四小时高密度输出！周鸿祎深度谈 AI"
navigation_title: "周鸿祎 · AI 革命、企业转型与未来"
catalog_keyword: "AI 转型"
published_at: "2025-09-24T12:00:00+08:00"
duration_ms: 12895082
language: zh-CN
participants:
  - id: luo-yonghao
    name: 罗永浩
    role: host
  - id: zhou-hongyi
    name: 周鸿祎
    role: guest
    profile:
      headline: "360 集团创始人"
      affiliations:
        - organization: "360 集团"
          title: "创始人"
          status: current
      checked_at: "2026-08-07"
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1hNJ1zLEb8/
    preferred: true
    identifiers:
      bvid: BV1hNJ1zLEb8
      aid: "115254088435022"
      cid: "32610844674"
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
    sha256: 576080341ed9fb42f1b17f005e3b9c20851e9eea9f0f348dae19ceb2093bf461
transcript:
  path: transcript.zh-CN.md
  platform_subtitle_access: no-anonymous-track-login-indicated
  translations: []
  acquisition_method: audio-asr
  asr_script: scripts/transcribe_qwen3_asr.py
  engine: mlx-audio
  model: mlx-community/Qwen3-ASR-1.7B-8bit
  aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
  options:
    language: Chinese
    temperature: 0.0
    max_tokens_per_chunk: 4096
    chunk_duration_seconds: 240.0
    max_sentence_characters: 160
  generated_at: "2026-08-06T19:12:34.008088Z"
  quality:
    source_chunks: 54
    aligned_chunks: 54
    alignment_items: 61695
    sentence_segments: 2086
    refined_segments: 2085
    rendered_blocks: 429
    rendered_lines: 2085
  performance:
    model_load_seconds: 1.939
    transcription_seconds: 466.144
    prompt_tokens: 168615
    generation_tokens: 43312
    prompt_tokens_per_second: 361.779
    generation_tokens_per_second: 92.93
    aligner_load_seconds: 0.216
    alignment_seconds: 94.457
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
      temperature: 0.0
      max_tokens_per_chunk: 4096
      chunk_duration_seconds: 240.0
      max_sentence_characters: 160
    generated_at: "2026-08-06T19:12:34.008088Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
    quality:
      source_chunks: 54
      aligned_chunks: 54
      alignment_items: 61695
      sentence_segments: 2086
      refined_segments: 2085
      rendered_blocks: 429
      rendered_lines: 2085
    performance:
      model_load_seconds: 1.939
      transcription_seconds: 466.144
      prompt_tokens: 168615
      generation_tokens: 43312
      prompt_tokens_per_second: 361.779
      generation_tokens_per_second: 92.93
      aligner_load_seconds: 0.216
      alignment_seconds: 94.457
local_audio_cache:
  path: .cache/media/luoyonghao/005-zhou-hongyi/source.m4a
  metadata_path: .cache/media/luoyonghao/005-zhou-hongyi/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-06T18:44:48.849254Z"
  verified_at: "2026-08-06T18:44:48.849254Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 196161841
  duration_ms: 12895082
  sha256: c48039754c1358ade2e4f0886a4b4c0b2bf465fede0d1663f0af0a528982f402
last_verified_at: 2026-08-07
---

# 周鸿祎 × 罗永浩：AI 革命、企业转型与未来

## 单集信息

- 节目：罗永浩的十字路口（第 5 期）
- 主持人：罗永浩
- 嘉宾：周鸿祎，360 集团创始人
- 发布时间：2025-09-24 12:00（UTC+8）
- 本地音频时长：03:34:55.082（AAC、48 kHz、双声道）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1hNJ1zLEb8/)
- 字幕状态：匿名访问未发现公开字幕轨；播放器提示登录后可能存在字幕
- 本地来源：独立音轨已下载，并通过媒体探测、时长、大小和 SHA-256 校验
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的结构化总结草稿](./summary.zh-CN.md)
- 处理状态：机器逐字稿与总结草稿均已生成

## 内容概览

周鸿祎回顾自己从互联网安全创业者到企业家内容创作者的角色变化，解释为什么持续公开表达，以及个人品牌如何影响 360 的组织与业务。他也复盘迈巴赫拍卖事件及其引发的争议，讨论企业家面对公众监督时的判断与边界。

访谈的主体聚焦 AI 革命。周鸿祎从大模型能力、智能体、脑机接口、国内 AI 团队和商业模式出发，说明自己为何长期看好 AI，并讨论传统软件、安全行业和企业组织在这一轮技术变革中的机会。

## 发布者章节概览

- 00:00:00 — 为什么当网红企业家
- 00:28:17 — 迈巴赫事件前因后果
- 00:51:07 — 加入 AI 革命大军
- 02:30:30 — 对 AI 的未来很乐观
- 03:28:02 — 聊点儿中年话题

## 核心议题

- 企业家公开表达、个人品牌与公司治理
- 迈巴赫事件中的舆论、商业和信任问题
- 大模型与智能体带来的新一轮技术革命
- 国内 AI 团队、产品机会与商业模式
- AI 对安全软件和传统企业转型的影响
- 中年企业家的工作方式、竞争心态与人生选择

## 待补充

- [x] 核对发布者正式期号、BVID、aid、cid 和 page
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取并验证本地独立音轨及来源 sidecar
- [x] 使用 Qwen3-ASR 与 ForcedAligner 生成机器逐字稿
- [x] 基于完整逐字稿完善结构化总结草稿
- [ ] 校对专有名词、数字、断句及主持人与嘉宾的说话人区分
- [ ] 核听关键片段并完成必要事实核查
