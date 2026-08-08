# Python 脚本用法

本页集中记录 PodWiki 的 Python 工具和推荐运行方式。所有命令都从仓库根目录执行。
第一次新增单集时，先按[单集端到端处理流程](./episode-processing.md)确定目录、元数据、
语言分组和停止点，再回到本页复制具体命令。

## 环境准备

项目使用 Python 3.12+ 和 `uv`。媒体获取还要求系统可执行文件 `ffmpeg`、
`ffprobe`；YouTube 处理另外要求 Deno 或 Node.js。正式本地 Qwen ASR 支持两条
明确路径：Apple Silicon（macOS `arm64`）上的 MLX，以及 Windows x86-64 上的
NVIDIA CUDA。其他平台可以整理元数据和已有文本，不能静默换用远端或付费 ASR。
前端最终门禁需要 Node.js 和 npm。

开始前先完成一次预检：

```bash
python3 --version
uv --version
ffmpeg -version
ffprobe -version
node --version
npm --version
```

只处理 Bilibili 且不运行前端时，Deno/Node.js 与 npm 不是下载阶段的必需项；
但交付完整仓库变更前仍需在具备 Node.js/npm 的环境运行 Web 门禁。

`asr`（MLX）与 `asr-cuda` 依赖组互斥，不能使用 `uv sync --all-groups`。
Apple Silicon/MLX 先同步对应依赖：

```bash
uv sync --group asr
env UV_CACHE_DIR=.cache/uv uv run --no-sync hf --help
```

后续 MLX 命令统一使用仓库内的 uv 缓存，并通过 `--no-sync` 避免 worker 运行期间
改写共享 `.venv`：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python <script> <arguments>
```

PowerShell 不提供 POSIX 的 `env`、`export` 或反斜杠续行。先在当前终端设置环境变量，
再运行后续命令；多行命令可改成单行，或把示例中的 `\` 换成 PowerShell 反引号：

```powershell
$env:UV_CACHE_DIR = ".cache/uv"
$env:HF_ENDPOINT = "https://hf-mirror.com"
uv run --no-sync python <script> <arguments>
```

Windows/CUDA 建议使用被 Git 忽略的独立环境。首次创建并锁定依赖时：

```powershell
uv venv --python 3.12 .cache/venvs/qwen-cuda
. .\.cache\venvs\qwen-cuda\Scripts\Activate.ps1
uv sync --active --group asr-cuda --locked
```

正式 worker 直接使用
`.cache/venvs/qwen-cuda/Scripts/python.exe`，不要在长任务运行期间同步依赖。

本页余下 `env UV_CACHE_DIR=.cache/uv ...` 示例在 PowerShell 中均省略该前缀，沿用上面已
设置的 `$env:UV_CACHE_DIR`；`export HF_ENDPOINT=...` 同理只需设置一次。

在中国大陆首次下载 Hugging Face 模型前，为当前终端设置镜像：

```bash
export HF_ENDPOINT=https://hf-mirror.com
```

下载 Apple Silicon/MLX 使用的 Qwen3-ASR 和 ForcedAligner：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync hf download \
  mlx-community/Qwen3-ASR-1.7B-8bit \
  --local-dir .cache/models/qwen3-asr-1.7b-8bit

env UV_CACHE_DIR=.cache/uv uv run --no-sync hf download \
  mlx-community/Qwen3-ForcedAligner-0.6B-8bit \
  --local-dir .cache/models/qwen3-forced-aligner-0.6b-8bit
```

Windows/CUDA 使用官方模型：

```powershell
$env:HF_ENDPOINT = "https://huggingface.co"
& .cache/venvs/qwen-cuda/Scripts/hf.exe download Qwen/Qwen3-ASR-1.7B `
  --local-dir .cache/models/Qwen3-ASR-1.7B
& .cache/venvs/qwen-cuda/Scripts/hf.exe download Qwen/Qwen3-ForcedAligner-0.6B `
  --local-dir .cache/models/Qwen3-ForcedAligner-0.6B
```

