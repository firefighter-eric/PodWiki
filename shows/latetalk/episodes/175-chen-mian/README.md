---
schema_version: 1
kind: episode
id: "latetalk:175"
show_id: latetalk
episode_key: "175"
episode_number: 175
slug: 175-chen-mian
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-07
  source: publisher-website
  note: "晚点聊官网与官方 RSS 明确标为 175 期"
title: "对话 Liblib 陈冕：关于活下来，以及所有接近死亡的时刻【晚点聊LateTalk】"
navigation_title: "陈冕 · AI 应用公司的生存策略"
catalog_keyword: "Liblib"
published_at: "2026-07-30T20:53:06+08:00"
duration_ms: 7714000
language: zh-CN
participants:
  - id: latepost-reporters
    name: 《晚点 LatePost》记者
    role: host
  - id: chen-mian
    name: 陈冕
    role: guest
    profile:
      headline: "演语科技 Evoken 创始人"
      affiliations:
        - organization: "演语科技 Evoken"
          title: "创始人"
          status: current
      checked_at: "2026-08-07"
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1ZP3863E3E/
    preferred: true
    identifiers:
      bvid: BV1ZP3863E3E
      aid: "117009018787091"
      cid: "40444691975"
      page: 1
  - platform: website
    kind: episode
    url: https://podcast.latepost.com/175
    identifiers:
      episode_number: "175"
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
    sha256: a4d2deadaa8a09782f5e2e95ddafed7542bee3031e3ef0dd3824f6fcb09469e0
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
  generated_at: "2026-08-07T10:27:52.813905Z"
  quality:
    source_chunks: 33
    aligned_chunks: 33
    alignment_items: 39754
    sentence_segments: 1464
    refined_segments: 1461
    rendered_blocks: 252
    rendered_lines: 1461
  performance:
    model_load_seconds: 1.963
    transcription_seconds: 337.161
    prompt_tokens: 100868
    generation_tokens: 27414
    prompt_tokens_per_second: 299.172
    generation_tokens_per_second: 81.309
    aligner_load_seconds: 0.335
    alignment_seconds: 69.952
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
    generated_at: "2026-08-07T10:27:52.813905Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/latetalk/175-chen-mian/source.m4a
  metadata_path: .cache/media/latetalk/175-chen-mian/source.metadata.json
  git_ignored: true
  extractor: BiliBili
  acquired_at: "2026-08-07T09:39:12.218044Z"
  verified_at: "2026-08-07T09:39:12.218044Z"
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 92954548
  duration_ms: 7713088
  sha256: 45bf612f0d27ba66baa83cf228585ab75a047ad9e1be2356743a984d38ada0ab
last_verified_at: 2026-08-07
---

# 对话 Liblib 陈冕：关于活下来，以及所有接近死亡的时刻【晚点聊LateTalk】

> 本页保留发布者简介形成的内容提纲，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 节目：晚点聊 LateTalk #175
- 主播：《晚点 LatePost》记者（发布者未公开具体姓名）
- 嘉宾：陈冕，演语科技 Evoken 创始人
- Bilibili 发布时间：2026-07-30 20:53:06（UTC+8）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1ZP3863E3E/) · [官方节目页](https://podcast.latepost.com/175)
- 字幕状态：未发现匿名公开字幕轨；平台提示字幕查询需要登录，未使用 cookies 或登录态
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

发布者简介称，本期围绕陈冕与 Evoken 在模型能力不断变化的环境中如何经营 Liblib、Lovart 与 LibTV 展开，讨论产品速度、商业模式、组织焦虑、外界争议，以及独立 AI 应用公司如何持续生存。简介中的收入、融资与估值数据均为发布者材料，尚未独立核查。

## 章节概览

官方节目页提供了从争议回应、创业经历、产品市场匹配到组织与生存策略的时间线；最终总结将以完整正式逐字稿中的实际时间码为准。

## 核心议题

- AI 应用公司面对模型能力上移时的生存空间
- 速度、定价与产品创新之间的取舍
- 创始人的焦虑如何影响组织与决策
- 外界争议、融资叙事和经营事实之间的边界

## 待补充

- [x] 核对 BVID、aid、cid、page、正式期号与嘉宾
- [x] 检查匿名访问可见的平台字幕轨并记录边界
- [x] 获取公开音轨并完成编码、时长、大小和哈希校验
- [x] 生成 Qwen3-ASR 机器逐字稿及完整 lineage
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 核听关键片段、校对专有名词并核查高影响事实
