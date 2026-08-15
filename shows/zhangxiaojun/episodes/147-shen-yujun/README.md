---
schema_version: 1
kind: episode
id: "zhangxiaojun:147"
show_id: zhangxiaojun
episode_key: "147"
episode_number: 147
slug: 147-shen-yujun
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-09
  source: publisher-rss
  url: https://www.xiaoyuzhoufm.com/episode/6a5f79b3a3fec224d5a128cd
title: "和蚂蚁灵波沈宇军聊：机器人原生基础模型、大脑和本体的关系、预训练与数据scale up、老师汤晓鸥"
navigation_title: "沈宇军 · 机器人原生基础模型"
catalog_keyword: "机器人基础模型"
published_at: "2026-07-22T08:00:00+08:00"
duration_ms: 6633451
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: shen-yujun
    name: 沈宇军
    role: guest
sources:
  - platform: xiaoyuzhou
    kind: episode
    title: "147. 和蚂蚁灵波沈宇军聊：机器人原生基础模型、大脑和本体的关系、预训练与数据scale up、老师汤晓鸥"
    url: https://www.xiaoyuzhoufm.com/episode/6a5f79b3a3fec224d5a128cd
    preferred: false
    identifiers:
      eid: 6a5f79b3a3fec224d5a128cd
      pid: 626b46ea9cbbf0451cf5a962
      media_id: 626b46ea9cbbf0451cf5a962/luXTyuAfi_2ONiM15fW6Lpypo2GA.m4a
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 6a5f79b3a3fec224d5a128cd
  - platform: bilibili
    kind: video
    title: "和蚂蚁灵波沈宇军聊：机器人原生基础模型、大脑和本体的关系、预训练与数据scale up、老师汤晓鸥"
    url: https://www.bilibili.com/video/BV1cRK86zEpQ/
    preferred: true
    identifiers:
      bvid: BV1cRK86zEpQ
      aid: "116958284480617"
      cid: "40187331377"
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
    sha256: 2a81ffaeafee23bc5d42b06fe17bd09b0e136be2e4a2d4df9fd18d68fa3281b3
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
    planned_chunk_count: 28
    final_leaf_chunk_count: 28
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 114688
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: "2026-08-09T23:10:48.580035Z"
  quality:
    source_chunks: 28
    aligned_chunks: 28
    alignment_items: 33357
    sentence_segments: 727
    refined_segments: 727
    rendered_blocks: 237
    rendered_lines: 727
  performance:
    model_load_seconds: 0.187
    transcription_seconds: 290.851
    prompt_tokens: 86742
    generation_tokens: 22022
    attempt_prompt_tokens: 86742
    attempt_generation_tokens: 22022
    generation_call_count: 28
    prompt_tokens_per_second: 298.235
    generation_tokens_per_second: 75.716
    aligner_load_seconds: 0.212
    alignment_seconds: 44.902
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
    generated_at: "2026-08-09T23:10:48.580035Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/147-shen-yujun/source.m4a
  metadata_path: .cache/media/zhangxiaojun/147-shen-yujun/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-09T12:35:54.998616Z"
  verified_at: "2026-08-09T12:35:54.998616Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 102786476
  duration_ms: 6633451
  sha256: d5bd21a19fb675e34368d1f280c6ff7c9bdb885ac002e9e1b3f315ea2c333eb0
last_verified_at: 2026-08-09
---

# 和蚂蚁灵波沈宇军聊：机器人原生基础模型、大脑和本体的关系、预训练与数据 scale up、老师汤晓鸥

> 本页保留发布者标题、简介与章节形成的概览，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。正式期号只取自发布者 RSS，不按 Bilibili 标题或导入顺序推断。

## 单集信息

