---
schema_version: 1
kind: episode
id: "zhangxiaojun:103"
show_id: zhangxiaojun
episode_key: "103"
episode_number: 103
slug: 103-chen-mian
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-09
  source: publisher-rss
  url: https://www.xiaoyuzhoufm.com/episode/68455e0a6dbe9284e75c6fbf
title: "Lovart创始人陈冕复盘应用创业这两年：这一刻就是好爽啊！！哈哈哈哈哈"
navigation_title: "陈冕 · Lovart 与 AI 应用创业"
catalog_keyword: "Lovart"
published_at: "2025-07-19T11:37:52+08:00"
duration_ms: 6296698
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: chen-mian
    name: 陈冕
    role: guest
sources:
  - platform: xiaoyuzhou
    kind: episode
    title: "103. Lovart创始人陈冕复盘应用创业这两年：这一刻就是好爽啊！！哈哈哈哈哈"
    url: https://www.xiaoyuzhoufm.com/episode/68455e0a6dbe9284e75c6fbf
    preferred: false
    identifiers:
      eid: 68455e0a6dbe9284e75c6fbf
      pid: 626b46ea9cbbf0451cf5a962
      media_id: 626b46ea9cbbf0451cf5a962/lmO2h713Srj2qeJhHSqI04Y-qMje.m4a
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 68455e0a6dbe9284e75c6fbf
  - platform: bilibili
    kind: video
    title: "Lovart创始人陈冕复盘应用创业这两年：这一刻就是好爽啊！！哈哈哈哈哈"
    url: https://www.bilibili.com/video/BV1N2uXzNEBa/
    preferred: true
    identifiers:
      bvid: BV1N2uXzNEBa
      aid: "114877775547446"
      cid: "31140348644"
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
    sha256: 0bb3c5a0901cddcce5275afb00079ad98769d61b73783115b3a613b184656ac4
transcript:
  path: transcript.zh-CN.md
  platform_subtitle_access: no-anonymous-public-track
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
    planned_chunk_count: 27
    final_leaf_chunk_count: 27
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 110592
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: "2026-08-09T21:29:58.120541Z"
  quality:
    source_chunks: 27
    aligned_chunks: 27
    alignment_items: 33152
    sentence_segments: 1143
    refined_segments: 1141
    rendered_blocks: 212
    rendered_lines: 1141
  performance:
    model_load_seconds: 0.18
    transcription_seconds: 300.781
    prompt_tokens: 82348
    generation_tokens: 23095
    attempt_prompt_tokens: 82348
    attempt_generation_tokens: 23095
    generation_call_count: 27
    prompt_tokens_per_second: 273.781
    generation_tokens_per_second: 76.783
    aligner_load_seconds: 0.158
    alignment_seconds: 46.22
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
    generated_at: "2026-08-09T21:29:58.120541Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/103-chen-mian/source.m4a
  metadata_path: .cache/media/zhangxiaojun/103-chen-mian/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-09T12:33:03.129520Z"
  verified_at: "2026-08-09T12:33:03.129520Z"
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 77417326
  duration_ms: 6296698
  sha256: 470326223bfe7602a3130837f5b9581a4fe2b50868865f1fd63c4501bf1fb7f2
last_verified_at: 2026-08-09
---

# Lovart 创始人陈冕复盘应用创业这两年：这一刻就是好爽啊！！哈哈哈哈哈

> 本页保留发布者简介与章节形成的概览，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 节目：张小珺商业访谈录 #103
- 主持人：张小珺
- 嘉宾：陈冕
- Bilibili 发布时间：2025-07-19 11:37:52（UTC+8）
- Bilibili 视频时长：01:44:57；官方 RSS 音频时长：01:45:27
- RSS 正式标题：Lovart 创始人陈冕复盘应用创业这两年：这一刻就是好爽啊！！哈哈哈哈哈
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/68455e0a6dbe9284e75c6fbf)、[Bilibili 视频](https://www.bilibili.com/video/BV1N2uXzNEBa/)
- 来源状态：公开单 P；匿名状态未取得公开字幕轨，平台返回 `need_login: true` 与空 tracks；未登录且未绕过访问控制；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 完整性核验：冻结 manifest 将发布者 Bilibili 上传精确映射到 RSS 第 103 期；本地所选音轨从冷开场、节目片头和正式访谈连续覆盖至主持人告别，Bilibili 与 RSS 记录时长相差约 30.302 秒，支持将其视为完整官方视频播客版，而不是片段或高光版。本集没有专用跨平台声学采样证据；该映射不证明两版逐句相同，也不据此推断具体内容差异
- 本地音频：AAC、44.1 kHz、双声道、77,417,326 字节
- 正式期号：发布者 RSS 标题明确标注 `103.`，GUID 为 `68455e0a6dbe9284e75c6fbf`
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

Lovart 创始人陈冕从十年移动互联网履历讲到两年 AI 应用创业，复盘商业模式、补贴战、下架与现金危机，并解释团队如何从第一代专业创作工具走向面向设计师的垂类 Agent。

## 核心议题

- 商业模式、终局判断与创业者能力匹配
- 第一代产品的补贴竞争、融资节奏与现金管理
- Lovart 的画布、工作流和垂类 Agent 产品判断
- 通用与垂类 Agent、组织变化及创业者状态

## 待补充

- [x] 通过发布者 RSS 标题、GUID、enclosure 与时长核对正式第 103 期
- [x] 核对 Bilibili BVID、aid、cid、page 与发布者账号
- [x] 检查匿名访问可见的平台字幕轨，且未绕过登录控制
- [x] 获取公开音轨并完成编码、时长、大小和哈希核验
- [x] 生成完整 Qwen3-ASR 机器逐字稿及 adaptive v2 产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 核听专有名词、多人衔接与识别错误，并核查融资、估值、用户、收入、市场排名、公司内部决策、模型能力、健康与其他高影响事实
