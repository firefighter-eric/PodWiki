---
schema_version: 1
kind: episode
id: "sv101:bili-bv1wk3i6nedq"
show_id: sv101
episode_key: bili-bv1wk3i6nedq
episode_number: null
slug: bili-bv1wk3i6nedq-ye-qiyi
release_type: regular
numbering:
  status: not-in-publisher-feed
  checked_at: 2026-08-06
  source: publisher-rss
  note: "硅谷101官方 RSS 未收录与该 Bilibili 视频对应的单集，无法据此核实或推导正式期号"
title: "对话叶奇意：“寻找”月之暗面杨植麟、中国两代AI、十年人才迁徙，与AGI信仰【101视频播客】"
navigation_title: "叶奇意 · AI 人才迁徙、Kimi 投资与 AGI"
catalog_keyword: "Kimi"
published_at: "2026-07-28T15:49:07+08:00"
duration_ms: 4224000
language: zh-CN
participants:
  - id: ye-qiyi
    name: 叶奇意
    aliases:
      - Kiwi
    role: guest
    profile:
      headline: "Ailoha! 创始人"
      affiliations:
        - organization: "Ailoha!"
          title: "创始人"
          status: current
      checked_at: "2026-08-07"
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1wK3i6NEdQ/
    preferred: true
    identifiers:
      bvid: BV1wK3i6NEdQ
      aid: "116996469428261"
      cid: "40369459006"
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
    sha256: b803284537eb8a39d943bb6736313b0ce4d51096ccbca13189e67d44e0b6676d
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
  generated_at: "2026-08-06T16:17:10.251592Z"
  quality:
    source_chunks: 18
    aligned_chunks: 18
    alignment_items: 23293
    sentence_segments: 499
    refined_segments: 499
    rendered_blocks: 144
    rendered_lines: 499
  performance:
    model_load_seconds: 1.355
    transcription_seconds: 162.459
    prompt_tokens: 55234
    generation_tokens: 15592
    prompt_tokens_per_second: 339.993
    generation_tokens_per_second: 95.976
    aligner_load_seconds: 0.223
    alignment_seconds: 30.971
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
    generated_at: "2026-08-06T16:17:10.251592Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/sv101/bili-bv1wk3i6nedq-ye-qiyi/source.m4a
  metadata_path: .cache/media/sv101/bili-bv1wk3i6nedq-ye-qiyi/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-06T15:39:57.419455Z"
  verified_at: "2026-08-06T15:39:57.419455Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 65511030
  duration_ms: 4223744
  sha256: 4f08be3ff8561235d04b56f38f66eddae61e65611788f86435f028f4c1649784
last_verified_at: 2026-08-07
---

# 对话叶奇意：“寻找”月之暗面杨植麟、中国两代 AI、十年人才迁徙，与 AGI 信仰【101视频播客】

> 本页保留 Bilibili 发布者简介和章节形成的概览；另有依据完整 Qwen3-ASR 机器逐字稿整理的总结草稿。关键片段尚未逐段核听，专有名词和外部事实也尚未完成独立核查。

## 单集信息

- 节目：硅谷101（官方 RSS 未收录对应视频，无法核实正式期号）
- 嘉宾：叶奇意（Kiwi），Ailoha! 创始人
- 发布时间：2026-07-28 15:49:07（UTC+8）
- Bilibili 标示时长：01:10:24；本地音轨时长：01:10:23.744
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1wK3i6NEdQ/)
- 编号状态：硅谷101官方 RSS 未收录与该 Bilibili 视频对应的单集；保留 `episode_number: null` 和 `numbering.status: not-in-publisher-feed`，不根据合集位置、输入顺序或发布日期推导正式期号
- 标题边界：Bilibili 当前顶层标题为本页所用标题；单 P 的 `part` 字段仍保留旧标题“对话叶奇意：押注Kimi、中国AI往事、十年传承与迁徙，与Scaling Law【101视频播客】”，不以该内部字段覆盖当前标题
- 字幕边界：匿名 Bilibili player API、yt-dlp 人工字幕列表和自动字幕列表均为空；sidecar 为 `need_login: false`、`tracks: []`。这里只能确认未发现匿名独立字幕轨，不能排除画面硬字幕
- 访问状态：匿名公开音轨可获取；公开元数据为 `pay: 0`、`ugc_pay: 0`、`is_chargeable_season: false`
- 本地来源：AAC、48 kHz、双声道、65,511,030 字节；时长、大小和 SHA-256 已通过独立校验
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的结构化总结草稿](./summary.zh-CN.md)

## 发布者内容概览

发布者以 Kimi K3 发布后在硅谷引发的关注为开端，把月之暗面放在全球 AI 开源争论和竞争的背景下。叶奇意称自己在 AI 行业“打杂了十年”；发布者介绍她经历过上一代“AI 四小龙”的兴起，并在美团龙珠主导推动月之暗面 A1 轮投资。

节目试图把 Kimi 放入更长的中国 AI 发展脉络中观察：杨植麟、唐杰、创新工场 AI 工程院，以及上一轮 AI 创业留下的人才、经验与技术理想，共同构成了延续多年的积累。发布者强调，上一代公司的起伏没有让这些积累消失，而是让它们在大模型时代以新的方式重新汇合。

围绕投资与产业判断，节目讨论月之暗面在尚无产品、胜算并不明朗时为何仍获得领投，Kimi 的发展与两代 AI 创业人才迁徙之间的关系，以及在算力差距短期难以弥合的情况下，中国 AI 公司还可能依靠哪些能力逼近全球前沿。

## 完整章节概览

> 以下时间码和标题完整来自 Bilibili 发布者章节元数据。

- [00:00:00] K3 时刻
- [00:03:18] “寻找杨植麟”
- [00:13:47] 领投 Kimi
- [00:18:09] 投流与探索期
- [00:26:34] K2 到 K3
- [00:32:30] AI 1.0 困局
- [00:38:57] 人才迁徙
- [00:49:10] “中文版 GPT-2”
- [00:56:29] 模型商品化
- [01:05:19] “AI 公民”

## 核心议题

- Kimi K3 与全球 AI 开源竞争的新阶段
- 月之暗面早期融资判断及其不确定性
- 杨植麟与上一代中国 AI 创业、研究网络的连续性
- 两代“AI 四小龙”之间的人才、经验和技术理想迁徙
- 从 K2 到 K3 的产品与模型发展脉络
- AI 1.0 公司的困局及其留下的产业积累
- 投流、产品探索和模型能力之间的关系
- 模型商品化趋势与中国 AI 公司的竞争路径
- “AI 公民”及长期 AGI 信仰

## 待补充

- [x] 核对当前 Bilibili 发布者材料，确认未明确正式期号
- [x] 核对 Bilibili 的 BVID、aid、cid 和 page
- [x] 检查匿名公开字幕轨并记录其证据边界
- [x] 获取独立音轨并完成编码、时长、大小和 SHA-256 校验
- [x] 核对硅谷101官方 RSS，确认未收录对应视频，无法据此核实正式期号
- [x] 使用 Qwen3-ASR 与 ForcedAligner 生成完整机器逐字稿，并选为根目录正式机器稿
- [ ] 核对主持人身份后再补充 participant，当前不依据节目常驻阵容推断
- [ ] 校对专有名词、断句和识别错误
- [x] 基于完整机器逐字稿生成独立总结草稿
- [ ] 核听总结关键片段并核查高影响事实，再决定是否升级为 `reviewed`
