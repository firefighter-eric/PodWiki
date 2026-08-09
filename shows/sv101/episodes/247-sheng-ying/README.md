---
schema_version: 1
kind: episode
id: "sv101:247"
show_id: sv101
episode_key: "247"
episode_number: 247
slug: 247-sheng-ying
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-06
  source: publisher-episode-page
  url: https://sv101.fireside.fm/260
title: "对话盛颖：xAI，Infra的浪漫，SGLang，开源，平权与“甄嬛传”【101视频播客】"
navigation_title: "盛颖 · SGLang、Infra 产品观与开源"
catalog_keyword: "SGLang"
published_at: "2026-08-05T12:30:00+08:00"
duration_ms: 6461504
language: zh-CN
participants:
  - id: chen-qian
    name: 陈茜
    role: host
  - id: sheng-ying
    name: 盛颖
    role: guest
    profile:
      headline: "RadixArk 联合创始人兼 CEO、SGLang 发起人"
      affiliations:
        - organization: "RadixArk"
          title: "联合创始人兼 CEO、SGLang 发起人"
          status: current
        - organization: "xAI"
          title: "推理团队负责人"
          status: former
      checked_at: "2026-08-07"
sources:
  - platform: website
    kind: episode
    url: https://sv101.fireside.fm/260
    preferred: false
    identifiers:
      page_id: "260"
      episode_number: "247"
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1GaM968E6T/
    preferred: true
    identifiers:
      bvid: BV1GaM968E6T
      aid: "117030577576158"
      cid: "40555644556"
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
    sha256: 420d014947e058a5e62384fb5f6215623f1254868ef6189132b8d61d806733bc
transcript:
  path: transcript.zh-CN.md
  platform_subtitle_access: no-anonymous-public-track
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
  generated_at: "2026-08-06T16:00:03.066203Z"
  quality:
    source_chunks: 27
    aligned_chunks: 27
    alignment_items: 36851
    sentence_segments: 1111
    refined_segments: 1111
    rendered_blocks: 219
    rendered_lines: 1111
  performance:
    model_load_seconds: 2.292
    transcription_seconds: 257.323
    prompt_tokens: 84488
    generation_tokens: 24636
    prompt_tokens_per_second: 328.339
    generation_tokens_per_second: 95.741
    aligner_load_seconds: 0.214
    alignment_seconds: 50.623
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
    generated_at: "2026-08-06T16:00:03.066203Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/sv101/247-sheng-ying/source.m4a
  metadata_path: .cache/media/sv101/247-sheng-ying/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-06T15:39:52.232988Z"
  verified_at: "2026-08-06T15:42:16.803500Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 95660420
  duration_ms: 6461504
  sha256: eea2aa7f2a6a574d4523c6877d7445042683e4768ab8863f602d64168bbc0a8e
last_verified_at: 2026-08-07
---

# 对话盛颖：xAI，Infra的浪漫，SGLang，开源，平权与“甄嬛传”【101视频播客】

> 本页保留硅谷101官方单集页、发布者简介和发布者章节形成的概览；另有依据完整 Qwen3-ASR 机器逐字稿整理的总结草稿。关键片段尚未逐段核听，专有名词和外部事实也尚未完成独立核查。

## 单集信息

- 节目：硅谷101 #247
- 主持人：陈茜，硅谷101 联合创始人
- 嘉宾：盛颖，RadixArk 联合创始人兼 CEO、xAI 前推理团队负责人、开源推理引擎 SGLang 发起人
- 官方播客发布时间：2026-08-05 12:30:00（UTC+8；Fireside 页面原始时间为 2026-08-04 21:30:00 UTC-7）
- Bilibili 发布时间：2026-08-03 16:20:00（UTC+8）
- 官方播客音频时长：01:46:26
- Bilibili 标示时长：01:47:42；本地 Bilibili 音轨时长：01:47:41.504
- 来源：[硅谷101 官方 E247 单集页](https://sv101.fireside.fm/260)、[Bilibili 视频](https://www.bilibili.com/video/BV1GaM968E6T/)
- 编号状态：官方单集页标题明确标注 `E247`，正式期号已核实
- 字幕边界：匿名 Bilibili player API、yt-dlp 人工字幕列表和自动字幕列表均为空；sidecar 的字幕能力字段为 `need_login: true`。官方单集页同时明确称视频版带有精校字幕及术语注解，因此这里只能确认“未暴露匿名独立字幕轨”，不能据此否定视频内字幕，也未使用 cookies 或登录态
- 访问状态：匿名公开音轨可获取；公开元数据为 `pay: 0`、`ugc_pay: 0`、`is_chargeable_season: false`
- 本地来源：AAC、48 kHz、双声道、95,660,420 字节；时长、大小和 SHA-256 已通过独立校验
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的结构化总结草稿](./summary.zh-CN.md)

