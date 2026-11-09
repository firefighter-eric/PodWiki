---
schema_version: 1
kind: episode
id: latetalk:184
show_id: latetalk
episode_key: '184'
episode_number: 184
slug: 184-chen-zhe
release_type: regular
numbering:
  status: verified
  checked_at: '2026-11-08'
  source: https://podcast.latepost.com/184
title: 具身季报 26Q3：Astra 之后，重新划分物理 AI 与通用 AI 的边界【晚点聊LateTalk】
navigation_title: 陈哲 · 通用模型与物理AI的边界
catalog_keyword: 物理AI
published_at: '2026-10-29T03:02:33+00:00'
duration_ms: 6384582
language: zh-CN
participants:
  - id: chen-zhe
    name: 陈哲
    aliases: []
    role: guest
  - id: cheng-manqi
    name: 程曼祺
    aliases: []
    role: host
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1fdsR6SEVR/
    preferred: true
    title: 具身季报 26Q3：Astra 之后，重新划分物理 AI 与通用 AI 的边界【晚点聊LateTalk】
    identifiers:
      bvid: BV1fdsR6SEVR
      aid: '117521948678256'
      cid: '43140842797'
      page: 1
  - platform: rss
    kind: feed-item
    url: https://podcast.latepost.com/184
    preferred: false
    title: 与陈哲的「具身季报26Q3」：Astra冲击后，通用模型会吃掉Robotics吗？
    identifiers:
      guid: 1ba74c4b-43e4-416c-aafe-f191fcb44898
      feed_url: https://podcast.latepost.com/rss
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
    sha256: 5459e8cc0d43c562edd12c05c17e7e206390d2fb987b1180aa493816e9224143
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
    planned_chunk_count: 27
    final_leaf_chunk_count: 27
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 110592
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: '2026-11-08T15:53:55.414326Z'
  access_context: authenticated-subtitle-check-public-audio
  platform_subtitle_access:
    anonymous_tracks: []
    need_login: false
    authenticated_context: checked-no-subtitle-control-or-track
  quality:
    source_chunks: 27
    aligned_chunks: 27
    alignment_items: 33446
    sentence_segments: 758
    source_segments: 758
    refined_segments: 758
    rendered_blocks: 217
    rendered_lines: 758
  performance:
    model_load_seconds: 0.395
    transcription_seconds: 234.003
    prompt_tokens: 83488
    generation_tokens: 21829
    attempt_prompt_tokens: 83488
    attempt_generation_tokens: 21829
    generation_call_count: 27
    prompt_tokens_per_second: 356.782
    generation_tokens_per_second: 93.285
    aligner_load_seconds: 0.219
    alignment_seconds: 35.408
asr_runs:
  - id: qwen3-asr
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    generated_at: '2026-11-08T15:53:55.414326Z'
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 74830590
  duration_ms: 6384582
  sha256: 547f0eb552382993c0752f707b811459408d82e954199b17d03baf830ef7fdc6
  path: .cache/media/latetalk/184-chen-zhe/source.m4a
  metadata_path: .cache/media/latetalk/184-chen-zhe/source.metadata.json
  git_ignored: true
  acquired_at: '2026-11-08T15:40:45.305294Z'
  verified_at: '2026-11-08T15:40:45.305294Z'
last_verified_at: '2026-11-08'
asr_artifacts:
  raw:
    path: asr/qwen3-asr/raw.json
    git_ignored: false
    format: podwiki-raw-asr-json-v1
    sha256: 195ab47c3cf8186390d74e7279dd163b6f07719bacfe6cdf8daef8d2e8e798b2
  aligned:
    path: asr/qwen3-asr/aligned.json
    git_ignored: false
    format: podwiki-aligned-asr-json-v1
    sha256: 9b8bb84a18ead08ddecf04ac4fcaa89c73563f7b600ebb5da925ef4fd95ce804
  refined:
    path: asr/qwen3-asr/refined.json
    git_ignored: false
    format: podwiki-refined-asr-json-v1
    sha256: 759a8d5f59ca80eefbbb2529fc802e9ced66d1c01292141463f299f5adde34fd
  transcript:
    path: asr/qwen3-asr/transcript.zh-CN.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
    sha256: 5459e8cc0d43c562edd12c05c17e7e206390d2fb987b1180aa493816e9224143
  renderer: scripts/render_asr_transcript.py
---

# 具身季报 26Q3：Astra 之后，重新划分物理 AI 与通用 AI 的边界【晚点聊LateTalk】

> 逐字稿由本地固定版本Qwen3-ASR与ForcedAligner生成，状态为`machine`；全文总结为`draft`。尚未完成逐段人工核听。

## 单集信息

- 总结：[查看全文总结](./summary.zh-CN.md)
- 正式逐字稿：[查看中文逐字稿](./transcript.zh-CN.md)
- 原始节目：[发布者完整单集](https://www.bilibili.com/video/BV1fdsR6SEVR/)

## 来源核验

- 官方发布者、公开免费单P、BVID/aid/cid/page与本地音频大小、时长和SHA-256均已核实。
- 播客完整性由官方RSS同集映射或官方播客正片合集核实；实际输入来自批准的B站正片。
- 本机已登录Chrome完整播放界面未提供可用字幕控件或轨道；随后使用匿名公开免费音轨进行本地ASR。

## 待审核

- 逐段核听人名、公司与模型名、数字、否定词及说话人归属。
- 对总结中的关键引文和高影响事实做必要的回听及独立核查；当前不得标为reviewed。
