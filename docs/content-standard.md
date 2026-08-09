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
`简介`、`节目页`。播客名称链接到节目 front matter 中已核实的首选发布者
页面，节目页链接到本地节目 README。新增节目或节目简介、来源
发生变化时必须同步更新该表。

根 `README.md` 的单集表格使用六列，顺序固定为：`标题`、`访谈人物`、
`播客名称`、`日期`、`总结`、`逐字稿`。节目 `README.md` 的单集表格
仍使用五列：`标题`、`播客名称`、`日期`、`总结链接`、`逐字稿链接`。

- 标题单元格的可见文本必须精确等于单集 `title`，并链接到首选发布者来源的
  规范 URL；文本中的 ASCII `|` 在 Markdown 表格里写为 `\|`。`title` 不包含期号。
  发布者原标题若以已核实
  正式期号开头，只从 `title` 删除该期号与紧随空白，并把未改写原标题保存在
  `sources[].title`；其他原标题继续原样使用。
- 仅根索引增加访谈人物列；内容来自单集 front matter 中 `role: guest` 的
  参与者，多位嘉宾使用 `、` 分隔。没有已核实嘉宾时显示 `—`；嘉宾身份尚未
  核实时，不根据标题自行猜测，也不把一般参与者或主播提升为嘉宾。
- 根索引与对应节目索引必须在每次新增或更新单集后同时更新。
- 总结与逐字稿列直接链接到各自的本地 Markdown 文件。
- 根索引的“播客名称”必须使用节目 `title` 并链接对应本地节目 README；
  节目索引的“播客名称”必须是同一个节目 `title`。
- 两级单集索引均以日期倒序排列，单集集合必须与当前 Web 收录集合完全一致，
  不得缺失、多出或重复同一 summary 链接。

### 参与者与嘉宾背景

`participants` 保存参与者在本集中的稳定身份、姓名、别名和角色。嘉宾使用
`role: guest`；需要展示学历、公司、职位或简历时，在对应参与者下增加可选的
`profile`，不要把这些背景拼进 `name`、`role` 或 `navigation_title`。没有足够
依据时省略 `profile`，不得用空占位或推测内容补齐。

```yaml
participants:
  - id: guest-id
    name: 嘉宾姓名
    aliases: []
    role: guest
    profile:
      headline: "一句话背景"
      bio: "可选的简短人物介绍。"
      affiliations:
        - organization: 机构名称
          title: 职位
          status: current
      education:
        - institution: 学校名称
          credential: 学位
          field: 专业或研究方向
      checked_at: YYYY-MM-DD
```

`profile` 存在时，`headline` 和 `checked_at` 必填。`headline` 是面向读者的一行
背景摘要，只能概括同一份 profile 中已有依据的事实；`bio` 是可选短介绍。
`affiliations` 和 `education` 是可选列表，也可以为空：

- `affiliations[].organization` 必填，`title` 可选，`status` 只能是 `current`
  或 `former`；`current` 只表示截至 `profile.checked_at` 仍为当前关系，不表示
  读者访问页面时仍然有效。
- `education[].institution` 必填，`credential` 和 `field` 可选；不确定学位或
  专业时省略对应字段，不能用相近概念代填。
- `checked_at` 使用 `YYYY-MM-DD`，表示整份 profile 最近一次完成来源核对的日期。
  背景变化后应更新字段和日期，不能只刷新日期而不重新核实内容。该日期仅用于
  仓库维护和内容校验，不作为“资料截至”之类的维护提示展示给读者。

profile 中每项事实必须来自本集 `sources` 已登记的来源，或来自嘉宾明确自述。
使用额外的发布者人物介绍、机构主页等材料时，先把其规范 URL 登记到 `sources`；
使用嘉宾自述时，必须回听音频或使用已经人工核对的逐字稿确认原意。发布者标题和
机器 ASR 只能作为检索线索，不能单独证明学历、任职、公司关系或 `current` 状态，
也不得根据行业常识、姓名或上下文猜测。

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
yiqitietalk
```

### 单集 ID

单集 ID 使用 `<show_id>:<episode_key>`，并在 front matter 中显式保存
`episode_key`：

```yaml
id: "whynottv:004"
show_id: whynottv
episode_key: "004"
```

`episode_key` 只使用小写 ASCII 字母、数字和分隔单词的单个连字符，不能使用
空格、下划线、连续连字符或首尾连字符。纯数字 key 必须作为带引号的 YAML
字符串保存，避免 `004` 被解析成数值后丢失前导零。

单集目录使用 `<episode_key>-<short-slug>`，例如：

```text
004-weng-jiayi
```

目录名用于阅读，front matter 中的 `id` 才是稳定主键。
每个单集 `id` 在整个仓库中必须唯一，并且必须精确等于
`<show_id>:<episode_key>`；不得让两个目录复用同一主键。

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

无正式期号的小宇宙单集使用稳定键 `xiaoyuzhou-<eid>`；`eid` 是规范单集 URL
中的 24 位小写十六进制标识。例如：

```text
xiaoyuzhou-6a58ef45016dcc7e05434f8e-wang-wei-wuwa
```

小宇宙页面标题中的 `EP98`、`S6E1` 或 `vol:152` 不能单独作为正式期号证据；
只有发布者明确确认其编号语义后才能写入 `episode_number`。否则保持 `null`，
并使用上述来源键。

`episode_number` 与标题分开保存。单集 `title`、Markdown 一级标题和 Wiki
索引展示标题均不得拼接 `#<number>`、`<number>.` 等期号前缀或后缀。

