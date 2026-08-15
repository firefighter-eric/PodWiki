---
schema_version: 1
kind: episode
id: "zhangxiaojun:91"
show_id: zhangxiaojun
episode_key: "91"
episode_number: 91
slug: 91-he-junxian
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-09
  source: publisher-rss
  url: https://www.xiaoyuzhoufm.com/episode/67aacd6b247d51713cedbeda
title: "逐篇讲解DeepSeek关键9篇论文及创新点——“勇敢者的游戏”"
navigation_title: "何俊贤 · DeepSeek 九篇论文"
catalog_keyword: "DeepSeek"
published_at: "2025-02-12T17:46:17+08:00"
duration_ms: 12053014
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: he-junxian
    name: 何俊贤
    role: guest
sources:
  - platform: xiaoyuzhou
    kind: episode
    title: "91. 逐篇讲解DeepSeek关键9篇论文及创新点——“勇敢者的游戏”"
    url: https://www.xiaoyuzhoufm.com/episode/67aacd6b247d51713cedbeda
    preferred: false
    identifiers:
      eid: 67aacd6b247d51713cedbeda
      pid: 626b46ea9cbbf0451cf5a962
      media_id: 626b46ea9cbbf0451cf5a962/lpHslH0xLNHJTbSqJa84E90CHAEI.m4a
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 67aacd6b247d51713cedbeda
  - platform: bilibili
    kind: video
    title: "逐篇讲解DeepSeek关键9篇论文及创新点——“勇敢者的游戏”"
    url: https://www.bilibili.com/video/BV1xuK5eREJi/
    preferred: true
    identifiers:
      bvid: BV1xuK5eREJi
      aid: "113990210421078"
      cid: "28352253606"
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
    sha256: 010010f58bc29e2c52d28e43c20136b3821cd80b0d3abb057caa6288f9e99ded
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
    planned_chunk_count: 51
    final_leaf_chunk_count: 51
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 208896
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: "2026-08-09T23:21:56.832782Z"
  quality:
    source_chunks: 51
    aligned_chunks: 51
    alignment_items: 62715
    sentence_segments: 1242
    refined_segments: 1242
    rendered_blocks: 449
    rendered_lines: 1242
  performance:
    model_load_seconds: 0.176
    transcription_seconds: 575.002
    prompt_tokens: 157614
    generation_tokens: 45164
    attempt_prompt_tokens: 157614
    attempt_generation_tokens: 45164
    generation_call_count: 51
    prompt_tokens_per_second: 274.111
    generation_tokens_per_second: 78.546
    aligner_load_seconds: 0.17
    alignment_seconds: 82.372
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
    generated_at: "2026-08-09T23:21:56.832782Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/91-he-junxian/source.m4a
  metadata_path: .cache/media/zhangxiaojun/91-he-junxian/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-09T12:36:06.473596Z"
  verified_at: "2026-08-09T12:36:06.473596Z"
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 106304174
  duration_ms: 12053014
  sha256: 3098776535317c1a6bbece8af17003cb3698e7a23367e8145931d3dc4119cfb0
last_verified_at: 2026-08-09
---

# 逐篇讲解 DeepSeek 关键 9 篇论文及创新点——“勇敢者的游戏”

> 本页保留 Bilibili 原标题与发布者 RSS 正式标题，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。正式期号只取自发布者 RSS，不按 Bilibili 标题或导入顺序推断。

## 单集信息

