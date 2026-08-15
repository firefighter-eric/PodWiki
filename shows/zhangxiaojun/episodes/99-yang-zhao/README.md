---
schema_version: 1
kind: episode
id: "zhangxiaojun:99"
show_id: zhangxiaojun
episode_key: "99"
episode_number: 99
slug: 99-yang-zhao
release_type: regular
numbering:
  status: verified
  checked_at: 2026-08-09
  source: publisher-rss
  url: https://www.xiaoyuzhoufm.com/episode/680cd1378aed253fa3a5736b
title: "人类驯服可控核聚变还有多少路程？对能量奇点创始人杨钊3小时访谈"
navigation_title: "杨钊 · 可控核聚变商业化"
catalog_keyword: "可控核聚变"
published_at: "2025-06-18T19:46:40+08:00"
duration_ms: 9222594
language: zh-CN
participants:
  - id: zhang-xiaojun
    name: 张小珺
    role: host
  - id: yang-zhao
    name: 杨钊
    role: guest
sources:
  - platform: xiaoyuzhou
    kind: episode
    title: "99. 对能量奇点创始人杨钊3小时访谈：人类驯服可控核聚变还有多少路程？"
    url: https://www.xiaoyuzhoufm.com/episode/680cd1378aed253fa3a5736b
    preferred: false
    identifiers:
      eid: 680cd1378aed253fa3a5736b
      pid: 626b46ea9cbbf0451cf5a962
      media_id: 626b46ea9cbbf0451cf5a962/lpfMu_I9XS-X21W8dt1zz23bpA0y.m4a
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 680cd1378aed253fa3a5736b
  - platform: bilibili
    kind: video
    title: "人类驯服可控核聚变还有多少路程？对能量奇点创始人杨钊3小时访谈"
    url: https://www.bilibili.com/video/BV17sNEz2ER8/
    preferred: true
    identifiers:
      bvid: BV17sNEz2ER8
      aid: "114704114519888"
      cid: "30564680913"
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
    sha256: 791e0aeadc0b4f05aef06c38314aa416a5911e5d67653f95c0d27297e395536b
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
    planned_chunk_count: 39
    final_leaf_chunk_count: 39
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 159744
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: "2026-08-09T23:44:31.827122Z"
  quality:
    source_chunks: 39
    aligned_chunks: 39
    alignment_items: 50238
    sentence_segments: 1298
    refined_segments: 1298
    rendered_blocks: 314
    rendered_lines: 1298
  performance:
    model_load_seconds: 0.182
    transcription_seconds: 423.166
    prompt_tokens: 120599
    generation_tokens: 33148
    attempt_prompt_tokens: 120599
    attempt_generation_tokens: 33148
    generation_call_count: 39
    prompt_tokens_per_second: 284.992
    generation_tokens_per_second: 78.333
    aligner_load_seconds: 0.144
    alignment_seconds: 64.547
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
    generated_at: "2026-08-09T23:44:31.827122Z"
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/99-yang-zhao/source.m4a
  metadata_path: .cache/media/zhangxiaojun/99-yang-zhao/source.metadata.json
  git_ignored: true
  acquired_at: "2026-08-09T12:36:25.960348Z"
  verified_at: "2026-08-09T12:36:25.960348Z"
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 88285683
  duration_ms: 9222594
  sha256: c2d56a1f27c42a2b8712f20c36d78e31f929044b165dcdf364fceb13e7879065
last_verified_at: 2026-08-09
---

# 人类驯服可控核聚变还有多少路程？对能量奇点创始人杨钊 3 小时访谈

> 本页保留发布者标题、简介与章节形成的概览，并已基于完整 Qwen3-ASR 机器逐字稿形成独立总结草稿；逐字稿与总结均未完成人工审核。正式期号只取自发布者 RSS，不按 Bilibili 标题或导入顺序推断。

## 单集信息

