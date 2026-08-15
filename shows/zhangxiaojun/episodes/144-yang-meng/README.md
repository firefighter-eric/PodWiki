---
schema_version: 1
kind: episode
id: "zhangxiaojun:144"
show_id: zhangxiaojun
episode_key: "144"
episode_number: 144
slug: 144-yang-meng
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-09
  source: publisher-rss
  url: https://www.xiaoyuzhoufm.com/episode/6a2543dcb30e1571aea20d0b
title: "对阳萌的4小时访谈：消费电子死与生、第三类公司、端侧模型、产品方法、游戏模式"
navigation_title: "阳萌 · 消费电子与产品方法"
catalog_keyword: "消费电子"
published_at: "2026-06-08T08:00:00+08:00"
duration_ms: 13052181
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: yang-meng
    name: 阳萌
    role: guest
sources:
  - platform: xiaoyuzhou
    kind: episode
    title: "144. 对阳萌的4小时访谈：消费电子死与生、第三类公司、端侧模型、产品方法、游戏模式"
    url: https://www.xiaoyuzhoufm.com/episode/6a2543dcb30e1571aea20d0b
    preferred: false
    identifiers:
      eid: 6a2543dcb30e1571aea20d0b
      pid: 626b46ea9cbbf0451cf5a962
      media_id: 626b46ea9cbbf0451cf5a962/lnjlEQjGjo1TxuPOuvYgmDV7oo8B.m4a
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 6a2543dcb30e1571aea20d0b
  - platform: bilibili
    kind: video
    title: "对阳萌的4小时访谈：消费电子死与生、第三类公司、端侧模型、产品方法、游戏模式"
    url: https://www.bilibili.com/video/BV1dyE86bENz/
    preferred: true
    identifiers:
      bvid: BV1dyE86bENz
      aid: "116709679696075"
      cid: "38938477886"
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
    sha256: 87e16062da7dfa3215211ff15d91e60f0fdbf1515d0efae469c8dc3c51cb9008
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
    planned_chunk_count: 55
    final_leaf_chunk_count: 55
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 225280
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: "2026-08-09T23:05:04.007144Z"
  quality:
    source_chunks: 55
    aligned_chunks: 55
    alignment_items: 63430
    sentence_segments: 2346
    refined_segments: 2346
    rendered_blocks: 424
    rendered_lines: 2346
  performance:
    model_load_seconds: 0.179
    transcription_seconds: 606.958
    prompt_tokens: 170677
    generation_tokens: 44088
    attempt_prompt_tokens: 170677
    attempt_generation_tokens: 44088
    generation_call_count: 55
    prompt_tokens_per_second: 281.201
    generation_tokens_per_second: 72.638
    aligner_load_seconds: 0.162
    alignment_seconds: 89.757
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
    generated_at: "2026-08-09T23:05:04.007144Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/144-yang-meng/source.m4a
  metadata_path: .cache/media/zhangxiaojun/144-yang-meng/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-09T12:35:48.875348Z"
  verified_at: "2026-08-09T12:35:48.875348Z"
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 193183350
  duration_ms: 13052181
  sha256: 3740bf2901ebc20061bbfb9d234bc482e1ad10b597b613d58eaba5e0fe542f9f
last_verified_at: 2026-08-09
---

# 对阳萌的 4 小时访谈：消费电子死与生、第三类公司、端侧模型、产品方法、游戏模式

> 本页保留 Bilibili 原标题与发布者 RSS 正式标题，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。正式期号只取自发布者 RSS，不按 Bilibili 标题或导入顺序推断。

## 单集信息

