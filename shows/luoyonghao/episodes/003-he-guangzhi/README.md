---
schema_version: 1
kind: episode
id: "luoyonghao:003"
show_id: luoyonghao
episode_key: "003"
episode_number: 3
slug: 003-he-guangzhi
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-09
  source: publisher-rss-description
  url: https://feed.xyzfm.space/wmnkvmrpwuww
title: "【正片】何广智×罗永浩！何广智：我到长安了"
navigation_title: "何广智 · 从穷门到脱口秀冠军"
catalog_keyword: "脱口秀"
published_at: "2025-09-01T12:11:58+08:00"
duration_ms: 12048960
language: zh-CN
participants:
  - id: luo-yonghao
    name: "罗永浩"
    aliases: []
    role: host
  - id: he-guangzhi
    name: "何广智"
    aliases: []
    role: guest
sources:
  - platform: bilibili
    kind: video
    title: "【正片】何广智×罗永浩！何广智：我到长安了"
    url: https://www.bilibili.com/video/BV1Jih9zjEEc/
    preferred: true
    identifiers:
      bvid: BV1Jih9zjEEc
      aid: "115110794233514"
      cid: "32084463171"
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
    sha256: ff4f31297e5588ea8f2370bffd2ccd085f0435ce1ffdec09f5944806176748b5
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
  generated_at: "2026-08-09T13:05:16.431117Z"
  quality:
    source_chunks: 51
    aligned_chunks: 51
    alignment_items: 60932
    sentence_segments: 2270
    refined_segments: 2270
    rendered_blocks: 395
    rendered_lines: 2270
  performance:
    model_load_seconds: 1.75
    transcription_seconds: 498.003
    prompt_tokens: 157564
    generation_tokens: 44194
    prompt_tokens_per_second: 316.391
    generation_tokens_per_second: 88.742
    aligner_load_seconds: 0.243
    alignment_seconds: 74.351
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
    generated_at: "2026-08-09T13:05:16.431117Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/luoyonghao/003-he-guangzhi/source.m4a
  metadata_path: .cache/media/luoyonghao/003-he-guangzhi/source.metadata.json
  git_ignored: true
  recovered_at: "2026-08-09T12:31:52.298237Z"
  verified_at: "2026-08-09T12:31:52.298237Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 189297533
  duration_ms: 12048960
  sha256: 58c858febbb0e3eeb1b0d8130974732c3545dc8128cd60e49b00927855692cc9
last_verified_at: 2026-08-09
---

# 【正片】何广智×罗永浩！何广智：我到长安了

> 发布者标题、官方播客 RSS 简介与章节概览继续保留；当前已补充完整机器逐字稿及基于全文形成的独立总结。逐字稿与总结均待人工核听、校对，状态分别为 `machine` 与 `draft`。

## 单集信息

- 节目：罗永浩的十字路口（第 3 期）
- 主持人：罗永浩
- 嘉宾：何广智
- 发布时间：2025-09-01 12:11:58（UTC+8）
- Bilibili 视频时长：03:20:49
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1Jih9zjEEc/)
- 来源状态：公开单 P；匿名访问未发现公开字幕轨；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 本地音频：AAC、48 kHz、双声道、189,297,533 字节
- 编号状态：发布者材料明确为第 3 期

## 内容文件

- [完整机器逐字稿](./transcript.zh-CN.md)
- [独立中文总结](./summary.zh-CN.md)

## 发布者材料概览

发布者围绕何广智从苏北走向上海、进入脱口秀行业并获得比赛冠军的成长经历，整理他的创作、生活与舞台选择。

## 发布者章节概览

- `[00:00:00]` 圆满了。回顾夺冠之路
- `[01:13:02]` 从小出身“穷门”
- `[01:48:35]` 上海，配得上我的梦想
- `[02:14:18]` 从“练习生”到“炸场王”
- `[02:36:19]` 有资格去李诞家喝酒了
- `[03:01:25]` 要不然买个路虎？

## 核心议题

- 何广智的成长与城市迁移
- 脱口秀创作和舞台经历
- 冠军之后的生活与判断

## 剩余人工审核

- 回听总结引用的关键片段并确认说话人归属
- 校对逐字稿中的人名、作品名、节目季数与明显同音识别
- 交叉核查积蓄金额、工作年限、演出数量和行业时间线等高影响口述
