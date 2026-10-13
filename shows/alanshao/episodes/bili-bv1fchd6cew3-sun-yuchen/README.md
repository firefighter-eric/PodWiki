---
schema_version: 1
kind: episode
id: alanshao:bili-bv1fchd6cew3
show_id: alanshao
episode_key: bili-bv1fchd6cew3
episode_number: null
slug: bili-bv1fchd6cew3-sun-yuchen
release_type: regular
numbering:
  status: unknown
  checked_at: '2026-10-13'
  source: publisher-page
title: 对话孙宇晨：年轻人如何抓住AI时代的机会？
navigation_title: 孙宇晨 · AI时代的机会与人生选择
catalog_keyword: AI机会
published_at: '2026-10-10T12:00:00+08:00'
duration_ms: 15749337
language: zh-CN
participants:
  - id: alan-shao
    name: 邵艾伦
    aliases:
      - Alan
    role: host
  - id: sun-yuchen
    name: 孙宇晨
    aliases:
      - Justin Sun
    role: guest
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1fcHD6cEw3/
    title: 对话孙宇晨：年轻人如何抓住AI时代的机会？
    preferred: true
    identifiers:
      bvid: BV1fcHD6cEw3
      aid: '117403434486720'
      cid: '42651419955'
      page: 1
  - platform: xiaoyuzhou
    kind: episode
    url: https://www.xiaoyuzhoufm.com/episode/6aca25e3e742e36efcc0ebfd
    preferred: false
    identifiers:
      eid: 6aca25e3e742e36efcc0ebfd
      pid: 6ac9b4c0ea31d4852ed6bf04
      media_id: 6ac9b4c0ea31d4852ed6bf04/li2QS6klD60mcLTGLVFrnHlWmZEk.m4a
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
    sha256: 540eaa02fe2835c67a202b3278d8e5781f976f64abeee674465bb0ed5f32f983
transcript:
  path: transcript.zh-CN.md
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
    planned_chunk_count: 66
    final_leaf_chunk_count: 66
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 270336
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: '2026-10-13T05:47:29.652231Z'
  access_context: anonymous
  quality:
    source_chunks: 66
    aligned_chunks: 66
    alignment_items: 73166
    sentence_segments: 2254
    source_segments: 2254
    refined_segments: 2254
    rendered_blocks: 535
    rendered_lines: 2254
  performance:
    model_load_seconds: 0.205
    transcription_seconds: 549.602
    prompt_tokens: 205934
    generation_tokens: 54016
    attempt_prompt_tokens: 205934
    attempt_generation_tokens: 54016
    generation_call_count: 66
    prompt_tokens_per_second: 374.697
    generation_tokens_per_second: 98.282
    aligner_load_seconds: 0.217
    alignment_seconds: 81.087
  translations: []
  platform_subtitle_access: authenticated-seen-user-selected-asr
  platform_subtitle_languages:
    - zh-CN
  processing_choice:
    requested_at: '2026-10-13'
    basis: explicit-user-request-for-local-asr-after-subtitle-capture-blocker
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
  - id: qwen3-asr
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    generated_at: '2026-10-13T05:47:29.652231Z'
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  size_bytes: 224212019
  duration_ms: 15749337
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  sha256: fec88016772a47da622260c30f81150573a20b9e67979cb0fdcc337cef93a3c4
  path: .cache/media/alanshao/bili-bv1fchd6cew3-sun-yuchen/source.m4a
  metadata_path: .cache/media/alanshao/bili-bv1fchd6cew3-sun-yuchen/source.metadata.json
  git_ignored: true
  acquired_at: '2026-10-13T01:33:40.453566Z'
  verified_at: '2026-10-13T01:33:40.453566Z'
last_verified_at: '2026-10-13'
---

# 对话孙宇晨：年轻人如何抓住AI时代的机会？

> 正式稿来自本地固定版本 Qwen3-ASR 与 ForcedAligner，为 `machine`；基于完整正式稿的总结为 `draft`，尚未完成人工审核。

## 单集信息

- 嘉宾：孙宇晨。主持人：邵艾伦 Alan。
- 总结：[查看总结](./summary.zh-CN.md)
- 正式逐字稿：[查看中文逐字稿](./transcript.zh-CN.md)
- 原始节目：[Bilibili 完整单集](https://www.bilibili.com/video/BV1fcHD6cEw3/) · [小宇宙同集](https://www.xiaoyuzhoufm.com/episode/6aca25e3e742e36efcc0ebfd)
- 发布者未给出正式期号，使用 BVID 稳定键。

## 处理记录

- 完整公开音频已核对 BVID／aid／cid、文件大小、时长与 SHA-256；本集共 66 个转写及对齐 chunk，正式稿为 2,254 段。
- 上一任务在已授权的 Bilibili 登录态播放器确认中文 AI 字幕，但采集通道未能保存响应正文。2026-10-13 用户明确要求改用本地 ASR；该选择仅适用于本集，不改变其他单集的字幕优先规则。
- 使用 Apple Silicon／MLX 专用 ASR 与 ForcedAligner，复用共享模型，通过固定 revision、逐文件身份和 raw → aligned → refined → 正式稿的哈希链校验。
- 发布者明确的主持人姓名与薄肌主题通过本集 `asr/corrections.json` 做确定性校正，保留原始 raw 和 aligned，不视为全文人工审核。
- 总结依据完整所选逐字稿及本地 LM Studio 连续编辑笔记，所有正文时间码绑定所选稿。

## 待审核

- 回听核对说话人、专有名词、数字、否定词、长句和时间戳。
- 对健康、药物、心理困扰、投资和收益、科研成果以及人物经历完成必要的独立事实核查。
- 人工审核总结中的发言归属、论据与限制条件。
