# PodWiki 单集端到端处理流程

本文是新人和通用 AI 新增或继续处理单集时的统一入口。它规定执行顺序、停止点、
产物和完成门禁；字段契约以[内容标准](./content-standard.md)为准，具体 CLI 参数以
[脚本用法](./python-scripts.md)为准，来源限制与恢复策略同时遵守
[项目处理 skill](../.agents/skills/podwiki-process-episode/SKILL.md)。

## 1. 适用范围与停止条件

当前完整 happy path 是：单个公开 Bilibili 视频，没有可直接使用的公开字幕，在
Apple Silicon 上以 Qwen3-ASR 和 ForcedAligner 生成机器逐字稿。YouTube 当前支持
规范化、metadata intake 和公开媒体获取，但 tracked episode 的 source identifiers
与无正式期号 key 尚未形成内容契约，因此不能自动完成入库。

先根据请求确定停止点：

- 只检查来源：完成第 3 节，把 intake sidecar 留在 `.cache/` 后报告；
- 只获取媒体：完成第 5 节，只保留 `.cache/` 音频和 sidecar；新单集不创建或提交
  不完整的 README、总结与逐字稿；
- 只转写：按请求停在 raw 或 aligned 检查点，报告尚未达到可发布状态；
- 新增或完整处理：继续完成全文档、双索引和第 11 节全部门禁。

部分流程不以 Web 构建通过为完成条件，也不得把缓存检查点提交为一个完整单集。

遇到以下情况时停止自动流程并报告，不自行寻找绕过方式：

- 登录、会员、付费、地区、年龄或其他访问控制；
- 找到公开字幕：仓库目前只有字幕发现能力，尚无下载、转换和 lineage 导入工具；
- 只有本地媒体但没有可核实的来源与授权记录；
- 非 Apple Silicon 环境需要新跑正式 ASR；
- YouTube 单集需要完整入库：当前尚未定义 tracked source identifiers，且无正式
  期号时也没有稳定 episode key；
- 新节目没有可核实的 Bilibili 频道或空间：当前根节目索引契约无法登记；
- 需要远端或付费 ASR，但用户没有明确授权数据传输、凭据和费用。

不要把停止条件改写为成功。每集分别报告已到达阶段、已有产物、可恢复点和下一步。

## 2. 开始前检查

先确认工作树和现有产物，避免覆盖其他人的工作：

```bash
git status -sb
git branch --show-current
```

完整本地流程需要：

- Python 3.12+、`uv`；
- `ffmpeg`、`ffprobe`；
- macOS Apple Silicon 和 MLX，用于当前正式本地 ASR；
- Deno 或 Node.js，用于 YouTube 获取；
- Node.js 和 npm，用于最终 Web 门禁。

```bash
python3 --version
uv --version
ffmpeg -version
ffprobe -version
node --version
npm --version
```

先同步一次依赖。多个 worker 之后都使用 `--no-sync`，不能并发修改共享 `.venv`：

```bash
uv sync --all-groups
env UV_CACHE_DIR=.cache/uv uv run --no-sync hf --help
```

首次 checkout 或 `apps/web/package-lock.json` 变化后安装锁定的前端依赖：

```bash
npm --prefix apps/web ci
```

首次准备 Qwen 模型时：

```bash
export HF_ENDPOINT=https://hf-mirror.com
env UV_CACHE_DIR=.cache/uv uv run --no-sync hf download \
  mlx-community/Qwen3-ASR-1.7B-8bit \
  --local-dir .cache/models/qwen3-asr-1.7b-8bit
env UV_CACHE_DIR=.cache/uv uv run --no-sync hf download \
  mlx-community/Qwen3-ForcedAligner-0.6B-8bit \
  --local-dir .cache/models/qwen3-forced-aligner-0.6b-8bit
```

模型、媒体、sidecar、日志和翻译检查点全部放在 `.cache/`，不得提交 Git。

## 3. 规范化来源并做 metadata intake

先把用户输入转换为单视频规范 URL：

- Bilibili：`https://www.bilibili.com/video/<BVID>/`；
- Bilibili 活动页 `/festival/...?...bvid=<BVID>`：提取 `bvid` 后改写为上述视频地址；
- YouTube：`https://www.youtube.com/watch?v=<video-id>`；
- 删除 `spm_id_from`、`vd_source`、播放列表和其他追踪参数。

