import { describe, expect, it } from "vitest";
import {
  getEpisode,
  getEpisodes,
  getShows,
  searchContent,
  timestampToId,
} from "@/lib/content";
import { getMarkdownSection } from "@/lib/markdown";

describe("PodWiki content loader", () => {
  it("loads every current show and episode from the repository", async () => {
    const shows = await getShows();
    const episodes = await getEpisodes();
    expect(shows.map((show) => show.id)).toEqual([
      "zhangxiaojun",
      "luoyonghao",
      "whynottv",
    ]);
    expect(episodes).toHaveLength(15);
    expect(episodes.every((episode) => episode.summaryRaw && episode.transcriptSegments.length > 0)).toBe(true);
  });

  it("keeps official nullable episode numbering intact", async () => {
    const episode = await getEpisode(
      "zhangxiaojun",
      "bili-bv1nb3u6teru-liao-heng",
    );
    expect(episode?.episodeNumber).toBeNull();
    expect(episode?.episodeKey).toBe("bili-bv1nb3u6teru");
  });

  it("returns summary and timestamped transcript search results", async () => {
    const results = await searchContent("第一性原理");
    expect(results.some((result) => result.section === "总结")).toBe(true);
    expect(results.some((result) => result.section === "逐字稿" && result.timestamp)).toBe(true);
  });

  it("creates stable timestamp anchors", () => {
    expect(timestampToId("01:37:13")).toBe("t-01-37-13");
  });

  it("maps every chapter to a real transcript anchor", async () => {
    const episodes = await getEpisodes();
    for (const episode of episodes) {
      const ids = new Set(episode.transcriptSegments.map((segment) => segment.id));
      expect(episode.chapters.length).toBeGreaterThan(1);
      for (const chapter of episode.chapters) {
        expect(ids.has(chapter.href.split("#")[1])).toBe(true);
      }
    }
    const target = await getEpisode("zhangxiaojun", "145-hong-lide");
    expect(target?.chapters.some((chapter) => chapter.timestamp === "02:51:16")).toBe(true);
  });

  it("extracts all reader summary sections", async () => {
    const episodes = await getEpisodes();
    for (const episode of episodes) {
      expect(getMarkdownSection(episode.summaryRaw, "一句话总结")).not.toBe("");
      expect(getMarkdownSection(episode.summaryRaw, "核心观点")).not.toBe("");
    }
  });
});
