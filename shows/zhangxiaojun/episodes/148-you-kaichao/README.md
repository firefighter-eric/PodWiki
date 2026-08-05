---
schema_version: 1
kind: episode
id: "zhangxiaojun:148"
show_id: zhangxiaojun
episode_key: "148"
episode_number: 148
slug: 148-you-kaichao
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-05
  source: publisher-rss
title: "148. 对游凯超3小时访谈：开源Infra、和模型Co-design 、“如果vLLM失败，我们会后悔一辈子”"
published_at: "2026-07-28T08:00:00+08:00"
duration_ms: 10826000
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: you-kaichao
    name: 游凯超
    role: guest
sources:
  - platform: rss
    kind: feed-item
    url: https://www.xiaoyuzhoufm.com/episode/6a66ed17a3fec224d5a3f744
    preferred: false
    identifiers:
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 6a66ed17a3fec224d5a3f744
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV18Qg96YE1W/
    preferred: true
    identifiers:
      bvid: BV18Qg96YE1W
      aid: "116988315699992"
      cid: "40309098797"
      page: 1
workflow:
  metadata: verified
  summary: outline
  transcript: source-acquired
summary_basis:
  - publisher-description
  - publisher-chapters
transcript:
  path: transcript.zh-CN.md
  platform_subtitle_access: not-exposed-as-public-track
asr_artifacts:
  raw:
    path: asr/raw.json
    git_ignored: false
    format: engine-native-json
  refined:
    path: asr/refined.json
    git_ignored: false
    format: podwiki-refined-asr-json-v1
  renderer: scripts/render_asr_transcript.py
local_audio_cache:
  path: .cache/media/zhangxiaojun/148-you-kaichao/source.m4a
  metadata_path: .cache/media/zhangxiaojun/148-you-kaichao/source.metadata.json
  git_ignored: true
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 164063328
  duration_ms: 10748821
  sha256: b3b2e1c16cb04f8433530ed5928e6287da85b4a73b0a57f20876b451e5504f29
  acquired_at: "2026-08-05T12:00:46.159856Z"
  verified_at: "2026-08-05T12:00:46.159856Z"
last_verified_at: 2026-08-05
---

# 148. 对游凯超 3 小时访谈：开源 Infra、模型 Co-design 与 vLLM

> 当前内容根据发布者 RSS 与 Bilibili 简介及章节整理，是结构化概览，不是基于完整逐字稿完成的总结。

## 单集信息

- 节目：张小珺Jùn｜商业访谈录 #148
- 主持人：张小珺
- 嘉宾：游凯超，Inferact 联合创始人兼首席科学家
- 发布时间：2026-07-28 08:00（UTC+8）
- 官方 RSS 音频时长：03:00:26
- Bilibili 视频及本地音频时长：02:59:09；比 RSS 版本短约 1 分 17 秒
- RSS GUID：`6a66ed17a3fec224d5a3f744`
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/6a66ed17a3fec224d5a3f744)、[Bilibili 视频](https://www.bilibili.com/video/BV18Qg96YE1W/)
- 字幕状态：匿名访问未发现独立公开字幕轨；播放器元数据提示字幕能力需要登录，但未证明登录后存在字幕
- 本地音频：AAC、48 kHz、双声道、164,063,328 字节；sidecar 已记录 SHA-256 和来源身份

## 内容概览

发布者介绍称，游凯超是 Inferact 联合创始人兼首席科学家。Inferact 由伯克利校园开源项目 vLLM 演化而来，维护者在约三年里将一篇算法论文发展为开源社区，再进一步建立公司。

本期从游凯超由算法研究转向机器学习系统的经历谈起，回顾 vLLM 的诞生、社区维护者围绕开源项目所作的选择，以及社区走向商业组织后面临的治理与运营问题。技术部分讨论模型结构、AI Infra 与 Harness Engineering 的联合设计，并从 Token 和电力两个角度观察基础设施演进，最后延伸到技术预测。

发布者简介还提到 Inferact 在 2026 年初获得 1.5 亿美元种子轮融资；该信息目前仅按发布者表述记录，尚未在本单集处理中独立事实核查。

## 章节概览

> 以下时间码来自发布者 RSS 与 Bilibili 简介，两个来源给出的章节一致。

- 00:02:18 — 从算法到机器学习系统
- 00:37:56 — 开源项目 vLLM 的诞生
- 01:07:25 — “如果 vLLM 失败了，我们会后悔一辈子”
- 01:20:11 — “仁慈的独裁者”
- 01:37:16 — 从社区到创业
- 01:52:56 — 模型与 Infra 的 Co-design
- 02:15:10 — Token VS 电力
- 02:35:41 — 技术预测

## 核心议题

- 从算法研究转向机器学习系统与 AI Infra
- vLLM 从论文、校园项目到开源社区的演进
- 开源维护者的长期投入、治理选择与社区责任
- 社区项目商业化之后的组织与运营问题
- 模型、Infra 与 Harness Engineering 的联合设计
- Token 供给、电力约束与基础设施技术预测

## 待补充

- [x] 通过发布者 RSS GUID 核对官方期号
- [x] 核对 Bilibili 视频的 aid、cid 和 page
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取并验证本地独立音轨及来源 sidecar
- [ ] 运行机器转写并生成逐字稿
- [ ] 校对专有名词、断句和识别错误
- [ ] 增加主持人与嘉宾的说话人区分
- [ ] 基于完整内容完成事实核查和正式总结
