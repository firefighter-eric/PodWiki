import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import { TranscriptView } from "@/components/transcript-view";
import { getEpisode } from "@/lib/content";

describe("TranscriptView", () => {
  it("renders an English episode as a static bilingual transcript", async () => {
    const episode = await getEpisode("sv101", "bili-bv1dzsczfemv-li-mu");
    expect(episode).toBeDefined();

    const html = renderToStaticMarkup(createElement(TranscriptView, { episode: episode! }));
    expect(html).toContain("中英对照逐字稿");
    expect(html).toContain("机器翻译 · 未审核");
    expect(html).toContain('class="transcript-lines bilingual-transcript-lines"');
    expect(html).toContain('lang="en"');
    expect(html).toContain('lang="zh-CN"');
    expect(html.indexOf("Yeah, today I&#x27;m gonna talk about voice agent."))
      .toBeLessThan(html.indexOf("好，今天我要谈谈语音智能体（Voice Agent）。"));
  });

  it("keeps a Chinese episode on the original transcript presentation", async () => {
    const episode = await getEpisode("sv101", "247-sheng-ying");
    expect(episode).toBeDefined();

    const html = renderToStaticMarkup(createElement(TranscriptView, { episode: episode! }));
    expect(html).toContain("完整逐字稿");
    expect(html).not.toContain("中英对照逐字稿");
    expect(html).not.toContain("bilingual-transcript-lines");
  });
});
