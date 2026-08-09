import { describe, expect, it } from "vitest";
import generatedSearchIndex from "@/.generated/search-index.json";
import { searchContent as searchGeneratedIndex } from "@/lib/search";
import {
  buildSearchDocumentsForTesting,
  getEpisodes,
  searchContent as searchRuntimeContent,
} from "@/lib/content";
import { getReaderFacingSummary } from "@/lib/reader-copy";
import {
  hydrateSearchIndex,
  type GeneratedSearchIndex,
} from "@/lib/search-core";

describe("generated search index", () => {
  it("matches every document built by the formal content loader", async () => {
    expect(hydrateSearchIndex(generatedSearchIndex as GeneratedSearchIndex))
      .toEqual(await buildSearchDocumentsForTesting());
  });

  it("stores exactly the formal reader projection instead of relying on hydration to redact it", async () => {
    const summaries = new Map(
      (await getEpisodes()).map((episode) => [
        episode.id,
        getReaderFacingSummary(episode.summaryRaw),
      ]),
    );
    for (const document of (generatedSearchIndex as GeneratedSearchIndex).documents) {
      expect(document.summaryRaw, document.id).toBe(summaries.get(document.id));
    }
  });

  it("rejects a generated index without a valid content digest", () => {
    expect(() => hydrateSearchIndex({
      ...(generatedSearchIndex as GeneratedSearchIndex),
      contentDigest: "not-a-sha256",
    })).toThrow("invalid content digest");
  });

  it("preserves the runtime content search contract", async () => {
    for (const query of [
      "田渊栋",
      "第一性原理",
      "端到端延迟必须很低",
      "AI",
      "不存在词条xyz",
    ]) {
      expect(await searchGeneratedIndex(query)).toEqual(await searchRuntimeContent(query));
    }
  });

  it("does not expose editorial status or artifact provenance in summary results", async () => {
    for (const document of (generatedSearchIndex as GeneratedSearchIndex).documents) {
      const readerSummary = document.summaryRaw.replaceAll("ASR—LLM—TTS", "");
      expect(readerSummary, document.id).not.toMatch(
        /(?:状态：\s*`?(?:draft|machine|reviewed)|SHA-256|Qwen3-ASR|qwen-asr-transformers|source_transcript|selection_status|PodWiki|本稿|逐字稿|正式稿|\bASR\b|正式(?:审核|复核)|\*\*待(?:事实核查|技术验证|人工(?:审核|复核))\*\*)/iu,
      );
    }

    for (const query of [
      "状态：draft",
      "7b52225e6148512a66d5b8cff80689894205335b83c25e5d852132c16c5a52c3",
      "qwen-asr-transformers",
    ]) {
      const results = await searchGeneratedIndex(query);
      expect(results.filter((result) => result.section === "总结"), query).toEqual([]);
      expect(results).toEqual(await searchRuntimeContent(query));
    }
  });
});
