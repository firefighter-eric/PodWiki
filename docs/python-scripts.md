# Python 脚本用法

本页集中记录 PodWiki 的 Python 工具和推荐运行方式。所有命令都从仓库根目录执行。

## 环境准备

项目使用 Python 3.12+ 和 `uv`。开始媒体处理或 ASR 前，先同步全部依赖：

```bash
uv sync --all-groups
```

后续命令统一使用仓库内的 uv 缓存，并通过 `--no-sync` 避免 worker 运行期间改写共享 `.venv`：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python <script> <arguments>
```

在中国大陆首次下载 Hugging Face 模型前，为当前终端设置镜像：

```bash
export HF_ENDPOINT=https://hf-mirror.com
```

下载项目默认的 Qwen3-ASR 和 ForcedAligner：

```bash
hf download mlx-community/Qwen3-ASR-1.7B-8bit \
  --local-dir .cache/models/qwen3-asr-1.7b-8bit

hf download mlx-community/Qwen3-ForcedAligner-0.6B-8bit \
  --local-dir .cache/models/qwen3-forced-aligner-0.6b-8bit
```

## 脚本一览

| 脚本 | 用途 | 主要产物 |
| --- | --- | --- |
| `scripts/acquire_media.py` | 获取一个公开 Bilibili 或 YouTube 视频的音轨 | `.cache/media/.../source.m4a` 与来源 sidecar |
| `scripts/transcribe_qwen3_asr.py` | 使用 Qwen3-ASR 转写并强制对齐 | `raw.json`、`aligned.json` |
| `scripts/render_asr_transcript.py` | 清理对齐结果并渲染逐字稿 | `refined.json`、`transcript.zh-CN.md` |
| `scripts/process_qwen3_asr_batch.py` | 串行处理一个或多个已缓存单集 | 每集完整 Qwen 产物与日志 |
| `scripts/transcribe_audio.py` | 生成 MLX Whisper 对比基线 | Whisper `raw.json` |
| `scripts/validate.py` | 校验内容、来源和 ASR 产物链 | 终端校验结果 |

## 获取公开音轨

`acquire_media.py` 只处理单个公开 Bilibili 或 YouTube 视频，不处理账号、播放列表、多 P 或受访问控制的内容。

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/acquire_media.py \
  --url https://www.bilibili.com/video/BVID/ \
  --output .cache/media/<show-id>/<episode-folder>/source.m4a
```

脚本会规范化 URL，检查公开元数据，下载或续传音频，并用 `ffprobe`、时长、文件大小和 SHA-256 校验结果。未指定 `--metadata-output` 时，来源信息保存在音频旁的 `source.metadata.json`。

若 Bilibili 的公开视频页出现已知的 `Unable to extract initial state` extractor
兼容错误，但官方匿名 view、player 和 playurl API 对请求 BVID、aid、cid、page
均验证一致，脚本会从公开 DASH 清单中选择码率最高的匿名音轨作为回退。其他
extractor 或传输错误不会触发这条回退。回退要求 `state == 0`，并要求付费、
试看、充电专属和 upower 等关键访问字段全部显式为 `0`/`false`；字段缺失时
按拒绝处理。`no_reprint` 会作为来源边界记录但不等同于访问限制，`download`
字段也不构成处理授权。脚本不会使用 cookies，也不会把临时签名媒体 URL 写入
sidecar。

只检查来源而不下载：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/acquire_media.py \
  --url https://www.bilibili.com/video/BVID/ \
  --output .cache/media/<show-id>/<episode-folder>/source.m4a \
  --metadata-only
```

已有音频默认不会被替换；只有明确需要覆盖时才使用 `--overwrite`。

## 处理单个 Qwen3-ASR 单集

Apple Silicon 上的中文单集默认使用 Qwen3-ASR 1.7B 8-bit 和 Qwen3-ForcedAligner 0.6B 8-bit：

```bash
env HF_ENDPOINT=https://hf-mirror.com HF_HUB_OFFLINE=1 \
  UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/transcribe_qwen3_asr.py \
  --input .cache/media/<show-id>/<episode-folder>/source.m4a \
  --output shows/<show-id>/episodes/<episode-folder>/asr/qwen3-asr/raw.json \
  --aligned-output shows/<show-id>/episodes/<episode-folder>/asr/qwen3-asr/aligned.json \
  --model mlx-community/Qwen3-ASR-1.7B-8bit \
  --model-path .cache/models/qwen3-asr-1.7b-8bit \
  --aligner mlx-community/Qwen3-ForcedAligner-0.6B-8bit \
  --aligner-path .cache/models/qwen3-forced-aligner-0.6b-8bit \
  --language Chinese --no-verbose
