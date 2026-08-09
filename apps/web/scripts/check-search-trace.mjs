import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const searchIndexMarker = "podwiki-search-index-v1";
const maximumTraceBytes = 30 * 1024 * 1024;
const webRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const tracePath = path.join(
  webRoot,
  ".next/server/app/api/search/route.js.nft.json",
);
const generatedIndexPath = path.join(webRoot, ".generated/search-index.json");

if (!fs.existsSync(tracePath)) {
  throw new Error(`Search route trace is missing; run npm run build first: ${tracePath}`);
}
if (!fs.existsSync(generatedIndexPath)) {
  throw new Error(`Generated search index is missing: ${generatedIndexPath}`);
}

const trace = JSON.parse(fs.readFileSync(tracePath, "utf8"));
if (!Array.isArray(trace.files)) throw new Error("Search route trace has no files array");
const generatedIndex = JSON.parse(fs.readFileSync(generatedIndexPath, "utf8"));
if (generatedIndex.format !== searchIndexMarker) {
  throw new Error(`Generated search index has an unexpected format: ${String(generatedIndex.format)}`);
}
if (!/^[0-9a-f]{64}$/u.test(generatedIndex.contentDigest)) {
  throw new Error("Generated search index has an invalid content digest");
}
const actualContentDigest = createHash("sha256")
  .update(JSON.stringify(generatedIndex.documents))
  .digest("hex");
if (actualContentDigest !== generatedIndex.contentDigest) {
  throw new Error("Generated search index content digest does not match its documents");
}

const traceDirectory = path.dirname(tracePath);
const traceFiles = [...new Set(trace.files)];
let totalBytes = 0;
let containsGeneratedIndex = false;
const tracedMarkdown = [];

for (const relativePath of traceFiles) {
  if (typeof relativePath !== "string") continue;
  const absolutePath = path.resolve(traceDirectory, relativePath);
  if (!fs.existsSync(absolutePath)) {
    throw new Error(`Search route trace references a missing file: ${absolutePath}`);
  }
  const stat = fs.statSync(absolutePath);
  if (!stat.isFile()) continue;
  totalBytes += stat.size;

  const normalizedPath = absolutePath.split(path.sep).join("/");
  if (/\/shows\/.+\.md$/u.test(normalizedPath)) tracedMarkdown.push(absolutePath);
  if (relativePath.endsWith(".js") || relativePath.endsWith(".json")) {
    const source = fs.readFileSync(absolutePath, "utf8");
    if (source.includes(generatedIndex.contentDigest)) containsGeneratedIndex = true;
  }
}

if (tracedMarkdown.length > 0) {
  throw new Error(`Search route still traces source Markdown:\n${tracedMarkdown.join("\n")}`);
}
if (!containsGeneratedIndex) {
  throw new Error(
    `Search route trace does not contain generated index ${generatedIndex.contentDigest}`,
  );
}
if (totalBytes > maximumTraceBytes) {
  throw new Error(
    `Search route trace is ${(totalBytes / 1024 / 1024).toFixed(2)} MiB; limit is 30 MiB`,
  );
}

console.log(JSON.stringify({
  files: traceFiles.length,
  bytes: totalBytes,
  mebibytes: Number((totalBytes / 1024 / 1024).toFixed(2)),
  sourceMarkdownFiles: tracedMarkdown.length,
  format: searchIndexMarker,
  contentDigest: generatedIndex.contentDigest,
}));
