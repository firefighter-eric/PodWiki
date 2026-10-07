# PodWiki AI 维护指南

本文件适用于整个仓库；子目录存在更具体的 `AGENTS.md` 时，同时遵守其规则。

## 扫描剧集更新

扫描节目、频道或 feed 是否有新剧集时，依次完整阅读：

1. [内容标准](./docs/content-standard.md)：播客与完整单集的收录边界；
2. 对应节目 `shows/<show-id>/README.md`：已核实来源与节目级例外；
3. [PodWiki 扫描剧集 skill](./.agents/skills/podwiki-scan-episodes/SKILL.md)：扫描范围、
   完整性、去重、结果状态和候选清单契约。

扫描只生成被 Git 忽略的证据和候选清单，不下载媒体、不创建单集目录、不运行 ASR、
不更新索引。必需来源无法完整覆盖时只能报告 `partial` 或 `blocked`，不得报告
“没有更新”。

## 新增或处理单集

开始修改前，依次完整阅读：

1. [单集处理流程](./docs/episode-processing.md)：端到端步骤、输入输出和停止点；
2. [内容标准](./docs/content-standard.md)：目录、元数据、状态、逐字稿、译稿与索引契约；
3. [PodWiki 添加剧集 skill](./.agents/skills/podwiki-add-episodes/SKILL.md)：精确输入、
   来源限制、ASR 恢复语义和完成检查。

按流程选择相关模板和脚本，不要从已有单集反向猜测未核实的元数据。

## 本地大模型与共享资源

- 翻译、总结、全文阅读笔记等文本大模型任务，优先使用 LM Studio 中已安装且适合任务的模型，通过其本地 API 调用；先核对模型标识、量化格式、上下文容量和服务可用性，避免在项目中重复下载权重。
- 首次用于正式批量处理前，用少量代表性片段核对漏译、术语、逐段对应和耗时；不凭版本号或推理引擎名称宣称质量更好、速度更快。执行记录中保存实际模型、提示词、参数和输入来源，保留原有 machine／draft 审核状态。
- LM Studio 不支持或不适合的专用模型，先检查用户 Models 目录中的可用副本，再按需下载到共享位置。此机器的共享位置为 `/Users/eric/Models`，PodWiki 模型存放在 `/Users/eric/Models/PodWiki`，项目 `.cache/models` 通过软链接引用；可提交代码中的路径应支持配置，不写死个人绝对路径。
- 新 checkout 下载模型前先运行 `uv run --no-sync python scripts/setup_shared_models.py`，
  创建用户级共享目录的链接；可用 `--shared-root` 覆盖位置。迁移前确认没有活动模型任务，
  两处都存在模型时先核对冲突，禁止覆盖。
- ASR 和时间戳对齐继续使用对应的专用模型；文本大模型不替代转写或对齐，不因 LM Studio 不可用而静默改用远端服务。
- uv 默认使用用户级共享依赖缓存，可用 `uv cache dir` 核对。不要重新设置项目本地 `.cache/uv`，除非操作者为明确的隔离需求显式覆盖。

## 不可省略的规则

- PodWiki 只收录播客。账号或频道身份、视频时长、访谈外观、标题中的 `EP` 都不能
  单独证明内容是播客；新节目必须有发布者的播客声明、公开播客 feed/平台页，或
  明确标为播客正片的官方合集。只导入完整单集；片段、预告、Shorts、普通视频、
  课程、演讲、发布会、直播及回放默认排除，除非发布者也把同一完整内容作为
  该播客的正式单集发布。
- 只保存去除追踪参数的规范来源 URL；正式期号必须来自发布者，不按输入顺序推断。
- 可以在用户明确授权的平台、登录身份与来源范围内，使用现有浏览器会话或 cookies
  下载用户有权访问、且原本符合本仓库收录边界的公开免费完整单集。登录态只作为
  访问与传输上下文，不扩大节目、批次或内容授权；不得绕过会员、付费、私密、地区
  或其他访问控制。cookie、token、浏览器配置和其他凭据只允许临时存在于被 Git
  忽略的 `.cache/`，不得写入命令输出、日志、sidecar、Markdown 或 Git。
- Bilibili 登录态出现中文 AI 字幕时，优先按添加剧集 skill 保存原始字幕响应并使用
  `scripts/import_bilibili_subtitles.py`；不得记录带 `auth_key` 的签名 URL，也不得忽略
  已发现字幕改跑音频 ASR。
- 保留已有来源和 ASR 产物；只有明确要求覆盖时才使用重转写或重对齐选项。
- 下载媒体、日志和临时文件只放在 `.cache/`；模型权重按上面的共享资源规则存放，
  项目仅保留被忽略的引用。上述本地资源不得提交到 Git。
- 正式本地 Qwen ASR 按平台选择 Apple Silicon/MLX 或 Windows/NVIDIA CUDA；不得因
  平台不同而静默切换到远端服务。
- 本地长 ASR 逐集、逐子进程串行执行，避免并发争用 Metal 统一内存或 CUDA 显存，
  并以子进程退出作为对应加速器资源的回收边界。
- 英文正式逐字稿必须同时提供逐段对齐的中文译稿，并保持英文稿为 selected 原文。
- YouTube 官方完整正片播放列表可以作为发现面；tracked 视频必须保留大小写敏感的
  `video_id`、官方 `channel_id` 和扫描时的 `playlist_id`。存在发布者英文 `json3`
  字幕时优先使用字幕导入器；只有逐事件时间轴完全一致时才可配对平台
  `zh-Hans-en` 机器译轨，任何漂移都失败关闭。
- 发布者材料概览使用 `summary: outline`，完整机器稿生成的总结使用
  `summary: draft`，机器逐字稿和机器译稿使用 `machine`；没有完成对应人工工作，
  任何内容都不得标记为 `reviewed`。

## 完成门禁

提交前至少完成以下检查，并分别报告每集达到的状态和剩余人工审核项：

```bash
uv run --no-sync python -m unittest discover -s tests -v
uv run --no-sync python scripts/validate.py
npm --prefix apps/web run check
git diff --check
git status --short
```

同时确认根 README 与对应节目 README 的索引已同步，媒体仍被忽略，预期的 ASR 与 Markdown 产物可被 Git 跟踪。
