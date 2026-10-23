---
schema_version: 1
kind: episode
id: zhangxiaojun:155
show_id: zhangxiaojun
episode_key: '155'
episode_number: 155
slug: 155-qian-cheng
release_type: regular
numbering:
  status: verified
  checked_at: '2026-10-23'
  source: publisher-feed
  url: https://www.xiaoyuzhoufm.com/episode/6ad4dacd641ef406308d86e5
title: 和科沃斯钱程聊，父与子、企二代接班的样本与肌理、机器人、我内心的追寻
navigation_title: 钱程 · 接班、全球化与经营的克制
catalog_keyword: 科沃斯
published_at: '2026-10-21T08:00:00+08:00'
duration_ms: 7191787
language: zh-CN
participants:
  - id: qian-cheng
    name: 钱程
    aliases: []
    role: guest
  - id: zhangxiaojun
    name: 张小珺
    aliases: []
    role: host
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1NtJB6TEkE/
    preferred: true
    title: 和科沃斯钱程聊，父与子、企二代接班的样本与肌理、机器人、我内心的追寻
    identifiers:
      bvid: BV1NtJB6TEkE
      aid: '117457020783075'
      cid: '42727114817'
      page: 1
  - platform: rss
    kind: feed
    url: https://feed.xyzfm.space/dk4yh3pkpjp3
    preferred: false
    title: 155. 和科沃斯钱程聊，父与子、企二代接班的样本与肌理、机器人，和我内心的追寻
    identifiers:
      feed_url: https://feed.xyzfm.space/dk4yh3pkpjp3
      guid: 6ad4dacd641ef406308d86e5
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
    sha256: e3c956eabf15c0012a0e597ec9fa880900611062c4fd1dd0b9a52a26cbb5846d
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
  generated_at: '2026-10-23T15:24:53.259051Z'
  access_context: anonymous
  platform_subtitle_access:
    anonymous_tracks: []
    need_login: true
    authenticated_context: not-authorized-or-used
  quality:
    source_chunks: 30
    aligned_chunks: 30
    alignment_items: 31868
    sentence_segments: 1222
    source_segments: 1222
    refined_segments: 1220
    rendered_blocks: 239
    rendered_lines: 1220
  performance:
    model_load_seconds: 0.187
    transcription_seconds: 229.87
    prompt_tokens: 94036
    generation_tokens: 21424
    attempt_prompt_tokens: 94036
    attempt_generation_tokens: 21424
    generation_call_count: 30
    prompt_tokens_per_second: 409.083
    generation_tokens_per_second: 93.2
    aligner_load_seconds: 0.218
    alignment_seconds: 36.341
asr_runs:
  - id: qwen3-asr
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    generated_at: '2026-10-23T15:24:53.259051Z'
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  size_bytes: 94989375
  duration_ms: 7191787
  sha256: a2d33a11db564e506a9016ad49d673bb29d51134fb1168dc0f4c3970d2963afc
  path: .cache/media/zhangxiaojun/155-qian-cheng/source.m4a
  metadata_path: .cache/media/zhangxiaojun/155-qian-cheng/source.metadata.json
  git_ignored: true
  acquired_at: '2026-10-23T15:14:11.778490Z'
  verified_at: '2026-10-23T15:14:11.778490Z'
last_verified_at: '2026-10-23'
asr_artifacts:
  raw:
    path: asr/qwen3-asr/raw.json
    git_ignored: false
    format: podwiki-raw-asr-json-v1
    sha256: dbbabd654cd4b1a7105c5f0292d1486e24500961edeb0116a99c8f83ed217321
  aligned:
    path: asr/qwen3-asr/aligned.json
    git_ignored: false
    format: podwiki-aligned-asr-json-v1
    sha256: 7f5d18684ab24de71a094ab71ff56b781370f6f75550657e0759fad747106f7d
  refined:
    path: asr/qwen3-asr/refined.json
    git_ignored: false
    format: podwiki-refined-asr-json-v1
    sha256: 3bf6b13feb804d1c59fb0dd9b5d9625bb5b6ec63e13ca152ad92c92a6ba626f3
  transcript:
    path: asr/qwen3-asr/transcript.zh-CN.md
    git_ignored: false
    format: podwiki-transcript-markdown-v1
    sha256: e3c956eabf15c0012a0e597ec9fa880900611062c4fd1dd0b9a52a26cbb5846d
  renderer: scripts/render_asr_transcript.py
---

# 和科沃斯钱程聊，父与子、企二代接班的样本与肌理、机器人、我内心的追寻

> 逐字稿由本地固定版本Qwen3-ASR与ForcedAligner生成，状态为`machine`；全文总结为`draft`。尚未完成逐段人工核听。

## 单集信息

- 总结：[查看全文总结](./summary.zh-CN.md)
- 正式逐字稿：[查看中文逐字稿](./transcript.zh-CN.md)
- 原始节目：[发布者完整单集](https://www.bilibili.com/video/BV1NtJB6TEkE/)

## 来源核验

- 官方发布者、公开免费单P、BVID/aid/cid/page与本地音频大小、时长和SHA-256均已核实。
- 与官方播客发布的嘉宾、内容主题、章节和完整时长对应；小宇宙仅作身份和同集交叉核对。
- 本次匿名上下文未发现可用字幕；没有使用登录态，也未把匿名检查解释为所有上下文均无字幕。

## 待审核

- 逐段核听人名、公司与模型名、数字、否定词及说话人归属。
- 对总结中的关键引文和高影响事实做必要的回听及独立核查；当前不得标为reviewed。