- 节目：张小珺商业访谈录 #91
- 主持人：张小珺
- 嘉宾：何俊贤
- Bilibili 发布时间：2025-02-12 17:46:17（UTC+8）
- 发布者 RSS 发布时间：2025-02-11 12:41:27（UTC+8）
- Bilibili 视频音轨时长：03:20:53.014；官方 RSS 音频时长：03:20:52
- RSS 正式标题：91. 逐篇讲解DeepSeek关键9篇论文及创新点——“勇敢者的游戏”
- Bilibili 原标题：逐篇讲解DeepSeek关键9篇论文及创新点——“勇敢者的游戏”
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/67aacd6b247d51713cedbeda)、[Bilibili 视频](https://www.bilibili.com/video/BV1xuK5eREJi/)
- 来源状态：公开单 P；匿名状态下平台返回 `need_login: false` 与空 tracks，未发现匿名公开字幕轨；未登录且未绕过访问控制；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 播客与完整性核验：发布者 RSS 正文明确称《商业访谈录》为播客，并直接把 `BV1xuK5eREJi` 链接为本期“含投屏的视频版本”；冻结 manifest 将该 BVID 唯一映射到正式 GUID `67aacd6b247d51713cedbeda`，标题、嘉宾、九篇论文主题与章节时间线一致。Bilibili 所选单 P 音轨从主持人开场、嘉宾介绍和基座模型讲解连续到 R1、强化学习问答及节目收尾，支持其为完整官方视频播客版，而不是片段、预告或直播回放。RSS 与视频音轨时长相差约 1.014 秒；本集没有专用跨平台声学抽样证据，因此该映射不证明两端逐句或音轨相同，也不据此推断具体剪辑差异
- 本地音频：AAC、44.1 kHz、双声道、106,304,174 字节
- 正式期号：发布者 RSS 标题明确标注 `91.`，GUID 为 `67aacd6b247d51713cedbeda`；Bilibili 标题没有期号，未据其反推编号
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

何俊贤沿基座模型与推理模型两条路线，讲解 DeepSeek LLM、MoE、V2、V3、Coder、Prover 与 R1 等论文，并用 Math Shepherd、DeepSeek Math 补足奖励模型、GRPO 与在线强化学习的技术演进；贯穿全场的判断是，DeepSeek 通过严谨实验、持续开源和面向效率的差异化选择，逐步形成了自己的技术栈。

## 核心议题

- DeepSeek LLM、scaling law 与基准评测诚实性
- 细粒度 MoE、共享专家与激活参数
- V2 的 MLA、KV cache 与部署成本
- V3 的 MTP、FP8 训练与基础设施优化
- Coder、Math Shepherd、DeepSeek Math 与 GRPO
- Prover、规则奖励、R1-Zero 与长推理
- 算法创新、工程创新和未来 scaling 路线

## 待补充

- [x] 通过发布者 RSS 标题、GUID、enclosure、简介与章节核对正式第 91 期
- [x] 核对 Bilibili BVID、aid、cid、page、发布者账号与单 P 完整播客映射
- [x] 检查匿名访问可见的平台字幕轨，且未绕过登录控制
- [x] 获取公开音轨并完成编码、时长、大小、媒体哈希与重新解码 PCM 承诺核验
- [x] 生成完整 Qwen3-ASR 机器逐字稿及 adaptive v2 产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 人工核听开头预告与 `00:01:15` 主持人正式开场之间的衔接、屏幕分享时的中英混说、长句断点和说话人切换；末句停在 `03:20:38`、距离音频端点约 14.8 秒，需确认其为正常片尾留白
- [ ] 校正机器稿中的系统性近音异写，尤其“张小俊/张小军”应按来源核为“张小珺”、“潘佳怡/潘家怡”、“二万/二湾”所指 R1、“MLE/MIE”所指 MoE、“G R P U”所指 GRPO、“DPU”所指 DPO、“请亲纳/齐齐纳/斯克尼诺”所指 Chinchilla，以及 Lean、Math Shepherd、C-Eval 等；逐一核对张小珺、何俊贤、潘家怡、梁文锋及节目提到的研究者和团队
- [ ] 核查论文、模型、公司和技术专名，尤其 DeepSeek LLM、DeepSeekMoE、DeepSeek-V2/V3、DeepSeek-Coder/Coder-V2、Math Shepherd、DeepSeekMath、DeepSeek-Prover/Prover-V1.5、DeepSeek-R1/R1-Zero、Llama 2/3、Mistral/Mixtral、Kimi K1.5、OpenAI o1、Chinchilla scaling law、MoE、MLA、MHA/GQA/MQA、KV cache、RoPE、MTP、FP8、PPO/GRPO/DPO、PRM/ORM、RFT、pass@k、AIME、GSM8K、MCTS/RMaxTS、Lean、C-Eval、Skywork 与昆仑万维
- [ ] 回听并查原始论文中的模型参数、激活参数、专家数、训练 token、SFT 数据量、GPU 型号与数量、GPU-hour、训练成本、KV cache 降幅、吞吐倍率、benchmark 分数、C-Eval 47 到 71 的对照、PRM800K 数据规模和团队实验周期；所有数字均须同时确认单位、版本、比较对象和统计口径
- [ ] 高影响事实需继续保持为嘉宾陈述或录制时判断：DeepSeek 是否首创或最早大规模使用相关技术、是否未刷榜、V2 API 是否盈利并引发价格战、V3 与 Llama 的成本/能力比较、R1 与 OpenAI o1 的技术路线是否相同、国外团队的关注与评价、模型是否出现自我反思、强化学习能否迁移到开放任务，以及 DeepSeek 的组织动机、算力总量和商业化目标
