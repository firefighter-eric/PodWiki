import "server-only";
import { cache } from "react";
import fs from "node:fs";
import path from "node:path";
import matter from "gray-matter";
import { z } from "zod";
import type {
  Chapter,
  Episode,
  EpisodeCard,
  SearchResult,
  ShowSummary,
  TranscriptSegment,
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

const episodeSchema = z
  .object({
    id: z.string(),
    show_id: z.string(),
    episode_key: z.union([z.string(), z.number()]).transform(String),
    episode_number: z.number().nullable().optional().default(null),
    slug: z.string().optional(),
    title: z.string(),
    published_at: z.union([z.string(), z.date()]),
    duration_ms: z.number(),
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
    transcript: transcriptProvenanceSchema,
  })
  .passthrough();

const showSchema = z
  .object({
    id: z.string(),
    title: z.string(),
  })
  .passthrough();

const showOrder = ["zhangxiaojun", "luoyonghao", "whynottv"];

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

function readMarkdown(filePath: string): { data: Record<string, unknown>; content: string } {
  const raw = fs.readFileSync(filePath, "utf8");
  const parsed = matter(raw);
  return { data: parsed.data, content: parsed.content.trim() };
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
        href: `${href}?view=transcript#${target?.id ?? timestampToId(timestamp)}`,
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
      href: `${href}?view=transcript#${firstSegment.id}`,
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

const loadContent = cache(async (): Promise<{ shows: ShowSummary[]; episodes: Episode[] }> => {
  const repositoryRoot = findRepositoryRoot();
  const showsRoot = path.join(repositoryRoot, "shows");
  const showDirectories = fs
    .readdirSync(showsRoot, { withFileTypes: true })
    .filter((entry) => entry.isDirectory() && fs.existsSync(path.join(showsRoot, entry.name, "README.md")));

  const showData = new Map<string, { title: string; description: string }>();
  for (const directory of showDirectories) {
    const parsed = readMarkdown(path.join(showsRoot, directory.name, "README.md"));
    const show = showSchema.parse(parsed.data);
    showData.set(show.id, {
      title: show.title,
      description: extractShowDescription(parsed.content),
    });
  }

  const episodes: Episode[] = [];
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
      const summaryPath = path.join(episodeRoot, metadata.summary.path);
      const transcriptPath = path.join(episodeRoot, metadata.transcript.path);
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
      const preferredSource = metadata.sources.find((source) => source.preferred) ?? metadata.sources[0];

      const transcriptSegments = parseTranscript(transcript.content);
      const episode: Episode = {
        id: metadata.id,
        showId: metadata.show_id,
        showTitle: currentShow.title,
        episodeKey: metadata.episode_key,
        episodeNumber: metadata.episode_number,
        folder,
        title: metadata.title,
        editorialTitle,
        displayTitle: normalizedTitle.displayTitle,
        subtitle: normalizedTitle.subtitle,
        publishedAt,
        publishedDate: publishedAt.slice(0, 10),
        durationMs: metadata.duration_ms,
        durationLabel: formatDuration(metadata.duration_ms),
        participants: metadata.participants,
        guests: metadata.participants.filter((participant) => participant.role === "guest"),
        hosts: metadata.participants.filter((participant) => participant.role === "host"),
        sources: metadata.sources,
        preferredSource,
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
        href,
      };
      episode.chapters = parseChapters(
        episode.readmeRaw,
        episode.summaryRaw,
        href,
        transcriptSegments,
      );
      episodes.push(episode);
    }
  }

  episodes.sort((a, b) => Date.parse(b.publishedAt) - Date.parse(a.publishedAt));

  const shows: ShowSummary[] = [...showData.entries()]
    .map(([id, data]) => {
      const showEpisodes = episodes.filter((episode) => episode.showId === id);
      return {
        id,
        title: data.title,
        shortTitle: showShortTitle(id, data.title),
        description: data.description,
        episodeCount: showEpisodes.length,
        href: `/shows/${id}`,
        latestEpisodeHref: showEpisodes[0]?.href ?? `/shows/${id}`,
      };
    })
    .sort((a, b) => showOrder.indexOf(a.id) - showOrder.indexOf(b.id));

  return { shows, episodes };
});

export async function getShows(): Promise<ShowSummary[]> {
  return (await loadContent()).shows;
}

export async function getEpisodes(): Promise<Episode[]> {
  return (await loadContent()).episodes;
}

export async function getEpisode(showId: string, folder: string): Promise<Episode | undefined> {
  return (await getEpisodes()).find(
    (episode) => episode.showId === showId && episode.folder === folder,
  );
}

export async function getShow(showId: string): Promise<ShowSummary | undefined> {
  return (await getShows()).find((show) => show.id === showId);
}

export async function getEpisodeCards(showId?: string): Promise<EpisodeCard[]> {
  const episodes = showId
    ? (await getEpisodes()).filter((episode) => episode.showId === showId)
    : await getEpisodes();
  return episodes.map((episode) => ({
    id: episode.id,
    showId: episode.showId,
    showTitle: episode.showTitle,
    episodeNumber: episode.episodeNumber,
    folder: episode.folder,
    title: episode.title,
    editorialTitle: episode.editorialTitle,
    displayTitle: episode.displayTitle,
    subtitle: episode.subtitle,
    publishedDate: episode.publishedDate,
    durationLabel: episode.durationLabel,
    guests: episode.guests,
    workflow: episode.workflow,
    href: episode.href,
  }));
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
      episode.showTitle,
      ...episode.participants.flatMap((participant) => [participant.name, ...(participant.aliases ?? [])]),
    ].join(" ");
    if (episodeHaystack.toLocaleLowerCase("zh-CN").includes(lowerQuery)) {
      results.push({
        id: `${episode.id}:episode`,
        title: episode.displayTitle,
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
        title: episode.displayTitle,
        showTitle: episode.showTitle,
        section: "总结",
        snippet: snippetAround(episode.summaryRaw.replace(/[#*`>\[\]]/gu, ""), query),
        href: `${episode.href}?view=summary`,
        score: 60,
      });
    }

    const transcriptMatches = episode.transcriptSegments
      .filter((segment) => segment.text.toLocaleLowerCase("zh-CN").includes(lowerQuery))
      .slice(0, 3);
    for (const segment of transcriptMatches) {
      results.push({
        id: `${episode.id}:${segment.id}`,
        title: episode.displayTitle,
        showTitle: episode.showTitle,
        section: "逐字稿",
        snippet: snippetAround(segment.text, query),
        href: `${episode.href}?view=transcript#${segment.id}`,
        timestamp: segment.timestamp,
        score: 50,
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
