---
schema_version: 1
kind: episode
id: "svvector:bili-bv1zvqkb5egd"
show_id: svvector
episode_key: bili-bv1zvqkb5egd
episode_number: null
slug: bili-bv1zvqkb5egd-huang-dongxu
release_type: regular
numbering:
  status: unknown
  checked_at: 2026-08-08
  source: publisher-xiaoyuzhou
  url: https://www.xiaoyuzhoufm.com/episode/69d9bef7e2c8be3155e93e3a
  note: "发布者小宇宙节目 feed 已收录本期，但单集标题未标注正式期号；不根据发布时间或相邻单集推导"
title: "硅谷坐标 x黄东旭-龙虾的“记忆” ：谈 Agent 时代基础设施的重构"
navigation_title: "黄东旭 · Agent 记忆与基础设施重构"
catalog_keyword: "Agent 记忆"
published_at: "2026-04-11T11:13:36+08:00"
duration_ms: 2670848
language: zh-CN
participants:
  - id: cao-qingyun
    name: 曹卿云
    role: host
  - id: huang-dongxu
    name: 黄东旭
    role: guest
    profile:
      headline: "PingCAP 联合创始人兼 CTO、数据库专家"
      affiliations:
        - organization: "PingCAP"
          title: "联合创始人兼 CTO"
          status: current
      checked_at: "2026-08-08"
sources:
  - platform: xiaoyuzhou
    kind: episode
    url: https://www.xiaoyuzhoufm.com/episode/69d9bef7e2c8be3155e93e3a
    preferred: false
    identifiers:
      eid: 69d9bef7e2c8be3155e93e3a
      pid: 69a4b82b27e15c06061cfc2d
      media_id: 69a4b82b27e15c06061cfc2d/lmMa4hQhV1iyAtFivUQl8ZBc3YjG.m4a
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1zvQKB5EGd/
    preferred: true
    identifiers:
      bvid: BV1zvQKB5EGd
      aid: "116383866232205"
      cid: "37408278249"
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
    sha256: f0555c106a0b45ca4e627f7346cc69592f8e8f4de1bf72b954c634f4b9d775be
transcript:
  path: transcript.zh-CN.md
  translations: []
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
    temperature: 0.0
    max_tokens_per_chunk: 4096
    chunk_duration_seconds: 240.0
    max_sentence_characters: 160
  generated_at: "2026-08-08T14:57:42.946761Z"
  quality:
    source_chunks: 12
    aligned_chunks: 12
    alignment_items: 12121
    sentence_segments: 340
    refined_segments: 340
    rendered_blocks: 91
    rendered_lines: 340
  performance:
    model_load_seconds: 1.362
    transcription_seconds: 84.179
    prompt_tokens: 34939
    generation_tokens: 7907
    prompt_tokens_per_second: 415.064
    generation_tokens_per_second: 93.933
    aligner_load_seconds: 0.227
    alignment_seconds: 17.009
asr_artifacts:
  raw:
    path: asr/qwen3-asr/raw.json
    git_ignored: false
    format: podwiki-raw-asr-json-v1
    sha256: 159db4dec6507edad99673308bcd18921c07630af9ade7c39b8acc7b3d47f2ee
  aligned:
    path: asr/qwen3-asr/aligned.json
    git_ignored: false
    format: podwiki-aligned-asr-json-v1
    sha256: 9f749e2f9027688dcd436d0071a696a204d9990749ae074bac13f5b748b6c80b
  refined:
    path: asr/qwen3-asr/refined.json
    git_ignored: false
    format: podwiki-refined-asr-json-v1
    sha256: 8d17f707a51bdb325af3e2ad074e57f7f7330dc317dd30057ab718f4c555ca21
  transcript:
    path: asr/qwen3-asr/transcript.zh-CN.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
    sha256: f0555c106a0b45ca4e627f7346cc69592f8e8f4de1bf72b954c634f4b9d775be
  renderer: scripts/render_asr_transcript.py
asr_runs:
  - id: qwen3-asr-1.7b-8bit
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    generated_at: "2026-08-08T14:57:42.946761Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/svvector/bili-bv1zvqkb5egd-huang-dongxu/source.m4a
  metadata_path: .cache/media/svvector/bili-bv1zvqkb5egd-huang-dongxu/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-08T14:18:04.938060Z"
  verified_at: "2026-08-08T14:18:04.938060Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 39937603
  duration_ms: 2670848
  sha256: 4db6fe198f42f23ebae8561d2f8972f1bf50e84957145a1b07b457ca31c3ed17
last_verified_at: 2026-08-08
---

# 硅谷坐标 x黄东旭-龙虾的“记忆” ：谈 Agent 时代基础设施的重构

