---
schema_version: 1
kind: episode
id: "zhangxiaojun:94"
show_id: zhangxiaojun
episode_key: "94"
episode_number: 94
slug: 94-song-lin
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-09
  source: publisher-rss
  url: https://www.xiaoyuzhoufm.com/episode/67bb3696606e5c5940533ef4
title: "逐篇讲解DeepSeek、Kimi、MiniMax注意力机制新论文——“硬件上的暴力美学”"
navigation_title: "松琳 · 注意力机制与硬件设计"
catalog_keyword: "注意力机制"
published_at: "2025-02-24T07:00:00+08:00"
duration_ms: 9372502
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: song-lin
    name: 松琳
    role: guest
sources:
  - platform: xiaoyuzhou
    kind: episode
    title: "94. 逐篇讲解DeepSeek、Kimi、MiniMax注意力机制新论文——“硬件上的暴力美学”"
    url: https://www.xiaoyuzhoufm.com/episode/67bb3696606e5c5940533ef4
    preferred: false
    identifiers:
      eid: 67bb3696606e5c5940533ef4
      pid: 626b46ea9cbbf0451cf5a962
      media_id: 626b46ea9cbbf0451cf5a962/lqyo-JyWn3Mw0yr1x6rq86eePyXk.m4a
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 67bb3696606e5c5940533ef4
  - platform: bilibili
    kind: video
    title: "逐篇讲解DeepSeek、Kimi、MiniMax注意力机制新论文——“硬件上的暴力美学”"
    url: https://www.bilibili.com/video/BV1ZmAQekEMc/
    preferred: true
    identifiers:
      bvid: BV1ZmAQekEMc
      aid: "114054265835426"
      cid: "28544009271"
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
    sha256: a88504fb3a4745b342790d62f10df1636b47facaab453ba496e9591a9a502ae0
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
  generated_at: "2026-08-09T23:28:31.750414Z"
  quality:
    source_chunks: 40
    aligned_chunks: 40
    alignment_items: 33323
    sentence_segments: 731
    refined_segments: 731
    rendered_blocks: 343
    rendered_lines: 731
  performance:
    model_load_seconds: 0.183
    transcription_seconds: 331.118
    prompt_tokens: 122566
    generation_tokens: 24681
    attempt_prompt_tokens: 122566
    attempt_generation_tokens: 24681
    generation_call_count: 40
    prompt_tokens_per_second: 370.158
    generation_tokens_per_second: 74.538
    aligner_load_seconds: 0.151
    alignment_seconds: 53.873
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
    generated_at: "2026-08-09T23:28:31.750414Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/94-song-lin/source.m4a
  metadata_path: .cache/media/zhangxiaojun/94-song-lin/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-09T12:36:14.194112Z"
  verified_at: "2026-08-09T12:36:14.194112Z"
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 96188547
  duration_ms: 9372502
  sha256: d1766f599acd40a3a741c2bfd9dfd86c5d167d204e32b884765bc3752a353bea
last_verified_at: 2026-08-09
---

# 逐篇讲解 DeepSeek、Kimi、MiniMax 注意力机制新论文——“硬件上的暴力美学”

> 本页保留发布者标题、简介与章节形成的概览，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。正式期号只取自发布者 RSS，不按 Bilibili 标题或导入顺序推断。

## 单集信息

