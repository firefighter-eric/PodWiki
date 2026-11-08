---
schema_version: 1
kind: show
id: yiqitietalk
title: 一起铁TALK
aliases:
  - 一起铁talk
language: zh-CN
status: active
formats:
  - running-podcast
  - conversation
topics:
  - 跑步
  - 训练
  - 生活
sources:
  - platform: xiaoyuzhou
    kind: podcast
    external_id: 6951e312febad13106eb017e
    url: https://www.xiaoyuzhoufm.com/podcast/6951e312febad13106eb017e
    preferred: true
last_verified_at: 2026-11-08
---

# 一起铁TALK

一档面向在生活中持续“狂奔”的人的对谈节目，以跑步为入口，聊训练、生活经验和真实处境，为听众提供一个可以原地休息的角落。

## 本次更新核对（2026-11-08）

- 增量窗口：北京时间 `2026-05-22T11:59:31.882+08:00` 至 `2026-11-08T22:45:14.002517+08:00`；匿名访问，扫描结果为 `complete`。
- 官方栏目页按发布时间倒序返回 24 集中的前 15 集，整批读至 2026-03-21，已越过窗口起点。窗口内 11 集全部完成分类：8 集已收录、3 集 `eligible-new`，无排除项或身份待判项；这不表示已扫描全部历史。
- 当前正式索引仍为 **21** 集，本次新增可发布单集 **0** 集。下列 3 集已冻结为精确候选；没有新增正式单集目录或索引行。表中保留发布者原标题，不据此建立正式期号。

