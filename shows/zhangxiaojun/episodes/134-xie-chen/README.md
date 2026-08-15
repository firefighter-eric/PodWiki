---
schema_version: 1
kind: episode
id: "zhangxiaojun:134"
show_id: zhangxiaojun
episode_key: "134"
episode_number: 134
slug: 134-xie-chen
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-09
  source: publisher-rss
  url: https://www.xiaoyuzhoufm.com/episode/69c953b4b977fb2c478df5c3
title: "【数据的综述】和谢晨聊，新时代的石油、历史、版图、数据金字塔、定价与Recipe"
navigation_title: "谢晨 · AI 与机器人数据产业"
catalog_keyword: "数据产业"
published_at: "2026-03-30T11:00:00+08:00"
duration_ms: 9410112
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: xie-chen
    name: 谢晨
    role: guest
sources:
  - platform: xiaoyuzhou
    kind: episode
    title: "134. 【数据的综述】和谢晨聊，新时代的石油、历史、版图、数据金字塔、定价与Recipe"
    url: https://www.xiaoyuzhoufm.com/episode/69c953b4b977fb2c478df5c3
    preferred: false
    identifiers:
      eid: 69c953b4b977fb2c478df5c3
      pid: 626b46ea9cbbf0451cf5a962
      media_id: 626b46ea9cbbf0451cf5a962/lkInPy65_ZR4cQmK23rmHJ_hhLVQ.m4a
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 69c953b4b977fb2c478df5c3
  - platform: bilibili
    kind: video
    title: "【数据的综述】和谢晨聊，新时代的石油、历史、版图、数据金字塔、定价与Recipe"
    url: https://www.bilibili.com/video/BV1sLX9B4EqD/
    preferred: true
    identifiers:
      bvid: BV1sLX9B4EqD
      aid: "116313401918882"
      cid: "37078828577"
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
    sha256: 3df5062b419d339c5534c89ed63496c9d7540516e70913b72d6307bd158fb5c2
transcript:
  path: transcript.zh-CN.md
  platform_subtitle_access: no-anonymous-public-track
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
    planned_chunk_count: 40
    final_leaf_chunk_count: 40
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 163840
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: "2026-08-09T22:34:30.870795Z"
  quality:
    source_chunks: 40
    aligned_chunks: 40
    alignment_items: 46954
    sentence_segments: 1239
    refined_segments: 1237
    rendered_blocks: 320
    rendered_lines: 1237
  performance:
    model_load_seconds: 0.178
    transcription_seconds: 402.795
    prompt_tokens: 123054
    generation_tokens: 30878
    attempt_prompt_tokens: 123054
    attempt_generation_tokens: 30878
    generation_call_count: 40
    prompt_tokens_per_second: 305.5
    generation_tokens_per_second: 76.659
    aligner_load_seconds: 0.189
    alignment_seconds: 67.946
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
    generated_at: "2026-08-09T22:34:30.870795Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/134-xie-chen/source.m4a
  metadata_path: .cache/media/zhangxiaojun/134-xie-chen/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-09T12:34:59.622454Z"
  verified_at: "2026-08-09T12:34:59.622454Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 159540329
  duration_ms: 9410112
  sha256: 7f2a20de6ff46f83d169f0bdb55dcd57bc101c9dbe7e832e76ee55f06180394e
last_verified_at: 2026-08-09
---

# 【数据的综述】和谢晨聊，新时代的石油、历史、版图、数据金字塔、定价与 Recipe

> 本页保留发布者标题、简介与章节形成的概览，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。正式期号只取自发布者 RSS，不按 Bilibili 标题或导入顺序推断。

## 单集信息