## 脚本一览

| 脚本 | 用途 | 主要产物 |
| --- | --- | --- |
| `scripts/acquire_media.py` | 获取一个公开 Bilibili/YouTube 视频或小宇宙单集的音轨 | `.cache/media/.../source.m4a` 与来源 sidecar |
| `scripts/transcribe_qwen3_asr.py` | 使用 Qwen3-ASR 转写并强制对齐 | `raw.json`、`aligned.json` |
| `scripts/transcribe_qwen3_asr_cuda.py` | 在 Windows/NVIDIA CUDA 上使用官方 Qwen 模型转写并强制对齐 | `raw.json`、`aligned.json` |
| `scripts/render_asr_transcript.py` | 清理对齐结果并渲染逐字稿 | `refined.json`、`transcript.<language>.md` |
| `scripts/process_qwen3_asr_batch.py` | 串行处理一个或多个已缓存单集 | 每集完整 Qwen 产物与日志 |
| `scripts/transcribe_audio.py` | 生成 MLX Whisper 对比基线 | Whisper `raw.json` |
| `scripts/validate.py` | 校验内容、来源和 ASR 产物链 | 终端校验结果 |

## 获取公开音轨

`acquire_media.py` 的每次调用只处理一个公开 Bilibili/YouTube 视频或小宇宙单集，
不直接接收账号、播放列表、多 P、播客栏目页或受访问控制的内容。用户明确授权的
单一已核实栏目批量导入，必须先按[单集处理流程](./episode-processing.md)冻结 PID、
规范单集 URL 与 `eid` manifest，再由外层任务逐集串行调用本脚本；脚本本身不会
枚举栏目或在运行中扩展范围。

传给脚本的 Bilibili 地址必须已经是
`https://www.bilibili.com/video/<BVID>/`。如果收到
`/festival/...?...bvid=<BVID>` 一类活动页，先提取查询参数中的 BVID 并改写成
上述规范视频地址；脚本会拒绝直接传入活动页。

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

先检查 sidecar 中的 `source.subtitle_languages`、
`source.automatic_caption_languages` 和
`source.platform_metadata.subtitle.tracks`。仓库目前尚未提供公开字幕的下载、
转换与 lineage 导入工具；发现可用字幕时应停止自动流程、报告该分支尚未实现，
不要绕过字幕直接启动 ASR。只有确认没有可用公开字幕且来源允许处理时，才下载音频。

已有音频默认不会被替换；只有明确需要覆盖时才使用 `--overwrite`。

小宇宙输入必须是单集页，播客栏目页不能直接下载：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/acquire_media.py \
  --url https://www.xiaoyuzhoufm.com/episode/<episode-id> \
  --output .cache/media/<show-id>/<episode-folder>/source.m4a
