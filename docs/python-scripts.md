# Python 脚本用法

本页集中记录 PodWiki 的 Python 工具和推荐运行方式。所有命令都从仓库根目录执行。
第一次新增单集时，先按[单集端到端处理流程](./episode-processing.md)确定目录、元数据、
语言分组和停止点，再回到本页复制具体命令。

## 环境准备

项目使用 Python 3.12 和 `uv 0.9.16`。媒体获取还要求系统可执行文件 `ffmpeg`、
`ffprobe`；YouTube 处理另外要求 Deno 或 Node.js。正式本地 Qwen ASR 支持两条
明确路径：Apple Silicon（macOS 14+ `arm64`）上的 MLX，以及 Windows x86-64 上的
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

`asr`（MLX）与 `asr-cuda` extras 互斥。媒体和目标 ASR extra 在同一次 locked
命令中同步，避免后一次安装卸载前一次依赖；不能组合两个互斥的 ASR extras。
Apple Silicon/MLX 使用：

```bash
uv sync --locked --extra media --extra asr
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
uv run --no-sync python <script> <arguments>
```

Windows/CUDA 建议使用被 Git 忽略的独立环境。首次创建并锁定依赖时：

```powershell
uv venv --python 3.12 .cache/venvs/qwen-cuda
. .\.cache\venvs\qwen-cuda\Scripts\Activate.ps1
uv sync --active --locked --extra media --extra asr-cuda
```

正式 worker 直接使用
`.cache/venvs/qwen-cuda/Scripts/python.exe`，不要在长任务运行期间同步依赖。

本页余下 `env UV_CACHE_DIR=.cache/uv ...` 示例在 PowerShell 中均省略该前缀，沿用上面已
设置的 `$env:UV_CACHE_DIR`。模型下载默认使用 Hugging Face 官方入口；仅当官方入口在
当前网络不可达时，才临时设置 `HF_ENDPOINT` 镜像。镜像只是传输入口，不是上游真实性
证明；完整 commit pin、每个下载 payload 的 metadata/ETag 与重新计算的 SHA-256
只负责锁定和复现取得的本地 snapshot，来源信任仍以官方 Hub 为准。MLX 的
`*-pinned-v2` 与 CUDA native 的 `*-pinned-v3` 目录都不得与缺少逐文件 metadata
的旧 snapshot/symlink cache 混用。

下载 Apple Silicon/MLX 使用的 Qwen3-ASR 和 ForcedAligner：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync hf download \
  mlx-community/Qwen3-ASR-1.7B-8bit \
  --revision a8379a2e2f9e313c9292cdf1af4055ab56d50d55 \
  --local-dir .cache/models/qwen3-asr-1.7b-8bit-pinned-v2

env UV_CACHE_DIR=.cache/uv uv run --no-sync hf download \
  mlx-community/Qwen3-ForcedAligner-0.6B-8bit \
  --revision 0e1a68e91d815300c7c9754b2a7639378b23db15 \
  --local-dir .cache/models/qwen3-forced-aligner-0.6b-8bit-pinned-v2
```

Windows/CUDA 使用官方模型：

```powershell
& .cache/venvs/qwen-cuda/Scripts/hf.exe download Qwen/Qwen3-ASR-1.7B-hf `
  --revision bcd2b5b7f32b480ab5790554cfa8347f246a14f3 `
  --local-dir .cache/models/Qwen3-ASR-1.7B-hf-pinned-v3
& .cache/venvs/qwen-cuda/Scripts/hf.exe download Qwen/Qwen3-ForcedAligner-0.6B-hf `
  --revision c07281df297b9905d24a508279258cccf987a064 `
  --local-dir .cache/models/Qwen3-ForcedAligner-0.6B-hf-pinned-v3
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
| `scripts/audit_correction_migration.py` | 重放按集修正规则并校验旧产物等价性 | JSON 审计报告 |

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

已有音频缺 sidecar 时，只有已从独立记录核对出原音频 SHA-256 才能恢复：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/acquire_media.py \
  --url <canonical-url> \
  --output .cache/media/<show-id>/<episode-folder>/source.m4a \
  --metadata-only --repair-metadata \
  --expected-sha256 <64位小写SHA-256>
```

该模式拒绝已存在 sidecar、错误 hash、来源身份漂移和访问状态变化；它不修改音频，
不伪造未知历史 `acquired_at`，只记录实际 `verified_at` / `recovered_at` 与 legacy
恢复标记。普通下载使用可恢复 transaction journal 成对提交音频和 sidecar。

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
env HF_HUB_OFFLINE=1 \
  UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/transcribe_qwen3_asr.py \
  --input .cache/media/<show-id>/<episode-folder>/source.m4a \
  --output shows/<show-id>/episodes/<episode-folder>/asr/qwen3-asr/raw.json \
  --aligned-output shows/<show-id>/episodes/<episode-folder>/asr/qwen3-asr/aligned.json \
  --model mlx-community/Qwen3-ASR-1.7B-8bit \
  --model-path .cache/models/qwen3-asr-1.7b-8bit-pinned-v2 \
  --aligner mlx-community/Qwen3-ForcedAligner-0.6B-8bit \
  --aligner-path .cache/models/qwen3-forced-aligner-0.6b-8bit-pinned-v2 \
  --language Chinese --no-verbose
```

