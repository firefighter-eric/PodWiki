# PodWiki 内容标准

状态：`0.1-draft`

这是一份由首个真实单集驱动的草案。结构稳定前允许调整字段；一旦进入正式版本，再通过 `schema_version` 管理兼容性。

## 1. 内容层级

```text
shows/<show_id>/
├── README.md
└── episodes/<episode_folder>/
    ├── README.md
    ├── summary.<language>.md
    ├── transcript.<language>.md       # 当前选中的正式原文逐字稿
    ├── transcript.zh-CN.md            # selected 为英文时必需的逐段中文译稿
    └── asr/
        ├── qwen3-asr/
        │   ├── raw.json
        │   ├── aligned.json
        │   ├── refined.json
        │   └── transcript.<language>.md
        └── whisper/                 # 仅在已有基线时保留
            ├── raw.json
            ├── refined.json
            └── transcript.<language>.md

.cache/media/<show_id>/<episode_folder>/
├── source.<audio-extension>
└── source.metadata.json
```

| 文件 | 职责 | 是否人工维护 |
| --- | --- | --- |
| 节目 `README.md` | 节目元数据与介绍 | 是 |
| 单集 `README.md` | 单集元数据、来源概览、章节与处理状态 | 是 |
| `summary.<language>.md` | 基于完整内容的结构化总结 | 是 |
| `transcript.<language>.md` | 正式逐字稿或机器初稿 | 是 |
| `transcript.zh-CN.md`（英文原稿的派生译稿） | 与 selected 英文稿逐段对齐的中文译稿 | 是 |
| `asr/<run_id>/raw.json` | ASR 引擎原始输出和音频身份，作为可续跑检查点保留 | 否，不修改 |
| `asr/<run_id>/aligned.json` | 对齐器输出、句级时间戳和 raw/audio SHA-256 | 脚本生成 |
| `asr/<run_id>/refined.json` | 确定性清洗、去重和渲染来源的结构化结果 | 脚本生成 |
| `asr/<run_id>/transcript.<language>.md` | 某次 ASR run 的可读 Markdown | 脚本生成 |
| `.cache/**/source.*` | 用于转写的本地音频或视频 | 否 |
| `.cache/**/source.metadata.json` | 来源标识、媒体探测结果与 SHA-256 sidecar | 脚本生成 |

raw、aligned、refined ASR 和最终 Markdown 都提交到 Git：JSON 用于复现、续跑与调试，Markdown 用于日常阅读和人工校对。`.cache/` 整体不提交 Git，只保存可重新下载或体积较大的媒体、来源 sidecar、模型别名、日志与临时文件。

暂不同时维护 `show.yaml`、`episode.yaml` 或正式 JSONL，避免同一信息出现多个主数据源。将来需要搜索或 API 时，从 Markdown front matter 和逐字稿生成结构化索引。

### Wiki 索引表

根 `README.md` 先使用节目介绍表展示当前收录范围，顺序固定为：`播客`、
`简介`、`节目页`。播客名称链接到节目 front matter 中已核实的 Bilibili
频道或空间 URL，节目页链接到本地节目 README。新增节目或节目简介、来源
发生变化时必须同步更新该表。

根 `README.md` 的单集表格使用六列，顺序固定为：`标题`、`访谈人物`、
`播客名称`、`日期`、`总结`、`逐字稿`。节目 `README.md` 的单集表格
仍使用五列：`标题`、`播客名称`、`日期`、`总结链接`、`逐字稿链接`。

- 标题链接到首选发布者来源的规范 URL，并且不包含期号。
- 仅根索引增加访谈人物列；内容来自单集 front matter 中 `role: guest` 的
  参与者，多位嘉宾使用 `、` 分隔。嘉宾身份尚未核实时，不根据标题自行猜测。
- 根索引与对应节目索引必须在每次新增或更新单集后同时更新。
- 总结与逐字稿列直接链接到各自的本地 Markdown 文件。

## 2. 标识符与路径

### 节目 ID

- 只使用小写 ASCII 字母和数字。
- 不使用空格、下划线或连字符。
- 建立后保持稳定，不随节目改名或平台迁移而改变。

首批节目 ID：

```text
whynottv
zhangxiaojun
sv101
luoyonghao
latetalk
```

### 单集 ID

单集 ID 使用 `<show_id>:<episode_key>`，并在 front matter 中显式保存
`episode_key`：

