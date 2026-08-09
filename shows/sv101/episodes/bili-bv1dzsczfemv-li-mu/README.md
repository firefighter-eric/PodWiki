---
schema_version: 1
kind: episode
id: "sv101:bili-bv1dzsczfemv"
show_id: sv101
episode_key: bili-bv1dzsczfemv
episode_number: null
slug: bili-bv1dzsczfemv-li-mu
release_type: special
numbering:
  status: not-in-publisher-feed
  checked_at: 2026-08-06
  source: publisher-rss
  note: "硅谷101官方 RSS 未收录与该 Bilibili 视频对应的年度科技大会演讲，无法据此核实或推导正式期号"
title: "语音智能体商业落地的教训、经验与实践｜李沐硅谷101年度线下大会演讲（全英）"
navigation_title: "李沐 · 语音智能体商业落地与系统门槛"
catalog_keyword: "语音智能体"
published_at: "2025-10-27T12:33:28+08:00"
duration_ms: 1640938
language: en
participants:
  - id: li-mu
    name: 李沐
    role: guest
    profile:
      headline: "Boson AI 联合创始人、前亚马逊高级首席科学家"
      affiliations:
        - organization: "Boson AI"
          title: "联合创始人"
          status: current
        - organization: "亚马逊"
          title: "高级首席科学家"
          status: former
      checked_at: "2026-08-07"
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1dZsCzfEMV/
    preferred: true
    identifiers:
      bvid: BV1dZsCzfEMV
      aid: "115444241470918"
      cid: "33430966033"
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
    path: transcript.en.md
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    selection_status: selected
    sha256: 028c4cd0ecfc9981d19adc2ad9915e8379afdf7a90e33f5bb9e81e1f928f81cd
transcript:
  path: transcript.en.md
  translations:
    - language: zh-CN
      path: transcript.zh-CN.md
      source_language: en
      source_path: transcript.en.md
      alignment: segment
      status: machine
      generated_at: "2026-08-06T16:59:01Z"
      source_sha256: 028c4cd0ecfc9981d19adc2ad9915e8379afdf7a90e33f5bb9e81e1f928f81cd
      sha256: 640afbd8a93b11b0506276658c4589bbe361f348a0319d8c385f6730cd0bed21
  platform_subtitle_access: no-anonymous-track-login-indicated
  platform_subtitle_languages: []
  automatic_caption_languages: []
  acquisition_method: audio-asr
  asr_script: scripts/transcribe_qwen3_asr.py
  engine: mlx-audio
  model: mlx-community/Qwen3-ASR-1.7B-8bit
  aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
  options:
    language: English
    temperature: 0.0
    max_tokens_per_chunk: 4096
    chunk_duration_seconds: 240.0
    max_sentence_characters: 160
  generated_at: "2026-08-06T16:21:15.463887Z"
  quality:
    source_chunks: 7
    aligned_chunks: 7
    alignment_items: 4484
    sentence_segments: 340
    refined_segments: 340
    rendered_blocks: 111
    rendered_lines: 340
  performance:
    model_load_seconds: 1.3
    transcription_seconds: 56.566
    prompt_tokens: 21460
    generation_tokens: 5372
    prompt_tokens_per_second: 379.399
    generation_tokens_per_second: 94.974
    aligner_load_seconds: 1.239
    alignment_seconds: 8.13
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
    path: asr/qwen3-asr/transcript.en.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
  renderer: scripts/render_asr_transcript.py
asr_runs:
  - id: qwen3-asr-1.7b-8bit
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    generated_at: "2026-08-06T16:21:15.463887Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.en.md
local_audio_cache:
  path: .cache/media/sv101/bili-bv1dzsczfemv-li-mu/source.m4a
  metadata_path: .cache/media/sv101/bili-bv1dzsczfemv-li-mu/source.metadata.json
  git_ignored: true
  extractor: BiliBili
  acquired_at: "2026-08-06T15:40:02.855542Z"
  verified_at: "2026-08-06T15:40:02.855542Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 21267375
  duration_ms: 1640938
  sha256: 17d13406e75657d3a141a56f5707d5fd98110c97b91b52e6d125fe5aae5c0b5a
last_verified_at: 2026-08-07
---

# 语音智能体商业落地的教训、经验与实践｜李沐硅谷101年度线下大会演讲（全英）

> 本页保留 Bilibili 发布者简介与平台章节，并已基于完整英文 Qwen3-ASR 机器逐字稿形成中文总结草稿；关键片段尚未核听，英文识别、数字、产品细节与外部事实也尚未完成人工校对或独立核查。

