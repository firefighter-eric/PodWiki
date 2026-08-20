---
schema_version: 1
kind: episode
id: "sv101:249"
show_id: sv101
episode_key: "249"
episode_number: 249
slug: 249-zhang-hongjiang-huang-dongxu
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-20
  source: publisher-episode-page
  url: https://www.sv101.net/262
title: "Token经济转点：OpenClaw、Hermes到本地自研的Agent进化之路【硅谷101播客】"
navigation_title: "张宏江、黄东旭 · Token经济与Agent进化"
catalog_keyword: "Token经济"
published_at: "2026-08-20T08:00:00+08:00"
duration_ms: 5241000
language: zh-CN
participants:
  - id: hongjun
    name: 泓君
    aliases: []
    role: host
  - id: zhang-hongjiang
    name: 张宏江
    aliases: []
    role: guest
    profile:
      headline: "Llama Ventures 高级技术合伙人、美国国家工程院外籍院士"
      bio: "据本期发布者介绍，张宏江曾任微软亚洲工程院院长、微软亚太研发集团首席技术官和金山软件首席执行官，现参与 AI 投资与产业研究。"
      affiliations:
        - organization: Llama Ventures
          title: 高级技术合伙人
          status: current
        - organization: 北京智源人工智能研究院
          title: 理事长
          status: current
        - organization: 源码资本
          title: 合伙人
          status: current
        - organization: 微软亚太研发集团
          title: 首席技术官
          status: former
        - organization: 金山软件
          title: 首席执行官
          status: former
      checked_at: 2026-08-20
  - id: huang-dongxu
    name: 黄东旭
    aliases: []
    role: guest
    profile:
      headline: "Llama Ventures 合伙人、PingCAP 联合创始人兼 CTO"
      affiliations:
        - organization: Llama Ventures
          title: 合伙人
          status: current
        - organization: PingCAP
          title: 联合创始人兼 CTO
          status: current
      checked_at: 2026-08-20
sources:
  - platform: website
    kind: episode
    url: https://www.sv101.net/262
    preferred: false
    identifiers:
      page_id: "262"
      episode_number: "249"
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1yFbo66E4q/
    preferred: true
    identifiers:
      bvid: BV1yFbo66E4q
      aid: "117124093713367"
      cid: "41078688449"
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
    sha256: 46b9499d52666ad283ac49253e2edbc3f5a8c6d42c2c1f83c4c7261d010b7746
transcript:
  path: transcript.zh-CN.md
  platform_subtitle_access: authenticated-ai-track
  platform_subtitle_languages:
    - zh-CN
  acquisition_method: platform-ai-subtitle
  engine: bilibili-subtitles
  model: bilibili-ai-subtitle-zh
  options:
    source_language: zh
    format: bilibili-ai-subtitle-json
    access_context: authenticated
    max_edge_gap_seconds: 30
  generated_at: "2026-08-20T06:26:17.116515Z"
  quality:
    source_segments: 2343
    rendered_lines: 2343
    source_duration_ms: 5241000
    first_start_ms: 40
    last_end_ms: 5238880
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
    generated_at: "2026-08-20T06:26:17.116515Z"
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
      source_segments: 2343
      rendered_lines: 2343
      edge_coverage: within-30-seconds
local_audio_cache: null
last_verified_at: 2026-08-20
---

# Token经济转点：OpenClaw、Hermes到本地自研的Agent进化之路【硅谷101播客】

> 本页依据官方节目页、Bilibili 元数据与完整 B 站 AI 中文字幕整理；逐字稿和总结尚未人工回听校对。本集直接导入平台字幕，未下载音频或运行本地 ASR。

## 单集信息

- 节目：硅谷101
- 主播：泓君
- 嘉宾：张宏江、黄东旭
- 正式期号：E249
- 发布时间：2026-08-20 08:00（北京时间）
- 来源：[Bilibili 正片](https://www.bilibili.com/video/BV1yFbo66E4q/) · [官方节目页](https://www.sv101.net/262)
- 逐字稿：[Bilibili AI 中文字幕机器稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的中文总结](./summary.zh-CN.md)

## 内容概览

节目从硅谷过去半年的 Token Maxing 热潮切入，讨论 Agent 使用成本从“不计代价追求能力”转向“本地开源模型与前沿云模型分工”的过程，并延伸到 OpenClaw、Hermes、多 Agent 协作、Agent-native 创业和 ToB 基础设施机会。

## 章节概览

官方章节覆盖 Token Maxing 的成本转折、黄东旭的高强度 Agent 实践、OpenClaw 与 Hermes 的产品演进、多 Agent 协作、本地模型经济账、Agent 创业边界和 AGI 判断。

## 核心议题

- Token 消耗应如何与真实产出和 ROI 对齐
- 本地开源模型与前沿云模型如何分工
- Agent 从单体工具走向协作网络会带来哪些工程与组织问题
- 创业团队如何避免被基础模型升级直接吞没

## 待补充

- [x] 核对官方节目页、E249、BVID、aid、cid、单 P、发布者与公开免费状态
- [x] 保存并导入登录态可见的 Bilibili 中文 AI 字幕原始响应
- [x] 生成 tracked raw/refined、正式逐字稿、总结草稿和双索引
- [ ] 人工回听并校对人名、模型名、英文术语、数字和说话人归属
- [ ] 独立核查节目中涉及公司预算、模型性能、收入和行业预测的高影响陈述