侧栏和搜索结果使用单独维护的 `navigation_title`，统一写成
“人物 · 精简题目”。人物只可来自已核实的 `participants`，并按以下顺序选择：
存在 `role: guest` 时使用全部嘉宾；否则使用明确的 `role: participant`；仍没有时
使用本期实际出场的 `role: host`。同级多位人物按记录顺序用 `、` 连接。不得从标题
猜测人物，也不得为了导航把 `participant` 或 `host` 改成 `guest`。人物和题目之间
使用两侧各有一个空格的 ` · `。题目保留最有辨识度的主题，避免平台栏目名、访谈
时长、期号和内部 `episode_key`，完整标题不超过 40 个字符。发布者未改写原标题
保存在 `sources[].title`；规范展示标题保存在 `title`，不要为了导航展示而覆盖它。
这些导航和发现列表不得在标题前增加 `#<期号>`、`第 <期号> 期`、`特访`、
`特别` 等徽标；期号与发布类型只在单集详情、来源和元数据语境中展示。

单集详情页同样以 `navigation_title` 作为读者看到的标题契约：页面主标题显示
上述证据化人物，副标题显示精简题目，浏览器与分享元数据使用完整
“人物 · 精简题目”。发布者原标题继续保存在 `sources[].title`，只用于来源溯源、
内容核验和原始标题检索，不得替代详情页的规范标题。

首页最近更新目录另行维护 `catalog_keyword`，用于左侧红色索引词。
它必须是 1–20 个字符的单个编辑关键词，优先选择最有辨识度的品牌、模型或
独特主题，并保留官方大小写，例如 `SGLang`、`OpenAI`、`昇腾`。关键词不是
人物名或完整标题，不得写入期号、`特访`、`特别` 等发布类型。目录正文仍从
`navigation_title` 和 `participants` 渲染黑色人物名与灰色精简题目。

单个播客的节目页不展示 `catalog_keyword`。其单集列表采用三层结构：首行使用
红色导航人物和小字“播客名 · 发布日期”，第二行放大精简题目，第三行单独展示
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
每集必须至少登记一个 `sources` 条目，并且恰好一个条目使用 YAML 布尔值
`preferred: true` 作为 Web 首选来源；其余条目可以写 `preferred: false` 或省略。

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

小宇宙栏目和单集地址分别固定为：

```text
https://www.xiaoyuzhoufm.com/podcast/<podcast-id>
https://www.xiaoyuzhoufm.com/episode/<episode-id>
```

`podcast-id` 和 `episode-id` 均为 24 位小写十六进制标识。保存时删除查询参数、
片段和末尾斜杠。栏目 README 使用 podcast URL；单集来源使用 episode URL。
单集 `sources[].identifiers` 固定记录以下三个字段：

```yaml
identifiers:
  eid: 6a58ef45016dcc7e05434f8e
  pid: 6588196412e01d7ba13aad47
  media_id: 6588196412e01d7ba13aad47/example-token.m4a
```

小宇宙单集来源固定使用 `platform: xiaoyuzhou` 与 `kind: episode`；
即使最初是通过 RSS 发现，也不得把已绑定规范小宇宙单集 URL 的条目声明为
`platform: rss`。RSS feed URL 和 GUID 可作为补充 identifiers 保留。

`media_id` 必须同时等于公开页面的 `mediaKey` 与 `media.id`，其首段必须等于
该单集自己的 `pid`，且公开 CDN URL path 必须精确为 `/<media_id>`。不能用外层
栏目列表的 PID 覆盖联播或串台单集自身已核实的 `episode.pid`。

## 4. 时间和日期

- `published_at` 使用带时区的 RFC 3339 时间，并作为带引号的 YAML 字符串保存。
- `duration_ms` 使用正整数毫秒。对于 `acquisition_method: audio-asr` 的正式逐字稿，
  它必须精确等于该 selected ASR 输入在 `local_audio_cache.duration_ms` 中记录的
  实际媒体探测值，而不是发布者页面或 RSS 中经过整秒取整的展示时长。发布者时长
  可以保留在来源说明中，但不得覆盖正式逐字稿所绑定的音频时长。非音频 ASR 来源
  可以不登记 `local_audio_cache`，但必须在 selected run 中明确登记其来源
  provenance，不能借用另一份媒体时长。
