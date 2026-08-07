import "server-only";
import { cache } from "react";
import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import matter from "gray-matter";
import { z } from "zod";
import { getTranscriptHref } from "@/lib/reader-routes";
import type {
  BilingualTranscript,
  BilingualTranscriptSegment,
  Chapter,
  Episode,
  EpisodeCard,
  SearchResult,
  ShowSummary,
  TranscriptSegment,
  TranscriptTranslationMetadata,
} from "@/lib/types";

const participantSchema = z
  .object({
    id: z.string().optional(),
    name: z.string(),
    role: z.string().optional(),
    aliases: z.array(z.string()).optional(),
  })
  .passthrough();

const sourceSchema = z
  .object({
    platform: z.string().optional(),
    kind: z.string().optional(),
    url: z.string(),
    preferred: z.boolean().optional(),
  })
  .passthrough();

const transcriptProvenanceSchema = z
  .object({
    path: z.string(),
    engine: z.string().optional(),
    model: z.string().optional(),
    selection_status: z.string().optional(),
  })
  .passthrough();

const transcriptTranslationSchema = z
  .object({
    language: z.string().min(1),
    path: z.string().min(1),
    source_language: z.string().min(1),
    source_path: z.string().min(1),
    alignment: z.literal("segment"),
    status: z.enum(["machine", "edited", "reviewed"]),
    generated_at: z.union([z.string().datetime({ offset: true }), z.date()]),
    source_sha256: z.string().regex(/^[0-9a-f]{64}$/u),
    sha256: z.string().regex(/^[0-9a-f]{64}$/u),
  })
  .passthrough();

const episodeTranscriptSchema = transcriptProvenanceSchema.extend({
  translations: z.array(transcriptTranslationSchema).optional().default([]),
});

const episodeSchema = z
  .object({
    id: z.string(),
    show_id: z.string(),
    episode_key: z.union([z.string(), z.number()]).transform(String),
    episode_number: z.number().nullable().optional().default(null),
    release_type: z.enum(["regular", "special", "bonus", "trailer"]).default("regular"),
    slug: z.string().optional(),
    title: z.string(),
    navigation_title: z.string(),
    catalog_keyword: z.string().min(1).max(20).refine(
      (value) => value === value.trim(),
      "catalog_keyword must not have leading or trailing whitespace",
    ),
    published_at: z.union([z.string(), z.date()]),
    duration_ms: z.number(),
    language: z.string(),
    participants: z.array(participantSchema).default([]),
    sources: z.array(sourceSchema).default([]),
    workflow: z
      .object({
        metadata: z.string().optional(),
        summary: z.string().optional(),
        transcript: z.string().optional(),
      })
      .default({}),
    summary: z
      .object({
        path: z.string(),
        source_transcript: transcriptProvenanceSchema.optional(),
      })
      .passthrough(),
    transcript: episodeTranscriptSchema,
  })
  .passthrough();

const showSchema = z
  .object({
    id: z.string(),
    title: z.string(),
  })
  .passthrough();

const showOrder = ["zhangxiaojun", "sv101", "latetalk", "luoyonghao", "whynottv"];

function findRepositoryRoot(): string {
  const configuredRoot = process.env.PODWIKI_REPOSITORY_ROOT;
  const monorepoRoot = path.resolve(/* turbopackIgnore: true */ process.cwd(), "../..");
  const candidates = configuredRoot
    ? [path.resolve(configuredRoot), process.cwd(), monorepoRoot]
    : [process.cwd(), monorepoRoot];

  const found = candidates.find((candidate) =>
    fs.existsSync(path.join(candidate, "shows")),
  );

  if (!found) {
    throw new Error(`Unable to locate PodWiki shows directory from ${process.cwd()}`);
  }

  return found;
}

function readMarkdown(filePath: string): {
  data: Record<string, unknown>;
  content: string;
  sha256: string;
} {
  const bytes = fs.readFileSync(filePath);
  const raw = bytes.toString("utf8");
  const parsed = matter(raw);
  return {
    data: parsed.data,
    content: parsed.content.trim(),
    sha256: createHash("sha256").update(bytes).digest("hex"),
  };
}

function resolveEpisodeAsset(episodeRoot: string, relativePath: string, label: string): string {
  const resolvedPath = path.resolve(episodeRoot, relativePath);
  const relativeToEpisode = path.relative(episodeRoot, resolvedPath);
  if (
    relativeToEpisode === "" ||
    relativeToEpisode.startsWith(`..${path.sep}`) ||
    path.isAbsolute(relativeToEpisode)
  ) {
    throw new Error(`${label} must stay inside the episode directory: ${relativePath}`);
  }
  return resolvedPath;
}