## 发布者内容概览

发布者介绍称，盛颖曾负责 xAI 推理团队，是开源推理引擎 SGLang 的发起人，也是 RadixArk 联合创始人兼 CEO。节目以她对 AI Infra 的理解为主线：基础设施不只是支撑产品的后台能力，也可以是需要结构、美感和工程创造力的产品本身。

访谈从盛颖对数学世界的向往谈起，回顾她从哥伦比亚大学到斯坦福、从形式化验证转向 AI Infra 的路径，以及连续发表论文之外的迷茫、停滞、低谷和重新寻找方向。发布者把这种经历概括为：只有真正被问题吸引，她才会进入高度专注并把事情做到极致的状态。

职业与技术部分覆盖 Google 实习、Databricks、Two Sigma、xAI、SGLang 和 RadixArk。发布者重点描述了她在早期 xAI 同时获得支持与自由、参与生产级推理系统的经历，也解释了 SGLang 社区快速扩张后，仅靠开发者业余维护难以持续，最终推动她离开 xAI 创办 RadixArk 的选择。

节目最后把开源生态、LMSYS、平等与平权、个人价值观和强力 AI 的未来联系起来。发布者强调，盛颖关心的并非抽象的“making impact”，而是她认为正确的事情最终是否真正发生，以及人类如何构建一个能与强力 AI 共存而不落败的未来。

## 完整章节概览

> 以下时间码和标题完整来自硅谷101官方 E247 单集页的“你将听到”。

- [00:02:16] 违约金、纽约与数学之美：“世界与我无关”
- [00:16:06] 顶刊、低谷期与甄嬛传：“世界又与我有关了”
- [00:26:01] 谷歌实习：最早的“AI for code”
- [00:31:54] Databricks：人生导师 Ion Stoica 与“making impact”价值观
- [00:34:37] xAI：拥有“support”和“freedom”的美好 v1.0 时代
- [00:44:07] RadixArk：“两个月也等不了”
- [00:48:07] Two Sigma：“有组织的公司”应该有的样子
- [00:51:10] SGLang：“AI Infra 是浪漫的”
- [01:15:29] SandHill Road 的套路与规则
- [01:19:33] “养大我”的开源生态
- [01:27:03] LMSYS：平等、平权，以及“她赢了，不需要被解释”
- [01:37:42] “世间的美好是存在的”

## 核心议题

- 数学之美、个人兴趣与研究方向选择之间的关系
- 从形式化验证转向 AI Infra 的学习和职业路径
- 顶刊、低谷期和重新出发背后的个人经验
- Databricks、Two Sigma 与早期 xAI 的组织和工程环境
- SGLang 从学术项目走向生产级开源推理引擎的过程
- 开源社区扩张、长期维护与创办 RadixArk 的现实选择
- AI Infra 的产品观、工程美感与模型服务能力
- LMSYS、开源生态中的平等与平权
- 个人价值观、技术影响和与强力 AI 共存的未来

## 待补充

- [x] 通过官方单集页核实 E247、主持人与嘉宾身份
- [x] 核对 Bilibili 的 BVID、aid、cid 和 page
- [x] 检查匿名公开字幕轨，并记录官方“精校字幕”表述与 API 暴露边界
- [x] 获取独立音轨并完成编码、时长、大小和 SHA-256 校验
- [x] 使用 Qwen3-ASR 与 ForcedAligner 生成完整机器逐字稿，并选为根目录正式机器稿
- [ ] 校对专有名词、断句和识别错误
- [ ] 增加主持人与嘉宾的说话人区分
- [x] 基于完整机器逐字稿生成独立总结草稿
- [ ] 核听总结关键片段并核查高影响事实，再决定是否升级为 `reviewed`