- 正文时间码统一显示为 `[HH:MM:SS]`：小时固定为两位 `00`–`99`，分钟和秒
  必须为 `00`–`59`。当前内容超过 99 小时时，应先更新格式契约与两端校验器，
  不能直接写入三位小时。

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

Web 只收录同时满足以下三项的单集：`metadata: verified`、`summary` 为
`draft` 或 `reviewed`、`transcript` 为 `machine`、`edited` 或 `reviewed`。
其他合法状态表示处理中的仓库记录，可以暂时没有总结或逐字稿资产，但不会进入
节目页、侧栏、搜索或详情路由。达到 Web 收录状态后，`summary.path` 和
`transcript.path` 指向的文件必须存在，否则构建与仓库校验失败，不能静默降级。
处理中英文单集也可以先登记计划中的 `transcript.en.md` 并保留空的
`transcript.translations`；一旦声明具体译稿条目，该条目的路径、哈希和对齐契约
仍会立即校验。

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

通用的 `summary.path` 和 `transcript.path` 必须是单集目录内的相对 POSIX 路径；
路径解析后的真实文件也必须留在该目录内，不能借助符号链接指向目录外文件。

总结文件采用以下严格顺序。前六项属于读者内容；第七项是仓库内的编辑记录，
不进入 Web 正文、全文搜索、SEO 描述或分享元数据：

1. 一句话总结；
2. 为什么值得听；
3. 核心观点先使用一张按本期内容设计列名的 Markdown 逻辑速览表，再按
   “嘉宾主张、依据与经历、边界、原文定位”展开；
4. `5 分钟读完`（既有内容可以使用 `整体总结` 标题）；
5. 主题导航；
6. 阅读边界；
7. 编辑记录（不对读者展示）。

逻辑速览表必须表达该期内容中的关系，不使用 `01`、`02` 等装饰性序号替代
语义维度，也不要求所有单集复用相同列。可以按内容使用“阶段 / 决策 / 结果”、
“问题 / 机制 / 边界”或其他更合适的列；表中结论必须能够在后续完整核心观点中
找到依据，不能为了视觉效果新增未经节目支持的判断。首列应使用简短的逻辑维度
标签，不在 Markdown 中手动插入换行；网页桌面端会按首列内容取宽并保持标签完整，
窄屏则转换为纵向卡片。

`draft` 可以依据完整机器逐字稿生成，但必须在 front matter、单集 README 或总结
开头的仓库编辑说明中明确记录尚未核听。该状态不得在 Web 读者界面重复展示。只有在总结所
引用的关键片段已经回听、专有名词已经校对，并且高影响事实已经完成必要的
交叉核查后，才能标记为 `reviewed`；这不等同于整份逐字稿已经逐字审核。

Web 的读者投影固定从 `## 一句话总结` 开始，到 `## 编辑记录（不对读者展示）`
之前结束；七个二级标题必须按上述顺序各出现一次，旧版混合边界标题不再接受。
全文搜索必须索引同一投影，不能回显 `draft`、`machine`、模型名、内部路径、
SHA-256、lineage 或审核待办。`阅读边界` 与核心观点中的“边界”继续面向读者保留，
但应写成证据范围、利益关系、发言归属、时效性或风险限制，不写“待回听”
“待校对”“人工审核时”等维护动作。
逐字稿与译稿的真实状态继续保存在 front matter 和校验链中，页面只使用“完整逐字稿”
或“中英对照逐字稿”等读者文案，不把工作流枚举当作徽章展示。

`summary.source_transcript` 必须记录总结实际使用的逐字稿，而不是事后改写为
当前默认模型。总结中的时间码默认必须来自当前正式逐字稿。若正式 ASR 引擎
切换而尚未迁移总结时间码，必须在总结和单集元数据中明确链接其归档来源逐字
稿，并把 `selection_status` 记为 `superseded`，不能声称仍指向当前正式稿。
涉及个人回忆、观点、预测和外部事实时，应明确区分嘉宾陈述、发布者材料、
PodWiki 归纳和独立核查结果。

达到 Web 收录状态时，`summary.source_transcript.path`、`engine`、`model`、
`selection_status` 和 `sha256` 全部必填；路径必须留在单集目录内、文件必须存在且
SHA-256 必须匹配。总结中每一个 `[HH:MM:SS]` 引用都必须在该来源逐字稿的时间戳
集合中精确存在。`selected` 来源必须等于当前 `transcript.path`；`superseded`
来源必须精确对应一条保留的 superseded ASR run 及其 transcript artifact。

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

