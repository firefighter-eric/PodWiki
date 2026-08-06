# PodWiki

PodWiki 是一个使用 Markdown 构建的播客 Wiki，收录值得长期阅读的中文播客与视频访谈，并为每期节目保存可追溯的来源、结构化元数据、内容总结和带时间码逐字稿。

项目优先服务播客内容的发现与阅读：节目页提供单集索引，单集页记录来源与处理状态，独立的总结和逐字稿用于快速理解与深入检索。

## Web 阅读器

`apps/web` 是基于 Next.js App Router 的浅色阅读器，直接从仓库中的节目 Markdown 构建页面，提供节目切换、全文搜索、章节定位、摘要/逐字稿切换和本地阅读设置。当前版本专注文字阅读，不包含音频播放器。

```bash
cd apps/web
npm install
npm run dev
```

提交前可运行完整门禁：

```bash
cd apps/web
npm run check
```

部署到 Vercel 时将 Root Directory 设为 `apps/web`，并保持构建步骤可包含 Root Directory 之外的源码。默认内容目录是仓库根目录下的 `shows/`；非标准目录结构可通过 `PODWIKI_REPOSITORY_ROOT` 指定仓库根目录。

## 收录播客

| 播客 | 简介 | 节目页 |
| --- | --- | --- |
| [张小珺商业访谈录](https://space.bilibili.com/280780745/) | 商业与科技深度访谈，关注技术浪潮中的公司、人物与组织。 | [README](./shows/zhangxiaojun/) |
| [罗永浩的十字路口](https://space.bilibili.com/538596213/) | 围绕创业、科技与社会议题，与企业家和研究者展开长谈。 | [README](./shows/luoyonghao/) |
| [WhynotTV](https://space.bilibili.com/14145636/) | 聚焦 AI 技术、工程实践、商业逻辑与个人成长的长篇对谈。 | [README](./shows/whynottv/) |

## 单集索引

| 标题 | 访谈人物 | 播客名称 | 日期 | 总结 | 逐字稿 |
| --- | --- | --- | --- | --- | --- |
| [游凯超：开源 Infra、模型 Co-design 与 vLLM](https://www.bilibili.com/video/BV18Qg96YE1W/) | 游凯超 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-07-28 | [总结](./shows/zhangxiaojun/episodes/148-you-kaichao/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/148-you-kaichao/transcript.zh-CN.md) |
| [特别访谈：廖恒、昇腾史与全球芯片产业](https://www.bilibili.com/video/BV1nB3u6tERu/) | 廖恒 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-07-25 | [总结](./shows/zhangxiaojun/episodes/bili-bv1nb3u6teru-liao-heng/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/bili-bv1nb3u6teru-liao-heng/transcript.zh-CN.md) |
| [柯丽一鸣：Pi 与通用机器人](https://www.bilibili.com/video/BV12bNB6vEtt/) | 柯丽一鸣 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-07-16 | [总结](./shows/zhangxiaojun/episodes/146-ke-liyiming/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/146-ke-liyiming/transcript.zh-CN.md) |
| [洪力德：SpaceX 开发史](https://www.bilibili.com/video/BV1HfEy6jEUx/) | 洪力德 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-06-12 | [总结](./shows/zhangxiaojun/episodes/145-hong-lide/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/145-hong-lide/transcript.zh-CN.md) |
| [姚顺宇：模型训练与技术预测](https://www.bilibili.com/video/BV1YR5E6EE9o/) | 姚顺宇 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-05-11 | [总结](./shows/zhangxiaojun/episodes/140-yao-shunyu/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/140-yao-shunyu/transcript.zh-CN.md) |
| [对罗福莉3.5小时访谈：AI 范式已然巨变](https://www.bilibili.com/video/BV1iVoVBgERD/) | 罗福莉 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-04-24 | [总结](./shows/zhangxiaojun/episodes/138-luo-fuli/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/138-luo-fuli/transcript.zh-CN.md) |
| [携程梁建章 × 罗永浩：企业家与学者之间的“往返票”](https://www.bilibili.com/video/BV1TTdBBtErj/) | 梁建章 | [罗永浩的十字路口](./shows/luoyonghao/) | 2026-04-17 | [总结](./shows/luoyonghao/episodes/025-liang-jianzhang/summary.zh-CN.md) | [逐字稿](./shows/luoyonghao/episodes/025-liang-jianzhang/transcript.zh-CN.md) |
| [对谢赛宁的7小时马拉松访谈：世界模型、逃出硅谷与 AMI Labs](https://www.bilibili.com/video/BV1tew5zVEDf/) | 谢赛宁 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-03-16 | [总结](./shows/zhangxiaojun/episodes/133-xie-saining/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/133-xie-saining/transcript.zh-CN.md) |
| [印奇出任阶跃星辰董事长的访谈：聪明人的诱惑、取舍与超长链路淘汰赛](https://www.bilibili.com/video/BV1ZczaBJE58/) | 印奇 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-01-26 | [总结](./shows/zhangxiaojun/episodes/131-yin-qi/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/131-yin-qi/transcript.zh-CN.md) |
| [翁家翌：OpenAI、强化学习、Infra 与后训练](https://www.bilibili.com/video/BV1darmBcE4A/) | 翁家翌 | [WhynotTV](./shows/whynottv/) | 2026-01-17 | [总结](./shows/whynottv/episodes/004-weng-jiayi/summary.zh-CN.md) | [逐字稿](./shows/whynottv/episodes/004-weng-jiayi/transcript.zh-CN.md) |
| [全球大模型第一股的上市访谈，和智谱 CEO 张鹏聊：敢问路在何方？](https://www.bilibili.com/video/BV1awiDBDEWS/) | 张鹏 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-01-08 | [总结](./shows/zhangxiaojun/episodes/129-zhang-peng/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/129-zhang-peng/transcript.zh-CN.md) |
| [Manus 决定出售前最后的访谈：啊，这奇幻的 2025 年漂流啊…](https://www.bilibili.com/video/BV1knvYBDEjs/) | 季逸超 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2025-12-30 | [总结](./shows/zhangxiaojun/episodes/128-ji-yichao/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/128-ji-yichao/transcript.zh-CN.md) |
| [MiniMax 创始人闫俊杰 × 罗永浩：大山并非无法翻越](https://www.bilibili.com/video/BV11NmtBzE36/) | 闫俊杰 | [罗永浩的十字路口](./shows/luoyonghao/) | 2025-12-10 | [总结](./shows/luoyonghao/episodes/013-yan-junjie/summary.zh-CN.md) | [逐字稿](./shows/luoyonghao/episodes/013-yan-junjie/transcript.zh-CN.md) |
| [朱啸虎现实主义故事的第三次连载：人工智能的盛筵与泡泡](https://www.bilibili.com/video/BV13AmpBiE2o/) | 朱啸虎 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2025-12-09 | [总结](./shows/zhangxiaojun/episodes/122-zhu-xiaohu/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/122-zhu-xiaohu/transcript.zh-CN.md) |
| [和杨植麟时隔1年的对话：K2、Agentic LLM、缸中之脑和“站在无限的开端”](https://www.bilibili.com/video/BV1hFe1zSEXp/) | 杨植麟 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2025-08-27 | [总结](./shows/zhangxiaojun/episodes/113-yang-zhilin/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/113-yang-zhilin/transcript.zh-CN.md) |

内容格式和审核状态见[内容标准](./docs/content-standard.md)，Python 工具和处理命令见[脚本用法](./docs/python-scripts.md)。项目脚本使用 [Apache License 2.0](./LICENSE)；该许可证不自动改变所链接或引用的第三方节目内容的权利状态。
