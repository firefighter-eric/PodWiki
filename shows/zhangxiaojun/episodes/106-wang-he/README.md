---
schema_version: 1
kind: episode
id: "zhangxiaojun:106"
show_id: zhangxiaojun
episode_key: "106"
episode_number: 106
slug: 106-wang-he
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-09
  source: publisher-rss
  url: https://www.xiaoyuzhoufm.com/episode/6857f2174abe6e29cb65d76e
title: "机器人泡沫了吗？和10亿美金创始人聊：资本轰炸下的具身智能真相"
navigation_title: "王鹤 · 具身智能与资本热潮"
catalog_keyword: "具身智能"
published_at: "2025-07-02T19:00:00+08:00"
duration_ms: 9490943
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: wang-he
    name: 王鹤
    role: guest
sources:
  - platform: xiaoyuzhou
    kind: episode
    title: "106. 和王鹤聊，具身智能的学术边缘史和资本轰炸后的人为乱象"
    url: https://www.xiaoyuzhoufm.com/episode/6857f2174abe6e29cb65d76e
    preferred: false
    identifiers:
      eid: 6857f2174abe6e29cb65d76e
      pid: 626b46ea9cbbf0451cf5a962
      media_id: 626b46ea9cbbf0451cf5a962/ljW674lpeFFafN4uO3zPJ38RlWD5.m4a
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 6857f2174abe6e29cb65d76e
  - platform: bilibili
    kind: video
    title: "机器人泡沫了吗？和10亿美金创始人聊：资本轰炸下的具身智能真相"
    url: https://www.bilibili.com/video/BV1WLgQz8Enk/
    preferred: true
    identifiers:
      bvid: BV1WLgQz8Enk
      aid: "114778487917310"
      cid: "30797071359"
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
    sha256: af4d8027e240dabc2c9b3dc40b7cb951b6233523aae698a92e0155cb55b26278
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
    planned_chunk_count: 40
    final_leaf_chunk_count: 40
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 163840
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: "2026-08-09T21:37:32.682246Z"
  quality:
    source_chunks: 40
    aligned_chunks: 40
    alignment_items: 37924
    sentence_segments: 1041
    refined_segments: 1041
    rendered_blocks: 337
    rendered_lines: 1041
  performance:
    model_load_seconds: 0.188
    transcription_seconds: 382.717
    prompt_tokens: 124104
    generation_tokens: 26939
    attempt_prompt_tokens: 124104
    attempt_generation_tokens: 26939
    generation_call_count: 40
    prompt_tokens_per_second: 324.271
    generation_tokens_per_second: 70.389
    aligner_load_seconds: 0.276
    alignment_seconds: 61.473
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
    generated_at: "2026-08-09T21:37:32.682246Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/106-wang-he/source.m4a
  metadata_path: .cache/media/zhangxiaojun/106-wang-he/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-09T12:33:08.916498Z"
  verified_at: "2026-08-09T12:33:08.916498Z"
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 143774009
  duration_ms: 9490943
  sha256: 251cc4c2a275177e19695f316ab1c57c83d9d73853014620c189f23ef087a73c
last_verified_at: 2026-08-09
---

# 机器人泡沫了吗？和 10 亿美金创始人聊：资本轰炸下的具身智能真相

> 本页保留发布者简介与章节形成的概览，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 节目：张小珺商业访谈录 #106
- 主持人：张小珺
- 嘉宾：王鹤
- Bilibili 发布时间：2025-07-02 19:00:00（UTC+8）
- Bilibili 视频时长：02:38:11；官方 RSS 音频时长：02:38:52
- RSS 正式标题：和王鹤聊，具身智能的学术边缘史和资本轰炸后的人为乱象
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/6857f2174abe6e29cb65d76e)、[Bilibili 视频](https://www.bilibili.com/video/BV1WLgQz8Enk/)
- 来源状态：公开单 P；匿名状态未取得公开字幕轨，平台返回 `need_login: true` 与空 tracks；未登录且未绕过访问控制；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 完整性核验：冻结 manifest 将发布者 Bilibili 上传映射到 RSS 第 106 期，发布者简介明确称其为《商业访谈录》机器人专场，并列出从正式开场到“最后的快问快答”的贯穿式章节；本地所选音轨从冷开场、节目片头和正式访谈连续覆盖至主持人告别。Bilibili 与 RSS 记录时长相差约 41.058 秒，支持将其视为完整官方视频播客版，而不是片段或高光版。本集没有专用跨平台声学采样证据；该映射不证明两版逐句相同，也不据此推断具体内容差异
- 本地音频：AAC、44.1 kHz、双声道、143,774,009 字节
- 正式期号：发布者 RSS 标题明确标注 `106.`，GUID 为 `6857f2174abe6e29cb65d76e`
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

北京大学助理教授、银河通用创始人兼 CTO 王鹤梳理具身智能从计算机视觉边缘流派走向资本中心的过程，并讨论机器人软硬件、场景泛化、真实与合成数据、生产力产品和行业宣传边界。

## 核心议题

- 具身智能、机器人、视觉、语言和智能的学术关系
- 从人类视频、物体位姿到合成数据的研究路径
- 软硬件选择、场景内泛化和商业复制
- 生产力、遥操披露、规模应用与资本泡沫

## 待补充

- [x] 通过发布者 RSS 标题、GUID、enclosure 与时长核对正式第 106 期
- [x] 核对 Bilibili BVID、aid、cid、page 与发布者账号
- [x] 检查匿名访问可见的平台字幕轨，且未绕过登录控制
- [x] 获取公开音轨并完成编码、时长、大小和哈希核验
- [x] 生成完整 Qwen3-ASR 机器逐字稿及 adaptive v2 产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 核听专有名词、多人衔接与识别错误，并核查学术史、论文贡献、融资估值、产品指标、同行评价、技术效果、神经科学、人口数据与其他高影响事实
