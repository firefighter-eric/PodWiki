---
schema_version: 1
kind: episode
id: "luoyonghao:002"
show_id: luoyonghao
episode_key: "002"
episode_number: 2
slug: 002-he-xiaopeng
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-07
  source: publisher-weibo
  url: https://www.weibo.com/7762107285/Q1BG11Jel
title: "【正片】何小鹏×罗永浩！何小鹏讲述从财富自由奔赴无尽地狱模式的创业故事"
navigation_title: "何小鹏 · 从 UC 到造车、芯片与飞行汽车"
catalog_keyword: "飞行汽车"
published_at: "2025-08-26T12:00:00+08:00"
duration_ms: 10024298
language: zh-CN
participants:
  - id: luo-yonghao
    name: 罗永浩
    role: host
  - id: he-xiaopeng
    name: 何小鹏
    role: guest
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1jTedzREds/
    preferred: true
    identifiers:
      bvid: BV1jTedzREds
      aid: "115088195325847"
      cid: "31942640377"
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
    sha256: fd05b043c445188b206259145dfba480fc8cd1c3cc308f99052220ecd83d0e0d
transcript:
  path: transcript.zh-CN.md
  platform_subtitle_access: no-anonymous-track-login-indicated
  translations: []
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
  generated_at: "2026-08-06T19:02:45.981918Z"
  quality:
    source_chunks: 42
    aligned_chunks: 42
    alignment_items: 45269
    sentence_segments: 1656
    refined_segments: 1653
    rendered_blocks: 333
    rendered_lines: 1653
  performance:
    model_load_seconds: 1.908
    transcription_seconds: 338.01
    prompt_tokens: 131078
    generation_tokens: 30896
    prompt_tokens_per_second: 387.796
    generation_tokens_per_second: 91.406
    aligner_load_seconds: 0.201
    alignment_seconds: 70.492
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
    options:
      language: Chinese
      temperature: 0.0
      max_tokens_per_chunk: 4096
      chunk_duration_seconds: 240.0
      max_sentence_characters: 160
    generated_at: "2026-08-06T19:02:45.981918Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
    quality:
      source_chunks: 42
      aligned_chunks: 42
      alignment_items: 45269
      sentence_segments: 1656
      refined_segments: 1653
      rendered_blocks: 333
      rendered_lines: 1653
    performance:
      model_load_seconds: 1.908
      transcription_seconds: 338.01
      prompt_tokens: 131078
      generation_tokens: 30896
      prompt_tokens_per_second: 387.796
      generation_tokens_per_second: 91.406
      aligner_load_seconds: 0.201
      alignment_seconds: 70.492
local_audio_cache:
  path: .cache/media/luoyonghao/002-he-xiaopeng/source.m4a
  metadata_path: .cache/media/luoyonghao/002-he-xiaopeng/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-06T18:45:23.423378Z"
  verified_at: "2026-08-06T18:45:23.423378Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 159715649
  duration_ms: 10024298
  sha256: a1f2f70400161d7299e9a9aef9e16b0fc2546a6e15871b33044f7f5ee26f180e
last_verified_at: 2026-08-07
---

# 何小鹏 × 罗永浩：从 UC 到造车、芯片与飞行汽车

## 单集信息

- 节目：罗永浩的十字路口（第 2 期）
- 主持人：罗永浩
- 嘉宾：何小鹏，小鹏汽车董事长、UC 优视联合创始人
- 发布时间：2025-08-26 12:00（UTC+8）
- 本地音频时长：02:47:04.298（AAC、48 kHz、双声道）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1jTedzREds/)
- 字幕状态：匿名访问未发现公开字幕轨；播放器提示登录后可能存在字幕
- 本地来源：独立音轨已下载，并通过媒体探测、时长、大小和 SHA-256 校验
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的结构化总结草稿](./summary.zh-CN.md)
- 处理状态：机器逐字稿与总结草稿均已生成，尚未核听或完成人工审核

## 内容概览

何小鹏回顾从创立 UC 浏览器、实现财富自由，到再次进入智能汽车行业的创业路径。他讨论早期创业中的合伙人选择、品牌命名、产品判断和管理经验，也解释为什么在已经获得商业成功后仍选择进入投入更大、周期更长的造车行业。

访谈进一步覆盖自动驾驶、自研芯片、飞行汽车、汽车行业淘汰赛以及 AI 对产品经理和企业组织的影响，并呈现互联网创业方法与传统制造业复杂协作之间的差异。

## 发布者章节概览

- 00:00:00 — 财富自由的三条路径
- 00:13:56 — UC 的成功
- 00:26:20 — 何以“小鹏”
- 00:49:40 — 烧钱的 AI
- 01:03:32 — “淘汰赛”
- 01:17:53 — 计算机系和产品经理
- 01:36:40 — 自研芯片和飞行汽车
- 02:04:25 — “老实”和“暴躁”
- 02:17:18 — 互联网和传统车企
- 02:32:13 — AI 很“可怕”

## 核心议题

- 从 UC 浏览器到小鹏汽车的连续创业经历
- 财富自由之后重新创业的动机与代价
- 智能汽车的产品定位、组织管理与行业淘汰赛
- 自动驾驶、自研芯片和飞行汽车的长期投入
- 互联网团队与传统汽车工业的协作差异
- AI 对汽车产业、产品经理和企业竞争的影响

## 待补充

- [x] 通过发布者官方微博核对正式期号
- [x] 核对 BVID、aid、cid 和 page
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取并验证本地独立音轨及来源 sidecar
- [x] 使用 Qwen3-ASR 与 ForcedAligner 生成机器逐字稿
- [x] 基于完整机器逐字稿形成结构化总结草稿
- [ ] 校对专有名词、数字、断句及主持人与嘉宾的说话人区分
- [ ] 核听关键片段并完成必要事实核查
