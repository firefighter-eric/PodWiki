---
schema_version: 1
kind: "episode"
id: "yiqitietalk:xiaoyuzhou-6ace0097e742e36efcc2599d"
show_id: "yiqitietalk"
episode_key: "xiaoyuzhou-6ace0097e742e36efcc2599d"
episode_number: null
slug: "xiaoyuzhou-6ace0097e742e36efcc2599d-wu-xiangdong"
release_type: "regular"
numbering:
  status: "unknown"
  checked_at: "2026-11-08"
  source: "publisher-page"
  url: "https://www.xiaoyuzhoufm.com/episode/6ace0097e742e36efcc2599d"
  note: "原标题数字标签保留在来源中；未取得独立正式期号字段，使用 eid 稳定键，不按列表位置推断。"
title: "22 吴向东：2:07:55 PB背后，一起“搞个大的”"
navigation_title: "孙瑞一、吴向东 · 柏林PB与自主训练"
catalog_keyword: "柏林马拉松"
published_at: "2026-10-13T18:13:58.197000+08:00"
duration_ms: 5292700
language: "zh-CN"
participants:
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
    title: "22 吴向东：2:07:55 PB背后，一起“搞个大的”"
    url: "https://www.xiaoyuzhoufm.com/episode/6ace0097e742e36efcc2599d"
    preferred: true
    identifiers:
      eid: "6ace0097e742e36efcc2599d"
      pid: "6951e312febad13106eb017e"
      media_id: "6951e312febad13106eb017e/llErTsJDkSnVD4aK5hEhSZfD61yp.m4a"
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
    sha256: "b979c8d01ce791606fc9f2dbb1bf4c2c366930ed319b5486be52f24bfcb33470"
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
  generated_at: "2026-11-08T17:29:29.669642Z"
  quality:
    source_chunks: 45
    aligned_chunks: 45
    alignment_items: 21661
    sentence_segments: 631
    refined_segments: 631
    rendered_blocks: 176
    rendered_lines: 631
  performance:
    model_load_seconds: 2.036
    transcription_seconds: 315.913
    aligner_load_seconds: 1.635
    alignment_seconds: 22.893
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
    generated_at: "2026-11-08T17:29:29.669642Z"
    artifacts:
      raw: "asr/qwen3-asr/raw.json"
      aligned: "asr/qwen3-asr/aligned.json"
      refined: "asr/qwen3-asr/refined.json"
      transcript: "asr/qwen3-asr/transcript.zh-CN.md"
    quality:
      source_chunks: 45
      aligned_chunks: 45
      alignment_items: 21661
      sentence_segments: 631
      refined_segments: 631
      rendered_blocks: 176
      rendered_lines: 631
    performance:
      model_load_seconds: 2.036
      transcription_seconds: 315.913
      aligner_load_seconds: 1.635
      alignment_seconds: 22.893
local_audio_cache:
  path: ".cache/media/yiqitietalk/xiaoyuzhou-6ace0097e742e36efcc2599d/source.m4a"
  metadata_path: ".cache/media/yiqitietalk/xiaoyuzhou-6ace0097e742e36efcc2599d/source.metadata.json"
  git_ignored: true
  acquired_at: "2026-11-08T14:56:58.626712Z"
  verified_at: "2026-11-08T14:56:58.626712Z"
  codec: "aac"
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 85597314
  duration_ms: 5292700
  sha256: "5a8dbfbd00b6573a1c2bd4e0fd9de1a01966e08365a59151c693663c5e3ba2ef"
last_verified_at: "2026-11-08"
---

# 22 吴向东：2:07:55 PB背后，一起“搞个大的”

> 来源身份与公开免费音频已核验。正式逐字稿是完整本地 Qwen3-ASR 机器稿，尚未人工核听；全文总结基于完整机器稿，状态为 draft。

## 单集信息

- 来源：[小宇宙发布者单集页](https://www.xiaoyuzhoufm.com/episode/6ace0097e742e36efcc2599d)
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
| [raw](./asr/qwen3-asr/raw.json) | `1ed1a7cab82f92212aca4123c9c9d9878a26ee70c557d2c6bdd72779f339d931` |
| [aligned](./asr/qwen3-asr/aligned.json) | `23b1b91b43ef19e83ca5df7b68e154b0dcd47cd38e43762411281a0d92db0c40` |
| [refined](./asr/qwen3-asr/refined.json) | `4fdab372981a589749fbe47265bb3d3114b84f66d137f1ae46b520d15f1bf1c9` |
| [selected 运行稿](./asr/qwen3-asr/transcript.zh-CN.md) | `b979c8d01ce791606fc9f2dbb1bf4c2c366930ed319b5486be52f24bfcb33470` |
| [根逐字稿](./transcript.zh-CN.md) | `b979c8d01ce791606fc9f2dbb1bf4c2c366930ed319b5486be52f24bfcb33470` |
