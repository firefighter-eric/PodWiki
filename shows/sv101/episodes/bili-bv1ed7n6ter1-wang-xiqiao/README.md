---
schema_version: 1
kind: episode
id: "sv101:bili-bv1ed7n6ter1"
show_id: sv101
episode_key: bili-bv1ed7n6ter1
episode_number: null
slug: bili-bv1ed7n6ter1-wang-xiqiao
release_type: regular
numbering:
  status: not-in-publisher-feed
  checked_at: 2026-08-06
  source: publisher-rss
  note: "截至 2026-08-06，发布者官方 RSS 未收录这条 Bilibili 新视频，无法取得正式期号或 RSS GUID，保留 episode_number: null"
title: "对话王熙乔：AI时代的教育者、十年沉浮，与人类文明的下一步【101视频播客】"
navigation_title: "王熙乔 · AI 时代的教育与文明"
catalog_keyword: "AI 教育"
published_at: "2026-06-27T13:06:06+08:00"
duration_ms: 8705237
language: zh-CN
participants:
  - id: wang-xiqiao
    name: 王熙乔
    role: guest
    profile:
      headline: "探月学校创始人、校长"
      affiliations:
        - organization: "探月学校"
          title: "创始人、校长"
          status: current
      checked_at: "2026-08-07"
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1Ed7n6TEr1/
    preferred: true
    identifiers:
      bvid: BV1Ed7n6TEr1
      aid: "116820308662439"
      cid: "39454770108"
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
    sha256: 0c2b26ad38ffc5803ab5edf5aec9375c456b830efc9d2a8e6ede769e77127f0b
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
  generated_at: "2026-08-06T16:10:56.041604Z"
  quality:
    source_chunks: 37
    aligned_chunks: 37
    alignment_items: 43415
    sentence_segments: 1058
    refined_segments: 1058
    rendered_blocks: 299
    rendered_lines: 1058
  performance:
    model_load_seconds: 1.663
    transcription_seconds: 306.858
    prompt_tokens: 113839
    generation_tokens: 29155
    prompt_tokens_per_second: 370.987
    generation_tokens_per_second: 95.013
    aligner_load_seconds: 0.215
    alignment_seconds: 60.225
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
    generated_at: "2026-08-06T16:10:56.041604Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/sv101/bili-bv1ed7n6ter1-wang-xiqiao/source.m4a
  metadata_path: .cache/media/sv101/bili-bv1ed7n6ter1-wang-xiqiao/source.metadata.json
  git_ignored: true
  extractor: BiliBiliPublicAPI
  acquired_at: "2026-08-06T15:45:36.385928Z"
  verified_at: "2026-08-06T15:45:36.385928Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 133862366
  duration_ms: 8705237
  sha256: dcd360ab2eceadc979951939b7c54b671eaa50ca9efcf70c60c865ca9d7f1a96
last_verified_at: 2026-08-07
---

# 对话王熙乔：AI时代的教育者、十年沉浮，与人类文明的下一步【101视频播客】

> 本页保留 Bilibili 发布者简介与平台章节，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；音频和总结均未完成人工审核，机器稿中的姓名、术语、数字、引文与说话人归属仍可能有误。

## 单集信息

- 节目：硅谷101
- 嘉宾：王熙乔，探月学校创始人、校长（身份来自发布者简介）
- 发布时间：2026-06-27 13:06:06（UTC+8）
- Bilibili 平台整秒时长：02:25:06
- 本地 Bilibili 音轨：02:25:05.237（AAC、48 kHz、双声道）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1Ed7n6TEr1/)
- 编号状态：截至 2026-08-06，发布者官方 RSS 未收录这条新视频，无法取得正式期号或 RSS GUID，保留 `episode_number: null`
- 字幕状态：匿名 view/player 元数据未列出公开字幕轨；sidecar 同时标记字幕查询需要登录。这里只能确认“未发现匿名公开字幕轨”，不能据此排除登录可见字幕或画面硬字幕
- 获取方式：yt-dlp 无法解析该页 initial state 后，项目脚本在核对同一 BVID/CID 与公开访问状态后使用 Bilibili 官方匿名 playurl API 获取音轨；未使用 cookies 或登录态
- 本地来源：音轨已通过媒体探测、时长、大小和 SHA-256 校验
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，尚未核听或完成人工审核

## 内容概览

发布者简介称，王熙乔在十八岁时判断 AI 将改变大量职业，并认为新的职业会更需要创造力与好奇心。基于这一判断，他放弃美国大学的录取机会，创办了探月学校，希望回应技术发展给教育带来的挑战。

简介把此后十年的办学历程概括为一段反复承压的过程：扩张失误、“双减”政策和疫情等因素一度使学校辗转多个临时场地，这段经历被媒体称为“流浪月球”。发布者同时称，探月后来接手原清华附中国际部，并由高中扩展至初中和小学，形成 K12 覆盖。

本期对话围绕这十年的经历展开，讨论教育价值观、学校与人的成长、AI 时代的教育变化，以及在人类文明延续的尺度下如何理解下一代的生命力。本节保留发布者对节目内容的概述；基于完整机器稿的独立梳理、原文定位和事实边界见[总结草稿](./summary.zh-CN.md)。

## 章节概览

> 以下章节标题和边界来自 Bilibili 平台章节；平台按整秒记录，末章终点比本地音轨精确时长向上取整。

- 00:00:00–00:03:38 — 探月
- 00:03:38–00:11:23 — 价值观
- 00:11:23–00:22:15 — “大问题”
- 00:22:15–00:41:28 — 北大附与美国夫妇
- 00:41:28–00:55:13 — 18岁的高中校长
- 00:55:13–01:14:23 — “流浪月球”
- 01:14:23–01:33:55 — 素养图谱与学校的意义
- 01:33:55–02:02:05 — 人类终极追求与价值
- 02:02:05–02:25:06 — “让生命力冒出来“

## 核心议题

- AI 对职业结构与教育目标的潜在影响
- 创办探月学校时的价值判断与教育理念
- 创新教育机构在扩张、政策和疫情中的现实压力
- “流浪月球”阶段的组织经历与反思
- 学校从高中向 K12 覆盖的发展路径
- 学校、人的成长与“生命力”之间的关系
- 从人类文明延续的尺度思考下一代教育

## 待补充

- [x] 核对 Bilibili 视频的 BVID、aid、cid 和 page
- [x] 检查匿名访问可见的平台字幕轨并记录边界
- [x] 获取独立音轨并完成编码、时长、大小和哈希校验
- [x] 生成 Qwen3-ASR 机器逐字稿并保留原始、对齐、精炼与渲染产物
- [x] 基于完整机器逐字稿形成独立总结草稿并核验时间码存在性
- [ ] 核听总结引用的关键片段并完成人工内容审核
- [ ] 校对专有名词、断句及主持人与嘉宾的说话人区分
- [ ] 独立核查发布者简介涉及的学校沿革与其他外部事实