```yaml
id: "whynottv:004"
show_id: whynottv
episode_key: "004"
```

单集目录使用 `<episode_key>-<short-slug>`，例如：

```text
004-weng-jiayi
```

目录名用于阅读，front matter 中的 `id` 才是稳定主键。

`episode_number` 只保存出版方明确给出的正式期号；没有正式期号时写为
`null`，不得用抓取顺序、输入顺序、平台合集位置或发布日期推导。无正式
期号的 Bilibili 单集使用稳定键 `bili-<lowercase-bvid>`，目录仍可追加人物
slug，例如：

```text
bili-bv1nb3u6teru-liao-heng
```

无正式期号的 YouTube 单集尚未定义稳定 key；在规范补充前停止建档并请求维护者
确认，不得直接小写或改写大小写敏感的 YouTube video ID。YouTube 的 tracked
`sources[].identifiers` 契约也尚未定义，因此当前仅支持 intake 与公开媒体获取，
不自动创建正式单集。

`episode_number` 与标题分开保存。单集 `title`、Markdown 一级标题和 Wiki
索引展示标题均不得拼接 `#<number>`、`<number>.` 等期号前缀或后缀。

侧栏和搜索结果使用单独维护的 `navigation_title`，
统一写成“访谈人物 · 精简题目”。人物必须来自 `participants` 中 `role: guest`
的记录，多位嘉宾按记录顺序用 `、` 连接；人物和题目之间使用两侧各有一个
空格的 ` · `。题目保留最有辨识度的主题，避免平台栏目名、访谈时长、期号和
内部 `episode_key`，完整标题不超过 40 个字符。发布者原标题继续原样保存在
`title`，不要为了导航展示而覆盖它。
这些导航和发现列表不得在标题前增加 `#<期号>`、`第 <期号> 期`、`特访`、
`特别` 等徽标；期号与发布类型只在单集详情、来源和元数据语境中展示。

单集详情页同样以 `navigation_title` 作为读者看到的标题契约：页面主标题显示
访谈人物，副标题显示精简题目，浏览器与分享元数据使用完整“人物 · 精简题目”。
发布者原标题继续保存在 `title`，只用于来源溯源、内容核验和原始标题检索，
不得替代详情页的规范标题。

首页最近更新目录另行维护 `catalog_keyword`，用于左侧红色索引词。
它必须是 1–20 个字符的单个编辑关键词，优先选择最有辨识度的品牌、模型或
独特主题，并保留官方大小写，例如 `SGLang`、`OpenAI`、`昇腾`。关键词不是
人物名或完整标题，不得写入期号、`特访`、`特别` 等发布类型。目录正文仍从
`navigation_title` 和 `participants` 渲染黑色人物名与灰色精简题目。

单个播客的节目页不展示 `catalog_keyword`。其单集列表采用三层结构：首行使用
红色嘉宾名和小字“播客名 · 发布日期”，第二行放大精简题目，第三行单独展示
从总结的“一句话总结”自动提取的两行简介。简介是已有总结的展示层摘要，不新增
或手工维护重复元数据。

```yaml
id: "zhangxiaojun:bili-bv1nb3u6teru"
episode_key: bili-bv1nb3u6teru
episode_number: null
slug: bili-bv1nb3u6teru-liao-heng
release_type: special
navigation_title: "廖恒 · 芯片产业周期与昇腾工程史"
catalog_keyword: "昇腾"
numbering:
  status: not-in-publisher-feed
  checked_at: 2026-08-05
```

`release_type` 允许值为 `regular`、`special`、`bonus`、`trailer`。
`numbering.status` 允许值为 `verified`、`not-in-publisher-feed`、`unknown`。
单集以后获得正式期号时，只补充 `episode_number` 和编号来源，不改变既有
`id`、`episode_key` 或目录。

## 3. URL 规范

所有内容来源只保存规范链接，不保存用户提供的原始追踪链接。

Bilibili 视频地址固定为：

```text
https://www.bilibili.com/video/<BVID>/
```

处理规则：

1. 保留 `https`、主机名、视频路径和 BVID。
2. 删除 `?` 后的全部查询参数。
3. 删除 `#` 后的片段标识。
4. 不保存 `spm_id_from`、`vd_source` 等追踪参数。
5. 不在其他字段保留含追踪参数的原始 URL。

例如：

