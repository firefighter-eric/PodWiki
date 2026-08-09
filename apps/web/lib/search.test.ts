import { describe, expect, it } from "vitest";
import generatedSearchIndex from "@/.generated/search-index.json";
import { searchContent as searchGeneratedIndex } from "@/lib/search";
import {
  buildSearchDocumentsForTesting,
  searchContent as searchRuntimeContent,
} from "@/lib/content";
import {
  hydrateSearchIndex,
  type GeneratedSearchIndex,
} from "@/lib/search-core";

describe("generated search index", () => {
  it("matches every document built by the formal content loader", async () => {
    expect(hydrateSearchIndex(generatedSearchIndex as GeneratedSearchIndex))
      .toEqual(await buildSearchDocumentsForTesting());
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
});
