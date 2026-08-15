---
schema_version: 1
kind: episode
id: "zhangxiaojun:137"
show_id: zhangxiaojun
episode_key: "137"
episode_number: 137
slug: 137-hong-letong
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-09
  source: publisher-rss
  url: https://www.xiaoyuzhoufm.com/episode/69e4e6951d989496e7fecc7b
title: "对洪乐潼的4小时访谈：AI for Math、把数学变成Lean、数学天书中的证明、直觉、被创造的与被发现的"
navigation_title: "洪乐潼 · AI for Math 与数学直觉"
catalog_keyword: "AI for Math"
published_at: "2026-04-20T11:00:00+08:00"
duration_ms: 15790506
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: hong-letong
    name: 洪乐潼
    aliases:
      - Carina
    role: guest
sources:
  - platform: xiaoyuzhou
    kind: episode
    title: "137. 对洪乐潼的4小时访谈：AI for Math、把数学变成Lean、数学天书中的证明、直觉、被创造与被发现的"
    url: https://www.xiaoyuzhoufm.com/episode/69e4e6951d989496e7fecc7b
    preferred: false
    identifiers:
      eid: 69e4e6951d989496e7fecc7b
      pid: 626b46ea9cbbf0451cf5a962
      media_id: 626b46ea9cbbf0451cf5a962/lha_FAiWxTGet0QMbcOSts3cb5Vb.m4a
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 69e4e6951d989496e7fecc7b
  - platform: bilibili
    kind: video
    title: "对洪乐潼的4小时访谈：AI for Math、把数学变成Lean、数学天书中的证明、直觉、被创造的与被发现的"
    url: https://www.bilibili.com/video/BV13BdfBoELd/
    preferred: true
    identifiers:
      bvid: BV13BdfBoELd
      aid: "116431815443051"
      cid: "37639884303"
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
    sha256: e2004fdfeb87330af3d69e296aff07fcab3a7655e9fbda68951462106d635393
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
    planned_chunk_count: 66
    final_leaf_chunk_count: 66
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 270336
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: "2026-08-09T22:48:48.437422Z"
  quality:
    source_chunks: 66
    aligned_chunks: 66
    alignment_items: 78818
    sentence_segments: 1733
    refined_segments: 1733
    rendered_blocks: 554
    rendered_lines: 1733
  performance:
    model_load_seconds: 0.173
    transcription_seconds: 732.041
    prompt_tokens: 206478
    generation_tokens: 53085
    attempt_prompt_tokens: 206478
    attempt_generation_tokens: 53085
    generation_call_count: 66
    prompt_tokens_per_second: 282.058
    generation_tokens_per_second: 72.516
    aligner_load_seconds: 0.146
    alignment_seconds: 112.092
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
    generated_at: "2026-08-09T22:48:48.437422Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/137-hong-letong/source.m4a
  metadata_path: .cache/media/zhangxiaojun/137-hong-letong/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-09T12:35:22.693364Z"
  verified_at: "2026-08-09T12:35:22.693364Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 226262539
  duration_ms: 15790506
  sha256: 0194046257fc2c6fb784637f00e4b015d113b51a34d2dd35b35df5437a37f816
last_verified_at: 2026-08-09
---

# 对洪乐潼的 4 小时访谈：AI for Math、把数学变成 Lean、数学天书中的证明、直觉、被创造的与被发现的

> 本页保留 Bilibili 原标题与发布者 RSS 正式标题，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。正式期号只取自发布者 RSS，不按 Bilibili 标题或导入顺序推断。

## 单集信息

