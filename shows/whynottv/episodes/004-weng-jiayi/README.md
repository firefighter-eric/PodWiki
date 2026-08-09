---
schema_version: 1
kind: episode
id: "whynottv:004"
show_id: whynottv
episode_key: "004"
episode_number: 4
slug: 004-weng-jiayi
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-05
  source: publisher-title
title: "翁家翌：OpenAI，GPT，强化学习，Infra，后训练，天授，tuixue，开源，CMU，清华｜WhynotTV Podcast"
navigation_title: "翁家翌 · OpenAI、强化学习、Infra 与后训练"
catalog_keyword: "后训练"
published_at: "2026-01-17T15:09:39+08:00"
duration_ms: 7365000
language: zh-CN
participants:
  - id: weng-jiayi
    name: 翁家翌
    role: guest
    profile:
      headline: "Tianshou 开源实践、CMU 求学与 OpenAI 工作经历"
      bio: "发布者材料围绕其强化学习、后训练基础设施和开源实践经历展开。"
      education:
        - institution: "卡内基梅隆大学（CMU）"
      checked_at: "2026-08-06"
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1darmBcE4A/
    preferred: true
    identifiers:
      bvid: BV1darmBcE4A
      aid: "115909138055436"
      cid: "35438791242"
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
    path: asr/whisper/transcript.zh-CN.md
    engine: mlx-whisper
    model: mlx-community/whisper-large-v3-turbo-q4
    selection_status: superseded
    sha256: e9c928f628ac9fbbf9efdbccfb7cfab1a90cd2a0d40e907b8ddf1451056ab3da
transcript:
  path: transcript.zh-CN.md
  platform_subtitle_access: not-exposed-as-track
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
  generated_at: "2026-08-06T03:56:30.162831Z"
  quality:
    source_chunks: 31
    aligned_chunks: 31
    alignment_items: 31245
    sentence_segments: 995
    refined_segments: 995
    rendered_blocks: 247
    rendered_lines: 995
  performance:
    transcription_seconds: 318.534
    alignment_seconds: 56.938
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
      max_sentence_characters: 160
    generated_at: "2026-08-06T03:56:30.162831Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
    quality:
      source_chunks: 31
      aligned_chunks: 31
      alignment_items: 31245
      sentence_segments: 995
      refined_segments: 995
      rendered_blocks: 247
      rendered_lines: 995
    performance:
      transcription_seconds: 318.534
      alignment_seconds: 56.938
    benchmark: docs/asr-benchmark.md
  - id: whisper-large-v3-turbo-q4
    selection_status: superseded
    engine: mlx-whisper
    model: mlx-community/whisper-large-v3-turbo-q4
    artifacts:
      raw: asr/whisper/raw.json
      refined: asr/whisper/refined.json
      transcript: asr/whisper/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/whynottv/004-weng-jiayi/source.m4a
  git_ignored: true
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 99676986
  duration_ms: 7364975
  sha256: 9eb8aab184a964f3ff8205a505c26a1acb957d9995bb8d61f0fbc6c1b252b11f
last_verified_at: 2026-08-06
---

# 翁家翌：OpenAI、强化学习、Infra 与后训练

> 本页概览根据发布者公开简介和章节整理；基于完整机器逐字稿生成的总结初稿单独保存在 [`summary.zh-CN.md`](./summary.zh-CN.md)。

## 单集信息

- 节目：WhynotTV Podcast #4
- 嘉宾：翁家翌
- 时长：02:02:45
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1darmBcE4A/)
- 总结：[查看结构化总结初稿](./summary.zh-CN.md)
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)

## 内容概览

本期围绕翁家翌的成长和技术经历展开：从计算机竞赛、清华学习与开源实践，延伸到强化学习框架 Tianshou、CMU 求学和加入 OpenAI 的过程；后半部分讨论研究与工程能力、RLHF 与后训练基础设施、大模型未来瓶颈，以及个人选择和长期目标。

## 章节概览

- 00:02:33 — 成长经历、竞赛、升学与清华阶段
- 00:41:08 — Tianshou、tuixue 和开源影响力
- 00:56:21 — CMU、加入 OpenAI，以及研究与工程能力
- 01:13:13 — 强化学习、后训练、ChatGPT 与工业级 RL 基础设施
- 01:32:08 — 大模型瓶颈、AGI、组织挑战与人才竞争
- 01:52:48 — 未来观、个人选择、创业与长期目标

## 核心议题

- 开源工具如何扩大个人工作的影响力
- AI 研究中工程基础设施为什么重要
- 从学术评价体系走向真实问题与实际影响
- RLHF 和后训练从研究方法变为工业系统时面临的挑战
- 大模型继续发展的技术与组织瓶颈

## 待补充

- [ ] 确认主持人显示名称
- [x] 检查平台字幕轨；当前视频未暴露独立字幕轨
- [x] 下载独立音轨并完成本地机器转写
- [x] 完成 Qwen3-ASR 与 Whisper 的首轮对比，选用 Qwen 并保留 Whisper 基线
- [ ] 校对专有名词、断句和识别错误
- [ ] 增加主持人与嘉宾的说话人区分
- [x] 基于完整机器逐字稿生成结构化总结初稿
- [ ] 核听总结引用的关键片段并校对专有名词
- [ ] 完成事实核查并将总结标记为 `reviewed`

## ASR 运行记录

- 当前正式逐字稿：[Qwen3-ASR 版本](./transcript.zh-CN.md)
- 已归档基线：[Whisper 版本](./asr/whisper/transcript.zh-CN.md)
- 对比记录：[ASR 基准](../../../../docs/asr-benchmark.md)
