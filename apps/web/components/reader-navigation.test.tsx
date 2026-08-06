import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import { MobileReaderTools } from "@/components/mobile-reader-tools";
import { ReaderPreferences } from "@/components/reader-preferences";
import { RightRail } from "@/components/right-rail";
import { getEpisode } from "@/lib/content";
import { getEpisodeDescription } from "@/lib/episode-label";

function renderWithPreferences(element: React.ReactNode) {
  return renderToStaticMarkup(createElement(ReaderPreferences, null, element));
}

describe("reader navigation", () => {
  it("shows the chapter menu only for the transcript view", async () => {
    const episode = await getEpisode("sv101", "247-sheng-ying");
    expect(episode).toBeDefined();

    const summaryHtml = renderWithPreferences(createElement(MobileReaderTools, {
      chapters: episode!.chapters,
      showChapters: false,
    }));
    const transcriptHtml = renderWithPreferences(createElement(MobileReaderTools, {
      chapters: episode!.chapters,
      showChapters: true,
    }));

    expect(summaryHtml).not.toContain("章节目录");
    expect(summaryHtml).toContain("阅读设置");
    expect(transcriptHtml).toContain('class="mobile-chapter-tool"');
    expect(transcriptHtml).toContain("章节目录");
    expect(transcriptHtml).toContain("?view=transcript#t-00-00-00");
  });

  it("does not render the redundant chapter link in the right rail", async () => {
    const episode = await getEpisode("sv101", "247-sheng-ying");
    expect(episode).toBeDefined();

    for (const view of ["summary", "transcript"] as const) {
      const html = renderWithPreferences(createElement(RightRail, { episode: episode!, view }));
      expect(html).not.toContain('href="#chapter-list"');
      expect(html).not.toContain("关键信息仍需人工核查");
      expect(html).not.toContain("总结基于归档 Whisper 稿");
    }
  });

  it("uses a human-readable label instead of an internal episode key", async () => {
    const episode = await getEpisode("sv101", "bili-bv1dzsczfemv-li-mu");
    expect(episode).toBeDefined();

    const html = renderWithPreferences(createElement(RightRail, {
      episode: episode!,
      view: "summary",
    }));

    expect(html).toContain("特别访谈 · 2025-10-27");
    expect(html).not.toContain("bili-bv1dzsczfemv");

    const episodeWithoutSubtitle = await getEpisode(
      "sv101",
      "bili-bv1pnku6de3v-vincent-koc",
    );
    expect(episodeWithoutSubtitle).toBeDefined();

    const description = getEpisodeDescription(episodeWithoutSubtitle!);
    expect(description).toBe("硅谷101特别访谈播客总结与逐字稿");
    expect(description).not.toContain("bili-bv1pnku6de3v");
  });
});
