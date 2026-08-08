---
schema_version: 1
kind: episode
id: "svvector:bili-bv1smxjbieex"
show_id: svvector
episode_key: bili-bv1smxjbieex
episode_number: null
slug: bili-bv1smxjbieex-jimmy-cheng
release_type: regular
numbering:
  status: unknown
  checked_at: 2026-08-08
  source: publisher-bilibili-and-feed
  note: "Bilibili 标题与 part 字段、发布者小宇宙单集标题均未给出正式期号；不根据发布日期或列表顺序推导"
title: "硅谷坐标 x Jimmy Cheng，GTC回顾-AI时代英伟达的护城河"
navigation_title: "程暨杨 · GTC、英伟达护城河与芯片设计"
catalog_keyword: "GTC"
published_at: "2026-03-26T04:30:16+08:00"
duration_ms: 1654421
language: zh-CN
participants:
  - id: cao-qingyun
    name: 曹卿云
    role: host
  - id: jimmy-cheng
    name: 程暨杨
    role: guest
    aliases:
      - Jimmy Cheng
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1SmXJBiEEx/
    preferred: true
    identifiers:
      bvid: BV1SmXJBiEEx
      aid: "116291692141502"
      cid: "36981900588"
      page: 1
  - platform: xiaoyuzhou
    kind: episode
    url: https://www.xiaoyuzhoufm.com/episode/69c44ae0852cf1b8bbe44abe
    preferred: false
    identifiers:
      episode_id: 69c44ae0852cf1b8bbe44abe
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
    sha256: af6d59222f94d3463e715a1607de2b87a0e235c5be53f09c79f0a2df09aac5a5
transcript:
  path: transcript.zh-CN.md
  platform_subtitle_access: no-anonymous-track-login-indicated
  platform_subtitle_languages: []
  automatic_caption_languages: []
  translations: []
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
  generated_at: "2026-08-08T14:55:54.962558Z"
  quality:
    source_chunks: 7
    aligned_chunks: 7
    alignment_items: 6680
    sentence_segments: 241
    refined_segments: 241
    rendered_blocks: 55
    rendered_lines: 241
  performance:
    model_load_seconds: 1.329
    transcription_seconds: 53.208
    prompt_tokens: 21635
    generation_tokens: 5024
    prompt_tokens_per_second: 406.638
    generation_tokens_per_second: 94.428
    aligner_load_seconds: 0.159
    alignment_seconds: 9.854
asr_artifacts:
  raw:
    path: asr/qwen3-asr/raw.json
    git_ignored: false
    format: podwiki-raw-asr-json-v1
    sha256: e6d448627c3f7796ea6a6b23fd0ded85ed227534c8fdff4a56bfe962da89de8a
  aligned:
    path: asr/qwen3-asr/aligned.json
    git_ignored: false
    format: podwiki-aligned-asr-json-v1
    sha256: 3b0b6351dc6771d0fcfa2664cc3ad849a9bc79bc03adcd0a8b915d6593c999e9
  refined:
    path: asr/qwen3-asr/refined.json
    git_ignored: false
    format: podwiki-refined-asr-json-v1
    sha256: a5eef8274bce1e18c773542e577eb8da7dfcf7a4c70786cfa8dc9badc3c8aaf1
  transcript:
    path: asr/qwen3-asr/transcript.zh-CN.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
    sha256: af6d59222f94d3463e715a1607de2b87a0e235c5be53f09c79f0a2df09aac5a5
  renderer: scripts/render_asr_transcript.py
asr_runs:
  - id: qwen3-asr-1.7b-8bit
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    generated_at: "2026-08-08T14:55:54.962558Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/svvector/bili-bv1smxjbieex-jimmy-cheng/source.m4a
  metadata_path: .cache/media/svvector/bili-bv1smxjbieex-jimmy-cheng/source.metadata.json
  git_ignored: true
  extractor: BiliBili
  acquired_at: "2026-08-08T14:17:02.727929Z"
  verified_at: "2026-08-08T14:17:02.727929Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 24510768
  duration_ms: 1654421
  sha256: 6a5ae612c7bc9ffb11bb7d6d46d354f88675ddb4afa0d7ad8283486fd907e156
last_verified_at: 2026-08-08
---

# 硅谷坐标 x Jimmy Cheng，GTC回顾-AI时代英伟达的护城河