## 7. 公开来源获取顺序

1. 检查平台人工字幕或自动字幕。
2. 当前仓库尚未提供公开字幕的下载、转换和 lineage 导入工具；发现公开字幕时
   停止自动流程并报告该分支尚未实现，不得直接忽略字幕改跑音频 ASR。
3. 有权处理且没有公开字幕时，再从公开媒体生成 ASR。
4. 校验并渲染根目录机器初稿，状态标记为 `machine`。
5. 说话人识别与专有名词校对。
6. 人工审核后把状态改为 `reviewed`。
7. 画面硬字幕 OCR 仅作为最后手段。

首版不处理会员、付费、私密、地区限制或其他访问控制。默认不批量抓取整个账号、
频道、播放列表或播客栏目；只有用户明确授权一个已核实的单一栏目时，才允许对该
栏目执行有界批量导入。开始下载前必须冻结包含栏目 PID、每集规范 URL 与 `eid` 的
manifest，之后逐集、限速处理，不在运行中自动扩展范围。每一集仍须独立通过
`NORMAL`、`FREE`、非私密、`PUBLIC`、栏目身份、enclosure/媒体 URL、公开 M4A
字节数与时长校验；任何不符合条件的单集必须拒绝并单独报告。该例外不允许跨栏目、
使用登录态，或枚举和获取付费/私密内容。

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

正常获取记录 `acquired_at`。若旧音频存在且 sidecar 缺失，只能通过显式的安全恢复
流程，在调用者提供的预期 SHA-256、公开来源身份、实际文件哈希和 ffprobe 结果全部
一致后补建 sidecar；这类记录使用 `recovered_at` 代替未知的 `acquired_at`，并同时
记录本次 `verified_at`，不得伪造历史采集时间。

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

Apple Silicon 的 `scripts/transcribe_qwen3_asr.py` 与 Windows/NVIDIA CUDA 的
`scripts/transcribe_qwen3_asr_cuda.py` 都先使用 Qwen3-ASR 生成 raw JSON，再用
Qwen3-ForcedAligner 生成 aligned JSON。有效 raw 存在而 aligned 缺失时只重跑
对齐；两者完整且身份、参数和 SHA-256 均匹配时直接跳过。长音频必须逐集、
逐子进程串行运行，以子进程退出作为 Metal unified memory 或 CUDA VRAM 的回收边界。

Windows/NVIDIA CUDA 的分块契约是 120 秒名义归属区间，每个内部边界向两侧各带
5 秒解码上下文。ForcedAligner 必须以精确文字和时间对齐选出唯一交叉点，且精确锚点必须
通常属于至少 3 个连续字符的匹配链；只有唯一的连续 2 字符匹配链，且两组对齐时间差均不超过
250 ms 并记录严格置信证据时，才可作为短链回退。aligned-gap 回退只有在整个空隙通过声学静音门禁时才可用。
短尾块必须重新分摊到最后两个归属区间。重叠文字只归属一次，不得直接拼接相邻解码窗口。在 boundary reconciliation 完成前，raw 只是
`pending` 检查点，不能成为下游输入；只有边界全部可重现地完成，且 active-audio
coverage guard 确认每个归属区间未在活跃语音中过早截断后，才可写入 `complete` raw
和 aligned 产物。`chunk_duration_seconds`、`chunk_context_seconds`、boundary reconciliation
方法、alignment coverage guard 和 aligned-gap guard 方法都是可重现参数；任一项不匹配都不得复用旧产物。

新 CUDA v2 产物使用官方 Transformers-native `*-hf` 模型，并在 options 中记录
`backend: transformers-native` 与精确 Transformers 版本。历史 markerless CUDA 完整链
保留 `qwen-asr==0.0.6` 的原始 model/options，只允许只读校验与跳过；markerless partial、
pending、realign，以及需要新对齐的旧 qwen-asr v2 raw 都必须 `--retranscribe`，不得把旧
raw 与 native aligner 混合或给历史产物回填当前身份。

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

达到 Web 收录状态的 `machine`、`edited` 或 `reviewed` 逐字稿必须在 `asr_runs`
中恰好绑定一条 `selected` run；缺少 `asr_runs`、零条或多条 selected 都是门禁
错误。Qwen run 必须通过 raw、aligned、refined、run Markdown 与根正式稿的完整
hash lineage；其他引擎或来源也必须在 selected run 中记录 engine、model 和完整
tracked artifacts，不能仅凭根 Markdown 声称来源明确。

根 README 的节目表、根单集索引和每个节目 README 的单集表都属于内容契约。
校验器必须比对其列顺序、metadata 集合、preferred 来源链接、日期、总结/正式逐字稿
链接和日期倒序；新增或改动内容时不允许任何一个索引滞后。