- 节目：张小珺商业访谈录 #94
- 主持人：张小珺
- 嘉宾：松琳
- Bilibili 发布时间：2025-02-24 07:00:00（UTC+8）
- Bilibili 视频音轨时长：02:36:12.502；官方 RSS 音频时长：02:36:12
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/67bb3696606e5c5940533ef4)、[Bilibili 视频](https://www.bilibili.com/video/BV1ZmAQekEMc/)
- 来源状态：公开单 P；匿名状态下平台返回空 tracks 并提示需要登录才能进一步检查，未取得匿名公开字幕轨；未使用 cookies 或登录态，且未绕过访问控制；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 完整性核验：发布者 RSS 将本期明确列为《张小珺商业访谈录》第 94 期，标题、嘉宾与主题和同一发布者账号上传的 Bilibili 单 P 一致；冻结 manifest 将 `BV1ZmAQekEMc` 精确映射到该 RSS 条目。发布者简介称“今天这集节目”延续论文系列，并明确把成片称为“我们的播客节目”；简介列出三篇论文及嘉宾，章节从 `00:02:30` 连续延伸至 `02:30:07`，支持其为完整官方视频播客版而非课程、演讲、片段或高光。RSS 与本地视频音轨时长相差约 0.502 秒；本集没有专用跨平台声学抽样证据，因此该映射不证明两端逐句相同，也不据此推断具体剪辑差异
- 本地音频：AAC、44.1 kHz、双声道、96,188,547 字节
- 正式期号：发布者 RSS 标题明确标注 `94.`，GUID 为 `67bb3696606e5c5940533ef4`；Bilibili 标题没有期号，未据其反推编号
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

松琳与张小珺以 DeepSeek 的 Native Sparse Attention、Kimi 的 MoBA 和 MiniMax-01 的 Lightning Attention 为主线，拆解长上下文注意力怎样同时面对算法表达、训练可微性、显存访问与矩阵计算效率。

讨论从自注意力和 KV cache 的成本出发，比较动态稀疏、块级选择与线性—softmax 混合架构，并把三条路线放回硬件协同、训练稳定性、检索能力和工程取舍中理解。

## 核心议题

- 长上下文为什么同时受计算复杂度、KV cache 与内存墙约束
- DeepSeek NSA 的三分支结构、GQA 共享选择与硬件对齐
- Kimi MoBA 的极简块稀疏路线及训练、索引取舍
- MiniMax-01 的 Lightning Attention、chunkwise 计算与混合架构
- 三篇论文的可比边界、开源传播与架构创新判断

## 待补充

- [x] 通过发布者 RSS 标题、GUID、enclosure、简介与章节核对正式第 94 期
- [x] 核对 Bilibili BVID、aid、cid、page、发布者账号与单 P 完整播客映射
- [x] 检查匿名状态的平台字幕轨，且未使用登录态或绕过访问控制
- [x] 获取公开音轨并完成编码、时长、大小、媒体哈希与重新解码 PCM 承诺核验
- [x] 生成完整 Qwen3-ASR 机器逐字稿及 adaptive v2 产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 人工核听片头摘要、主持人与嘉宾的快速轮换、笑声和掌声较长的段落，以及最后一条对齐在 `02:36:02.895` 结束、距离 `02:36:12.502` 音频端点约 9.607 秒的收尾；校正“张小军/张小俊”“松林”“Kimmy”“NIS/DBC”“MOMA/mobile”“S one”“负二 attention”等明显或疑似近音误识别
- [ ] 核查人名、机构、论文、模型、系统与技术专名，尤其张小珺、松琳及机器稿中的“杨松林”“Young King”，DeepSeek、Kimi、MiniMax、Native Sparse Attention（NSA）、Quest、MoBA、Lightning Attention、FlashAttention、SRAM、HBM、GQA、KV cache、tensor core、Triton、CUDA、Mamba 2、GLA、RetNet、xLSTM、Titans、TTT、Zamba、Jamba、Mamba、RWKV、Hymba 与 Flash Linear Attention；不在核实前把机器识别出的姓名、别名或履历写入人物档案
- [ ] 回听并查证数字、配置与图表口径：64K 上下文与约十倍速度、64/16 和 512/3 的块选择、192/64/2560 等维度、A100/H100 与 tensor core 的倍数关系、百万 token、7:1 与 80 层、10%—20% 层比例、90%/10% 训练 token，以及节目中多次修正或由图表口述的数字
- [ ] 高影响事实需核验三篇论文的精确实现与基准、是否从头预训练、模型性能与 GPT-4o 对比、产品部署和上下文长度、公司开源范围、相关团队及作者归属；关于路线优劣、竞品实现、人才流动、中美差异和产业影响的说法均保持为嘉宾陈述或录制时判断
