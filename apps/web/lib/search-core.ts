import { assertReaderFacingSummary } from "@/lib/reader-copy";
import { getTranscriptHref } from "@/lib/reader-routes";
import type { SearchResult } from "@/lib/types";

export const searchIndexFormat = "podwiki-search-index-v1" as const;

export type RawSearchSegment = [timestamp: string, text: string];

export type RawSearchEpisodeDocument = {
  id: string;
  title: string;
  titleSource: string;
  showTitle: string;
  href: string;
  episodeHaystack: string;
  summaryRaw: string;
  transcriptSegments: RawSearchSegment[];
  translationSegments: RawSearchSegment[];
};

export type GeneratedSearchIndex = {
  format: typeof searchIndexFormat;
  contentDigest: string;
  documents: RawSearchEpisodeDocument[];
};

export type IndexedSearchText = {
  text: string;
  normalized: string;
};

export type SearchSegmentDocument = {
  id: string;
  timestamp: string;
  content: IndexedSearchText;
};

export type SearchEpisodeDocument = {
  id: string;
  title: string;
  titleNormalized: string;
  showTitle: string;
  href: string;
  episodeHaystack: IndexedSearchText;
  summaryNormalized: string;
  summarySnippet: IndexedSearchText;
  transcriptSegments: SearchSegmentDocument[];
  translationSegments: SearchSegmentDocument[];
};

const searchResultCacheLimit = 64;

function compactSearchText(text: string): string {
  return text.replace(/\s+/gu, " ").trim();
}

export function indexSearchText(text: string): IndexedSearchText {
  const compact = compactSearchText(text);
  return {
    text: compact,
    normalized: compact.toLocaleLowerCase("zh-CN"),
  };
}

export function toSearchSegment(segment: {
  id: string;
  timestamp: string;
  text: string;
}): SearchSegmentDocument {
  return {
    id: segment.id,
    timestamp: segment.timestamp,
    content: indexSearchText(segment.text),
  };
}

function hydrateSegments(segments: RawSearchSegment[]): SearchSegmentDocument[] {
  const seen = new Map<string, number>();
  return segments.map(([timestamp, text]) => {
    if (!/^\d{2}:[0-5]\d:[0-5]\d$/u.test(timestamp)) {
      throw new Error(`Invalid generated search timestamp: ${timestamp}`);
    }
    const baseId = `t-${timestamp.replaceAll(":", "-")}`;
    const duplicateIndex = seen.get(baseId) ?? 0;
    seen.set(baseId, duplicateIndex + 1);
    return toSearchSegment({
      id: duplicateIndex === 0 ? baseId : `${baseId}-${duplicateIndex + 1}`,
      timestamp,
      text,
    });
  });
}

