---
schema_version: 1
kind: "episode"
id: "zhangxiaojun:xiaoyuzhou-6a8472b95aeb2a5712e8de78"
show_id: "zhangxiaojun"
episode_key: "xiaoyuzhou-6a8472b95aeb2a5712e8de78"
episode_number: null
slug: "xiaoyuzhou-6a8472b95aeb2a5712e8de78-su-tinghao"
release_type: "regular"
numbering:
  status: "unknown"
  checked_at: "2026-11-09"
  source: "publisher-page"
  url: "https://www.xiaoyuzhoufm.com/episode/6a8472b95aeb2a5712e8de78"
  note: "保留发布者原标题；页面及RSS未提供独立正式期号字段，使用eid稳定键，不由标题数字推断。"
title: "151. 17岁被2026年ICML收录论文的小少年：我bet开心！开心！开心！"
navigation_title: "苏庭灏 · 高中生的AI探索"
catalog_keyword: "高中生AI探索"
published_at: "2026-08-19T08:00:00+08:00"
duration_ms: 4190000
language: "zh-CN"
participants:
  - id: "zhangxiaojun"
    name: "张小珺"
    aliases: []
    role: "host"
  - id: "su-tinghao"
    name: "苏庭灏"
    aliases: []
    role: "guest"
sources:
  - platform: "xiaoyuzhou"
    kind: "episode"
    title: "151. 17岁被2026年ICML收录论文的小少年：我bet开心！开心！开心！"
    url: "https://www.xiaoyuzhoufm.com/episode/6a8472b95aeb2a5712e8de78"
    preferred: true
    identifiers:
      eid: "6a8472b95aeb2a5712e8de78"
      pid: "626b46ea9cbbf0451cf5a962"
      media_id: "626b46ea9cbbf0451cf5a962/lgS-qEdm2hDrXRFKGNSPhG4I5h5U.m4a"
  - platform: "rss"
    kind: "feed"
    url: "https://feed.xyzfm.space/dk4yh3pkpjp3"
    preferred: false
    identifiers:
      feed_url: "https://feed.xyzfm.space/dk4yh3pkpjp3"
      guid: "6a8472b95aeb2a5712e8de78"
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
    sha256: "c66536f60cfa1f287e6fab702cdba27dce9640a96e89fee44c01bd174323a7cf"
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
    audio_decode_profile: "normalized-rematrix-v1"
    max_sentence_characters: 160
  generated_at: "2026-11-09T01:44:08.188585Z"
  quality:
    source_chunks: 35
    aligned_chunks: 35
    alignment_items: 20326
    sentence_segments: 721
    refined_segments: 721
    rendered_blocks: 136
    rendered_lines: 721
  performance:
    model_load_seconds: 2.144
    transcription_seconds: 287.541
    aligner_load_seconds: 1.388
    alignment_seconds: 17.795
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
      audio_decode_profile: "normalized-rematrix-v1"
      max_sentence_characters: 160
    generated_at: "2026-11-09T01:44:08.188585Z"
    artifacts:
      raw: "asr/qwen3-asr/raw.json"
      aligned: "asr/qwen3-asr/aligned.json"
      refined: "asr/qwen3-asr/refined.json"
      transcript: "asr/qwen3-asr/transcript.zh-CN.md"
    quality:
      source_chunks: 35
      aligned_chunks: 35
      alignment_items: 20326
      sentence_segments: 721
      refined_segments: 721
      rendered_blocks: 136
      rendered_lines: 721
    performance:
      model_load_seconds: 2.144
      transcription_seconds: 287.541
      aligner_load_seconds: 1.388
      alignment_seconds: 17.795
local_audio_cache:
  path: ".cache/media/zhangxiaojun/xiaoyuzhou-6a8472b95aeb2a5712e8de78/source.m4a"
  metadata_path: ".cache/media/zhangxiaojun/xiaoyuzhou-6a8472b95aeb2a5712e8de78/source.metadata.json"
  git_ignored: true
  acquired_at: "2026-11-08T16:58:21.256087Z"
  verified_at: "2026-11-08T16:58:21.256087Z"
  codec: "aac"
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 67762945
  duration_ms: 4190000
  sha256: "241d214be4f647d6b32d48754e766384c2df0c3ca2c1711234366947d6978377"
