---
schema_version: 1
kind: episode
id: "zhangxiaojun:143"
show_id: zhangxiaojun
episode_key: "143"
episode_number: 143
slug: 143-he-xiaopeng
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-09
  source: publisher-rss
  url: https://www.xiaoyuzhoufm.com/episode/6a170f747460cabdeb56dabb
title: "对何小鹏的第二次访谈：更大赌注、人形机器人Iron诞生、那场意外、技术剧变下CEO、GX和缝合怪"
navigation_title: "何小鹏 · 人形机器人 Iron 与 CEO"
catalog_keyword: "人形机器人"
published_at: "2026-05-28T08:00:00+08:00"
duration_ms: 5172053
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: he-xiaopeng
    name: 何小鹏
    role: guest
sources:
  - platform: xiaoyuzhou
    kind: episode
    title: "143. 对何小鹏的第二次访谈：更大赌注、人形机器人Iron诞生、那场意外、技术剧变下CEO、GX和缝合怪"
    url: https://www.xiaoyuzhoufm.com/episode/6a170f747460cabdeb56dabb
    preferred: false
    identifiers:
      eid: 6a170f747460cabdeb56dabb
      pid: 626b46ea9cbbf0451cf5a962
      media_id: 626b46ea9cbbf0451cf5a962/ljeKstsAfrj-oVTm2bpL92S4nwoc.m4a
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 6a170f747460cabdeb56dabb
  - platform: bilibili
    kind: video
    title: "对何小鹏的第二次访谈：更大赌注、人形机器人Iron诞生、那场意外、技术剧变下CEO、GX和缝合怪"
    url: https://www.bilibili.com/video/BV1d4GU6wEDo/
    preferred: true
    identifiers:
      bvid: BV1d4GU6wEDo
      aid: "116647503334242"
      cid: "38657721264"
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
    sha256: e1b2a122c4d0068e953a8311511a8b26b39f04b4d4ea3cfa892e97d55637e704
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
    planned_chunk_count: 22
    final_leaf_chunk_count: 22
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 90112
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: "2026-08-09T22:53:14.905237Z"
  quality:
    source_chunks: 22
    aligned_chunks: 22
    alignment_items: 24048
    sentence_segments: 805
    refined_segments: 804
    rendered_blocks: 174
    rendered_lines: 804
  performance:
    model_load_seconds: 0.179
    transcription_seconds: 223.09
    prompt_tokens: 67635
    generation_tokens: 15866
    attempt_prompt_tokens: 67635
    attempt_generation_tokens: 15866
    generation_call_count: 22
    prompt_tokens_per_second: 303.173
    generation_tokens_per_second: 71.119
    aligner_load_seconds: 0.28
    alignment_seconds: 35.734
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
    generated_at: "2026-08-09T22:53:14.905237Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/143-he-xiaopeng/source.m4a
  metadata_path: .cache/media/zhangxiaojun/143-he-xiaopeng/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-09T12:35:30.541224Z"
  verified_at: "2026-08-09T12:35:30.541224Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 88784962
  duration_ms: 5172053
  sha256: 0805c7810499a9f4dbfb8ee922167585fd163107c92bb46fb37f97f5bf2c575a
last_verified_at: 2026-08-09
---

# 对何小鹏的第二次访谈：更大赌注、人形机器人 Iron 诞生、那场意外、技术剧变下 CEO、GX 和缝合怪

> 本页保留发布者标题、简介与章节形成的概览，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。正式期号只取自发布者 RSS，不按 Bilibili 标题或导入顺序推断。

## 单集信息

- 节目：张小珺商业访谈录 #143
- 主持人：张小珺
- 嘉宾：何小鹏
- Bilibili 发布时间：2026-05-28 08:00:00（UTC+8）
- Bilibili 视频时长：01:26:13；官方 RSS 音频时长：01:28:21
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/6a170f747460cabdeb56dabb)、[Bilibili 视频](https://www.bilibili.com/video/BV1d4GU6wEDo/)
- 来源状态：公开单 P；匿名状态下平台返回空 tracks 并提示需要登录才能进一步检查，未取得匿名公开字幕轨；未使用 cookies 或登录态，且未绕过访问控制；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 完整性核验：发布者 RSS 将本期明确列为《张小珺商业访谈录》第 143 期，标题、嘉宾与主题和同一发布者账号上传的 Bilibili 单 P 一致；冻结 manifest 将 `BV1d4GU6wEDo` 精确映射到该 RSS 条目。发布者在 Bilibili 简介中称其为对何小鹏的访谈，并明确说明视频播客在视频平台播出，章节从 `00:01:13` 连续延伸至 `01:16:30`，支持其为完整官方视频播客版而非片段或高光。RSS 与本地视频音轨时长相差约 128.947 秒；本集没有专用跨平台声学抽样证据，因此该映射不证明两端逐句相同，也不据此推断具体剪辑差异
- 本地音频：AAC、48 kHz、双声道、88,784,962 字节
- 正式期号：发布者 RSS 标题明确标注 `143.`，GUID 为 `6a170f747460cabdeb56dabb`；Bilibili 标题没有期号，未据其反推编号
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

何小鹏返场讨论小鹏从“智能电动汽车”走向物理 AI 的转型：为什么把旧自动驾驶体系视为软件与 AI 的“缝合怪”，如何在组织规模已经很大时下注新的 foundation model 路线，以及人形机器人 Iron 从四足、双足到通用人形路线的演进。

后半段继续讨论拟人机器人的运动控制、社会接受、量产和商业化难题，并以新车 GX、自动驾驶 L4、软硬件价值分配和产业集中度为例，说明他如何理解汽车、机器人与全球化三条曲线。

## 核心议题

- 数字 AI 工具、物理 AI 基础设施与企业一号位的边界
- 从软件“缝合怪”转向 foundation model 的组织赌注
- 人形机器人 Iron 的三阶段研发、运动控制与社会形态
- 机器人量产、商业化、胜率与不同细分路线
- GX、自动驾驶 L4、软硬件价值和汽车产业集中度

## 待补充

- [x] 通过发布者 RSS 标题、GUID、enclosure、简介与章节核对正式第 143 期
- [x] 核对 Bilibili BVID、aid、cid、page、发布者账号与单 P 完整播客映射
- [x] 检查匿名状态的平台字幕轨，且未使用登录态或绕过访问控制
- [x] 获取公开音轨并完成编码、时长、大小、媒体哈希与重新解码 PCM 承诺核验
- [x] 生成完整 Qwen3-ASR 机器逐字稿及 adaptive v2 产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 人工核听开场冷开、主持人口播、多人切换，以及最后一条对齐在 `01:26:03.863` 结束、距离 `01:26:12.053` 音频端点 8.190 秒的收尾；校正“未尽之约/微博财经”“小朋友”“周汤”“O L”“SOPIC”“LC”“中汽”“飞擎”“GS”等明显或疑似近音误识别
- [ ] 核查人名、公司、模型、产品和技术专名，尤其张小珺、何小鹏、于凯、李斌，XPeng、小鹏集团、Iron、GX、G9、VA/VIA、Waymo、Google、Tesla、DeepSeek、Qwen、豆包、Claude Code、H100、Level 4/5、MPC、Tier 1/2、SOP/SOD、PDCA、地平线等
- [ ] 回听并查证年份、组织调整、团队与招聘人数、研发和数据成本、H100 数量、AI 投入比例、软件价值比例、机器人身高与关节数、量产节点、冗余数量、L4 时间表、销量涨幅、研发费用和 2030 年车企数量等；产品能力、路线优劣、公司胜率和行业终局均保持为嘉宾陈述或录制时判断
