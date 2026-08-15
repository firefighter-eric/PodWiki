---
schema_version: 1
kind: episode
id: "zhangxiaojun:132"
show_id: zhangxiaojun
episode_key: "132"
episode_number: 132
slug: 132-gao-jiyang
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-09
  source: publisher-rss
  url: https://www.xiaoyuzhoufm.com/episode/698ebb0b66e2c30377510cf6
title: "对星海图高继扬的3小时访谈：鲶鱼、曾国藩、机器人、Waymo与Momenta的两面、一只狼与许华哲的离开"
navigation_title: "高继扬 · 具身智能与创业工程"
catalog_keyword: "星海图"
published_at: "2026-02-13T17:11:18+08:00"
duration_ms: 11053802
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: gao-jiyang
    name: 高继扬
    role: guest
sources:
  - platform: xiaoyuzhou
    kind: episode
    title: "132. 对星海图创始人高继扬的3小时访谈：鲶鱼、曾国藩、Waymo与Momenta的两面、一只狼与许华哲的离开"
    url: https://www.xiaoyuzhoufm.com/episode/698ebb0b66e2c30377510cf6
    preferred: false
    identifiers:
      eid: 698ebb0b66e2c30377510cf6
      pid: 626b46ea9cbbf0451cf5a962
      media_id: 626b46ea9cbbf0451cf5a962/lplNqS9I0z2b64zp9zF2h6EkhXjr.m4a
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 698ebb0b66e2c30377510cf6
  - platform: bilibili
    kind: video
    title: "对星海图高继扬的3小时访谈：鲶鱼、曾国藩、机器人、Waymo与Momenta的两面、一只狼与许华哲的离开"
    url: https://www.bilibili.com/video/BV1arcjzpE1B/
    preferred: true
    identifiers:
      bvid: BV1arcjzpE1B
      aid: "116062532141170"
      cid: "36029333967"
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
    sha256: 301bc9ea0d51095d6e6d5cc90d084e57b15d1b6dac59660929e119b8f1512748
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
    planned_chunk_count: 47
    final_leaf_chunk_count: 47
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 192512
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: "2026-08-09T22:26:29.656010Z"
  quality:
    source_chunks: 47
    aligned_chunks: 47
    alignment_items: 56467
    sentence_segments: 1586
    refined_segments: 1586
    rendered_blocks: 382
    rendered_lines: 1586
  performance:
    model_load_seconds: 0.175
    transcription_seconds: 491.244
    prompt_tokens: 144553
    generation_tokens: 38854
    attempt_prompt_tokens: 144553
    attempt_generation_tokens: 38854
    generation_call_count: 47
    prompt_tokens_per_second: 294.259
    generation_tokens_per_second: 79.093
    aligner_load_seconds: 0.167
    alignment_seconds: 74.419
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
    generated_at: "2026-08-09T22:26:29.656010Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/132-gao-jiyang/source.m4a
  metadata_path: .cache/media/zhangxiaojun/132-gao-jiyang/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-09T12:34:31.027727Z"
  verified_at: "2026-08-09T12:34:31.027727Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 160341236
  duration_ms: 11053802
  sha256: dc43df08f191a85d419db480c63ae3e7b8b1d14e8582262bd4bdf86b95f526a0
last_verified_at: 2026-08-09
---

# 对星海图高继扬的 3 小时访谈：鲶鱼、曾国藩、机器人、Waymo 与 Momenta 的两面、一只狼与许华哲的离开

> 本页保留 Bilibili 原标题与发布者 RSS 正式标题，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。正式期号只取自发布者 RSS，不按 Bilibili 标题或导入顺序推断。

## 单集信息

