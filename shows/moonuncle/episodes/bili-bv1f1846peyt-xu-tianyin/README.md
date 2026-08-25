---
schema_version: 1
kind: episode
id: "moonuncle:bili-bv1f1846peyt"
show_id: moonuncle
episode_key: bili-bv1f1846peyt
episode_number: null
slug: bili-bv1f1846peyt-xu-tianyin
release_type: regular
numbering:
  status: unknown
  checked_at: 2026-08-25
  source: publisher-season
  note: "官方播客合集与标题未提供正式期号；不根据合集位置推导"
title: "徐天音：系统，UIUC，教授，最佳论文，Agent Infra，云计算，形式化验证，容错，纯粹"
navigation_title: "徐天音 · Agent Infra 与容错系统"
catalog_keyword: "Agent Infra"
published_at: "2026-08-23T15:16:20+08:00"
duration_ms: 7051297
language: zh-CN
participants:
  - id: yueqiu-dashu
    name: 月球大叔
    aliases: []
    role: host
  - id: xu-tianyin
    name: 徐天音
    aliases: []
    role: guest
sources:
  - platform: bilibili
    kind: video
    title: "徐天音：系统，UIUC，教授，最佳论文，Agent Infra，云计算，形式化验证，容错，纯粹"
    url: https://www.bilibili.com/video/BV1F1846pEYT/
    preferred: true
    identifiers:
      bvid: BV1F1846pEYT
      aid: "117143488304300"
      cid: "41173189287"
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
    sha256: 040ab946dce0471fe10a70f3dd79b2643a53968ff9dc88a0aa3c81c7eab21819
transcript:
  path: transcript.zh-CN.md
  platform_subtitle_access: authenticated-ai-track
  platform_subtitle_languages:
    - zh-CN
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
    planned_chunk_count: 30
    final_leaf_chunk_count: 30
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 122880
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: "2026-08-25T05:30:23.488751Z"
  quality:
    source_chunks: 30
    aligned_chunks: 30
    alignment_items: 40618
    sentence_segments: 1190
    refined_segments: 1190
    rendered_blocks: 263
    rendered_lines: 1190
  performance:
    model_load_seconds: 0.232
    transcription_seconds: 308.998
    prompt_tokens: 92211
    generation_tokens: 28131
    attempt_prompt_tokens: 92211
    attempt_generation_tokens: 28131
    generation_call_count: 30
    prompt_tokens_per_second: 298.419
    generation_tokens_per_second: 91.039
    aligner_load_seconds: 0.242
    alignment_seconds: 46.601
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
      planned_chunk_count: 30
      final_leaf_chunk_count: 30
      adaptive_split_count: 0
      adaptive_split_algorithm: adaptive-low-energy-bisect-v1
      adaptive_min_leaf_samples: 320000
      adaptive_max_depth: 4
      adaptive_max_split_count: 64
      adaptive_energy_window_samples: 1600
      adaptive_quantization: pcm-s16-round-half-away-v1
      adaptive_tie_break: energy-center-left-v1
      effective_total_token_budget: 122880
      token_budget_scope: adaptive-bisect-per-leaf-v2
      max_sentence_characters: 160
    generated_at: "2026-08-25T05:30:23.488751Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
    quality:
      source_chunks: 30
      aligned_chunks: 30
      alignment_items: 40618
      sentence_segments: 1190
      refined_segments: 1190
      rendered_blocks: 263
      rendered_lines: 1190
    performance:
      model_load_seconds: 0.232
      transcription_seconds: 308.998
      prompt_tokens: 92211
      generation_tokens: 28131
      attempt_prompt_tokens: 92211
      attempt_generation_tokens: 28131
      generation_call_count: 30
      prompt_tokens_per_second: 298.419
      generation_tokens_per_second: 91.039
      aligner_load_seconds: 0.242
      alignment_seconds: 46.601
local_audio_cache:
  path: .cache/media/moonuncle/bili-bv1f1846peyt-xu-tianyin/source.m4a
  metadata_path: .cache/media/moonuncle/bili-bv1f1846peyt-xu-tianyin/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-25T05:21:08.534377Z"
  verified_at: "2026-08-25T05:21:08.534377Z"
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 106937391
  duration_ms: 7051297
  sha256: 8c29e5ffabf3fbfe9a724aef9903227e9f8520b0b5c1879add582ffc9f9c0461
last_verified_at: 2026-08-25
---

# 徐天音：系统，UIUC，教授，最佳论文，Agent Infra，云计算，形式化验证，容错，纯粹

> 本页依据官方播客合集、发布者简介、时间轴与完整本地 Qwen3-ASR 机器稿整理；已确认登录态播放器存在中文 AI 字幕，但 Chrome 控制接口无法安全导出响应正文。用户明确要求改用公开音轨和本地 ASR，逐字稿和总结尚未人工回听校对。

## 单集信息

- 节目：月球大叔的硅谷播客
- 主持人：月球大叔
- 嘉宾：徐天音（UIUC 教授，本期录制期间访问 UC Berkeley Sky Lab）
- 发布时间：2026-08-23 15:16:20（UTC+8）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1F1846pEYT/)
- 编号状态：发布者未提供正式期号，保留 `episode_number: null`
- 本地来源：公开音轨已获取，并通过媒体探测、大小与 SHA-256 校验
- 字幕状态：登录态 Chrome 播放器确认存在中文 AI 字幕；因响应正文无法由受支持的 Chrome 控制接口导出，按用户明确要求改用本地 Qwen3-ASR
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的中文总结](./summary.zh-CN.md)

## 内容概览

发布者以徐天音从博士申请、系统研究训练到 UIUC 任教的经历为主线，讨论 AI Agent 对系统接口、容错、运维和形式化验证提出的新要求，以及研究选题、学生培养和工业实践之间的关系。

## 章节概览

- `[00:01:00]` 两次申请美国 PhD 与进入 UCSD
- `[00:08:37]` 系统研究训练与 PCheck
- `[00:19:38]` AI Agent 为什么要求重新设计系统接口
- `[00:41:34]` AI 时代的论文、同行评审与研究生产力
- `[00:49:48]` 如何选择真正重要的研究问题
- `[00:58:38]` AI SRE、SREGym 与真实故障环境
- `[01:09:30]` Model Checking 与 AI 加速形式化建模
- `[01:23:05]` Agent-native 系统、容错、Undo 与 Microreboot
- `[01:33:00]` UIUC、Berkeley 与工业界研究的文化差异
- `[01:47:21]` 持续学习与给年轻研究者的建议

## 核心议题

- AI Agent 成为系统用户后，登录、安全、反馈和恢复接口如何改变
- 如何从配置错误、运维故障和真实用户行为中提炼系统研究问题
- 形式化方法怎样帮助约束和验证 AI 生成代码
- 导师、学生、工业实习和研究文化如何共同影响研究质量

## 待补充

- [x] 核对 BVID、aid、cid、单 P、发布者、官方播客合集与公开免费状态
- [x] 使用登录态 Chrome 确认中文 AI 字幕存在
- [x] 获取公开音轨并完成编码、时长、大小和 SHA-256 校验
- [x] 使用本机 MLX Qwen3-ASR 与 ForcedAligner 生成完整机器逐字稿
- [x] 对发布者确认的人名、机构名、系统名与关键术语应用可审计字面纠正
- [x] 基于完整机器逐字稿生成总结草稿
- [x] 同步根索引、节目索引与 Web 计数并完成发布门禁
- [ ] 人工回听并校对人名、论文名、系统名、英文术语、数字和说话人归属
- [ ] 独立核查学术经历、系统指标与行业判断等高影响陈述
