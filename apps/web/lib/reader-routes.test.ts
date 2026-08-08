import { describe, expect, it } from "vitest";
import { canonicalizeReaderHref, getTranscriptHref } from "@/lib/reader-routes";

describe("reader route helpers", () => {
  const episodeHref = "/shows/sv101/episodes/247-sheng-ying";

  it("builds canonical transcript paths with stable anchors", () => {
    expect(getTranscriptHref(episodeHref)).toBe(`${episodeHref}/transcript`);
    expect(getTranscriptHref(episodeHref, "t-00-00-56"))
      .toBe(`${episodeHref}/transcript#t-00-00-56`);
    expect(getTranscriptHref(
      episodeHref,
      `${episodeHref}?view=transcript#t-00-00-56`,
    )).toBe(`${episodeHref}/transcript#t-00-00-56`);
  });

  it("canonicalizes legacy reader query links without dropping other state", () => {
    expect(canonicalizeReaderHref(`${episodeHref}?view=summary`)).toBe(episodeHref);
    expect(canonicalizeReaderHref(`${episodeHref}?view=transcript#t-00-00-56`))
      .toBe(`${episodeHref}/transcript#t-00-00-56`);
    expect(canonicalizeReaderHref(`${episodeHref}?view=transcript&from=search#t-00-00-56`))
      .toBe(`${episodeHref}/transcript?from=search#t-00-00-56`);
  });
});
