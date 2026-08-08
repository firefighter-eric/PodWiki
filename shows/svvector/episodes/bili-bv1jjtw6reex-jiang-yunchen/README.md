---
schema_version: 1
kind: episode
id: "svvector:bili-bv1jjtw6reex"
show_id: svvector
episode_key: bili-bv1jjtw6reex
episode_number: null
slug: bili-bv1jjtw6reex-jiang-yunchen
release_type: regular
numbering:
  status: unknown
  checked_at: 2026-08-08
  source: publisher-feed
  url: https://www.xiaoyuzhoufm.com/episode/6a43572c2e335a35a80ba3d8
  note: "发布者官方小宇宙 feed 收录对应单集，但标题和单集元数据均未给出正式期号；不按列表位置推导"
title: "【视频播客】硅谷坐标 x Tensormesh 江鋆晨：AI 的记忆-KvCache的三层理解"
navigation_title: "江鋆晨 · KV Cache 三层理解与 AI 记忆"
catalog_keyword: "KV Cache"
published_at: "2026-06-30T21:37:01+08:00"
duration_ms: 2742378
language: zh-CN
participants:
  - id: cao-qingyun
    name: 曹卿云
    role: host
  - id: jiang-yunchen
    name: 江鋆晨
    role: guest
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1JjTw6REEX/
    preferred: true
    identifiers:
      bvid: BV1JjTw6REEX
      aid: "116839300470624"
      cid: "39537872406"
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
    sha256: b16ec84bf710b6a0e06a021f0fe78cc264be06ecb2141343a0b37f05a8c308a3
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
  generated_at: "2026-08-08T14:52:49.491935Z"
  quality:
    source_chunks: 12
    aligned_chunks: 12
    alignment_items: 14131
    sentence_segments: 369
    refined_segments: 369
    rendered_blocks: 99
    rendered_lines: 369
  performance:
    model_load_seconds: 1.336
    transcription_seconds: 105.53
    prompt_tokens: 35867
    generation_tokens: 10199
    prompt_tokens_per_second: 339.884
    generation_tokens_per_second: 96.648
    aligner_load_seconds: 0.165
    alignment_seconds: 19.043
asr_artifacts:
  raw:
    path: asr/qwen3-asr/raw.json
    git_ignored: false
    format: podwiki-raw-asr-json-v1
    sha256: a6e77c1e40e0c92525ad979593b8dc598e2facdd6e52d8fe04a75d5b59690028
  aligned:
    path: asr/qwen3-asr/aligned.json
    git_ignored: false
    format: podwiki-aligned-asr-json-v1
    sha256: e628e7d2cdf90c1f6303c416d37d0bde1d7d07a5474b8336c427d7075119199a
  refined:
    path: asr/qwen3-asr/refined.json
    git_ignored: false
    format: podwiki-refined-asr-json-v1
    sha256: 35a61bf5a79810cbae0a31f047966b977456eb736370fe99edd81304d0bfd4d2
  transcript:
    path: asr/qwen3-asr/transcript.zh-CN.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
    sha256: b16ec84bf710b6a0e06a021f0fe78cc264be06ecb2141343a0b37f05a8c308a3
  renderer: scripts/render_asr_transcript.py
asr_runs:
  - id: qwen3-asr-1.7b-8bit
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    generated_at: "2026-08-08T14:52:49.491935Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/svvector/bili-bv1jjtw6reex-jiang-yunchen/source.m4a
  metadata_path: .cache/media/svvector/bili-bv1jjtw6reex-jiang-yunchen/source.metadata.json
  git_ignored: true
  extractor: BiliBili
  acquired_at: "2026-08-08T14:17:06.937840Z"
  verified_at: "2026-08-08T14:17:06.937840Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 43557782
  duration_ms: 2742379
  sha256: 1f2e63bb890a4b643c35f197d795b2e8161cf8ddbde27b7f810e7f7fc3550590
last_verified_at: 2026-08-08
---

# 【视频播客】硅谷坐标 x Tensormesh 江鋆晨：AI 的记忆-KvCache的三层理解

> 本页保留 Bilibili 发布者简介及时间轴形成的概览；另有依据完整机器逐字稿整理的总结草稿。关键片段尚未逐段核听，人物经历、技术判断、产品信息和外部事实也尚未独立核查。

## 单集信息

