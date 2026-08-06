---
schema_version: 1
kind: episode
id: "sv101:bili-bv1pnku6de3v"
show_id: sv101
episode_key: bili-bv1pnku6de3v
episode_number: null
slug: bili-bv1pnku6de3v-vincent-koc
release_type: special
numbering:
  status: not-in-publisher-feed
  checked_at: 2026-08-07
  source: publisher-rss-checked
  url: https://feeds.fireside.fm/sv101/rss
  note: "硅谷101官方 RSS 未收录与该发布者视频对应的单集，无法核实或推导正式期号"
title: "对话Vincent Koc：OpenClaw的反思与进化，与Agent的下一步 | B站 x WAIC AI会客厅【101视频播客】"
navigation_title: "Vincent Koc - OpenClaw 反思、架构与 Agent 未来"
published_at: "2026-07-20T20:25:06+08:00"
duration_ms: 3938752
language: en
participants:
  - id: vincent-koc
    name: Vincent Koc
    role: guest
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1pNKU6dE3V/
    preferred: true
    identifiers:
      bvid: BV1pNKU6dE3V
      aid: "116951305297432"
      cid: "40134051148"
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
    path: transcript.en.md
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    selection_status: selected
    sha256: edfb6442d3fcbbfef5122a1c9b3ce4a105fa29c6ad0670da0596416f2f62cbdd
transcript:
  path: transcript.en.md
  translations:
    - language: zh-CN
      path: transcript.zh-CN.md
      source_language: en
      source_path: transcript.en.md
      alignment: segment
      status: edited
      generated_at: "2026-08-06T20:23:41Z"
      source_sha256: edfb6442d3fcbbfef5122a1c9b3ce4a105fa29c6ad0670da0596416f2f62cbdd
      sha256: 408599a73d11276153acc682826a0f2d2879cefb37e8da7c4f6def5222411c81
  platform_subtitle_access: no-anonymous-track-login-indicated
  platform_subtitle_languages: []
  automatic_caption_languages: []
  acquisition_method: audio-asr
  asr_script: scripts/transcribe_qwen3_asr.py
  engine: mlx-audio
  model: mlx-community/Qwen3-ASR-1.7B-8bit
  aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
  options:
    language: English
    temperature: 0.0
    max_tokens_per_chunk: 4096
    chunk_duration_seconds: 240.0
    max_sentence_characters: 160
  generated_at: "2026-08-06T20:12:31.919097Z"
  quality:
    source_chunks: 17
    aligned_chunks: 17
    alignment_items: 15023
    sentence_segments: 798
    refined_segments: 797
    rendered_blocks: 344
    rendered_lines: 797
  performance:
    model_load_seconds: 1.386
    transcription_seconds: 205.576
    prompt_tokens: 51511
    generation_tokens: 19284
    prompt_tokens_per_second: 250.572
    generation_tokens_per_second: 93.806
    aligner_load_seconds: 0.158
    alignment_seconds: 27.062
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
    path: asr/qwen3-asr/transcript.en.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
  renderer: scripts/render_asr_transcript.py
asr_runs:
  - id: qwen3-asr-1.7b-8bit
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    options:
      language: English
      temperature: 0.0
      max_tokens_per_chunk: 4096
      chunk_duration_seconds: 240.0
      max_sentence_characters: 160
    generated_at: "2026-08-06T20:12:31.919097Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.en.md
    quality:
      source_chunks: 17
      aligned_chunks: 17
      alignment_items: 15023
      sentence_segments: 798
      refined_segments: 797
      rendered_blocks: 344
      rendered_lines: 797
    performance:
      model_load_seconds: 1.386
      transcription_seconds: 205.576
      prompt_tokens: 51511
      generation_tokens: 19284
      prompt_tokens_per_second: 250.572
      generation_tokens_per_second: 93.806
      aligner_load_seconds: 0.158
      alignment_seconds: 27.062
local_audio_cache:
  path: .cache/media/sv101/bili-bv1pnku6de3v-vincent-koc/source.m4a
  metadata_path: .cache/media/sv101/bili-bv1pnku6de3v-vincent-koc/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-06T18:50:40.115417Z"
  verified_at: "2026-08-06T18:50:40.115417Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 53175736
  duration_ms: 3938752
  sha256: e6005050842e76ad1a996526634aae5355bba969150be387945783024e8bf287
