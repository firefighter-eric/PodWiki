---
schema_version: 1
kind: episode
id: "luoyonghao:001"
show_id: luoyonghao
episode_key: "001"
episode_number: 1
slug: 001-li-xiang
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-09
  source: publisher-rss-description
  url: https://feed.xyzfm.space/wmnkvmrpwuww
  note: "发布者在第 27 期简介中回指李想为节目开播的第一期嘉宾"
title: "【正片】李想×罗永浩！四小时马拉松访谈！李想首度公开讲述25年创业之路"
navigation_title: "李想 · 二十五年创业之路"
catalog_keyword: "创业"
published_at: "2025-08-19T12:00:00+08:00"
duration_ms: 14235840
language: zh-CN
participants:
  - id: luo-yonghao
    name: "罗永浩"
    aliases: []
    role: host
  - id: li-xiang
    name: "李想"
    aliases: []
    role: guest
sources:
  - platform: bilibili
    kind: video
    title: "【正片】李想×罗永浩！四小时马拉松访谈！李想首度公开讲述25年创业之路"
    url: https://www.bilibili.com/video/BV1FwY4zkEef/
    preferred: true
    identifiers:
      bvid: BV1FwY4zkEef
      aid: "115049943269792"
      cid: "31789090706"
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
    sha256: 356b980fe363b5291f055e85285452ce2506e191f3f447396c9d7323ca694d40
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
  generated_at: "2026-08-09T12:55:30.944102Z"
  quality:
    source_chunks: 60
    aligned_chunks: 60
    alignment_items: 80823
    sentence_segments: 2660
    refined_segments: 2659
    rendered_blocks: 478
    rendered_lines: 2659
  performance:
    model_load_seconds: 1.719
    transcription_seconds: 635.853
    prompt_tokens: 186152
    generation_tokens: 56874
    prompt_tokens_per_second: 292.759
    generation_tokens_per_second: 89.445
    aligner_load_seconds: 0.218
    alignment_seconds: 95.208
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
    generated_at: "2026-08-09T12:55:30.944102Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/luoyonghao/001-li-xiang/source.m4a
  metadata_path: .cache/media/luoyonghao/001-li-xiang/source.metadata.json
  git_ignored: true
  recovered_at: "2026-08-09T12:31:50.830243Z"
  verified_at: "2026-08-09T12:31:50.830243Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 196999893
  duration_ms: 14235840
  sha256: 5be653e9e8231f29765d97b1b6a3cd0fd9367b59dffb241f002503ac4dc31d62
last_verified_at: 2026-08-09
---

# 【正片】李想×罗永浩！四小时马拉松访谈！李想首度公开讲述25年创业之路

> 本页保留发布者材料形成的内容提纲，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 节目：罗永浩的十字路口（第 1 期）
- 主持人：罗永浩
- 嘉宾：李想
- 发布时间：2025-08-19 12:00:00（UTC+8）
- Bilibili 视频时长：03:57:16
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1FwY4zkEef/)
- 来源状态：公开单 P；匿名访问未发现公开字幕轨；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 本地音频：AAC、48 kHz、双声道、196,999,893 字节
- 编号状态：发布者材料明确为第 1 期
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

发布者以李想二十五年的创业经历为主线，回顾早期创业、造车过程中的关键转折与逆境，以及他对长期创业的判断。

## 章节概览

- `[00:00:00]` 上大学还是创业 李想不一样的成长
- `[00:48:21]` 24岁身价过亿 还要寻找下一个风口
- `[00:55:34]` 李想也非常喜欢 宫本茂 和 乔布斯
- `[01:12:05]` 从汽车之家到理想 选对团队是关键
- `[01:36:37]` 融资困境遇贵人 李想谈及不禁落泪
- `[01:59:08]` 理想ONE 500 万内最佳家用 SUV
- `[02:18:16]` 李想：面对泼脏水 不愿同流合污
- `[03:07:09]` 李想创业二十年至暗时刻 堪比TVB
- `[03:25:38]` 罗永浩分享公众前 真情流露时刻
- `[03:43:27]` 人工智能发展五个阶段及未来趋势

## 核心议题

- 二十五年创业经历与关键转折
- 理想汽车的创业过程与挑战
- 企业家面对逆境与长期选择

## 待补充

- [x] 核对 BVID、aid、cid、page、正式期号与参与者
- [x] 检查匿名访问可见的平台字幕轨并记录边界
- [x] 获取公开音轨并完成编码、时长、大小和哈希校验
- [x] 生成完整 Qwen3-ASR 机器逐字稿及 v2 产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 核听关键片段、校对专有名词并核查高影响事实
