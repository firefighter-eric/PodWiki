---
schema_version: 1
kind: episode
id: "luoyonghao:bili-bv1aed4bkeci"
show_id: luoyonghao
episode_key: "bili-bv1aed4bkeci"
episode_number: null
slug: bili-bv1aed4bkeci-wu-liao-zhai
release_type: special
numbering:
  status: unknown
  checked_at: 2026-08-09
  source: publisher-rss-and-season
  url: https://feed.xyzfm.space/wmnkvmrpwuww
  note: "发布者定义为《无聊斋》与《罗永浩的十字路口》联名款特别现场，但未提供正式期号"
title: "【正片】“无聊斋” × 罗永浩的十字路口！喜剧工作者在AI时代可以多“活”几年"
navigation_title: "阎鹤祥、石老板、刘旸教主、六兽 · 喜剧与恐惧"
catalog_keyword: "喜剧"
published_at: "2026-04-10T12:00:00+08:00"
duration_ms: 9037290
language: zh-CN
participants:
  - id: luo-yonghao
    name: "罗永浩"
    aliases: []
    role: host
  - id: yan-hexiang
    name: "阎鹤祥"
    aliases: []
    role: participant
  - id: shi-laoban
    name: "石老板"
    aliases: []
    role: participant
  - id: liu-yang-jiaozhu
    name: "刘旸教主"
    aliases: []
    role: participant
  - id: liu-shou
    name: "六兽"
    aliases: []
    role: participant
sources:
  - platform: bilibili
    kind: video
    title: "【正片】“无聊斋” × 罗永浩的十字路口！喜剧工作者在AI时代可以多“活”几年"
    url: https://www.bilibili.com/video/BV1AeD4BkECi/
    preferred: true
    identifiers:
      bvid: BV1AeD4BkECi
      aid: "116374454208336"
      cid: "37365744093"
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
    sha256: 67b2a6c026186b4f91350b25a64cdee4e2fb9bc2a01d77db0eda010d077de1fa
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
    final_leaf_chunk_count: 41
    adaptive_split_count: 3
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 167936
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: "2026-08-09T19:44:23.651992Z"
  quality:
    source_chunks: 41
    aligned_chunks: 41
    alignment_items: 43920
    sentence_segments: 2252
    refined_segments: 2234
    rendered_blocks: 307
    rendered_lines: 2234
  performance:
    model_load_seconds: 0.178
    transcription_seconds: 622.24
    prompt_tokens: 118230
    generation_tokens: 33976
    attempt_prompt_tokens: 124855
    attempt_generation_tokens: 46264
    generation_call_count: 44
    prompt_tokens_per_second: 190.007
    generation_tokens_per_second: 54.603
    aligner_load_seconds: 0.162
    alignment_seconds: 64.025
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
    generated_at: "2026-08-09T19:44:23.651992Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/luoyonghao/bili-bv1aed4bkeci-wu-liao-zhai/source.m4a
  metadata_path: .cache/media/luoyonghao/bili-bv1aed4bkeci-wu-liao-zhai/source.metadata.json
  git_ignored: true
  recovered_at: "2026-08-09T12:32:21.057484Z"
  verified_at: "2026-08-09T12:32:21.057484Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 134035259
  duration_ms: 9037290
  sha256: aca5955d9211b7b2cf7433651549b74f68d2b8f7f96c1923158ab79359452a5a
last_verified_at: 2026-08-09
---

# 【正片】“无聊斋” × 罗永浩的十字路口！喜剧工作者在AI时代可以多“活”几年

> 本页保留发布者材料形成的内容提纲，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 节目：罗永浩的十字路口
- 主持人：罗永浩
- 参与者：阎鹤祥、石老板、刘旸教主、六兽
- 发布时间：2026-04-10 12:00:00（UTC+8）
- Bilibili 视频时长：02:30:37
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1AeD4BkECi/)
- 来源状态：公开单 P；匿名访问未发现公开字幕轨；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 本地音频：AAC、48 kHz、双声道、134,035,259 字节
- 发布类型：发布者定义为《无聊斋》与《罗永浩的十字路口》的联名特别现场，保留 `release_type: special`
- 编号状态：发布者未提供正式期号，保留 `episode_number: null`，不按合集位置或发布时间推断
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

发布者把本集定义为《无聊斋》与《十字路口》的联名特别现场，几位喜剧工作者从生活中的恐惧和尴尬经验谈到 AI 时代的喜剧工作。

## 章节概览

发布者元数据未提供章节；以下导航由 PodWiki 依据完整逐字稿整理，不是发布者章节：

- `[00:02:46]` 以“恐惧”为主题的现场游戏
- `[00:53:49]` 听众投稿：现实生活中的恐惧
- `[01:23:38]` 独自出行、拒绝与安全感
- `[01:43:19]` 脸盲与线下社交压力
- `[02:02:34]` 从现实恐惧转入 AI 恐惧
- `[02:04:44]` AI 幻觉、版权与法律风险
- `[02:10:34]` 喜剧创作、活人感与职业替代
- `[02:24:18]` 在实践中学习使用 AI
- `[02:29:35]` 珍惜真实情绪与现场关系

## 核心议题

- 恐惧、尴尬与喜剧素材
- 社交责任、休息羞耻与现实安全感
- AI 幻觉、版权、职业替代与情感陪伴
- AI 时代的喜剧创作与“活人感”

## 待补充

- [x] 核对 BVID、aid、cid、page、联名特别现场边界与参与者
- [x] 检查匿名访问可见的平台字幕轨并记录边界
- [x] 获取公开音轨并完成编码、时长、大小和哈希校验
- [x] 生成完整 Qwen3-ASR 机器逐字稿及 adaptive v2 产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 核听关键片段、校对专有名词和数字，并核查高影响事实
