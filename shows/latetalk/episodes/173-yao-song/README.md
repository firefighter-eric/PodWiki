---
schema_version: 1
kind: episode
id: "latetalk:173"
show_id: latetalk
episode_key: "173"
episode_number: 173
slug: 173-yao-song
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-07
  source: publisher-website
  note: "晚点聊官网与官方 RSS 明确标为 173 期"
title: "26 岁 3 亿美元卖公司“开心只有两分钟”，不想 boring 就继续 suffering【晚点聊 LateTalk】"
navigation_title: "姚颂 · 十年硬科技创业与物理 AI"
catalog_keyword: "Striding"
published_at: "2026-07-22T12:00:00+08:00"
duration_ms: 10507000
language: zh-CN
participants:
  - id: cheng-manqi
    name: 程曼祺
    role: host
    aliases:
      - 曼祺
  - id: yao-song
    name: 姚颂
    role: guest
    profile:
      headline: "正行创新创始人兼 CEO"
      affiliations:
        - organization: "正行创新"
          title: "创始人兼 CEO"
          status: current
      checked_at: "2026-08-07"
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1tYgz6JEvm/
    preferred: true
    identifiers:
      bvid: BV1tYgz6JEvm
      aid: "116961203720637"
      cid: "40178617047"
      page: 1
  - platform: website
    kind: episode
    url: https://podcast.latepost.com/173
    identifiers:
      episode_number: "173"
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
    sha256: 9710fe09016fb3736b07ff5b47820b3e6bfd87db4c7e4eb09e0cbc36db94e74f
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
  generated_at: "2026-08-07T10:16:19.794812Z"
  quality:
    source_chunks: 44
    aligned_chunks: 44
    alignment_items: 54035
    sentence_segments: 1486
    refined_segments: 1486
    rendered_blocks: 353
    rendered_lines: 1486
  performance:
    model_load_seconds: 1.942
    transcription_seconds: 459.885
    prompt_tokens: 137378
    generation_tokens: 35952
    prompt_tokens_per_second: 298.724
    generation_tokens_per_second: 78.176
    aligner_load_seconds: 0.232
    alignment_seconds: 91.508
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
    generated_at: "2026-08-07T10:16:19.794812Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/latetalk/173-yao-song/source.m4a
  metadata_path: .cache/media/latetalk/173-yao-song/source.metadata.json
  git_ignored: true
  extractor: BiliBili
  acquired_at: "2026-08-07T09:39:48.989348Z"
  verified_at: "2026-08-07T09:39:48.989348Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 166020988
  duration_ms: 10506283
  sha256: b7804b521eb00524bfe84d03aa4d2c0a863881c758a59d1b2e725230929c83c8
last_verified_at: 2026-08-07
---

# 26 岁 3 亿美元卖公司“开心只有两分钟”，不想 boring 就继续 suffering【晚点聊 LateTalk】

> 本页保留发布者简介形成的内容提纲，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 节目：晚点聊 LateTalk #173
- 主持人：程曼祺
- 嘉宾：姚颂，正行创新创始人兼 CEO
- Bilibili 发布时间：2026-07-22 12:00:00（UTC+8）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1tYgz6JEvm/) · [官方节目页](https://podcast.latepost.com/173)
- 字幕状态：未发现匿名公开字幕轨；平台提示字幕查询需要登录，未使用 cookies 或登录态
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

发布者简介称，本期从姚颂在清华的经历谈起，回顾深鉴科技、东方空间与正行创新三次硬科技创业，讨论出售第一家公司后的心理变化、商业航天经历，以及其对物理 AI、端侧部署和商业落地的判断。

## 章节概览

官方节目页按清华经历、出售深鉴、东方空间、第三次创业和 Striding 五组议题提供时间线；最终总结将以完整正式逐字稿中的实际时间码为准。

## 核心议题

- 十年三次硬科技创业的连续性与变化
- 技术创业中的融资、并购和个人选择
- 商业航天经历带来的经验与遗憾
- 物理 AI 的技术路线、部署方式和商业节奏

## 待补充

- [x] 核对 BVID、aid、cid、page、正式期号与参与者
- [x] 检查匿名访问可见的平台字幕轨并记录边界
- [x] 获取公开音轨并完成编码、时长、大小和哈希校验
- [x] 生成 Qwen3-ASR 机器逐字稿及完整 lineage
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 核听关键片段、校对专有名词并核查高影响事实