| 发布日期（北京时间） | 发布者原标题与规范来源 | 处理状态 |
| --- | --- | --- |
| 2026-11-05 | [24 李大林：被说“捡漏”后北马再夺冠。扬眉吐气的李大林与晓霞，背后经历了什么？](https://www.xiaoyuzhoufm.com/episode/6aeca1ea5b7c4709bfe1b7bf) | ASR 原始检查点已保存；01:58:00 对齐唯一性门禁失败 |
| 2026-10-21 | [23 梁田田：穿牛仔裤跑 800 米的女孩，如今成长为全国冠军，赛场之外和场上有何不同？](https://www.xiaoyuzhoufm.com/episode/6ad89de4ef67611cac7a05ee) | 音频已核验；因前一集长音频资格失败而中止 |
| 2026-10-13 | [22 吴向东：2:07:55 PB背后，一起“搞个大的”](https://www.xiaoyuzhoufm.com/episode/6ace0097e742e36efcc2599d) | 音频已核验；因长音频资格失败而未启动正式 ASR |

三集公开页面均绑定本栏目 PID，明确为 `NORMAL`、`FREE`、非私密和 `PUBLIC`，完整简介、章节与 M4A 身份可核对。
单集页面的 `isTranscriptEnabled: true` 是功能开关，`transcript` 只提供与音频一致的 `mediaId` 占位，没有显式公开正文、segment 或字幕 URL。
首次 metadata-only intake 因未知布尔字段失败关闭；本次修复采集器后，严格校验并保留该原值，继续独立发现真实字幕载荷，未屏蔽任何已发现的字幕。
三集重新 intake 均通过，当前匿名上下文的公开字幕 tracks 为空；音频已按冻结顺序串行获取，并完成字节数、ffprobe、时长与 SHA-256 核验，媒体与 sidecar 只保留在 Git 忽略的 `.cache/`。

本次按用户明确授权，以 Linux / RTX 5090 实测替代指定 RTX A2000 的资格门禁；使用固定 revision 的 Qwen3-ASR 1.7B 与 ForcedAligner，以及 PyTorch 2.13.0/CUDA 13.0、Transformers 5.14.1、NumPy 2.4.6 独立环境。模型关键文件哈希、成对英文金标准与 245 秒中文跨块样本均通过核验，这不代表 A2000 已验证。

首个完整单集在 `7080.000s` 的重叠边界出现一条 41 字匹配链与两条“怎么样”紧密短链冲突，无法证明唯一单调映射。原有门禁正确失败关闭；只保留 `pending` raw，没有完整 aligned、refined、正式 Markdown 或全文总结。
按用户“验证失败就停止”的条件，已停止本任务后续 GPU 处理：第二集刚启动后被中止，第三集没有启动。不放宽边界门禁，也不把短样本成功或未完成的 raw 当作完整稿。

恢复需先在新的明确指示下解决该边界歧义并重新通过长音频资格门禁；`pending` raw 不能作为下游输入，也不能伪造为可直接 align-only 续跑的完整检查点。后续仍需完整逐字稿、全文总结及逐集核听、说话人和专名校对、高影响事实核查；本次没有新内容被标为 `machine`、`draft` 或 `reviewed`。

扫描证据、inventory 和通过校验的 `scan.json` 在被 Git 忽略的 `.cache/scans/20261108T143900Z-three-shows/yiqitietalk/` 及其父目录；
冻结清单位于 `.cache/intake/yiqitietalk/manifest.json`，绑定来源 scan 的 SHA-256，范围仅为上表 3 个 eid。
媒体在 `.cache/media/yiqitietalk/`；原始检查点与处理中元数据保存在 `.cache/pending-episodes/yiqitietalk/`，文件哈希清单为 `.cache/pipeline/pending-episode-artifacts.json`。所有失败与中止证据均留在忽略目录，没有把不完整单集提交为已收录内容。

## 单集

| 标题 | 播客名称 | 日期 | 总结链接 | 逐字稿链接 |
| --- | --- | --- | --- | --- |
| [郑小倩：首马 229，竟怀疑自己，场地冠军到到浙江纪录](https://www.xiaoyuzhoufm.com/episode/6a8675c1ef65145dfcc264f8) | 一起铁TALK | 2026-08-20 | [总结](./episodes/21-zheng-xiaoqian/summary.zh-CN.md) | [逐字稿](./episodes/21-zheng-xiaoqian/transcript.zh-CN.md) |
| [姚妙“教”吴向东越野？不不不，让我们一起撒开脚丫](https://www.xiaoyuzhoufm.com/episode/6a5f4d33a3fec224d5a1136a) | 一起铁TALK | 2026-07-21 | [总结](./episodes/20-yao-miao/summary.zh-CN.md) | [逐字稿](./episodes/20-yao-miao/transcript.zh-CN.md) |
| [此沙与吴向东的首次越野赛](https://www.xiaoyuzhoufm.com/episode/6a5cd2586356eb2d9be50430) | 一起铁TALK | 2026-07-20 | [总结](./episodes/19-ci-sha/summary.zh-CN.md) | [逐字稿](./episodes/19-ci-sha/transcript.zh-CN.md) |
| [吴健：运动员与迈胜创始人](https://www.xiaoyuzhoufm.com/episode/6a58b864016dcc7e05433391) | 一起铁TALK | 2026-07-16 | [总结](./episodes/18-wu-jian/summary.zh-CN.md) | [逐字稿](./episodes/18-wu-jian/transcript.zh-CN.md) |
| [徐冰洁：给你带来的荣耀和光环，就得忍受它的枯燥](https://www.xiaoyuzhoufm.com/episode/6a47910b3fb7233cbf433c35) | 一起铁TALK | 2026-07-03 | [总结](./episodes/17-xu-bingjie/summary.zh-CN.md) | [逐字稿](./episodes/17-xu-bingjie/transcript.zh-CN.md) |
| [许乐：我还要干票大的！](https://www.xiaoyuzhoufm.com/episode/6a3a595e2e335a35a808142c) | 一起铁TALK | 2026-06-23 | [总结](./episodes/16-xu-le/summary.zh-CN.md) | [逐字稿](./episodes/16-xu-le/transcript.zh-CN.md) |
| [吴冰：我要参加亚运会马拉松比赛啦！](https://www.xiaoyuzhoufm.com/episode/6a3257ae4233e62bc54b5ec4) | 一起铁TALK | 2026-06-17 | [总结](./episodes/15-wu-bing/summary.zh-CN.md) | [逐字稿](./episodes/15-wu-bing/transcript.zh-CN.md) |
| [李美珍：我是你们的马拉松运动员李美珍](https://www.xiaoyuzhoufm.com/episode/6a25611c7444b5722234d445) | 一起铁TALK | 2026-06-07 | [总结](./episodes/14-li-meizhen/summary.zh-CN.md) | [逐字稿](./episodes/14-li-meizhen/transcript.zh-CN.md) |
| [杨春龙：我的过去与我的未来](https://www.xiaoyuzhoufm.com/episode/69eda0281e94ae69212b1c74) | 一起铁TALK | 2026-04-26 | [总结](./episodes/13-yang-chunlong/summary.zh-CN.md) | [逐字稿](./episodes/13-yang-chunlong/transcript.zh-CN.md) |
| [何杰：亚运会、全运会马拉松男子冠军，两次男子马拉松国家纪录创造者](https://www.xiaoyuzhoufm.com/episode/69d4aacee2c8be3155905460) | 一起铁TALK | 2026-04-07 | [总结](./episodes/12-he-jie/summary.zh-CN.md) | [逐字稿](./episodes/12-he-jie/transcript.zh-CN.md) |
| [申加升、巴斯（李鹏程）：F4初出道，顶级耐力运动员的大聊天](https://www.xiaoyuzhoufm.com/episode/69c9b88eb977fb2c4790ec42) | 一起铁TALK | 2026-03-30 | [总结](./episodes/11-shen-jiasheng-li-pengcheng/summary.zh-CN.md) | [逐字稿](./episodes/11-shen-jiasheng-li-pengcheng/transcript.zh-CN.md) |
| [张唯雅：三个跑步的人，坐在家里瞎聊](https://www.xiaoyuzhoufm.com/episode/69be8dc42d318777c90884be) | 一起铁TALK | 2026-03-21 | [总结](./episodes/10-zhang-weiya/summary.zh-CN.md) | [逐字稿](./episodes/10-zhang-weiya/transcript.zh-CN.md) |
| [路颖：中国女子路跑运动员](https://www.xiaoyuzhoufm.com/episode/69b51ccdcaaea1fb3b32ba7c) | 一起铁TALK | 2026-03-14 | [总结](./episodes/9-lu-ying/summary.zh-CN.md) | [逐字稿](./episodes/9-lu-ying/transcript.zh-CN.md) |
| [大阪之夜， 王颖（吴向东经纪人）、吴向东与孙瑞一 聊天局](https://www.xiaoyuzhoufm.com/episode/69a5692ea22480add6aeca35) | 一起铁TALK | 2026-03-02 | [总结](./episodes/8-wang-ying/summary.zh-CN.md) | [逐字稿](./episodes/8-wang-ying/transcript.zh-CN.md) |
| [李芷萱：我的PB 奥运 全运 和结婚](https://www.xiaoyuzhoufm.com/episode/69992553a22480add6994d83) | 一起铁TALK | 2026-02-21 | [总结](./episodes/7-li-zhixuan/summary.zh-CN.md) | [逐字稿](./episodes/7-li-zhixuan/transcript.zh-CN.md) |
| [管油胜：这十年我都没有认真做过运动员](https://www.xiaoyuzhoufm.com/episode/6987349566e2c303774c39fc) | 一起铁TALK | 2026-02-07 | [总结](./episodes/6-guan-yousheng/summary.zh-CN.md) | [逐字稿](./episodes/6-guan-yousheng/transcript.zh-CN.md) |
| [姚妙：在奔跑中寻找](https://www.xiaoyuzhoufm.com/episode/697df6e62fc7f49d0925c9e4) | 一起铁TALK | 2026-01-31 | [总结](./episodes/5-yao-miao/summary.zh-CN.md) | [逐字稿](./episodes/5-yao-miao/transcript.zh-CN.md) |
| [贾俄仁加：运动员、贾老板、父亲，多重身份加身，仍要奋力一搏](https://www.xiaoyuzhoufm.com/episode/6975d6bfef1cf272a75432b6) | 一起铁TALK | 2026-01-25 | [总结](./episodes/4-jia-e-ren-jia/summary.zh-CN.md) | [逐字稿](./episodes/4-jia-e-ren-jia/transcript.zh-CN.md) |
| [张德顺：山里跑出来的天才女子正在向下一座山进发](https://www.xiaoyuzhoufm.com/episode/696b98a8109824f9e1050609) | 一起铁TALK | 2026-01-17 | [总结](./episodes/3-zhang-deshun/summary.zh-CN.md) | [逐字稿](./episodes/3-zhang-deshun/transcript.zh-CN.md) |
| [李健 铁蛋：职业运动员就是要做自己认为对的事情](https://www.xiaoyuzhoufm.com/episode/69624948f8b05f9f75d72c22) | 一起铁TALK | 2026-01-10 | [总结](./episodes/2-li-jian/summary.zh-CN.md) | [逐字稿](./episodes/2-li-jian/transcript.zh-CN.md) |
| [在赛场狂奔，在播客走心，一起铁Talk](https://www.xiaoyuzhoufm.com/episode/6952860114db1df9ef5c3a88) | 一起铁TALK | 2025-12-29 | [总结](./episodes/1-sun-ruiyi-wu-xiangdong/summary.zh-CN.md) | [逐字稿](./episodes/1-sun-ruiyi-wu-xiangdong/transcript.zh-CN.md) |
