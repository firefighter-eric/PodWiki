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
last_verified_at: 2026-11-09
---

# 一起铁TALK

一档面向在生活中持续“狂奔”的人的对谈节目，以跑步为入口，聊训练、生活经验和真实处境，为听众提供一个可以原地休息的角落。

## 本次更新核对（2026-11-08）

- 增量窗口：北京时间 `2026-05-22T11:59:31.882+08:00` 至 `2026-11-08T22:45:14.002517+08:00`；匿名访问，扫描结果为 `complete`。
- 官方栏目页倒序返回 24 集中的前 15 集，整批读至 2026-03-21，已越过窗口起点。窗口内 11 集全部分类：8 集已收录、3 集 `eligible-new`；这不表示扫描了全部历史。
- 三个精确 eid 在添加前冻结，现已全部完成，本次新增 **3** 集，正式索引共 **24** 集。发布者原标题中的数字标签保留，不由标题单独推断正式期号。

| 发布日期（北京时间） | 新增完整单集 | 状态与人工待办 |
| --- | --- | --- |
| 2026-11-05 | [李大林、李晓霞](./episodes/xiaoyuzhou-6aeca1ea5b7c4709bfe1b7bf-li-dalin-li-xiaoxia/) | `transcript: machine`、`summary: draft`；待核听、说话人和专名校对，成绩、奖金及反兴奋剂相关说法核查 |
| 2026-10-21 | [梁田田](./episodes/xiaoyuzhou-6ad89de4ef67611cac7a05ee-liang-tiantian/) | `transcript: machine`、`summary: draft`；待核听、专名与赛事/纪录、睡眠及训练说法核查 |
| 2026-10-13 | [吴向东](./episodes/xiaoyuzhou-6ace0097e742e36efcc2599d-wu-xiangdong/) | `transcript: machine`、`summary: draft`；待核听，PB秒数、日期、治疗/HRV、产品名及赛事规则核查 |

三集匿名页面均绑定本栏目 PID，明确为 `NORMAL`、`FREE`、非私密、`PUBLIC` 的完整正片。
`isTranscriptEnabled: true` 及匹配音频的 mediaId 占位已严格校验并保留；当前上下文没有公开正文、segments 或字幕轨，不忽略实际字幕载荷。
公开 M4A 及 sidecar 均通过字节数、ffprobe、时长与 SHA-256 校验，媒体只存放于被 Git 忽略的 `.cache/`。

按本批明确授权，使用 Linux / RTX 5090 实测替代指定 A2000 资格门禁；ASR 与 ForcedAligner 均使用仓库固定 native revision，独立环境为 PyTorch 2.13.0/CUDA 13.0、Transformers 5.14.1、NumPy 2.4.6，不代表 A2000 已验证。
首集在 01:58:00 的快速重复词边界曾失败关闭；原 pending raw 和失败记录完整保留。修复新增完整相同窗口证明，保留原最近切点、全部重复词和候选，不降低时间差门限或改找切点；反例测试、英文金标准、中文跨块样本及三集完整链现已通过。

每集均串行生成 raw、aligned、refined 和 Markdown，根稿与 selected 运行稿字节一致，单集页列出真实模型 revision、哈希链与处理参数。
全文总结基于完整逐字稿逐段通读并核对全部引用时间码；均保持 `draft`，没有人工审核的内容不标为 `reviewed`。

扫描 inventory、证据与通过校验的 `scan.json` 位于 `.cache/scans/20261108T143900Z-three-shows/yiqitietalk/`；
冻结清单 `.cache/intake/yiqitietalk/manifest.json` 绑定来源 scan 哈希，范围始终为上述 3 个 eid。旧失败记录和 pending 文件仍在忽略缓存，未覆盖既有已收录单集。

## 单集

| 标题 | 播客名称 | 日期 | 总结链接 | 逐字稿链接 |
| --- | --- | --- | --- | --- |
| [24 李大林：被说“捡漏”后北马再夺冠。扬眉吐气的李大林与晓霞，背后经历了什么？](https://www.xiaoyuzhoufm.com/episode/6aeca1ea5b7c4709bfe1b7bf) | 一起铁TALK | 2026-11-05 | [总结](./episodes/xiaoyuzhou-6aeca1ea5b7c4709bfe1b7bf-li-dalin-li-xiaoxia/summary.zh-CN.md) | [逐字稿](./episodes/xiaoyuzhou-6aeca1ea5b7c4709bfe1b7bf-li-dalin-li-xiaoxia/transcript.zh-CN.md) |
| [23 梁田田：穿牛仔裤跑 800 米的女孩，如今成长为全国冠军，赛场之外和场上有何不同？](https://www.xiaoyuzhoufm.com/episode/6ad89de4ef67611cac7a05ee) | 一起铁TALK | 2026-10-21 | [总结](./episodes/xiaoyuzhou-6ad89de4ef67611cac7a05ee-liang-tiantian/summary.zh-CN.md) | [逐字稿](./episodes/xiaoyuzhou-6ad89de4ef67611cac7a05ee-liang-tiantian/transcript.zh-CN.md) |
| [22 吴向东：2:07:55 PB背后，一起“搞个大的”](https://www.xiaoyuzhoufm.com/episode/6ace0097e742e36efcc2599d) | 一起铁TALK | 2026-10-13 | [总结](./episodes/xiaoyuzhou-6ace0097e742e36efcc2599d-wu-xiangdong/summary.zh-CN.md) | [逐字稿](./episodes/xiaoyuzhou-6ace0097e742e36efcc2599d-wu-xiangdong/transcript.zh-CN.md) |
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