- 节目：张小珺商业访谈录 #132
- 主持人：张小珺
- 嘉宾：高继扬
- Bilibili 发布时间：2026-02-13 17:11:18（UTC+8）
- Bilibili 视频时长：03:04:14；官方 RSS 音频时长：03:04:52
- RSS 正式标题：132. 对星海图创始人高继扬的3小时访谈：鲶鱼、曾国藩、Waymo与Momenta的两面、一只狼与许华哲的离开
- Bilibili 原标题：对星海图高继扬的3小时访谈：鲶鱼、曾国藩、机器人、Waymo与Momenta的两面、一只狼与许华哲的离开
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/698ebb0b66e2c30377510cf6)、[Bilibili 视频](https://www.bilibili.com/video/BV1arcjzpE1B/)
- 来源状态：公开单 P；匿名状态下平台返回 `need_login: true` 与空 tracks，未取得匿名可用字幕轨；未登录且未绕过访问控制；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 完整性核验：发布者 RSS 将本期明确列为《张小珺商业访谈录》第 132 期，标题、嘉宾、主题和章节顺序与同一发布者账号上传的 Bilibili 单 P 正片一致；冻结 manifest 将 `BV1arcjzpE1B` 精确映射到该 RSS 条目。Bilibili 章节覆盖整段上传，所选音轨从冷开场、节目片头和嘉宾介绍连续到发布端点，支持其为完整官方视频播客版而非片段或高光。RSS 与视频时长相差约 38.198 秒，因此该证据不证明两端逐句一致
- 本地音频：AAC、48 kHz、双声道、160,341,236 字节
- 正式期号：发布者 RSS 标题明确标注 `132.`，GUID 为 `698ebb0b66e2c30377510cf6`；Bilibili 标题没有期号，未据其反推编号
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

高继扬从物理竞赛、AI 研究、Waymo 与 Momenta 的经历讲到创办星海图，围绕 AI-native 系统、整机与物理数据闭环、真实数据配方、机器人大脑、应用场景与组织取舍，解释为什么具身智能既需要长期理想，也必须逐阶段把头伸进供应链、客户与交付的“土里”。

## 核心议题

- 从归纳总结、曾国藩到工程师的“拆解加测量”
- Waymo 与 Momenta 的技术路线、组织文化和客户距离
- 整机、供应链、物理数据闭环与开发者市场
- 真实数据、Data Recipe、VLM/VLA 双系统与生产力场景
- 务实创新、合伙人机制、许华哲离开与组织价值观
- 长期理想、阶段优先级、客户价值与“狼”的生存状态

## 待补充

- [x] 通过发布者 RSS 标题、GUID、enclosure、简介与章节核对正式第 132 期
- [x] 核对 Bilibili BVID、aid、cid、page、发布者账号与单 P 完整性证据
- [x] 检查匿名访问可见的平台字幕轨，且未绕过登录控制
- [x] 获取公开音轨并完成编码、时长、大小、媒体哈希与重新解码 PCM 承诺核验
- [x] 生成完整 Qwen3-ASR 机器逐字稿及 adaptive v2 产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 人工核听 `02:57:51` 附近疑似重复段、时间戳冻结，以及 `03:04:10` 的突兀收尾；校正“高继阳”“杨志林”“蒙曼塔”“WeMo”“巨深/巨帧智能”“派零”“五米”“G7 Plus”等明显或疑似近音误识别，并核对说话人切换
- [ ] 核查人名、公司、模型、产品与机构专名，尤其高继扬、张小珺、杨植麟、汤晓鸥、曹旭东、赵航、许华哲、杨泽一及早期团队/投资人姓名，以及 SenseTime、Waymo、Momenta、VectorNet、VLA、VLM、Diffusion Policy、Data Recipe、R1、G0/G0 Plus 等
- [ ] 回听并查证教育与任职年份、论文与团队贡献、期权和融资金额、估值、客户/员工/车型数量、开源数据时长、真实数据成本与训练成本比例、硬件寿命、传播周期、投资方和产品能力等数字与高影响事实；公司内部离职原因、组织评价、行业路线胜负和未来出货目标均保持为嘉宾陈述或录制时判断
