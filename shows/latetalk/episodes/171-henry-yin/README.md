---
schema_version: 1
kind: episode
id: "latetalk:171"
show_id: latetalk
episode_key: "171"
episode_number: 171
slug: 171-henry-yin
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-07
  source: publisher-website
  note: "晚点聊官网与官方 RSS 明确标为 171 期"
title: "AI 季报 26Q2：从 coding 到 RSI，强者愈强的未来？【晚点聊LateTalk】"
navigation_title: "Henry Yin · AI 季报、Coding 与 RSI"
catalog_keyword: "AI 季报"
published_at: "2026-07-22T10:08:13+08:00"
duration_ms: 5983000
language: zh-CN
participants:
  - id: cheng-manqi
    name: 程曼祺
    role: host
    aliases:
      - 曼祺
  - id: henry-yin
    name: Henry Yin
    role: guest
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1Mhgz6QEHA/
    preferred: true
    identifiers:
      bvid: BV1Mhgz6QEHA
      aid: "116961153523086"
      cid: "40178683792"
      page: 1
  - platform: website
    kind: episode
    url: https://podcast.latepost.com/171
    identifiers:
      episode_number: "171"
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
    sha256: 58723349d3147b7cc41b0ab84d3f41d08b5fe5f63b3bab44db70ab8c7a28fa93
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
  generated_at: "2026-08-07T10:00:11.093579Z"
  quality:
    source_chunks: 25
    aligned_chunks: 25
    alignment_items: 32987
    sentence_segments: 792
    refined_segments: 792
    rendered_blocks: 207
    rendered_lines: 792
  performance:
    model_load_seconds: 1.707
    transcription_seconds: 277.34
    prompt_tokens: 78229
    generation_tokens: 22229
    prompt_tokens_per_second: 282.072
    generation_tokens_per_second: 80.152
    aligner_load_seconds: 0.233
    alignment_seconds: 54.426
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
    generated_at: "2026-08-07T10:00:11.093579Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/latetalk/171-henry-yin/source.m4a
  metadata_path: .cache/media/latetalk/171-henry-yin/source.metadata.json
  git_ignored: true
  extractor: BiliBili
  acquired_at: "2026-08-07T09:39:46.369007Z"
  verified_at: "2026-08-07T09:39:46.369007Z"
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 72549956
  duration_ms: 5982714
  sha256: d90401a964cece0ea4052b37334d68d1118b729fbbb7e1ba896990b37d7779a6
last_verified_at: 2026-08-07
---

# AI 季报 26Q2：从 coding 到 RSI，强者愈强的未来？【晚点聊LateTalk】

> 本页保留发布者简介形成的内容提纲，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 节目：晚点聊 LateTalk #171
- 主持人：程曼祺
- 嘉宾：Henry Yin，MoE Capital 创始合伙人
- Bilibili 发布时间：2026-07-22 10:08:13（UTC+8）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1Mhgz6QEHA/) · [官方节目页](https://podcast.latepost.com/171)
- 字幕状态：未发现匿名公开字幕轨；平台提示字幕查询需要登录，未使用 cookies 或登录态
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

发布者简介称，本期按“推进智能前沿”和“智能扩散”两条线复盘 2026 年第二季度，覆盖 OpenAI 与 Anthropic 的竞争、Coding Agent、递归自我改进、物理 AI、企业模型与交互创新。节目在录制后存在信息时滞，相关市场份额和公司动态尚未独立核查。

## 章节概览

官方节目页按 OpenAI 对 Anthropic、RSI、物理 AI、智能扩散和重点公司提供时间线；最终总结将以完整正式逐字稿中的实际时间码为准。

## 核心议题

- Coding Agent 与模型公司的竞争格局
- RSI 的定义、技术路径和创业机会
- 物理 AI 与 Robotics 的行业动向
- 模型能力向企业与新交互形态的扩散

## 待补充

- [x] 核对 BVID、aid、cid、page、正式期号与参与者
- [x] 检查匿名访问可见的平台字幕轨并记录边界
- [x] 获取公开音轨并完成编码、时长、大小和哈希校验
- [x] 生成 Qwen3-ASR 机器逐字稿及完整 lineage
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 核听关键片段、校对专有名词并核查高影响事实
