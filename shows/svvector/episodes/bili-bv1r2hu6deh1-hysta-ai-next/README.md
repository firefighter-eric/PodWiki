---
schema_version: 1
kind: episode
id: svvector:bili-bv1r2hu6deh1
show_id: svvector
episode_key: bili-bv1r2hu6deh1
episode_number: null
slug: bili-bv1r2hu6deh1-hysta-ai-next
release_type: special
numbering:
  status: not-in-publisher-feed
  checked_at: '2026-10-23'
  source: publisher-page
title: 【硅谷坐标 × 华源HYSTA 特别节目】：AI 的下一程：对话11 位硅谷顶级AI从业者
navigation_title: 李严冰、Ion Stoica、Ed H. Chi、Bill Jia、乔琳、Li Fan、Dawn Song、贾扬清、田渊栋、葛小川、Connie Chan · AI规模化的分歧与边界
catalog_keyword: AI规模化
published_at: '2026-10-08T07:00:56+08:00'
duration_ms: 2702059
language: zh-CN
participants:
  - id: li-yanbing
    name: 李严冰
    aliases: []
    role: guest
  - id: ion-stoica
    name: Ion Stoica
    aliases: []
    role: guest
  - id: ed-chi
    name: Ed H. Chi
    aliases: []
    role: guest
  - id: bill-jia
    name: Bill Jia
    aliases: []
    role: guest
  - id: qiao-lin
    name: 乔琳
    aliases: []
    role: guest
  - id: li-fan
    name: Li Fan
    aliases: []
    role: guest
  - id: dawn-song
    name: Dawn Song
    aliases: []
    role: guest
  - id: jia-yangqing
    name: 贾扬清
    aliases: []
    role: guest
  - id: tian-yuandong
    name: 田渊栋
    aliases: []
    role: guest
  - id: ge-xiaochuan
    name: 葛小川
    aliases: []
    role: guest
  - id: connie-chan
    name: Connie Chan
    aliases: []
    role: guest
  - id: cao-qingyun
    name: 曹卿云
    aliases: []
    role: host
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1R2HU6DEh1/
    preferred: true
    title: 【硅谷坐标 × 华源HYSTA 特别节目】：AI 的下一程：对话11 位硅谷顶级AI从业者
    identifiers:
      bvid: BV1R2HU6DEh1
      aid: '117402092181727'
      cid: '42552395630'
      page: 1
  - platform: xiaoyuzhou
    kind: episode
    url: https://www.xiaoyuzhoufm.com/episode/6ad5afbc0e4e410a05bf02fe
    preferred: false
    title: AI 的下一程：对话 11 位硅谷顶级 AI 从业者｜硅谷坐标 × 华源 HYSTA 特别节目
    identifiers:
      eid: 6ad5afbc0e4e410a05bf02fe
      pid: 69a4b82b27e15c06061cfc2d
      media_id: 69a4b82b27e15c06061cfc2d/llxNJtj_-QZWdmltGglPzl22FS9t.m4a
workflow:
  metadata: verified
  summary: draft
  transcript: machine
summary_basis:
  - complete-machine-transcript
summary:
  path: summary.zh-CN.md
  language: zh-CN
  source_transcript:
    path: transcript.zh-CN.md
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    selection_status: selected
    sha256: 3a8943c3536edfeed1ec81979d8c766fbc7224e237096540578f783f921ddbe6
transcript:
  path: transcript.zh-CN.md
  translations: []
  acquisition_method: audio-asr
  asr_script: scripts/transcribe_qwen3_asr.py
  engine: mlx-audio
  model: mlx-community/Qwen3-ASR-1.7B-8bit
  aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
  options:
    language: Chinese
    temperature: 0.0
    max_tokens_per_chunk: 4096
    chunk_duration_seconds: 240.0
    planned_chunk_count: 12
    final_leaf_chunk_count: 12
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 49152
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: '2026-10-23T15:20:48.202353Z'
  access_context: anonymous
  platform_subtitle_access:
    anonymous_tracks: []
    need_login: true
    authenticated_context: not-authorized-or-used
  quality:
    source_chunks: 12
    aligned_chunks: 12
    alignment_items: 10389
    sentence_segments: 369
    source_segments: 369
    refined_segments: 369
    rendered_blocks: 122
    rendered_lines: 369
  performance:
    model_load_seconds: 0.191
    transcription_seconds: 86.627
    prompt_tokens: 35342
    generation_tokens: 8180
    attempt_prompt_tokens: 35342
    attempt_generation_tokens: 8180
    generation_call_count: 12
    prompt_tokens_per_second: 407.979
    generation_tokens_per_second: 94.428
    aligner_load_seconds: 0.186
    alignment_seconds: 13.017
asr_runs:
  - id: qwen3-asr
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    generated_at: '2026-10-23T15:20:48.202353Z'
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 26257589
  duration_ms: 2702059
  sha256: d488968a304e417b5b6cfa597f4e338886cfc4b1f340309521a7b3febec689c5
  path: .cache/media/svvector/bili-bv1r2hu6deh1-hysta-ai-next/source.m4a
  metadata_path: .cache/media/svvector/bili-bv1r2hu6deh1-hysta-ai-next/source.metadata.json
  git_ignored: true
  acquired_at: '2026-10-23T15:14:26.892411Z'
  verified_at: '2026-10-23T15:14:26.892411Z'
last_verified_at: '2026-10-23'
asr_artifacts:
  raw:
    path: asr/qwen3-asr/raw.json
    git_ignored: false
    format: podwiki-raw-asr-json-v1
    sha256: c0d53d87d1f0a03fac213373ad12f50e1085870ed59c8164b64f6364201799d7
  aligned:
    path: asr/qwen3-asr/aligned.json
    git_ignored: false
    format: podwiki-aligned-asr-json-v1
    sha256: 9b380dc2be1fdb38d6d6fa0d62095761106cc8fc4b48ee300622eaaad7020d9a
  refined:
    path: asr/qwen3-asr/refined.json
    git_ignored: false
    format: podwiki-refined-asr-json-v1
    sha256: d6033b05b9b76b4ea2d480386592c47ca99fe540be0ae867a5f3d16969dae28e
  transcript:
    path: asr/qwen3-asr/transcript.zh-CN.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
    sha256: 3a8943c3536edfeed1ec81979d8c766fbc7224e237096540578f783f921ddbe6
  renderer: scripts/render_asr_transcript.py
---

# 【硅谷坐标 × 华源HYSTA 特别节目】：AI 的下一程：对话11 位硅谷顶级AI从业者

> 逐字稿由本地固定版本Qwen3-ASR与ForcedAligner生成，状态为`machine`；全文总结为`draft`。尚未完成逐段人工核听。

## 单集信息

- 总结：[查看全文总结](./summary.zh-CN.md)
- 正式逐字稿：[查看中文逐字稿](./transcript.zh-CN.md)
- 原始节目：[发布者完整单集](https://www.bilibili.com/video/BV1R2HU6DEh1/)

## 来源核验

- 官方发布者、公开免费单P、BVID/aid/cid/page与本地音频大小、时长和SHA-256均已核实。
- 与官方播客发布的嘉宾、内容主题、章节和完整时长对应；小宇宙仅作身份和同集交叉核对。
- 本次匿名上下文未发现可用字幕；没有使用登录态，也未把匿名检查解释为所有上下文均无字幕。

## 待审核

- 逐段核听人名、公司与模型名、数字、否定词及说话人归属。
- 对总结中的关键引文和高影响事实做必要的回听及独立核查；当前不得标为reviewed。