## 单集信息

- 节目：硅谷101年度科技大会特别内容（无正式期号）
- 演讲嘉宾：李沐，发布者介绍为 Boson AI 联合创始人、前亚马逊高级首席科学家
- 发布时间：2025-10-27 12:33:28（UTC+8）
- 内容语言：英文；发布者说明大会演讲以中文字幕呈现
- Bilibili 标示时长：00:27:21
- 本地 Bilibili 音轨：00:27:20.938（AAC、48 kHz、双声道）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1dZsCzfEMV/)
- 编号状态：截至 2026-08-06，硅谷101官方 RSS 未收录与该 Bilibili 视频对应的年度科技大会演讲；保留 `episode_number: null`，不根据大会合集位置或发布日期推导正式期号
- 字幕状态：匿名访问未发现独立公开字幕轨；平台字幕检查提示登录后可能存在字幕。发布者所说的中文字幕不能据此判定为独立字幕轨或画面硬字幕
- 来源权利提示：Bilibili 公开元数据记录 `rights.no_reprint=1`；本页仅记录来源与研究材料，不转载原媒体。`download=1` 只是平台元数据字段，不视为项目取得转载或其他额外授权
- 本地来源：音轨已获取，并通过独立 ffprobe、文件大小和 SHA-256 校验
- 英文逐字稿：[Qwen3-ASR 机器初稿](./transcript.en.md)
- 中文逐字稿：[逐段对齐的机器翻译](./transcript.zh-CN.md)（未人工审核）
- 中文总结：[基于完整英文机器稿的总结草稿](./summary.zh-CN.md)
- 处理状态：英文机器逐字稿、逐段对齐的中文机器翻译与中文总结草稿均已生成；音频尚未核听，英文识别和中文翻译均未完成人工审核

## 内容概览

发布者简介将演讲定位为对语音智能体从技术突破走向商业落地的经验总结。简介提到两个实践场景：在开放世界游戏中让智能体承担游戏设计与 NPC 角色，以及在保险行业中让 AI 电话销售通过行业要求并完成真实业务流程。

发布者称，语音智能体虽然已经进入可以投入使用的阶段，但从单点落地走向规模化仍有大量问题需要探索。演讲据此讨论语音智能体的关键能力、不同系统架构、行业约束，以及团队从实践中形成的反思。页面说明该演讲来自 2025 年 10 月 5 日举办的 Alignment 2025 年度科技大会。基于完整英文机器稿的中文梳理、原文定位与事实边界见[总结草稿](./summary.zh-CN.md)。

## 章节概览

> 以下时间范围和标题来自 Bilibili 发布者章节。

- 00:00:00–00:01:39 — 语音智能体的关键
- 00:01:39–00:07:13 — AI扮演游戏中的NPC
- 00:07:13–00:13:10 — 游戏Voice Agent落地案例
- 00:13:10–00:17:44 — 保险行业三重挑战
- 00:17:44–00:23:31 — 四大语音智能体架构
- 00:23:31–00:25:02 — AI电话销售智能体的反思
- 00:25:02–00:27:21 — 商业落地仍处于“Day One”

## 核心议题

- 语音智能体走向商业落地所需的关键能力
- 游戏中的生成式角色、NPC 与动态体验设计
- 保险电话销售场景中的业务流程和行业约束
- 不同语音智能体系统架构的取舍
- 从可用原型到规模化部署之间的工程与商业差距
- 实践案例暴露的失败经验、反思与后续探索方向

## 待补充

- [x] 核对 Bilibili 视频的规范 URL、BVID、aid、cid 和 page
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取并独立验证本地音轨、来源 sidecar、大小和 SHA-256
- [x] 记录发布者 `rights.no_reprint=1` 的来源权利提示
- [x] 核对发布者官方 RSS，确认未收录对应视频，无法推导正式期号
- [x] 生成完整英文 Qwen3-ASR 机器逐字稿并保留原始、对齐、精炼与渲染产物
- [x] 按英文机器稿的 340 个 segment 逐行生成中文机器翻译，并保持时间戳一一对齐
- [x] 基于完整英文机器逐字稿撰写中文总结草稿并核验时间码存在性
- [ ] 校对英文识别、断句、产品名与技术术语
- [ ] 逐段人工审核中文机器翻译，不以当前机器翻译替代英文源稿
- [ ] 核听关键片段并核查高影响外部事实
