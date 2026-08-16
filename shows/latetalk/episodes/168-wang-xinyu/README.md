---
schema_version: 1
kind: episode
id: "latetalk:168"
show_id: latetalk
episode_key: "168"
episode_number: 168
slug: 168-wang-xinyu
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-16
  source: publisher-website
  note: "晚点聊官方节目页与 RSS 标题明确标为 168 期"
title: "对话王新宇：美团龙珠怎么投科技【晚点聊 LateTalk】"
navigation_title: "王新宇 · 美团龙珠的科技投资方法"
catalog_keyword: "美团龙珠"
published_at: "2026-06-11T07:30:00+08:00"
duration_ms: 7574421
language: zh-CN
participants:
  - id: wang-xinyu
    name: 王新宇
    aliases: []
    role: guest
    profile:
      headline: "美团龙珠合伙人"
      affiliations:
        - organization: "美团龙珠"
          title: "合伙人"
          status: current
      checked_at: 2026-08-16
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1vZEo6vEx1/
    preferred: true
    identifiers:
      bvid: BV1vZEo6vEx1
      aid: "116726758970901"
      cid: "39018760359"
      page: 1
  - platform: website
    kind: episode
    url: https://podcast.latepost.com/168
    identifiers:
      episode_number: "168"
      rss_guid: 567e4022-c39c-4dc5-b16f-125525d1288e
workflow:
  metadata: verified
  summary: draft
  transcript: machine
summary_basis:
  - publisher-description
  - complete-machine-transcript
summary:
  path: summary.zh-CN.md
  language: zh-CN
  source_transcript:
    path: transcript.zh-CN.md
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    selection_status: selected
    sha256: 85a7b1018fa7edfde23b51982b947e048f306f6b28951dc75004988ca732a6cb
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
    planned_chunk_count: 32
    effective_total_token_budget: 131072
    max_sentence_characters: 160
  generated_at: "2026-08-16T04:37:17.390963Z"
  quality:
    source_chunks: 32
    aligned_chunks: 32
    alignment_items: 39158
    sentence_segments: 1116
    refined_segments: 1115
    rendered_blocks: 258
    rendered_lines: 1115
  performance:
    model_load_seconds: 0.203
    transcription_seconds: 276.413
    prompt_tokens: 99049
    generation_tokens: 26422
    prompt_tokens_per_second: 358.337
    generation_tokens_per_second: 95.589
    aligner_load_seconds: 0.143
    alignment_seconds: 42.667
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
    generated_at: "2026-08-16T04:37:17.390963Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/latetalk/168-wang-xinyu/source.m4a
  metadata_path: .cache/media/latetalk/168-wang-xinyu/source.metadata.json
  git_ignored: true
  extractor: BiliBili
  acquired_at: "2026-08-16T04:13:02.154793Z"
  verified_at: "2026-08-16T04:13:02.154793Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 104997813
  duration_ms: 7574421
  sha256: 48bffbe090316068e18471ddd7ebe784b39debcd3cf5796146c7aac19fed18aa
last_verified_at: 2026-08-16
---

# 对话王新宇：美团龙珠怎么投科技【晚点聊 LateTalk】

> 本页保留发布者简介形成的内容提纲，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 节目：晚点聊 LateTalk #168
- 嘉宾：王新宇，美团龙珠合伙人（身份来自发布者简介）
- 发布时间：2026-06-11 07:30:00（UTC+8）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1vZEo6vEx1/) · [官方节目页](https://podcast.latepost.com/168)
- 字幕状态：未发现匿名公开字幕轨；平台提示字幕查询需要登录，未使用登录态
- 本地音轨：02:06:14.421（AAC、48 kHz、双声道）
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

发布者简介围绕美团龙珠的科技投资展开，涉及具身智能投入、宇树和月之暗面等案例，以及王新宇对科技投资规模、阶段和长期布局的判断。

## 章节概览

Bilibili 匿名元数据未提供平台章节。

## 核心议题

- 美团龙珠的科技投资方法
- 具身智能的投入与泡沫判断
- 宇树和月之暗面的投资案例
- 长周期科技投资的组织与决策

## 待补充

- [x] 核对 BVID、aid、cid、page、正式期号与嘉宾
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取公开音轨并完成媒体校验
- [x] 生成 Qwen3-ASR 机器逐字稿及可复现产物链
- [x] 基于完整逐字稿形成独立总结草稿
- [ ] 回听并校对专有名词与高影响事实
