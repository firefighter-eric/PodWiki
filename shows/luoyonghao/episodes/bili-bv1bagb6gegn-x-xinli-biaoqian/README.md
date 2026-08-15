---
schema_version: 1
kind: episode
id: "luoyonghao:bili-bv1bagb6gegn"
show_id: luoyonghao
episode_key: "bili-bv1bagb6gegn"
episode_number: null
slug: bili-bv1bagb6gegn-x-xinli-biaoqian
release_type: special
numbering:
  status: unknown
  checked_at: 2026-08-09
  source: publisher-rss-branch-and-season
  url: https://feed.xyzfm.space/wmnkvmrpwuww
  note: "发布者明确将其定义为《十字路口》分支系列《X字路口》的完整播客正片，但未提供正式期号；不根据发布日期或合集顺序推导"
title: "【正片】罗永浩的X字路口！“精神病”失控大乱斗，强迫症、ADHD、攻击型人格障碍......."
navigation_title: "小镟、林简七、史里芬、曹国 · 性格与心理标签"
catalog_keyword: "人格标签"
published_at: "2026-07-24T12:02:10+08:00"
duration_ms: 9190293
language: zh-CN
participants:
  - id: xiao-xuan
    name: "小镟"
    aliases: []
    role: guest
  - id: lin-jianqi
    name: "林简七"
    aliases: []
    role: guest
  - id: shi-lifen
    name: "史里芬"
    aliases: []
    role: guest
  - id: cao-guo
    name: "曹国"
    aliases: []
    role: guest
sources:
  - platform: bilibili
    kind: video
    title: "【正片】罗永浩的X字路口！“精神病”失控大乱斗，强迫症、ADHD、攻击型人格障碍......."
    url: https://www.bilibili.com/video/BV1Bagb6gEgN/
    preferred: true
    identifiers:
      bvid: BV1Bagb6gEgN
      aid: "116972343854758"
      cid: "40240481107"
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
    sha256: 204e3de8d55f522fbaf9390740b7a7fc5b94a745f5e4136f60b9371be07b04ec
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
    planned_chunk_count: 39
    final_leaf_chunk_count: 39
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 159744
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: "2026-08-09T19:53:59.639895Z"
  quality:
    source_chunks: 39
    aligned_chunks: 39
    alignment_items: 47681
    sentence_segments: 2493
    refined_segments: 2487
    rendered_blocks: 295
    rendered_lines: 2487
  performance:
    model_load_seconds: 0.176
    transcription_seconds: 498.957
    prompt_tokens: 120183
    generation_tokens: 36720
    attempt_prompt_tokens: 120183
    attempt_generation_tokens: 36720
    generation_call_count: 39
    prompt_tokens_per_second: 240.868
    generation_tokens_per_second: 73.593
    aligner_load_seconds: 0.19
    alignment_seconds: 66.353
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
    generated_at: "2026-08-09T19:53:59.639895Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/luoyonghao/bili-bv1bagb6gegn-x-xinli-biaoqian/source.m4a
  metadata_path: .cache/media/luoyonghao/bili-bv1bagb6gegn-x-xinli-biaoqian/source.metadata.json
  git_ignored: true
  recovered_at: "2026-08-09T12:32:22.368264Z"
  verified_at: "2026-08-09T12:32:22.368264Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 140079094
  duration_ms: 9190293
  sha256: 0813d8d20dc10f128a61873a14b8790df5b14e24c5ff81af82ef325f5622f16e
last_verified_at: 2026-08-09
---

# 【正片】罗永浩的X字路口！“精神病”失控大乱斗，强迫症、ADHD、攻击型人格障碍.......

> 本页保留发布者材料形成的内容提纲，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 节目：罗永浩的十字路口
- 嘉宾：小镟、林简七、史里芬、曹国
- 发布时间：2026-07-24 12:02:10（UTC+8）
- Bilibili 视频时长：02:33:10
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1Bagb6gEgN/)
- 来源状态：公开单 P；匿名访问未发现公开字幕轨；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 本地音频：AAC、48 kHz、双声道、140,079,094 字节
- 编号状态：《X字路口》为发布者确认的分支特别篇，但未提供正式 X 期号；保留 `episode_number: null`、`release_type: special`
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

发布者以性格缺点、ADHD、强迫症等个人经验和标签为话题，组织四位参与者进行多人喜剧对谈。

## 章节概览

- `[00:00:00]` 聊聊缺点
- `[00:11:07]` 发际线粉
- `[00:22:26]` ADHD
- `[00:32:49]` 强迫症
- `[01:23:34]` 林简七个性签名
- `[01:34:31]` ADHD爱迟到
- `[02:07:12]` 做公益了不起
- `[02:22:38]` 秃头帅哥

## 核心议题

- 个人缺点与自我描述
- ADHD、强迫症等经验表达
- 心理标签在喜剧对谈中的使用

## 待补充

- [x] 核对 BVID、aid、cid、page、参与者、special 类型与期号缺失状态
- [x] 检查匿名访问可见的平台字幕轨并记录边界
- [x] 获取公开音轨并完成编码、时长、大小和哈希校验
- [x] 生成完整 Qwen3-ASR 机器逐字稿及 adaptive v2 产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 核听多人抢话片段、校对专有名词并核查医学、数字与高影响事实
