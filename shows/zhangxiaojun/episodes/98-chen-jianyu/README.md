---
schema_version: 1
kind: episode
id: "zhangxiaojun:98"
show_id: zhangxiaojun
episode_key: "98"
episode_number: 98
slug: 98-chen-jianyu
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-09
  source: publisher-rss
  url: https://www.xiaoyuzhoufm.com/episode/67f28c6e0decaeb0943fb14a
title: "逐篇解析机器人基座模型和VLA经典论文——“人就是最智能的VLA”"
navigation_title: "陈建宇 · 机器人基座模型与 VLA"
catalog_keyword: "VLA"
published_at: "2025-04-07T00:39:35+08:00"
duration_ms: 8981246
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: chen-jianyu
    name: 陈建宇
    role: guest
sources:
  - platform: xiaoyuzhou
    kind: episode
    title: "98. 逐篇讲解机器人基座模型和VLA经典论文——“人就是最智能的VLA”"
    url: https://www.xiaoyuzhoufm.com/episode/67f28c6e0decaeb0943fb14a
    preferred: false
    identifiers:
      eid: 67f28c6e0decaeb0943fb14a
      pid: 626b46ea9cbbf0451cf5a962
      media_id: 626b46ea9cbbf0451cf5a962/lqi4NGfX-65ZwWUnKXBWTyWnkWMT.m4a
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 67f28c6e0decaeb0943fb14a
  - platform: bilibili
    kind: video
    title: "逐篇解析机器人基座模型和VLA经典论文——“人就是最智能的VLA”"
    url: https://www.bilibili.com/video/BV1q6RzYnENi/
    preferred: true
    identifiers:
      bvid: BV1q6RzYnENi
      aid: "114291948652862"
      cid: "29270870489"
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
    sha256: a93a899eae12f4c66ae86daaf0f134123eac6bba6b347cd148027a952a78df75
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
    planned_chunk_count: 38
    final_leaf_chunk_count: 38
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 155648
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: "2026-08-09T23:36:14.503973Z"
  quality:
    source_chunks: 38
    aligned_chunks: 38
    alignment_items: 44544
    sentence_segments: 930
    refined_segments: 930
    rendered_blocks: 321
    rendered_lines: 930
  performance:
    model_load_seconds: 0.184
    transcription_seconds: 392.932
    prompt_tokens: 117443
    generation_tokens: 30546
    attempt_prompt_tokens: 117443
    attempt_generation_tokens: 30546
    generation_call_count: 38
    prompt_tokens_per_second: 298.889
    generation_tokens_per_second: 77.739
    aligner_load_seconds: 0.15
    alignment_seconds: 60.135
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
    generated_at: "2026-08-09T23:36:14.503973Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/98-chen-jianyu/source.m4a
  metadata_path: .cache/media/zhangxiaojun/98-chen-jianyu/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-09T12:36:18.363276Z"
  verified_at: "2026-08-09T12:36:18.363276Z"
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 87295533
  duration_ms: 8981246
  sha256: 1f35be693ff7388929358ab08ada609c477624419b2b41fd11d98f6dde3b9955
last_verified_at: 2026-08-09
---

# 逐篇解析机器人基座模型和 VLA 经典论文——“人就是最智能的 VLA”

> 本页分别保留 Bilibili 原标题中的“逐篇解析”和发布者 RSS 正式标题中的“逐篇讲解”，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。正式期号只取自发布者 RSS，不按 Bilibili 标题或导入顺序推断。

## 单集信息

