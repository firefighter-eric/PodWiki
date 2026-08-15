---
schema_version: 1
kind: episode
id: "zhangxiaojun:117"
show_id: zhangxiaojun
episode_key: "117"
episode_number: 117
slug: 117-xie-qingchi
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-09
  source: publisher-rss
  url: https://www.xiaoyuzhoufm.com/episode/68ff9d1b083a71a4eb86c52c
title: "干货！开源一段论文探索之旅给大家"
navigation_title: "谢青池 · AI 论文与模型范式"
catalog_keyword: "AI论文"
published_at: "2025-10-28T10:24:46+08:00"
duration_ms: 15757502
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: xie-qingchi
    name: 谢青池
    role: guest
sources:
  - platform: xiaoyuzhou
    kind: episode
    title: "117. 开源一段论文探索之旅：模型范式、Infra和数据、语言、多模态的完整变迁史"
    url: https://www.xiaoyuzhoufm.com/episode/68ff9d1b083a71a4eb86c52c
    preferred: false
    identifiers:
      eid: 68ff9d1b083a71a4eb86c52c
      pid: 626b46ea9cbbf0451cf5a962
      media_id: 626b46ea9cbbf0451cf5a962/ludOBUWHSc2Y_GA47pSOwlGC8JPS.m4a
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 68ff9d1b083a71a4eb86c52c
  - platform: bilibili
    kind: video
    title: "干货！开源一段论文探索之旅给大家"
    url: https://www.bilibili.com/video/BV1pkyqBxEdB/
    preferred: true
    identifiers:
      bvid: BV1pkyqBxEdB
      aid: "115449392204906"
      cid: "33448463916"
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
    sha256: 4e29ad575c514848b33dc463975903bedeaeb9938d597ba3bfab64e39d7d731a
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
    planned_chunk_count: 66
    final_leaf_chunk_count: 66
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 270336
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: "2026-08-09T22:08:09.384553Z"
  quality:
    source_chunks: 66
    aligned_chunks: 66
    alignment_items: 72183
    sentence_segments: 1987
    refined_segments: 1987
    rendered_blocks: 532
    rendered_lines: 1987
  performance:
    model_load_seconds: 0.18
    transcription_seconds: 663.009
    prompt_tokens: 206042
    generation_tokens: 50282
    attempt_prompt_tokens: 206042
    attempt_generation_tokens: 50282
    generation_call_count: 66
    prompt_tokens_per_second: 310.768
    generation_tokens_per_second: 75.839
    aligner_load_seconds: 0.169
    alignment_seconds: 100.893
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
    generated_at: "2026-08-09T22:08:09.384553Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/117-xie-qingchi/source.m4a
  metadata_path: .cache/media/zhangxiaojun/117-xie-qingchi/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-09T12:34:01.383395Z"
  verified_at: "2026-08-09T12:34:01.383395Z"
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 144579120
  duration_ms: 15757502
  sha256: 6a198473853688bca3bcc53946bc2df9c8cf1cd4c0820b5cc82058f4af6cbcfc
last_verified_at: 2026-08-09
---

# 干货！开源一段论文探索之旅给大家

> 本页保留 Bilibili 原标题与发布者简介、章节形成的概览，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。RSS 正式标题另行原样保留，不用 Bilibili 标题反推期号或改写 RSS 标题。

## 单集信息

- 节目：张小珺商业访谈录 #117
- 主持人：张小珺
- 嘉宾：谢青池
- Bilibili 发布时间：2025-10-28 10:24:46（UTC+8）
- Bilibili 视频时长：04:22:38；官方 RSS 音频时长：04:22:37
- RSS 正式标题：117. 开源一段论文探索之旅：模型范式、Infra和数据、语言、多模态的完整变迁史
- Bilibili 原标题：干货！开源一段论文探索之旅给大家
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/68ff9d1b083a71a4eb86c52c)、[Bilibili 视频](https://www.bilibili.com/video/BV1pkyqBxEdB/)
- 来源状态：公开单 P；匿名状态下平台返回 `need_login: false` 与空 tracks，未取得公开字幕轨；未登录且未绕过访问控制；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 完整性核验：发布者 RSS 正文明确把同一 Bilibili BVID 标为本集投屏视频版，并给出与视频简介一致的四部分论文时间线；冻结 manifest 将该上传精确映射到 RSS 第 117 期。两端时长仅相差约 0.502 秒，本地所选音轨从冷开场、节目片头和嘉宾介绍连续覆盖至节目收尾，支持将其视为完整官方视频播客版，而不是片段或高光版。该映射不证明两版逐句相同
- 本地音频：AAC、44.1 kHz、双声道、144,579,120 字节
- 正式期号：发布者 RSS 标题明确标注 `117.`，GUID 为 `68ff9d1b083a71a4eb86c52c`；Bilibili 标题没有期号，未据其推断编号
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

谢青池把阅读两百多篇 AI 论文形成的探索路径整理成一次长篇分享：先讲如何用历史、人物与范式理解论文，再沿模型结构、Infra 与数据、语言模型和多模态四条时间线串联关键工作，最后回到技术边界、产品判断与 AI 从业者的学习方式。

## 核心议题

- AI 论文阅读方法与学习路径
- 从 GPU、AlexNet、Transformer 到强化学习、MoE 与后训练的模型范式
- ZeRO、Scaling Law、开源数据集与万卡训练的 Infra/数据演进
- 从 Word2Vec、GPT/BERT 到 InstructGPT 的语言模型路线
- 从视频理解、GAN/Diffusion 到 ViT、CLIP、Stable Diffusion 与 DiT 的多模态路线
- 技术—硬件协同、模型边界、全栈 builder 与长期学习

## 待补充

- [x] 通过发布者 RSS 标题、GUID、enclosure 与时长核对正式第 117 期
- [x] 核对 Bilibili BVID、aid、cid、page 与发布者账号
- [x] 检查匿名访问可见的平台字幕轨，且未绕过登录控制
- [x] 获取公开音轨并完成编码、时长、大小和哈希核验
- [x] 生成完整 Qwen3-ASR 机器逐字稿及 adaptive v2 产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 核听主持人/嘉宾姓名、论文与作者专名、公司和产品名、英文缩写与多人衔接；重点处理机器稿中的近音误识别，并核查论文年份、模型参数、数据集规模、GPU/集群规模、训练时长、正确率、引用量、成本、公司职务与收购、产品能力、行业判断和预测等数字与高影响事实