function formatDuration(durationMs: number): string {
  const totalSeconds = Math.round(durationMs / 1000);
  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;
  return [hours, minutes, seconds].map((value) => String(value).padStart(2, "0")).join(":");
}

function normalizeTitle(rawTitle: string): { displayTitle: string; subtitle: string } {
  const cleaned = rawTitle.replace(/\s*\|\s*B站.*$/u, "").trim();
  const [first, ...rest] = cleaned.split(/[：:]/u);
  const displayTitle = first
    .replace(/SpaceX/gu, " SpaceX ")
    .replace(/Falcon\s*9/gu, "Falcon 9")
    .replace(/\s+/gu, " ")
    .trim();

  return {
    displayTitle,
    subtitle: rest.join("：").trim(),
  };
}

function extractMarkdownTitle(markdown: string): string | undefined {
  return /^#\s+(.+)$/mu.exec(markdown)?.[1]?.trim();
}

function extractSummaryIntro(markdown: string): string {
  const heading = /^##\s+一句话总结\s*$/mu.exec(markdown);
  if (!heading) return "";

  const remainder = markdown.slice(heading.index + heading[0].length);
  const nextHeading = /^##\s+/mu.exec(remainder);
  return remainder
    .slice(0, nextHeading?.index ?? remainder.length)
    .replace(/!\[[^\]]*\]\([^)]+\)/gu, "")
    .replace(/\[([^\]]+)\]\([^)]+\)/gu, "$1")
    .replace(/\[(?:\d{2}:){2}\d{2}\]/gu, "")
    .replace(/[*_`]/gu, "")
    .replace(/\s+/gu, " ")
    .trim();
}

function normalizeProvenance(
  value: z.infer<typeof transcriptProvenanceSchema>,
) {
  return {
    path: value.path,
    engine: value.engine,
    model: value.model,
    selectionStatus: value.selection_status,
  };
}

function normalizeTranslationMetadata(
  value: z.infer<typeof transcriptTranslationSchema>,
): TranscriptTranslationMetadata {
  return {
    language: value.language,
    path: value.path,
    sourceLanguage: value.source_language,
    sourcePath: value.source_path,
    alignment: value.alignment,
    status: value.status,
    generatedAt: value.generated_at instanceof Date
      ? value.generated_at.toISOString()
      : value.generated_at,
    sourceSha256: value.source_sha256,
    sha256: value.sha256,
  };
}

function extractHeadingSection(markdown: string, heading: string): string {
  const escapedHeading = heading.replace(/[.*+?^${}()|[\]\\]/gu, "\\$&");
  const headingMatch = new RegExp(`^##\\s+${escapedHeading}\\s*$`, "mu").exec(markdown);
  if (!headingMatch) return "";
  const remainder = markdown.slice(headingMatch.index + headingMatch[0].length);
  const nextHeading = /^##\s+/mu.exec(remainder);
  return remainder.slice(0, nextHeading?.index ?? remainder.length);
}

export function timestampToSeconds(timestamp: string): number {
  const [hours, minutes, seconds] = timestamp.split(":").map(Number);
  return hours * 3600 + minutes * 60 + seconds;
}

export function timestampToId(timestamp: string): string {
  return `t-${timestamp.replaceAll(":", "-")}`;
}

export function findNearestTranscriptSegment(
  segments: TranscriptSegment[],
  timestamp: string,
): TranscriptSegment | undefined {
  const targetSeconds = timestampToSeconds(timestamp);
  return segments.reduce<TranscriptSegment | undefined>((nearest, segment) => {
    if (!nearest) return segment;
    const currentDistance = Math.abs(segment.seconds - targetSeconds);
    const nearestDistance = Math.abs(nearest.seconds - targetSeconds);
    return currentDistance < nearestDistance ? segment : nearest;
  }, undefined);
}

function parseTranscript(raw: string): TranscriptSegment[] {
  const seen = new Map<string, number>();
  const segments: TranscriptSegment[] = [];
  const linePattern = /^\[(\d{2}:\d{2}:\d{2})\]\s+(.+?)\s{0,2}$/gmu;

  for (const match of raw.matchAll(linePattern)) {
    const timestamp = match[1];
    const baseId = timestampToId(timestamp);
    const duplicateIndex = seen.get(baseId) ?? 0;
    seen.set(baseId, duplicateIndex + 1);
    segments.push({
      timestamp,
      seconds: timestampToSeconds(timestamp),
      text: match[2].trim(),
      id: duplicateIndex === 0 ? baseId : `${baseId}-${duplicateIndex + 1}`,
    });
  }

  return segments;
}

export function pairTranscriptSegments(
  sourceSegments: TranscriptSegment[],
  translationSegments: TranscriptSegment[],
  label = "transcript translation",
): BilingualTranscriptSegment[] {
  if (sourceSegments.length !== translationSegments.length) {
    throw new Error(
      `${label} segment count mismatch: source has ${sourceSegments.length}, translation has ${translationSegments.length}`,
    );
  }

  return sourceSegments.map((source, index) => {
    const translation = translationSegments[index];
    if (source.timestamp !== translation.timestamp) {
      throw new Error(
        `${label} timestamp mismatch at segment ${index + 1}: source ${source.timestamp}, translation ${translation.timestamp}`,
      );
    }
    return {
      timestamp: source.timestamp,
      seconds: source.seconds,
      id: source.id,
      sourceText: source.text,
      translationText: translation.text,
    };
  });
}

function loadTranscriptTranslations({
  episodeRoot,
  episodeId,
  episodeLanguage,
  sourcePath,
  sourceSha256,
  sourceContent,
  sourceSegments,
  values,
}: {
  episodeRoot: string;
  episodeId: string;
  episodeLanguage: string;
  sourcePath: string;
  sourceSha256: string;
  sourceContent: string;
  sourceSegments: TranscriptSegment[];
  values: z.infer<typeof transcriptTranslationSchema>[];
}): {
  translations: TranscriptTranslationMetadata[];
  bilingualTranscript?: BilingualTranscript;
} {
  const sourceIsEnglish = /^en(?:-|$)/iu.test(episodeLanguage);
  if (!sourceIsEnglish && values.length > 0) {
    throw new Error(`${episodeId} transcript translations are only supported for English sources`);
  }

  const sourceTitle = extractMarkdownTitle(sourceContent);
  if (sourceIsEnglish && !sourceTitle) {
    throw new Error(`${episodeId} English transcript is missing its Markdown H1 title`);
  }

  const languages = new Set<string>();
  let bilingualTranscript: BilingualTranscript | undefined;
  const translations = values.map((value) => {
    const metadata = normalizeTranslationMetadata(value);
    if (languages.has(metadata.language)) {
      throw new Error(`${episodeId} has more than one ${metadata.language} transcript translation`);
    }
    languages.add(metadata.language);

    if (!/^en(?:-|$)/iu.test(metadata.sourceLanguage)) {
      throw new Error(
        `${episodeId} ${metadata.language} translation source_language must be an English language tag`,
      );
    }
    if (metadata.sourcePath !== sourcePath) {
      throw new Error(
        `${episodeId} ${metadata.language} translation source_path ${metadata.sourcePath} does not match selected transcript ${sourcePath}`,
      );
    }
    if (metadata.path === sourcePath) {
      throw new Error(`${episodeId} ${metadata.language} translation must not overwrite its source transcript`);
    }
    if (metadata.sourceSha256 !== sourceSha256) {
      throw new Error(
        `${episodeId} ${metadata.language} translation source SHA-256 does not match ${sourcePath}`,
      );
    }

    const translationPath = resolveEpisodeAsset(
      episodeRoot,
      metadata.path,
      `${episodeId} ${metadata.language} translation path`,
    );
    if (!fs.existsSync(translationPath)) {
      throw new Error(`${episodeId} is missing ${metadata.language} translation: ${translationPath}`);
    }
    const translation = readMarkdown(translationPath);
    if (translation.sha256 !== metadata.sha256) {
      throw new Error(`${episodeId} ${metadata.language} translation SHA-256 does not match ${metadata.path}`);
    }
    if (extractMarkdownTitle(translation.content) !== sourceTitle) {
      throw new Error(
        `${episodeId} ${metadata.language} translation Markdown H1 does not match ${sourcePath}`,
      );
    }

    const segments = parseTranscript(translation.content);
    const pairedSegments = pairTranscriptSegments(
      sourceSegments,
      segments,
      `${episodeId} ${metadata.language} translation`,
    );
    if (sourceIsEnglish && metadata.language === "zh-CN") {
      bilingualTranscript = { ...metadata, segments: pairedSegments };
    }
    return metadata;
  });

  if (sourceIsEnglish && !bilingualTranscript) {
    throw new Error(`${episodeId} has an English transcript but no zh-CN segment translation`);
  }

  return {
    translations,
    bilingualTranscript,
  };
}

function parseChapters(
  readmeRaw: string,
  summaryRaw: string,
  href: string,
  transcriptSegments: TranscriptSegment[],
): Chapter[] {
  const patterns = [
    /^-\s+(\d{2}:\d{2}:\d{2})\s+[—–-]\s+(.+)$/gmu,
    /^-\s+(?:\*\*)?\[(\d{2}:\d{2}:\d{2})\](?:[^*]*\*\*)?\s*[—–-]?\s*(.+)$/gmu,
  ];

  const collect = (source: string, pattern: RegExp): Chapter[] => {
    const result: Chapter[] = [];
    const seen = new Set<string>();
    for (const match of source.matchAll(pattern)) {
      const timestamp = match[1];
      const title = match[2]
        .replace(/\[[^\]]+\]/gu, "")
        .replace(/[*_`]/gu, "")
        .trim();
      if (!title || seen.has(timestamp)) continue;
      seen.add(timestamp);
      const target = findNearestTranscriptSegment(transcriptSegments, timestamp);
      result.push({
        timestamp,
        title,
        seconds: timestampToSeconds(timestamp),
        href: getTranscriptHref(href, target?.id ?? timestampToId(timestamp)),
      });
    }
    return result;
  };

  const summaryChapters = collect(extractHeadingSection(summaryRaw, "主题导航"), patterns[1]);
  const readmeChapters = collect(readmeRaw, patterns[0]);
  const chapters = summaryChapters.length >= 4 ? summaryChapters : readmeChapters;

  if (!chapters.some((chapter) => chapter.seconds === 0) && transcriptSegments[0]) {
    const firstSegment = transcriptSegments[0];
    chapters.unshift({
      timestamp: firstSegment.timestamp,
      title: "开场",
      seconds: firstSegment.seconds,
      href: getTranscriptHref(href, firstSegment.id),
    });
  }

  return chapters.toSorted((a, b) => a.seconds - b.seconds);
}

function showShortTitle(showId: string, title: string): string {
  if (showId === "whynottv") return "WhynotTV";
  return title;
}

function extractShowDescription(markdown: string): string {
  const withoutHeading = markdown.replace(/^#\s+.+$/mu, "").trim();
  return withoutHeading.split(/^##\s+/mu)[0].replace(/\s+/gu, " ").trim();
}

type ShowCatalogData = {
  id: string;
  title: string;
  description: string;
};

type EpisodeCatalogEntry = {
  card: EpisodeCard;
  publishedAt: string;
};

type ContentCatalog = {
  shows: ShowSummary[];
  episodeEntries: EpisodeCatalogEntry[];
};

function resolveNamedDirectory(parent: string, name: string): string | undefined {
  if (!name) return undefined;
  const resolved = path.resolve(parent, name);
  const relative = path.relative(parent, resolved);
  if (
    !relative ||
    relative.startsWith(`..${path.sep}`) ||
    path.isAbsolute(relative) ||
    relative.includes(path.sep)
  ) {
    return undefined;
  }
  return resolved;
}

const loadShowById = cache(async (showId: string): Promise<ShowCatalogData | undefined> => {
  const showsRoot = path.join(findRepositoryRoot(), "shows");
  const showRoot = resolveNamedDirectory(showsRoot, showId);
  if (!showRoot) return undefined;
  const readmePath = path.join(showRoot, "README.md");
  if (!fs.existsSync(readmePath)) return undefined;

  const readme = readMarkdown(readmePath);
  const metadata = showSchema.parse(readme.data);
  return {
    id: metadata.id,
    title: metadata.title,
    description: extractShowDescription(readme.content),
  };
});

function episodeCardFromMetadata({
  metadata,
  showTitle,
  folder,
  summaryRaw,
}: {
  metadata: z.infer<typeof episodeSchema>;
  showTitle: string;
  folder: string;
  summaryRaw: string;
}): EpisodeCatalogEntry {
  const publishedAt = metadata.published_at instanceof Date
    ? metadata.published_at.toISOString()
    : metadata.published_at;
  const editorialTitle = extractMarkdownTitle(summaryRaw) ?? metadata.title;
  const normalizedTitle = normalizeTitle(editorialTitle);

  return {
    publishedAt,
    card: {
      id: metadata.id,
      showId: metadata.show_id,
      showTitle,
      episodeNumber: metadata.episode_number,
      folder,
      title: metadata.title,
      navigationTitle: metadata.navigation_title,
      catalogKeyword: metadata.catalog_keyword,
      editorialTitle,
      displayTitle: normalizedTitle.displayTitle,
      subtitle: normalizedTitle.subtitle,
      summaryIntro: extractSummaryIntro(summaryRaw),
      publishedDate: publishedAt.slice(0, 10),
      guests: metadata.participants.filter((participant) => participant.role === "guest"),
      workflow: metadata.workflow,
      href: `/shows/${metadata.show_id}/episodes/${folder}`,
    },
  };
}

const loadCatalog = cache(async (): Promise<ContentCatalog> => {
  const repositoryRoot = findRepositoryRoot();
  const showsRoot = path.join(repositoryRoot, "shows");
  const showDirectories = fs
    .readdirSync(showsRoot, { withFileTypes: true })
    .filter((entry) => entry.isDirectory() && fs.existsSync(path.join(showsRoot, entry.name, "README.md")));

  const showData = new Map<string, ShowCatalogData>();
  for (const directory of showDirectories) {
    const show = await loadShowById(directory.name);
    if (!show) continue;
    if (show.id !== directory.name) {
      throw new Error(
        `Show id ${show.id} does not match its directory name ${directory.name}`,
      );
    }
    showData.set(directory.name, show);
  }

  const episodeEntries: EpisodeCatalogEntry[] = [];
  for (const [showId, currentShow] of showData) {
    const episodesRoot = path.join(showsRoot, showId, "episodes");
    if (!fs.existsSync(episodesRoot)) continue;
    for (const directory of fs.readdirSync(episodesRoot, { withFileTypes: true })) {
      if (!directory.isDirectory()) continue;
      const folder = directory.name;
      const episodeRoot = path.join(episodesRoot, folder);
      const readmePath = path.join(episodeRoot, "README.md");
      if (!fs.existsSync(readmePath)) continue;

      const readme = readMarkdown(readmePath);
      const metadata = episodeSchema.parse(readme.data);
      if (metadata.show_id !== showId) {
        throw new Error(
          `Episode ${metadata.id} declares show ${metadata.show_id} but is stored under ${showId}`,
        );
      }
      const summaryPath = resolveEpisodeAsset(
        episodeRoot,
        metadata.summary.path,
        `${metadata.id} summary path`,
      );
      const transcriptPath = resolveEpisodeAsset(
        episodeRoot,
        metadata.transcript.path,
        `${metadata.id} transcript path`,
      );
      if (!fs.existsSync(summaryPath)) {
        throw new Error(`Missing summary for ${metadata.id}: ${summaryPath}`);
      }
      if (!fs.existsSync(transcriptPath)) {
        throw new Error(`Missing transcript for ${metadata.id}: ${transcriptPath}`);
      }

      const summary = readMarkdown(summaryPath);
      episodeEntries.push(episodeCardFromMetadata({
        metadata,
        showTitle: currentShow.title,
        folder,
        summaryRaw: summary.content,
      }));
    }
  }

  episodeEntries.sort((a, b) => Date.parse(b.publishedAt) - Date.parse(a.publishedAt));

  const shows: ShowSummary[] = [...showData.entries()]
    .map(([id, data]) => {
      const showEpisodes = episodeEntries.filter((entry) => entry.card.showId === id);
      return {
        id,
        title: data.title,
        shortTitle: showShortTitle(id, data.title),
        description: data.description,
        episodeCount: showEpisodes.length,
        href: `/shows/${id}`,
        latestEpisodeHref: showEpisodes[0]?.card.href ?? `/shows/${id}`,
      };
    })
    .sort((a, b) => showOrder.indexOf(a.id) - showOrder.indexOf(b.id));

  return { shows, episodeEntries };
});

const loadEpisodeByLocation = cache(async (
  showId: string,
  folder: string,
): Promise<Episode | undefined> => {
  const repositoryRoot = findRepositoryRoot();
  const showsRoot = path.join(repositoryRoot, "shows");
  const showRoot = resolveNamedDirectory(showsRoot, showId);
  if (!showRoot) return undefined;

  const show = await loadShowById(showId);
  if (!show || show.id !== showId) return undefined;

  const episodesRoot = path.join(showRoot, "episodes");
  const episodeRoot = resolveNamedDirectory(episodesRoot, folder);
  if (!episodeRoot) return undefined;
  const readmePath = path.join(episodeRoot, "README.md");
  if (!fs.existsSync(readmePath)) return undefined;

  const readme = readMarkdown(readmePath);
  const metadata = episodeSchema.parse(readme.data);
  if (metadata.show_id !== showId) return undefined;

  const summaryPath = resolveEpisodeAsset(
    episodeRoot,
    metadata.summary.path,
    `${metadata.id} summary path`,
  );
  const transcriptPath = resolveEpisodeAsset(
    episodeRoot,
    metadata.transcript.path,
    `${metadata.id} transcript path`,
  );
  if (!fs.existsSync(summaryPath)) {
    throw new Error(`Missing summary for ${metadata.id}: ${summaryPath}`);
  }
  if (!fs.existsSync(transcriptPath)) {
    throw new Error(`Missing transcript for ${metadata.id}: ${transcriptPath}`);
  }

  const summary = readMarkdown(summaryPath);
  const transcript = readMarkdown(transcriptPath);
  const publishedAt = metadata.published_at instanceof Date
    ? metadata.published_at.toISOString()
    : metadata.published_at;
  const href = `/shows/${metadata.show_id}/episodes/${folder}`;
  const editorialTitle = extractMarkdownTitle(summary.content) ?? metadata.title;
  const normalizedTitle = normalizeTitle(editorialTitle);
  const transcriptSegments = parseTranscript(transcript.content);
  const { translations: transcriptTranslations, bilingualTranscript } = loadTranscriptTranslations({
    episodeRoot,
    episodeId: metadata.id,
    episodeLanguage: metadata.language,
    sourcePath: metadata.transcript.path,
    sourceSha256: transcript.sha256,
    sourceContent: transcript.content,
    sourceSegments: transcriptSegments,
    values: metadata.transcript.translations,
  });
  const episode: Episode = {
    id: metadata.id,
    showId: metadata.show_id,
    showTitle: show.title,
    episodeKey: metadata.episode_key,
    episodeNumber: metadata.episode_number,
    releaseType: metadata.release_type,
    folder,
    title: metadata.title,
    navigationTitle: metadata.navigation_title,
    catalogKeyword: metadata.catalog_keyword,
    editorialTitle,
    displayTitle: normalizedTitle.displayTitle,
    subtitle: normalizedTitle.subtitle,
    summaryIntro: extractSummaryIntro(summary.content),
    publishedAt,
    publishedDate: publishedAt.slice(0, 10),
    durationMs: metadata.duration_ms,
    durationLabel: formatDuration(metadata.duration_ms),
    language: metadata.language,
    participants: metadata.participants,
    guests: metadata.participants.filter((participant) => participant.role === "guest"),
    hosts: metadata.participants.filter((participant) => participant.role === "host"),
    sources: metadata.sources,
    preferredSource: metadata.sources.find((source) => source.preferred) ?? metadata.sources[0],
    workflow: metadata.workflow,
    summarySourceTranscript: metadata.summary.source_transcript
      ? normalizeProvenance(metadata.summary.source_transcript)
      : undefined,
    transcriptMeta: normalizeProvenance(metadata.transcript),
    summaryRaw: summary.content,
    transcriptRaw: transcript.content,
    readmeRaw: readme.content,
    chapters: [],
    transcriptSegments,
    transcriptTranslations,
    bilingualTranscript,
    href,
  };
  episode.chapters = parseChapters(
    episode.readmeRaw,
    episode.summaryRaw,
    href,
    transcriptSegments,
  );
  return episode;
});

const loadAllEpisodes = cache(async (): Promise<Episode[]> => {
  const { episodeEntries } = await loadCatalog();
  const episodes = await Promise.all(
    episodeEntries.map(({ card }) => loadEpisodeByLocation(card.showId, card.folder)),
  );
  return episodes.filter((episode): episode is Episode => episode !== undefined);
});

export async function getShows(): Promise<ShowSummary[]> {
  return (await loadCatalog()).shows;
}

export async function getEpisodes(): Promise<Episode[]> {
  return loadAllEpisodes();
}

export async function getEpisode(showId: string, folder: string): Promise<Episode | undefined> {
  return loadEpisodeByLocation(showId, folder);
}

export async function getShow(showId: string): Promise<ShowSummary | undefined> {
  return (await getShows()).find((show) => show.id === showId);
}

export async function getEpisodeCards(showId?: string): Promise<EpisodeCard[]> {
  const { episodeEntries } = await loadCatalog();
  const cards = episodeEntries.map((entry) => entry.card);
  return showId ? cards.filter((episode) => episode.showId === showId) : cards;
}

function snippetAround(text: string, query: string, radius = 58): string {
  const normalizedText = text.replace(/\s+/gu, " ").trim();
  const index = normalizedText.toLocaleLowerCase("zh-CN").indexOf(query.toLocaleLowerCase("zh-CN"));
  if (index < 0) return normalizedText.slice(0, radius * 2);
  const start = Math.max(0, index - radius);
  const end = Math.min(normalizedText.length, index + query.length + radius);
  return `${start > 0 ? "…" : ""}${normalizedText.slice(start, end)}${end < normalizedText.length ? "…" : ""}`;
}

export async function searchContent(rawQuery: string): Promise<SearchResult[]> {
  const query = rawQuery.trim();
  if (!query) return [];
  const lowerQuery = query.toLocaleLowerCase("zh-CN");
  const results: SearchResult[] = [];

  for (const episode of await getEpisodes()) {
    const episodeHaystack = [
      episode.title,
      episode.navigationTitle,
      episode.catalogKeyword,
      episode.showTitle,
      ...episode.participants.flatMap((participant) => [participant.name, ...(participant.aliases ?? [])]),
    ].join(" ");
    if (episodeHaystack.toLocaleLowerCase("zh-CN").includes(lowerQuery)) {
      results.push({
        id: `${episode.id}:episode`,
        title: episode.navigationTitle,
        showTitle: episode.showTitle,
        section: "单集",
        snippet: snippetAround(episodeHaystack, query),
        href: episode.href,
        score: episode.title.toLocaleLowerCase("zh-CN").includes(lowerQuery) ? 90 : 70,
      });
    }

    if (episode.summaryRaw.toLocaleLowerCase("zh-CN").includes(lowerQuery)) {
      results.push({
        id: `${episode.id}:summary`,
        title: episode.navigationTitle,
        showTitle: episode.showTitle,
        section: "总结",
        snippet: snippetAround(episode.summaryRaw.replace(/[#*`>\[\]]/gu, ""), query),
        href: episode.href,
        score: 60,
      });
    }

    const transcriptMatches = episode.transcriptSegments
      .filter((segment) => segment.text.toLocaleLowerCase("zh-CN").includes(lowerQuery))
      .slice(0, 3);
    for (const segment of transcriptMatches) {
      results.push({
        id: `${episode.id}:${segment.id}`,
        title: episode.navigationTitle,
        showTitle: episode.showTitle,
        section: "逐字稿",
        snippet: snippetAround(segment.text, query),
        href: getTranscriptHref(episode.href, segment.id),
        timestamp: segment.timestamp,
        score: 50,
      });
    }

    const translationMatches = episode.bilingualTranscript?.segments
      .filter((segment) => segment.translationText.toLocaleLowerCase("zh-CN").includes(lowerQuery))
      .slice(0, 3) ?? [];
    for (const segment of translationMatches) {
      results.push({
        id: `${episode.id}:translation:${segment.id}`,
        title: episode.navigationTitle,
        showTitle: episode.showTitle,
        section: "译稿",
        snippet: snippetAround(segment.translationText, query),
        href: getTranscriptHref(episode.href, segment.id),
        timestamp: segment.timestamp,
        score: 49,
      });
    }
  }

  return results
    .sort((a, b) => b.score - a.score || a.title.localeCompare(b.title, "zh-CN"))
    .slice(0, 24);
}

export function findRelatedSegments(episode: Episode, targetTimestamp?: string): TranscriptSegment[] {
  const requestedSeconds = targetTimestamp
    ? timestampToSeconds(targetTimestamp)
    : Math.round(episode.durationMs / 1000 / 3);
  const targetIndex = episode.transcriptSegments.findIndex(
    (segment) => segment.seconds >= requestedSeconds,
  );
  const safeIndex = targetIndex < 0 ? episode.transcriptSegments.length - 1 : targetIndex;
  return episode.transcriptSegments.slice(Math.max(0, safeIndex - 2), safeIndex + 3);
}
