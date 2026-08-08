---
schema_version: 1
kind: episode
id: "svvector:002"
show_id: svvector
episode_key: "002"
episode_number: 2
slug: 002-alan-du
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-08
  source: publisher-bilibili-part
  note: "Bilibili 发布者 part 字段明确写为 ‘EP02-对话微软战投合伙人：AI 时代软件的护城河’"
title: "硅谷坐标 x 微软战投合伙人：AI 时代软件的护城河"
navigation_title: "Alan Du · AI 软件护城河与 Agent 支付"
catalog_keyword: "M12"
published_at: "2026-03-16T17:26:27+08:00"
duration_ms: 3406250
language: zh-CN
participants:
  - id: cao-qingyun
    name: 曹卿云
    role: host
  - id: alan-du
    name: Alan Du
    role: guest
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1fpwEzTExd/
    preferred: true
    identifiers:
      bvid: BV1fpwEzTExd
      aid: "116238105776327"
      cid: "36738633230"
      page: 1
  - platform: xiaoyuzhou
    kind: episode
    url: https://www.xiaoyuzhoufm.com/episode/69b7befacaaea1fb3b8bbe45
    preferred: false
    identifiers:
      episode_id: 69b7befacaaea1fb3b8bbe45
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
    sha256: 94f1dc3903e946a24758fa7af110d5340fdf5cf90b02fee1aa9e8c55f4c7e255
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
  generated_at: "2026-08-08T14:38:04.255570Z"
  quality:
    source_chunks: 15
    aligned_chunks: 15
    alignment_items: 15737
    sentence_segments: 377
    refined_segments: 377
    rendered_blocks: 118
    rendered_lines: 377
  performance:
    model_load_seconds: 2.05
    transcription_seconds: 110.557
    prompt_tokens: 44553
    generation_tokens: 10418
    prompt_tokens_per_second: 403.004
    generation_tokens_per_second: 94.236
    aligner_load_seconds: 0.221
    alignment_seconds: 22.997
  translations: []
asr_artifacts:
  raw:
    path: asr/qwen3-asr/raw.json
    git_ignored: false
    format: podwiki-raw-asr-json-v1
    sha256: 25e6d37ed719d4fa4fb5894bc8557fa2475a7ecd2a10c17615e79c4aff6197a5
  aligned:
    path: asr/qwen3-asr/aligned.json
    git_ignored: false
    format: podwiki-aligned-asr-json-v1
    sha256: f3b3e65119757f54b16d17ec5459d887221dae656713101313c511d4f77f1df8
  refined:
    path: asr/qwen3-asr/refined.json
    git_ignored: false
    format: podwiki-refined-asr-json-v1
    sha256: 4908f1957db467b28f7fccfabb60b9834adb1226ab03ec812788d2d492253436
  transcript:
    path: asr/qwen3-asr/transcript.zh-CN.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
    sha256: 94f1dc3903e946a24758fa7af110d5340fdf5cf90b02fee1aa9e8c55f4c7e255
  renderer: scripts/render_asr_transcript.py
asr_runs:
  - id: qwen3-asr-1.7b-8bit
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    generated_at: "2026-08-08T14:38:04.255570Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/svvector/002-alan-du/source.m4a
  metadata_path: .cache/media/svvector/002-alan-du/source.metadata.json
  git_ignored: true
  extractor: BiliBili
  acquired_at: "2026-08-08T14:17:15.826724Z"
  verified_at: "2026-08-08T14:17:15.826724Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 62141330
  duration_ms: 3406250
  sha256: 69ebcd9beeb03ee819411de2830e2457569c47d94260dac893535e16808378b6
last_verified_at: 2026-08-08
---

# 硅谷坐标 x 微软战投合伙人：AI 时代软件的护城河

> 本页保留 Bilibili 发布者简介形成的来源概览，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿。逐字稿与总结均未完成人工核听；嘉宾口述的行业数字、公司案例与合规判断也未独立核查。

## 单集信息

- 节目：硅谷坐标 SV-Vector 第 2 期
- 主持人：曹卿云，《硅谷坐标》主持人
- 嘉宾：Alan Du，M12 投资合伙人（前 PayPal Ventures Partner）
- 采访日期：发布者简介记为 2026-03-12
- 发布时间：2026-03-16 17:26:27（UTC+8）
- Bilibili 标示时长：00:56:47
- 本地 Bilibili 音轨：00:56:46.250（AAC、48 kHz、双声道）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1fpwEzTExd/)；[小宇宙单集](https://www.xiaoyuzhoufm.com/episode/69b7befacaaea1fb3b8bbe45)
- 编号状态：Bilibili 发布者 `part` 字段明确写为“EP02-对话微软战投合伙人：AI 时代软件的护城河”，因此核实正式期号为 2
- 字幕状态：匿名访问未发现独立公开字幕轨；平台字幕字段提示登录后可能存在字幕。本流程未使用 cookies，不能据此判断登录可见字幕或画面硬字幕是否存在
- 来源权利提示：Bilibili 公开元数据记录 `rights.no_reprint=1`；本页只记录来源与研究材料，不转载原媒体。`download=1` 只是平台元数据字段，不视为项目取得转载或其他额外授权
- 本地来源：音轨及 sidecar 已获取，并通过 ffprobe、文件大小与 SHA-256 校验
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 处理状态：元数据已核实，机器逐字稿为 `machine`，独立总结为 `draft`，均等待人工复核

## 内容概览

发布者简介称，曹卿云在硅谷采访微软战略投资基金 M12 合伙人 Alan Du，讨论 AI 时代的软件护城河。简介提出的问题包括：哪些软件更容易被颠覆、护城河将迁移到哪里，以及如何理解算力投入与 AI 收入之间的落差。

发布者材料还把 M12 的投资策略、AI 泡沫、Agent 支付中的身份与合规、底层代码能力、强监管行业落地和创业建议列为访谈重点。现已另行提供基于完整机器稿的总结；其中所有数字、公司案例和行业判断仍按嘉宾口述记录，不代表 PodWiki 已独立确认。

## 章节概览

> 以下时间点和标题来自 Bilibili 发布者简介；平台结构化 `chapters` 字段为空。

- 00:00:00 — 开场与话题概览
- 00:01:10 — M12 投资策略
- 00:07:24 — AI 软件护城河
- 00:18:25 — AI 泡沫之争
- 00:28:42 — AI 收入和资本开支的落差
- 00:35:02 — Agent 支付：身份、合规与微支付
- 00:41:00 — AI 能写底层代码吗？
- 00:46:45 — 强监管行业 AI 落地
- 00:50:12 — 创业建议

## 核心议题

- M12 的投资策略与大公司、创业公司的分工
- AI 原生产品对传统软件护城河的影响
- 算力投入、商业收入与 AI 泡沫判断
- Agent 支付中的身份、合规、安全和微支付
- AI 编程能力的边界与底层代码
- 强监管行业的 AI 落地路径
- 面向创业者的产品化与市场建议

## 待补充

- [x] 核对发布者 `EP02` 标记、Bilibili 规范 URL 和平台标识符
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取并独立验证本地音轨、sidecar、大小和 SHA-256
- [x] 记录发布者 `rights.no_reprint=1` 的来源权利边界
- [x] 生成并校验 Qwen3-ASR 机器逐字稿及完整 lineage
- [x] 基于完整机器逐字稿撰写独立总结草稿
- [ ] 校对 M12、支付、合规与软件行业专有名词
- [ ] 核听关键片段并核查高影响外部事实