> 本页保留 Bilibili 与发布者小宇宙简介形成的内容概览；另有依据完整机器逐字稿整理的总结草稿。关键片段尚未逐段核听，产品、数字、技术判断和外部事实也尚未独立核查。

## 单集信息

- 节目：硅谷坐标 SV-Vector（官方节目 feed 已收录，未标正式期号）
- 主持人：曹卿云
- 嘉宾：黄东旭，发布者介绍为 PingCAP 联合创始人兼 CTO、资深数据库专家、连续创业者
- 发布时间：2026-04-11 11:13:36（UTC+8）
- Bilibili 来源元数据时长：00:44:30.847
- 本地 Bilibili 音轨：00:44:30.848（AAC、48 kHz、双声道）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1zvQKB5EGd/)、[发布者小宇宙单集页](https://www.xiaoyuzhoufm.com/episode/69d9bef7e2c8be3155e93e3a)
- 编号状态：截至 2026-08-08，发布者小宇宙节目 feed 已收录本期，但标题未给出正式期号；保留 `episode_number: null`，不按发布时间或相邻内容推导
- 字幕状态：匿名访问未发现独立公开字幕轨；平台字幕元数据提示字幕能力需要登录，但这不能证明登录后一定存在字幕，处理过程未使用 cookies 或登录态
- 来源权利提示：Bilibili 公开元数据记录 `rights.no_reprint=1`；本页仅记录来源与研究材料，不转载原媒体。`download=1` 只是平台元数据字段，不视为项目取得转载或其他额外授权
- 本地来源：音轨已获取，并通过独立 ffprobe、文件大小和 SHA-256 校验
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[核心观点与 5 分钟版](./summary.zh-CN.md)
- 处理状态：机器逐字稿已完成并选为正式稿，总结为 `draft`；说话人、专名、数字、隐私安全与关键技术判断仍待人工复核

## 内容概览

发布者简介称，本期由主持人曹卿云采访黄东旭，围绕 AI Agent 的记忆问题、存储新范式、基础设施生态和组织影响展开。讨论从普通用户开始使用 Agent 的产品形态切入，梳理 Prompt、Context 与 Harness Engineering 的演进，并区分上下文窗口和外挂记忆所承担的短期、长期记忆职责。

后续议题包括 Agent 时代的数据特点、“一虾一库”的存储设想、记忆层的商业化路径、向量数据库的定位，以及 SQL、文件系统和多 Agent 协同。发布者简介还把讨论延伸到人与 Agent 的协作方式及其对团队结构和软件工程的影响；这些观点当前仅按发布者材料概括，需在完整逐字稿生成后回到原文核对。

## 章节概览

> 以下时间码和标题来自 Bilibili 发布者简介。

- 01:36 — 普通人开始“养龙虾”，Agent native 产品形态正式出现
- 03:31 — 三代演进：从 Prompt 到 Context 再到 Harness Engineering
- 09:15 — 单体 Agent 的灾难性失忆与 compaction 困境
- 10:28 — 上下文窗口与外挂记忆：短期和长期记忆的本质差异
- 14:38 — 解决记忆问题的产品哲学：怎么记、怎么提取
- 17:28 — Agent 时代的数据特点与数据价值
- 23:31 — “一虾一库”：Agent 时代的数据存储新范式
- 27:17 — 记忆层的商业化路径：从备份订阅到领域专家知识变现
- 29:14 — 以 Agent 为最终使用者的基础设施生态链重构
- 33:16 — 向量数据库终局：独立向量数据库将被收敛
- 34:51 — SQL 与文件系统：经典接口在 Agent 时代依然是第一语言
- 36:25 — 下一个边界突破：多 Agent 协同下的 Scaling Law
- 37:54 — 人与 Agent 协作的最佳范式
- 40:04 — Agent 带来的组织架构冲击：高度碎片化的部落型团队
- 41:37 — 上一个时代的软件工程的终结：在变中寻找不变

## 核心议题

- Agent 的短期记忆、长期记忆与上下文压缩问题
- Prompt、Context 与 Harness Engineering 的产品演进
- Agent 时代的数据特点、数据价值和存储接口
- 记忆层、向量数据库、SQL 与文件系统的定位
- 多 Agent 协同和基础设施生态链重构
- 人与 Agent 的协作方式及其组织影响

## 待补充

- [x] 核对 Bilibili 视频的规范 URL、BVID、aid、cid 和 page
- [x] 核对发布者小宇宙节目页及其编号展示
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取并独立验证本地音轨、来源 sidecar、大小和 SHA-256
- [x] 记录发布者 `rights.no_reprint=1` 的来源权利提示
- [x] 使用 Qwen3-ASR 与 ForcedAligner 生成机器逐字稿
- [ ] 校对主持人、嘉宾、专有名词、数字和断句
- [x] 基于完整机器逐字稿生成总结草稿
- [ ] 核听关键片段并完成必要事实核查
