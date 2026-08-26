---
schema_version: 1
kind: episode
id: "zhangxiaojun:152"
show_id: zhangxiaojun
episode_key: "152"
episode_number: 152
slug: 152-sun-yutao
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-27
  source: publisher-rss
  url: https://www.xiaoyuzhoufm.com/episode/6a8eadd61352af56ff3c6017
title: "领读Kimi K3技术报告：从架构创新聊起，注意力美学、多教师蒸馏和开源MoE"
navigation_title: "孙宇涛 · Kimi K3 架构、训练与基础设施"
catalog_keyword: "Kimi K3"
published_at: "2026-08-26T17:40:17+08:00"
duration_ms: 7459675
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: sun-yutao
    name: 孙宇涛
    role: guest
    profile:
      headline: "清华大学计算机系博士候选人、上海创智学院璞锐学者"
      bio: "据发布者介绍与本期自述，孙宇涛主要研究大模型架构与预训练，重点关注推理效率，以及模型架构与基础设施的协同设计。"
      affiliations:
        - organization: "上海创智学院"
          title: "璞锐学者"
          status: current
      education:
        - institution: "清华大学"
          credential: "博士候选人"
          field: "计算机"
      checked_at: "2026-08-27"
sources:
  - platform: xiaoyuzhou
    kind: episode
    url: https://www.xiaoyuzhoufm.com/episode/6a8eadd61352af56ff3c6017
    preferred: false
    identifiers:
      eid: 6a8eadd61352af56ff3c6017
      pid: 626b46ea9cbbf0451cf5a962
      media_id: 626b46ea9cbbf0451cf5a962/lrVnGxoafcZ7vzH8HywULkwNb6n6.m4a
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 6a8eadd61352af56ff3c6017
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1KZ8X6uEPL/
    preferred: true
    identifiers:
      bvid: BV1KZ8X6uEPL
      aid: "117161104247436"
      cid: "41286961556"
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
    engine: bilibili-subtitles
    model: bilibili-ai-subtitle-zh
    selection_status: selected
    sha256: 10f92f3e94fa035b66dbd455848b264bfee44bd1697b8a03892f6350aaf94f5c
transcript:
  path: transcript.zh-CN.md
  platform_subtitle_access: authenticated-ai-track
  platform_subtitle_languages:
    - zh-CN
  automatic_caption_languages: []
  acquisition_method: platform-ai-subtitle
  engine: bilibili-subtitles
  model: bilibili-ai-subtitle-zh
  options:
    source_language: zh
    format: bilibili-ai-subtitle-json
    access_context: authenticated
    max_edge_gap_seconds: 30
  generated_at: "2026-08-26T17:51:10.826595Z"
  quality:
    source_segments: 3253
    rendered_lines: 3253
    source_duration_ms: 7460000
    first_start_ms: 3640
    last_end_ms: 7455740
  translations: []
asr_artifacts:
  raw:
    path: asr/bilibili-subtitles/raw.json
    git_ignored: false
    format: podwiki-bilibili-subtitle-raw-v1
  refined:
    path: asr/bilibili-subtitles/refined.json
    git_ignored: false
    format: podwiki-bilibili-subtitle-refined-v1
  transcript:
    path: asr/bilibili-subtitles/transcript.zh-CN.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
  renderer: scripts/import_bilibili_subtitles.py
asr_runs:
  - id: bilibili-subtitles
    selection_status: selected
    engine: bilibili-subtitles
    model: bilibili-ai-subtitle-zh
    generated_at: "2026-08-26T17:51:10.826595Z"
    artifacts:
      raw: asr/bilibili-subtitles/raw.json
      refined: asr/bilibili-subtitles/refined.json
      transcript: asr/bilibili-subtitles/transcript.zh-CN.md
    options:
      source_language: zh
      format: bilibili-ai-subtitle-json
      access_context: authenticated
      max_edge_gap_seconds: 30
    quality:
      source_segments: 3253
      rendered_lines: 3253
      edge_coverage: within-30-seconds
local_audio_cache: null
last_verified_at: 2026-08-27
---

# 领读 Kimi K3 技术报告：架构、训练与基础设施

> 本页依据发布者 RSS、Bilibili 正片与完整 B 站 AI 中文字幕整理；逐字稿和总结尚未人工回听校对。本集直接导入平台字幕，未下载音频或运行本地 ASR。

## 单集信息

- 节目：张小珺商业访谈录 #152
- 主持人：张小珺
- 嘉宾：孙宇涛，清华大学计算机系博士候选人、上海创智学院璞锐学者
- 发布时间：2026-08-26 17:40:17（北京时间，Bilibili）
- 官方 RSS 发布时间：2026-08-26 17:33:46（北京时间）
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/6a8eadd61352af56ff3c6017)、[Bilibili 正片](https://www.bilibili.com/video/BV1KZ8X6uEPL/)
- 时长：Bilibili 02:04:20；官方 RSS 02:04:19
- 逐字稿：[Bilibili AI 中文字幕机器稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的中文总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与总结草稿已生成，等待人工核听

## 内容概览

张小珺与孙宇涛把 Kimi K3 技术报告当作一张路线图，从线性注意力、Gated MLA、Attention Residuals、LatentMoE、Muon 和 Quantile Balancing，讲到预训练、长上下文、量化、多教师 on-policy 蒸馏，以及训练和推理基础设施。讨论的主线不是孤立罗列技巧，而是解释架构选择如何与稳定性、通信、显存和推理效率共同设计。

## 发布者章节概览

> 发布者只为前三个入口提供精确时间码；其余层级来自官方 RSS 的内容提纲，不据列表顺序推导时间。

- 00:02:00 — 孙宇涛自我介绍、研究经历与架构兴趣
- 00:16:05 — 从 Kimi K3 论文出发，说明讲解框架与研究脉络
- 00:19:02 — 开始领读论文
  - Model Architecture：线性注意力、Gated MLA、Attention Residuals、Stable LatentMoE、SiTU-GLU、Muon、Quantile Balancing、Native Vision
  - Pre-Training：Scaling Law、长上下文扩展
  - Post-Training：训练流水线、强化学习、多教师 on-policy 蒸馏、部署感知训练与 draft model
  - Infrastructure：KDA kernel、分布式训练、专家并行、显存优化、多模态、RL 与推理

## 核心议题

- Kimi Delta Attention 的研究脉络、细粒度衰减与 kernel 约束
- Gated MLA、Attention Residuals 与训练稳定性
- LatentMoE 如何同时改变模型架构、通信量和 overlap 策略
- Muon、激活异常值与 Quantile Balancing
- WSD、RNoPE、QAT 与多教师 on-policy 蒸馏的取舍
- 长上下文训练、专家并行、CPU offload、多模态和 prefix cache 的基础设施设计
- 技术进步、团队协作与模型规模之间的关系

## 待补充

- [x] 通过官方 RSS 核对播客身份、正式期号、嘉宾、标题、提纲与时长
- [x] 核对 BVID、aid、cid、单 P、发布者、日期、时长和公开免费状态
- [x] 使用登录态 Chrome 确认并保存 Bilibili 中文 AI 字幕原始响应
- [x] 生成 tracked raw/refined、正式逐字稿和总结草稿
- [ ] 人工回听并校对人名、论文名、模型名、英文术语、数字和说话人归属
- [ ] 对照 Kimi K3 技术报告与引用论文复核技术细节和归因