```

脚本只读取无需登录即可访问的规范单集 HTML 与其中的 `__NEXT_DATA__`，拒绝页面或媒体
重定向，并核对 `eid`、单集自身 `pid`、嵌套栏目 `pid`、`mediaKey`、`media.id` 和 CDN
path。`media.id` 必须是 `<episode-pid>/<token>.m4a`，不能用外层栏目列表的 PID 覆盖
联播单集自己的身份。只有 `NORMAL`、`FREE`、`isPrivateMedia: false`、`PUBLIC` 四项均
明确成立，且 `media.xyzcdn.net` 的 M4A URL 与 enclosure 完全一致时才继续；付费、私密、
登录态或字段缺失一律拒绝，也不会使用 cookie 或 token。即使处于已授权的单栏目
批量导入，每次调用也仍只下载 frozen manifest 中的一个规范单集 URL，并逐集执行
相同的公开状态和媒体身份校验。

如果 `__NEXT_DATA__` 明确暴露 transcript、subtitle 或 caption 文本、分段或 HTTPS
轨道 URL，脚本会在 `source.platform_metadata.subtitle` 中保留页面字段与规范化轨道，
并据此填充人工字幕或自动字幕语言列表。小宇宙页面常见的
`transcript.mediaId == media.id` / `transcriptMediaId == media.id` 只是音频身份占位，
不能据此声称存在字幕。未知候选字段、冲突标记、错误类型或没有公开文本/URL 的另一
裸 media ID 一律拒绝；脚本不会跟随字幕 URL，也不会调用需登录的字幕 API、cookie
或 token。发现规范化轨道后仍按上文 intake 契约停止，不启动音频 ASR。

每次采集会按固定顺序锁住最终音频和 metadata sidecar，直到音频探测、原子提升和 sidecar
原子写入全部结束，避免并发任务交错身份。小宇宙音频另在 staging 目标的系统级独占锁下，
先写入与媒体 URL 绑定的 partial 文件并实时限制总字节数。续传 checkpoint 原子记录 URL、
strong ETag、partial 大小和 SHA-256；每次续传前都会重算前缀哈希。只有 checkpoint 完整时才用 `Range`、
`If-Range`、精确 HTTP 206 和 `Content-Range` 续传，否则从零重下。请求固定为 identity
content encoding，编码响应、永久 4xx 与本地磁盘错误不会当作网络暂态重试。最终结果还会
用 `ffprobe`、发布页字节数、时长和 SHA-256 交叉校验；输出文件名必须使用小写 `.m4a`。

`--metadata-only` 遇到已有本地音频时，不会盲目复制旧 sidecar：它先校验规范 URL、旧
SHA-256 和当前 `eid`/`pid`/`media_id`，再重新探测大小与时长。任一身份或内容发生变化
都会拒绝复用并要求显式 `--overwrite`；没有本地音频时，新 sidecar 不写 `media` 字段。

## 处理单个 Qwen3-ASR 单集

Apple Silicon/MLX 上的中文单集使用 Qwen3-ASR 1.7B 8-bit 和
Qwen3-ForcedAligner 0.6B 8-bit：

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

Windows/CUDA 正式流程优先使用下文的批处理入口。它会调用
`transcribe_qwen3_asr_cuda.py`，并在 tracked metadata 中保留官方 Hub ID：
`Qwen/Qwen3-ASR-1.7B`、`Qwen/Qwen3-ForcedAligner-0.6B`，engine 为
`qwen-asr-transformers`。直接调用 worker 只用于单集诊断；同样必须提供本地
输入、raw 与 aligned 输出，并遵守恢复/覆盖语义。

有效的 `raw.json` 是转写检查点：缺少对齐产物时会从对齐阶段恢复；有效且身份匹配的 raw/aligned 会直接跳过。只有显式传入 `--retranscribe` 或 `--realign` 才会替换相应产物。

## 渲染逐字稿

对齐完成后，用同一次运行生成哈希关联的 refined JSON 和 Markdown。以下是 MLX 中文示例；
其他语言使用对应的 BCP 47 文件名和 `--language`：

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

手工渲染 CUDA 产物时，把 `--engine` 与 `--model` 分别改为
`qwen-asr-transformers` 和 `Qwen/Qwen3-ASR-1.7B`。正常批处理会自动传入正确值。

四份 Qwen 产物全部校验通过后，才把 run Markdown 作为单集根目录的正式
`transcript.<language>.md`，并同步更新单集 README 的来源、哈希和 workflow 状态。

## 串行批处理

`process_qwen3_asr_batch.py` 会让每个单集运行在独立子进程中，避免连续长任务积累
Metal 统一内存或 CUDA 显存状态。重复传入 `--episode` 可以限制处理范围。
Apple Silicon/MLX 示例：

```bash
env HF_ENDPOINT=https://hf-mirror.com HF_HUB_OFFLINE=1 \
  UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/process_qwen3_asr_batch.py \
  --backend mlx \
  --episode shows/<show-id>/episodes/<episode-folder> \
  --model-path .cache/models/qwen3-asr-1.7b-8bit \
  --aligner-path .cache/models/qwen3-forced-aligner-0.6b-8bit