- 节目：张小珺商业访谈录 #98
- 主持人：张小珺
- 嘉宾：陈建宇
- Bilibili 发布时间：2025-04-07 00:39:35（UTC+8）
- 发布者 RSS 发布时间：2025-04-07 07:00:00（UTC+8）
- Bilibili 视频音轨时长：02:29:41.246；官方 RSS 音频时长：02:29:41
- RSS 正式标题：98. 逐篇讲解机器人基座模型和VLA经典论文——“人就是最智能的VLA”
- Bilibili 原标题：逐篇解析机器人基座模型和VLA经典论文——“人就是最智能的VLA”
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/67f28c6e0decaeb0943fb14a)、[Bilibili 视频](https://www.bilibili.com/video/BV1q6RzYnENi/)
- 来源状态：公开单 P；匿名状态下平台返回 `need_login: true` 与空 tracks，未发现匿名公开字幕轨；未登录且未绕过访问控制；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 播客与完整性核验：发布者 RSS 正文明确称其为“播客节目”，把本条列为正式第 98 期，并直接把 `BV1q6RzYnENi` 链接为本集“含投屏的视频版本”；冻结 manifest 将该 BVID 唯一映射到 GUID `67f28c6e0decaeb0943fb14a`。Bilibili 发布者账号、嘉宾、机器人基座模型与 VLA 主题、论文顺序及节目收尾均与 RSS 对应，所选单 P 从主持人开场连续覆盖讲解、问答和订阅口播，支持其为完整官方视频播客版，而不是课程片段、预告或直播回放。RSS 与视频音轨时长只相差约 0.246 秒；本集没有专用跨平台声学抽样证据，因此该映射不证明两端逐句或音轨相同，也不据此推断具体剪辑差异
- 本地音频：AAC、44.1 kHz、双声道、87,295,533 字节
- 正式期号：发布者 RSS 标题明确标注 `98.`，GUID 为 `67f28c6e0decaeb0943fb14a`；Bilibili 标题没有期号，未据其反推编号
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

陈建宇以“从利用现成基础模型，到为机器人预训练基础模型”为主线，依次解释规划、感知、执行三段式方案与端到端 VLA 的差别，再沿 ALOHA、Gato、RT 系列、OpenVLA、HiRT、π0、Diffusion Policy、RDT 和预测式策略等工作，讨论通用机器人模型如何处理跨本体数据、动作频率、未来预测与强化学习；最后把技术路线落到星动纪元的软硬件一体化和 To A、To B、To C 商业阶段。

## 核心议题

- 大语言模型与通用人形本体为何共同改变机器人路线
- 利用 LLM/VLM/Code LM 改造 Planning、Perception、Actuation
- 从 ALOHA、Gato、RT-1 到跨本体 Transformer 策略
- PaLM-E、RT-2、RT-X 与 OpenVLA 的网络知识迁移
- HiRT、Helix、π0 与 GR00T N1 的动作模块和分频处理
- Diffusion Policy、RDT-1B 与动作—未来联合生成
- UP-VLA、在线强化学习及 To A/To B/To C 商业路径

## 待补充

- [x] 通过发布者 RSS 标题、GUID、enclosure、简介与章节核对正式第 98 期
- [x] 核对 Bilibili BVID、aid、cid、page、发布者账号与单 P 完整播客映射
- [x] 检查匿名访问可见的平台字幕轨，且未绕过登录控制
- [x] 获取公开音轨并完成编码、时长、大小、媒体哈希与重新解码 PCM 承诺核验
- [x] 生成完整 Qwen3-ASR 机器逐字稿及 adaptive v2 产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 人工核听开头约一分钟论文预告与 `00:01:17` 主持人正式开场之间的剪辑、投屏演示期间的长句断点和说话人切换，以及末句停在 `02:29:24`、距离音频端点约 14.4 秒的片尾留白
- [ ] 校正机器稿中的系统性近音异写，尤其“张小军/张小俊”应按来源核为“张小珺”、“心动纪元”应核为“星动纪元”、“巨深智能”应核为“具身智能”、“Rober/robust 仿射性 model”应核为 robot foundation model、“V O M/V O A”应结合语境核为 VLM/VLA，以及 “See can/C 看”所指 SayCan、“acton”所指 Octo、“派”所指 Physical Intelligence
- [ ] 核查人名、机构和论文作者，尤其陈建宇、张小珺、Sergey Levine、Chelsea Finn、李飞飞、Masayoshi Tomizuka、清华大学交叉信息研究院、上海人工智能实验室或上海姚期智研究院的节目表述、UC Berkeley、Stanford、Google Robotics/DeepMind、ByteDance AI Lab、Figure AI、Physical Intelligence、NVIDIA 与星动纪元
- [ ] 核查论文、模型和技术专名，尤其 SayCan、Inner Monologue、DoReMi、VoxPoser、ALOHA/Mobile ALOHA、ACT、MPC、Gato、RT-1/RT-2/RT-X、Octo、CrossFormer、GR-1/GR-2、PaLM-E、Open X-Embodiment、OpenVLA、HiRT、Helix、π0、GR00T N1、Diffusion Policy、RDT-1B、Prediction with Action、Video Prediction Policy、UP-VLA、VLM/VLA、MPC、SFT、PPO、RLHF、flow matching 与 diffusion transformer
- [ ] 回听并查原始论文中的年份、参数和数据口径：ALOHA/Mobile ALOHA 成本，RT-1 的 130K episodes、700 个任务、13 台机器人与 17 个月采集，见过任务接近 100% 和未见任务约 75% 的成功率，PaLM-E 的 562B，Open X-Embodiment 的约 60 个数据集，RT-2 的 1–3 Hz，HiRT 中几十 M 的动作策略与数 B 的 VLM、Helix 的约 80M、RDT-1B 与约 one million 预训练样本，以及在线强化学习从不足 50 到接近 100 的图表
- [ ] 高影响事实需继续保持为嘉宾陈述或录制时判断：robot foundation model 是否是通往通用机器人的“正解”、未来五年能否经常见到机器人、VLA/具身模型能否统一语言模型、自动驾驶与机器人、Physical Intelligence 的人才密度和估值、字节机器人研究在国内大公司实验室中的位置、星动纪元的批量销售与商业闭环、机器人 scaling 是否已出现迹象，以及 To A、To B、To C 的阶段预测