不要把活动页直接传给脚本。先用来源 ID 做临时 intake，只读取元数据而不下载：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/acquire_media.py \
  --url <canonical-url> \
  --output .cache/intake/<source-id>/source.m4a \
  --metadata-only
```

检查 `.cache/intake/<source-id>/source.metadata.json`：

1. `source.canonical_url` 与输入的规范 URL 一致；
2. Bilibili 的 `source.bvid`、`source.aid`、`source.cid`、`source.page` 完整且
   身份一致；
3. `source.title`、发布者、发布时间和时长合理；
4. `source.availability`、`source.live_status` 和平台字段表明来源公开、非直播、
   非受限；
5. `source.subtitle_languages`、`source.automatic_caption_languages` 和
   `source.platform_metadata.subtitle.tracks` 均无可用公开字幕。

存在公开字幕时在这里停止。不要因为当前没有 importer 就忽略字幕改跑音频 ASR。

## 4. 确定身份并创建目录

先确认节目是否已经存在于 `shows/<show-id>/`。新节目必须有可核实的 Bilibili
频道或空间，使用 `templates/show/README.md`，节目 ID 只使用稳定的小写 ASCII
字母和数字。

只有确认节目尚不存在时才创建节目目录：

```bash
mkdir -p shows/<show-id>
cp -n templates/show/README.md shows/<show-id>/README.md
```

单集身份按以下顺序确定：

1. 只有发布者明确给出的正式期号才能写入 `episode_number`；
2. 有正式期号时，`episode_key` 使用保留前导零的正式编号；
3. 无正式期号的 Bilibili 视频使用 `bili-<lowercase-bvid>`；
4. 不根据输入顺序、发布日期、合集位置或抓取顺序猜期号；
5. YouTube 单集当前只完成 intake/acquire；完整入库前请求维护者补充 source
   identifiers 和稳定 episode key 契约。

目录名为 `<episode-key>-<short-slug>`，但 front matter 中的
`<show-id>:<episode-key>` 才是稳定主键。如果目录已经存在，检查并续跑，不再复制
模板；只有“新增或完整处理”且目录全新时才执行。只获取媒体时确定路径即可，不创建
跟踪文件：

```bash
mkdir -p shows/<show-id>/episodes/<episode-folder>
cp -n templates/episode/README.md shows/<show-id>/episodes/<episode-folder>/README.md
```

根据 intake sidecar 和已核实的发布者材料填写模板，不能保留示例占位符：

| sidecar / 已核实来源 | 单集字段 |
| --- | --- |
| `source.canonical_url` | `sources[].url` |
| `source.bvid`、`source.aid`、`source.cid`、`source.page` | `sources[].identifiers` |
| 发布者原标题 | `title` |
| 发布时间 | 带时区 RFC 3339 `published_at` |
| `source.duration_seconds` | 换算为整数毫秒 `duration_ms` |
| `source.language` 或核实后的实际口语 | BCP 47 `language`；不能沿用模板默认值猜测 |
| 已核实嘉宾 | `participants`，嘉宾使用 `role: guest` |
| 嘉宾与精简主题 | `navigation_title`，格式为“人物 · 题目” |
| 独特主题词 | `catalog_keyword` |

元数据只在完成来源核验后标为 `verified`。尚未取得音频时保持
`workflow.transcript: not-started`；基于发布者简介或章节的内容只能是
`workflow.summary: outline`，不能冒充完整总结。

## 5. 下载并核验音频

确定最终目录后，把来源下载到规范 cache 位置：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/acquire_media.py \
  --url <canonical-url> \
  --output .cache/media/<show-id>/<episode-folder>/source.m4a
```

必须同时存在 `source.m4a` 和 `source.metadata.json`。脚本会检查 codec、时长、
大小、采样率、声道和 SHA-256；把这些真实值记录进单集 README 的
`local_audio_cache` 后，才能将状态改为 `source-acquired`。默认复用身份和哈希匹配
的已有音频；只有用户明确要求覆盖时才用 `--overwrite`。

## 6. 按语言串行运行 Qwen ASR

批处理的语言参数作用于整次运行，而且默认是 `Chinese` / `zh-CN`。仓库包含中英文
单集，所以必须按语言分组，并用重复的 `--episode` 显式列出本次范围。不要省略
`--episode` 扫描全部缓存，也不要把全库扫描与 `--retranscribe` 或 `--realign`
组合。

中文组：

