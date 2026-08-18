---
schema_version: 1
kind: episode
id: "latetalk:179"
show_id: latetalk
episode_key: "179"
episode_number: 179
slug: 179-cheng-manqi
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-18
  source: publisher-website
  note: "晚点聊官网与官方 RSS 明确标为 179 期"
title: "蒸馏风暴：一场大家不愿公开谈论的技术竞赛【晚点聊LateTalk】"
navigation_title: "程曼祺 · 蒸馏误解、门槛与代价"
catalog_keyword: "蒸馏"
published_at: "2026-08-18T07:00:00+08:00"
duration_ms: 2973995
language: zh-CN
participants:
  - id: gao-honghao
    name: 高洪浩
    role: host
  - id: cheng-manqi
    name: 程曼祺
    role: guest
    aliases:
      - 曼祺
    profile:
      headline: "《晚点 LatePost》科技报道负责人"
      affiliations:
        - organization: "晚点 LatePost"
          title: "科技报道负责人"
          status: current
      checked_at: "2026-08-18"
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV14fbv6DELm/
    preferred: true
    identifiers:
      bvid: BV14fbv6DELm
      aid: "117111527576047"
      cid: "41003388181"
      page: 1
  - platform: website
    kind: episode
    url: https://podcast.latepost.com/179
    identifiers:
      episode_number: "179"
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
    sha256: 9779aaa0ab71732cff794ff01dcdadfeb7df3530e62914563734a5aaf44e91bc
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
    planned_chunk_count: 13
    effective_total_token_budget: 53248
    max_sentence_characters: 160
  generated_at: "2026-08-18T04:07:28.150726Z"
  quality:
    source_chunks: 13
    aligned_chunks: 13
    alignment_items: 16001
    sentence_segments: 495
    refined_segments: 495
    rendered_blocks: 99
    rendered_lines: 495
  performance:
    model_load_seconds: 0.465
    transcription_seconds: 120.766
    prompt_tokens: 38899
    generation_tokens: 10936
    prompt_tokens_per_second: 322.102
    generation_tokens_per_second: 90.555
    aligner_load_seconds: 0.245
    alignment_seconds: 18.168
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
    generated_at: "2026-08-18T04:07:28.150726Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/latetalk/179-cheng-manqi/source.m4a
  metadata_path: .cache/media/latetalk/179-cheng-manqi/source.metadata.json
  git_ignored: true
  extractor: BiliBili
  acquired_at: "2026-08-18T04:03:21.758548Z"
  verified_at: "2026-08-18T04:03:21.758548Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 38031027
  duration_ms: 2973995
  sha256: d623e11c87e994199ec259c4a4b6e48fc89f00262ae1c30e71bd83aa6f2cc689
last_verified_at: 2026-08-18
---

# 蒸馏风暴：一场大家不愿公开谈论的技术竞赛【晚点聊LateTalk】

> 本页保留发布者简介形成的内容提纲，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 节目：晚点聊 LateTalk #179
- 主播：高洪浩，《晚点 LatePost》主笔
- 嘉宾：程曼祺，《晚点 LatePost》科技报道负责人
- Bilibili 发布时间：2026-08-18 07:00:00（UTC+8）；官方 RSS 发布时间为 2026-08-17 06:45:00（UTC+8）
- Bilibili 标题使用“大家不愿公开谈论”，官方节目页标题使用“无人公开谈论”
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV14fbv6DELm/) · [官方节目页](https://podcast.latepost.com/179)
- 字幕状态：未发现匿名公开字幕轨；平台提示字幕查询需要登录，未使用 cookies 或登录态
- 本地 Bilibili 音轨：00:49:33.995（AAC、48 kHz、双声道）
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

发布者将本期定位为“编辑部”节目。高洪浩与程曼祺结合近期同多位中国 AI lab 从业者的交流和公开资料，讨论蒸馏为什么在 2026 年受到关注、大规模蒸馏的数据与工程门槛、学生模型能否超越教师模型，以及规则争议和商业代价。

## 章节概览

- 02:04–10:17：蒸馏的定义、数据形态与用途变化
- 13:51–24:41：字节为什么不蒸馏，以及其他公司的选择
- 28:52–37:29：大规模蒸馏的账号、数据管线与技术门槛
- 38:35–44:05：蒸馏红线、双标争议与前沿模型商业逻辑

## 核心议题

- 蒸馏与一般使用强模型输出训练之间的边界
- 从模型压缩到能力增强的用途变化
- 大规模蒸馏所需的数据、账号和工程管线
- 学生模型逼近或超越教师模型的技术与商业限制

## 待补充

- [x] 核对 BVID、aid、cid、page、正式期号与参与者角色
- [x] 检查匿名访问可见的平台字幕轨并记录边界
- [x] 获取公开音轨并完成编码、时长、大小和哈希校验
- [x] 生成 Qwen3-ASR 机器逐字稿及完整产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 核听关键片段、校对专有名词并核查高影响事实
