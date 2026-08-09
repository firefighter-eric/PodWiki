import "server-only";
import generatedSearchIndex from "@/.generated/search-index.json";
import {
  createSearchContent,
  hydrateSearchIndex,
  type GeneratedSearchIndex,
} from "@/lib/search-core";

const searchDocuments = hydrateSearchIndex(
  generatedSearchIndex as GeneratedSearchIndex,
);

export const searchContent = createSearchContent(async () => searchDocuments);
