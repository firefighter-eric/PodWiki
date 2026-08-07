# PodWiki

PodWiki 是一个使用 Markdown 构建的播客 Wiki，收录值得长期阅读的中文播客与视频访谈，并为每期节目保存可追溯的来源、结构化元数据、内容总结和带时间码逐字稿。

项目优先服务播客内容的发现与阅读：节目页提供单集索引，单集页记录来源与处理状态，独立的总结和逐字稿用于快速理解与深入检索。

## 新增单集 / AI 处理

新增、下载、转写、翻译或更新单集时，从[单集处理流程](./docs/episode-processing.md)开始，并同时遵守[内容标准](./docs/content-standard.md)与项目的 [PodWiki episode 处理 skill](./.agents/skills/podwiki-process-episode/SKILL.md)。

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
| [硅谷101](https://space.bilibili.com/508452265/) | 关注全球科技创新、人工智能、创业与商业的深度访谈和产业分析。 | [README](./shows/sv101/) |
| [晚点聊 LateTalk](https://space.bilibili.com/3546915742419882/) | 《晚点 LatePost》出品的科技访谈节目，关注从业者的真实思考。 | [README](./shows/latetalk/) |
| [罗永浩的十字路口](https://space.bilibili.com/538596213/) | 围绕创业、科技与社会议题，与企业家和研究者展开长谈。 | [README](./shows/luoyonghao/) |
| [WhynotTV](https://space.bilibili.com/14145636/) | 聚焦 AI 技术、工程实践、商业逻辑与个人成长的长篇对谈。 | [README](./shows/whynottv/) |
| [跑步播客「大概纸示」](https://www.xiaoyuzhoufm.com/podcast/6697cbecf103d7b06d18488b) | 以长跑为起点，延伸到越野跑、骑行、徒步等户外运动。 | [README](./shows/dagaizhishi/) |
| [一起铁TALK](https://www.xiaoyuzhoufm.com/podcast/6951e312febad13106eb017e) | 以跑步为入口，聊训练、生活经验和真实处境。 | [README](./shows/yiqitietalk/) |
| [信口开合·跑步播客](https://www.xiaoyuzhoufm.com/podcast/6588196412e01d7ba13aad47) | 用跑步的方式，探索和连接更大的世界。 | [README](./shows/xinkoukaihe/) |
| [二的三次方](https://www.xiaoyuzhoufm.com/podcast/64bf965274d8c90965c62fff) | 八位喜剧人发起的聊天播客，记录喜剧人线下的样子。 | [README](./shows/erdesancifang/) |

## 单集索引

| 标题 | 访谈人物 | 播客名称 | 日期 | 总结 | 逐字稿 |
| --- | --- | --- | --- | --- | --- |
| [对话田渊栋：AI 自进化如何到来【晚点聊 LateTalk】](https://www.bilibili.com/video/BV1XnuH66EzS/) | 田渊栋 | [晚点聊 LateTalk](./shows/latetalk/) | 2026-08-07 | [总结](./shows/latetalk/episodes/178-tian-yuandong/summary.zh-CN.md) | [逐字稿](./shows/latetalk/episodes/178-tian-yuandong/transcript.zh-CN.md) |
| [详解 Kimi K3：强到冲击 Anthropic 估值的模型什么样？【晚点聊LateTalk】](https://www.bilibili.com/video/BV1nWM26QEu5/) | 赵晨阳、曾致远 | [晚点聊 LateTalk](./shows/latetalk/) | 2026-08-06 | [总结](./shows/latetalk/episodes/177-zhao-chenyang-zeng-zhiyuan/summary.zh-CN.md) | [逐字稿](./shows/latetalk/episodes/177-zhao-chenyang-zeng-zhiyuan/transcript.zh-CN.md) |
| [对话盛颖：xAI，Infra的浪漫，SGLang，开源，平权与“甄嬛传”](https://www.bilibili.com/video/BV1GaM968E6T/) | 盛颖 | [硅谷101](./shows/sv101/) | 2026-08-05 | [总结](./shows/sv101/episodes/247-sheng-ying/summary.zh-CN.md) | [逐字稿](./shows/sv101/episodes/247-sheng-ying/transcript.zh-CN.md) |
| [姚顺雨，来到腾讯 300 天【晚点聊LateTalk】](https://www.bilibili.com/video/BV1DDGu6VEzo/) | 高洪浩 | [晚点聊 LateTalk](./shows/latetalk/) | 2026-08-01 | [总结](./shows/latetalk/episodes/176-gao-honghao/summary.zh-CN.md) | [逐字稿](./shows/latetalk/episodes/176-gao-honghao/transcript.zh-CN.md) |
| [对话 Liblib 陈冕：关于活下来，以及所有接近死亡的时刻【晚点聊LateTalk】](https://www.bilibili.com/video/BV1ZP3863E3E/) | 陈冕 | [晚点聊 LateTalk](./shows/latetalk/) | 2026-07-30 | [总结](./shows/latetalk/episodes/175-chen-mian/summary.zh-CN.md) | [逐字稿](./shows/latetalk/episodes/175-chen-mian/transcript.zh-CN.md) |
| [AI 冲击企业软件巨头？与SAP原欣聊大模型 to B 的颠覆与边界【晚点聊LateTalk】](https://www.bilibili.com/video/BV1zQ3i6YErP/) | 原欣 | [晚点聊 LateTalk](./shows/latetalk/) | 2026-07-28 | [总结](./shows/latetalk/episodes/174-yuan-xin/summary.zh-CN.md) | [逐字稿](./shows/latetalk/episodes/174-yuan-xin/transcript.zh-CN.md) |
| [具身季报 26Q2：世界模型大风不停，和不想被贴标签的人【晚点聊LateTalk】](https://www.bilibili.com/video/BV1Eb3Y6QEMs/) | 陈哲 | [晚点聊 LateTalk](./shows/latetalk/) | 2026-07-28 | [总结](./shows/latetalk/episodes/170-chen-zhe/summary.zh-CN.md) | [逐字稿](./shows/latetalk/episodes/170-chen-zhe/transcript.zh-CN.md) |
| [对话叶奇意：“寻找”月之暗面杨植麟、中国两代AI、十年人才迁徙，与AGI信仰](https://www.bilibili.com/video/BV1wK3i6NEdQ/) | 叶奇意 | [硅谷101](./shows/sv101/) | 2026-07-28 | [总结](./shows/sv101/episodes/bili-bv1wk3i6nedq-ye-qiyi/summary.zh-CN.md) | [逐字稿](./shows/sv101/episodes/bili-bv1wk3i6nedq-ye-qiyi/transcript.zh-CN.md) |
| [游凯超：开源 Infra、模型 Co-design 与 vLLM](https://www.bilibili.com/video/BV18Qg96YE1W/) | 游凯超 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-07-28 | [总结](./shows/zhangxiaojun/episodes/148-you-kaichao/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/148-you-kaichao/transcript.zh-CN.md) |
| [特别访谈：廖恒、昇腾史与全球芯片产业](https://www.bilibili.com/video/BV1nB3u6tERu/) | 廖恒 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-07-25 | [总结](./shows/zhangxiaojun/episodes/bili-bv1nb3u6teru-liao-heng/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/bili-bv1nb3u6teru-liao-heng/transcript.zh-CN.md) |
| [Momenta IPO 后再访曹旭东：就是想做没有尽头的 AI【晚点聊LateTalk】](https://www.bilibili.com/video/BV1ASga6xEeZ/) | 曹旭东 | [晚点聊 LateTalk](./shows/latetalk/) | 2026-07-24 | [总结](./shows/latetalk/episodes/172-cao-xudong/summary.zh-CN.md) | [逐字稿](./shows/latetalk/episodes/172-cao-xudong/transcript.zh-CN.md) |
| [对话深庭纪王弢：人形之外，具身还有另一种答案【晚点LatePost】](https://www.bilibili.com/video/BV1GsgD6sEnU/) | 王弢 | [晚点聊 LateTalk](./shows/latetalk/) | 2026-07-23 | [总结](./shows/latetalk/episodes/bili-bv1gsgd6senu-wang-tao/summary.zh-CN.md) | [逐字稿](./shows/latetalk/episodes/bili-bv1gsgd6senu-wang-tao/transcript.zh-CN.md) |
| [26 岁 3 亿美元卖公司“开心只有两分钟”，不想 boring 就继续 suffering【晚点聊 LateTalk】](https://www.bilibili.com/video/BV1tYgz6JEvm/) | 姚颂 | [晚点聊 LateTalk](./shows/latetalk/) | 2026-07-22 | [总结](./shows/latetalk/episodes/173-yao-song/summary.zh-CN.md) | [逐字稿](./shows/latetalk/episodes/173-yao-song/transcript.zh-CN.md) |
| [AI 季报 26Q2：从 coding 到 RSI，强者愈强的未来？【晚点聊LateTalk】](https://www.bilibili.com/video/BV1Mhgz6QEHA/) | Henry Yin | [晚点聊 LateTalk](./shows/latetalk/) | 2026-07-22 | [总结](./shows/latetalk/episodes/171-henry-yin/summary.zh-CN.md) | [逐字稿](./shows/latetalk/episodes/171-henry-yin/transcript.zh-CN.md) |
| [Vincent Koc - OpenClaw 的反思、架构与 Agent 未来](https://www.bilibili.com/video/BV1pNKU6dE3V/) | Vincent Koc | [硅谷101](./shows/sv101/) | 2026-07-20 | [总结](./shows/sv101/episodes/bili-bv1pnku6de3v-vincent-koc/summary.zh-CN.md) | [英文逐字稿](./shows/sv101/episodes/bili-bv1pnku6de3v-vincent-koc/transcript.en.md) · [中文机器翻译](./shows/sv101/episodes/bili-bv1pnku6de3v-vincent-koc/transcript.zh-CN.md) |
| [世界模型这半年：路线争议、数据来源与商业落地【晚点LatePost】](https://www.bilibili.com/video/BV1Z9KA6sE9Q/) | 王广润、蒲韬、仲黎若 | [晚点聊 LateTalk](./shows/latetalk/) | 2026-07-18 | [总结](./shows/latetalk/episodes/bili-bv1z9ka6se9q-wang-guangrun-pu-tao-zhong-liruo/summary.zh-CN.md) | [逐字稿](./shows/latetalk/episodes/bili-bv1z9ka6se9q-wang-guangrun-pu-tao-zhong-liruo/transcript.zh-CN.md) |
| [柯丽一鸣：Pi 与通用机器人](https://www.bilibili.com/video/BV12bNB6vEtt/) | 柯丽一鸣 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-07-16 | [总结](./shows/zhangxiaojun/episodes/146-ke-liyiming/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/146-ke-liyiming/transcript.zh-CN.md) |
| [AI 硬件大爆发，谁能抢占下一个“iPhone 时刻”【晚点LatePost】](https://www.bilibili.com/video/BV1bVNn6XERr/) | 李宏伟 | [晚点聊 LateTalk](./shows/latetalk/) | 2026-07-10 | [总结](./shows/latetalk/episodes/bili-bv1bvnn6xerr-li-hongwei/summary.zh-CN.md) | [逐字稿](./shows/latetalk/episodes/bili-bv1bvnn6xerr-li-hongwei/transcript.zh-CN.md) |
| [Nathan Lambert - 中国 AI 生态、开源模型与算力焦虑](https://www.bilibili.com/video/BV1HXTs6bEzH/) | Nathan Lambert | [硅谷101](./shows/sv101/) | 2026-07-03 | [总结](./shows/sv101/episodes/bili-bv1hxts6bezh-nathan-lambert/summary.zh-CN.md) | [英文逐字稿](./shows/sv101/episodes/bili-bv1hxts6bezh-nathan-lambert/transcript.en.md) · [中文机器翻译](./shows/sv101/episodes/bili-bv1hxts6bezh-nathan-lambert/transcript.zh-CN.md) |
| [对话王熙乔：AI时代的教育者、十年沉浮，与人类文明的下一步](https://www.bilibili.com/video/BV1Ed7n6TEr1/) | 王熙乔 | [硅谷101](./shows/sv101/) | 2026-06-27 | [总结](./shows/sv101/episodes/bili-bv1ed7n6ter1-wang-xiqiao/summary.zh-CN.md) | [逐字稿](./shows/sv101/episodes/bili-bv1ed7n6ter1-wang-xiqiao/transcript.zh-CN.md) |
| [洪力德：SpaceX 开发史](https://www.bilibili.com/video/BV1HfEy6jEUx/) | 洪力德 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-06-12 | [总结](./shows/zhangxiaojun/episodes/145-hong-lide/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/145-hong-lide/transcript.zh-CN.md) |
| [再访田渊栋：46.5亿美金估值的RSI，与AI自进化](https://www.bilibili.com/video/BV1DY7C6nEWM/) | 田渊栋 | [硅谷101](./shows/sv101/) | 2026-06-05 | [总结](./shows/sv101/episodes/bili-bv1dy7c6newm-tian-yuandong/summary.zh-CN.md) | [逐字稿](./shows/sv101/episodes/bili-bv1dy7c6newm-tian-yuandong/transcript.zh-CN.md) |
| [“谷歌太慢了”：与Andrew Dai聊Gemini的翻身之战，出走与视觉理解模型](https://www.bilibili.com/video/BV1JCLw61E2d/) | Andrew Dai | [硅谷101](./shows/sv101/) | 2026-05-19 | [总结](./shows/sv101/episodes/bili-bv1jclw61e2d-andrew-dai/summary.zh-CN.md) | [逐字稿](./shows/sv101/episodes/bili-bv1jclw61e2d-andrew-dai/transcript.zh-CN.md) |
| [李想 - AI、具身智能与 L9 Livis](https://www.bilibili.com/video/BV1LD5T6pEp4/) | 李想 | [罗永浩的十字路口](./shows/luoyonghao/) | 2026-05-13 | [总结](./shows/luoyonghao/episodes/027-li-xiang/summary.zh-CN.md) | [逐字稿](./shows/luoyonghao/episodes/027-li-xiang/transcript.zh-CN.md) |
| [姚顺宇：模型训练与技术预测](https://www.bilibili.com/video/BV1YR5E6EE9o/) | 姚顺宇 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-05-11 | [总结](./shows/zhangxiaojun/episodes/140-yao-shunyu/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/140-yao-shunyu/transcript.zh-CN.md) |
| [徐丹飞 - 人类数据、行为克隆与机器人学习](https://www.bilibili.com/video/BV1usRgBEESe/) | 徐丹飞 | [WhynotTV](./shows/whynottv/) | 2026-05-01 | [总结](./shows/whynottv/episodes/005-xu-danfei/summary.zh-CN.md) | [逐字稿](./shows/whynottv/episodes/005-xu-danfei/transcript.zh-CN.md) |
| [对罗福莉3.5小时访谈：AI 范式已然巨变](https://www.bilibili.com/video/BV1iVoVBgERD/) | 罗福莉 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-04-24 | [总结](./shows/zhangxiaojun/episodes/138-luo-fuli/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/138-luo-fuli/transcript.zh-CN.md) |
| [携程梁建章 × 罗永浩：企业家与学者之间的“往返票”](https://www.bilibili.com/video/BV1TTdBBtErj/) | 梁建章 | [罗永浩的十字路口](./shows/luoyonghao/) | 2026-04-17 | [总结](./shows/luoyonghao/episodes/025-liang-jianzhang/summary.zh-CN.md) | [逐字稿](./shows/luoyonghao/episodes/025-liang-jianzhang/transcript.zh-CN.md) |
| [对谢赛宁的7小时马拉松访谈：世界模型、逃出硅谷与 AMI Labs](https://www.bilibili.com/video/BV1tew5zVEDf/) | 谢赛宁 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-03-16 | [总结](./shows/zhangxiaojun/episodes/133-xie-saining/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/133-xie-saining/transcript.zh-CN.md) |
| [印奇出任阶跃星辰董事长的访谈：聪明人的诱惑、取舍与超长链路淘汰赛](https://www.bilibili.com/video/BV1ZczaBJE58/) | 印奇 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-01-26 | [总结](./shows/zhangxiaojun/episodes/131-yin-qi/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/131-yin-qi/transcript.zh-CN.md) |
| [翁家翌：OpenAI、强化学习、Infra 与后训练](https://www.bilibili.com/video/BV1darmBcE4A/) | 翁家翌 | [WhynotTV](./shows/whynottv/) | 2026-01-17 | [总结](./shows/whynottv/episodes/004-weng-jiayi/summary.zh-CN.md) | [逐字稿](./shows/whynottv/episodes/004-weng-jiayi/transcript.zh-CN.md) |
| [全球大模型第一股的上市访谈，和智谱 CEO 张鹏聊：敢问路在何方？](https://www.bilibili.com/video/BV1awiDBDEWS/) | 张鹏 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2026-01-08 | [总结](./shows/zhangxiaojun/episodes/129-zhang-peng/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/129-zhang-peng/transcript.zh-CN.md) |
| [Manus 决定出售前最后的访谈：啊，这奇幻的 2025 年漂流啊…](https://www.bilibili.com/video/BV1knvYBDEjs/) | 季逸超 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2025-12-30 | [总结](./shows/zhangxiaojun/episodes/128-ji-yichao/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/128-ji-yichao/transcript.zh-CN.md) |
| [MiniMax 创始人闫俊杰 × 罗永浩：大山并非无法翻越](https://www.bilibili.com/video/BV11NmtBzE36/) | 闫俊杰 | [罗永浩的十字路口](./shows/luoyonghao/) | 2025-12-10 | [总结](./shows/luoyonghao/episodes/013-yan-junjie/summary.zh-CN.md) | [逐字稿](./shows/luoyonghao/episodes/013-yan-junjie/transcript.zh-CN.md) |
| [朱啸虎现实主义故事的第三次连载：人工智能的盛筵与泡泡](https://www.bilibili.com/video/BV13AmpBiE2o/) | 朱啸虎 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2025-12-09 | [总结](./shows/zhangxiaojun/episodes/122-zhu-xiaohu/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/122-zhu-xiaohu/transcript.zh-CN.md) |
| [语音智能体商业落地的教训、经验与实践](https://www.bilibili.com/video/BV1dZsCzfEMV/) | 李沐 | [硅谷101](./shows/sv101/) | 2025-10-27 | [总结](./shows/sv101/episodes/bili-bv1dzsczfemv-li-mu/summary.zh-CN.md) | [英文逐字稿](./shows/sv101/episodes/bili-bv1dzsczfemv-li-mu/transcript.en.md) · [中文机器翻译](./shows/sv101/episodes/bili-bv1dzsczfemv-li-mu/transcript.zh-CN.md) |
| [潘天鸿 - 影视飓风、影像冒险与创业](https://www.bilibili.com/video/BV1B5xkzPEhx/) | 潘天鸿 | [罗永浩的十字路口](./shows/luoyonghao/) | 2025-10-10 | [总结](./shows/luoyonghao/episodes/006-pan-tianhong/summary.zh-CN.md) | [逐字稿](./shows/luoyonghao/episodes/006-pan-tianhong/transcript.zh-CN.md) |
| [周鸿祎 - AI 革命、企业转型与未来](https://www.bilibili.com/video/BV1hNJ1zLEb8/) | 周鸿祎 | [罗永浩的十字路口](./shows/luoyonghao/) | 2025-09-24 | [总结](./shows/luoyonghao/episodes/005-zhou-hongyi/summary.zh-CN.md) | [逐字稿](./shows/luoyonghao/episodes/005-zhou-hongyi/transcript.zh-CN.md) |
| [陈天奇 - XGBoost、TVM 与机器学习系统](https://www.bilibili.com/video/BV1s6pgzLE3y/) | 陈天奇 | [WhynotTV](./shows/whynottv/) | 2025-09-12 | [总结](./shows/whynottv/episodes/003-chen-tianqi/summary.zh-CN.md) | [逐字稿](./shows/whynottv/episodes/003-chen-tianqi/transcript.zh-CN.md) |
| [和杨植麟时隔1年的对话：K2、Agentic LLM、缸中之脑和“站在无限的开端”](https://www.bilibili.com/video/BV1hFe1zSEXp/) | 杨植麟 | [张小珺商业访谈录](./shows/zhangxiaojun/) | 2025-08-27 | [总结](./shows/zhangxiaojun/episodes/113-yang-zhilin/summary.zh-CN.md) | [逐字稿](./shows/zhangxiaojun/episodes/113-yang-zhilin/transcript.zh-CN.md) |
| [何小鹏 - 从 UC 到造车、芯片与飞行汽车](https://www.bilibili.com/video/BV1jTedzREds/) | 何小鹏 | [罗永浩的十字路口](./shows/luoyonghao/) | 2025-08-26 | [总结](./shows/luoyonghao/episodes/002-he-xiaopeng/summary.zh-CN.md) | [逐字稿](./shows/luoyonghao/episodes/002-he-xiaopeng/transcript.zh-CN.md) |
| [胡渊鸣 - Meshy AI、太极与图形学创业](https://www.bilibili.com/video/BV1XmtyzKEzQ/) | 胡渊鸣 | [WhynotTV](./shows/whynottv/) | 2025-08-08 | [总结](./shows/whynottv/episodes/002-hu-yuanming/summary.zh-CN.md) | [逐字稿](./shows/whynottv/episodes/002-hu-yuanming/transcript.zh-CN.md) |
| [杨硕 - 妙动科技、Optimus 与人形机器人](https://www.bilibili.com/video/BV1em3XznEFx/) | 杨硕 | [WhynotTV](./shows/whynottv/) | 2025-07-05 | [总结](./shows/whynottv/episodes/001-yang-shuo/summary.zh-CN.md) | [逐字稿](./shows/whynottv/episodes/001-yang-shuo/transcript.zh-CN.md) |

内容格式和审核状态见[内容标准](./docs/content-standard.md)，Python 工具和处理命令见[脚本用法](./docs/python-scripts.md)。项目脚本使用 [Apache License 2.0](./LICENSE)；该许可证不自动改变所链接或引用的第三方节目内容的权利状态。