```text
输入：https://www.bilibili.com/video/BV1darmBcE4A/?spm_id_from=...&vd_source=...
保存：https://www.bilibili.com/video/BV1darmBcE4A/
```

`sources[].identifiers` 同时记录 `bvid`、`aid`、`cid` 和 `page`，避免只依赖可能变化的网页路径。

## 4. 时间和日期

- `published_at` 使用带时区的 RFC 3339 时间。
- `duration_ms` 使用整数毫秒。
- 正文时间码统一显示为 `[HH:MM:SS]`。

示例：

```yaml
published_at: "2026-01-17T15:09:39+08:00"
duration_ms: 7365000
```

## 5. 单集处理状态

```yaml
workflow:
  metadata: verified
  summary: outline
  transcript: not-started
```

允许值：

- `metadata`: `draft`、`verified`
- `summary`: `empty`、`outline`、`draft`、`reviewed`
- `transcript`: `not-started`、`source-acquired`、`machine`、`edited`、`reviewed`、`blocked`

总结必须说明依据是完整逐字稿、平台简介还是平台章节，不能把基于简介的概览标成完整内容总结。

### 独立总结文件

发布者简介和章节整理的 `outline` 保留在单集 `README.md`，用于在完整逐字稿
尚未生成时提供来源概览。基于完整内容形成的 `draft` 或 `reviewed` 总结保存为
独立的 `summary.<language>.md`，并在单集 front matter 中记录稳定路径：

```yaml
workflow:
  summary: draft
summary_basis:
  - publisher-description
  - publisher-chapters
  - complete-machine-transcript
summary:
  path: summary.zh-CN.md
  language: zh-CN
  source_transcript:
    path: transcript.zh-CN.md
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    selection_status: selected
    sha256: "<source-transcript-sha256>"
```

总结文件采用以下阅读层级：

1. 一句话总结；
2. 为什么值得听；
3. 核心观点先使用一张按本期内容设计列名的 Markdown 逻辑速览表，再按
   “嘉宾主张、依据与经历、边界、原文定位”展开；
4. 面向快速阅读的整体总结；
5. 主题导航；
6. 事实边界与待核实事项。

逻辑速览表必须表达该期内容中的关系，不使用 `01`、`02` 等装饰性序号替代
语义维度，也不要求所有单集复用相同列。可以按内容使用“阶段 / 决策 / 结果”、
“问题 / 机制 / 边界”或其他更合适的列；表中结论必须能够在后续完整核心观点中
找到依据，不能为了视觉效果新增未经节目支持的判断。首列应使用简短的逻辑维度
标签，不在 Markdown 中手动插入换行；网页桌面端会按首列内容取宽并保持标签完整，
窄屏则转换为纵向卡片。

`draft` 可以依据完整机器逐字稿生成，但必须明确说明尚未核听。只有在总结所
引用的关键片段已经回听、专有名词已经校对，并且高影响事实已经完成必要的
交叉核查后，才能标记为 `reviewed`；这不等同于整份逐字稿已经逐字审核。

`summary.source_transcript` 必须记录总结实际使用的逐字稿，而不是事后改写为
当前默认模型。总结中的时间码默认必须来自当前正式逐字稿。若正式 ASR 引擎
切换而尚未迁移总结时间码，必须在总结和单集元数据中明确链接其归档来源逐字
稿，并把 `selection_status` 记为 `superseded`，不能声称仍指向当前正式稿。
涉及个人回忆、观点、预测和外部事实时，应明确区分嘉宾陈述、发布者材料、
PodWiki 归纳和独立核查结果。

## 6. 逐字稿格式

逐字稿采用紧凑的字幕行格式，每个 refined ASR segment 独占一行：

    # 单集标题

    [00:00:08] 欢迎来到本期节目。
    [00:00:11] 今天我们从他的成长经历聊起。

规则：

- 时间戳使用该 ASR segment 的原始开始时间，不人工估算拆句时间。
- 一级标题使用单集正式标题，不使用“逐字稿”作为标题。
- 每个 segment 一行，不再为时间点创建标题或 HTML 锚点。
- 每行末尾保留两个空格作为 Markdown 硬换行，不使用 fenced code block。
- 完成说话人识别后，可写为 `[00:00:08] 主持人：欢迎来到本期节目。`。
- 不确定的姓名使用 `说话人 1`、`说话人 2`，确认后再替换。
- 听不清写为 `[听不清 00:23:14]`，不根据上下文猜测。
- 事实不确定写为 `[待核实]`。
- 逐字稿记录获取方式；校对状态和生成信息统一保存在单集 `README.md`，不在逐字稿中重复。

