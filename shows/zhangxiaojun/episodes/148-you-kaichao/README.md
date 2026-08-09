---
schema_version: 1
kind: episode
id: "zhangxiaojun:148"
show_id: zhangxiaojun
episode_key: "148"
episode_number: 148
slug: 148-you-kaichao
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-05
  source: publisher-rss
title: "对游凯超3小时访谈：开源Infra、和模型Co-design 、“如果vLLM失败，我们会后悔一辈子”"
navigation_title: "游凯超 · vLLM、开源治理与模型—Infra 协同"
catalog_keyword: "vLLM"
published_at: "2026-07-28T08:00:00+08:00"
duration_ms: 10826000
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: you-kaichao
    name: 游凯超
    role: guest
    profile:
      headline: "Inferact 联合创始人兼首席科学家"
      affiliations:
        - organization: "Inferact"
          title: "联合创始人兼首席科学家"
          status: current
      checked_at: "2026-08-06"
sources:
  - platform: rss
    kind: feed-item
    url: https://www.xiaoyuzhoufm.com/episode/6a66ed17a3fec224d5a3f744
    preferred: false
    identifiers:
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 6a66ed17a3fec224d5a3f744
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV18Qg96YE1W/
    preferred: true
    identifiers:
      bvid: BV18Qg96YE1W
      aid: "116988315699992"
      cid: "40309098797"
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
    sha256: 3c44db870658466a8f193b36a4d0f073e1dbba8cd1b83b34d344d2a3dc6d58ff
transcript:
  path: transcript.zh-CN.md
  platform_subtitle_access: not-exposed-as-public-track
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
  generated_at: "2026-08-06T04:21:00.821450Z"
  quality:
    source_chunks: 45
    aligned_chunks: 45
    alignment_items: 55701
    sentence_segments: 1608
    refined_segments: 1608
    rendered_blocks: 358
    rendered_lines: 1608
  performance:
    transcription_seconds: 385.432
    alignment_seconds: 79.089
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
    generated_at: "2026-08-06T04:21:00.821450Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/148-you-kaichao/source.m4a
  metadata_path: .cache/media/zhangxiaojun/148-you-kaichao/source.metadata.json
  git_ignored: true
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 164063328
  duration_ms: 10748821
  sha256: b3b2e1c16cb04f8433530ed5928e6287da85b4a73b0a57f20876b451e5504f29
  acquired_at: "2026-08-05T12:00:46.159856Z"
  verified_at: "2026-08-05T12:00:46.159856Z"
last_verified_at: 2026-08-06
---

# 对游凯超 3 小时访谈：开源 Infra、模型 Co-design 与 vLLM

> 本页保留发布者简介与章节形成的结构化概览；另有依据完整机器逐字稿整理的总结草稿，尚未完成关键片段核听和独立事实核查。

## 单集信息

- 节目：张小珺商业访谈录 #148
- 主持人：张小珺
- 嘉宾：游凯超，Inferact 联合创始人兼首席科学家
- 发布时间：2026-07-28 08:00（UTC+8）
- 官方 RSS 音频时长：03:00:26
- Bilibili 视频及本地音频时长：02:59:09；比 RSS 版本短约 1 分 17 秒
- RSS GUID：`6a66ed17a3fec224d5a3f744`
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/6a66ed17a3fec224d5a3f744)、[Bilibili 视频](https://www.bilibili.com/video/BV18Qg96YE1W/)
- 字幕状态：匿名访问未发现独立公开字幕轨；播放器元数据提示字幕能力需要登录，但未证明登录后存在字幕
- 本地音频：AAC、48 kHz、双声道、164,063,328 字节；sidecar 已记录 SHA-256 和来源身份
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[核心观点与 5 分钟版](./summary.zh-CN.md)

## 内容概览

发布者介绍称，游凯超是 Inferact 联合创始人兼首席科学家。Inferact 由伯克利校园开源项目 vLLM 演化而来，维护者在约三年里将一篇算法论文发展为开源社区，再进一步建立公司。

本期从游凯超由算法研究转向机器学习系统的经历谈起，回顾 vLLM 的诞生、社区维护者围绕开源项目所作的选择，以及社区走向商业组织后面临的治理与运营问题。技术部分讨论模型结构、AI Infra 与 Harness Engineering 的联合设计，并从 Token 和电力两个角度观察基础设施演进，最后延伸到技术预测。

发布者简介还提到 Inferact 在 2026 年初获得 1.5 亿美元种子轮融资；该信息目前仅按发布者表述记录，尚未在本单集处理中独立事实核查。

## 章节概览

> 以下时间码来自发布者 RSS 与 Bilibili 简介，两个来源给出的章节一致。

- 00:02:18 — 从算法到机器学习系统
- 00:37:56 — 开源项目 vLLM 的诞生
- 01:07:25 — “如果 vLLM 失败了，我们会后悔一辈子”
- 01:20:11 — “仁慈的独裁者”
- 01:37:16 — 从社区到创业
- 01:52:56 — 模型与 Infra 的 Co-design
- 02:15:10 — Token VS 电力
- 02:35:41 — 技术预测

## 核心议题

- 从算法研究转向机器学习系统与 AI Infra
- vLLM 从论文、校园项目到开源社区的演进
- 开源维护者的长期投入、治理选择与社区责任
- 社区项目商业化之后的组织与运营问题
- 模型、Infra 与 Harness Engineering 的联合设计
- Token 供给、电力约束与基础设施技术预测

## 待补充

- [x] 通过发布者 RSS GUID 核对官方期号
- [x] 核对 Bilibili 视频的 aid、cid 和 page
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取并验证本地独立音轨及来源 sidecar
- [x] 使用 Qwen3-ASR 与 ForcedAligner 生成机器逐字稿
- [ ] 校对专有名词、断句和识别错误
- [ ] 增加主持人与嘉宾的说话人区分
- [x] 基于完整机器逐字稿生成总结草稿
- [ ] 核听总结引用的关键片段并完成必要事实核查