- 节目：硅谷坐标 SV-Vector
- 主持人：曹卿云
- 嘉宾：江鋆晨，发布者介绍为 TensorMesh 和 LMCache 联合创始人、TensorMesh CEO、芝加哥大学计算机系副教授
- 发布时间：2026-06-30 21:37:01（UTC+8）
- Bilibili 来源时长：00:45:42.378
- 本地音轨：00:45:42.379（AAC、48 kHz、双声道）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1JjTw6REEX/)
- 编号状态：发布者官方小宇宙 feed 收录对应音频单集，但没有给出正式期号；保留 `episode_number: null`，不按发布日期或列表位置推导
- 字幕状态：匿名 view/player 元数据未列出公开字幕轨，sidecar 同时标记字幕查询需要登录；这里只能确认“未发现匿名公开字幕轨”，不能排除登录可见字幕或画面硬字幕
- 转载边界：Bilibili 公开元数据标记 `no_reprint: 1`；这里只将其记录为来源与转载边界，不把技术可下载性解释为转载授权
- 本地来源：独立音轨已通过编码、采样率、声道、时长、大小和 SHA-256 校验
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[核心观点与 5 分钟版](./summary.zh-CN.md)
- 当前状态：机器逐字稿已完成并选为正式稿，总结为 `draft`；说话人、专有名词、技术细节和外部事实仍待人工复核

## 内容概览

发布者简介称，本期由曹卿云与江鋆晨讨论 AI 的“记忆与存储”。江鋆晨所参与创办的 TensorMesh 与开源项目 LMCache 聚焦大模型记忆管理，访谈从 Prefill 与 Decode 的资源和成本差异切入，解释 KV Cache 在推理系统中的作用。

简介把 KV Cache 分成三层理解：首先是可以保存和复用的计算状态；其次是包含注意力和语义信息、能够在保持语义的前提下被压缩或改造的数据；再次是可以通过改变其中信息来影响模型注意力和输出的操作层。节目也讨论学术界与工业界在这一方向上的认知差异、典型企业客户、竞争格局和软硬件投入之间的经济账。

后半段延伸到存储层级、传输速度与成本的权衡，大模型市场可能呈现的格局，中国模型的前景，以及 Transformer 之外架构变化对 KV Cache 路线的影响。本节只转述发布者材料，不代表这些技术判断已经由 PodWiki 独立验证。

## 章节概览

> 以下时间码和标题来自 Bilibili 发布者简介，并非平台独立章节轨。

- 00:52 — AI 推理瓶颈：资源与 workflow 的不对等
- 02:01 — TensorMesh 到底解决哪一个环节
- 03:20 — 反直觉的成本真相：贵的不是输出，是输入
- 07:10 — 与模型厂 cached token 的区别
- 08:50 — KV Cache 的三层理解
- 11:30 — 为什么学术界领先工业界
- 15:10 — 客户画像：拥有共享知识库的企业
- 20:45 — 与竞争对手的区别
- 22:00 — 对“压缩”的看法
- 23:35 — 多模态时代，KV Cache 怎么扩展
- 25:15 — 存储供给瓶颈看法
- 25:40 — 经济账：以存代算
- 27:00 — 这个存储周期有什么不同
- 28:42 — 存储传输速度与成本的 tradeoff
- 30:35 — 哪个存储层受益最多
- 32:30 — 历史的回响：KV Cache 之于 CDN
- 35:50 — 公司顾问 Ion Stoica 和 Hui Zhang，与 Databricks / Spark
- 37:30 — Tokenmaxxing 和 utilization efficiency 的机会与挑战
- 39:57 — 模型格局：大模型像在线视频，不像搜索
- 41:23 — 如何看中国模型前景
- 42:08 — 如果从 Transformer 架构换成 Mamba
- 43:38 — xAI 收购 Cursor
- 44:22 — AI 时代的汽油：懂 KV Cache 的人接触不到它，接触得到的人不懂它

## 核心议题

- Agent 和长上下文工作负载中的 AI 推理瓶颈
- Prefill、Decode 与输入侧成本结构
- KV Cache 作为计算状态、语义数据和模型操作层的三层理解
- TensorMesh、LMCache 与企业共享知识场景
- KV Cache 压缩、跨存储层复用和软硬件经济账
- 学术研究、工业落地与开源生态之间的差异
- 大模型市场格局、中国模型与架构变化

## 待补充

- [x] 核对规范来源、发布账号、BVID、aid、cid 和 page
- [x] 核对发布者官方小宇宙 feed，确认单集已收录但没有明确正式期号
- [x] 检查匿名访问可见的平台字幕轨并记录登录提示边界
- [x] 获取独立音轨并完成编码、时长、大小和哈希校验
- [x] 使用 Qwen3-ASR 与 ForcedAligner 生成中文机器逐字稿
- [x] 基于完整正式逐字稿生成结构化中文总结
- [ ] 校对说话人、公司名、模型名、系统术语和英文缩写
- [ ] 核听关键片段并独立核查高影响外部事实