export function hydrateSearchIndex(index: GeneratedSearchIndex): SearchEpisodeDocument[] {
  if (index.format !== searchIndexFormat) {
    throw new Error(`Unsupported generated search index format: ${String(index.format)}`);
  }
  if (!/^[0-9a-f]{64}$/u.test(index.contentDigest)) {
    throw new Error("Generated search index has an invalid content digest");
  }

  return index.documents.map((document) => {
    const readerSummary = document.summaryRaw;
    assertReaderFacingSummary(readerSummary);
    return {
      id: document.id,
      title: document.title,
      titleNormalized: document.titleSource.toLocaleLowerCase("zh-CN"),
      showTitle: document.showTitle,
      href: document.href,
      episodeHaystack: indexSearchText(document.episodeHaystack),
      summaryNormalized: readerSummary.toLocaleLowerCase("zh-CN"),
      summarySnippet: indexSearchText(readerSummary.replace(/[#*`>\[\]]/gu, "")),
      transcriptSegments: hydrateSegments(document.transcriptSegments),
      translationSegments: hydrateSegments(document.translationSegments),
    };
  });
}

function snippetAround(
  indexedText: IndexedSearchText,
  normalizedQuery: string,
  queryLength: number,
  radius = 58,
): string {
  const index = indexedText.normalized.indexOf(normalizedQuery);
  if (index < 0) return indexedText.text.slice(0, radius * 2);
  const start = Math.max(0, index - radius);
  const end = Math.min(indexedText.text.length, index + queryLength + radius);
  return `${start > 0 ? "…" : ""}${indexedText.text.slice(start, end)}${end < indexedText.text.length ? "…" : ""}`;
}

function findFirstSegmentMatches(
  segments: SearchSegmentDocument[],
  normalizedQuery: string,
  limit = 3,
): SearchSegmentDocument[] {
  const matches: SearchSegmentDocument[] = [];
  for (const segment of segments) {
    if (!segment.content.normalized.includes(normalizedQuery)) continue;
    matches.push(segment);
    if (matches.length === limit) break;
  }
  return matches;
}

export function createSearchContent(
  getDocuments: () => Promise<SearchEpisodeDocument[]>,
): (rawQuery: string) => Promise<SearchResult[]> {
  const searchResultCache = new Map<string, SearchResult[]>();

  function getCachedSearchResults(query: string): SearchResult[] | undefined {
    const cached = searchResultCache.get(query);
    if (!cached) return undefined;
    searchResultCache.delete(query);
    searchResultCache.set(query, cached);
    return cached;
  }

  function cacheSearchResults(query: string, results: SearchResult[]): SearchResult[] {
    searchResultCache.set(query, results);
    if (searchResultCache.size > searchResultCacheLimit) {
      const oldestQuery = searchResultCache.keys().next().value;
      if (oldestQuery !== undefined) searchResultCache.delete(oldestQuery);
    }
    return results;
  }

  return async (rawQuery: string): Promise<SearchResult[]> => {
    const query = rawQuery.trim();
    if (!query) return [];
    const lowerQuery = query.toLocaleLowerCase("zh-CN");
    const cached = getCachedSearchResults(lowerQuery);
    if (cached) return cached;
    const results: SearchResult[] = [];

    for (const episode of await getDocuments()) {
      if (episode.episodeHaystack.normalized.includes(lowerQuery)) {
        results.push({
          id: `${episode.id}:episode`,
          title: episode.title,
          showTitle: episode.showTitle,
          section: "单集",
          snippet: snippetAround(episode.episodeHaystack, lowerQuery, query.length),
          href: episode.href,
          score: episode.titleNormalized.includes(lowerQuery) ? 90 : 70,
        });
      }

      if (episode.summaryNormalized.includes(lowerQuery)) {
        results.push({
          id: `${episode.id}:summary`,
          title: episode.title,
          showTitle: episode.showTitle,
          section: "总结",
          snippet: snippetAround(episode.summarySnippet, lowerQuery, query.length),
          href: episode.href,
          score: 60,
        });
      }

      const transcriptMatches = findFirstSegmentMatches(
        episode.transcriptSegments,
        lowerQuery,
      );
      for (const segment of transcriptMatches) {
        results.push({
          id: `${episode.id}:${segment.id}`,
          title: episode.title,
          showTitle: episode.showTitle,
          section: "逐字稿",
          snippet: snippetAround(segment.content, lowerQuery, query.length),
          href: getTranscriptHref(episode.href, segment.id),
          timestamp: segment.timestamp,
          score: 50,
        });
      }

      const translationMatches = findFirstSegmentMatches(
        episode.translationSegments,
        lowerQuery,
      );
      for (const segment of translationMatches) {
        results.push({
          id: `${episode.id}:translation:${segment.id}`,
          title: episode.title,
          showTitle: episode.showTitle,
          section: "译稿",
          snippet: snippetAround(segment.content, lowerQuery, query.length),
          href: getTranscriptHref(episode.href, segment.id),
          timestamp: segment.timestamp,
          score: 49,
        });
      }
    }

    return cacheSearchResults(lowerQuery, results
      .sort((a, b) => b.score - a.score || a.title.localeCompare(b.title, "zh-CN"))
      .slice(0, 24));
  };
}
