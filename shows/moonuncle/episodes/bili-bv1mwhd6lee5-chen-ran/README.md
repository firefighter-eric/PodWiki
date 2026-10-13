---
schema_version: 1
kind: episode
id: moonuncle:bili-bv1mwhd6lee5
show_id: moonuncle
episode_key: bili-bv1mwhd6lee5
episode_number: null
slug: bili-bv1mwhd6lee5-chen-ran
release_type: regular
numbering:
  status: unknown
  checked_at: '2026-10-14'
  source: https://www.bilibili.com/video/BV1MWHD6LEE5/
title: 陈然：全职奶爸，清华，CMU，AI斩杀线，0人公司，百亿token，财务规划，职业选择，创业收购，主体性，硅谷
navigation_title: 陈然 · 零人公司与人生主体性
catalog_keyword: 零人公司
published_at: '2026-10-08T03:38:31Z'
duration_ms: 6975065
language: zh-CN
participants:
  - id: chenran
    name: 陈然
    aliases: []
    role: guest
  - id: moonuncle
    name: 月球大叔
    aliases: []
    role: host
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1MWHD6LEE5/
    preferred: true
    title: 陈然：全职奶爸，清华，CMU，AI斩杀线，0人公司，百亿token，财务规划，职业选择，创业收购，主体性，硅谷
    identifiers:
      bvid: BV1MWHD6LEE5
      aid: '117403182700721'
      cid: '42548462880'
      page: 1
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
    sha256: 49cfbb50ce53984542708d275d9451befe2b8b0121409fae7d61bbb460e170af
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
    planned_chunk_count: 30
    final_leaf_chunk_count: 30
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 122880
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: '2026-10-13T17:39:50.416802Z'
  quality:
    source_chunks: 30
    aligned_chunks: 30
    alignment_items: 37042
    sentence_segments: 1065
    source_segments: 1065
    refined_segments: 1065
    rendered_blocks: 235
    rendered_lines: 1065
  performance:
    model_load_seconds: 0.182
    transcription_seconds: 284.426
    prompt_tokens: 91218
    generation_tokens: 25215
    attempt_prompt_tokens: 91218
    attempt_generation_tokens: 25215
    generation_call_count: 30
    prompt_tokens_per_second: 320.709
    generation_tokens_per_second: 88.652
    aligner_load_seconds: 0.14
    alignment_seconds: 47.04
  access_context: anonymous
asr_runs:
  - id: qwen3-asr
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    generated_at: '2026-10-13T17:39:50.416802Z'
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/moonuncle/bili-bv1mwhd6lee5-chen-ran/source.m4a
  metadata_path: .cache/media/moonuncle/bili-bv1mwhd6lee5-chen-ran/source.metadata.json
  git_ignored: true
  size_bytes: 95711624
  duration_ms: 6975065
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  sha256: 80fb803c0f9dd9829161a849353d8f0b88e55f332a7e6768e082667a18f69384
  verified_at: '2026-10-13T17:13:13.073667Z'
  acquired_at: '2026-10-13T17:13:13.073667Z'
last_verified_at: '2026-10-14'
asr_artifacts:
  raw:
    path: asr/qwen3-asr/raw.json
    git_ignored: false
    format: podwiki-raw-asr-json-v1
    sha256: 9635b5303baedb82d173737009a0ddffbef7fb64c35f416198b93eff0d959774
  aligned:
    path: asr/qwen3-asr/aligned.json
    git_ignored: false
    format: podwiki-aligned-asr-json-v1
    sha256: cdd797d5f473ceea5ef4f20ab30be054ae977e4cb153a2e0f72184a698b38a53
  refined:
    path: asr/qwen3-asr/refined.json
    git_ignored: false
    format: podwiki-refined-asr-json-v1
    sha256: f8958ff946d92d0015776736cef9d83d7b8312231de831ccf8827469ad560b7d
  transcript:
    path: asr/qwen3-asr/transcript.zh-CN.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
    sha256: 49cfbb50ce53984542708d275d9451befe2b8b0121409fae7d61bbb460e170af
  renderer: scripts/render_asr_transcript.py
---

# 陈然：全职奶爸，清华，CMU，AI斩杀线，0人公司，百亿token，财务规划，职业选择，创业收购，主体性，硅谷

> 中文逐字稿由本地 Qwen3-ASR 与 ForcedAligner 生成，保持 machine 状态。

## 单集信息

- 来源：[BV1MWHD6LEE5](https://www.bilibili.com/video/BV1MWHD6LEE5/)

## 内容概览

已完成本地机器逐字稿；完整内容总结依据当前所选中文稿。

## 完整逐字稿

- [查看中文逐字稿](./transcript.zh-CN.md)

## 完整总结

- [查看中文总结](./summary.zh-CN.md)