- 节目：张小珺商业访谈录 #99
- 主持人：张小珺
- 嘉宾：杨钊
- Bilibili 发布时间：2025-06-18 19:46:40（UTC+8）
- Bilibili 视频音轨时长：02:33:42.594；官方 RSS 音频时长：02:34:35
- 来源：[发布者 RSS 单集页](https://www.xiaoyuzhoufm.com/episode/680cd1378aed253fa3a5736b)、[Bilibili 视频](https://www.bilibili.com/video/BV17sNEz2ER8/)
- 来源状态：公开单 P；匿名状态下平台返回空 tracks 并提示需要登录才能进一步检查，未取得匿名公开字幕轨；未使用 cookies 或登录态，且未绕过访问控制；规范本地音频及 media sidecar 已完成身份、大小、时长与 SHA-256 核验
- 完整性核验：发布者 RSS 将本期明确列为《张小珺商业访谈录》第 99 期，标题、嘉宾与主题和同一发布者账号上传的 Bilibili 单 P 一致；冻结 manifest 将 `BV17sNEz2ER8` 精确映射到该 RSS 条目。发布者简介明确称“这集节目”邀请能量奇点创始人杨钊，并把内容称为“我们的播客节目”；章节从 `00:03:00` 连续延伸至 `02:30:57`，Bilibili 音轨还包含片头、快问快答与节目收尾，支持其为完整官方视频播客版而非片段、高光、课程、演讲或直播回放。RSS 与本地视频音轨时长相差约 52.406 秒；本集没有专用跨平台声学抽样证据，因此该映射不证明两端逐句相同，也不据此推断具体剪辑差异
- 本地音频：AAC、44.1 kHz、双声道、88,285,683 字节
- 正式期号：发布者 RSS 标题明确标注 `99.`，GUID 为 `680cd1378aed253fa3a5736b`；Bilibili 标题没有期号，未据其反推编号
- 逐字稿：[Qwen3-ASR 机器初稿](./transcript.zh-CN.md)
- 总结：[基于完整机器稿的总结草稿](./summary.zh-CN.md)
- 当前状态：机器逐字稿与独立总结草稿均已生成，等待人工核听

## 内容概览

杨钊从裂变、聚变、磁约束、托卡马克、Q 值与三乘积讲起，解释能量奇点为何把高温超导材料视为缩小装置、降低度电成本的一条候选路径，并区分科学可行性、工程可行性和商业可行性。

访谈随后沿着洪荒 70、洪荒 170、洪荒 380 与经天磁体展开，讨论完整装置怎样从物理设计走到制造和联调、创业公司为何选择关键系统自研，以及资本、人才、交付能力和长期成本怎样共同决定核聚变商业化的进度。

## 核心议题

- 从核聚变基础概念到 Q 值、三乘积与托卡马克路线
- 高温超导磁体的小型化与降本假设
- 洪荒 70、洪荒 170、洪荒 380 的分阶段验证逻辑
- 非标复杂设备的设计、制造、联调与问题定位
- 聚变度电成本、长期运行、燃料路线与商业化边界
- AI 与能源需求、团队建设、融资耐心和创业失败条件

## 待补充

- [x] 通过发布者 RSS 标题、GUID、enclosure、简介与章节核对正式第 99 期
- [x] 核对 Bilibili BVID、aid、cid、page、发布者账号与单 P 完整播客映射
- [x] 检查匿名状态的平台字幕轨，且未使用登录态或绕过访问控制
- [x] 获取公开音轨并完成编码、时长、大小、媒体哈希与重新解码 PCM 承诺核验
- [x] 生成完整 Qwen3-ASR 机器逐字稿及 adaptive v2 产物哈希链
- [x] 基于完整机器稿形成独立总结草稿
- [ ] 人工核听冷开场、主持人与嘉宾的快速轮换、专业名词密集段落，以及最后一条对齐在 `02:33:07.429` 结束、距离 `02:33:42.594` 音频端点约 35.165 秒的收尾；确认该尾段是否仅为音乐或还含未对齐语音，并校正“张小军”“杨昭”“能量起点”“刀/穿”“红方/国光/红黄”“今天磁体”等明显或疑似近音误识别
- [ ] 核查人名、机构、装置、公司与技术专名，尤其张小珺、杨钊、能量奇点、洪荒 70、洪荒 170、洪荒 380、经天磁体、ITER、EAST、KSTAR、JT-60SA、NIF、SPARC、CFS、MIT、Helion Energy、FRC、DeepMind，以及氘、氚、托卡马克、高温超导、Q 值、三乘积等
- [ ] 回听并查证 Q 值和三乘积口径、磁场与尺寸定标率、ITER 的资金和工期、装置数量与纪录、21.7/23/29 特斯拉、洪荒 70/170/380 的成本与功率、2027 与 2030—2035 路线图、公司估值和融资额、团队人数，以及氘氘和氘氚反应条件等数字
- [ ] 高影响事实需核验高温超导路线的降本幅度、洪荒 70 和经天磁体的“全球第一/最高”说法、与 CFS/Helion 等路线的比较、Q≥10 与示范电站时间预测、度电成本与监管判断、放射性和安全边界、AI 能耗趋势、投资人与融资信息；不得把节目中的公司口径、竞品评价或未来预测直接视为独立事实
