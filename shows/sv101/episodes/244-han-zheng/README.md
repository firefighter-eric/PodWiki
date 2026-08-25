---
schema_version: 1
kind: episode
id: "sv101:244"
show_id: sv101
episode_key: "244"
episode_number: 244
slug: 244-han-zheng
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-25
  source: publisher-episode-page
  url: https://www.sv101.net/257
title: "机器人走错路了？与苏度韩铮聊聊具身智能的3D数据、路径分野与硅谷竞赛【硅谷101播客】"
navigation_title: "韩铮 · 具身智能的 3D 数据与路径分野"
catalog_keyword: "Sim-to-Real"
published_at: "2026-07-16T08:00:00+08:00"
duration_ms: 4661611
language: zh-CN
participants:
  - id: hongjun
    name: 泓君
    aliases: []
    role: host
  - id: han-zheng
    name: 韩铮
    aliases: []
    role: guest
    profile:
      headline: "苏度科技联合创始人兼 CEO"
      affiliations:
        - organization: 苏度科技
          title: 联合创始人兼 CEO
          status: current
      checked_at: 2026-08-25
sources:
  - platform: website
    kind: episode
    url: https://www.sv101.net/257
    preferred: false
    identifiers:
      page_id: "257"
      episode_number: "244"
  - platform: bilibili
    kind: video
    title: "机器人走错路了？与苏度韩铮聊聊具身智能的3D数据、路径分野与硅谷竞赛【硅谷101播客】"
    url: https://www.bilibili.com/video/BV1PRNq6fEh4/
    preferred: true
    identifiers:
      bvid: BV1PRNq6fEh4
      aid: "116924914670389"
      cid: "39985284305"
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
    sha256: a229d7af460b8a8f59dae8fda9828ad2b9fe2d85ba5a8e527b997bd7dd798263
transcript:
  path: transcript.zh-CN.md
  platform_subtitle_access: no-authenticated-track
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
    planned_chunk_count: 20
    effective_total_token_budget: 81920
    max_sentence_characters: 160
  generated_at: "2026-08-25T04:32:25.024216Z"
  quality:
    source_chunks: 20
    aligned_chunks: 20
    alignment_items: 23297
    sentence_segments: 540
    refined_segments: 540
    rendered_blocks: 159
    rendered_lines: 540
  performance:
    model_load_seconds: 0.2
    transcription_seconds: 183.492
    prompt_tokens: 60963
    generation_tokens: 15323
    prompt_tokens_per_second: 332.238
    generation_tokens_per_second: 83.508
    aligner_load_seconds: 0.225
    alignment_seconds: 28.472
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
    options:
      language: Chinese
      temperature: 0
      max_tokens_per_chunk: 4096
      chunk_duration_seconds: 240
      planned_chunk_count: 20
      effective_total_token_budget: 81920
      max_sentence_characters: 160
    generated_at: "2026-08-25T04:32:25.024216Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
    quality:
      source_chunks: 20
      aligned_chunks: 20
      alignment_items: 23297
      sentence_segments: 540
      refined_segments: 540
      rendered_blocks: 159
      rendered_lines: 540
    performance:
      model_load_seconds: 0.2
      transcription_seconds: 183.492
      prompt_tokens: 60963
      generation_tokens: 15323
      prompt_tokens_per_second: 332.238
      generation_tokens_per_second: 83.508
      aligner_load_seconds: 0.225
      alignment_seconds: 28.472
local_audio_cache:
  path: .cache/media/sv101/244-han-zheng/source.m4a
  metadata_path: .cache/media/sv101/244-han-zheng/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-25T04:18:41.052245Z"
  verified_at: "2026-08-25T04:18:41.052245Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 68477335
  duration_ms: 4661611
  sha256: bafb40b7092247e0499fdd0010c3da901793bc43b08671c279e69f782902dfb3
last_verified_at: 2026-08-25
---

# 机器人走错路了？与苏度韩铮聊聊具身智能的3D数据、路径分野与硅谷竞赛【硅谷101播客】

> 本页依据官方节目页、Bilibili 元数据与完整本地 Qwen3-ASR 机器稿整理；逐字稿和总结尚未人工回听校对。登录态 Chrome 播放器未显示可用字幕轨，因此获取公开音轨并运行本地 ASR。

## 单集信息

- 节目：硅谷101 E244
- 主播：泓君
- 嘉宾：韩铮（苏度科技联合创始人兼 CEO）
- 发布时间：2026-07-16 08:00（北京时间）
- 来源：[Bilibili 正片](https://www.bilibili.com/video/BV1PRNq6fEh4/) · [官方节目页](https://www.sv101.net/257)
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的中文总结](./summary.zh-CN.md)

## 内容概览

节目从机器人操作需要怎样的 3D 数据切入，对比真实世界模仿数据与 Sim-to-Real 路线，并讨论端到端 VLA、上下分层架构、软硬件协同和具身智能商业化之间的取舍。

## 章节概览

- `[00:08:01]` 从 ImageNet、ShapeNet 到机器人 3D 数据
- `[00:17:13]` Sim-to-Real 的含义与路线分野
- `[00:24:41]` 在仿真器中重建物理交互和训练环境
- `[00:31:12]` 开放世界物体的零样本抓取演示
- `[00:39:03]` 通用能力与垂直商业化场景
- `[00:42:31]` 软硬件协同如何缩小仿真到现实的差距
- `[00:48:16]` 可解释分层模型与端到端 VLA
- `[00:57:34]` 上下分层是否会重新成为主流
- `[01:06:30]` Google DeepMind 与波士顿动力的竞争判断

## 核心议题

- 机器人操作为什么需要结构化 3D 与动力学数据
- 仿真规模、物理一致性与视觉真实度如何取舍
- 零样本操作能力如何评估，演示与泛化如何区分
- 端到端路线和上下分层路线各自依赖什么数据条件
- 通用机器人研发与短期商业化怎样平衡

## 待补充

- [x] 核对官方节目页、E244、BVID、aid、cid、单 P、发布者与公开免费状态
- [x] 使用登录态 Chrome 核查播放器无可用字幕轨
- [x] 获取公开音轨并完成编码、时长、大小和 SHA-256 校验
- [x] 使用本机 MLX Qwen3-ASR 与 ForcedAligner 生成完整机器逐字稿
- [x] 对发布者确认的人名和公司名应用可审计字面纠正
- [x] 基于完整机器逐字稿生成总结草稿并同步索引
- [ ] 人工回听并校对公司名、模型名、英文术语、数字和说话人归属
- [ ] 独立核查成功率、数据规模、公司合作与行业预测等高影响陈述
