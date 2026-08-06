import { describe, expect, it } from "vitest";
import {
  getEpisode,
  getEpisodes,
  getShows,
  pairTranscriptSegments,
  searchContent,
  timestampToId,
} from "@/lib/content";
import type { TranscriptSegment } from "@/lib/types";
import { getMarkdownSection } from "@/lib/markdown";

describe("PodWiki content loader", () => {
  it("loads every current show and episode from the repository", async () => {
    const shows = await getShows();
    const episodes = await getEpisodes();
    expect(shows.map((show) => show.id)).toEqual([
      "zhangxiaojun",
      "sv101",
      "luoyonghao",
      "whynottv",
    ]);
    expect(episodes).toHaveLength(31);
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

  it("provides concise person-topic titles for every navigation item", async () => {
    const episodes = await getEpisodes();

    for (const episode of episodes) {
      const guestNames = episode.guests.map((guest) => guest.name).join("、");
      expect(guestNames).not.toBe("");
      expect(episode.navigationTitle).toMatch(/^.+ - .+$/u);
      expect(episode.navigationTitle.startsWith(`${guestNames} - `)).toBe(true);
      expect(episode.navigationTitle.length).toBeLessThanOrEqual(40);
    }
  });

  it("returns summary and timestamped transcript search results", async () => {
    const results = await searchContent("第一性原理");
    expect(results.some((result) => result.section === "总结")).toBe(true);
    expect(results.some((result) => result.section === "逐字稿" && result.timestamp)).toBe(true);
  });

  it("loads and strictly pairs the English transcript with its Chinese machine translation", async () => {
    const episode = await getEpisode("sv101", "bili-bv1dzsczfemv-li-mu");
    const translation = episode?.transcriptTranslations[0];
    const bilingual = episode?.bilingualTranscript;

    expect(episode?.language).toBe("en");
    expect(translation).toMatchObject({
      language: "zh-CN",
      sourceLanguage: "en",
      sourcePath: "transcript.en.md",
      path: "transcript.zh-CN.md",
      alignment: "segment",
      status: "machine",
    });
    expect(bilingual?.segments).toHaveLength(episode?.transcriptSegments.length ?? 0);
    expect(bilingual?.segments.every((segment, index) => (
      segment.timestamp === episode?.transcriptSegments[index]?.timestamp
      && segment.sourceText === episode?.transcriptSegments[index]?.text
      && Boolean(segment.translationText)
    ))).toBe(true);
  });

  it("indexes Chinese transcript translations with their source timestamp anchors", async () => {
    const results = await searchContent("端到端延迟必须很低");
    expect(results).toContainEqual(expect.objectContaining({
      section: "译稿",
      timestamp: "00:00:56",
      href: expect.stringContaining("bili-bv1dzsczfemv-li-mu?view=transcript#t-00-00-56"),
      snippet: expect.stringContaining("端到端延迟必须很低"),
    }));
  });

  it("rejects a translation whose timestamp order diverges from its source", () => {
    const segment = (timestamp: string, text: string): TranscriptSegment => ({
      timestamp,
      seconds: 0,
      text,
      id: timestampToId(timestamp),
    });
    expect(() => pairTranscriptSegments(
      [segment("00:00:00", "source one"), segment("00:00:02", "source two")],
      [segment("00:00:00", "译文一"), segment("00:00:03", "译文二")],
      "test translation",
    )).toThrow("test translation timestamp mismatch at segment 2");
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
