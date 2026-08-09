import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import matter from "gray-matter";

const searchIndexFormat = "podwiki-search-index-v1";
const webRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const repositoryRoot = path.resolve(webRoot, "../..");
const showsRoot = path.join(repositoryRoot, "shows");
const outputDirectory = path.join(webRoot, ".generated");
const outputPath = path.join(outputDirectory, "search-index.json");
const summaryH2 = /^##\s+(.+?)\s*$/gmu;
const expectedSummaryHeadings = [
  "一句话总结",
  "为什么值得听",
  "核心观点",
  ["5 分钟读完", "整体总结"],
  "主题导航",
  "阅读边界",
  "编辑记录（不对读者展示）",
];
const editorCopy = [
  /(?:状态\s*(?:为|：)|当前为|仍是).{0,12}(?:draft|reviewed|machine|草稿|未审核|待审核)/iu,
  /(?:\b(?:source_transcript|selection_status|lineage)\b|SHA-256|[a-f\d]{64})/iu,
  /(?:qwen-asr-transformers|mlx-audio|transcript\.(?:zh-CN|en)\.md|README(?:\.md)?)/iu,
  /(?:PodWiki|本稿|逐字稿|正式稿|\bASR\b)/iu,
  /机器(?:逐字稿|稿|初稿|转写|识别|翻译)/u,
  /(?:草稿|未审核|待审核|待校对|待回听|待核听|人工(?:审核|复核)|正式(?:审核|复核)|回听|核听|校对)/u,
  /`(?:draft|reviewed|machine|selected)`/iu,
  /frozen publisher metadata/iu,
];

function matchesExpectedHeading(actual, expected) {
  return typeof expected === "string" ? actual === expected : expected.includes(actual);
}

function getReaderFacingSummary(markdown) {
  const headings = [...markdown.matchAll(summaryH2)];
  const structureIsValid = headings.length === expectedSummaryHeadings.length
    && headings.every((heading, index) => (
      matchesExpectedHeading(heading[1].trim(), expectedSummaryHeadings[index])
    ));
  if (!structureIsValid) {
    const actual = headings.map((heading) => heading[1].trim()).join(" → ") || "无二级标题";
    throw new Error(`Summary reader sections are missing or out of order: ${actual}`);
  }

  const readerSummary = markdown.slice(headings[0].index, headings.at(-1).index).trim();
  const copyForAudit = readerSummary.replaceAll("ASR—LLM—TTS", "");
  const internalMatch = editorCopy
    .map((pattern) => pattern.exec(copyForAudit))
    .find((match) => match !== null);
  if (internalMatch) {
    throw new Error(`Summary reader content contains editor-only copy: ${internalMatch[0]}`);
  }

  return readerSummary;
}

function readMarkdown(filePath) {
  const bytes = fs.readFileSync(filePath);
  const parsed = matter(bytes.toString("utf8"));
  return {
    data: parsed.data,
    content: parsed.content.trim(),
    sha256: createHash("sha256").update(bytes).digest("hex"),
  };
}

function requireString(value, label) {
  if (typeof value !== "string" || value.length === 0) {
    throw new Error(`${label} must be a non-empty string`);
  }
  return value;
}

function resolveEpisodeAsset(episodeRoot, relativePath, label) {
  const value = requireString(relativePath, label);
  const resolved = path.resolve(episodeRoot, value);
  const relative = path.relative(episodeRoot, resolved);
  if (
    !relative
    || relative.startsWith(`..${path.sep}`)
    || path.isAbsolute(relative)
    || relative.includes(path.sep)
  ) {
    throw new Error(`${label} must name one file in the episode directory: ${value}`);
  }
  if (!fs.existsSync(resolved)) throw new Error(`${label} does not exist: ${resolved}`);
  return resolved;
}

function parseTranscript(markdown, label) {
  const segments = [...markdown.matchAll(
    /^\[(\d{2}:[0-5]\d:[0-5]\d)\]\s+(.+?)\s{0,2}$/gmu,
  )].map((match) => [match[1], match[2].trim()]);
  if (segments.length === 0) throw new Error(`${label} has no timestamped segments`);
  return segments;
}

function isWebPublishable(workflow) {
  return workflow?.metadata === "verified"
    && (workflow.summary === "draft" || workflow.summary === "reviewed")
    && ["machine", "edited", "reviewed"].includes(workflow.transcript);
}

function participantSearchTerms(participant) {
  const profile = participant.profile;
  return [
    participant.name,
    ...(participant.aliases ?? []),
    ...(profile ? [
      profile.headline,
      ...(profile.bio ? [profile.bio] : []),
      ...(profile.affiliations ?? []).flatMap((affiliation) => [
        affiliation.organization,
        ...(affiliation.title ? [affiliation.title] : []),
      ]),
      ...(profile.education ?? []).flatMap((education) => [
        education.institution,
        ...(education.credential ? [education.credential] : []),
        ...(education.field ? [education.field] : []),
      ]),
    ] : []),
  ].map((value, index) => requireString(value, `${participant.name ?? "participant"} search term ${index + 1}`));
}