### 英文正式逐字稿的中文逐行译稿

当单集 `language: en`，或当前 selected `transcript.path` 以 `.en.md` 结尾时，
根目录必须同时提供 `transcript.zh-CN.md`。英文稿仍是正式原稿：
`transcript.path` 必须继续指向 `transcript.en.md`，索引仍链接英文 selected 稿，
中文译稿只登记在 `transcript.translations`：

```yaml
language: en
transcript:
  path: transcript.en.md
  translations:
    - language: zh-CN
      path: transcript.zh-CN.md
      source_language: en
      source_path: transcript.en.md
      alignment: segment
      status: machine
      generated_at: "YYYY-MM-DDTHH:MM:SSZ"
      source_sha256: "<transcript.en.md SHA-256>"
      sha256: "<transcript.zh-CN.md SHA-256>"
```

`status` 允许值为 `machine`、`edited`、`reviewed`；它只描述译稿自身的审核
程度。`generated_at` 使用带时区的 RFC 3339 时间。两个 SHA-256 分别绑定当前
selected 英文稿和中文译稿，英文原稿发生变化后必须重新生成或重新核验译稿并
更新哈希。

译稿沿用逐字稿格式，并遵守严格的一对一 segment 契约：

- 两份 Markdown 的一级标题完全相同，标题后都保留一个空行。
- 正文行数完全相同；英文原稿的每一行只对应中文译稿的一行。
- 每对正文行的 `[HH:MM:SS]` 必须逐行完全一致，顺序也不得变化。
- 只翻译该 segment 的文本，不合并、拆分、遗漏或新增 segment，也不重新估算
  时间戳；每行继续保留 Markdown 硬换行。

中文译稿不是 ASR 引擎产物，不进入 `asr/`、`asr_artifacts` 或 `asr_runs`，
也不得替代 selected 英文稿。中文总结与这份逐行译稿是不同内容层：总结负责
提炼，译稿负责忠实保持原稿的逐段结构。

## 7. Bilibili 获取顺序

1. 检查平台人工字幕或自动字幕。
2. 当前仓库尚未提供公开字幕的下载、转换和 lineage 导入工具；发现公开字幕时
   停止自动流程并报告该分支尚未实现，不得直接忽略字幕改跑音频 ASR。
3. 有权处理且没有公开字幕时，再从公开媒体生成 ASR。
4. 校验并渲染根目录机器初稿，状态标记为 `machine`。
5. 说话人识别与专有名词校对。
6. 人工审核后把状态改为 `reviewed`。
7. 画面硬字幕 OCR 仅作为最后手段。

首版不处理会员、付费、地区限制或其他访问控制，不批量抓取整个账号。

## 8. 机器转写

机器转写状态统一记录在单集 `README.md`，不能与人工校对稿混淆：

```yaml
workflow:
  transcript: machine
transcript:
  path: transcript.zh-CN.md
  acquisition_method: audio-asr
  asr_script: scripts/transcribe_qwen3_asr.py
  engine: mlx-audio
  model: mlx-community/Qwen3-ASR-1.7B-8bit
  aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
  options:
    language: Chinese
    temperature: 0
    max_tokens_per_chunk: 4096
    chunk_duration_seconds: 240
    max_sentence_characters: 160
  generated_at: "YYYY-MM-DDTHH:MM:SSZ"
  quality:
    source_chunks: 0
    aligned_chunks: 0
    alignment_items: 0
    sentence_segments: 0
    refined_segments: 0
    rendered_blocks: 0
    rendered_lines: 0
  performance:
    transcription_seconds: 0
    alignment_seconds: 0
```

逐字稿不包含 YAML front matter。语言、来源、转写状态、模型、生成时间和质量统计等信息只保存在单集 `README.md`。

本地音频验证完成后，在单集 README 记录可重建但不提交 Git 的 cache 身份：

```yaml
local_audio_cache:
  path: .cache/media/<show-id>/<episode-folder>/source.m4a
  metadata_path: .cache/media/<show-id>/<episode-folder>/source.metadata.json
  git_ignored: true
  acquired_at: "YYYY-MM-DDTHH:MM:SSZ"
  verified_at: "YYYY-MM-DDTHH:MM:SSZ"
  codec: aac
  sample_rate_hz: 44100
  channels: 2
  size_bytes: 0
  duration_ms: 0
  sha256: "<source-audio-sha256>"
```

