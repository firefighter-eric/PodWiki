---
schema_version: 1
kind: episode
id: zhangxiaojun:153
show_id: zhangxiaojun
episode_key: '153'
episode_number: 153
slug: 153-zeng-ming
release_type: regular
numbering:
  status: verified
  checked_at: '2026-09-26'
  source: https://www.xiaoyuzhoufm.com/episode/6a97f287f03e74ee6b03ea5b
title: 和曾鸣聊产业史观：残酷的真相、会消亡的公司、优秀≠卓越、“OAI、Anth大概率不是原生时代大赢家”
navigation_title: 曾鸣 · AI产业演化与组织变革
catalog_keyword: 产业演化
published_at: '2026-09-03T08:00:00+08:00'
duration_ms: 9262997
language: zh-CN
participants:
  - id: zeng-ming
    name: 曾鸣
    aliases: []
    role: guest
  - id: zhang-xiaojun
    name: 张小珺
    aliases: []
    role: host
sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1XNtJ6UEmm/
    title: 和曾鸣聊产业史观：残酷的真相、会消亡的公司、优秀≠卓越、“OAI、Anth大概率不是原生时代大赢家”
    preferred: true
    identifiers:
      bvid: BV1XNtJ6UEmm
      aid: '117200832825941'
      cid: '41470002219'
      page: 1
  - platform: xiaoyuzhou
    kind: episode
    url: https://www.xiaoyuzhoufm.com/episode/6a97f287f03e74ee6b03ea5b
    preferred: false
    title: 153. 和曾鸣聊产业史观：残酷的真相、会消亡的公司、优秀≠卓越、“OAI、Anth大概率不是原生时代大赢家”
    identifiers:
      eid: 6a97f287f03e74ee6b03ea5b
      pid: 626b46ea9cbbf0451cf5a962
      media_id: 626b46ea9cbbf0451cf5a962/luZvhPtdKotbkVR-SHFRKVVUiM2P.m4a
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
    sha256: 076106606f864c4a69efadc1fe7c5d153b94a9f116ac0fa20f40f7cc3859e699
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
    planned_chunk_count: 39
    final_leaf_chunk_count: 39
    adaptive_split_count: 0
    adaptive_split_algorithm: adaptive-low-energy-bisect-v1
    adaptive_min_leaf_samples: 320000
    adaptive_max_depth: 4
    adaptive_max_split_count: 64
    adaptive_energy_window_samples: 1600
    adaptive_quantization: pcm-s16-round-half-away-v1
    adaptive_tie_break: energy-center-left-v1
    effective_total_token_budget: 159744
    token_budget_scope: adaptive-bisect-per-leaf-v2
    max_sentence_characters: 160
  generated_at: '2026-09-26T04:21:06.187563Z'
  access_context: authenticated
  quality:
    source_chunks: 39
    aligned_chunks: 39
    alignment_items: 41695
    sentence_segments: 1527
    source_segments: 1527
    refined_segments: 1524
    rendered_blocks: 310
    rendered_lines: 1524
  performance:
    model_load_seconds: 0.295
    transcription_seconds: 381.964
    prompt_tokens: 121123
    generation_tokens: 27799
    attempt_prompt_tokens: 121123
    attempt_generation_tokens: 27799
    generation_call_count: 39
    prompt_tokens_per_second: 317.106
    generation_tokens_per_second: 72.779
    aligner_load_seconds: 0.231
    alignment_seconds: 60.971
  translations: []
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
    generated_at: '2026-09-26T04:21:06.187563Z'
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
local_audio_cache:
  path: .cache/media/zhangxiaojun/153-zeng-ming/source.m4a
  size_bytes: 160905553
  duration_ms: 9262997
  codec: aac
  sample_rate_hz: 48000
  channels: 2
  sha256: 3e189f7a466181b28e4816c92aeaf27d009d8157235bddf11fb8c04dd20db92f
  metadata_path: .cache/media/zhangxiaojun/153-zeng-ming/source.metadata.json
  git_ignored: true
  acquired_at: '2026-09-26T04:10:23.080420+00:00'
  verified_at: '2026-09-26T04:10:23.080420+00:00'
last_verified_at: '2026-09-26'
---

# 和曾鸣聊产业史观：残酷的真相、会消亡的公司、优秀≠卓越、“OAI、Anth大概率不是原生时代大赢家”

> 完整中文稿由本地 Qwen3-ASR 和 ForcedAligner 生成，状态为 `machine`；总结依据所选完整稿，状态为 `draft`，尚未完成对应人工审核。

## 单集信息

- 总结：[查看总结](./summary.zh-CN.md)
- 正式逐字稿：[查看中文逐字稿](./transcript.zh-CN.md)
- 原始节目：[发布者完整单集](https://www.bilibili.com/video/BV1XNtJ6UEmm/)

平台返回的 120 条 AI 字幕只覆盖约 197 秒，主题与本期不符，未导入。用户于 2026-09-26 明确允许弃用该无效字幕并改用完整音频本地转写；原响应保留在忽略缓存作为核验记录。正式期号 153 来自已核实的官方 RSS 与小宇宙单集，本稿绑定 B 站 2:34:23 视频音轨。官方 RSS 音频标示 2:34:18，相差约 5 秒；两版的标题、嘉宾、完整章节和主体对应，本稿时间码只适用于所选 B 站音轨，平台间剪辑差异尚未逐帧核对。

## 待审核

- 回听核对机器稿中的专有名词、数字、否定词和说话人归属。
- 审核总结引用的产业预测、历史类比、观点归属与时间码。
