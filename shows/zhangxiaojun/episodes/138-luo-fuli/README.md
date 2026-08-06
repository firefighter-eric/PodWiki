---
schema_version: 1
kind: episode
id: "zhangxiaojun:138"
show_id: zhangxiaojun
episode_key: "138"
episode_number: 138
slug: 138-luo-fuli
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-06
  source: publisher-rss
title: "对罗福莉3.5小时访谈：AI 范式已然巨变"
navigation_title: "罗福莉 - Agent 时代的模型、Infra 与组织"
published_at: "2026-04-24T11:44:26+08:00"
duration_ms: 12996000
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: luo-fuli
    name: 罗福莉
    role: guest
sources:
  - platform: rss
    kind: feed-item
    url: https://www.xiaoyuzhoufm.com/episode/69eae15a1e94ae692107cc50
    preferred: false
    identifiers:
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 69eae15a1e94ae692107cc50
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1iVoVBgERD/
    preferred: true
    identifiers:
      bvid: BV1iVoVBgERD
      aid: "116457333588484"
      cid: "37760077818"
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
    sha256: 7df5026e1b23e2850824be643be2195c9d321342a13212a5b1c85fbab5170762
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
  generated_at: "2026-08-06T08:05:09.170790Z"
  quality:
    source_chunks: 54
    aligned_chunks: 54
    alignment_items: 59646
    sentence_segments: 1186
    refined_segments: 1186
    rendered_blocks: 455
    rendered_lines: 1186
  performance:
    model_load_seconds: 2.119
    transcription_seconds: 489.777
    prompt_tokens: 168406
    generation_tokens: 41736
    prompt_tokens_per_second: 343.844
    generation_tokens_per_second: 85.215
    aligner_load_seconds: 0.219
    alignment_seconds: 96.337
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
    generated_at: "2026-08-06T08:05:09.170790Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/138-luo-fuli/source.m4a
  metadata_path: .cache/media/zhangxiaojun/138-luo-fuli/source.metadata.json
  git_ignored: true
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 207809298
  duration_ms: 12878869
  sha256: 8533826318ef456531275ee15308567ee6c2579c5e0f4344e4ab5fca5d9f3632
  acquired_at: "2026-08-06T06:57:51.236304Z"
  verified_at: "2026-08-06T06:57:51.236304Z"
last_verified_at: 2026-08-06
---

# 对罗福莉 3.5 小时访谈：AI 范式已然巨变

> 本页保留发布者简介形成的概览；另有依据完整机器逐字稿整理的总结草稿，尚未完成关键片段核听和独立事实核查。

## 单集信息

- 节目：张小珺商业访谈录（第 138 期）
- 主持人：张小珺
- 嘉宾：罗福莉，小米大模型团队负责人
- 发布时间：2026-04-24 11:44（UTC+8）
- 官方 RSS 时长：03:36:36；Bilibili 视频时长：03:34:39
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/69eae15a1e94ae692107cc50)、[Bilibili 视频](https://www.bilibili.com/video/BV1iVoVBgERD/)
- 字幕状态：匿名访问未发现公开字幕轨；播放器提示登录后可能存在字幕
- 本地音频：AAC、48 kHz、双声道、207,809,298 字节；sidecar 已记录 SHA-256 和来源身份
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[核心观点与 5 分钟版](./summary.zh-CN.md)

## 内容概览

罗福莉从一线模型训练视角讨论 2026 年由 Chat 向 Agent 转变的技术范式，重点涉及 Agent 后训练、RL Infra、算力分配、大规模预训练的下一步和研究组织如何重组。

## 核心议题

- 从 Pre-train 主导的 Chat 时代转向 Post-train 主导的 Agent 时代
- Agent RL、Rollout 与 RL Infra 的系统变化
- 预训练、后训练和研究探索之间的算力分配
- 技术范式变化下的研究组织与文化

## 待补充

- [x] 通过发布者 RSS GUID 核对官方期号
- [x] 核对 Bilibili 视频的 aid、cid 和 page
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取并验证本地独立音轨及来源 sidecar
- [x] 使用 Qwen3-ASR 与 ForcedAligner 生成机器逐字稿
- [ ] 校对专有名词、断句和识别错误
- [ ] 增加主持人与嘉宾的说话人区分
- [x] 基于完整机器逐字稿生成总结草稿
- [ ] 核听总结引用的关键片段并完成必要事实核查
