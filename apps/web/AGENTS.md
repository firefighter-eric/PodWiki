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
- 不在导航和发现列表前置 `#<期号>`、`第 <期号> 期`、`特访`、`特别` 等徽标。
  正式期号和发布类型只在单集详情、来源和元数据语境中展示。
- 紧凑导航和发现列表的辅助时间只展示 `publishedDate`，不要附加节目时长；
  逐字稿搜索结果的定位时间戳除外。
- 节目单集和最近更新目录使用三段式层级：左侧红色 `catalogKeyword`，正文黑色
  嘉宾名，下一行灰色精简题目。关键词必须来自内容元数据，不得在组件中猜测。
- 侧栏及搜索仍保持“人物 · 题目”的完整可访问文本和自然换行，不套用目录的
  关键词三段式样式。
