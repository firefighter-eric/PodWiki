<!-- BEGIN:nextjs-agent-rules -->

# This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` (resolved from this file's directory; in monorepos the `next` package may not be visible from the repo root) before writing any code. Heed deprecation notices.

This block is written and re-added by `next dev` — verify at `node_modules/next/dist/server/lib/generate-agent-files.js`. Removing it from a diff only re-creates the uncommitted change; committing it with your work keeps the tree clean.

<!-- END:nextjs-agent-rules -->

## PodWiki 单集导航标题

- 遵循 `../../docs/content-standard.md` 的 `navigation_title` 与
  `catalog_keyword` 规范。侧栏和搜索结果统一渲染单集 `navigationTitle`；
  不要从发布者原标题、`episodeNumber` 或 `releaseType` 重新拼接。
- `navigationTitle` 的内容契约是“访谈人物 · 精简题目”。可以为视觉样式拆分人物
  与题目，但必须保持原始字符串顺序和完整的可访问文本。
- 单集详情页的主标题也必须来自 `navigationTitle`：主标题显示人物，副标题显示
  精简题目，浏览器和分享元数据使用完整“人物 · 题目”。发布者原标题只用于
  来源溯源，不得重新成为详情页可见标题。
- 不在导航和发现列表前置 `#<期号>`、`第 <期号> 期`、`特访`、`特别` 等徽标。
  正式期号和发布类型只在单集详情、来源和元数据语境中展示。
- 紧凑导航和发现列表的辅助时间只展示 `publishedDate`，不要附加节目时长；
  逐字稿搜索结果的定位时间戳除外。
- 首页最近更新目录使用三段式层级：左侧红色 `catalogKeyword`，正文黑色嘉宾名，
  下一行灰色精简题目。关键词必须来自内容元数据，不得在组件中猜测。
- 单个播客的节目页使用更丰富的三层编辑列表：首行红色嘉宾名和小字“播客名 · 日期”，
  第二行放大精简题目，第三行单独展示从“一句话总结”提取的两行简介。不要为了该列表
  再维护一套简介字段，也不要把 `catalogKeyword` 当作人物名展示。人物列优先获得可用
  宽度，“播客名 · 日期”作为一组靠最右对齐；窄屏允许内容自然收缩或换行，但不得造成
  人物与元信息碰撞或页面横向溢出。
- 侧栏视觉采用两行结构：首行“人物 / 日期”，次行单独显示题目并单行截断。`/shows`
  全局列表先显示红色人物名，再紧随弱化的播客来源；进入 `/shows/<showId>` 后省略
  重复来源。全局链接的可访问文本使用“人物 · 题目 · 播客来源 · 日期”，并保持人物
  与题目优先；单播客列表的可访问文本也省略重复来源。搜索结果保持完整标题，两者都
  不套用目录的关键词三段式样式。
- `/shows` 的“全部单集”必须直接按完整 `publishedAt` 跨播客倒序排列，不得先按播客
  分组；选中播客后只做保序过滤。同一发布时间必须使用稳定的单集标识或链接作为
  确定性排序兜底，不得依赖文件系统枚举顺序。
- 全局侧栏是播客来源的主选择器：来源链接使用 `/shows/<showId>`，选中来源后
  侧栏单集列表只展示该来源；正文目录不再重复一套来源筛选控件。
- 包含标题、摘要或逐字稿内容的整卡链接必须允许文字拖选与复制，并禁用链接原生拖拽；
  形成文字选区时不得触发导航，普通点击、键盘 Enter、右键菜单和新标签页语义必须保留。
  不要对所有 `a`、`button` 或页面全局设置可选中样式，只标记承载可复制正文的链接。
- `/shows` 首页为每档播客使用一张发现卡，每张按全局发布时间排序展示该播客最新
  3 集，并保留到节目页和单集页的真实链接；节目详情页不重复渲染发现卡。
- 所有单集总结的“核心观点”开头维护一张逻辑速览表。列名和行内容由该期议题
  决定，不得由组件生成 `01`、`02` 等装饰性序号，也不得强制所有节目共用同一组列。
  首列作为简短的逻辑维度标签，桌面端按内容取宽且不拆字，不要在 Markdown 中手动
  插入换行；手机端继续转换为纵向卡片。组件只解析并忠实渲染 Markdown 表格；其后
  的完整观点、依据、边界和原文定位保留。
