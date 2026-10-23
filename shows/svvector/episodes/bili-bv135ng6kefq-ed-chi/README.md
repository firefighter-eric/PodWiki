---
schema_version: 1
kind: episode
id: svvector:bili-bv135ng6kefq
show_id: svvector
episode_key: bili-bv135ng6kefq
episode_number: null
slug: bili-bv135ng6kefq-ed-chi
release_type: regular
numbering:
  status: not-in-publisher-feed
  checked_at: '2026-10-23'
  source: publisher-page
title: 硅谷坐标 x 谷歌DeepMind研究副总裁 Ed H. Chi（纪怀新）：个性化通用助理的未来
navigation_title: Ed H. Chi · 通用助理、记忆与模型成本
catalog_keyword: 通用助理
published_at: '2026-10-18T13:12:24+08:00'
duration_ms: 1933205
language: zh-CN
participants:
  - id: ed-chi
    name: Ed H. Chi
    aliases: []
    role: guest
  - id: cao-qingyun
    name: 曹卿云
    aliases: []
    role: host
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV135ng6KEfQ/
    preferred: true
    title: 硅谷坐标 x 谷歌DeepMind研究副总裁 Ed H. Chi（纪怀新）：个性化通用助理的未来
    identifiers:
      bvid: BV135ng6KEfQ
      aid: '117460174905059'
      cid: '42838392905'
      page: 1
  - platform: xiaoyuzhou
    kind: episode
    url: https://www.xiaoyuzhoufm.com/episode/6ad5aa4b641ef406308dc7f3
    preferred: false
    title: 模型能力终将普及，AI 的终局是能力与成本之比｜对话 Google DeepMind 研究副总裁 Ed Chi
    identifiers:
      eid: 6ad5aa4b641ef406308dc7f3
      pid: 69a4b82b27e15c06061cfc2d
      media_id: 69a4b82b27e15c06061cfc2d/li168WAkOTdR_DADorbR5gqvjpya.m4a
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
    sha256: c74ddfc45e64401cb7005c705975dea81b88b7362319f7ffbdc8202f530b07e7
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
    planned_chunk_count: 9
    final_leaf_chunk_count: 9
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 36864
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: '2026-10-23T15:17:04.226872Z'
  access_context: anonymous
  platform_subtitle_access:
    anonymous_tracks: []
    need_login: true
    authenticated_context: not-authorized-or-used
  quality:
    source_chunks: 9
    aligned_chunks: 9
    alignment_items: 8285
    sentence_segments: 167
    source_segments: 167
    refined_segments: 167
    rendered_blocks: 71
    rendered_lines: 167
  performance:
    model_load_seconds: 0.277
    transcription_seconds: 60.943
    prompt_tokens: 25293
    generation_tokens: 5683
    attempt_prompt_tokens: 25293
    attempt_generation_tokens: 5683
    generation_call_count: 9
    prompt_tokens_per_second: 415.026
    generation_tokens_per_second: 93.251
    aligner_load_seconds: 0.162
    alignment_seconds: 9.386
asr_runs:
  - id: qwen3-asr
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    generated_at: '2026-10-23T15:17:04.226872Z'
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 21393775
  duration_ms: 1933205
  sha256: ef7b098319e44d94d030d1acacd4381654918005841bd7f8de4964583edae5e6
  path: .cache/media/svvector/bili-bv135ng6kefq-ed-chi/source.m4a
  metadata_path: .cache/media/svvector/bili-bv135ng6kefq-ed-chi/source.metadata.json
  git_ignored: true
  acquired_at: '2026-10-23T15:14:23.698252Z'
  verified_at: '2026-10-23T15:14:23.698252Z'
last_verified_at: '2026-10-23'
asr_artifacts:
  raw:
    path: asr/qwen3-asr/raw.json
    git_ignored: false
    format: podwiki-raw-asr-json-v1
    sha256: 2af4c29f036b3b9fd1f54c53e7d6b4c075d0251823846d811e0e94c38b17433d
  aligned:
    path: asr/qwen3-asr/aligned.json
    git_ignored: false
    format: podwiki-aligned-asr-json-v1
    sha256: e1fb2428986ed98fef0038cbda7dd733dc202c1fb5435cf56e91cc53842768e0
  refined:
    path: asr/qwen3-asr/refined.json
    git_ignored: false
    format: podwiki-refined-asr-json-v1
    sha256: 01c63de384aaa141703dba1f5b21d7b8ce749afa9859f8f717521c00d7a76fb7
  transcript:
    path: asr/qwen3-asr/transcript.zh-CN.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
    sha256: c74ddfc45e64401cb7005c705975dea81b88b7362319f7ffbdc8202f530b07e7
  renderer: scripts/render_asr_transcript.py
---

# 硅谷坐标 x 谷歌DeepMind研究副总裁 Ed H. Chi（纪怀新）：个性化通用助理的未来

> 逐字稿由本地固定版本Qwen3-ASR与ForcedAligner生成，状态为`machine`；全文总结为`draft`。尚未完成逐段人工核听。

## 单集信息

- 总结：[查看全文总结](./summary.zh-CN.md)
- 正式逐字稿：[查看中文逐字稿](./transcript.zh-CN.md)
- 原始节目：[发布者完整单集](https://www.bilibili.com/video/BV135ng6KEfQ/)

## 来源核验

- 官方发布者、公开免费单P、BVID/aid/cid/page与本地音频大小、时长和SHA-256均已核实。
- 与官方播客发布的嘉宾、内容主题、章节和完整时长对应；小宇宙仅作身份和同集交叉核对。
- 本次匿名上下文未发现可用字幕；没有使用登录态，也未把匿名检查解释为所有上下文均无字幕。

## 待审核

- 逐段核听人名、公司与模型名、数字、否定词及说话人归属。
- 对总结中的关键引文和高影响事实做必要的回听及独立核查；当前不得标为reviewed。
