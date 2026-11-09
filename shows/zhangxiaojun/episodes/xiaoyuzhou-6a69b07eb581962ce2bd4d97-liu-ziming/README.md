---
schema_version: 1
kind: "episode"
id: "zhangxiaojun:xiaoyuzhou-6a69b07eb581962ce2bd4d97"
show_id: "zhangxiaojun"
episode_key: "xiaoyuzhou-6a69b07eb581962ce2bd4d97"
episode_number: null
slug: "xiaoyuzhou-6a69b07eb581962ce2bd4d97-liu-ziming"
release_type: "regular"
numbering:
  status: "unknown"
  checked_at: "2026-11-09"
  source: "publisher-page"
  url: "https://www.xiaoyuzhoufm.com/episode/6a69b07eb581962ce2bd4d97"
  note: "保留发布者原标题；页面及RSS未提供独立正式期号字段，使用eid稳定键，不由标题数字推断。"
title: "149. 亲历中美neo labs资本狂潮，和清华刘子鸣聊：AI for AI、机制可解释性和Max Tegmark"
navigation_title: "刘子鸣 · AI研究与新型实验室"
catalog_keyword: "AI for AI"
published_at: "2026-07-31T07:30:00+08:00"
duration_ms: 6035200
language: "zh-CN"
participants:
  - id: "zhangxiaojun"
    name: "张小珺"
    aliases: []
    role: "host"
  - id: "liu-ziming"
    name: "刘子鸣"
    aliases: []
    role: "guest"
sources:
  - platform: "xiaoyuzhou"
    kind: "episode"
    title: "149. 亲历中美neo labs资本狂潮，和清华刘子鸣聊：AI for AI、机制可解释性和Max Tegmark"
    url: "https://www.xiaoyuzhoufm.com/episode/6a69b07eb581962ce2bd4d97"
    preferred: true
    identifiers:
      eid: "6a69b07eb581962ce2bd4d97"
      pid: "626b46ea9cbbf0451cf5a962"
      media_id: "626b46ea9cbbf0451cf5a962/lm33Q4N6w8TZcd2fXDBUK9UnC2xv.m4a"
  - platform: "rss"
    kind: "feed"
    url: "https://feed.xyzfm.space/dk4yh3pkpjp3"
    preferred: false
    identifiers:
      feed_url: "https://feed.xyzfm.space/dk4yh3pkpjp3"
      guid: "6a69b07eb581962ce2bd4d97"
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
    sha256: "32dbff7e35bfa20032d0223e686997ac6d9287d54632deebb01140f9360a7a83"
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
    chunk_duration_seconds: 60.0
    chunk_context_seconds: 8.0
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
    asr_language_conditioning: "forced-prefix-v1"
    max_sentence_characters: 160
  generated_at: "2026-11-09T02:00:52.551519Z"
  quality:
    source_chunks: 101
    aligned_chunks: 101
    alignment_items: 31373
    sentence_segments: 880
    refined_segments: 880
    rendered_blocks: 203
    rendered_lines: 880
  performance:
    model_load_seconds: 2.146
    transcription_seconds: 508.493
    aligner_load_seconds: 1.672
    alignment_seconds: 43.787
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
      chunk_duration_seconds: 60.0
      chunk_context_seconds: 8.0
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
      asr_language_conditioning: "forced-prefix-v1"
      max_sentence_characters: 160
    generated_at: "2026-11-09T02:00:52.551519Z"
    artifacts:
      raw: "asr/qwen3-asr/raw.json"
      aligned: "asr/qwen3-asr/aligned.json"
      refined: "asr/qwen3-asr/refined.json"
      transcript: "asr/qwen3-asr/transcript.zh-CN.md"
    quality:
      source_chunks: 101
      aligned_chunks: 101
      alignment_items: 31373
      sentence_segments: 880
      refined_segments: 880
      rendered_blocks: 203
      rendered_lines: 880
    performance:
      model_load_seconds: 2.146
      transcription_seconds: 508.493
      aligner_load_seconds: 1.672
      alignment_seconds: 43.787
local_audio_cache:
  path: ".cache/media/zhangxiaojun/xiaoyuzhou-6a69b07eb581962ce2bd4d97/source.m4a"
  metadata_path: ".cache/media/zhangxiaojun/xiaoyuzhou-6a69b07eb581962ce2bd4d97/source.metadata.json"
  git_ignored: true
  acquired_at: "2026-11-08T16:58:37.728647Z"
  verified_at: "2026-11-08T16:58:37.728647Z"
  codec: "aac"
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 97604907
  duration_ms: 6035200
  sha256: "1f8531ce9ae29b52d11944e32865427ae25e40ff9d16c3c49b5c7c572ba0eb1a"
last_verified_at: "2026-11-09"
---

# 149. 亲历中美neo labs资本狂潮，和清华刘子鸣聊：AI for AI、机制可解释性和Max Tegmark

> 来源身份与公开免费音频已核验。正式逐字稿是完整本地 Qwen3-ASR 机器稿，尚未人工核听；全文总结基于完整机器稿，状态为 draft。

## 单集信息

- 来源：[小宇宙发布者单集页](https://www.xiaoyuzhoufm.com/episode/6a69b07eb581962ce2bd4d97)
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
- 新运行显式选择 normalized-rematrix-v1，对ASR、对齐和声学探测统一使用防溢出的降混系数；60秒归属块、8秒两侧上下文，固定模型revision不变。原始媒体未修改，预处理profile进入raw/aligned及选定运行元数据。
- 中文识别显式使用 Qwen 官方 assistant 语言前缀 `forced-prefix-v1`；前缀与预处理选项绑定 raw/aligned 和 selected 元数据，旧运行默认行为不变。完整音频重新转写，没有用翻译替换识别结果。
- 新样本与本集完整长音频已通过；所有边界、时间戳和覆盖门禁保持原值，片尾豁免为0秒，没有靠扩大豁免或抬高容差通过。

## 产物可追溯性

- ASR：`Qwen/Qwen3-ASR-1.7B-hf`，固定 revision `bcd2b5b7f32b480ab5790554cfa8347f246a14f3`。
- 对齐器：`Qwen/Qwen3-ForcedAligner-0.6B-hf`，固定 revision `c07281df297b9905d24a508279258cccf987a064`。
- 实际运行环境：Linux / RTX 5090，Transformers 5.14.1、PyTorch 2.13.0+cu130、NumPy 2.4.6；逐集子进程串行。关键模型文件哈希保存在 raw/aligned 的 model identity 中。
- 核听与核查范围见[总结的编辑记录](./summary.zh-CN.md#编辑记录不对读者展示)，当前逐字稿和总结尚未完成对应人工审核。

| 产物 | SHA-256 |
| --- | --- |
| [raw](./asr/qwen3-asr/raw.json) | `76bbd2abe078b15bdbe05e9352ef1c18a8130d2208230efec81b47e8779d3323` |
| [aligned](./asr/qwen3-asr/aligned.json) | `0d724fa86e16d2d1d59c22c4e28205057ab777e4f7ea8509abcbcf5ccf7949d3` |
| [refined](./asr/qwen3-asr/refined.json) | `9a080c779505c6134b5e1640b3e4428490772c7ef7d7f85c5bad09f7be30e01c` |
| [selected 运行稿](./asr/qwen3-asr/transcript.zh-CN.md) | `32dbff7e35bfa20032d0223e686997ac6d9287d54632deebb01140f9360a7a83` |
| [根逐字稿](./transcript.zh-CN.md) | `32dbff7e35bfa20032d0223e686997ac6d9287d54632deebb01140f9360a7a83` |
