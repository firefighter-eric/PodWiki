import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import {
  EpisodeHeroTitle,
  EpisodeSidebarTitle,
} from "@/components/episode-navigation-title";
import { MobileReaderTools } from "@/components/mobile-reader-tools";
import { ReaderPreferences } from "@/components/reader-preferences";
import { RightRail } from "@/components/right-rail";
import { getRecentEpisodeCommandItems } from "@/components/search-dialog";
import { ShowCatalog } from "@/components/show-catalog";
import { SummaryView } from "@/components/summary-view";
import { getEpisode, getEpisodes, getShows } from "@/lib/content";
import { getEpisodeDescription, getEpisodeLabel } from "@/lib/episode-label";

function renderWithPreferences(element: React.ReactNode) {
  return renderToStaticMarkup(createElement(ReaderPreferences, null, element));
}

describe("reader navigation", () => {
  it("uses the canonical person-topic title in the reader hero", async () => {
    const episode = await getEpisode("zhangxiaojun", "145-hong-lide");
    expect(episode).toBeDefined();

    const html = renderToStaticMarkup(createElement(EpisodeHeroTitle, {
      title: episode!.navigationTitle,
    }));

    expect(html).toBe(
      "<h1>洪力德</h1><p class=\"episode-subtitle\">SpaceX 开发史与工程组织</p>",
    );
    expect(html).not.toContain("口述 SpaceX 开发史");
    expect(episode!.title).toContain("口述SpaceX开发史");
  });

  it("renders sidebar episodes as name-date metadata above a one-line topic", () => {
    const html = renderToStaticMarkup(createElement(EpisodeSidebarTitle, {
      title: "游凯超 · vLLM、开源治理与模型—Infra 协同",
      publishedDate: "2026-07-28",
    }));

    expect(html).toContain('<strong class="episode-nav-name">游凯超</strong>');
    expect(html).toContain('<time dateTime="2026-07-28">2026-07-28</time>');
    expect(html).toContain(
      '<span class="episode-nav-topic" title="vLLM、开源治理与模型—Infra 协同">vLLM、开源治理与模型—Infra 协同</span>',
    );
  });

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

  it("does not invent a special-interview label for unnumbered regular episodes", async () => {
    const episode = await getEpisode("sv101", "bili-bv1wk3i6nedq-ye-qiyi");
    expect(episode).toBeDefined();
    expect(episode?.episodeNumber).toBeNull();
    expect(episode?.releaseType).toBe("regular");
    expect(getEpisodeLabel(episode!.episodeNumber, episode!.releaseType)).toBeNull();
    expect(getEpisodeDescription({
      showTitle: episode!.showTitle,
      episodeNumber: episode!.episodeNumber,
      releaseType: episode!.releaseType,
      subtitle: "",
    })).toBe("硅谷101播客总结与逐字稿");

    const html = renderWithPreferences(createElement(RightRail, {
      episode: episode!,
      view: "summary",
    }));
    expect(html).not.toContain("特别访谈");
    expect(html).toContain("2026-07-28");
    expect(getEpisodeLabel(null, "bonus")).toBe("加更");
    expect(getEpisodeLabel(null, "trailer")).toBe("预告");
  });

  it("uses person-topic titles without episode badges in discovery lists", async () => {
    const [shows, episodes] = await Promise.all([getShows(), getEpisodes()]);
    const selectedEpisodes = ["247-sheng-ying", "bili-bv1wk3i6nedq-ye-qiyi"].map((folder) => {
      const episode = episodes.find((candidate) => candidate.folder === folder);
      expect(episode).toBeDefined();
      return episode!;
    });

    const catalogHtml = renderToStaticMarkup(createElement(ShowCatalog, {
      shows,
      episodes: selectedEpisodes,
    }));
    expect(catalogHtml).toContain('<span class="episode-keyword">SGLang</span>');
    expect(catalogHtml).toContain('<span class="episode-keyword">Kimi</span>');
    expect(catalogHtml).toContain('class="catalog-tally" aria-label="2 期内容，来自 5 档播客"');
    expect(catalogHtml).not.toContain('class="show-grid"');
    expect(catalogHtml).toContain('<strong>盛颖</strong><span>SGLang、Infra 产品观与开源</span>');
    expect(catalogHtml).toContain('<strong>叶奇意</strong><span>AI 人才迁徙、Kimi 投资与 AGI</span>');
    expect(catalogHtml).not.toContain('class="episode-navigation-title"');
    expect(catalogHtml).not.toContain('class="episode-number"');
    expect(catalogHtml).not.toContain(">#247<");
    expect(catalogHtml).not.toContain(">特别<");
    expect(catalogHtml).not.toContain("01:46:26");
    expect(catalogHtml).not.toContain("01:10:24");

    const selectedShowHtml = renderToStaticMarkup(createElement(ShowCatalog, {
      shows,
      episodes: selectedEpisodes,
      selectedShow: shows.find((show) => show.id === "sv101"),
    }));
    expect(selectedShowHtml).toContain('<strong class="show-episode-person">盛颖</strong>');
    expect(selectedShowHtml).toContain('<span class="show-episode-title">SGLang、Infra 产品观与开源</span>');
    expect(selectedShowHtml).toContain('class="show-episode-intro"');
    expect(selectedShowHtml.indexOf('class="show-episode-title"')).toBeLessThan(
      selectedShowHtml.indexOf('class="show-episode-intro"'),
    );
    expect(selectedShowHtml).not.toContain('class="episode-keyword"');

    const recentItems = getRecentEpisodeCommandItems(selectedEpisodes);
    expect(recentItems.map((item) => item.title)).toEqual([
      "盛颖 · SGLang、Infra 产品观与开源",
      "叶奇意 · AI 人才迁徙、Kimi 投资与 AGI",
    ]);
    expect(recentItems.map((item) => item.snippet)).toEqual([
      "2026-08-05",
      "2026-07-28",
    ]);
    expect(recentItems.every((item) => !item.meta.includes("第 "))).toBe(true);
  });

  it("shows three recent episodes for each podcast on the homepage only", async () => {
    const [shows, episodes] = await Promise.all([getShows(), getEpisodes()]);
    const homeHtml = renderToStaticMarkup(createElement(ShowCatalog, { shows, episodes }));

    expect(homeHtml.match(/class="podcast-preview-card"/g)).toHaveLength(5);
    expect(homeHtml.match(/class="podcast-preview-episode"/g)).toHaveLength(15);
    expect(homeHtml).toContain("按播客浏览");
    expect(homeHtml.match(/查看全部 12 期/g)).toHaveLength(2);
    expect(homeHtml).toContain("查看全部 8 期");
    expect(homeHtml).toContain("查看全部 6 期");
    expect(homeHtml).toContain("查看全部 5 期");

    const showHtml = renderToStaticMarkup(createElement(ShowCatalog, {
      shows,
      episodes: episodes.filter((episode) => episode.showId === "sv101"),
      selectedShow: shows.find((show) => show.id === "sv101"),
    }));
    expect(showHtml).not.toContain("podcast-preview-card");
  });

  it("renders episode-authored core-point logic tables for every podcast", async () => {
    const episodes = await getEpisodes();
    const showIds = ["zhangxiaojun", "sv101", "latetalk", "luoyonghao", "whynottv"];

    for (const showId of showIds) {
      const episode = episodes.find((candidate) => candidate.showId === showId);
      expect(episode).toBeDefined();

      const html = renderToStaticMarkup(await SummaryView({ episode: episode! }));
      expect(html).toContain('<table class="core-points-table">');
      expect(html).toContain('<caption class="sr-only">本期核心观点逻辑表</caption>');
      expect(html).toContain('<th scope="col">');
      expect(html).toContain('data-label=');
      expect(html).not.toContain('<th scope="row">01</th>');
      expect(html).not.toContain('class="core-points-summary"><h2>核心观点</h2><ul>');
    }
  });
});