> 本页保留 Bilibili 发布者简介及时间点形成的来源概览；另有依据完整机器逐字稿整理的总结草稿。嘉宾观点、专有名词、产品参数和外部事实均未完成人工核听或独立核查。

## 单集信息

- 节目：硅谷坐标 SV-Vector（正式期号未核实）
- 主持人：曹卿云，《硅谷坐标》主持人
- 嘉宾：程暨杨（Jimmy Cheng）；发布者介绍为华美半导体协会副会长、Synopsys 新思科技企业战略部技术战略中心负责人、前幕僚长
- 采访日期：发布者简介记为 2026-03-23
- 发布时间：2026-03-26 04:30:16（UTC+8）
- Bilibili 标示时长：00:27:35
- 本地 Bilibili 音轨：00:27:34.421（AAC、48 kHz、双声道）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1SmXJBiEEx/)；[小宇宙单集](https://www.xiaoyuzhoufm.com/episode/69c44ae0852cf1b8bbe44abe)
- 编号状态：截至 2026-08-08，Bilibili 标题与 `part` 字段、小宇宙单集标题均未给出正式期号；保留 `episode_number: null`，不按发布时间或列表顺序推导
- 字幕状态：匿名访问未发现独立公开字幕轨；平台字幕字段提示登录后可能存在字幕。本流程未使用 cookies，不能据此判断登录可见字幕或画面硬字幕是否存在
- 来源权利提示：Bilibili 公开元数据记录 `rights.no_reprint=1`；本页只记录来源与研究材料，不转载原媒体。`download=1` 只是平台元数据字段，不视为项目取得转载或其他额外授权
- 本地来源：音轨及 sidecar 已获取，并通过 ffprobe、文件大小与 SHA-256 校验
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[核心观点与 5 分钟版](./summary.zh-CN.md)
- 处理状态：机器逐字稿已完成并选为正式稿，总结为 `draft`；说话人、专名、数字和关键技术判断仍待人工复核

## 内容概览

发布者简介称，曹卿云在 GTC 后采访程暨杨，围绕 Agent 时代英伟达的战略格局与护城河展开讨论。简介把 GTC、OpenClaw、产业链利润与议价权、开源模型、推理芯片和芯片设计自动化列为主要议题。

简介还把讨论延伸到 Synopsys 在 Agent 时代的定位、AI 对芯片硬件工程师的影响，以及 Physical AI 从仿真走向现实世界时面临的挑战。以上仅是对发布者材料的整理，尚不代表对完整访谈内容或相关判断的独立确认。

## 章节概览

> 以下时间点和标题来自 Bilibili 发布者简介；平台结构化 `chapters` 字段为空。

- 00:01:44 — GTC 大会：OpenClaw 引领 Agent 新纪元
- 00:03:55 — Agent 时代的英伟达护城河
- 00:07:28 — 产业链利润与议价权再分配
- 00:10:51 — 英伟达推动开源模型的考量
- 00:12:03 — 开源对芯片定制化的影响
- 00:13:46 — 推理市场与 LPU 的崛起
- 00:15:17 — Agent 时代的底层芯片架构（SRAM）
- 00:16:10 — 未来推理芯片市场格局
- 00:19:50 — Agent 时代 Synopsys（新思科技）的护城河
- 00:22:10 — AI 会取代芯片硬件工程师吗？
- 00:24:09 — AI 设计芯片的边界
- 00:25:52 — Physical AI：跨越 Sim-to-Real 的挑战

## 核心议题

- GTC 与 Agent 时代的英伟达战略
- 芯片产业链利润、议价权和开源模型
- 推理芯片、LPU、SRAM 与未来市场格局
- Synopsys 与 AI 辅助芯片设计的边界
- 芯片硬件工程师角色可能发生的变化
- Physical AI 的 Sim-to-Real 挑战

## 待补充

- [x] 核对 Bilibili 规范 URL、BVID、aid、cid 和 page
- [x] 检查发布者音频 feed 与 Bilibili `part` 字段，确认没有可验证的正式期号
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取并独立验证本地音轨、sidecar、大小和 SHA-256
- [x] 记录发布者 `rights.no_reprint=1` 的来源权利边界
- [x] 生成并校验 Qwen3-ASR 机器逐字稿
- [x] 基于完整逐字稿撰写独立总结草稿
- [ ] 校对人名、公司名、芯片术语与英文缩写
- [ ] 核听关键片段并核查高影响外部事实