- 节目：张小珺商业访谈录 #147
- 主持人：张小珺
- 嘉宾：沈宇军
- Bilibili 发布时间：2026-07-22 08:00:00（UTC+8）
- Bilibili 视频音轨时长：01:50:33.451；官方 RSS 音频时长：01:52:54
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/6a5f79b3a3fec224d5a128cd)、[Bilibili 视频](https://www.bilibili.com/video/BV1cRK86zEpQ/)
- 来源状态：公开单 P；匿名状态下平台返回空 tracks 并提示需要登录才能进一步检查，未取得匿名公开字幕轨；未使用 cookies 或登录态，且未绕过访问控制；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 完整性核验：发布者 RSS 将本期明确列为《张小珺商业访谈录》第 147 期，标题、嘉宾与主题和同一发布者账号上传的 Bilibili 单 P 一致；冻结 manifest 将 `BV1cRK86zEpQ` 精确映射到该 RSS 条目。发布者在简介中称其为对蚂蚁灵波首席科学家沈宇军的访谈，并同时列出音频播客和视频播客平台，章节从 `00:02:03` 连续延伸至 `01:31:48`，支持其为完整官方视频播客版而非片段或高光。RSS 与本地视频音轨时长相差约 140.549 秒；本集没有专用跨平台声学抽样证据，因此该映射不证明两端逐句相同，也不据此推断具体剪辑差异
- 本地音频：AAC、48 kHz、双声道、102,786,476 字节
- 正式期号：发布者 RSS 标题明确标注 `147.`，GUID 为 `6a5f79b3a3fec224d5a128cd`；Bilibili 标题没有期号，未据其反推编号
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

沈宇军从个人研究经历和蚂蚁灵波的成立谈起，解释团队为什么选择只做机器人“大脑”、如何把跨本体、跨任务和跨场景作为通用目标，以及第二代六个模型怎样把视觉、空间、视频、世界模型与动作控制连接起来。

后半段围绕真机与第一视角数据、具身预训练、位置和任务泛化继续展开，并讨论大脑与本体的交替演进、灵巧手和传感器、进入家庭的前提，以及一家“背靠大厂的创业公司”怎样看待技术路线中的赌注。

## 核心议题

- 从数字世界模型迁移到具身原生基础模型
- 通用大脑、跨本体路线与六个开源模型的关系
- 真机数据、Ego 数据、预训练与数据规模化
- 大脑、本体、传感器和落地场景的协同演进
- 蚂蚁灵波的创业定位、技术赌注与家庭机器人愿景

## 待补充

- [x] 通过发布者 RSS 标题、GUID、enclosure、简介与章节核对正式第 147 期
- [x] 核对 Bilibili BVID、aid、cid、page、发布者账号与单 P 完整播客映射
- [x] 检查匿名状态的平台字幕轨，且未使用登录态或绕过访问控制
- [x] 获取公开音轨并完成编码、时长、大小、媒体哈希与重新解码 PCM 承诺核验
- [x] 生成完整 Qwen3-ASR 机器逐字稿及 adaptive v2 产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 人工核听片头摘要、主持人口播、嘉宾与主持人的快速轮换，以及最后一条对齐在 `01:50:27.387` 结束、距离 `01:50:33.451` 音频端点约 6.064 秒的收尾；校正“蚂蚁宁波”“巨深/巨身/巨神/巨帧”“机声”“素材员”“不及预期数据”等明显或疑似近音误识别
- [ ] 核查人名、机构、模型、产品与技术专名，尤其张小珺、沈宇军、汤晓鸥，蚂蚁灵波、蚂蚁集团、清华大学、香港中文大学、商汤科技、字节跳动、Generalist、Physical Intelligence、Figure、宇树、智源，以及 Lingbo Vision、Lingbo Depth、VLA、Video、World、VA 2.0、WAM、DINO v2、MoE、Wan、Ego、UMI、in-context learning 等
- [ ] 回听并查证年份、团队和模型规模、构型数量、数据小时数与清洗比例、真机数据成本降幅、训练周期、任务样本数、互联网与机器人数据量差距、十万/百万小时判断、后训练数据量，以及行业玩家数量和家庭任务比例等；模型效果、路线优劣、产业格局和中国数据优势均保持为嘉宾陈述或录制时判断
- [ ] 高影响事实需核验沈宇军的教育与任职经历、蚂蚁灵波的成立和组织关系、模型开源范围、六个模型的架构与能力、数据来源与规模、真机展示效果、合作伙伴与“数据联盟”、集团战略和行业落地进展；不得把节目中的公司口径、竞品评价或时间预测直接视为独立事实