```

有效的 `raw.json` 是转写检查点：缺少对齐产物时会从对齐阶段恢复；有效且身份匹配的 raw/aligned 会直接跳过。只有显式传入 `--retranscribe` 或 `--realign` 才会替换相应产物。

## 渲染逐字稿

对齐完成后，用同一次运行生成哈希关联的 refined JSON 和 Markdown：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/render_asr_transcript.py \
  --input shows/<show-id>/episodes/<episode-folder>/asr/qwen3-asr/aligned.json \
  --refined-output shows/<show-id>/episodes/<episode-folder>/asr/qwen3-asr/refined.json \
  --output shows/<show-id>/episodes/<episode-folder>/asr/qwen3-asr/transcript.zh-CN.md \
  --episode-id <show-id>:<episode-key> \
  --title "<episode-title>" \
  --engine mlx-audio \
  --model mlx-community/Qwen3-ASR-1.7B-8bit
```

四份 Qwen 产物全部校验通过后，才把 run Markdown 作为单集根目录的正式 `transcript.zh-CN.md`，并同步更新单集 README 的来源、哈希和 workflow 状态。

## 串行批处理

`process_qwen3_asr_batch.py` 会让每个单集运行在独立子进程中，避免连续长任务积累 Metal/统一内存状态。重复传入 `--episode` 可以限制处理范围：

```bash
env HF_ENDPOINT=https://hf-mirror.com HF_HUB_OFFLINE=1 \
  UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/process_qwen3_asr_batch.py \
  --episode shows/<show-id>/episodes/<episode-folder> \
  --model-path .cache/models/qwen3-asr-1.7b-8bit \
  --aligner-path .cache/models/qwen3-forced-aligner-0.6b-8bit
```

不传 `--episode` 时，脚本发现所有已有缓存音频的单集。它会串行启动 worker，在 `.cache/logs/qwen3-asr/` 保存每集日志，继续处理其他单集，并在任一单集失败时最终返回非零状态。

默认按中文语音处理并生成 `transcript.zh-CN.md`。处理英文等其他语言时，同时
传入 ASR 使用的语言名称和用于产物文件名的 BCP 47 标签，例如：

```bash
env HF_ENDPOINT=https://hf-mirror.com HF_HUB_OFFLINE=1 \
  UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/process_qwen3_asr_batch.py \
  --episode shows/<show-id>/episodes/<episode-folder> \
  --language English --transcript-language en \
  --model-path .cache/models/qwen3-asr-1.7b-8bit \
  --aligner-path .cache/models/qwen3-forced-aligner-0.6b-8bit
```

## MLX Whisper 基线

MLX Whisper 只用于保留已有基线或显式对比，不作为当前中文单集的默认正式逐字稿：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/transcribe_audio.py \
  --input .cache/media/<show-id>/<episode-folder>/source.m4a \
  --output shows/<show-id>/episodes/<episode-folder>/asr/whisper/raw.json \
  --model mlx-community/whisper-large-v3-turbo-q4 \
  --language zh
```

## 校验

运行单元测试：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python -m unittest discover -s tests -v
```

校验 Markdown、规范来源 URL、严格 JSON、Qwen 产物路径及 SHA-256 lineage：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/validate.py
```

最后还应运行 `git diff --check`，检查 `git status --short`，并确认根 README 的三列节目介绍表中，播客名称链接已核实的 Bilibili 空间，节目页链接本地节目 README。根 README 的单集表格采用“标题、访谈人物、播客名称、日期、总结、逐字稿”六列，节目 README 的单集表格仍采用“标题、播客名称、日期、总结链接、逐字稿链接”五列，且两处内容已经同步。根表的访谈人物来自单集 front matter 中 `role: guest` 的参与者；多位嘉宾使用顿号分隔。

完整处理规则、恢复语义和来源限制见 [PodWiki episode 处理 skill](../.agents/skills/podwiki-process-episode/SKILL.md)；内容字段和状态定义见[内容标准](./content-standard.md)。
