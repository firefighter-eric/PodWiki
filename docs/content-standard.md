# PodWiki 内容标准

状态：`0.1-draft`

这是一份由首个真实单集驱动的草案。结构稳定前允许调整字段；一旦进入正式版本，再通过 `schema_version` 管理兼容性。

## 1. 内容层级

```text
shows/<show_id>/
├── README.md
└── episodes/<episode_folder>/
    ├── README.md
    ├── transcript.<language>.md
    └── asr/
        ├── raw.json
        └── refined.json

.cache/media/<show_id>/<episode_folder>/
├── source.<audio-extension>
└── source.metadata.json
```

| 文件 | 职责 | 是否人工维护 |
| --- | --- | --- |
| 节目 `README.md` | 节目元数据与介绍 | 是 |
| 单集 `README.md` | 单集元数据、总结与章节 | 是 |
| `transcript.<language>.md` | 正式逐字稿或机器初稿 | 是 |
| `asr/raw.json` | ASR 引擎原始输出，作为可追溯输入保留 | 否，不修改 |
| `asr/refined.json` | 确定性清洗、去重和合并后的结构化结果 | 脚本生成 |
| `.cache/**/source.*` | 用于转写的本地音频或视频 | 否 |
| `.cache/**/source.metadata.json` | 来源标识、媒体探测结果与 SHA-256 sidecar | 脚本生成 |

原始 ASR、refined ASR 和最终 Markdown 都提交到 Git：前两者用于复现与调试，Markdown 用于日常阅读和人工校对。`.cache/` 整体不提交 Git，只保存可重新下载或体积较大的媒体、来源 sidecar 与临时文件。

暂不同时维护 `show.yaml`、`episode.yaml` 或正式 JSONL，避免同一信息出现多个主数据源。将来需要搜索或 API 时，从 Markdown front matter 和逐字稿生成结构化索引。

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

```yaml
id: "zhangxiaojun:bili-bv1nb3u6teru"
episode_key: bili-bv1nb3u6teru
episode_number: null
slug: bili-bv1nb3u6teru-liao-heng
release_type: special
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

## 7. Bilibili 获取顺序

1. 检查平台人工字幕或自动字幕。
2. 有权处理且没有字幕时，再从公开媒体生成 ASR。
3. 说话人识别与专有名词校对。
4. 人工审核后写入正式逐字稿。
5. 画面硬字幕 OCR 仅作为最后手段。

首版不处理会员、付费、地区限制或其他访问控制，不批量抓取整个账号。

## 8. 机器转写

机器转写状态统一记录在单集 `README.md`，不能与人工校对稿混淆：

```yaml
workflow:
  transcript: machine
transcript:
  path: transcript.zh-CN.md
  acquisition_method: audio-asr
  asr_script: scripts/transcribe_audio.py
  engine: mlx-whisper
  model: mlx-community/whisper-large-v3-turbo-q4
  options:
    language: zh
    temperature: 0
    word_timestamps: false
  generated_at: "YYYY-MM-DDTHH:MM:SSZ"
  quality:
    source_segments: 0
    refined_segments: 0
    rendered_lines: 0
```

逐字稿不包含 YAML front matter。语言、来源、转写状态、模型、生成时间和质量统计等信息只保存在单集 `README.md`。

渲染规则：

- 删除空白段。
- 删除不含任何 Unicode 字母或数字（`L` / `N` 类别）的纯标点、符号或 emoji 段。
- 删除完全相同的连续重复段。
- 保留低置信文本，交给人工复核，不静默删除内容。
- 只自动修正常见且确定的专有名词拼写。
- 没有说话人识别时，不猜测说话人。
- 每个 refined segment 渲染为一行 `[HH:MM:SS] 文本`。

### ASR 产物层级

1. `raw.json`：ASR 引擎原始结果，不做内容修改；部分引擎可能输出 `NaN` 等非标准 JSON 常量，refine 脚本读取时统一转为 `null`。
2. `refined.json`：保留清洗后的 segment、可选合并 block，以及它们与原始 segment 的索引映射。
3. `transcript.<language>.md`：由 refined segment 逐行渲染，供人阅读、校对和版本管理。

`scripts/transcribe_audio.py` 使用 MLX Whisper 把本地音频写成格式化的原始 JSON。该步骤通过 uv 的 `asr` 依赖组运行，仅支持 Apple Silicon Mac。

`scripts/render_asr_transcript.py` 必须在同一次运行中生成 refined JSON 和 Markdown，避免两份结果使用不同的清洗逻辑。

### 多模型候选

同一单集对比多个 ASR 模型时，不覆盖当前正式产物。候选模型使用稳定的
`run_id` 保存在独立目录：

```text
asr/
├── raw.json
├── refined.json
└── qwen3-asr/
    ├── raw.json
    ├── aligned.json
    ├── refined.json
    └── transcript.zh-CN.md
```

单集根目录的 `transcript.<language>.md` 及 `transcript` front matter 始终表示
当前选中的正式版本。候选结果记录在 `asr_candidates`，例如：

```yaml
asr_candidates:
  - id: qwen3-asr-1.7b-8bit
    selection_status: candidate
    engine: mlx-audio
    model: mlx-community/Qwen3-ASR-1.7B-8bit
    aligner: mlx-community/Qwen3-ForcedAligner-0.6B-8bit
    artifacts:
      raw: asr/qwen3-asr/raw.json
      aligned: asr/qwen3-asr/aligned.json
      refined: asr/qwen3-asr/refined.json
      transcript: asr/qwen3-asr/transcript.zh-CN.md
```

`selection_status` 允许值为 `candidate`、`selected`、`rejected`。候选被选中后，
先更新正式 Markdown 和 `transcript` 元数据，再将状态改为 `selected`；其他
引擎结果继续保留以便追溯。