function loadTranslationSegments({
  episodeRoot,
  episodeId,
  language,
  transcriptMetadata,
  transcriptPath,
  transcriptSha256,
  transcriptSegments,
}) {
  const translations = transcriptMetadata.translations ?? [];
  const sourceIsEnglish = /^en(?:-|$)/iu.test(language);
  if (!sourceIsEnglish && translations.length > 0) {
    throw new Error(`${episodeId} transcript translations are only supported for English sources`);
  }
  const translation = translations.find((value) => value.language === "zh-CN");
  if (!sourceIsEnglish) return [];
  if (!translation) throw new Error(`${episodeId} has an English transcript but no zh-CN translation`);
  if (translation.source_path !== transcriptMetadata.path) {
    throw new Error(`${episodeId} zh-CN translation source_path does not match transcript.path`);
  }
  if (translation.source_sha256 !== transcriptSha256) {
    throw new Error(`${episodeId} zh-CN translation source SHA-256 mismatch`);
  }
  const translationPath = resolveEpisodeAsset(
    episodeRoot,
    translation.path,
    `${episodeId} zh-CN translation path`,
  );
  if (translationPath === transcriptPath) {
    throw new Error(`${episodeId} zh-CN translation must not overwrite its source transcript`);
  }
  const translationMarkdown = readMarkdown(translationPath);
  if (translation.sha256 !== translationMarkdown.sha256) {
    throw new Error(`${episodeId} zh-CN translation SHA-256 mismatch`);
  }
  const translationSegments = parseTranscript(
    translationMarkdown.content,
    `${episodeId} zh-CN translation`,
  );
  if (translationSegments.length !== transcriptSegments.length) {
    throw new Error(`${episodeId} zh-CN translation segment count mismatch`);
  }
  for (let index = 0; index < transcriptSegments.length; index += 1) {
    if (translationSegments[index][0] !== transcriptSegments[index][0]) {
      throw new Error(`${episodeId} zh-CN translation timestamp mismatch at segment ${index + 1}`);
    }
  }
  return translationSegments;
}

function buildSearchIndex() {
  const shows = new Map();
  for (const directory of fs.readdirSync(showsRoot, { withFileTypes: true })) {
    if (!directory.isDirectory()) continue;
    const readmePath = path.join(showsRoot, directory.name, "README.md");
    if (!fs.existsSync(readmePath)) continue;
    const metadata = readMarkdown(readmePath).data;
    if (metadata.id !== directory.name) {
      throw new Error(`Show id ${String(metadata.id)} does not match directory ${directory.name}`);
    }
    shows.set(directory.name, requireString(metadata.title, `${directory.name} title`));
  }

  const entries = [];
  for (const [showId, showTitle] of shows) {
    const episodesRoot = path.join(showsRoot, showId, "episodes");
    if (!fs.existsSync(episodesRoot)) continue;
    for (const directory of fs.readdirSync(episodesRoot, { withFileTypes: true })) {
      if (!directory.isDirectory()) continue;
      const folder = directory.name;
      const episodeRoot = path.join(episodesRoot, folder);
      const readmePath = path.join(episodeRoot, "README.md");
      if (!fs.existsSync(readmePath)) continue;
      const metadata = readMarkdown(readmePath).data;
      if (!isWebPublishable(metadata.workflow)) continue;
      const episodeId = requireString(metadata.id, `${readmePath} id`);
      if (metadata.show_id !== showId || metadata.slug !== folder) {
        throw new Error(`${episodeId} directory metadata does not match ${showId}/${folder}`);
      }
      const summaryPath = resolveEpisodeAsset(
        episodeRoot,
        metadata.summary?.path,
        `${episodeId} summary path`,
      );
      const transcriptPath = resolveEpisodeAsset(
        episodeRoot,
        metadata.transcript?.path,
        `${episodeId} transcript path`,
      );
      // Keep the generated production artifact reader-facing too. The full parity test
      // against lib/reader-copy.ts guards this small build-time projection from drifting.
      const summary = getReaderFacingSummary(readMarkdown(summaryPath).content);
      const transcript = readMarkdown(transcriptPath);
      const transcriptSegments = parseTranscript(transcript.content, `${episodeId} transcript`);
      const language = requireString(metadata.language, `${episodeId} language`);
      const translationSegments = loadTranslationSegments({
        episodeRoot,
        episodeId,
        language,
        transcriptMetadata: metadata.transcript,
        transcriptPath,
        transcriptSha256: transcript.sha256,
        transcriptSegments,
      });
      const participants = Array.isArray(metadata.participants) ? metadata.participants : [];
      const title = requireString(metadata.title, `${episodeId} title`);
      const navigationTitle = requireString(metadata.navigation_title, `${episodeId} navigation_title`);
      const href = `/shows/${showId}/episodes/${folder}`;

      entries.push({
        publishedAt: requireString(metadata.published_at, `${episodeId} published_at`),
        href,
        document: {
          id: episodeId,
          title: navigationTitle,
          titleSource: title,
          showTitle,
          href,
          episodeHaystack: [
            title,
            navigationTitle,
            requireString(metadata.catalog_keyword, `${episodeId} catalog_keyword`),
            showTitle,
            ...participants.flatMap(participantSearchTerms),
          ].join(" "),
          summaryRaw: summary,
          transcriptSegments,
          translationSegments,
        },
      });
    }
  }

  entries.sort((left, right) => (
    Date.parse(right.publishedAt) - Date.parse(left.publishedAt)
    || left.href.localeCompare(right.href)
  ));
  const documents = entries.map((entry) => entry.document);
  return {
    format: searchIndexFormat,
    contentDigest: createHash("sha256").update(JSON.stringify(documents)).digest("hex"),
    documents,
  };
}

const searchIndex = buildSearchIndex();
const serialized = `${JSON.stringify(searchIndex)}\n`;
fs.mkdirSync(outputDirectory, { recursive: true });
const temporaryPath = `${outputPath}.${process.pid}.tmp`;
fs.writeFileSync(temporaryPath, serialized);
fs.renameSync(temporaryPath, outputPath);
console.log(JSON.stringify({
  output: path.relative(repositoryRoot, outputPath),
  episodes: searchIndex.documents.length,
  bytes: Buffer.byteLength(serialized),
  contentDigest: searchIndex.contentDigest,
}));
