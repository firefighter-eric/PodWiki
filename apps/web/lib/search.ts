import "server-only";
import generatedSearchBundle from "@/.generated/search-index-bundle.json";
import { unpackSearchIndex } from "@/lib/search-bundle";
import {
  createSearchContent,
  hydrateSearchIndex,
} from "@/lib/search-core";

const searchDocuments = hydrateSearchIndex(
  unpackSearchIndex(generatedSearchBundle),
);

export const searchContent = createSearchContent(async () => searchDocuments);
