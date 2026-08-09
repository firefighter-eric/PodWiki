import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import { TranscriptView } from "@/components/transcript-view";
import { decodeTranscriptAnchor } from "@/components/transcript-anchor-sync";
import { getEpisode } from "@/lib/content";

describe("TranscriptView", () => {
  it("ignores malformed URL fragments instead of crashing the reader", () => {
    expect(decodeTranscriptAnchor("#t-00-01-02")).toBe("t-00-01-02");
    expect(decodeTranscriptAnchor("#%E6%B5%8B%E8%AF%95")).toBe("测试");
    expect(decodeTranscriptAnchor("#%E0%A4%A")).toBeUndefined();
  });

  it("renders an English episode as a static bilingual transcript", async () => {
    const episode = await getEpisode("sv101", "bili-bv1dzsczfemv-li-mu");
    expect(episode).toBeDefined();

    const html = renderToStaticMarkup(createElement(TranscriptView, { episode: episode! }));
    expect(html).toContain("中英对照逐字稿");
    expect(html).toContain("机器翻译 · 未审核");
    expect(html).toContain("英文原稿由语音识别生成");
    expect(html).toContain('class="transcript-lines bilingual-transcript-lines"');
    expect(html).toContain('lang="en"');
    expect(html).toContain('lang="zh-CN"');
    expect(html).toMatch(/href="#t-[^"]+" tabindex="-1"/u);
    expect(html.indexOf("Yeah, today I&#x27;m gonna talk about voice agent."))
      .toBeLessThan(html.indexOf("好，今天我要谈谈语音智能体（Voice Agent）。"));
  });

  it("keeps a Chinese episode on the original transcript presentation", async () => {
    const episode = await getEpisode("sv101", "247-sheng-ying");
    expect(episode).toBeDefined();

    const html = renderToStaticMarkup(createElement(TranscriptView, { episode: episode! }));
    expect(html).toContain("完整逐字稿");
    expect(html).not.toContain("中英对照逐字稿");
    expect(html).not.toContain("当前文本由语音识别生成");
    expect(html).not.toContain('class="transcript-notice"');
    expect(html).not.toContain("bilingual-transcript-lines");
    expect(html).toMatch(/href="#t-[^"]+" tabindex="-1"/u);
  });
});
