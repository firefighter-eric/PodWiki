---
schema_version: 1
kind: episode
id: "zhangxiaojun:bili-bv1nb3u6teru"
show_id: zhangxiaojun
episode_key: bili-bv1nb3u6teru
episode_number: null
slug: bili-bv1nb3u6teru-liao-heng
release_type: special
numbering:
  status: not-in-publisher-feed
  checked_at: 2026-08-05
  source: publisher-rss
  note: "截至核验日期未出现在发布者 RSS/feed 中，且无 RSS GUID；不推导正式期号"
title: "对华为半导体首席科学家廖恒的5小时访谈：一部昇腾史、18层宝塔与全球芯片恢弘30年史诗| B站 x WAIC AI会客厅"
published_at: "2026-07-25T21:19:38+08:00"
duration_ms: 16672000
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: liao-heng
    name: 廖恒
    role: guest
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1nB3u6tERu/
    preferred: true
    identifiers:
      bvid: BV1nB3u6tERu
      aid: "116980698843032"
      cid: "40282095854"
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
  platform_subtitle_access: no-anonymous-track
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
  path: .cache/media/zhangxiaojun/bili-bv1nb3u6teru-liao-heng/source.m4a
  metadata_path: .cache/media/zhangxiaojun/bili-bv1nb3u6teru-liao-heng/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-05T12:06:25.508889Z"
  verified_at: "2026-08-05T12:06:25.508889Z"
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 201246502
  duration_ms: 16671403
  sha256: e6c8982621c5587ca867e0417bb695b4658b59b6b7d9473613c2f3e48bcb3b7b
last_verified_at: 2026-08-05
---

# 对华为半导体首席科学家廖恒的访谈：昇腾史与全球芯片产业

> 当前内容根据 Bilibili 发布者简介和章节整理，是结构化概览，不是基于完整逐字稿完成的总结。

## 单集信息

- 节目：张小珺Jùn｜商业访谈录特别访谈（无正式期号）
- 主持人：张小珺
- 嘉宾：廖恒，华为 Fellow、半导体首席科学家
- 发布时间：2026-07-25 21:19:38（UTC+8）
- Bilibili 标示时长：04:37:52
- 本地 Bilibili 音轨：04:37:51.403（AAC、44.1 kHz、双声道）
- 来源：[Bilibili 视频](https://www.bilibili.com/video/BV1nB3u6tERu/)
- 编号状态：截至 2026-08-05，该内容未出现在发布者 RSS/feed 中，也没有 RSS GUID；因此保留 `episode_number: null`，不根据相邻单集推导为 #147
- 合作标记：Bilibili 公开元数据的 `is_cooperation` 为 `1`
- 字幕状态：匿名访问未发现独立公开字幕轨；处理过程中未使用 cookies 或登录态
- 本地来源：独立音轨已下载，并通过媒体探测、时长、大小和 SHA-256 校验

## 内容概览

发布者介绍称，本期嘉宾廖恒是华为 Fellow、半导体首席科学家。访谈从华为在 2020 年之后经历的挑战谈起，回顾昇腾芯片从低谷逐步走出的工程历程，并把这段经历放入中国半导体产业选择与发展的背景中观察。

节目也从更长时间尺度梳理全球半导体与芯片产业的历史、规律和整体格局，讨论摩尔定律、芯片产业的分层结构、人才与算力，以及 AI 与芯片的技术前沿。发布者将完整版定位为 Bilibili 与世界人工智能大会（WAIC）合作内容；页面同时说明节目不构成投资建议。

## 章节概览

> 以下时间码和标题来自 Bilibili 发布者简介。

- 00:02:08 — 芯片史：垄断之下漫长的日落
- 01:17:32 — 摩尔定律
- 01:31:45 — 18 层宝塔
- 01:58:18 — 华为昇腾史与中国道路
- 03:21:29 — 人才与算力
- 03:39:23 — AI 与芯片的科技前沿
- 04:16:45 — 工程师故事

## 核心议题

- 全球半导体产业的历史、竞争格局与长期规律
- 摩尔定律及芯片产业的多层结构
- 华为昇腾芯片在 2020 年之后的工程与产业历程
- 中国半导体产业的技术路线与现实选择
- 人才、算力和组织能力之间的关系
- AI 与芯片协同演进的技术前沿
- 工程师视角下的个人经历与产业变迁

## 待补充

- [x] 核对发布者 RSS/feed，确认截至 2026-08-05 没有正式期号或 RSS GUID
- [x] 核对 Bilibili 视频的 BVID、aid、cid 和 page
- [x] 检查匿名访问可见的平台字幕轨
- [x] 获取独立音轨并完成编码、时长、大小和哈希校验
- [ ] 运行机器转写并生成逐字稿
- [ ] 校对专有名词、断句和识别错误
- [ ] 增加主持人与嘉宾的说话人区分
- [ ] 基于完整内容完成事实核查和正式总结
