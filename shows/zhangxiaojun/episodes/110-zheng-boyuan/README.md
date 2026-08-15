---
schema_version: 1
kind: episode
id: "zhangxiaojun:110"
show_id: zhangxiaojun
episode_key: "110"
episode_number: 110
slug: 110-zheng-boyuan
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-09
  source: publisher-rss
  url: https://www.xiaoyuzhoufm.com/episode/6889da698e06fe8de77116a9
title: "逐段讲解Kimi K2报告并对照ChatGPT Agent、Qwen3-Coder等：“系统工程的力量”"
navigation_title: "郑博元 · Kimi K2 与 Agent 系统"
catalog_keyword: "Kimi K2"
published_at: "2025-07-31T12:27:33+08:00"
duration_ms: 8438349
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: zheng-boyuan
    name: 郑博元
    role: guest
sources:
  - platform: xiaoyuzhou
    kind: episode
    title: "110. 逐段讲解Kimi K2报告并对照ChatGPT Agent、Qwen3-Coder等：“系统工程的力量”"
    url: https://www.xiaoyuzhoufm.com/episode/6889da698e06fe8de77116a9
    preferred: false
    identifiers:
      eid: 6889da698e06fe8de77116a9
      pid: 626b46ea9cbbf0451cf5a962
      media_id: 626b46ea9cbbf0451cf5a962/lmPsWiJp6-hqPoFKrgtPxhcvrVJb.m4a
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 6889da698e06fe8de77116a9
  - platform: bilibili
    kind: video
    title: "逐段讲解Kimi K2报告并对照ChatGPT Agent、Qwen3-Coder等：“系统工程的力量”"
    url: https://www.bilibili.com/video/BV1cc8kzmEBs/
    preferred: true
    identifiers:
      bvid: BV1cc8kzmEBs
      aid: "114945941311077"
      cid: "31392595997"
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
    sha256: 1a95a4b26698c16b544766f8c3ce64819f086a1c4f198ab8f01d69084de4ce43
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
    planned_chunk_count: 36
    final_leaf_chunk_count: 36
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 147456
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: "2026-08-09T21:44:39.531077Z"
  quality:
    source_chunks: 36
    aligned_chunks: 36
    alignment_items: 36282
    sentence_segments: 834
    refined_segments: 833
    rendered_blocks: 309
    rendered_lines: 833
  performance:
    model_load_seconds: 0.181
    transcription_seconds: 360.848
    prompt_tokens: 110350
    generation_tokens: 25225
    attempt_prompt_tokens: 110350
    attempt_generation_tokens: 25225
    generation_call_count: 36
    prompt_tokens_per_second: 305.808
    generation_tokens_per_second: 69.905
    aligner_load_seconds: 0.19
    alignment_seconds: 56.89
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
    generated_at: "2026-08-09T21:44:39.531077Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/110-zheng-boyuan/source.m4a
  metadata_path: .cache/media/zhangxiaojun/110-zheng-boyuan/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-09T12:33:13.036897Z"
  verified_at: "2026-08-09T12:33:13.036897Z"
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 86092688
  duration_ms: 8438349
  sha256: df1de6a2d9d996e4a5bbb6cada7456a8998e34367f55037da4818ecdd663d99c
last_verified_at: 2026-08-09
---

# 逐段讲解 Kimi K2 报告并对照 ChatGPT Agent、Qwen3-Coder 等：“系统工程的力量”

> 本页保留发布者简介与章节形成的概览，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 节目：张小珺商业访谈录 #110
- 主持人：张小珺
- 嘉宾：郑博元
- Bilibili 发布时间：2025-07-31 12:27:33（UTC+8）
- Bilibili 视频时长：02:20:39；官方 RSS 音频时长：02:20:45
- RSS 正式标题：逐段讲解 Kimi K2 报告并对照 ChatGPT Agent、Qwen3-Coder 等：“系统工程的力量”
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/6889da698e06fe8de77116a9)、[Bilibili 视频](https://www.bilibili.com/video/BV1cc8kzmEBs/)
- 来源状态：公开单 P；匿名状态未取得公开字幕轨，平台返回 `need_login: true` 与空 tracks；未登录且未绕过访问控制；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 完整性核验：冻结 manifest 将发布者 Bilibili 上传精确映射到 RSS 第 110 期；两端标题一致，时长相差约 6.652 秒，本地所选音轨从冷开场、节目片头和嘉宾介绍连续覆盖至主持人告别，支持将其视为完整官方视频播客版，而不是片段或高光版。该映射不证明两版逐句相同，也不据此推断具体内容差异
- 本地音频：AAC、44.1 kHz、双声道、86,092,688 字节
- 正式期号：发布者 RSS 标题明确标注 `110.`，GUID 为 `6889da698e06fe8de77116a9`
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

郑博元与张小珺从 Agent 的环境交互定义出发，逐段阅读 Kimi K2、ChatGPT Agent、Qwen3-Coder 与 Manus 的公开技术材料，串起合成轨迹、可验证奖励、沙盒基础设施、上下文工程和 Agent 自我提升等问题。

## 核心议题

- Agent 的观察—行动循环、应用分类与安全边界
- Kimi K2 的工具使用数据合成、奖励设计和训练基础设施
- ChatGPT Agent、Qwen3-Coder 与 Manus 的技术路线比较
- Agent 自我提升、记忆管理和人机协作形态

## 待补充

- [x] 通过发布者 RSS 标题、GUID、enclosure 与时长核对正式第 110 期
- [x] 核对 Bilibili BVID、aid、cid、page 与发布者账号
- [x] 检查匿名访问可见的平台字幕轨，且未绕过登录控制
- [x] 获取公开音轨并完成编码、时长、大小和哈希核验
- [x] 生成完整 Qwen3-ASR 机器逐字稿及 adaptive v2 产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 核听中英文专名、论文与产品名、多人衔接和识别错误，并核查模型能力、训练数据、工具与环境数量、成本、基准分数、产品与研究判断、安全案例及其他高影响事实
