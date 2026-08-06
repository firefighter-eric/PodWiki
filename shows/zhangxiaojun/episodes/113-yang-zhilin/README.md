---
schema_version: 1
kind: episode
id: "zhangxiaojun:113"
show_id: zhangxiaojun
episode_key: "113"
episode_number: 113
slug: 113-yang-zhilin
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-06
  source: publisher-rss
title: "和杨植麟时隔1年的对话：K2、Agentic LLM、缸中之脑和“站在无限的开端”"
published_at: "2025-08-27T12:21:01+08:00"
duration_ms: 6073000
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: yang-zhilin
    name: 杨植麟
    role: guest
sources:
  - platform: rss
    kind: feed-item
    url: https://www.xiaoyuzhoufm.com/episode/68ae86d18ce45d46d49c4d50
    preferred: false
    identifiers:
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 68ae86d18ce45d46d49c4d50
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1hFe1zSEXp/
    preferred: true
    identifiers:
      bvid: BV1hFe1zSEXp
      aid: "115099134134471"
      cid: "31969772655"
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
    sha256: e9bdc7882eed21db1f8c189a3ce2e9245769ee52fa672b154b370a9d1c1ce82b
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
  generated_at: "2026-08-06T07:16:06.272003Z"
  quality:
    source_chunks: 25
    aligned_chunks: 25
    alignment_items: 32051
    sentence_segments: 775
    refined_segments: 775
    rendered_blocks: 212
    rendered_lines: 775
  performance:
    transcription_seconds: 242.308
    alignment_seconds: 59.229
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
    generated_at: "2026-08-06T07:16:06.272003Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/113-yang-zhilin/source.m4a
  metadata_path: .cache/media/zhangxiaojun/113-yang-zhilin/source.metadata.json
  git_ignored: true
  codec: aac
  sample_rate_hz: 48000
  channels: 1
  size_bytes: 86589935
  duration_ms: 5978837
  sha256: ba8d8326b8b731b7b1fa2dda64b318495bf92c365006b6318ddfc7a1a3659aa5
  acquired_at: "2026-08-06T06:59:03.289622Z"
  verified_at: "2026-08-06T06:59:03.289622Z"
last_verified_at: 2026-08-06
---

# 和杨植麟时隔 1 年的对话：K2、Agentic LLM 与“站在无限的开端”

> 本页保留发布者简介形成的概览；另有依据完整 Qwen3-ASR 机器逐字稿整理的总结草稿。机器稿与总结均尚未完成人工核听或独立事实核查。

## 单集信息

- 节目：张小珺商业访谈录（第 113 期）
- 主持人：张小珺
- 嘉宾：杨植麟，月之暗面创始人
- 发布时间：2025-08-27 12:21（UTC+8）
- 官方 RSS 时长：01:41:13；Bilibili 视频时长：01:39:39
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/68ae86d18ce45d46d49c4d50)、[Bilibili 视频](https://www.bilibili.com/video/BV1hFe1zSEXp/)
- 字幕状态：匿名访问未发现公开字幕轨；播放器提示登录后可能存在字幕
- 本地音频：AAC、48 kHz、单声道、86,589,935 字节；sidecar 已记录 SHA-256 和来源身份
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[核心观点与 5 分钟版](./summary.zh-CN.md)

## 内容概览

本期围绕 Kimi K2 的研发、Agentic LLM、长文本与泛化展开，也讨论杨植麟在创业起伏和舆论环境中的技术判断与个人思考。

## 核心议题

- K2 的研发路线与 Agentic LLM
- 长文本、泛化与模型能力边界
- 创业公司如何选择技术下注
- 杨植麟对行业变化和个人处境的反思

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
