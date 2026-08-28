---
schema_version: 1
kind: episode
id: "sv101:250"
show_id: sv101
episode_key: "250"
episode_number: 250
slug: 250-ying-bo
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-28
  source: publisher-rss
  url: https://feeds.fireside.fm/sv101/rss
title: "对话艾博生物CEO英博：“一人一药”，Moderna，AI制药，癌症疫苗的边界与未来【101视频播客】"
navigation_title: "英博 · 个性化mRNA肿瘤疫苗与制造"
catalog_keyword: "mRNA肿瘤疫苗"
published_at: "2026-08-28T13:35:06+08:00"
duration_ms: 4873894
language: zh-CN
participants:
  - id: yushan
    name: Yushan
    aliases:
      - 羽山
    role: host
  - id: ying-bo
    name: 英博
    aliases: []
    role: guest
    profile:
      headline: "艾博生物创始人、董事长兼 CEO"
      bio: "据本期发布者介绍，英博曾在 Moderna 从事 mRNA 相关核心研发，本期从临床、制造、自动化与监管角度讨论个性化 mRNA 肿瘤疫苗。"
      affiliations:
        - organization: 艾博生物
          title: 创始人、董事长兼 CEO
          status: current
        - organization: Moderna
          title: mRNA 研发人员
          status: former
      checked_at: 2026-08-28
sources:
  - platform: website
    kind: episode
    url: https://sv101.fireside.fm/263
    preferred: false
    identifiers:
      page_id: "263"
      episode_number: "250"
      guid: 73a69583-98ee-43d6-a892-3e7c93012dd9
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1aZtc68EzJ/
    preferred: true
    identifiers:
      bvid: BV1aZtc68EzJ
      aid: "117171472570152"
      cid: "41350204551"
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
    sha256: ee7b03db8a0b3c437627fba73f2b6d13d0b0bddf9bf4aeb231aca140e923163a
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
  generated_at: "2026-08-28T06:39:54.439243Z"
  quality:
    source_segments: 2087
    rendered_lines: 2087
    source_duration_ms: 4874000
    first_start_ms: 80
    last_end_ms: 4866160
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
    generated_at: "2026-08-28T06:39:54.439243Z"
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
      source_segments: 2087
      rendered_lines: 2087
      edge_coverage: within-30-seconds
local_audio_cache: null
last_verified_at: 2026-08-28
---

# 对话艾博生物CEO英博：“一人一药”，Moderna，AI制药，癌症疫苗的边界与未来【101视频播客】

> 本页依据官方节目 RSS、Bilibili 元数据与完整 B 站 AI 中文字幕整理；逐字稿和总结尚未人工回听校对。本集直接导入登录态可见的平台字幕，未下载音频或运行本地 ASR。

## 单集信息

- 节目：硅谷101
- 主播：Yushan（羽山）
- 嘉宾：英博；发布者介绍为艾博生物创始人、董事长兼 CEO，曾在 Moderna 从事 mRNA 相关核心研发
- 正式期号：E250
- 发布时间：2026-08-28 13:35:06（北京时间，Bilibili 正片）
- 来源：[Bilibili 正片](https://www.bilibili.com/video/BV1aZtc68EzJ/) · [官方节目页](https://sv101.fireside.fm/263)
- 逐字稿：[Bilibili AI 中文字幕机器稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的中文总结](./summary.zh-CN.md)

## 内容概览

节目从 Moderna 与默沙东个体化 mRNA 肿瘤疫苗的三期积极结果出发，讨论结果真正证明了什么、治疗性疫苗如何与 PD-1 联用，以及“一人一药”从肿瘤取样、新抗原预测到生产放行的完整链条。后半段进一步比较固定抗原与个性化路线，并拆解自动化、成本、AI、监管和规模化部署的现实边界。

## 章节概览

官方章节覆盖 mRNA 癌症疫苗、Moderna 三期结果、个性化制药流程、新抗原选择、全球技术路线、中国机会、自动化设备、AI 研发和监管上市。

## 核心议题

- 三期无复发生存期结果能证明什么，又不能证明什么
- 个性化新抗原疫苗为何需要与 PD-1 联用
- 四至六周的“一人一药”流程如何避免交叉污染并控制成本
- AI、自动化和监管如何共同决定个性化疗法能否规模化

## 待补充

- [x] 核对官方 RSS 的 E250、节目页、BVID、aid、cid、单 P、发布者与公开免费状态
- [x] 保存并导入登录态可见的 Bilibili 中文 AI 字幕原始响应
- [x] 生成 tracked raw/refined、正式逐字稿、总结草稿和双索引
- [ ] 人工回听并校对药物名、公司名、英文术语、数字与说话人归属
- [ ] 独立核查临床结果、上市时间、成本与行业预测等高影响陈述
