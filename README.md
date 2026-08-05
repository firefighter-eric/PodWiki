# PodWiki

PodWiki 用 Markdown 记录播客节目、单集元数据、总结与逐字稿。

当前采用的内容标准是 [`docs/content-standard.md`](./docs/content-standard.md) 中的 `0.1-draft`。先用一个真实单集验证结构，再根据阅读和处理体验调整标准。

## 节目

| 节目 ID | 播客 | 收录状态 | 单集数 | 当前内容 |
| --- | --- | --- | ---: | --- |
| [`whynottv`](./shows/whynottv/) | WhynotTV Podcast | 已开始 | 1 | 元数据、总结、原始 ASR、refined ASR、逐字稿 |
| `zhangxiaojun` | 张小珺Jùn｜商业访谈录 | 待收录 | 0 | — |
| `sv101` | 硅谷101 | 待收录 | 0 | — |
| `luoyonghao` | 罗永浩的十字路口 | 待收录 | 0 | — |

## 基本原则

- 节目和单集使用 `README.md` 的 YAML front matter 保存结构化元数据。
- 单集 `README.md` 正文保存总结，逐字稿单独保存为 `transcript.<language>.md`。
- Bilibili 链接只保存不含查询参数和追踪参数的规范地址。
- 原始 ASR 与 refined ASR 随单集保存，进入 Git 以便追溯和复现。
- 音频、视频和临时处理文件保留在本地 `.cache/`，不提交到 Git。
- 面向阅读的机器逐字稿或人工校对稿以 Markdown 形式提交到 Git。
- 第三方节目内容的权利归原权利人；每个单集单独记录来源提示、记录用途和是否有再分发意图。

项目脚本适用根目录的 [Apache License 2.0](./LICENSE)。该许可证不自动改变所链接或引用的第三方节目内容的权利状态。

## Python 与 uv

项目使用 Python 3.12+，通过 `uv` 管理运行环境。初始化或同步环境：

```bash
uv sync
```

校验内容结构和来源链接：

```bash
uv run python scripts/validate.py
```

当前校验会检查节目内容中的 Bilibili 视频链接是否已经去掉查询参数、片段标识和常见追踪参数。

在 Apple Silicon Mac 上，本地音频通过 MLX Whisper 生成原始 ASR JSON：

```bash
uv run --group asr python scripts/transcribe_audio.py \
  --input .cache/media/whynottv/004-weng-jiayi/source.m4a \
  --output shows/whynottv/episodes/004-weng-jiayi/asr/raw.json \
  --model mlx-community/whisper-large-v3-turbo-q4 \
  --language zh
```

ASR 渲染脚本再保存 refined JSON，并生成面向阅读的 Markdown：

```bash
uv run python scripts/render_asr_transcript.py \
  --input shows/whynottv/episodes/004-weng-jiayi/asr/raw.json \
  --refined-output shows/whynottv/episodes/004-weng-jiayi/asr/refined.json \
  --output shows/whynottv/episodes/004-weng-jiayi/transcript.zh-CN.md \
  --episode-id whynottv:004 \
  --title "翁家翌：OpenAI，GPT，强化学习，Infra，后训练，天授，tuixue，开源，CMU，清华｜WhynotTV Podcast #4" \
  --model mlx-community/whisper-large-v3-turbo-q4
```
