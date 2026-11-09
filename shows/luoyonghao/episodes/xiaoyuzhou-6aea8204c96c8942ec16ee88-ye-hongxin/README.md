---
schema_version: 1
kind: "episode"
id: "luoyonghao:xiaoyuzhou-6aea8204c96c8942ec16ee88"
show_id: "luoyonghao"
episode_key: "xiaoyuzhou-6aea8204c96c8942ec16ee88"
episode_number: null
slug: "xiaoyuzhou-6aea8204c96c8942ec16ee88-ye-hongxin"
release_type: "regular"
numbering:
  status: "unknown"
  checked_at: "2026-11-09"
  source: "publisher-page"
  url: "https://www.xiaoyuzhoufm.com/episode/6aea8204c96c8942ec16ee88"
  note: "保留发布者原标题；页面及RSS未提供独立正式期号字段，使用eid稳定键，不由标题数字推断。"
title: "徕芬科技创始人叶洪新×罗永浩！初中毕业后，我先造飞机去了......"
navigation_title: "叶洪新 · 自学研发与徕芬创业"
catalog_keyword: "徕芬创业"
published_at: "2026-11-04T12:02:24.589000+08:00"
duration_ms: 11964600
language: "zh-CN"
participants:
  - id: "luoyonghao"
    name: "罗永浩"
    aliases: []
    role: "host"
  - id: "ye-hongxin"
    name: "叶洪新"
    aliases: []
    role: "guest"
sources:
  - platform: "xiaoyuzhou"
    kind: "episode"
    title: "徕芬科技创始人叶洪新×罗永浩！初中毕业后，我先造飞机去了......"
    url: "https://www.xiaoyuzhoufm.com/episode/6aea8204c96c8942ec16ee88"
    preferred: true
    identifiers:
      eid: "6aea8204c96c8942ec16ee88"
      pid: "68981df29e7bcd326eb91d88"
      media_id: "68981df29e7bcd326eb91d88/ll4eKwtvjNpxit2gDkVcfPHF0ELi.m4a"
  - platform: "rss"
    kind: "feed"
    url: "https://feed.xyzfm.space/wmnkvmrpwuww"
    preferred: false
    identifiers:
      feed_url: "https://feed.xyzfm.space/wmnkvmrpwuww"
      guid: "6aea8204c96c8942ec16ee88"
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
    sha256: "6a99309b71cf46058823a9195c784ec310ce4616663827918a9cda8f750984f7"
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
  generated_at: "2026-11-08T17:44:50.272039Z"
  quality:
    source_chunks: 100
    aligned_chunks: 100
    alignment_items: 59546
    sentence_segments: 2214
    refined_segments: 2213
    rendered_blocks: 394
    rendered_lines: 2213
  performance:
    model_load_seconds: 2.175
    transcription_seconds: 840.966
    aligner_load_seconds: 1.594
    alignment_seconds: 60.113
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
    generated_at: "2026-11-08T17:44:50.272039Z"
    artifacts:
      raw: "asr/qwen3-asr/raw.json"
      aligned: "asr/qwen3-asr/aligned.json"
      refined: "asr/qwen3-asr/refined.json"
      transcript: "asr/qwen3-asr/transcript.zh-CN.md"
    quality:
      source_chunks: 100
      aligned_chunks: 100
      alignment_items: 59546
      sentence_segments: 2214
      refined_segments: 2213
      rendered_blocks: 394
      rendered_lines: 2213
    performance:
      model_load_seconds: 2.175
      transcription_seconds: 840.966
      aligner_load_seconds: 1.594
      alignment_seconds: 60.113
local_audio_cache:
  path: ".cache/media/luoyonghao/xiaoyuzhou-6aea8204c96c8942ec16ee88/source.m4a"
  metadata_path: ".cache/media/luoyonghao/xiaoyuzhou-6aea8204c96c8942ec16ee88/source.metadata.json"
  git_ignored: true
  acquired_at: "2026-11-08T16:58:11.585871Z"
  verified_at: "2026-11-08T16:58:11.585871Z"
  codec: "aac"
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 385111954
  duration_ms: 11964600
  sha256: "67f711142c98b9441ba606b4239b42870ba9508992473620d9fe658a69acd7e2"
last_verified_at: "2026-11-09"
---

# 徕芬科技创始人叶洪新×罗永浩！初中毕业后，我先造飞机去了......

> 来源身份与公开免费音频已核验。正式逐字稿是完整本地 Qwen3-ASR 机器稿，尚未人工核听；全文总结基于完整机器稿，状态为 draft。

## 单集信息

- 来源：[小宇宙发布者单集页](https://www.xiaoyuzhoufm.com/episode/6aea8204c96c8942ec16ee88)
- 总结：[全文总结草稿](./summary.zh-CN.md)
- 逐字稿：[完整机器逐字稿](./transcript.zh-CN.md)
- 发布者原标题保存在 sources.title，未以数字标签推断正式期号。

## 处理记录

- 匿名页面只有 isTranscriptEnabled 功能开关与 mediaId 占位，没有可用公开字幕载荷；公开 M4A 与 sidecar 已逐集核验。
- 本地 Linux / RTX 5090、固定 native Qwen3-ASR 1.7B 与 ForcedAligner；本任务经用户明确授权以 5090 实测替代指定 A2000 门禁，不代表 A2000 已完成验证。
- 串行子进程生成 raw、aligned、refined 与 Markdown；完整 hash lineage 及严格边界/音频覆盖门禁通过，根稿与 selected run 字节一致。
- 仍需逐集核听、说话人识别、专名与数字校对、高影响事实核查；保持 transcript: machine，不标为 reviewed。

## 本批来源选择

- Bilibili 必需发现面尚未完整覆盖，原增量扫描保持 partial。旧视频传输探测成功不等于已发现并核实本集 BVID；本批按用户对上述精确小宇宙 URL 的明确授权取得官方公开免费完整音频，不推断 Bilibili 标识，不扩大候选范围。

## 产物可追溯性

- ASR：`Qwen/Qwen3-ASR-1.7B-hf`，固定 revision `bcd2b5b7f32b480ab5790554cfa8347f246a14f3`。
- 对齐器：`Qwen/Qwen3-ForcedAligner-0.6B-hf`，固定 revision `c07281df297b9905d24a508279258cccf987a064`。
- 实际运行环境：Linux / RTX 5090，Transformers 5.14.1、PyTorch 2.13.0+cu130、NumPy 2.4.6；逐集子进程串行。关键模型文件哈希保存在 raw/aligned 的 model identity 中。
- 核听与核查范围见[总结的编辑记录](./summary.zh-CN.md#编辑记录不对读者展示)，当前逐字稿和总结尚未完成对应人工审核。

| 产物 | SHA-256 |
| --- | --- |
| [raw](./asr/qwen3-asr/raw.json) | `e253edbedf62545338fec7dbf0caf3ed43770304f325c3f33e0cdb049b44bf35` |
| [aligned](./asr/qwen3-asr/aligned.json) | `b1da6213619f167ccaedfdccf8b714723b22cae3804e3b523913098d43a3bbf7` |
| [refined](./asr/qwen3-asr/refined.json) | `469b25415ed30425816be7c38f8a6ff228d466582f5ffca4ff943cd0485e8110` |
| [selected 运行稿](./asr/qwen3-asr/transcript.zh-CN.md) | `6a99309b71cf46058823a9195c784ec310ce4616663827918a9cda8f750984f7` |
| [根逐字稿](./transcript.zh-CN.md) | `6a99309b71cf46058823a9195c784ec310ce4616663827918a9cda8f750984f7` |