```

Windows/CUDA 示例：

```powershell
& .cache/venvs/qwen-cuda/Scripts/python.exe scripts/process_qwen3_asr_batch.py `
  --backend cuda `
  --episode shows/<show-id>/episodes/<episode-folder> `
  --model-path .cache/models/Qwen3-ASR-1.7B `
  --aligner-path .cache/models/Qwen3-ForcedAligner-0.6B
```

`--backend cuda` 默认使用 `cuda:0`、`bfloat16`、SDPA、120 秒 chunk、batch size 1，
并按“ASR 模型完成并释放，再加载 ForcedAligner”的顺序控制显存。本机 NVIDIA RTX
A2000 8GB Laptop GPU 已验证适配这些默认值；只有目标 GPU 确实不支持 bf16 时才加
`--dtype float16`。同时提供 `--model-path` 与 `--aligner-path` 会强制设置
`HF_HUB_OFFLINE=1` 和 `TRANSFORMERS_OFFLINE=1`，禁止 worker 联网补取模型。

仓库同时包含中文和英文单集。批处理的 `--language` 与
`--transcript-language` 是整次运行共享的参数，默认值为 `Chinese` / `zh-CN`；
因此正式处理时必须按语言分组，并为每一集显式重复传入 `--episode`。不要在混合
语言仓库中省略 `--episode` 让脚本扫描所有缓存，更不要把这种全库扫描与
`--retranscribe` 或 `--realign` 组合。

技术上不传 `--episode` 时，脚本会发现所有已有缓存音频的单集；当前混合语言仓库
的正式流程不使用这个模式。对显式选中的同语言单集，它会串行启动 worker，在
`.cache/logs/qwen3-asr/` 保存每集日志，继续处理其他单集，并在任一单集失败时
最终返回非零状态。

默认按中文语音处理并生成 `transcript.zh-CN.md`。处理英文等其他语言时，同时
传入 ASR 使用的语言名称和用于产物文件名的 BCP 47 标签。以下继续以 MLX 为例；
Windows/CUDA 命令追加相同的两个语言参数即可：

```bash
env HF_ENDPOINT=https://hf-mirror.com HF_HUB_OFFLINE=1 \
  UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/process_qwen3_asr_batch.py \
  --backend mlx \
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
  --output .cache/benchmarks/<show-id>/<episode-folder>/whisper/raw.json \
  --model mlx-community/whisper-large-v3-turbo-q4 \
  --language zh
```

当前 Whisper worker 可能把引擎返回的 `NaN` 写入 raw JSON，而内容标准要求跟踪
的 JSON 为严格 JSON。正常新增单集不要创建、选择或提升新的 Whisper run；保留
已有基线即可。只有用户明确要求实验对比时才运行，并把新结果留在 `.cache/`，
同时在交付中说明该限制。

## 校验

运行单元测试：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python -m unittest discover -s tests -v
```

校验 Markdown、规范来源 URL、严格 JSON、Qwen 产物路径及 SHA-256 lineage：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/validate.py
```

首次 checkout 或 lockfile 变化后先安装锁定依赖：

```bash
npm --prefix apps/web ci
```

然后确认内容能够被前端严格加载并完成生产构建：

```bash
npm --prefix apps/web run check
```

最后还应运行 `git diff --check`，检查 `git status --short`，并确认根 README 的三列节目介绍表中，播客名称链接已核实的首选发布者页面，节目页链接本地节目 README。根 README 的单集表格采用“标题、访谈人物、播客名称、日期、总结、逐字稿”六列，节目 README 的单集表格仍采用“标题、播客名称、日期、总结链接、逐字稿链接”五列，且两处内容已经同步。根表的访谈人物来自单集 front matter 中 `role: guest` 的参与者；多位嘉宾使用顿号分隔。

完整编排顺序见[单集端到端处理流程](./episode-processing.md)，恢复语义和来源限制见
[PodWiki episode 处理 skill](../.agents/skills/podwiki-process-episode/SKILL.md)，
内容字段和状态定义见[内容标准](./content-standard.md)。
