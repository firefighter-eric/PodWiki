# PodWiki AI 维护指南

本文件适用于整个仓库；子目录存在更具体的 `AGENTS.md` 时，同时遵守其规则。

## 新增或处理单集

开始修改前，依次完整阅读：

1. [单集处理流程](./docs/episode-processing.md)：端到端步骤、输入输出和停止点；
2. [内容标准](./docs/content-standard.md)：目录、元数据、状态、逐字稿、译稿与索引契约；
3. [PodWiki episode 处理 skill](./.agents/skills/podwiki-process-episode/SKILL.md)：来源限制、ASR 恢复语义和完成检查。

按流程选择相关模板和脚本，不要从已有单集反向猜测未核实的元数据。

## 不可省略的规则

- PodWiki 只收录播客。账号或频道身份、视频时长、访谈外观、标题中的 `EP` 都不能
  单独证明内容是播客；新节目必须有发布者的播客声明、公开播客 feed/平台页，或
  明确标为播客正片的官方合集。只导入完整单集；片段、预告、Shorts、普通视频、
  课程、演讲、发布会、直播及回放默认排除，除非发布者也把同一完整内容作为
  该播客的正式单集发布。
- 只保存去除追踪参数的规范来源 URL；正式期号必须来自发布者，不按输入顺序推断。
- 不绕过登录、会员、付费、地区或其他访问控制；本流程不使用浏览器 cookies，
  即使用户提出也先停止并要求建立单独、明确记录的来源处理流程。
- 保留已有来源和 ASR 产物；只有明确要求覆盖时才使用重转写或重对齐选项。
- 下载媒体、模型、日志和临时文件只放在 `.cache/`，不得提交到 Git。
- 正式本地 Qwen ASR 按平台选择 Apple Silicon/MLX 或 Windows/NVIDIA CUDA；不得因
  平台不同而静默切换到远端服务。
- 本地长 ASR 逐集、逐子进程串行执行，避免并发争用 Metal 统一内存或 CUDA 显存，
  并以子进程退出作为对应加速器资源的回收边界。
- 英文正式逐字稿必须同时提供逐段对齐的中文译稿，并保持英文稿为 selected 原文。
- 发布者材料概览使用 `summary: outline`，完整机器稿生成的总结使用
  `summary: draft`，机器逐字稿和机器译稿使用 `machine`；没有完成对应人工工作，
  任何内容都不得标记为 `reviewed`。

## 完成门禁

提交前至少完成以下检查，并分别报告每集达到的状态和剩余人工审核项：

```bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python -m unittest discover -s tests -v
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/validate.py
npm --prefix apps/web run check
git diff --check
git status --short
```

同时确认根 README 与对应节目 README 的索引已同步，媒体仍被忽略，预期的 ASR 与 Markdown 产物可被 Git 跟踪。