Windows/CUDA 正式流程优先使用下文的批处理入口。它会调用
`transcribe_qwen3_asr_cuda.py`，并在 tracked metadata 中保留官方 Hub ID：
`Qwen/Qwen3-ASR-1.7B-hf`、`Qwen/Qwen3-ForcedAligner-0.6B-hf`，engine 为
`qwen-asr-transformers`，backend options 为 `transformers-native` 并记录精确
Transformers 版本。直接调用 worker 只用于单集诊断；同样必须提供本地
输入、raw 与 aligned 输出，并遵守恢复/覆盖语义。

有效的 v2 `raw.json` 是转写检查点：缺少对齐产物时会从对齐阶段恢复；有效且身份匹配的
raw/aligned 会直接跳过。markerless legacy 只允许完整链被校验并只读跳过；markerless
raw 缺 aligned、CUDA pending raw 需要 reconciliation，或请求 `--realign` 时都会在加载
运行时前失败，并提示 `--retranscribe`。不能用当前模型缓存给历史 raw 回填身份；只有
已有 native v2 raw 才可 align-only/`--realign`，且必须同时验证 pinned model/aligner
本地路径。旧 qwen-asr v2 raw 需要新对齐时同样失败关闭并要求 `--retranscribe`，不能
把旧 ASR raw 与 native aligner 混合。

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
`qwen-asr-transformers` 和 `Qwen/Qwen3-ASR-1.7B-hf`。正常批处理会自动传入正确值。

不带替换参数时，输入 hash、engine/model 和 transcript hash 全部匹配的现有 pair 会
直接 no-op；不匹配则失败关闭。只有已明确限定单集时才使用 `--rerender`。如需术语
修正，在该集 `asr/corrections.json` 写入：

```json
{
  "schema_version": 1,
  "episode_id": "<show-id>:<episode-key>",
  "version": 1,
  "input_asr_sha256": "<aligned.json SHA-256>",
  "rules": [
    {
      "id": "verified-name",
      "match": "机器误写",
      "replacement": "核实名称",
      "reason": "publisher metadata and human review",
      "case_sensitive": true,
      "expected_hits": 1
    }
  ]
}
```

map 必须绑定精确 `input_asr_sha256`。规则按顺序执行 literal replacement，不接受未
登记 regex。每条规则必须声明正数
`expected_hits`；实际命中变化会失败关闭。refined 会记录 map 路径/SHA-256、版本、
完整规则、预期命中和实际命中数。批处理自动读取该固定路径；成对写入通过
transaction journal 恢复，不能留下新旧 refined/Markdown 混合状态。

旧 refined 不批量回写 map provenance，避免仅为迁移元数据改变 14 集 selected artifact
哈希。CI 运行 `python scripts/audit_correction_migration.py`，以 map 内 aligned SHA 和
56 次预期命中重放 14 集，并逐字节校验现有 run Markdown、逐字段校验 segments/blocks；
新渲染则直接把 map SHA、版本、预期/实际命中写入 refined。

四份 Qwen 产物全部校验通过后，才把 run Markdown 作为单集根目录的正式
`transcript.<language>.md`，并同步更新单集 README 的来源、哈希和 workflow 状态。

## 串行批处理

`process_qwen3_asr_batch.py` 会让每个单集运行在独立子进程中，避免连续长任务积累
Metal 统一内存或 CUDA 显存状态。重复传入 `--episode` 可以限制处理范围。
Apple Silicon/MLX 示例：

```bash
env HF_HUB_OFFLINE=1 \
  UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/process_qwen3_asr_batch.py \
  --backend mlx \
  --episode shows/<show-id>/episodes/<episode-folder> \
  --model-path .cache/models/qwen3-asr-1.7b-8bit-pinned-v2 \
  --aligner-path .cache/models/qwen3-forced-aligner-0.6b-8bit-pinned-v2
```

Windows/CUDA 示例：

```powershell
& .cache/venvs/qwen-cuda/Scripts/python.exe scripts/process_qwen3_asr_batch.py `
  --backend cuda `
  --episode shows/<show-id>/episodes/<episode-folder> `
  --model-path .cache/models/Qwen3-ASR-1.7B-hf-pinned-v3 `
  --aligner-path .cache/models/Qwen3-ForcedAligner-0.6B-hf-pinned-v3 `
  --chunk-context 5
