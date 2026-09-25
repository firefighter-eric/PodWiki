import { createHash } from "node:crypto";
import { gunzipSync } from "node:zlib";
import type { GeneratedSearchIndex } from "@/lib/search-core";

type SearchIndexBundle = {
  format: string;
  contentDigest: string;
  payload: string;
};

export function unpackSearchIndex(bundle: SearchIndexBundle): GeneratedSearchIndex {
  if (bundle.format !== "podwiki-search-index-gzip-v1") {
    throw new Error("Unsupported search index bundle format");
  }
  const index = JSON.parse(
    gunzipSync(Buffer.from(bundle.payload, "base64")).toString("utf8"),
  ) as GeneratedSearchIndex;
  const digest = createHash("sha256")
    .update(JSON.stringify(index.documents))
    .digest("hex");
  if (digest !== bundle.contentDigest || digest !== index.contentDigest) {
    throw new Error("Search index bundle content digest mismatch");
  }
  return index;
}
