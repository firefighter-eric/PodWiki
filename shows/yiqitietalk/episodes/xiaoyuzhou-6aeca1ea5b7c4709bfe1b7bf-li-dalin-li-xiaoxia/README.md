---
schema_version: 1
kind: "episode"
id: "yiqitietalk:xiaoyuzhou-6aeca1ea5b7c4709bfe1b7bf"
show_id: "yiqitietalk"
episode_key: "xiaoyuzhou-6aeca1ea5b7c4709bfe1b7bf"
episode_number: null
slug: "xiaoyuzhou-6aeca1ea5b7c4709bfe1b7bf-li-dalin-li-xiaoxia"
release_type: "regular"
numbering:
  status: "unknown"
  checked_at: "2026-11-08"
  source: "publisher-page"
  url: "https://www.xiaoyuzhoufm.com/episode/6aeca1ea5b7c4709bfe1b7bf"
  note: "原标题数字标签保留在来源中；未取得独立正式期号字段，使用 eid 稳定键，不按列表位置推断。"
title: "24 李大林：被说“捡漏”后北马再夺冠。扬眉吐气的李大林与晓霞，背后经历了什么？"
navigation_title: "李大林、李晓霞 · 两人团队与马拉松成长"
catalog_keyword: "两人团队"
published_at: "2026-11-05T23:49:24.967000+08:00"
duration_ms: 8209200
language: "zh-CN"
participants:
  - id: "li-dalin"
    name: "李大林"
    aliases: []
    role: "guest"
  - id: "li-xiaoxia"
    name: "李晓霞"
    aliases: []
    role: "guest"
  - id: "sun-ruiyi"
    name: "孙瑞一"
    aliases: []
    role: "host"
  - id: "wu-xiangdong"
    name: "吴向东"
    aliases: []
    role: "host"
sources:
  - platform: "xiaoyuzhou"
    kind: "episode"
    title: "24 李大林：被说“捡漏”后北马再夺冠。扬眉吐气的李大林与晓霞，背后经历了什么？"
    url: "https://www.xiaoyuzhoufm.com/episode/6aeca1ea5b7c4709bfe1b7bf"
    preferred: true
    identifiers:
      eid: "6aeca1ea5b7c4709bfe1b7bf"
      pid: "6951e312febad13106eb017e"
      media_id: "6951e312febad13106eb017e/loY93jA5uMbXWAPEH3F6v8uk7ryX.m4a"
workflow:
  metadata: "verified"
  summary: "draft"
  transcript: "machine"
summary_basis:
  - "publisher-description"
  - "publisher-chapters"
  - "complete-machine-transcript"
summary:
  path: "summary.zh-CN.md"
  language: "zh-CN"
  source_transcript:
    path: "transcript.zh-CN.md"
    engine: "qwen-asr-transformers"
    model: "Qwen/Qwen3-ASR-1.7B-hf"
    selection_status: "selected"
    sha256: "f2f59e781e4bf81ef5eb074cfe51b4b2431fd26dfc4f002f12710b0cdee1b08e"
transcript:
  path: "transcript.zh-CN.md"
  translations: []
  platform_subtitle_access: "no-anonymous-track"
  platform_subtitle_languages: []
  automatic_caption_languages: []
  acquisition_method: "audio-asr"
  asr_script: "scripts/transcribe_qwen3_asr_cuda.py"
  engine: "qwen-asr-transformers"
  model: "Qwen/Qwen3-ASR-1.7B-hf"
  aligner: "Qwen/Qwen3-ForcedAligner-0.6B-hf"
  options:
    language: "Chinese"
    temperature: 0.0
    max_tokens_per_chunk: 2048
    chunk_duration_seconds: 120.0
    chunk_context_seconds: 5.0
    boundary_reconciliation: "forced-alignment-time-crossover-v3"
    alignment_coverage_guard: "active-audio-coverage-v1"
    aligned_gap_guard: "low-energy-gap-v1"
    backend: "transformers-native"
    transformers_version: "5.14.1"
    torch_version: "2.13.0"
    device: "cuda:0"
    dtype: "bfloat16"
    attention_implementation: "sdpa"
    max_inference_batch_size: 1
    final_outro_exemption_seconds: 0.0
    max_sentence_characters: 160
  generated_at: "2026-11-08T17:16:06.005204Z"
  quality:
    source_chunks: 69
    aligned_chunks: 69
    alignment_items: 37890
    sentence_segments: 1299
    refined_segments: 1297
    rendered_blocks: 277
    rendered_lines: 1297
  performance:
    model_load_seconds: 2.412
    transcription_seconds: 554.088
    aligner_load_seconds: 1.633
    alignment_seconds: 36.833
asr_artifacts:
  raw:
    path: "asr/qwen3-asr/raw.json"
    git_ignored: false
    format: "podwiki-raw-asr-json-v1"
  aligned:
    path: "asr/qwen3-asr/aligned.json"
    git_ignored: false
    format: "podwiki-aligned-asr-json-v1"
  refined:
    path: "asr/qwen3-asr/refined.json"
    git_ignored: false
    format: "podwiki-refined-asr-json-v1"
  transcript:
    path: "asr/qwen3-asr/transcript.zh-CN.md"
    git_ignored: false
    format: "podwiki-transcript-markdown-v1"
  renderer: "scripts/render_asr_transcript.py"