last_verified_at: 2026-08-07
---

# Vincent Koc - OpenClaw 的反思、架构与 Agent 未来

## 单集信息

- 节目：硅谷101（官方 RSS 未收录对应单集，正式期号未核实）
- 嘉宾：Vincent Koc，OpenClaw 基金会首席架构师
- 发布时间：2026-07-20 20:25:06（UTC+8）
- 主要语言：英语
- 本地音频时长：01:05:38.752（AAC、48 kHz、双声道）
- 来源：[发布者视频](https://www.bilibili.com/video/BV1pNKU6dE3V/)
- 字幕状态：匿名访问未发现公开字幕轨；播放器提示登录后可能存在字幕
- 本地来源：独立音轨已下载，并通过媒体探测、时长、大小和 SHA-256 校验
- 英文逐字稿：[Qwen3-ASR 机器初稿](./transcript.en.md)
- 中文逐字稿：[逐段对齐的机器译稿](./transcript.zh-CN.md)（已做初步专名与语义编辑，尚未逐段人工审核）
- 中文总结：[基于完整英文机器稿的总结草稿](./summary.zh-CN.md)
- 处理状态：英文机器逐字稿、经初步编辑的逐段中文机器译稿与中文总结草稿均已生成

## 内容概览

本期在 WAIC 2026 现场对话 OpenClaw 基金会首席架构师 Vincent Koc。发布者从项目在 2026 年初突然走红谈起，追问热潮退去后下载量、真实使用和全球社区的变化，以及 OpenClaw 为什么在中国形成格外强烈的传播效应。

技术部分围绕 Gateway 网关架构展开，并延伸到 Agent 进入现实世界后的安全、成本、记忆、模型偏见和交互问题。节目也讨论开源项目如何演化为基金会与全球社区，以及“后 Claw 时代”可能出现的竞争格局。

## 发布者章节概览

- 00:00:00 — “爆火的那一天”
- 00:07:44 — 龙虾热
- 00:10:56 — 热度消退与留存
- 00:20:47 — 架构
- 00:24:45 — 安全、模型与记忆
- 00:34:35 — Agent 交互
- 00:41:37 — 反思与教训
- 00:48:05 — 竞争
- 00:51:01 — 基金会与未来

## 核心议题

- OpenClaw 爆火、热度变化与真实用户留存
- Agent 在中国快速传播的社区与产品背景
- Gateway 网关架构及其在系统中的角色
- Agent 的安全、成本、记忆和模型偏见
- 人与 Agent 的交互方式及下一阶段产品形态
- 开源治理、基金会与全球社区的长期演进

## 待补充

- [x] 核对规范来源、发布账号、BVID、aid、cid 和 page
- [x] 核对硅谷101官方 RSS，确认未收录对应单集
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取并验证本地独立音轨及来源 sidecar
- [x] 使用 Qwen3-ASR 与 ForcedAligner 生成英文机器逐字稿
- [x] 生成与英文稿 797 个 segment 逐段对齐的中文机器译稿，并完成初步专名与语义编辑
- [x] 基于完整英文逐字稿完善结构化中文总结
- [ ] 校对英文识别、专有名词、断句和说话人区分
- [ ] 逐段人工审核中文机器译稿
- [ ] 核听关键片段并完成必要事实核查
- [ ] 将逐字稿、译稿和总结推进到人工审核状态

## ASR 运行记录

- 当前选中英文稿：[Qwen3-ASR 版本](./transcript.en.md)
- 可追溯运行产物：[Qwen3-ASR run](./asr/qwen3-asr/transcript.en.md)
- 模型：`mlx-community/Qwen3-ASR-1.7B-8bit`
- 对齐器：`mlx-community/Qwen3-ForcedAligner-0.6B-8bit`
- 尾部处理：`raw.json` 原样保留；`aligned.json` 删除首个有效 `[01:05:26] That's it.` 之后的 935 个静音区重复片段，再由项目渲染器重建 refined、run transcript 与根英文稿
