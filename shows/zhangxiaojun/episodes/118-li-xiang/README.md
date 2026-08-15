---
schema_version: 1
kind: episode
id: "zhangxiaojun:118"
show_id: zhangxiaojun
episode_key: "118"
episode_number: 118
slug: 118-li-xiang
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-09
  source: publisher-rss
  url: https://www.xiaoyuzhoufm.com/episode/6902c5f7abb5e1cf581296be
title: "对李想的第二次3小时访谈：CEO大模型、MoE、梁文锋、VLA、能量、记忆、对抗人性、亲密关系、人类的智慧"
navigation_title: "李想 · CEO 大模型、VLA 与组织"
catalog_keyword: "CEO大模型"
published_at: "2025-10-30T11:20:42+08:00"
duration_ms: 9832048
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: li-xiang
    name: 李想
    role: guest
sources:
  - platform: xiaoyuzhou
    kind: episode
    title: "118. 对李想的第二次3小时访谈：CEO大模型、MoE、梁文锋、VLA、能量、记忆、对抗人性、亲密关系、人类的智慧"
    url: https://www.xiaoyuzhoufm.com/episode/6902c5f7abb5e1cf581296be
    preferred: false
    identifiers:
      eid: 6902c5f7abb5e1cf581296be
      pid: 626b46ea9cbbf0451cf5a962
      media_id: 626b46ea9cbbf0451cf5a962/llLlRNWTyHSulV2QFLv5NBUAamP4.m4a
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 6902c5f7abb5e1cf581296be
  - platform: bilibili
    kind: video
    title: "对李想的第二次3小时访谈：CEO大模型、MoE、梁文锋、VLA、能量、记忆、对抗人性、亲密关系、人类的智慧"
    url: https://www.bilibili.com/video/BV1fiybB4EDU/
    preferred: true
    identifiers:
      bvid: BV1fiybB4EDU
      aid: "115460884530838"
      cid: "33514455594"
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
    sha256: 63d8d7647123878d5989a938b3b4259409f85e1b993616747341f0484b0606ab
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
    planned_chunk_count: 41
    final_leaf_chunk_count: 41
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 167936
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: "2026-08-09T22:16:53.371508Z"
  quality:
    source_chunks: 41
    aligned_chunks: 41
    alignment_items: 52906
    sentence_segments: 1605
    refined_segments: 1605
    rendered_blocks: 330
    rendered_lines: 1605
  performance:
    model_load_seconds: 0.184
    transcription_seconds: 446.455
    prompt_tokens: 128560
    generation_tokens: 35348
    attempt_prompt_tokens: 128560
    attempt_generation_tokens: 35348
    generation_call_count: 41
    prompt_tokens_per_second: 287.957
    generation_tokens_per_second: 79.175
    aligner_load_seconds: 0.151
    alignment_seconds: 67.738
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
    generated_at: "2026-08-09T22:16:53.371508Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/118-li-xiang/source.m4a
  metadata_path: .cache/media/zhangxiaojun/118-li-xiang/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-09T12:34:14.254014Z"
  verified_at: "2026-08-09T12:34:14.254014Z"
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 89422808
  duration_ms: 9832048
  sha256: 660d169c4520dfdf29516f828db6ba39708225a84b26262bbb3045ddcb018041
last_verified_at: 2026-08-09
---

# 对李想的第二次 3 小时访谈：CEO 大模型、MoE、梁文锋、VLA、能量、记忆、对抗人性、亲密关系、人类的智慧

> 本页保留发布者简介与章节形成的概览，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。

## 单集信息

- 节目：张小珺商业访谈录 #118
- 主持人：张小珺
- 嘉宾：李想
- Bilibili 发布时间：2025-10-30 11:20:42（UTC+8）
- Bilibili 视频时长：02:43:52；官方 RSS 音频时长：02:46:22
- RSS 正式标题：对李想的第二次 3 小时访谈：CEO 大模型、MoE、梁文锋、VLA、能量、记忆、对抗人性、亲密关系、人类的智慧
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/6902c5f7abb5e1cf581296be)、[Bilibili 视频](https://www.bilibili.com/video/BV1fiybB4EDU/)
- 来源状态：公开单 P；匿名状态未取得公开字幕轨，平台返回 `need_login: true` 与空 tracks；未登录且未绕过访问控制；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 完整性核验：发布者在 Bilibili 简介中明确称此前播出版仅 1 小时、当前上传为“完整版”，并说明本集同步上线小宇宙音频与 Bilibili 视频；冻结 manifest 将该 BVID 映射到 RSS 第 118 期，记录两版时长相差约 149.934 秒。发布者 RSS 还列出四章、从 CEO 大模型贯穿至亲密关系和人类智慧，本地所选音轨也从开场提问连续覆盖到最终 AI 与人的讨论。上述证据支持将 Bilibili 音轨视为完整官方视频播客版，而非片段或高光。本集没有专用跨平台声学抽样证据；映射不证明 Bilibili 与 RSS 逐句相同，也不据此推断具体内容差异
- 本地音频：AAC、44.1 kHz、双声道、89,422,808 字节
- 正式期号：发布者 RSS 标题明确标注 `118.`，GUID 为 `6902c5f7abb5e1cf581296be`
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

张小珺把李想当作一个“CEO 大模型”，依次调用技术、战略和组织专家：从 AI 工具的分级、DeepSeek 与人类最佳实践，深入到 VLA 司机大模型、世界模型和专业 Agent；再讨论理想如何从汽车公司走向人工智能终端企业，最后回到能量、记忆、家庭、亲密关系和人类智慧。

## 核心议题

- 信息、辅助与生产工具，以及专业 Agent 的判断标准
- DeepSeek、基座模型、VLA、世界模型与自动驾驶安全
- 规模、用户需求、技术产品和组织能力的战略联动
- 人工智能终端、软件硬件服务与未来产品边界
- 三至七人能量体、家庭支持、亲密关系与智慧

## 待补充

- [x] 通过发布者 RSS 标题、GUID、enclosure 与时长核对正式第 118 期
- [x] 核对 Bilibili BVID、aid、cid、page 与发布者账号
- [x] 检查匿名状态的平台字幕轨，且未绕过登录控制
- [x] 获取公开音轨并完成编码、时长、大小和哈希核验
- [x] 生成完整 Qwen3-ASR 机器逐字稿及 adaptive v2 产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 核听中英文专名、模型与芯片型号、多人衔接和识别错误，并核查自动驾驶安全与分级、模型参数和训练数据、成本效率、销量收入、组织人员、投资开源、家庭与其他高影响事实
