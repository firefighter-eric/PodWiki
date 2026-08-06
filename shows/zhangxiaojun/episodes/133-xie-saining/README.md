---
schema_version: 1
kind: episode
id: "zhangxiaojun:133"
show_id: zhangxiaojun
episode_key: "133"
episode_number: 133
slug: 133-xie-saining
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-06
  source: publisher-rss
title: "对谢赛宁的7小时马拉松访谈：世界模型、逃出硅谷与 AMI Labs"
navigation_title: "谢赛宁 - 表征学习、世界模型与 AMI Labs"
published_at: "2026-03-16T12:01:08+08:00"
duration_ms: 24329000
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: xie-saining
    name: 谢赛宁
    role: guest
sources:
  - platform: rss
    kind: feed-item
    url: https://www.xiaoyuzhoufm.com/episode/69b77577f8b8079bfa8eb837
    preferred: false
    identifiers:
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 69b77577f8b8079bfa8eb837
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1tew5zVEDf/
    preferred: true
    identifiers:
      bvid: BV1tew5zVEDf
      aid: "116236243435948"
      cid: "36779196929"
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
    sha256: fb27b1e6aee9d5e60fc8dc4d62467454db949605d90467458deeab78a83c5c68
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
  generated_at: "2026-08-06T08:58:12.978388Z"
  quality:
    source_chunks: 102
    aligned_chunks: 102
    alignment_items: 111821
    sentence_segments: 3241
    refined_segments: 3238
    rendered_blocks: 834
    rendered_lines: 3238
  performance:
    model_load_seconds: 2.192
    transcription_seconds: 910.751
    prompt_tokens: 317453
    generation_tokens: 77410
    prompt_tokens_per_second: 348.567
    generation_tokens_per_second: 84.997
    aligner_load_seconds: 0.217
    alignment_seconds: 187.035
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
    generated_at: "2026-08-06T08:58:12.978388Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/133-xie-saining/source.m4a
  metadata_path: .cache/media/zhangxiaojun/133-xie-saining/source.metadata.json
  git_ignored: true
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 385253978
  duration_ms: 24277504
  sha256: 07dcdf771b7df779266839b6671bb477176df739945fb6548cc5f4119343c4f7
  acquired_at: "2026-08-06T06:55:04.853052Z"
  verified_at: "2026-08-06T06:55:04.853052Z"
last_verified_at: 2026-08-06
---

# 对谢赛宁的 7 小时马拉松访谈：世界模型、逃出硅谷与 AMI Labs

> 本页保留发布者简介与章节形成的概览；另有依据完整机器逐字稿整理的总结草稿，尚未完成关键片段核听和独立事实核查。

## 单集信息

- 节目：张小珺商业访谈录（第 133 期）
- 主持人：张小珺
- 嘉宾：谢赛宁，AMI Labs 联合创始人兼首席科学官、纽约大学教授
- 发布时间：2026-03-16 12:01（UTC+8）
- 官方 RSS 时长：06:45:29；Bilibili 视频时长：06:44:38
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/69b77577f8b8079bfa8eb837)、[Bilibili 视频](https://www.bilibili.com/video/BV1tew5zVEDf/)
- 字幕状态：匿名访问未发现公开字幕轨；播放器提示登录后可能存在字幕
- 本地音频：AAC、48 kHz、双声道、385,253,978 字节；sidecar 已记录 SHA-256 和来源身份
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[核心观点与 5 分钟版](./summary.zh-CN.md)

## 内容概览

这场马拉松式访谈从谢赛宁的学术流浪、视觉研究与 DiT 展开，延伸到世界模型、语言模型的局限、AMI Labs 创业，以及杨立昆、李飞飞、何恺明等研究者对其思想路径的影响。

## 章节概览

发布者提供了从个人经历、视觉研究、世界模型到创业和研究共同体的长篇章节；正式机器逐字稿与总结已按当前 ASR 时间码补充。

## 核心议题

- 视觉研究、DiT 与世界模型
- 对 LLM、Scaling Law 与“苦涩教训”的批评
- 从学术机构到 AMI Labs 的创业选择
- AI 研究共同体中的师友、传承与价值观

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
