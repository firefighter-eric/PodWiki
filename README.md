# PodWiki

PodWiki 用 Markdown 记录播客节目、单集元数据、总结与逐字稿。

当前采用的内容标准是 [`docs/content-standard.md`](./docs/content-standard.md) 中的 `0.1-draft`。先用一个真实单集验证结构，再根据阅读和处理体验调整标准。

## 节目

| 节目 ID | 播客 | 收录状态 | 单集数 | 当前内容 |
| --- | --- | --- | ---: | --- |
| [`whynottv`](./shows/whynottv/) | WhynotTV Podcast | 已开始 | 1 | 元数据、总结、原始 ASR、refined ASR、逐字稿 |
| [`zhangxiaojun`](./shows/zhangxiaojun/) | 张小珺Jùn｜商业访谈录 | 已开始 | 5 | 元数据、内容概览、1 集原始 ASR、refined ASR 与逐字稿 |
| `sv101` | 硅谷101 | 待收录 | 0 | — |
| `luoyonghao` | 罗永浩的十字路口 | 待收录 | 0 | — |

## 基本原则

- 节目和单集使用 `README.md` 的 YAML front matter 保存结构化元数据。
- 单集 `README.md` 正文保存总结，逐字稿单独保存为 `transcript.<language>.md`。
- Bilibili 链接只保存不含查询参数和追踪参数的规范地址。
- 原始 ASR 与 refined ASR 随单集保存，进入 Git 以便追溯和复现。
- 音频、视频和临时处理文件保留在本地 `.cache/`，不提交到 Git。
- 面向阅读的机器逐字稿或人工校对稿以 Markdown 形式提交到 Git。

项目脚本适用根目录的 [Apache License 2.0](./LICENSE)。该许可证不自动改变所链接或引用的第三方节目内容的权利状态。

## Python 与 uv

项目使用 Python 3.12+，通过 `uv` 管理运行环境。媒体与 ASR worker 共享
同一个 `.venv`，因此开始并行任务前一次性同步全部依赖：

```bash
uv sync --all-groups
```

后续 worker 使用 `uv run --no-sync`，避免不同 dependency group 并发改写环境。

从公开的 Bilibili 或 YouTube 单视频获取音频与可复现 sidecar：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/acquire_media.py \
  --url https://www.bilibili.com/video/BVID/ \
  --output .cache/media/showid/episode-folder/source.m4a
```

脚本会规范化 URL、检查公开元数据与访问状态、拒绝多 P 或受访问控制的
来源，通过持久 staging 断点续传，并用 `ffprobe`、时长与 SHA-256 校验结果。
项目级完整工作流记录在
`.agents/skills/podwiki-process-episode/SKILL.md`。

校验内容结构和来源链接：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/validate.py
```

当前校验会检查节目内容中的 Bilibili 视频链接是否已经去掉查询参数、片段标识和常见追踪参数。

在 Apple Silicon Mac 上，本地音频通过 MLX Whisper 生成原始 ASR JSON：

在中国大陆下载 Hugging Face 模型前，先为当前终端设置镜像端点：

```bash
export HF_ENDPOINT=https://hf-mirror.com
```

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/transcribe_audio.py \
  --input .cache/media/whynottv/004-weng-jiayi/source.m4a \
  --output shows/whynottv/episodes/004-weng-jiayi/asr/raw.json \
  --model mlx-community/whisper-large-v3-turbo-q4 \
  --language zh
```

ASR 渲染脚本再保存 refined JSON，并生成面向阅读的 Markdown：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/render_asr_transcript.py \
  --input shows/whynottv/episodes/004-weng-jiayi/asr/raw.json \
  --refined-output shows/whynottv/episodes/004-weng-jiayi/asr/refined.json \
  --output shows/whynottv/episodes/004-weng-jiayi/transcript.zh-CN.md \
  --episode-id whynottv:004 \
  --title "翁家翌：OpenAI，GPT，强化学习，Infra，后训练，天授，tuixue，开源，CMU，清华｜WhynotTV Podcast #4" \
  --model mlx-community/whisper-large-v3-turbo-q4
```

Qwen3-ASR 作为候选引擎独立保存，先生成原始转写，再使用
Qwen3-ForcedAligner 生成字符或单词级时间戳并恢复为逐句分段：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/transcribe_qwen3_asr.py \
  --input .cache/media/whynottv/004-weng-jiayi/source.m4a \
  --output shows/whynottv/episodes/004-weng-jiayi/asr/qwen3-asr/raw.json \
  --aligned-output shows/whynottv/episodes/004-weng-jiayi/asr/qwen3-asr/aligned.json \
  --model mlx-community/Qwen3-ASR-1.7B-8bit \
  --aligner mlx-community/Qwen3-ForcedAligner-0.6B-8bit \
  --language Chinese
```

对齐结果可以继续复用相同的 refined JSON 和 Markdown 渲染流程：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/render_asr_transcript.py \
  --input shows/whynottv/episodes/004-weng-jiayi/asr/qwen3-asr/aligned.json \
  --refined-output shows/whynottv/episodes/004-weng-jiayi/asr/qwen3-asr/refined.json \
  --output shows/whynottv/episodes/004-weng-jiayi/asr/qwen3-asr/transcript.zh-CN.md \
  --episode-id whynottv:004 \
  --title "翁家翌：OpenAI，GPT，强化学习，Infra，后训练，天授，tuixue，开源，CMU，清华｜WhynotTV Podcast #4" \
  --engine mlx-audio \
  --model mlx-community/Qwen3-ASR-1.7B-8bit
```

候选引擎的 Markdown 只用于对比；选定正式模型后，才更新单集根目录的
`transcript.zh-CN.md`。首轮真实节目结果见
[`docs/asr-benchmark.md`](./docs/asr-benchmark.md)。
