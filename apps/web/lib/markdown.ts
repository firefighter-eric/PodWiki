import rehypeSlug from "rehype-slug";
import rehypeSanitize from "rehype-sanitize";
import rehypeStringify from "rehype-stringify";
import remarkGfm from "remark-gfm";
import remarkParse from "remark-parse";
import remarkRehype from "remark-rehype";
import { unified } from "unified";
import GithubSlugger from "github-slugger";
import { findNearestTranscriptSegment, timestampToId } from "@/lib/content";
import { getTranscriptHref } from "@/lib/reader-routes";
import type { TranscriptSegment } from "@/lib/types";

function linkTimestampReferences(
  markdown: string,
  episodeHref: string,
  transcriptSegments?: TranscriptSegment[],
): string {
  return markdown.replace(
    /\[(\d{2}:\d{2}:\d{2})\](?!\()/gu,
    (_match, timestamp: string) => {
      const nearest = transcriptSegments
        ? findNearestTranscriptSegment(transcriptSegments, timestamp)
        : undefined;
      return `[${timestamp}](${getTranscriptHref(
        episodeHref,
        nearest?.id ?? timestampToId(timestamp),
      )})`;
    },
  );
}

export async function markdownToHtml(
  markdown: string,
  episodeHref: string,
  transcriptSegments?: TranscriptSegment[],
): Promise<string> {
  const linkedMarkdown = linkTimestampReferences(markdown, episodeHref, transcriptSegments);
  const file = await unified()
    .use(remarkParse)
    .use(remarkGfm)
    .use(remarkRehype)
    .use(rehypeSlug)
    .use(rehypeSanitize)
    .use(rehypeStringify)
    .process(linkedMarkdown);
  return String(file);
}

export function getMarkdownSection(markdown: string, heading: string): string {
  const escapedHeading = heading.replace(/[.*+?^${}()|[\]\\]/gu, "\\$&");
  const headingPattern = new RegExp(`^##\\s+${escapedHeading}\\s*$`, "mu");
  const headingMatch = headingPattern.exec(markdown);
  if (!headingMatch) return "";

  const sectionStart = headingMatch.index + headingMatch[0].length;
  const remainder = markdown.slice(sectionStart);
  const nextHeading = /^##\s+/mu.exec(remainder);
  return remainder.slice(0, nextHeading?.index ?? remainder.length).trim();
}

export type CorePoint = {
  title: string;
  id: string;
  body: string;
};

export type CorePointTable = {
  columns: string[];
  rows: string[][];
};

function parseMarkdownTableRow(line: string): string[] {
  return line
    .trim()
    .replace(/^\|/u, "")
    .replace(/\|$/u, "")
    .split("|")
    .map((cell) => cell.trim());
}

export function getCorePointTable(markdown: string): CorePointTable | undefined {
  const section = getMarkdownSection(markdown, "核心观点");
  const overview = section.split(/^###\s+/mu)[0]?.trim() ?? "";
  const lines = overview.split("\n").map((line) => line.trim()).filter(Boolean);
  const tableStart = lines.findIndex((line) => line.startsWith("|") && line.endsWith("|"));
  if (tableStart < 0 || tableStart + 2 >= lines.length) return undefined;

  const columns = parseMarkdownTableRow(lines[tableStart]);
  const separators = parseMarkdownTableRow(lines[tableStart + 1]);
  if (
    columns.length < 2
    || separators.length !== columns.length
    || separators.some((cell) => !/^:?-{3,}:?$/u.test(cell))
  ) {
    return undefined;
  }

  const rows = lines
    .slice(tableStart + 2)
    .filter((line) => line.startsWith("|") && line.endsWith("|"))
    .map(parseMarkdownTableRow)
    .filter((row) => row.length === columns.length && row.some(Boolean));

  return rows.length > 0 ? { columns, rows } : undefined;
}

export function getCorePoints(markdown: string): CorePoint[] {
  const section = getMarkdownSection(markdown, "核心观点");
  const slugger = new GithubSlugger();
  return section
    .split(/^###\s+/mu)
    .slice(1)
    .map((block) => {
      const [titleLine = "", ...bodyLines] = block.split("\n");
      const title = titleLine.replace(/^\d+\.\s*/u, "").trim();
      return {
        title,
        id: slugger.slug(titleLine.trim()),
        body: bodyLines.join("\n").trim(),
      };
    })
    .filter((point) => point.title);
}

export function getExtendedSummary(markdown: string): string {
  const marker = /^##\s+5\s*分钟读完\s*$/mu;
  const index = markdown.search(marker);
  if (index < 0) return "";
  return markdown.slice(index).trim();
}

export function getFirstTimestamp(markdown: string): string | undefined {
  const timestamps = [...markdown.matchAll(/\[(\d{2}:\d{2}:\d{2})\]/gu)].map(
    (match) => match[1],
  );
  return timestamps.find((timestamp) => timestamp >= "00:20:00") ?? timestamps[0];
}