- 节目：张小珺商业访谈录 #137
- 主持人：张小珺
- 嘉宾：洪乐潼（Carina）
- Bilibili 发布时间：2026-04-20 11:00:00（UTC+8）
- Bilibili 视频时长：04:23:11；官方 RSS 音频时长：04:24:17
- RSS 正式标题：137. 对洪乐潼的4小时访谈：AI for Math、把数学变成Lean、数学天书中的证明、直觉、被创造与被发现的
- Bilibili 原标题：对洪乐潼的4小时访谈：AI for Math、把数学变成Lean、数学天书中的证明、直觉、被创造的与被发现的
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/69e4e6951d989496e7fecc7b)、[Bilibili 视频](https://www.bilibili.com/video/BV13BdfBoELd/)
- 来源状态：公开单 P；匿名状态下平台返回 `need_login: true` 与空 tracks，未取得匿名可用字幕轨；未登录且未绕过访问控制；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 播客与完整性核验：发布者 RSS 频道将《张小珺商业访谈录》明确描述为深度访谈播客，并将本期正式列为第 137 期；同一发布者 Bilibili 账号在简介中明确称其内容为“视频播客”，标题、嘉宾、主题及 14 项 OUTLINE 与 RSS 条目一致，冻结 manifest 将 `BV13BdfBoELd` 精确映射到 GUID `69e4e6951d989496e7fecc7b`。Bilibili 所选单 P 音轨从主持人开场、嘉宾介绍连续到末尾关于“语言即世界”的问答，支持其为完整官方视频播客版而非片段、预告或直播回放。RSS 与视频时长相差约 66.494 秒；本集没有专用跨平台声学抽样证据，因此该映射不证明两端逐句或音轨相同，也不据此推断具体剪辑差异
- 本地音频：AAC、48 kHz、双声道、226,262,539 字节
- 正式期号：发布者 RSS 标题明确标注 `137.`，GUID 为 `69e4e6951d989496e7fecc7b`；Bilibili 标题没有期号，未据其反推编号
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

洪乐潼从数学的创造与发现、证明和直觉谈起，回顾自己从广州、MIT、牛津到斯坦福的学习路径，以及从“不想创业”到创办 Axiom 的过程；技术讨论则围绕 Lean、证明器、猜想器、知识库、自动形式化、代码验证和递归自我改进，解释为什么她把 AI for Math 视为一场兼具科学登月与商业责任的系统工程。

## 核心议题

- 数学的创造与发现、公理契约、证明和直觉
- 蛮力型学习、自由注意力、失败与小团队共同体
- 从法学、Lean 和论文阅读走向 Axiom 创业
- 证明器、猜想器、知识库与自动形式化
- 数学、代码、软件验证与 AI for Science
- 融资、人才密度、bottom-up 文化与科学商业平衡
- 专门智能、递归自我改进和人类数学家的未来角色

## 待补充

- [x] 通过发布者 RSS 标题、GUID、enclosure、简介与 OUTLINE 核对正式第 137 期
- [x] 核对 Bilibili BVID、aid、cid、page、发布者账号与单 P 完整播客映射
- [x] 检查匿名访问可见的平台字幕轨，且未绕过登录控制
- [x] 获取公开音轨并完成编码、时长、大小、媒体哈希与重新解码 PCM 承诺核验
- [x] 生成完整 Qwen3-ASR 机器逐字稿及 adaptive v2 产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 人工核听开场姓名和公司介绍、长段中英混说、说话人切换，以及末句停在 `04:22:57`、距离音频端点约 13.5 秒的收尾；确认是否为正常片尾，并检查长段时间边界
- [ ] 校正机器稿中的明显或疑似近音异写，尤其“洪乐彤”“小俊”、Axim/Action、Cano/Kan/Can、Shubo、Wirth/Where 等；逐一核对张小珺、洪乐潼、Shubh/Shubho、Ken Ono、Kenny Lau、Kevin Buzzard、Evan Chen、François Charton、Guillaume Lample、Christian Szegedy、Demis Hassabis、Howard Morgan、Jim Simons 等人名
- [ ] 核查公司、论文、模型、语言和 Benchmark 专名，尤其 Axiom、Lean、Mathlib、ATP/ITP、AlphaGeometry、AlphaProof、Putnam、Draft/Sketch/Proof、Lean Hammer、Grind、MiniF2F、FrontierMath、Verina、DeepSeek/Seed/Hilbert/Kimina Prover、Curry–Howard correspondence、SMT/SAT、Jasper、Verve Coffee、B Capital、Menlo Ventures 等
- [ ] 回听并查证年龄、求学与任职年份、论文及团队贡献、融资金额与估值、投资方、员工人数和人员背景、Putnam/IMO 历史成绩及人工参与、Benchmark 分数、工具速度、Lean 数据规模、模型/卡数和研究成果；第三方公司的组织评价、路线优劣、AI for Math 的市场与 AGI/ASI 影响、中美关系及 2026 年预测均保持为嘉宾陈述或录制时判断