```

CUDA 的 120 秒参数表示每块独占的时间范围；worker 默认在两侧各增加 5 秒声学上下文。
重叠候选先完整转写、完整强制对齐，再以精确文本和时间约束的单一交接点分配边界；精确
锚点通常必须属于至少 3 个连续字符的匹配链；只有全局唯一的连续 2 字符匹配链，且两组
对齐时间差均不超过 250 ms 并记录严格置信证据时，才允许短链回退。aligned-gap 回退则要求整个空隙通过声学静音门禁。
短尾块会重新均分到最后两个归属区间，不会直接拼接两份重叠文字。找不到可靠交接点，或未对齐的长区间仍含持续活跃音频时，
本集失败关闭，不生成可选中的 complete 产物。raw checkpoint 会明确记录 `pending` / `complete`
归并状态；旧的无重叠产物必须使用 `--retranscribe` 更新。

coverage guard 会先汇总全部 chunk 的 owned alignment，再把全局并集裁剪到每个 ownership core；
覆盖区间与文字密度都来自全局相交 items，因此相邻 chunk 中跨越 core 边界的 item 仍能提供真实覆盖。
首部、内部或尾部的大空洞默认都要实际探测音频，持续活跃时拒绝。只有已经通过人工完整试听，
或有发布者章节、节目说明等证据确认是告别后的片尾时，才可对单个显式 episode 使用
`--realign --final-outro-exemption-seconds <seconds>`。该 CUDA-only 参数默认 `0`、最大 30 秒，
只豁免最后 core 的 trailing gap；必须在单集处理记录或 PR 说明中保留证据和实际秒数。
参数会写入 raw/aligned options 并受 raw SHA-256 lineage 约束。已有 v2 raw 缺少字段时
普通 resume 失败关闭；显式 `--realign` 会在其余 v2 lineage 完整匹配且新对齐通过后
安全升级该字段。markerless legacy raw 不适用该迁移，必须 `--retranscribe`。

`--backend cuda` 默认使用 `cuda:0`、`bfloat16`、SDPA、120 秒 chunk、batch size 1，
并按“ASR 模型完成并释放，再加载 ForcedAligner”的顺序控制显存。native adapter
已有 mocked API 与恢复契约测试，但 NVIDIA RTX A2000 的 golden-output、峰值显存和
长音频实机资格仍待完成；通过前不能声称硬件验证或提升新产物。只有目标 GPU 确实
不支持 bf16 时才加 `--dtype float16`。同时提供 `--model-path` 与 `--aligner-path` 会强制设置
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
env HF_HUB_OFFLINE=1 \
  UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/process_qwen3_asr_batch.py \
  --backend mlx \
  --episode shows/<show-id>/episodes/<episode-folder> \
  --language English --transcript-language en \
  --model-path .cache/models/qwen3-asr-1.7b-8bit-pinned-v2 \
  --aligner-path .cache/models/qwen3-forced-aligner-0.6b-8bit-pinned-v2
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

Whisper worker 会在写入前拒绝 `NaN`、`Infinity` 或不可序列化值，并且拒绝任何不在
`.cache/benchmarks/` 下的输出路径。既有两份历史 raw 中的 `avg_logprob: NaN` 已
规范为 JSON `null`，没有改动文本或时间戳。新结果仍只用于显式实验对比，不得选择、
提升或提交为正式 run。

## 校验

运行单元测试：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python -m unittest discover -s tests -v
```

校验 Markdown、规范来源 URL、严格 JSON、Qwen 产物路径及 SHA-256 lineage：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/validate.py
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/audit_correction_migration.py
```

首次 checkout 或 lockfile 变化后先安装锁定依赖：

```bash
npm --prefix apps/web ci
npm --prefix apps/web exec -- playwright install --with-deps chromium
```

然后确认内容能够被前端严格加载并完成生产构建：

```bash
npm --prefix apps/web run check
npm --prefix apps/web audit --audit-level=high
```

最后还应运行 `git diff --check`，检查 `git status --short`，并确认根 README 的三列节目介绍表中，播客名称链接已核实的首选发布者页面，节目页链接本地节目 README。根 README 的单集表格采用“标题、访谈人物、播客名称、日期、总结、逐字稿”六列，节目 README 的单集表格仍采用“标题、播客名称、日期、总结链接、逐字稿链接”五列，且两处内容已经同步。根表的访谈人物来自单集 front matter 中 `role: guest` 的参与者；多位嘉宾使用顿号分隔。

完整编排顺序见[单集端到端处理流程](./episode-processing.md)，恢复语义和来源限制见
[PodWiki episode 处理 skill](../.agents/skills/podwiki-process-episode/SKILL.md)，
内容字段和状态定义见[内容标准](./content-standard.md)。
