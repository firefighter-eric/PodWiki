# PodWiki

PodWiki 是一个使用 Markdown 构建的播客 Wiki，收录值得长期阅读的中文播客与视频访谈，并为每期节目保存可追溯的来源、结构化元数据、内容总结和带时间码逐字稿。

项目优先服务播客内容的发现与阅读：节目页提供单集索引，单集页记录来源与处理状态，独立的总结和逐字稿用于快速理解与深入检索。

## 新增单集 / AI 处理

新增、下载、转写、翻译或更新单集时，从[单集处理流程](./docs/episode-processing.md)开始，并同时遵守[内容标准](./docs/content-standard.md)与项目的 [PodWiki episode 处理 skill](./.agents/skills/podwiki-process-episode/SKILL.md)。

## Web 阅读器

`apps/web` 是基于 Next.js App Router 的浅色阅读器，直接从仓库中的节目 Markdown 构建页面，提供节目切换、全文搜索、章节定位、摘要/逐字稿切换和本地阅读设置。当前版本专注文字阅读，不包含音频播放器。

```bash
cd apps/web
npm ci
npm run dev
```

提交前可运行 Web 门禁：

```bash
cd apps/web
npm run check
```

仓库级完整门禁（Python、内容契约、Web 与 Git 检查）见根目录的
[AI 维护指南](./AGENTS.md#完成门禁)。

部署到 Vercel 时将 Root Directory 设为 `apps/web`，并保持构建步骤可包含 Root Directory 之外的源码。默认内容目录是仓库根目录下的 `shows/`；非标准目录结构可通过 `PODWIKI_REPOSITORY_ROOT` 指定仓库根目录。静态路由、内容加载量和同机 A/B 数据见 [Web 阅读器性能基准](./docs/web-performance.md)。

## 收录播客

| 播客 | 简介 | 节目页 |
| --- | --- | --- |
| [张小珺商业访谈录](https://space.bilibili.com/280780745/) | 商业与科技深度访谈，关注技术浪潮中的公司、人物与组织。 | [README](./shows/zhangxiaojun/) |
| [硅谷101](https://space.bilibili.com/508452265/) | 关注全球科技创新、人工智能、创业与商业的深度访谈和产业分析。 | [README](./shows/sv101/) |
| [硅谷坐标 SV-Vector](https://space.bilibili.com/3706937879300857/) | 立足硅谷，聚焦前沿科技与科技投资趋势的深度访谈节目。 | [README](./shows/svvector/) |
| [晚点聊 LateTalk](https://space.bilibili.com/3546915742419882/) | 《晚点 LatePost》出品的科技访谈节目，关注从业者的真实思考。 | [README](./shows/latetalk/) |
| [罗永浩的十字路口](https://space.bilibili.com/538596213/) | 围绕创业、科技与社会议题，与企业家和研究者展开长谈。 | [README](./shows/luoyonghao/) |
| [WhynotTV Podcast](https://space.bilibili.com/14145636/) | 聚焦 AI 技术、工程实践、商业逻辑与个人成长的长篇对谈。 | [README](./shows/whynottv/) |
| [一起铁TALK](https://www.xiaoyuzhoufm.com/podcast/6951e312febad13106eb017e) | 以跑步为入口，聊训练、生活经验和真实处境。 | [README](./shows/yiqitietalk/) |

## 单集索引

| 标题 | 访谈人物 | 播客名称 | 日期 | 总结 | 逐字稿 |
| --- | --- | --- | --- | --- | --- |
| [对话田渊栋：AI 自进化如何到来【晚点聊 LateTalk】](https://www.bilibili.com/video/BV1XnuH66EzS/) | 田渊栋 | [晚点聊 LateTalk](./shows/latetalk/) | 2026-08-07 | [总结](./shows/latetalk/episodes/178-tian-yuandong/summary.zh-CN.md) | [逐字稿](./shows/latetalk/episodes/178-tian-yuandong/transcript.zh-CN.md) |
| [详解 Kimi K3：强到冲击 Anthropic 估值的模型什么样？【晚点聊LateTalk】](https://www.bilibili.com/video/BV1nWM26QEu5/) | 赵晨阳、曾致远 | [晚点聊 LateTalk](./shows/latetalk/) | 2026-08-06 | [总结](./shows/latetalk/episodes/177-zhao-chenyang-zeng-zhiyuan/summary.zh-CN.md) | [逐字稿](./shows/latetalk/episodes/177-zhao-chenyang-zeng-zhiyuan/transcript.zh-CN.md) |
| [对话盛颖：xAI，Infra的浪漫，SGLang，开源，平权与“甄嬛传”【101视频播客】](https://www.bilibili.com/video/BV1GaM968E6T/) | 盛颖 | [硅谷101](./shows/sv101/) | 2026-08-05 | [总结](./shows/sv101/episodes/247-sheng-ying/summary.zh-CN.md) | [逐字稿](./shows/sv101/episodes/247-sheng-ying/transcript.zh-CN.md) |
| [姚顺雨，来到腾讯 300 天【晚点聊LateTalk】](https://www.bilibili.com/video/BV1DDGu6VEzo/) | 高洪浩 | [晚点聊 LateTalk](./shows/latetalk/) | 2026-08-01 | [总结](./shows/latetalk/episodes/176-gao-honghao/summary.zh-CN.md) | [逐字稿](./shows/latetalk/episodes/176-gao-honghao/transcript.zh-CN.md) |
| [硅谷坐标 × Lam Research 创始人林杰屏：AI超级周期和四十年半导体周期感悟](https://www.bilibili.com/video/BV1JZGc6iEjv/) | 林杰屏 | [硅谷坐标 SV-Vector](./shows/svvector/) | 2026-07-31 | [总结](./shows/svvector/episodes/bili-bv1jzgc6iejv-lin-jieping/summary.zh-CN.md) | [英文逐字稿](./shows/svvector/episodes/bili-bv1jzgc6iejv-lin-jieping/transcript.en.md) · [中文机器翻译](./shows/svvector/episodes/bili-bv1jzgc6iejv-lin-jieping/transcript.zh-CN.md) |
| [对话 Liblib 陈冕：关于活下来，以及所有接近死亡的时刻【晚点聊LateTalk】](https://www.bilibili.com/video/BV1ZP3863E3E/) | 陈冕 | [晚点聊 LateTalk](./shows/latetalk/) | 2026-07-30 | [总结](./shows/latetalk/episodes/175-chen-mian/summary.zh-CN.md) | [逐字稿](./shows/latetalk/episodes/175-chen-mian/transcript.zh-CN.md) |
| [AI 冲击企业软件巨头？与SAP原欣聊大模型 to B 的颠覆与边界【晚点聊LateTalk】](https://www.bilibili.com/video/BV1zQ3i6YErP/) | 原欣 | [晚点聊 LateTalk](./shows/latetalk/) | 2026-07-28 | [总结](./shows/latetalk/episodes/174-yuan-xin/summary.zh-CN.md) | [逐字稿](./shows/latetalk/episodes/174-yuan-xin/transcript.zh-CN.md) |
| [对话叶奇意：“寻找”月之暗面杨植麟、中国两代AI、十年人才迁徙，与AGI信仰【101视频播客】](https://www.bilibili.com/video/BV1wK3i6NEdQ/) | 叶奇意 | [硅谷101](./shows/sv101/) | 2026-07-28 | [总结](./shows/sv101/episodes/bili-bv1wk3i6nedq-ye-qiyi/summary.zh-CN.md) | [逐字稿](./shows/sv101/episodes/bili-bv1wk3i6nedq-ye-qiyi/transcript.zh-CN.md) |
| [具身季报 26Q2：世界模型大风不停，和不想被贴标签的人【晚点聊LateTalk】](https://www.bilibili.com/video/BV1Eb3Y6QEMs/) | 陈哲 | [晚点聊 LateTalk](./shows/latetalk/) | 2026-07-28 | [总结](./shows/latetalk/episodes/170-chen-zhe/summary.zh-CN.md) | [逐字稿](./shows/latetalk/episodes/170-chen-zhe/transcript.zh-CN.md) |
| [对游凯超3小时访谈：开源Infra、和模型Co-design 、“如果vLLM失败，我们会后悔一辈子”](https://www.bilibili.com/video/BV18Qg96YE1W/) | 游凯超 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-07-28 | [总结](./shows/zhangxiaojun/episodes/148-you-kaichao/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/148-you-kaichao/transcript.zh-CN.md) |
| [对华为半导体首席科学家廖恒的5小时访谈：一部昇腾史、18层宝塔与全球芯片恢弘30年史诗\| B站 x WAIC AI会客厅](https://www.bilibili.com/video/BV1nB3u6tERu/) | 廖恒 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-07-25 | [总结](./shows/zhangxiaojun/episodes/bili-bv1nb3u6teru-liao-heng/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/bili-bv1nb3u6teru-liao-heng/transcript.zh-CN.md) |
| [Momenta IPO 后再访曹旭东：就是想做没有尽头的 AI【晚点聊LateTalk】](https://www.bilibili.com/video/BV1ASga6xEeZ/) | 曹旭东 | [晚点聊 LateTalk](./shows/latetalk/) | 2026-07-24 | [总结](./shows/latetalk/episodes/172-cao-xudong/summary.zh-CN.md) | [逐字稿](./shows/latetalk/episodes/172-cao-xudong/transcript.zh-CN.md) |
| [对话深庭纪王弢：人形之外，具身还有另一种答案【晚点LatePost】](https://www.bilibili.com/video/BV1GsgD6sEnU/) | 王弢 | [晚点聊 LateTalk](./shows/latetalk/) | 2026-07-23 | [总结](./shows/latetalk/episodes/bili-bv1gsgd6senu-wang-tao/summary.zh-CN.md) | [逐字稿](./shows/latetalk/episodes/bili-bv1gsgd6senu-wang-tao/transcript.zh-CN.md) |
| [26 岁 3 亿美元卖公司“开心只有两分钟”，不想 boring 就继续 suffering【晚点聊 LateTalk】](https://www.bilibili.com/video/BV1tYgz6JEvm/) | 姚颂 | [晚点聊 LateTalk](./shows/latetalk/) | 2026-07-22 | [总结](./shows/latetalk/episodes/173-yao-song/summary.zh-CN.md) | [逐字稿](./shows/latetalk/episodes/173-yao-song/transcript.zh-CN.md) |
| [AI 季报 26Q2：从 coding 到 RSI，强者愈强的未来？【晚点聊LateTalk】](https://www.bilibili.com/video/BV1Mhgz6QEHA/) | Henry Yin | [晚点聊 LateTalk](./shows/latetalk/) | 2026-07-22 | [总结](./shows/latetalk/episodes/171-henry-yin/summary.zh-CN.md) | [逐字稿](./shows/latetalk/episodes/171-henry-yin/transcript.zh-CN.md) |
| [姚妙“教”吴向东越野？不不不，让我们一起撒开脚丫](https://www.xiaoyuzhoufm.com/episode/6a5f4d33a3fec224d5a1136a) | — | [一起铁TALK](./shows/yiqitietalk/) | 2026-07-21 | [总结](./shows/yiqitietalk/episodes/20-yao-miao/summary.zh-CN.md) | [逐字稿](./shows/yiqitietalk/episodes/20-yao-miao/transcript.zh-CN.md) |
| [对话Vincent Koc：OpenClaw的反思与进化，与Agent的下一步 \| B站 x WAIC AI会客厅【101视频播客】](https://www.bilibili.com/video/BV1pNKU6dE3V/) | Vincent Koc | [硅谷101](./shows/sv101/) | 2026-07-20 | [总结](./shows/sv101/episodes/bili-bv1pnku6de3v-vincent-koc/summary.zh-CN.md) | [英文逐字稿](./shows/sv101/episodes/bili-bv1pnku6de3v-vincent-koc/transcript.en.md) · [中文机器翻译](./shows/sv101/episodes/bili-bv1pnku6de3v-vincent-koc/transcript.zh-CN.md) |
| [此沙与吴向东的首次越野赛](https://www.xiaoyuzhoufm.com/episode/6a5cd2586356eb2d9be50430) | — | [一起铁TALK](./shows/yiqitietalk/) | 2026-07-20 | [总结](./shows/yiqitietalk/episodes/19-ci-sha/summary.zh-CN.md) | [逐字稿](./shows/yiqitietalk/episodes/19-ci-sha/transcript.zh-CN.md) |
| [世界模型这半年：路线争议、数据来源与商业落地【晚点LatePost】](https://www.bilibili.com/video/BV1Z9KA6sE9Q/) | 王广润、蒲韬、仲黎若 | [晚点聊 LateTalk](./shows/latetalk/) | 2026-07-18 | [总结](./shows/latetalk/episodes/bili-bv1z9ka6se9q-wang-guangrun-pu-tao-zhong-liruo/summary.zh-CN.md) | [逐字稿](./shows/latetalk/episodes/bili-bv1z9ka6se9q-wang-guangrun-pu-tao-zhong-liruo/transcript.zh-CN.md) |
| [对Physical Intelligence柯丽一鸣4小时访谈：Pi的开源模型研究，机器人的江湖、族谱与主角](https://www.bilibili.com/video/BV12bNB6vEtt/) | 柯丽一鸣 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-07-16 | [总结](./shows/zhangxiaojun/episodes/146-ke-liyiming/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/146-ke-liyiming/transcript.zh-CN.md) |
| [吴健：运动员与迈胜创始人](https://www.xiaoyuzhoufm.com/episode/6a58b864016dcc7e05433391) | 吴健 | [一起铁TALK](./shows/yiqitietalk/) | 2026-07-16 | [总结](./shows/yiqitietalk/episodes/18-wu-jian/summary.zh-CN.md) | [逐字稿](./shows/yiqitietalk/episodes/18-wu-jian/transcript.zh-CN.md) |
| [AI 硬件大爆发，谁能抢占下一个“iPhone 时刻”【晚点LatePost】](https://www.bilibili.com/video/BV1bVNn6XERr/) | 李宏伟 | [晚点聊 LateTalk](./shows/latetalk/) | 2026-07-10 | [总结](./shows/latetalk/episodes/bili-bv1bvnn6xerr-li-hongwei/summary.zh-CN.md) | [逐字稿](./shows/latetalk/episodes/bili-bv1bvnn6xerr-li-hongwei/transcript.zh-CN.md) |
| [美国AI研究员的中国之旅：年轻人，追赶者，算力焦虑与“AGI展示厅” ｜专访Nathan Lambert【101视频播客】](https://www.bilibili.com/video/BV1HXTs6bEzH/) | Nathan Lambert | [硅谷101](./shows/sv101/) | 2026-07-03 | [总结](./shows/sv101/episodes/bili-bv1hxts6bezh-nathan-lambert/summary.zh-CN.md) | [英文逐字稿](./shows/sv101/episodes/bili-bv1hxts6bezh-nathan-lambert/transcript.en.md) · [中文机器翻译](./shows/sv101/episodes/bili-bv1hxts6bezh-nathan-lambert/transcript.zh-CN.md) |
| [徐冰洁：给你带来的荣耀和光环，就得忍受它的枯燥](https://www.xiaoyuzhoufm.com/episode/6a47910b3fb7233cbf433c35) | — | [一起铁TALK](./shows/yiqitietalk/) | 2026-07-03 | [总结](./shows/yiqitietalk/episodes/17-xu-bingjie/summary.zh-CN.md) | [逐字稿](./shows/yiqitietalk/episodes/17-xu-bingjie/transcript.zh-CN.md) |
| [【视频播客】硅谷坐标 x Tensormesh 江鋆晨：AI 的记忆-KvCache的三层理解](https://www.bilibili.com/video/BV1JjTw6REEX/) | 江鋆晨 | [硅谷坐标 SV-Vector](./shows/svvector/) | 2026-06-30 | [总结](./shows/svvector/episodes/bili-bv1jjtw6reex-jiang-yunchen/summary.zh-CN.md) | [逐字稿](./shows/svvector/episodes/bili-bv1jjtw6reex-jiang-yunchen/transcript.zh-CN.md) |
| [对话王熙乔：AI时代的教育者、十年沉浮，与人类文明的下一步【101视频播客】](https://www.bilibili.com/video/BV1Ed7n6TEr1/) | 王熙乔 | [硅谷101](./shows/sv101/) | 2026-06-27 | [总结](./shows/sv101/episodes/bili-bv1ed7n6ter1-wang-xiqiao/summary.zh-CN.md) | [逐字稿](./shows/sv101/episodes/bili-bv1ed7n6ter1-wang-xiqiao/transcript.zh-CN.md) |
| [许乐：我还要干票大的！](https://www.xiaoyuzhoufm.com/episode/6a3a595e2e335a35a808142c) | — | [一起铁TALK](./shows/yiqitietalk/) | 2026-06-23 | [总结](./shows/yiqitietalk/episodes/16-xu-le/summary.zh-CN.md) | [逐字稿](./shows/yiqitietalk/episodes/16-xu-le/transcript.zh-CN.md) |
| [硅谷坐标 x 喜马拉雅资本常劲：AI时代的价值投资](https://www.bilibili.com/video/BV1np7P6REFg/) | 常劲 | [硅谷坐标 SV-Vector](./shows/svvector/) | 2026-06-22 | [总结](./shows/svvector/episodes/bili-bv1np7p6refg-chang-jin/summary.zh-CN.md) | [逐字稿](./shows/svvector/episodes/bili-bv1np7p6refg-chang-jin/transcript.zh-CN.md) |
| [吴冰：我要参加亚运会马拉松比赛啦！](https://www.xiaoyuzhoufm.com/episode/6a3257ae4233e62bc54b5ec4) | 吴冰 | [一起铁TALK](./shows/yiqitietalk/) | 2026-06-17 | [总结](./shows/yiqitietalk/episodes/15-wu-bing/summary.zh-CN.md) | [逐字稿](./shows/yiqitietalk/episodes/15-wu-bing/transcript.zh-CN.md) |
| [口述SpaceX开发史：和前高管洪力德聊，马斯克用人观、最大IPO、太空与AI、人类文明扩张前奏？](https://www.bilibili.com/video/BV1HfEy6jEUx/) | 洪力德 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-06-12 | [总结](./shows/zhangxiaojun/episodes/145-hong-lide/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/145-hong-lide/transcript.zh-CN.md) |
| [李美珍：我是你们的马拉松运动员李美珍](https://www.xiaoyuzhoufm.com/episode/6a25611c7444b5722234d445) | 李美珍 | [一起铁TALK](./shows/yiqitietalk/) | 2026-06-07 | [总结](./shows/yiqitietalk/episodes/14-li-meizhen/summary.zh-CN.md) | [逐字稿](./shows/yiqitietalk/episodes/14-li-meizhen/transcript.zh-CN.md) |
| [再访田渊栋：46.5亿美金估值的RSI，与AI自进化｜Neolabs特辑【101视频播客】](https://www.bilibili.com/video/BV1DY7C6nEWM/) | 田渊栋 | [硅谷101](./shows/sv101/) | 2026-06-05 | [总结](./shows/sv101/episodes/bili-bv1dy7c6newm-tian-yuandong/summary.zh-CN.md) | [逐字稿](./shows/sv101/episodes/bili-bv1dy7c6newm-tian-yuandong/transcript.zh-CN.md) |
| [硅谷坐标x璞林资本Kenny Zhang：Neocloud崛起背后的供需博弈与AI基建重构](https://www.bilibili.com/video/BV14JEN66EkC/) | Kenny Zhang | [硅谷坐标 SV-Vector](./shows/svvector/) | 2026-06-05 | [总结](./shows/svvector/episodes/bili-bv14jen66ekc-kenny-zhang/summary.zh-CN.md) | [逐字稿](./shows/svvector/episodes/bili-bv14jen66ekc-kenny-zhang/transcript.zh-CN.md) |
| [“谷歌太慢了”：与Andrew Dai聊Gemini的翻身之战，出走与视觉理解模型【硅谷101视频播客】](https://www.bilibili.com/video/BV1JCLw61E2d/) | Andrew Dai | [硅谷101](./shows/sv101/) | 2026-05-19 | [总结](./shows/sv101/episodes/bili-bv1jclw61e2d-andrew-dai/summary.zh-CN.md) | [逐字稿](./shows/sv101/episodes/bili-bv1jclw61e2d-andrew-dai/transcript.zh-CN.md) |
| [【正片】李想×罗永浩！李想的理想：通过 AI 技术，让普通人也过上富豪的生活](https://www.bilibili.com/video/BV1LD5T6pEp4/) | 李想 | [罗永浩的十字路口](./shows/luoyonghao/) | 2026-05-13 | [总结](./shows/luoyonghao/episodes/027-li-xiang/summary.zh-CN.md) | [逐字稿](./shows/luoyonghao/episodes/027-li-xiang/transcript.zh-CN.md) |
| [对姚顺宇的4小时访谈：请允许我小疯一下！在Anthropic和Gemini训模型、技术预测、英雄主义已过去](https://www.bilibili.com/video/BV1YR5E6EE9o/) | 姚顺宇 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-05-11 | [总结](./shows/zhangxiaojun/episodes/140-yao-shunyu/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/140-yao-shunyu/transcript.zh-CN.md) |
| [硅谷坐标 x FundaAI创始人周默：四大科技公司财报后的AI产业深度观察](https://www.bilibili.com/video/BV11QRrBcEz3/) | 周默 | [硅谷坐标 SV-Vector](./shows/svvector/) | 2026-05-05 | [总结](./shows/svvector/episodes/bili-bv11qrrbcez3-zhou-mo/summary.zh-CN.md) | [逐字稿](./shows/svvector/episodes/bili-bv11qrrbcez3-zhou-mo/transcript.zh-CN.md) |
| [Danfei Xu：人类数据，行为克隆，机器人GPT-3，全栈，EgoMimic，遥操作，UMI，斯坦福 \| WhynotTV Podcast](https://www.bilibili.com/video/BV1usRgBEESe/) | 徐丹飞 | [WhynotTV Podcast](./shows/whynottv/) | 2026-05-01 | [总结](./shows/whynottv/episodes/005-xu-danfei/summary.zh-CN.md) | [逐字稿](./shows/whynottv/episodes/005-xu-danfei/transcript.zh-CN.md) |
| [杨春龙：我的过去与我的未来](https://www.xiaoyuzhoufm.com/episode/69eda0281e94ae69212b1c74) | 杨春龙 | [一起铁TALK](./shows/yiqitietalk/) | 2026-04-26 | [总结](./shows/yiqitietalk/episodes/13-yang-chunlong/summary.zh-CN.md) | [逐字稿](./shows/yiqitietalk/episodes/13-yang-chunlong/transcript.zh-CN.md) |
| [硅谷坐标对话Terahop于让尘：AI 光互连的超级周期](https://www.bilibili.com/video/BV1kVoJBeE9h/) | 于让尘 | [硅谷坐标 SV-Vector](./shows/svvector/) | 2026-04-25 | [总结](./shows/svvector/episodes/005-yu-rangchen/summary.zh-CN.md) | [逐字稿](./shows/svvector/episodes/005-yu-rangchen/transcript.zh-CN.md) |
| [对罗福莉3.5小时访谈：AI 范式已然巨变](https://www.bilibili.com/video/BV1iVoVBgERD/) | 罗福莉 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-04-24 | [总结](./shows/zhangxiaojun/episodes/138-luo-fuli/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/138-luo-fuli/transcript.zh-CN.md) |
| [携程梁建章 × 罗永浩：企业家与学者之间的“往返票”](https://www.bilibili.com/video/BV1TTdBBtErj/) | 梁建章 | [罗永浩的十字路口](./shows/luoyonghao/) | 2026-04-17 | [总结](./shows/luoyonghao/episodes/025-liang-jianzhang/summary.zh-CN.md) | [逐字稿](./shows/luoyonghao/episodes/025-liang-jianzhang/transcript.zh-CN.md) |
| [硅谷坐标 x黄东旭-龙虾的“记忆” ：谈 Agent 时代基础设施的重构](https://www.bilibili.com/video/BV1zvQKB5EGd/) | 黄东旭 | [硅谷坐标 SV-Vector](./shows/svvector/) | 2026-04-11 | [总结](./shows/svvector/episodes/bili-bv1zvqkb5egd-huang-dongxu/summary.zh-CN.md) | [逐字稿](./shows/svvector/episodes/bili-bv1zvqkb5egd-huang-dongxu/transcript.zh-CN.md) |
| [何杰：亚运会、全运会马拉松男子冠军，两次男子马拉松国家纪录创造者](https://www.xiaoyuzhoufm.com/episode/69d4aacee2c8be3155905460) | 何杰 | [一起铁TALK](./shows/yiqitietalk/) | 2026-04-07 | [总结](./shows/yiqitietalk/episodes/12-he-jie/summary.zh-CN.md) | [逐字稿](./shows/yiqitietalk/episodes/12-he-jie/transcript.zh-CN.md) |
| [申加升、巴斯（李鹏程）：F4初出道，顶级耐力运动员的大聊天](https://www.xiaoyuzhoufm.com/episode/69c9b88eb977fb2c4790ec42) | 申加升、巴斯（李鹏程） | [一起铁TALK](./shows/yiqitietalk/) | 2026-03-30 | [总结](./shows/yiqitietalk/episodes/11-shen-jiasheng-li-pengcheng/summary.zh-CN.md) | [逐字稿](./shows/yiqitietalk/episodes/11-shen-jiasheng-li-pengcheng/transcript.zh-CN.md) |
| [硅谷坐标 x Jimmy Cheng，GTC回顾-AI时代英伟达的护城河](https://www.bilibili.com/video/BV1SmXJBiEEx/) | 程暨杨 | [硅谷坐标 SV-Vector](./shows/svvector/) | 2026-03-26 | [总结](./shows/svvector/episodes/bili-bv1smxjbieex-jimmy-cheng/summary.zh-CN.md) | [逐字稿](./shows/svvector/episodes/bili-bv1smxjbieex-jimmy-cheng/transcript.zh-CN.md) |
| [张唯雅：三个跑步的人，坐在家里瞎聊](https://www.xiaoyuzhoufm.com/episode/69be8dc42d318777c90884be) | 张唯雅 | [一起铁TALK](./shows/yiqitietalk/) | 2026-03-21 | [总结](./shows/yiqitietalk/episodes/10-zhang-weiya/summary.zh-CN.md) | [逐字稿](./shows/yiqitietalk/episodes/10-zhang-weiya/transcript.zh-CN.md) |
| [硅谷坐标 x 微软战投合伙人：AI 时代软件的护城河](https://www.bilibili.com/video/BV1fpwEzTExd/) | Alan Du | [硅谷坐标 SV-Vector](./shows/svvector/) | 2026-03-16 | [总结](./shows/svvector/episodes/002-alan-du/summary.zh-CN.md) | [逐字稿](./shows/svvector/episodes/002-alan-du/transcript.zh-CN.md) |
| [对谢赛宁的7小时马拉松访谈：世界模型、逃出硅谷与 AMI Labs](https://www.bilibili.com/video/BV1tew5zVEDf/) | 谢赛宁 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-03-16 | [总结](./shows/zhangxiaojun/episodes/133-xie-saining/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/133-xie-saining/transcript.zh-CN.md) |
| [路颖：中国女子路跑运动员](https://www.xiaoyuzhoufm.com/episode/69b51ccdcaaea1fb3b32ba7c) | — | [一起铁TALK](./shows/yiqitietalk/) | 2026-03-14 | [总结](./shows/yiqitietalk/episodes/9-lu-ying/summary.zh-CN.md) | [逐字稿](./shows/yiqitietalk/episodes/9-lu-ying/transcript.zh-CN.md) |
| [硅谷坐标 x 田渊栋: 解析大模型护城河、记忆存储瓶颈与Agent对社会冲击](https://www.bilibili.com/video/BV1FZPhzSEXt/) | 田渊栋 | [硅谷坐标 SV-Vector](./shows/svvector/) | 2026-03-07 | [总结](./shows/svvector/episodes/bili-bv1fzphzsext-tian-yuandong/summary.zh-CN.md) | [逐字稿](./shows/svvector/episodes/bili-bv1fzphzsext-tian-yuandong/transcript.zh-CN.md) |
| [大阪之夜， 王颖（吴向东经纪人）、吴向东与孙瑞一 聊天局](https://www.xiaoyuzhoufm.com/episode/69a5692ea22480add6aeca35) | — | [一起铁TALK](./shows/yiqitietalk/) | 2026-03-02 | [总结](./shows/yiqitietalk/episodes/8-wang-ying/summary.zh-CN.md) | [逐字稿](./shows/yiqitietalk/episodes/8-wang-ying/transcript.zh-CN.md) |
| [李芷萱：我的PB 奥运 全运 和结婚](https://www.xiaoyuzhoufm.com/episode/69992553a22480add6994d83) | 李芷萱 | [一起铁TALK](./shows/yiqitietalk/) | 2026-02-21 | [总结](./shows/yiqitietalk/episodes/7-li-zhixuan/summary.zh-CN.md) | [逐字稿](./shows/yiqitietalk/episodes/7-li-zhixuan/transcript.zh-CN.md) |
| [管油胜：这十年我都没有认真做过运动员](https://www.xiaoyuzhoufm.com/episode/6987349566e2c303774c39fc) | — | [一起铁TALK](./shows/yiqitietalk/) | 2026-02-07 | [总结](./shows/yiqitietalk/episodes/6-guan-yousheng/summary.zh-CN.md) | [逐字稿](./shows/yiqitietalk/episodes/6-guan-yousheng/transcript.zh-CN.md) |
| [姚妙：在奔跑中寻找](https://www.xiaoyuzhoufm.com/episode/697df6e62fc7f49d0925c9e4) | 姚妙 | [一起铁TALK](./shows/yiqitietalk/) | 2026-01-31 | [总结](./shows/yiqitietalk/episodes/5-yao-miao/summary.zh-CN.md) | [逐字稿](./shows/yiqitietalk/episodes/5-yao-miao/transcript.zh-CN.md) |
| [印奇出任阶跃星辰董事长的访谈：聪明人的诱惑、取舍与超长链路淘汰赛](https://www.bilibili.com/video/BV1ZczaBJE58/) | 印奇 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-01-26 | [总结](./shows/zhangxiaojun/episodes/131-yin-qi/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/131-yin-qi/transcript.zh-CN.md) |
| [贾俄仁加：运动员、贾老板、父亲，多重身份加身，仍要奋力一搏](https://www.xiaoyuzhoufm.com/episode/6975d6bfef1cf272a75432b6) | 贾俄仁加 | [一起铁TALK](./shows/yiqitietalk/) | 2026-01-25 | [总结](./shows/yiqitietalk/episodes/4-jia-e-ren-jia/summary.zh-CN.md) | [逐字稿](./shows/yiqitietalk/episodes/4-jia-e-ren-jia/transcript.zh-CN.md) |
| [翁家翌：OpenAI，GPT，强化学习，Infra，后训练，天授，tuixue，开源，CMU，清华｜WhynotTV Podcast](https://www.bilibili.com/video/BV1darmBcE4A/) | 翁家翌 | [WhynotTV Podcast](./shows/whynottv/) | 2026-01-17 | [总结](./shows/whynottv/episodes/004-weng-jiayi/summary.zh-CN.md) | [逐字稿](./shows/whynottv/episodes/004-weng-jiayi/transcript.zh-CN.md) |
| [张德顺：山里跑出来的天才女子正在向下一座山进发](https://www.xiaoyuzhoufm.com/episode/696b98a8109824f9e1050609) | 张德顺 | [一起铁TALK](./shows/yiqitietalk/) | 2026-01-17 | [总结](./shows/yiqitietalk/episodes/3-zhang-deshun/summary.zh-CN.md) | [逐字稿](./shows/yiqitietalk/episodes/3-zhang-deshun/transcript.zh-CN.md) |
| [李健 铁蛋：职业运动员就是要做自己认为对的事情](https://www.xiaoyuzhoufm.com/episode/69624948f8b05f9f75d72c22) | 李健（铁蛋） | [一起铁TALK](./shows/yiqitietalk/) | 2026-01-10 | [总结](./shows/yiqitietalk/episodes/2-li-jian/summary.zh-CN.md) | [逐字稿](./shows/yiqitietalk/episodes/2-li-jian/transcript.zh-CN.md) |
| [全球大模型第一股的上市访谈，和智谱 CEO 张鹏聊：敢问路在何方？](https://www.bilibili.com/video/BV1awiDBDEWS/) | 张鹏 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-01-08 | [总结](./shows/zhangxiaojun/episodes/129-zhang-peng/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/129-zhang-peng/transcript.zh-CN.md) |
| [Manus 决定出售前最后的访谈：啊，这奇幻的 2025 年漂流啊…](https://www.bilibili.com/video/BV1knvYBDEjs/) | 季逸超 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2025-12-30 | [总结](./shows/zhangxiaojun/episodes/128-ji-yichao/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/128-ji-yichao/transcript.zh-CN.md) |
| [在赛场狂奔，在播客走心，一起铁Talk](https://www.xiaoyuzhoufm.com/episode/6952860114db1df9ef5c3a88) | — | [一起铁TALK](./shows/yiqitietalk/) | 2025-12-29 | [总结](./shows/yiqitietalk/episodes/1-sun-ruiyi-wu-xiangdong/summary.zh-CN.md) | [逐字稿](./shows/yiqitietalk/episodes/1-sun-ruiyi-wu-xiangdong/transcript.zh-CN.md) |
| [MiniMax 创始人闫俊杰 × 罗永浩：大山并非无法翻越](https://www.bilibili.com/video/BV11NmtBzE36/) | 闫俊杰 | [罗永浩的十字路口](./shows/luoyonghao/) | 2025-12-10 | [总结](./shows/luoyonghao/episodes/013-yan-junjie/summary.zh-CN.md) | [逐字稿](./shows/luoyonghao/episodes/013-yan-junjie/transcript.zh-CN.md) |
| [朱啸虎现实主义故事的第三次连载：人工智能的盛筵与泡泡](https://www.bilibili.com/video/BV13AmpBiE2o/) | 朱啸虎 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2025-12-09 | [总结](./shows/zhangxiaojun/episodes/122-zhu-xiaohu/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/122-zhu-xiaohu/transcript.zh-CN.md) |
| [语音智能体商业落地的教训、经验与实践｜李沐硅谷101年度线下大会演讲（全英）](https://www.bilibili.com/video/BV1dZsCzfEMV/) | 李沐 | [硅谷101](./shows/sv101/) | 2025-10-27 | [总结](./shows/sv101/episodes/bili-bv1dzsczfemv-li-mu/summary.zh-CN.md) | [英文逐字稿](./shows/sv101/episodes/bili-bv1dzsczfemv-li-mu/transcript.en.md) · [中文机器翻译](./shows/sv101/episodes/bili-bv1dzsczfemv-li-mu/transcript.zh-CN.md) |
| [【正片】影视飓风TIM×罗永浩！用影像打开世界的梦想家](https://www.bilibili.com/video/BV1B5xkzPEhx/) | 潘天鸿 | [罗永浩的十字路口](./shows/luoyonghao/) | 2025-10-10 | [总结](./shows/luoyonghao/episodes/006-pan-tianhong/summary.zh-CN.md) | [逐字稿](./shows/luoyonghao/episodes/006-pan-tianhong/transcript.zh-CN.md) |
| [【正片】周鸿祎×罗永浩！近四小时高密度输出！周鸿祎深度谈 AI](https://www.bilibili.com/video/BV1hNJ1zLEb8/) | 周鸿祎 | [罗永浩的十字路口](./shows/luoyonghao/) | 2025-09-24 | [总结](./shows/luoyonghao/episodes/005-zhou-hongyi/summary.zh-CN.md) | [逐字稿](./shows/luoyonghao/episodes/005-zhou-hongyi/transcript.zh-CN.md) |
| [陈天奇：机器学习系统，长期主义，初心，XGBoost，MXNet，TVM，MLC LLM，OctoML｜WhynotTV Podcast](https://www.bilibili.com/video/BV1s6pgzLE3y/) | 陈天奇 | [WhynotTV Podcast](./shows/whynottv/) | 2025-09-12 | [总结](./shows/whynottv/episodes/003-chen-tianqi/summary.zh-CN.md) | [逐字稿](./shows/whynottv/episodes/003-chen-tianqi/transcript.zh-CN.md) |
| [和杨植麟时隔1年的对话：K2、Agentic LLM、缸中之脑和“站在无限的开端”](https://www.bilibili.com/video/BV1hFe1zSEXp/) | 杨植麟 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2025-08-27 | [总结](./shows/zhangxiaojun/episodes/113-yang-zhilin/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/113-yang-zhilin/transcript.zh-CN.md) |
| [【正片】何小鹏×罗永浩！何小鹏讲述从财富自由奔赴无尽地狱模式的创业故事](https://www.bilibili.com/video/BV1jTedzREds/) | 何小鹏 | [罗永浩的十字路口](./shows/luoyonghao/) | 2025-08-26 | [总结](./shows/luoyonghao/episodes/002-he-xiaopeng/summary.zh-CN.md) | [逐字稿](./shows/luoyonghao/episodes/002-he-xiaopeng/transcript.zh-CN.md) |
| [胡渊鸣：Meshy AI，太极，MIT，清华姚班，图形学，物理仿真模拟，开源，商业化，勇气 ，智慧 ｜ WhynotTV Podcast](https://www.bilibili.com/video/BV1XmtyzKEzQ/) | 胡渊鸣 | [WhynotTV Podcast](./shows/whynottv/) | 2025-08-08 | [总结](./shows/whynottv/episodes/002-hu-yuanming/summary.zh-CN.md) | [逐字稿](./shows/whynottv/episodes/002-hu-yuanming/transcript.zh-CN.md) |
| [杨硕：妙动科技，特斯拉Optimus，CMU，大疆，无人机，人形机器人｜WhynotTV Podcast](https://www.bilibili.com/video/BV1em3XznEFx/) | 杨硕 | [WhynotTV Podcast](./shows/whynottv/) | 2025-07-05 | [总结](./shows/whynottv/episodes/001-yang-shuo/summary.zh-CN.md) | [逐字稿](./shows/whynottv/episodes/001-yang-shuo/transcript.zh-CN.md) |

内容格式和审核状态见[内容标准](./docs/content-standard.md)，Python 工具和处理命令见[脚本用法](./docs/python-scripts.md)。项目脚本使用 [Apache License 2.0](./LICENSE)；该许可证不自动改变所链接或引用的第三方节目内容的权利状态。
