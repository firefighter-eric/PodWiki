---
schema_version: 1
kind: episode
id: "zhangxiaojun:150"
show_id: zhangxiaojun
episode_key: "150"
episode_number: 150
slug: 150-liu-mingyu
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-15
  source: publisher-rss
title: "对英伟达研究副总裁刘洺堉的4小时访谈：Cosmos 3、世界模型、武术、黄仁勋影响我的，和你不需要击败所有对手"
navigation_title: "刘洺堉 · Cosmos 3、世界模型与竞争观"
catalog_keyword: "Cosmos"
published_at: "2026-08-13T08:00:00+08:00"
duration_ms: 12972651
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: liu-mingyu
    name: 刘洺堉
    role: guest
sources:
  - platform: xiaoyuzhou
    kind: episode
    url: https://www.xiaoyuzhoufm.com/episode/6a7cbeb017676351c5710266
    preferred: false
    identifiers:
      eid: 6a7cbeb017676351c5710266
      pid: 626b46ea9cbbf0451cf5a962
      media_id: 626b46ea9cbbf0451cf5a962/lghqbPI7EHExAvJv1gjRFV_24k8Y.m4a
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 6a7cbeb017676351c5710266
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1fmgj66EtD/
    preferred: true
    identifiers:
      bvid: BV1fmgj66EtD
      aid: "117083123744912"
      cid: "40822047496"
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
    sha256: e63fffe49e4abd364fad16878ac3221487e76292d40c84993f3f608b8d333ddc
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
    planned_chunk_count: 55
    effective_total_token_budget: 225280
  generated_at: "2026-08-15T12:08:40.927341Z"
  quality:
    source_chunks: 55
    aligned_chunks: 55
    alignment_items: 55505
    sentence_segments: 1687
    refined_segments: 1685
    rendered_blocks: 450
    rendered_lines: 1685
  performance:
    transcription_seconds: 464.408
    alignment_seconds: 68.178
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
    generated_at: "2026-08-15T12:08:40.927341Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/150-liu-mingyu/source.m4a
  metadata_path: .cache/media/zhangxiaojun/150-liu-mingyu/source.metadata.json
  git_ignored: true
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 188073224
  duration_ms: 12972651
  sha256: e9d0e7fc25ff1e8cb73c2aaa8306d750e6beff752601548ebf40a3a73f7eb4a6
  acquired_at: "2026-08-15T11:58:14.236368Z"
  verified_at: "2026-08-15T11:58:14.236368Z"
last_verified_at: 2026-08-15
---

# 对刘洺堉的 4 小时访谈：Cosmos 3、世界模型与竞争观

> 本页保留发布者简介与章节形成的结构化概览；另有依据完整机器逐字稿整理的总结草稿，尚未完成关键片段核听和独立事实核查。

## 单集信息

- 节目：张小珺商业访谈录 #150
- 主持人：张小珺
- 嘉宾：刘洺堉
- 发布时间：2026-08-13 08:00（UTC+8）
- 官方 RSS 音频时长：03:36:12
- Bilibili 视频及本地音频时长：03:36:13
- RSS GUID：`6a7cbeb017676351c5710266`
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/6a7cbeb017676351c5710266)、[Bilibili 视频](https://www.bilibili.com/video/BV1fmgj66EtD/)
- 字幕状态：匿名访问未发现独立公开字幕轨；播放器元数据提示字幕能力需要登录，但未证明登录后存在字幕
- 本地音频：AAC、48 kHz、双声道、188,073,224 字节；sidecar 已记录 SHA-256 和来源身份
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[核心观点与 5 分钟版](./summary.zh-CN.md)

## 内容概览

发布者介绍称，本期围绕刘洺堉在英伟达的研究与管理经历展开，重点讨论世界基座模型 Cosmos 从立项到 Cosmos 3 的演进、Physical AI、开源策略、GPU 资源、组织哲学与市场竞争观，并延伸到武术训练对自我控制的影响。

## 章节概览

> 以下时间码来自发布者 RSS 与 Bilibili 简介，两个来源给出的章节一致。

- 00:02:35 — 英伟达的赌注与边界
- 00:29:57 — 意外、顿悟、转变
- 01:02:46 — 如何在英伟达拿到 GPU
- 01:21:57 — 从研究员到英伟达 VP：“我可能是第一个吧”
- 01:37:00 — Cosmos 的诞生
- 01:51:39 — 从 Cosmos 1 到 Cosmos 3 的演变
- 02:36:33 — “黑客帝国”
- 02:44:20 — 下一个 CUDA？
- 02:47:04 — 关于黄仁勋：Mission is the boss
- 03:12:20 — 模型竞争不是鱿鱼游戏

## 核心议题

- Cosmos 与 Physical AI 的产品边界和长期路线
- 从研究员到研究副总裁的技术与组织路径
- 研究团队争取 GPU 与公司资源的方式
- 世界模型从 Cosmos 1 到 Cosmos 3 的演进与开源选择
- 黄仁勋所塑造的任务导向组织文化
- 从“击败对手”转向“创造市场”的竞争观
- 武术训练、自我控制与管理方法

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