```bash
env HF_ENDPOINT=https://hf-mirror.com HF_HUB_OFFLINE=1 \
  UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/process_qwen3_asr_batch.py \
  --episode shows/<show-id>/episodes/<episode-folder> \
  --model-path .cache/models/qwen3-asr-1.7b-8bit \
  --aligner-path .cache/models/qwen3-forced-aligner-0.6b-8bit
```

英文组：

```bash
env HF_ENDPOINT=https://hf-mirror.com HF_HUB_OFFLINE=1 \
  UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/process_qwen3_asr_batch.py \
  --episode shows/<show-id>/episodes/<episode-folder> \
  --language English \
  --transcript-language en \
  --model-path .cache/models/qwen3-asr-1.7b-8bit \
  --aligner-path .cache/models/qwen3-forced-aligner-0.6b-8bit
```

脚本内部逐集、逐子进程串行运行，不再并发启动额外 Metal worker。每集产物为：

```text
asr/qwen3-asr/raw.json
asr/qwen3-asr/aligned.json
asr/qwen3-asr/refined.json
asr/qwen3-asr/transcript.<language>.md
```

`raw.json` 是恢复检查点：有效 raw 缺 aligned 时只重跑对齐，身份匹配的 raw/aligned
会跳过。仅在用户明确要求替换时使用 `--retranscribe` 或 `--realign`。已经完整的单集
不要为了“确认一下”重跑批处理；直接运行 validator，避免 renderer 产生无意义变更。

需要暂停时用正常的中断信号结束当前 worker，不删除已经完成的原子产物。每集日志在
`.cache/logs/qwen3-asr/<show-id>--<episode-folder>.log`。批处理失败后先读对应日志和
末尾 JSON 汇总，再用相同语言参数、单个显式 `--episode` 只重跑失败单集。

MLX Whisper 目前只保留既有历史基线。worker 可能输出非严格 JSON 的 `NaN`，正常
新增单集不要创建、选择或提升新的 Whisper run。明确要求实验时只输出到
`.cache/benchmarks/`。

## 7. 提升正式逐字稿并记录 provenance

批处理只生成 run 目录产物，不会自动完成下面任何一步。先检查四份 Qwen 产物、
时间戳顺序和 lineage，再把 run Markdown 原样复制为根正式稿：

根正式稿已经存在时，先比较内容；不同则停止，只有用户明确授权替换后才能覆盖。
以下 `-n` 会保护已有文件，随后用 `cmp` 确认 selected run 与根文件字节一致：

```bash
cp -n shows/<show-id>/episodes/<episode-folder>/asr/qwen3-asr/transcript.<language>.md \
  shows/<show-id>/episodes/<episode-folder>/transcript.<language>.md
cmp -s shows/<show-id>/episodes/<episode-folder>/asr/qwen3-asr/transcript.<language>.md \
  shows/<show-id>/episodes/<episode-folder>/transcript.<language>.md
```

需要记录哈希时使用实际文件计算，不复制旧值：

```bash
shasum -a 256 shows/<show-id>/episodes/<episode-folder>/transcript.<language>.md
shasum -a 256 shows/<show-id>/episodes/<episode-folder>/asr/qwen3-asr/raw.json
shasum -a 256 shows/<show-id>/episodes/<episode-folder>/asr/qwen3-asr/aligned.json
shasum -a 256 shows/<show-id>/episodes/<episode-folder>/asr/qwen3-asr/refined.json
```

更新单集 README：

- `workflow.transcript: machine`；
- `transcript.path`、语言、获取方式、engine、model、aligner、options、生成时间；
- 音频身份、质量和性能统计；
- `asr_artifacts` 的仓库相对 POSIX 路径；
- `asr_runs` 中只有当前选中 Qwen run 标记为 `selected`；
- 既有其他 run 保留为 `candidate` 或 `superseded`，不得删除。

根正式稿必须与 selected run Markdown 字节一致。所有路径、哈希和统计都从本次真实
产物读取，不能照抄另一集或模板默认值。

中文集完成上述元数据后可以运行 `scripts/validate.py` 检查整条链。英文集在第 8 节
译稿尚未完成前会触发预期的“缺少中文译稿”错误；必须完成译稿再以全库 validator
作为最终结果，不能把中间失败报告成校验通过。

## 8. 英文正式稿生成逐行中文译稿

当正式稿是 `transcript.en.md` 时，英文仍是 selected 原文；根目录必须另有
`transcript.zh-CN.md`，并登记在 `transcript.translations`，不能放进 `asr/`。

