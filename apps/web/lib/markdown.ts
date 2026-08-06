import rehypeSlug from "rehype-slug";
import rehypeStringify from "rehype-stringify";
import remarkGfm from "remark-gfm";
import remarkParse from "remark-parse";
import remarkRehype from "remark-rehype";
import { unified } from "unified";
import GithubSlugger from "github-slugger";
import { findNearestTranscriptSegment, timestampToId } from "@/lib/content";
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
      return `[${timestamp}](${episodeHref}?view=transcript#${nearest?.id ?? timestampToId(timestamp)})`;
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
