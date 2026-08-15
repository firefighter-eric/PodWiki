---
schema_version: 1
kind: episode
id: "luoyonghao:020"
show_id: luoyonghao
episode_key: "020"
episode_number: 20
slug: 020-bu-kai-wanxiao
release_type: special
numbering:
  status: verified
  checked_at: 2026-08-09
  source: publisher-rss-description
  url: https://feed.xyzfm.space/wmnkvmrpwuww
  note: "发布者明确称其为第二十期（乱斗篇）及《不开玩笑》联名款现场"
title: "【正片】“不开玩笑” × 罗永浩的十字路口！折腾未必会赢，但不折腾一定会后悔"
navigation_title: "史炎、宋方金、孙书恒、刘仁铖 · 折腾与再战"
catalog_keyword: "折腾"
published_at: "2026-02-28T12:00:43+08:00"
duration_ms: 8636650
language: zh-CN
participants:
  - id: luo-yonghao
    name: "罗永浩"
    aliases: []
    role: host
  - id: shi-yan
    name: "史炎"
    aliases: []
    role: participant
  - id: song-fangjin
    name: "宋方金"
    aliases: []
    role: participant
  - id: sun-shuheng
    name: "孙书恒"
    aliases: []
    role: participant
  - id: liu-rencheng
    name: "刘仁铖"
    aliases: []
    role: participant
sources:
  - platform: bilibili
    kind: video
    title: "【正片】“不开玩笑” × 罗永浩的十字路口！折腾未必会赢，但不折腾一定会后悔"
    url: https://www.bilibili.com/video/BV1kFA8z1E5s/
    preferred: true
    identifiers:
      bvid: BV1kFA8z1E5s
      aid: "116145814310675"
      cid: "36340173463"
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
    sha256: b68cc9c10796c203f2bffb1ed4f1e62ada4f240f09a2bbce3643081a18ed8a74
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
    planned_chunk_count: 36
    final_leaf_chunk_count: 45
    adaptive_split_count: 9
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 184320
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: "2026-08-09T18:50:53.387238Z"
  quality:
    source_chunks: 45
    aligned_chunks: 45
    alignment_items: 39460
    sentence_segments: 2098
    refined_segments: 2070
    rendered_blocks: 303
    rendered_lines: 2070
  performance:
    model_load_seconds: 0.168
    transcription_seconds: 675.455
    prompt_tokens: 113096
    generation_tokens: 30210
    attempt_prompt_tokens: 129125
    attempt_generation_tokens: 67074
    generation_call_count: 54
    prompt_tokens_per_second: 167.437
    generation_tokens_per_second: 44.725
    aligner_load_seconds: 0.129
    alignment_seconds: 45.248
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
    generated_at: "2026-08-09T18:50:53.387238Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/luoyonghao/020-bu-kai-wanxiao/source.m4a
  metadata_path: .cache/media/luoyonghao/020-bu-kai-wanxiao/source.metadata.json
  git_ignored: true
  recovered_at: "2026-08-09T12:32:11.531084Z"
  verified_at: "2026-08-09T12:32:11.531084Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 129842876
  duration_ms: 8636650
  sha256: 4baaaaa3c9d17425c3350d01a2f381dc3650fe97764055feec6e63278e1dcb70
last_verified_at: 2026-08-09
---

# 【正片】“不开玩笑” × 罗永浩的十字路口！折腾未必会赢，但不折腾一定会后悔

> 本页保留发布者材料形成的内容提纲，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 节目：罗永浩的十字路口（第 20 期）
- 主持人：罗永浩
- 参与者：史炎、宋方金、孙书恒、刘仁铖
- 发布时间：2026-02-28 12:00:43（UTC+8）
- Bilibili 视频时长：02:23:57
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1kFA8z1E5s/)
- 来源状态：公开单 P；匿名访问未发现公开字幕轨；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 本地音频：AAC、48 kHz、双声道、129,842,876 字节
- 编号状态：发布者材料明确为第 20 期
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

发布者将本集定义为《十字路口》第二十期乱斗篇及《不开玩笑》联名现场，围绕折腾、创业、失败与再战进行多人对谈。

## 章节概览

- `[00:00:00]` 聊聊折腾
- `[00:16:51]` “王哥卤味”
- `[00:26:32]` 最大单一遗憾
- `[00:40:46]` 心路历程
- `[01:00:47]` 不会卸妆
- `[01:20:41]` 网暴经历
- `[01:30:40]` 重启生活
- `[01:54:40]` 折腾电影
- `[02:04:33]` 继续折腾

## 核心议题

- 折腾、创业与再次出发
- 失败、天赋与个人缺陷
- 多人喜剧对谈与相互辩论

## 待补充

- [x] 核对 BVID、aid、cid、page、正式期号与参与者
- [x] 检查匿名访问可见的平台字幕轨并记录边界
- [x] 获取公开音轨并完成编码、时长、大小和哈希校验
- [x] 生成完整 Qwen3-ASR 机器逐字稿及 v2 产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 核听关键片段、校对专有名词并核查高影响事实