长稿使用可恢复的逐段流程：

1. 固定英文源文件并先计算 SHA-256；翻译期间源文件不得变化；
2. 按连续 segment 范围分块，每块保留源行号、首尾时间戳和术语表；
3. 中间结果写入 `.cache/translations/<show-id>/<episode-folder>/`；
4. 每个英文 segment 只生成一个中文 segment，保留相同时间戳和 Markdown 硬换行；
5. 逐块检查无合并、拆分、遗漏、增行和时间戳漂移，再按原顺序组装；
6. 对开头、中段、结尾、姓名、公司、模型和关键数字做语义抽样；
7. 计算最终中译稿 SHA-256，填写 `source_sha256`、`sha256`、RFC 3339
   `generated_at` 和真实审核状态。

结构完成后由 `scripts/validate.py` 检查标题、行数、逐行时间戳、顺序和哈希。自动
校验不能证明翻译语义正确；未经人工逐段审核保持 `status: machine`。

## 9. 基于完整正式稿生成总结

总结使用根目录当前 selected 正式稿，不使用平台简介代替完整内容。长稿先按连续
时间范围形成带时间码的局部提纲，再综合为 `summary.zh-CN.md`；中间笔记放 `.cache/`
而不是提交。

首次开始完整总结时再复制总结模板，避免把占位内容误当成已完成总结：

```bash
cp -n templates/episode/summary.zh-CN.md \
  shows/<show-id>/episodes/<episode-folder>/summary.zh-CN.md
```

必须遵守总结模板和内容标准：

- 一句话总结、为什么值得听、语义化逻辑速览表；
- 核心观点按“嘉宾主张、依据与经历、边界、原文定位”展开；
- 5 分钟读完、主题导航、事实边界与待核实项；
- 每个关键结论回到正式逐字稿核对时间码；
- 区分嘉宾陈述、发布者材料、PodWiki 归纳和独立核查；
- 不从 ASR 错字推导高影响事实，不编造逐字稿中不存在的因果关系。

更新 `summary.source_transcript` 的真实 path、engine、model、selection status 和
SHA-256。完整机器稿可以支持 `workflow.summary: draft`；没有回听、术语校对和必要
事实核查时不得标记 `reviewed`。

## 10. 同步两个 Wiki 索引

每次新增或更新单集都同时修改：

1. 新节目还要更新根 `README.md` 的三列“收录播客”表，节目名链接已核实的
   Bilibili 频道或空间，节目页链接本地 README；
2. 根 `README.md` 的六列表：标题、访谈人物、播客名称、日期、总结、逐字稿；
3. `shows/<show-id>/README.md` 的五列表：标题、播客名称、日期、总结链接、逐字稿链接。

标题链接规范发布者 URL，访谈人物只来自 `role: guest` 的已核实参与者。英文单集
同时提供“英文逐字稿”和“中文机器翻译”链接。当前 validator 不检查根 README，
因此两个表的排序、列数、人物和相对路径必须人工复核。

## 11. 统一完成门禁

从仓库根目录依次运行：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python -m unittest discover -s tests -v
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/validate.py
npm --prefix apps/web run check
git diff --check
git status --short
```

最后确认：

- `.cache/` 媒体、模型、日志和检查点仍被忽略；
- 预期的 README、总结、逐字稿和 ASR JSON 可被 Git 跟踪；
- selected Qwen 根逐字稿与 run Markdown 字节一致；
- 英文集的中文译稿结构和两个 SHA-256 均通过；
- 根索引和节目索引同步；
- 没有把 `machine`、`draft` 错标为 `reviewed`。

只有用户明确授权发布时，才创建分支、显式暂存本次审查过的路径、提交、推送和
创建 PR；不得用全量暂存命令把无关工作带入提交。没有远端 CI 时，应明确报告上述
本地门禁结果，不能声称 CI 已通过。

## 12. 每集交付报告

无论完成还是中断，每集分别报告：

- 规范来源 URL、show/episode ID；
- 已到达状态与可恢复点；
- 媒体、raw、aligned、refined、正式逐字稿、译稿和总结的实际路径；
- ASR engine/model/aligner 与语言；
- Python、仓库、Web 和 Git 门禁结果；
- 剩余人工回听、术语、翻译或事实核查；
- 任何访问、字幕、平台、环境或授权 blocker。
