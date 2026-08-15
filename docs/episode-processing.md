# PodWiki 单集端到端处理流程

本文是新人和通用 AI 新增或继续处理单集时的统一入口。它规定执行顺序、停止点、
产物和完成门禁；字段契约以[内容标准](./content-standard.md)为准，具体 CLI 参数以
[脚本用法](./python-scripts.md)为准，来源限制与恢复策略同时遵守
[项目处理 skill](../.agents/skills/podwiki-process-episode/SKILL.md)。

## 1. 适用范围与停止条件

当前完整 happy path 是：单个已通过播客边界核实、可匿名访问或经用户明确授权
登录态访问的公开免费 Bilibili 视频版单集或小宇宙单集，没有可直接使用的字幕，
在 Apple Silicon/MLX 或 Windows/NVIDIA CUDA 上以 Qwen3-ASR 和 ForcedAligner
生成机器逐字稿。
PodWiki 只收录符合[内容标准第 0 节](./content-standard.md#0-收录边界只收录播客)的
播客完整单集；长视频、访谈或频道投稿本身不构成收录依据。
用户明确授权时，也可以把一个已核实播客的公开免费单集作为冻结后的有界批次处理：
Bilibili 只允许官方播客正片合集或与公开播客 feed 逐集对应的白名单，小宇宙只允许
同一已核实栏目；批次中的每一集仍执行同一套单集流程和停止条件。
YouTube 当前支持规范化、metadata intake 和公开媒体获取，但 tracked episode 的
source identifiers 与无正式期号 key 尚未形成内容契约，因此不能自动完成入库。

先根据请求确定停止点：

- 只检查来源：完成第 3 节，把 intake sidecar 留在 `.cache/` 后报告；
- 只获取媒体：完成第 5 节，只保留 `.cache/` 音频和 sidecar；新单集不创建或提交
  不完整的 README、总结与逐字稿；
- 只转写：按请求停在 raw 或 aligned 检查点，报告尚未达到可发布状态；
- 新增或完整处理：继续完成全文档、双索引和第 11 节全部门禁。

部分流程不以 Web 构建通过为完成条件，也不得把缓存检查点提交为一个完整单集。

遇到以下情况时停止自动流程并报告，不自行寻找绕过方式：

- 需要登录态，但用户没有明确授权具体平台、登录身份与来源范围，或当前采集路径
  无法在不泄露凭据并保留完整来源 sidecar 的前提下使用该登录态；
- 会员专属、付费、私密、地区、年龄或其他受限内容；
- 找到当前授权访问上下文可用的字幕：仓库目前只有字幕发现能力，尚无下载、转换和
  lineage 导入工具；
- 只有本地媒体但没有可核实的来源与授权记录；
- 当前机器既不满足 Apple Silicon/MLX，也不满足 Windows x86-64/NVIDIA CUDA
  本地路径，却需要新跑正式 ASR；
- YouTube 单集需要完整入库：当前尚未定义 tracked source identifiers，且无正式
  期号时也没有稳定 episode key；
- 新节目没有可核实的首选发布者页面：当前根节目索引契约无法登记；
- 单集没有任何可核实的实际出场人物：无法按内容标准形成导航标题；不得从标题
  猜测人物，也不得把一般参与者或主播伪标为嘉宾；
- 需要远端或付费 ASR，但用户没有明确授权数据传输、凭据和费用。

不要把停止条件改写为成功。每集分别报告已到达阶段、已有产物、可恢复点和下一步。

## 2. 开始前检查

先确认工作树和现有产物，避免覆盖其他人的工作：

```bash
git status -sb
git branch --show-current
```

完整本地流程需要：

- Python 3.12、`uv 0.9.16`；
- `ffmpeg`、`ffprobe`；
- macOS 14+ Apple Silicon/MLX，或 Windows x86-64/NVIDIA CUDA，用于正式本地 ASR；
  新的 Transformers-native Windows CUDA adapter 尚未完成 RTX A2000 的 golden-output、
  峰值显存和长音频实机资格验证，完成前不能声称已通过硬件证明或提升其新产物；
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

MLX 与 CUDA extras 互斥，按本机平台只同步其中一个。媒体与对应 ASR extra 必须在
同一次命令中安装，避免后一次同步卸载前一次依赖；不要组合两个互斥的 ASR extras。
Apple Silicon/MLX 使用：

```bash
uv sync --locked --extra media --extra asr
env UV_CACHE_DIR=.cache/uv uv run --no-sync hf --help
```

Windows/CUDA 建议使用被 Git 忽略的独立环境，避免改写项目 `.venv`。首次创建时：

```powershell
$env:UV_CACHE_DIR = ".cache/uv"
uv venv --python 3.12 .cache/venvs/qwen-cuda
. .\.cache\venvs\qwen-cuda\Scripts\Activate.ps1
uv sync --active --locked --extra media --extra asr-cuda
```

之后的 CUDA 命令直接调用
`.cache/venvs/qwen-cuda/Scripts/python.exe`，不在 worker 运行期间同步依赖。

PowerShell 先设置 `$env:UV_CACHE_DIR = ".cache/uv"`，再省略命令前的 POSIX `env`
写法；`export` 与反斜杠续行的替换规则见[脚本用法](./python-scripts.md#环境准备)。

首次 checkout 或 `apps/web/package-lock.json` 变化后安装锁定的前端依赖：

```bash
npm --prefix apps/web ci
npm --prefix apps/web exec -- playwright install --with-deps chromium
```

首次准备 Apple Silicon/MLX 模型时，默认直接使用 Hugging Face 官方入口：

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

Windows/CUDA 使用官方非量化模型，并继续只写入 `.cache/models/`：

```powershell
& .cache/venvs/qwen-cuda/Scripts/hf.exe download Qwen/Qwen3-ASR-1.7B-hf `
  --revision bcd2b5b7f32b480ab5790554cfa8347f246a14f3 `
  --local-dir .cache/models/Qwen3-ASR-1.7B-hf-pinned-v3
& .cache/venvs/qwen-cuda/Scripts/hf.exe download Qwen/Qwen3-ForcedAligner-0.6B-hf `
  --revision c07281df297b9905d24a508279258cccf987a064 `
  --local-dir .cache/models/Qwen3-ForcedAligner-0.6B-hf-pinned-v3
```

只有官方入口在当前网络不可达时，才可临时把 `HF_ENDPOINT` 指向镜像；镜像仅是下载
传输层，不是上游真实性证明。完整 commit pin、每个下载 payload 对应的 metadata/ETag
与重新计算的 SHA-256 用于锁定和复现已取得的本地 snapshot，来源信任仍以官方 Hub
为准。CUDA native 的 `*-pinned-v3` 使用新目录，避免把旧的 qwen-asr snapshot 或
symlink cache 误当作 native v2 identity；不得复用或覆盖没有逐文件 download
metadata 的旧模型目录。MLX 继续使用其独立的 `*-pinned-v2` 目录。

模型、媒体、sidecar、日志和翻译检查点全部放在 `.cache/`，不得提交 Git。用户明确
授权登录态下载时，优先直接使用现有浏览器会话；确需导出 cookie、token 或浏览器
配置时，只能临时写入 `.cache/credentials/`，不得打印、写入 sidecar 或日志，并在
本次采集结束后清理临时副本。

## 3. 规范化来源并做 metadata intake

先把用户输入转换为单视频或单集规范 URL。规范化只确认来源身份，不代表获得收录
资格；包括单个 BVID/视频在内，下载或建档前仍须正面证明它属于已核实播客且是完整
正式单集：

- Bilibili：`https://www.bilibili.com/video/<BVID>/`；
- Bilibili 活动页 `/festival/...?...bvid=<BVID>`：提取 `bvid` 后改写为上述视频地址；
- YouTube：`https://www.youtube.com/watch?v=<video-id>`；
- 小宇宙：`https://www.xiaoyuzhoufm.com/episode/<episode-id>`；栏目页用于登记节目
  身份，也可在明确授权的单栏目批次中发现单集，但不能作为媒体获取输入；
- 删除 `spm_id_from`、`vd_source`、播放列表和其他追踪参数。

登录本身不再构成停止条件。需要登录态时，必须先记录用户明确授权的平台、登录身份
别名和本次规范来源或冻结 manifest 范围，再以同一访问上下文完成字幕检查与媒体获取；
只记录 `anonymous` 或 `authenticated` 等非敏感访问方式，不记录 cookie、token、账号
标识或浏览器配置路径。登录态不得用于扩大节目范围，也不得纳入会员专属、付费、私密、
地区或其他受限内容。

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
3. 小宇宙的 `source.eid`、`source.pid`、`source.media_id` 完整，页面中的
   episode/podcast/media 身份一致，并明确为 `NORMAL`、`FREE`、非私密、`PUBLIC`；
4. `source.title`、发布者、发布时间和时长合理；
5. `source.availability`、`source.live_status` 和平台字段表明来源公开免费、非直播、
   非会员专属、非付费、非私密且不受地区或其他访问限制；登录态只影响传输上下文；
6. `source.subtitle_languages`、`source.automatic_caption_languages` 和
   `source.platform_metadata.subtitle.tracks` 均无当前授权访问上下文可用的字幕。

存在可用字幕时在这里停止。不要因为当前没有 importer 就忽略字幕改跑音频 ASR。

### 明确授权的单播客批次

未获授权时仍只处理用户指定的单集，不枚举整栏。只有用户明确点名并授权一个已
核实的播客后，才可以发现它匿名或经授权登录态可见的公开免费完整单集；不得把授权
扩大到其他节目、账号
投稿或平台列表。下载任何媒体前先把本次范围冻结到
`.cache/intake/<show-id>/manifest.json`，至少记录：

- Bilibili：频道规范 URL 与 `mid`、明确标为播客正片的官方 `season_id` 与合集标题，
  或用于逐集交叉对应的公开播客 feed 规范 URL；每集规范 URL 与 BVID，使用 feed
  交叉核实时还要记录对应 GUID 和单集 URL；
- 小宇宙：栏目规范 URL、栏目 PID，以及每集规范 URL 与 `eid`；
- 冻结时间、白名单总数和播客身份/完整单集证据；后续校验结果写入各集 intake
  sidecar，不改写清单范围；
- 稳定顺序仅用于执行和复核，不作为正式期号。

冻结后不因节目新增单集而自动扩展本次批次。Bilibili 混合频道只允许白名单中的完整
播客正片，片段、直播、活动、课程和其他投稿保持排除；每集还要在实际授权访问上下文中
独立通过访问状态、单 P、来源身份和字幕检查。小宇宙只有栏目身份一致且明确为
`NORMAL`、`FREE`、非私密、`PUBLIC` 的条目才能进入下载清单。跨节目、未知状态、
会员专属、付费、私密、地区限制，或虽需登录但未获本次明确授权的条目，以及其他
不满足播客边界的条目必须拒绝并记录原因。随后严格按 manifest 串行、限速调用单集
采集命令，每次仍只传入一个规范单集 URL，并在进入下一集前完成该集的身份、sidecar、
字节数、时长与 SHA-256 校验。中断后从冻结的 manifest 和已验证 sidecar 恢复，不
重新发现或静默替换批次范围。

## 4. 确定身份并创建目录

先确认节目是否已经存在于 `shows/<show-id>/`。新节目必须有可核实的首选发布者
页面，使用 `templates/show/README.md`，节目 ID 只使用稳定的小写 ASCII
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
4. 无正式期号的小宇宙单集使用 `xiaoyuzhou-<eid>`；
5. 不根据输入顺序、发布日期、合集位置或抓取顺序猜期号；
6. YouTube 单集当前只完成 intake/acquire；完整入库前请求维护者补充 source
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
| `source.eid`、`source.pid`、`source.media_id` | 小宇宙 `sources[].identifiers` |
| 发布者原标题 | `title` |
| 发布时间 | 带时区 RFC 3339 `published_at` |
| `source.duration_seconds` | 换算为整数毫秒 `duration_ms` |
| `source.language` 或核实后的实际口语 | BCP 47 `language`；不能沿用模板默认值猜测 |
| 已核实出场人物 | `participants`；区分 `guest`、一般 `participant` 与 `host` |
| 已登记人物来源或经回听确认的嘉宾自述 | `participants[].profile` |
| 证据化人物与精简主题 | `navigation_title`；guest 优先，其次 participant、host |
| 独特主题词 | `catalog_keyword` |

`participants[].profile` 是可选的嘉宾背景；没有充分资料时删除模板中的整个
`profile`，不能保留占位内容。填写时必须遵守以下顺序：

1. 先把发布者人物介绍、机构主页等依据的规范 URL 登记到本集 `sources`；嘉宾在
   本集中的明确自述可以使用已登记的节目来源作为依据；
2. 机器 ASR 和发布者标题只能帮助定位，不能据此猜测学历、公司、职位或在职状态；
   使用嘉宾自述时回听对应音频，或确认所用逐字稿已经人工核对；
3. 填写必需的 `headline` 和 `checked_at: YYYY-MM-DD`；`bio` 可省略；
4. `affiliations` 条目的 `organization` 必填，`title` 可省略，`status` 只能是
   `current` 或 `former`；`education` 条目的 `institution` 必填，`credential`
   和 `field` 可省略；未知列表可以省略或写为空列表，不得补猜；
5. `status: current` 只表示截至 `checked_at` 仍属当前关系。更新背景时重新核实
   全部当前关系并同步日期，不能把旧资料描述成当前状态。

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

音频已存在但 sidecar 因旧流程或中断缺失时，不得直接手写来源身份。只有已从既有
README/raw 等独立记录核对出音频 SHA-256，才运行显式恢复：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/acquire_media.py \
  --url <canonical-url> \
  --output .cache/media/<show-id>/<episode-folder>/source.m4a \
  --metadata-only --repair-metadata \
  --expected-sha256 <64位小写SHA-256>
```

恢复会重新匿名核实来源身份、访问状态、ffprobe、时长、大小和 hash，只原子写 sidecar。
未知的历史 `acquired_at` 不会伪造；sidecar 记录真实 `verified_at`、`recovered_at` 与
`recovery.acquired_at_status: unknown-legacy`。正常下载则以事务 journal 绑定音频与
sidecar；若进程在两次提升之间中断，下一次相同目标调用会先完成该事务。

## 6. 按语言串行运行 Qwen ASR

批处理的语言参数作用于整次运行，而且默认是 `Chinese` / `zh-CN`。仓库包含中英文
单集，所以必须按语言分组，并用重复的 `--episode` 显式列出本次范围。不要省略
`--episode` 扫描全部缓存，也不要把全库扫描与 `--retranscribe` 或 `--realign`
组合。

Apple Silicon/MLX 中文组：

```bash
env HF_HUB_OFFLINE=1 \
  UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/process_qwen3_asr_batch.py \
  --backend mlx \
  --episode shows/<show-id>/episodes/<episode-folder> \
  --model-path .cache/models/qwen3-asr-1.7b-8bit-pinned-v2 \
  --aligner-path .cache/models/qwen3-forced-aligner-0.6b-8bit-pinned-v2
```

Apple Silicon/MLX 英文组：

```bash
env HF_HUB_OFFLINE=1 \
  UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/process_qwen3_asr_batch.py \
  --backend mlx \
  --episode shows/<show-id>/episodes/<episode-folder> \
  --language English \
  --transcript-language en \
  --model-path .cache/models/qwen3-asr-1.7b-8bit-pinned-v2 \
  --aligner-path .cache/models/qwen3-forced-aligner-0.6b-8bit-pinned-v2
```

Windows/CUDA 中文组使用官方模型和独立解释器：

```powershell
& .cache/venvs/qwen-cuda/Scripts/python.exe scripts/process_qwen3_asr_batch.py `
  --backend cuda `
  --episode shows/<show-id>/episodes/<episode-folder> `
  --model-path .cache/models/Qwen3-ASR-1.7B-hf-pinned-v3 `
  --aligner-path .cache/models/Qwen3-ForcedAligner-0.6B-hf-pinned-v3 `
  --chunk-context 5
```

同时提供两个本地模型路径时，批处理会设置 `HF_HUB_OFFLINE=1` 和
`TRANSFORMERS_OFFLINE=1`，因此 worker 不会联网补取模型。CUDA backend 记录的
engine/model/aligner 分别是 `qwen-asr-transformers`、`Qwen/Qwen3-ASR-1.7B-hf` 和
`Qwen/Qwen3-ForcedAligner-0.6B-hf`。backend options 记录
`backend: transformers-native` 与精确 Transformers 版本。默认参数为 `cuda:0`、`bfloat16`、SDPA、
120 秒名义归属 chunk、5 秒上下文和 batch size 1；每个内部边界向两侧各多解码
5 秒，再使用 ForcedAligner 的精确文字与时间对齐选择唯一交叉点。即使显式使用更宽 context，
`forced-alignment-time-crossover-v3` 也只在 seam 前后各 3 秒内枚举 crossover anchor；宽 context 的其余部分仅用于完整强制对齐和 coverage，
避免远离 seam 的重复口语制造假多解。精确锚点必须来自至少
3 个连续字符的匹配链；只有松散到超过 400 ms、比冲突长链至少再松 250 ms，且左右索引范围都被该长链完整包住的短候选，才可被至少两倍长且全部配对均在 400 ms 内的冲突链淘汰。
若一条完全位于 seam 单侧的可靠链与跨 seam 长链仅复用长链相邻边缘 1–2 字，worker 会保留单侧链并裁掉长链的重复前缀或后缀；
裁后长链仍须至少两倍长、seam 两侧各有至少 3 字且全部配对在 250 ms 内。其余达到门限的最大连续候选链
在两份对齐中必须形成不重叠、不交叉的唯一单调映射，
等长、时间更紧或无法比较的重复短语多解通常仍失败关闭。唯一例外是先按既有排序选出的最终 ownership cut 能证明所有可靠 exact pair
都完整落在 cut 同一侧：此时多解只存在于最终完全取自同一个 decode 的内部，不会造成正文双留或双删；产物必须记录
`ownership-cut-consistent-v1`、核对的 run 数和 pair 数。任何一对被 cut 分到不同 ownership 侧（包括只有一端恰好落在边界）仍立即失败，不得另找一个较宽松的 cut。
重复单字造成相邻 diagonal 分叉时，只允许
`adjacent-diagonal-repeated-token-indel-bubble-v1` 这一种窄修复：右侧必须恰好多一个相同单字，tight chain 与 shifted chain 的 offset 恰差 1，
冲突只能位于前链尾部与后链开头的 1–2 个 pair。替代 pair 的时间差不得优于 tight chain，平均劣势至少 250 ms；裁去 shifted chain 的冲突前缀后，
剩余 chain 必须至少两倍长、全部 pair 在 250 ms 内，并与其他 chain 形成严格唯一映射。最终按原排序选出的 anchor 仍必须来自 tight chain，
所有 pair 对 resulting cut 一致。产物必须逐项记录 diagonal offset、裁前/裁后范围、时间差统计、anchor pair 和 cut；不能用模糊字符串去重或一般编辑距离扩大该例外。

另一个独立、同样失败关闭的例外是
`zero-duration-right-indel-weak-bridge-v1`，仅用于实证中的右侧零时长单字插入：候选必须恰好形成 3 条 run；两条主链各至少 17 字、全部 pair 在 250 ms 内且严格有序，
左索引在 junction 处相邻，右索引只跳过 1 个清洗后恰为 1 字的 item。该 item 的时长最多 1 ms，而且其 start/end、两条主链左右两份对齐在 junction 的相邻 end/start
必须全部在 1 ms 内重合。第三条弱链必须恰为 3 字，左范围只能由前主链最后 1 字加后主链最初 2 字组成，右范围必须完整位于前主链内，且每个 pair 都松散到超过 400 ms；
弱链每个 left index 与每个 right index 还必须分别已被主链中的不同 tight pair 覆盖，
逐 pair 相比两侧主映射的最小时间劣势都至少 250 ms。删除弱链后必须只剩唯一单调映射，原排序选出的 anchor 必须来自主链；两条主链对 resulting cut 全部一致，而弱链在该 cut 下确实冲突。
产物不持久化可独立伪造的派生 delta 或 run 摘要，而是保存 seam 搜索窗及其两侧各一个邻项组成的 bounded `candidate_proof`；每个 item 记录 side、全局 item index、
清洗后单字、在 `decoded_text` 清洗字符序列中的 span、start 和 end。raw validator 先逐项绑定字符与 decode，再只从 proof 重建三条 run、所有 delta/优势、junction、anchor 和 cut；
aligned validator 还把 proof 中最终 owned 的每个 index/text/time 逐项绑定正式 alignment。非零时长、左侧或多 item indel、4 字弱链、部分覆盖、额外 run、proof 缺项或任何无法唯一分解的近邻形状一律不适用。

其后的统一例外 `single-axis-dominated-weak-runs-v1` 只在 repeated-token、上述 zero-duration repair 和原有 ownership-cut guard 都不能解决歧义时尝试，并复用同一 bounded `candidate_proof`，不信任持久化的 run 或 delta 摘要。dominance 与 edge repair 后必须有至少两条互不交叉、严格有序且全部 pair 在 250 ms 内的 tight backbone；每条待删除弱链至少 3 字且每个 pair 都松散到超过 400 ms，必须由同一条至少两倍长的 tight chain 在一侧逐 item 完整覆盖，每项时间优势至少 250 ms。弱链另一侧未被所有 tight chains 覆盖的 index 最多连续 2 项，并须严格夹在相邻 backbone 范围之间。所有在原始快照中合格的弱链必须原子删除，禁止级联或挑选子集；删除后映射必须唯一单调，正常最近 anchor 必须来自 tight backbone，且只有一个 ownership-consistent cut。raw validator 从 proof 重算完整 dominance/edge/atomic-drop/anchor/cut 流程；aligned validator继续逐项绑定最终 owned proof。任一 proof 篡改、覆盖缺口、边缘 gap、tie、残留冲突或更早 repair 可适用时均失败关闭。

标准 3 字 anchor、严格 2 字 anchor 和 aligned-gap 全部无解时，worker 还可识别
`exhausted-side-context-anchor`，但当前只允许左候选在 seam 前至少 15 秒、且至少占该 ownership core 的 15%（上限 27 秒）时明确耗尽；右候选还必须在默认 seam±3 秒窗口两侧各至少覆盖 3 字且有 item 跨 seam。
左侧末端附近 ±3 秒必须只有一条至少 3 字、全部 pair 在 250 ms 内的原始 exact chain；完整 shared context 只用来收集反证，所有可靠 pair 都必须与该 handoff cut 一致，
不得把全局 anchor 搜索半径扩大到 30 秒。接管最多丢弃左候选 1 个 item、1 个字、3 秒，最后保留的左 item 到首个右 item 的音频空隙不得超过 750 ms；
survivor 在 exhausted frontier 到 seam 的桥段中不得留下超过 3 秒的未核实 alignment 空洞；每个更长空洞都必须单独解码并通过严格静音探测，活跃语音立即拒绝。产物记录窗口、frontier、shortfall、跨缝证据、原始完整 context 的全部可靠 run/pair、桥段最大空洞与逐段声学结果、弃尾和 handoff；随后仍执行全局 active-audio coverage。

只有全局唯一的连续 2 字符匹配链，且两组对齐时间差均不超过
250 ms 并记录严格置信证据时，才允许短链回退。aligned-gap 回退还必须证明整个空隙在声学上接近静音。短尾块会
重新均分到最后两个归属区间，使边界语句只归属一个 chunk。对齐结果还会执行 active-audio coverage guard：worker 先汇总所有 chunk 的
owned alignment，再把这份全局并集分别裁剪到每个归属区间；覆盖区间和文字密度都使用全局相交 items，不能因 item 由相邻 chunk 拥有而制造假空洞。
如果全局并集在归属区间的首部、相邻 item 之间或尾部留下长空洞，worker 必须实际探测对应音频；只有安静区域可以继续，
持续活跃时失败关闭。首块、末块和句末标点都不构成默认豁免，不得将截断结果标记为完成。

唯一的活跃音频例外是显式 `--final-outro-exemption-seconds <seconds>`：默认值为 `0`、硬上限为 30 秒，且只适用于最后一个归属区间中
最后一个全局 aligned item 之后、不超过所给额度的 trailing gap。首部、内部和非末块空洞仍必须通过声学门禁。使用该选项前必须取得并保留
人工完整试听记录，或发布者章节、节目说明等能够证明该段只是告别后的片尾而非漏转写语音的证据；在单集处理记录或 PR 说明中写明证据和实际秒数。
该数值会同时进入 raw/aligned options，并由 aligned 的 raw SHA-256 lineage 绑定。已有
v2 raw 缺少该字段时，普通 resume 必须失败关闭；只有显式 `--realign` 才可在完整校验
其他 options、音频身份、v2 模型身份和 raw 内容后迁移并原子替换。markerless legacy
raw 不得使用这条迁移路径，必须显式 `--retranscribe` 建立真实的 v2 lineage。例如：

```powershell
& .cache/venvs/qwen-cuda/Scripts/python.exe scripts/process_qwen3_asr_batch.py `
  --backend cuda `
  --episode shows/<show-id>/episodes/<episode-folder> `
  --realign `
  --final-outro-exemption-seconds <verified-seconds> `
  --model-path .cache/models/Qwen3-ASR-1.7B-hf-pinned-v3 `
  --aligner-path .cache/models/Qwen3-ForcedAligner-0.6B-hf-pinned-v3
```

worker 会先完成并释放 ASR 模型，再加载 aligner；但 native 路径的 RTX A2000
golden-output、峰值显存和长音频验证仍待完成。通过这些实机门禁前不能提升新产物。
只有设备确实不支持 `bfloat16` 时才显式传入 `--dtype float16`。英文组在同一命令追加
`--language English` 和 `--transcript-language en`。

脚本内部逐集、逐子进程串行运行，不再并发启动额外加速器 worker；子进程退出同时
作为 Metal 统一内存或 CUDA 显存的回收边界。每集产物为：

```text
asr/qwen3-asr/raw.json
asr/qwen3-asr/aligned.json
asr/qwen3-asr/refined.json
asr/qwen3-asr/transcript.<language>.md
```

v2 `raw.json` 是恢复检查点：有效 v2 raw 缺 aligned 时只重跑对齐，身份匹配的
raw/aligned 会跳过。markerless legacy 只允许完整 raw/aligned 链被校验并只读跳过；
markerless raw 缺 aligned、CUDA pending raw 需要 reconciliation，或请求 `--realign`
时都必须失败关闭，并提示显式 `--retranscribe` 建立真实的 v2 转写与对齐身份，不能把
当前缓存身份回填到历史 raw。已经完整的单集不要为了“确认一下”重跑批处理；直接运行
validator，避免 renderer 产生无意义变更。

新生成的 raw/aligned/refined 使用 `lineage_schema_version: 2`：记录 Hub repository、
请求的完整 revision、每个下载 payload 的 metadata 所解析出的同一 resolved commit，
并重新计算 config、权重、tokenizer vocabulary/merges/processor 等全部 snapshot payload
的 SHA-256；三个阶段的身份必须精确相等，resume 遇到不一致会拒绝。没有 v2 marker 的
既有完整产物继续按 legacy hash 链只读，不要求批量改写；只有已有 v2 raw 才能做
align-only/`--realign`，且必须使用带逐文件 Hugging Face download metadata 的上述
pinned 本地 snapshot。markerless raw 需要任何新对齐时必须改用 `--retranscribe`。
当前保留的 73 条历史 selected 链（53 MLX、20 CUDA）均为 markerless legacy：产物没有记录
revision 或 local snapshot，当前机器也没有 CUDA 模型缓存，因此不能把现在可见的 MLX
cache 无证据回填到历史运行。它们只声明 audio/raw/aligned/refined/transcript 哈希链；
fresh/`--retranscribe` 会建立 v2 model identity，而 markerless `--realign` 被拒绝。
其中 20 条 CUDA 链继续按 `qwen-asr==0.0.6` 的历史 model/options 只读校验；任何
markerless partial/pending/realign，或需要新对齐的旧 qwen-asr v2 raw，都必须显式
`--retranscribe` 生成 Transformers-native 的新 model/aligner identity，禁止混合两代产物。

需要暂停时用正常的中断信号结束当前 worker，不删除已经完成的原子产物。每集日志在
`.cache/logs/qwen3-asr/<show-id>--<episode-folder>.log`。批处理失败后先读对应日志和
末尾 JSON 汇总，再用相同语言参数、单个显式 `--episode` 只重跑失败单集。

逐字稿清洗不得使用跨节目全局 replacement。某集确需确定性术语修正时，在该集
`asr/corrections.json` 登记 `schema_version`、`episode_id`、`version`、精确
`input_asr_sha256` 及带唯一 ID、
literal match/replacement、理由和正数 `expected_hits` 的规则。renderer 记录 map
SHA-256、版本、每条规则的预期/实际命中数，并在命中漂移时失败关闭；已有匹配 pair
默认 no-op，替换必须显式 `--rerender` 且限定具体单集。refined
与 Markdown 由可恢复 transaction journal 成对提交，中断后下一次调用先完成事务。

历史全局规则只迁移为确实改变文本的 14 份单集 map，不批量改写旧 refined。旧 refined
因而不会伪造新的 map provenance；CI 中的 `scripts/audit_correction_migration.py` 会把
map 绑定到精确 aligned SHA，重放 56 次预期命中，并证明旧 refined segments/blocks 与
run Markdown 字节完全一致。任何新渲染都会在 refined 中直接记录 map SHA、版本和命中。

MLX Whisper 只保留既有历史基线或显式实验。worker 拒绝 `NaN`/`Infinity` 等非严格
JSON，并强制所有新输出位于 `.cache/benchmarks/`；不得选择、提升或提交新基线。

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
- 5 分钟读完、主题导航、面向读者的阅读边界，以及不对读者展示的编辑记录；
- 每个关键结论回到正式逐字稿核对时间码；
- 区分嘉宾陈述、发布者材料、PodWiki 归纳和独立核查；
- 不从 ASR 错字推导高影响事实，不编造逐字稿中不存在的因果关系。

更新 `summary.source_transcript` 的真实 path、engine、model、selection status 和
SHA-256。完整机器稿可以支持 `workflow.summary: draft`；没有回听、术语校对和必要
事实核查时不得标记 `reviewed`。

## 10. 同步两个 Wiki 索引

单集达到 Web 收录状态后才同时加入两个单集索引；`outline`、`not-started`、
`source-acquired` 等处理中记录不得提前进入。已经进入索引的单集发生更新时，两个
索引必须同步刷新：

1. 新节目还要更新根 `README.md` 的三列“收录播客”表，节目名链接已核实的
   首选发布者页面，节目页链接本地 README；
2. 根 `README.md` 的六列表：标题、访谈人物、播客名称、日期、总结、逐字稿；
3. `shows/<show-id>/README.md` 的五列表：标题、播客名称、日期、总结链接、逐字稿链接。

标题链接规范发布者 URL，访谈人物只来自 `role: guest` 的已核实参与者；没有嘉宾
时写 `—`，不得用 participant 或 host 冒充。英文单集同时提供“英文逐字稿”和
“中文译稿”链接；译稿审核状态仍只保存在单集元数据。当前 validator 会严格检查根
节目表、根单集表和各节目表的集合、链接、嘉宾、日期及倒序；仍须人工复核标题可读性
与页面呈现，不能把校验通过当作编辑审核。

## 11. 统一完成门禁

从仓库根目录依次运行：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python -m unittest discover -s tests -v
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/validate.py
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/audit_correction_migration.py
npm --prefix apps/web audit --audit-level=high
npm --prefix apps/web run check
git diff --check
git status --short
```

涉及 Python、依赖或 CI 的改动还必须运行 [CONTRIBUTING](../CONTRIBUTING.md) 中的
lock、ruff、mypy、compile 与 supply-chain 完整门禁。

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