last_verified_at: "2026-11-09"
---

# 151. 17岁被2026年ICML收录论文的小少年：我bet开心！开心！开心！

> 来源身份与公开免费音频已核验。正式逐字稿是完整本地 Qwen3-ASR 机器稿，尚未人工核听；全文总结基于完整机器稿，状态为 draft。

## 单集信息

- 来源：[小宇宙发布者单集页](https://www.xiaoyuzhoufm.com/episode/6a8472b95aeb2a5712e8de78)
- 总结：[全文总结草稿](./summary.zh-CN.md)
- 逐字稿：[完整机器逐字稿](./transcript.zh-CN.md)
- 发布者原标题保存在 sources.title，未以数字标签推断正式期号。

## 处理记录

- 匿名页面只有 isTranscriptEnabled 功能开关与 mediaId 占位，没有可用公开字幕载荷；公开 M4A 与 sidecar 已逐集核验。
- 本地 Linux / RTX 5090、固定 native Qwen3-ASR 1.7B 与 ForcedAligner；本任务经用户明确授权以 5090 实测替代指定 A2000 门禁，不代表 A2000 已完成验证。
- 串行子进程生成 raw、aligned、refined 与 Markdown；完整 hash lineage 及严格边界/音频覆盖门禁通过，根稿与 selected run 字节一致。
- 仍需逐集核听、说话人识别、专名与数字校对、高影响事实核查；保持 transcript: machine，不标为 reviewed。

## 本批来源与恢复

- Bilibili 必需发现面保持 blocked；本批按用户对这个精确官方小宇宙 URL 的明确授权与来源例外处理，不推断 BVID，不扩展清单。
- 重新核验公开免费身份并复用哈希一致的原始完整音频；历史失败 raw 和诊断全部保留，不转换或覆盖其谱系。
- 新运行显式选择 normalized-rematrix-v1，对ASR、对齐和声学探测统一使用防溢出的降混系数；按本集原始选项记录的归属块、两侧5秒上下文，固定模型revision不变。原始媒体未修改，预处理profile进入raw/aligned及选定运行元数据。
- 新样本与本集完整长音频已通过；所有边界、时间戳和覆盖门禁保持原值，片尾豁免为0秒，没有靠扩大豁免或抬高容差通过。

## 产物可追溯性

- ASR：`Qwen/Qwen3-ASR-1.7B-hf`，固定 revision `bcd2b5b7f32b480ab5790554cfa8347f246a14f3`。
- 对齐器：`Qwen/Qwen3-ForcedAligner-0.6B-hf`，固定 revision `c07281df297b9905d24a508279258cccf987a064`。
- 实际运行环境：Linux / RTX 5090，Transformers 5.14.1、PyTorch 2.13.0+cu130、NumPy 2.4.6；逐集子进程串行。关键模型文件哈希保存在 raw/aligned 的 model identity 中。
- 核听与核查范围见[总结的编辑记录](./summary.zh-CN.md#编辑记录不对读者展示)，当前逐字稿和总结尚未完成对应人工审核。

| 产物 | SHA-256 |
| --- | --- |
| [raw](./asr/qwen3-asr/raw.json) | `724146f01df6603640e718fcfee84a001660cb2cdde9f3c3f2324d24ff21bb12` |
| [aligned](./asr/qwen3-asr/aligned.json) | `8108752ba2004e1624248e550fae8a3f2a20fc28088b4ac6f44a28eb5af90cec` |
| [refined](./asr/qwen3-asr/refined.json) | `c6a9a4a29942644b6b1237976fc980752672c6d90d807f68d3e5b3df838d95bc` |
| [selected 运行稿](./asr/qwen3-asr/transcript.zh-CN.md) | `c66536f60cfa1f287e6fab702cdba27dce9640a96e89fee44c01bd174323a7cf` |
| [根逐字稿](./transcript.zh-CN.md) | `c66536f60cfa1f287e6fab702cdba27dce9640a96e89fee44c01bd174323a7cf` |