asr_runs:
  - id: "qwen3-asr-1.7b-native-cuda"
    selection_status: "selected"
    engine: "qwen-asr-transformers"
    model: "Qwen/Qwen3-ASR-1.7B-hf"
    aligner: "Qwen/Qwen3-ForcedAligner-0.6B-hf"
    options:
      language: "Chinese"
      temperature: 0.0
      max_tokens_per_chunk: 2048
      chunk_duration_seconds: 120.0
      chunk_context_seconds: 5.0
      boundary_reconciliation: "forced-alignment-time-crossover-v3"
      alignment_coverage_guard: "active-audio-coverage-v1"
      aligned_gap_guard: "low-energy-gap-v1"
      backend: "transformers-native"
      transformers_version: "5.14.1"
      torch_version: "2.13.0"
      device: "cuda:0"
      dtype: "bfloat16"
      attention_implementation: "sdpa"
      max_inference_batch_size: 1
      final_outro_exemption_seconds: 0.0
      max_sentence_characters: 160
    generated_at: "2026-11-08T17:16:06.005204Z"
    artifacts:
      raw: "asr/qwen3-asr/raw.json"
      aligned: "asr/qwen3-asr/aligned.json"
      refined: "asr/qwen3-asr/refined.json"
      transcript: "asr/qwen3-asr/transcript.zh-CN.md"
    quality:
      source_chunks: 69
      aligned_chunks: 69
      alignment_items: 37890
      sentence_segments: 1299
      refined_segments: 1297
      rendered_blocks: 277
      rendered_lines: 1297
    performance:
      model_load_seconds: 2.412
      transcription_seconds: 554.088
      aligner_load_seconds: 1.633
      alignment_seconds: 36.833
local_audio_cache:
  path: ".cache/media/yiqitietalk/xiaoyuzhou-6aeca1ea5b7c4709bfe1b7bf/source.m4a"
  metadata_path: ".cache/media/yiqitietalk/xiaoyuzhou-6aeca1ea5b7c4709bfe1b7bf/source.metadata.json"
  git_ignored: true
  acquired_at: "2026-11-08T14:56:28.954688Z"
  verified_at: "2026-11-08T14:56:28.954688Z"
  codec: "aac"
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 132889261
  duration_ms: 8209200
  sha256: "15f89c382c005bd2471a785f3802370c4cbbd5bbb7eea632f4c4eeac5976a091"
last_verified_at: "2026-11-08"
---

# 24 李大林：被说“捡漏”后北马再夺冠。扬眉吐气的李大林与晓霞，背后经历了什么？

> 来源身份与公开免费音频已核验。正式逐字稿是完整本地 Qwen3-ASR 机器稿，尚未人工核听；全文总结基于完整机器稿，状态为 draft。

## 单集信息

- 来源：[小宇宙发布者单集页](https://www.xiaoyuzhoufm.com/episode/6aeca1ea5b7c4709bfe1b7bf)
- 总结：[全文总结草稿](./summary.zh-CN.md)
- 逐字稿：[完整机器逐字稿](./transcript.zh-CN.md)
- 发布者原标题保存在 sources.title，未以数字标签推断正式期号。

## 处理记录

- 匿名页面只有 isTranscriptEnabled 功能开关与 mediaId 占位，没有可用公开字幕载荷；公开 M4A 与 sidecar 已逐集核验。
- 本地 Linux / RTX 5090、固定 native Qwen3-ASR 1.7B 与 ForcedAligner；本任务经用户明确授权以 5090 实测替代指定 A2000 门禁，不代表 A2000 已完成验证。
- 串行子进程生成 raw、aligned、refined 与 Markdown；完整 hash lineage 及严格边界/音频覆盖门禁通过，根稿与 selected run 字节一致。
- 仍需逐集核听、说话人识别、专名与数字校对、高影响事实核查；保持 transcript: machine，不标为 reviewed。

- 主持人身份核验：[发布者首集说明](https://www.xiaoyuzhoufm.com/episode/6952860114db1df9ef5c3a88)明确“我是孙瑞一，我的搭档是吴向东”，并与本集完整谈话对应；该链接只用于节目身份，不是本批新增范围。

## 产物可追溯性

- ASR：`Qwen/Qwen3-ASR-1.7B-hf`，固定 revision `bcd2b5b7f32b480ab5790554cfa8347f246a14f3`。
- 对齐器：`Qwen/Qwen3-ForcedAligner-0.6B-hf`，固定 revision `c07281df297b9905d24a508279258cccf987a064`。
- 实际运行环境：Linux / RTX 5090，Transformers 5.14.1、PyTorch 2.13.0+cu130、NumPy 2.4.6；逐集子进程串行。关键模型文件哈希保存在 raw/aligned 的 model identity 中。
- 核听与核查范围见[总结的编辑记录](./summary.zh-CN.md#编辑记录不对读者展示)，当前逐字稿和总结尚未完成对应人工审核。

| 产物 | SHA-256 |
| --- | --- |
| [raw](./asr/qwen3-asr/raw.json) | `6cea80734133fb6be0acf1194ab43028b76b1ed58ca10b5d777af06857f71850` |
| [aligned](./asr/qwen3-asr/aligned.json) | `e10a730a82e9b6a324977d4b2662ea5782eb9c5b6deef1e7ebdc699db72ad731` |
| [refined](./asr/qwen3-asr/refined.json) | `b04641cbf1028cd1c47c1dfd9e7d6b46f7401d31ec09061adfdbbb49ce599b68` |
| [selected 运行稿](./asr/qwen3-asr/transcript.zh-CN.md) | `f2f59e781e4bf81ef5eb074cfe51b4b2431fd26dfc4f002f12710b0cdee1b08e` |
| [根逐字稿](./transcript.zh-CN.md) | `f2f59e781e4bf81ef5eb074cfe51b4b2431fd26dfc4f002f12710b0cdee1b08e` |
