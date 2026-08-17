import type { Metadata } from "next";
import { describe, expect, it, vi } from "vitest";
import { metadata as layoutMetadata } from "@/app/layout";
import { metadata as showsMetadata } from "@/app/shows/page";
import { generateMetadata as generateShowMetadata } from "@/app/shows/[showId]/page";
import { generateMetadata as generateEpisodeMetadata } from "@/app/shows/[showId]/episodes/[folder]/page";
import { generateMetadata as generateTranscriptMetadata } from "@/app/shows/[showId]/episodes/[folder]/transcript/page";
import robots from "@/app/robots";
import sitemap from "@/app/sitemap";
import { getEpisodeCards, getShows } from "@/lib/content";

vi.mock("next/font/local", () => ({
  default: () => ({ variable: "podwiki-local-font" }),
}));

const productionUrl = "https://podwiki.vercel.app";

function expectShareMetadata(metadata: Metadata, title: string, canonical: string) {
  expect(metadata.alternates?.canonical).toBe(canonical);
  expect(metadata.openGraph).toMatchObject({
    title,
    url: canonical,
    siteName: "PodWiki",
    locale: "zh_CN",
  });
  expect(metadata.openGraph).not.toHaveProperty("images");
  expect(metadata.twitter).toMatchObject({
    card: "summary",
    title,
  });
  expect(metadata.twitter).not.toHaveProperty("images");
}

describe("discovery metadata", () => {
  it("uses the production origin and canonical social metadata for the catalog", () => {
    expect(layoutMetadata.metadataBase).toEqual(new URL(productionUrl));
    expectShareMetadata(layoutMetadata, "PodWiki — 播客文字与总结", "/shows");
    expectShareMetadata(showsMetadata, "全部节目 · PodWiki", "/shows");
  });

  it("builds canonical social metadata for show, summary, and transcript pages", async () => {
    const showMetadata = await generateShowMetadata({
      params: Promise.resolve({ showId: "latetalk" }),
    });
    expectShareMetadata(showMetadata, "晚点聊 LateTalk · PodWiki", "/shows/latetalk");

    const params = Promise.resolve({ showId: "latetalk", folder: "178-tian-yuandong" });
    const episodeMetadata = await generateEpisodeMetadata({ params });
    expectShareMetadata(
      episodeMetadata,
      "田渊栋 · RSI 与 AI 自进化路径 · PodWiki",
      "/shows/latetalk/episodes/178-tian-yuandong",
    );
    expect(episodeMetadata.openGraph).toMatchObject({
      type: "article",
      publishedTime: "2026-08-07T09:00:00+08:00",
    });

    const transcriptMetadata = await generateTranscriptMetadata({ params });
    expectShareMetadata(
      transcriptMetadata,
      "田渊栋 · RSI 与 AI 自进化路径 · 逐字稿 · PodWiki",
      "/shows/latetalk/episodes/178-tian-yuandong/transcript",
    );
    expect(transcriptMetadata.openGraph).toMatchObject({
      type: "article",
      publishedTime: "2026-08-07T09:00:00+08:00",
    });
  });
});

describe("metadata routes", () => {
  it("lists the catalog, every show, and both views of every episode", async () => {
    const [entries, shows, episodes] = await Promise.all([
      sitemap(),
      getShows(),
      getEpisodeCards(),
    ]);
    const urls = new Set(entries.map((entry) => entry.url));
    const episodeSummaryEntries = entries.filter(
      (entry) => entry.url.includes("/episodes/") && !entry.url.endsWith("/transcript"),
    );
    const transcriptEntries = entries.filter((entry) => entry.url.endsWith("/transcript"));

    expect(shows.length).toBeGreaterThan(0);
    expect(episodes.length).toBeGreaterThan(0);
    expect(entries).toHaveLength(1 + shows.length + episodes.length * 2);
    expect(episodeSummaryEntries).toHaveLength(episodes.length);
    expect(transcriptEntries).toHaveLength(episodes.length);
    expect(urls).toContain(`${productionUrl}/shows`);

    for (const show of shows) {
      expect(urls).toContain(`${productionUrl}${show.href}`);
    }
    expect(entries.every((entry) => entry.lastModified === undefined)).toBe(true);
  });

  it("allows crawling and advertises the production sitemap", () => {
    expect(robots()).toEqual({
      rules: {
        userAgent: "*",
        allow: "/",
      },
      sitemap: `${productionUrl}/sitemap.xml`,
    });
  });
});
