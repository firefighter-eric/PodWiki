---
schema_version: 1
kind: episode
id: "latetalk:169"
show_id: latetalk
episode_key: "169"
episode_number: 169
slug: 169-zhou-nan
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-16
  source: publisher-website
  note: "晚点聊官方节目页与 RSS 标题明确标为 169 期"
title: "英伟达挑战者？Cerebras 投资故事【晚点聊LateTalk】"
navigation_title: "周楠 · Cerebras 与 AI 算力投资"
catalog_keyword: "Cerebras"
published_at: "2026-06-22T22:58:38+08:00"
duration_ms: 5955456
language: zh-CN
participants:
  - id: zhou-nan
    name: 周楠
    aliases: []
    role: guest
    profile:
      headline: "高通创投投资人，Cerebras 早期投资人"
      bio: "发布者简介称，周楠是 Cerebras 的早期投资人之一，目前任职于高通创投，早年曾加入百度硅谷 AI 实验室。"
      affiliations:
        - organization: "高通创投"
          title: "投资人"
          status: current
        - organization: "百度硅谷 AI 实验室"
          status: former
      checked_at: 2026-08-16
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV18g7M6JEkw/
    preferred: true
    identifiers:
      bvid: BV18g7M6JEkw
      aid: "116794320752739"
      cid: "39320880241"
      page: 1
  - platform: website
    kind: episode
    url: https://podcast.latepost.com/169
    identifiers:
      episode_number: "169"
      rss_guid: 2ad6ee49-2e3e-41fe-87a1-f810c4ee8352
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
    sha256: 45cc5856e35041873ed4f241149a445314c2041ffb82f7baca3c323dd400bfe0
transcript:
  path: transcript.zh-CN.md
  platform_subtitle_access: no-anonymous-track
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
    planned_chunk_count: 25
    effective_total_token_budget: 102400
    max_sentence_characters: 160
  generated_at: "2026-08-16T04:41:38.511142Z"
  quality:
    source_chunks: 25
    aligned_chunks: 25
    alignment_items: 30617
    sentence_segments: 744
    refined_segments: 744
    rendered_blocks: 202
    rendered_lines: 744
  performance:
    model_load_seconds: 0.185
    transcription_seconds: 218.919
    prompt_tokens: 77875
    generation_tokens: 20435
    prompt_tokens_per_second: 355.724
    generation_tokens_per_second: 93.345
    aligner_load_seconds: 0.138
    alignment_seconds: 34.413
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
    generated_at: "2026-08-16T04:41:38.511142Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/latetalk/169-zhou-nan/source.m4a
  metadata_path: .cache/media/latetalk/169-zhou-nan/source.metadata.json
  git_ignored: true
  extractor: BiliBili
  acquired_at: "2026-08-16T04:12:42.050996Z"
  verified_at: "2026-08-16T04:12:42.050996Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 73347755
  duration_ms: 5955456
  sha256: f3b98fd7333faac09079963f4c1fb7f5caee1ce86949f8618bb5cdbf4543b4a6
last_verified_at: 2026-08-16
---

# 英伟达挑战者？Cerebras 投资故事【晚点聊LateTalk】

> 本页保留发布者简介形成的内容提纲，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 节目：晚点聊 LateTalk #169
- 嘉宾：周楠，高通创投投资人、Cerebras 早期投资人（身份来自发布者简介）
- 发布时间：2026-06-22 22:58:38（UTC+8）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV18g7M6JEkw/) · [官方节目页](https://podcast.latepost.com/169)
- 字幕状态：匿名元数据未列出公开字幕轨
- 本地音轨：01:39:15.456（AAC、48 kHz、双声道）
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

发布者简介从 Cerebras 上市切入，讨论 AI 算力的新趋势、Scaling Law 在硅谷的早期发展，以及百度硅谷 AI 实验室的相关往事。简介把周楠描述为 Cerebras 的早期投资人之一。

## 章节概览

Bilibili 匿名元数据未提供平台章节。

## 核心议题

- Cerebras 的芯片路线与产业位置
- AI 算力投资的判断框架
- Scaling Law 的早期发展
- 百度硅谷 AI 实验室的行业记忆

## 待补充

- [x] 核对 BVID、aid、cid、page、正式期号与嘉宾
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取公开音轨并完成媒体校验
- [x] 生成 Qwen3-ASR 机器逐字稿及可复现产物链
- [x] 基于完整逐字稿形成独立总结草稿
- [ ] 回听并校对专有名词与高影响事实
