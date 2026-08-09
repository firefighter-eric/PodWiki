---
schema_version: 1
kind: episode
id: "latetalk:bili-bv1z9ka6se9q"
show_id: latetalk
episode_key: bili-bv1z9ka6se9q
episode_number: null
slug: bili-bv1z9ka6se9q-wang-guangrun-pu-tao-zhong-liruo
release_type: special
numbering:
  status: not-in-publisher-feed
  checked_at: 2026-08-07
  source: publisher-rss
  note: "晚点聊官方 RSS 未收录该 LatePost 合作视频，使用规范 BVID 稳定键"
title: "世界模型这半年：路线争议、数据来源与商业落地【晚点LatePost】"
navigation_title: "王广润、蒲韬、仲黎若 · 世界动作模型的路线与落地"
catalog_keyword: "X-Era Lab"
published_at: "2026-07-18T19:53:36+08:00"
duration_ms: 1845000
language: zh-CN
participants:
  - id: shen-yuan
    name: 申远
    role: host
  - id: wang-guangrun
    name: 王广润
    role: guest
    profile:
      headline: "X-Era Lab 首席科学家"
      affiliations:
        - organization: "X-Era Lab"
          title: "首席科学家"
          status: current
      checked_at: "2026-08-07"
  - id: pu-tao
    name: 蒲韬
    role: guest
    profile:
      headline: "研发总监"
      checked_at: "2026-08-07"
  - id: zhong-liruo
    name: 仲黎若
    role: guest
    profile:
      headline: "总裁"
      checked_at: "2026-08-07"
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1Z9KA6sE9Q/
    preferred: true
    identifiers:
      bvid: BV1Z9KA6sE9Q
      aid: "116940802692193"
      cid: "40070285026"
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
    sha256: 8bf704b6226ab9a2846e8dc63e458ae248b6adff0e369cdc25b08691f287e11d
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
  generated_at: "2026-08-07T10:37:17.806690Z"
  quality:
    source_chunks: 8
    aligned_chunks: 8
    alignment_items: 10133
    sentence_segments: 211
    refined_segments: 211
    rendered_blocks: 62
    rendered_lines: 211
  performance:
    model_load_seconds: 1.349
    transcription_seconds: 77.387
    prompt_tokens: 24128
    generation_tokens: 6397
    prompt_tokens_per_second: 311.794
    generation_tokens_per_second: 82.665
    aligner_load_seconds: 0.203
    alignment_seconds: 17.595
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
    generated_at: "2026-08-07T10:37:17.806690Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/latetalk/bili-bv1z9ka6se9q-wang-guangrun-pu-tao-zhong-liruo/source.m4a
  metadata_path: .cache/media/latetalk/bili-bv1z9ka6se9q-wang-guangrun-pu-tao-zhong-liruo/source.metadata.json
  git_ignored: true
  extractor: BiliBili
  acquired_at: "2026-08-07T09:42:27.584705Z"
  verified_at: "2026-08-07T09:42:27.584705Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 24653169
  duration_ms: 1844885
  sha256: 508407cc7649bdcd62b50ec53b4da990472556192cabd69cd38935c2fc332cf6
last_verified_at: 2026-08-07
---

# 世界模型这半年：路线争议、数据来源与商业落地【晚点LatePost】

> 本页保留 Bilibili 发布者简介与封面人物标注形成的内容提纲，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 收录范围：晚点聊 LateTalk Bilibili 频道合作视频（未进入 LateTalk 官方 RSS，无正式期号）
- 主持人：申远，晚点记者
- 嘉宾：王广润（X-Era Lab 首席科学家）、蒲韬（研发总监）、仲黎若（总裁）
- Bilibili 发布时间：2026-07-18 19:53:36（UTC+8）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1Z9KA6sE9Q/)
- 字幕状态：未发现匿名公开字幕轨；平台提示字幕查询需要登录，未使用 cookies 或登录态
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

发布者简介称，本期邀请聚焦世界动作模型的 X-Era Lab，讨论世界模型与 VLA 的差别、具身智能的涌现潜力、训练数据来源、路线争议，以及这类模型距离真实商业落地的距离。

## 章节概览

Bilibili 匿名元数据未提供平台章节；最终总结将以完整正式逐字稿中的实际时间码为准。

## 核心议题

- 世界动作模型与 VLA 的关系和路线分歧
- 世界模型训练所需的数据来源
- 具身智能能力是否会出现涌现
- 技术展示、评测与商业落地之间的距离

## 待补充

- [x] 核对 BVID、aid、cid、page、无正式期号状态与参与者
- [x] 检查匿名访问可见的平台字幕轨并记录边界
- [x] 获取公开音轨并完成编码、时长、大小和哈希校验
- [x] 生成 Qwen3-ASR 机器逐字稿及完整 lineage
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 核听关键片段、校对专有名词并核查高影响事实