- 节目：张小珺商业访谈录 #144
- 主持人：张小珺
- 嘉宾：阳萌
- Bilibili 发布时间：2026-06-08 08:00:00（UTC+8）
- Bilibili 视频时长：03:37:33；官方 RSS 音频时长：03:38:52
- RSS 正式标题：144. 对阳萌的4小时访谈：消费电子死与生、第三类公司、端侧模型、产品方法、游戏模式
- Bilibili 原标题：对阳萌的4小时访谈：消费电子死与生、第三类公司、端侧模型、产品方法、游戏模式
- Bilibili 单 P part 标题：对阳萌的4小时访谈：消费电子死与生、第三类公司、AI变量、产品方法、打游戏的模式选择
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/6a2543dcb30e1571aea20d0b)、[Bilibili 视频](https://www.bilibili.com/video/BV1dyE86bENz/)
- 来源状态：公开单 P；匿名状态下平台返回 `need_login: true` 与空 tracks，未取得匿名可用字幕轨；未登录且未绕过访问控制；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 播客与完整性核验：发布者 RSS 频道将《张小珺商业访谈录》明确描述为深度访谈播客，本期条目又明确声明其“视频播客”在 Bilibili 等平台播出，并将本期正式列为第 144 期；冻结 manifest 将 `BV1dyE86bENz` 精确映射到 GUID `6a2543dcb30e1571aea20d0b`，标题、嘉宾、主题和 9 项 OUTLINE 均一致。Bilibili 所选单 P 音轨从主持人开场与嘉宾介绍连续到末尾关于 AI 变革与人性的回答，支持其为完整官方视频播客版而非片段、预告或直播回放。RSS 与视频时长相差约 79.819 秒；本集没有专用跨平台声学抽样证据，因此该映射不证明两端逐句或音轨相同，也不据此推断具体剪辑差异
- 本地音频：AAC、48 kHz、双声道、193,183,350 字节
- 正式期号：发布者 RSS 标题明确标注 `144.`，GUID 为 `6a2543dcb30e1571aea20d0b`；Bilibili 标题没有期号，未据其反推编号
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

阳萌从博士辍学、Google 与安克早期创业谈起，复盘公司从五系品质产品转向七系极致创新的原因；技术部分以耳机通话为入口，解释端到端声学模型、参数搬运、存算一体和端侧模型；组织部分则围绕浅海、第三类公司、分层授权、AI 中台、流程智能体和创造者分配展开。

## 核心议题

- 真实用户价值与从 Google 到安克的创业原点
- 一三五七、五系到七系，以及消费电子的速生速死
- 深海、浅海、品类选择和第三类公司
- 端到端声学、存算一体芯片与端侧模型
- 感知、规划、控制与真正智能的家居和机器人
- 长价值链、分层授权与创造者平台
- AI 中台、预编排智能体、中层管理和价值分配
- 技术、品牌、使命愿景价值观三层护城河

## 待补充

- [x] 通过发布者 RSS 标题、GUID、enclosure、简介与 OUTLINE 核对正式第 144 期
- [x] 核对 Bilibili BVID、aid、cid、page、发布者账号与单 P 完整播客映射
- [x] 检查匿名访问可见的平台字幕轨，且未绕过登录控制
- [x] 获取公开音轨并完成编码、时长、大小、媒体哈希与重新解码 PCM 承诺核验
- [x] 生成完整 Qwen3-ASR 机器逐字稿及 adaptive v2 产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 人工核听开场姓名和公司介绍、中英混说、说话人切换与长句边界，以及末句停在 `03:37:25`、距离音频端点约 7.2 秒的收尾；确认空白是否为正常片尾
- [ ] 校正机器稿中的系统性或疑似近音异写，尤其“杨蒙”应按来源核为“阳萌”、“安客/安科”、具身/“巨深”、存算一体/“成串一体/纯创意体”、拓竹/“拓主”、影石/“insa”、Scrum/“Squarm”等；逐一核对张小珺、阳萌、赵东平、Ray/Raymond Mooney、Jeff Dean、Sanjay Ghemawat、陶冶、王滔、刘靖康、Jack Dorsey、Sam Altman、Ram Charan 等人名
- [ ] 核查公司、产品、方法和技术专名，尤其 Anker/安克创新、Google、Amazon、IDG、DeepSeek、智谱、华为 IPD、DJI/大疆、Bambu Lab/拓竹、Insta360/影石、Epson、Ring、AirPods Pro、SVM、Google File System、MapReduce、Bigtable、IoT、beamforming、NPU、MoE、冯·诺依曼架构、端侧模型、流程智能体、VLA、world model、TAO，以及机器稿中的“Open Call”“Squid/Stackit”等工具名和作“领导阶梯”的书名
- [ ] 回听并查证出生、求学、任职和创业年份，Google 奖项口径，三百万元启动资金、早期营收和销量、融资与上市时间线，市场规模、品类与产品线数量，研发/AI/员工人数，安防份额、芯片和模型参数、Token 与 AI 费用、分配比例、毛利率、员工收入、召回数量及损失；市值、财务、芯片首创性、产品性能、同行评价、岗位变化和未来路线均保持为嘉宾陈述或录制时判断