- 节目：张小珺商业访谈录 #134
- 主持人：张小珺
- 嘉宾：谢晨
- Bilibili 发布时间：2026-03-30 11:00:00（UTC+8）
- Bilibili 视频时长：02:36:51；官方 RSS 音频时长：02:38:22
- RSS 正式标题：134. 【数据的综述】和谢晨聊，新时代的石油、历史、版图、数据金字塔、定价与 Recipe
- Bilibili 原标题：【数据的综述】和谢晨聊，新时代的石油、历史、版图、数据金字塔、定价与 Recipe
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/69c953b4b977fb2c478df5c3)、[Bilibili 视频](https://www.bilibili.com/video/BV1sLX9B4EqD/)
- 来源状态：公开单 P；匿名状态下平台返回 `need_login: false` 与空 tracks，未取得匿名公开字幕轨；未登录且未绕过访问控制；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 完整性核验：发布者 RSS 将本期明确列为《张小珺商业访谈录》第 134 期，标题、嘉宾和主题与同一发布者账号上传的 Bilibili 单 P 一致；冻结 manifest 将 `BV1sLX9B4EqD` 精确映射到该 RSS 条目。发布者在 Bilibili 简介中称“通过一集节目完整聊聊”数据，并列出从 `00:01:07` 到 `02:28:52` 的全程章节，本地所选音轨也从节目开场连续覆盖到最后的终局讨论，支持其为完整官方视频播客版而非片段或高光。RSS 与视频时长相差约 91.888 秒；本集没有专用跨平台声学抽样证据，因此该映射不证明两端逐句相同，也不据此推断具体剪辑差异
- 本地音频：AAC、48 kHz、双声道、159,540,329 字节
- 正式期号：发布者 RSS 标题明确标注 `134.`，GUID 为 `69c953b4b977fb2c478df5c3`；Bilibili 标题没有期号，未据其反推编号
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

张小珺与返场嘉宾谢晨尝试对 AI 与机器人数据产业做一次系统综述：从“数据即教育”的定义出发，讨论 LLM、世界模型与 VLA 的关系，继而展开真机、仿真和人类第一视角组成的数据金字塔、规模化评测、Data Recipe、定价，以及模型商、数据商、本体商与场景方的产业分工。

## 核心议题

- 从静态数据集到反馈驱动学习系统的数据产业史
- LLM、世界模型、VLA 与零样本泛化
- 真机、仿真、人类第一视角与数据金字塔
- 规模化评测、sim-to-real / real-to-sim 与 Data Recipe
- 数据定价、Data Engine 和四方产业生态
- 中美团队、本体与大脑路线及 AI 自我学习终局

## 待补充

- [x] 通过发布者 RSS 标题、GUID、enclosure、简介与章节核对正式第 134 期
- [x] 核对 Bilibili BVID、aid、cid、page、发布者账号与单 P 完整播客映射
- [x] 检查匿名状态的平台字幕轨，且未绕过登录控制
- [x] 获取公开音轨并完成编码、时长、大小、媒体哈希与重新解码 PCM 承诺核验
- [x] 生成完整 Qwen3-ASR 机器逐字稿及 adaptive v2 产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 人工核听开场冷开片段、说话人切换，以及末句停在 `02:36:35`、距离音频端点约 15 秒的收尾；校正“巨深/聚深”“摘刀Com”“未来”“地脉”“派”“语数”“智源”“Vimo”“McQuar”“Search”“Enact”“LLOINF”等明显或疑似近音误识别
- [ ] 核查人名、公司、模型、产品和 Benchmark 专名，尤其谢晨、严海波、李飞飞及相关教授/团队，Jet.com、Cruise、Waymo、NVIDIA、蔚来、Scale AI、Mercor、Surge AI、Behavior、UMI、Generalist、Physical Intelligence、Figure、宇树、智元、VLA/VA、Data Foundry、Data Engine、RL infrastructure 等
- [ ] 回听并查证任职年份与项目贡献、客户与“全球前五”口径、标注人数和专家时薪、卡数、机器人数量、数据小时数与单价、Benchmark 成绩、团队人数、各类倍数和未来年限；公司合作、路线优劣、中美竞争和行业终局均保持为嘉宾陈述或录制时判断