未获取音频时模板中的 `local_audio_cache` 保持 `null`。所有值来自最终
`source.metadata.json` 的真实媒体探测结果，路径仍使用仓库相对 POSIX 形式；
不得把 intake sidecar 或另一集的值复制进来。

渲染规则：

- 删除空白段。
- 删除不含任何 Unicode 字母或数字（`L` / `N` 类别）的纯标点、符号或 emoji 段。
- 删除完全相同的连续重复段。
- 保留低置信文本，交给人工复核，不静默删除内容。
- 只自动修正常见且确定的专有名词拼写。
- 没有说话人识别时，不猜测说话人。
- 每个 refined segment 渲染为一行 `[HH:MM:SS] 文本`。

### ASR 产物层级

1. `raw.json`：ASR 引擎原始结果和音频 size/SHA-256，不做内容修改，也是续跑检查点。
2. `aligned.json`：ForcedAligner 输出、逐句时间戳、音频 SHA-256 和 raw JSON SHA-256。
3. `refined.json`：保留清洗后的 segment、可选合并 block、输入 ASR SHA-256，以及它们与源 segment 的索引映射。
4. `transcript.<language>.md`：由 refined segment 逐行渲染；其 SHA-256 写回 refined JSON，供人阅读、校对和版本管理。

三层 JSON 的 lineage 字段固定为以下结构。

`raw.json`：

```json
{
  "audio": {
    "size_bytes": 0,
    "sha256": "<source-audio-sha256>"
  }
}
```

`aligned.json`：

```json
{
  "source": {
    "raw_asr_path": "shows/<show>/episodes/<episode>/asr/qwen3-asr/raw.json",
    "audio_sha256": "<source-audio-sha256>",
    "raw_asr_sha256": "<raw-json-sha256>"
  }
}
```

`refined.json`：

```json
{
  "source": {
    "input_asr_path": "shows/<show>/episodes/<episode>/asr/qwen3-asr/aligned.json",
    "input_asr_sha256": "<aligned-json-sha256>"
  },
  "rendered_transcript": {
    "path": "shows/<show>/episodes/<episode>/asr/qwen3-asr/transcript.zh-CN.md",
    "sha256": "<run-markdown-sha256>"
  }
}
```

所有记录到 Git 的路径必须是仓库相对 POSIX 路径，不能写入开发者机器的绝对
路径。SHA-256 使用 64 位小写十六进制；JSON 必须是严格 JSON，不能包含重复
key、`NaN` 或 `Infinity`。

`scripts/transcribe_qwen3_asr.py` 使用 Qwen3-ASR 生成 raw JSON，再用 Qwen3-ForcedAligner 生成 aligned JSON。有效 raw 存在而 aligned 缺失时只重跑对齐；两者完整且身份、参数和 SHA-256 均匹配时直接跳过。长音频必须逐集、逐子进程串行运行，以子进程退出作为 Metal/unified memory 的回收边界。

`scripts/render_asr_transcript.py` 必须在同一次运行中生成 refined JSON 和 Markdown，使用临时文件和哈希关联两份产物，避免结果使用不同的清洗逻辑。

### 多模型运行记录

同一单集的每个 ASR 模型使用稳定 `run_id` 保存在独立目录；选中模型的
Markdown 同时复制到单集根目录，已有基线不删除：

```text
asr/
├── qwen3-asr/
│   ├── raw.json
│   ├── aligned.json
│   ├── refined.json
│   └── transcript.zh-CN.md
└── whisper/
    ├── raw.json
    ├── refined.json
    └── transcript.zh-CN.md
```

单集根目录的 `transcript.<language>.md` 及 `transcript` front matter 始终表示
当前选中的正式版本。各次运行记录在 `asr_runs`，例如：

```yaml
asr_runs:
  - id: qwen3-asr-1.7b-8bit
    selection_status: selected
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
```

`selection_status` 允许值为 `candidate`、`selected`、`superseded`、`rejected`。
只有 raw、aligned、refined、run Markdown 及其哈希全部通过校验后，才能把 run
Markdown 复制为根目录正式逐字稿并标记 `selected`。先前正式引擎改为
`superseded` 并继续保留，以便追溯和比较。
