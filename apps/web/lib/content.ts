import "server-only";
import { cache } from "react";
import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import matter from "gray-matter";
import { z } from "zod";
import { getReaderFacingSummary } from "@/lib/reader-copy";
import { getTranscriptHref } from "@/lib/reader-routes";
import {
  createSearchContent,
  indexSearchText,
  toSearchSegment,
  type SearchEpisodeDocument,
} from "@/lib/search-core";
import type {
  BilingualTranscript,
  BilingualTranscriptSegment,
  Chapter,
  Episode,
  EpisodeCard,
  ShowSummary,
  TranscriptSegment,
  TranscriptTranslationMetadata,
} from "@/lib/types";

const yamlDateSchema = z.preprocess((value) => {
  if (!(value instanceof Date)) return value;
  const isoValue = value.toISOString();
  return isoValue.endsWith("T00:00:00.000Z") ? isoValue.slice(0, 10) : value;
}, z.iso.date());

const stableSlugSchema = z.string().regex(/^[a-z0-9]+(?:-[a-z0-9]+)*$/u);
const sha256Schema = z.string().regex(/^[0-9a-f]{64}$/u);
const xiaoyuzhouIdSchema = z.string().regex(/^[0-9a-f]{24}$/u);

const participantAffiliationSchema = z
  .object({
    organization: z.string().min(1),
    title: z.string().min(1).optional(),
    status: z.enum(["current", "former"]),
  })
  .strict();

const participantEducationSchema = z
  .object({
    institution: z.string().min(1),
    credential: z.string().min(1).optional(),
    field: z.string().min(1).optional(),
  })
  .strict();

const participantProfileSchema = z
  .object({
    headline: z.string().min(1),
    bio: z.string().min(1).optional(),
    affiliations: z.array(participantAffiliationSchema).optional().default([]),
    education: z.array(participantEducationSchema).optional().default([]),
    checked_at: yamlDateSchema,
  })
  .strict()
  .transform(({ checked_at, ...profile }) => ({
    ...profile,
    checkedAt: checked_at,
  }));

const participantSchema = z
  .object({
    id: stableSlugSchema,
    name: z.string().min(1),
    role: z.enum(["guest", "participant", "host"]),
    aliases: z.array(z.string().min(1)).optional(),
    profile: participantProfileSchema.optional(),
  })
  .strict();

const sourceIdentifiersSchema = z
  .object({
    aid: z.string().regex(/^[1-9]\d*$/u).optional(),
    apple_podcasts_id: z.string().min(1).optional(),
    bvid: z.string().regex(/^BV[0-9A-Za-z]+$/u).optional(),
    cid: z.string().regex(/^[1-9]\d*$/u).optional(),
    channel_id: z.string().regex(/^UC[A-Za-z0-9_-]{22}$/u).optional(),
    eid: xiaoyuzhouIdSchema.optional(),
    episode_id: z.string().min(1).optional(),
    episode_number: z.string().min(1).optional(),
    feed_url: z.url().optional(),
    guid: z.string().min(1).optional(),
    media_id: z.string().regex(/^[0-9a-f]{24}\/[^/]+\.m4a$/u).optional(),
    mid: z.string().regex(/^[1-9]\d*$/u).optional(),
    page: z.number().int().positive().optional(),
    page_id: z.string().min(1).optional(),
    pid: xiaoyuzhouIdSchema.optional(),
    playlist_id: z.string().regex(/^[A-Za-z0-9_-]{10,64}$/u).optional(),
    rss_guid: z.string().min(1).optional(),
    show_id: z.string().min(1).optional(),
    video_id: z.string().regex(/^[A-Za-z0-9_-]{11}$/u).optional(),
  })
  .strict();

const sourceSchema = z
  .object({
    platform: z.enum([
      "apple-podcasts",
      "bilibili",
      "rss",
      "website",
      "xiaoyuzhou",
      "youtube",
    ]),
    kind: z.enum([
      "audio",
      "channel",
      "episode",
      "feed",
      "feed-item",
      "podcast",
      "playlist",
      "show",
      "video",
      "video-channel",
    ]),
    title: z.string().min(1).optional(),
    external_id: z.union([z.string().min(1), z.number()]).optional(),
    url: z.url().refine((url) => url.startsWith("https://"), "source URL must use HTTPS"),
    preferred: z.boolean().optional(),
    identifiers: sourceIdentifiersSchema.optional(),
  })
  .strict()
  .superRefine((source, context) => {
    const bilibiliVideo = /^https:\/\/www\.bilibili\.com\/video\/(BV[0-9A-Za-z]+)\/$/u
      .exec(source.url);
    if (source.platform === "bilibili" && source.kind === "video" && !bilibiliVideo) {
      context.addIssue({
        code: "custom",
        path: ["url"],
        message: "Bilibili video URL must be canonical",
      });
    }
    if (bilibiliVideo) {
      if (source.platform !== "bilibili") {
        context.addIssue({
          code: "custom",
          path: ["platform"],
          message: "Bilibili video URL must use platform bilibili",
        });
      }
      if (source.kind !== "video") {
        context.addIssue({
          code: "custom",
          path: ["kind"],
          message: "Bilibili video source must use kind video",
        });
      }
      const identifiers = source.identifiers;
      for (const field of ["bvid", "aid", "cid", "page"] as const) {
        if (identifiers?.[field] === undefined) {
          context.addIssue({
            code: "custom",
            path: ["identifiers", field],
            message: `Bilibili video source requires identifiers.${field}`,
          });
        }
      }
      if (bilibiliVideo[1] !== identifiers?.bvid) {
        context.addIssue({
          code: "custom",
          path: ["url"],
          message: "Bilibili video URL must be canonical and match identifiers.bvid",
        });
      }
    }

    const xiaoyuzhouEpisode = /^https:\/\/www\.xiaoyuzhoufm\.com\/episode\/([0-9a-f]{24})$/u
      .exec(source.url);
    if (source.platform === "xiaoyuzhou" && source.kind === "episode" && !xiaoyuzhouEpisode) {
      context.addIssue({
        code: "custom",
        path: ["url"],
        message: "Xiaoyuzhou episode URL must be canonical",
      });
    }
    if (xiaoyuzhouEpisode) {
      if (source.platform !== "xiaoyuzhou") {
        context.addIssue({
          code: "custom",
          path: ["platform"],
          message: "Xiaoyuzhou episode URL must use platform xiaoyuzhou",
        });
      }
      if (source.kind !== "episode") {
        context.addIssue({
          code: "custom",
          path: ["kind"],
          message: "Xiaoyuzhou episode source must use kind episode",
        });
      }
      const identifiers = source.identifiers;
      for (const field of ["eid", "pid", "media_id"] as const) {
        if (identifiers?.[field] === undefined) {
          context.addIssue({
            code: "custom",
            path: ["identifiers", field],
            message: `Xiaoyuzhou episode source requires identifiers.${field}`,
          });
        }
      }
      const urlEid = xiaoyuzhouEpisode[1];
      if (!urlEid || urlEid !== identifiers?.eid) {
        context.addIssue({
          code: "custom",
          path: ["url"],
          message: "Xiaoyuzhou episode URL must be canonical and match identifiers.eid",
        });
      }
      if (identifiers?.media_id && identifiers.pid) {
        if (!identifiers.media_id.startsWith(`${identifiers.pid}/`)) {
          context.addIssue({
            code: "custom",
            path: ["identifiers", "media_id"],
            message: "Xiaoyuzhou identifiers.media_id must start with identifiers.pid",
          });
        }
      }
    }

    const youtubeVideo = /^https:\/\/www\.youtube\.com\/watch\?v=([A-Za-z0-9_-]{11})$/u
      .exec(source.url);
    if (source.platform === "youtube" && source.kind === "video" && !youtubeVideo) {
      context.addIssue({
        code: "custom",
        path: ["url"],
        message: "YouTube video URL must be canonical",
      });
    }
    if (youtubeVideo) {
      if (source.platform !== "youtube" || source.kind !== "video") {
        context.addIssue({
          code: "custom",
          path: ["url"],
          message: "YouTube video URL must use platform youtube and kind video",
        });
      }
      for (const field of ["video_id", "channel_id"] as const) {
        if (source.identifiers?.[field] === undefined) {
          context.addIssue({
            code: "custom",
            path: ["identifiers", field],
            message: `YouTube video source requires identifiers.${field}`,
          });
        }
      }
      if (youtubeVideo[1] !== source.identifiers?.video_id) {
        context.addIssue({
          code: "custom",
          path: ["url"],
          message: "YouTube video URL must match identifiers.video_id",
        });
      }
    }

    const youtubePlaylist = /^https:\/\/www\.youtube\.com\/playlist\?list=([A-Za-z0-9_-]{10,64})$/u
      .exec(source.url);
    if (source.platform === "youtube" && source.kind === "playlist" && !youtubePlaylist) {
      context.addIssue({
        code: "custom",
        path: ["url"],
        message: "YouTube playlist URL must be canonical",
      });
    }
    if (youtubePlaylist) {
      if (source.platform !== "youtube" || source.kind !== "playlist") {
        context.addIssue({
          code: "custom",
          path: ["url"],
          message: "YouTube playlist URL must use platform youtube and kind playlist",
        });
      }
      for (const field of ["playlist_id", "channel_id"] as const) {
        if (source.identifiers?.[field] === undefined) {
          context.addIssue({
            code: "custom",
            path: ["identifiers", field],
            message: `YouTube playlist source requires identifiers.${field}`,
          });
        }
      }
      if (youtubePlaylist[1] !== source.identifiers?.playlist_id) {
        context.addIssue({
          code: "custom",
          path: ["url"],
          message: "YouTube playlist URL must match identifiers.playlist_id",
        });
      }
    }
  });

const transcriptProvenanceSchema = z
  .object({
    path: z.string().min(1),
    engine: z.string().min(1).optional(),
    model: z.string().min(1).optional(),
    selection_status: z.enum(["selected", "superseded"]).optional(),
    sha256: sha256Schema.optional(),
  });

const summarySourceTranscriptSchema = z
  .object({
    path: z.string().min(1),
    engine: z.string().min(1),
    model: z.string().min(1),
    selection_status: z.enum(["selected", "superseded"]),
    sha256: sha256Schema,
  })
  .strict();

const transcriptTranslationSchema = z
  .object({
    language: z.literal("zh-CN"),
    path: z.literal("transcript.zh-CN.md"),
    source_language: z.literal("en"),
    source_path: z.literal("transcript.en.md"),
    alignment: z.literal("segment"),
    status: z.enum(["machine", "edited", "reviewed"]),
    generated_at: z.union([z.string().datetime({ offset: true }), z.date()]),
    source_sha256: sha256Schema,
    sha256: sha256Schema,
  })
  .strict();

const episodeTranscriptSchema = transcriptProvenanceSchema.extend({
  translations: z.array(transcriptTranslationSchema).optional().default([]),
});

function isQwenAsr(engine: string, model: string): boolean {
  return engine.includes("qwen") || model.includes("Qwen3-ASR");
}

const asrRunSchema = z
  .object({
    id: z.string().min(1),
    selection_status: z.enum(["candidate", "selected", "superseded", "rejected"]),
    engine: z.string().min(1),
    model: z.string().min(1),
    aligner: z.string().min(1).optional(),
    generated_at: z.union([z.string().datetime({ offset: true }), z.date()]).optional(),
    artifacts: z
      .object({
        raw: z.string().min(1),
        aligned: z.string().min(1).optional(),
        refined: z.string().min(1),
        transcript: z.string().min(1),
      })
      .strict(),
    options: z.record(z.string(), z.unknown()).optional(),
    quality: z.record(z.string(), z.unknown()).optional(),
    performance: z.record(z.string(), z.unknown()).optional(),
    benchmark: z.unknown().optional(),
  })
  .strict()
  .superRefine((run, context) => {
    if (isQwenAsr(run.engine, run.model) && !run.artifacts.aligned) {
      context.addIssue({
        code: "custom",
        path: ["artifacts", "aligned"],
        message: "Qwen ASR runs require an aligned artifact",
      });
    }
  });

const workflowSchema = z.object({
  metadata: z.enum(["draft", "verified"]),
  summary: z.enum(["empty", "outline", "draft", "reviewed"]),
  transcript: z.enum([
    "not-started",
    "source-acquired",
    "machine",
    "edited",
    "reviewed",
    "blocked",
  ]),
}).strict();

type EpisodeWorkflow = z.infer<typeof workflowSchema>;

const webSummaryStatuses = new Set<EpisodeWorkflow["summary"]>(["draft", "reviewed"]);
const webTranscriptStatuses = new Set<EpisodeWorkflow["transcript"]>([
  "machine",
  "edited",
  "reviewed",
]);

export function isEpisodeWebPublishable(workflow: EpisodeWorkflow): boolean {
  return workflow.metadata === "verified"
    && webSummaryStatuses.has(workflow.summary)
    && webTranscriptStatuses.has(workflow.transcript);
}

function getExpectedNavigationPerson(
  participants: z.infer<typeof participantSchema>[],
): string | undefined {
  for (const role of ["guest", "participant", "host"] as const) {
    const names = participants
      .filter((participant) => participant.role === role)
      .map((participant) => participant.name);
    if (names.length > 0) return names.join("、");
  }
  return undefined;
}

const episodeSchema = z
  .object({
    schema_version: z.literal(1),
    kind: z.literal("episode"),
    id: z.string().min(1),
    show_id: z.string().regex(/^[a-z0-9]+$/u),
    episode_key: stableSlugSchema,
    episode_number: z.number().int().positive().nullable(),
    release_type: z.enum(["regular", "special", "bonus"]),
    slug: stableSlugSchema,
    numbering: z.object({
      status: z.enum(["verified", "not-in-publisher-feed", "unknown"]),
      checked_at: yamlDateSchema,
      source: z.string().min(1),
      url: z.url().optional(),
      note: z.string().min(1).optional(),
    }).strict(),
    title: z.string().min(1),
    navigation_title: z.string().min(1).max(40),
    catalog_keyword: z.string().min(1).max(20).refine(
      (value) => value === value.trim(),
      "catalog_keyword must not have leading or trailing whitespace",
    ),
    published_at: z.string().datetime({ offset: true }),
    duration_ms: z.number().int().positive(),
    language: z.string().min(1),
    participants: z.array(participantSchema).min(1),
    sources: z.array(sourceSchema).min(1).refine(
      (sources) => sources.filter((source) => source.preferred === true).length === 1,
      "sources must contain exactly one preferred source",
    ),
    workflow: workflowSchema,
    summary: z
      .object({
        path: z.string().min(1),
        language: z.string().min(1).optional(),
        source_transcript: summarySourceTranscriptSchema.nullable().optional(),
      })
      .strict(),
    transcript: episodeTranscriptSchema,
    asr_runs: z.array(asrRunSchema).optional().default([]),
  })
  .superRefine((value, context) => {
    const expectedId = `${value.show_id}:${value.episode_key}`;
    if (value.id !== expectedId) {
      context.addIssue({
        code: "custom",
        path: ["id"],
        message: `episode id must equal ${expectedId}`,
      });
    }
    const participantIds = new Set<string>();
    value.participants.forEach((participant, index) => {
      if (participantIds.has(participant.id)) {
        context.addIssue({
          code: "custom",
          path: ["participants", index, "id"],
          message: `participant id must be unique within the episode: ${participant.id}`,
        });
      }
      participantIds.add(participant.id);
    });
    const expectedNavigationPerson = getExpectedNavigationPerson(value.participants);
    const navigationPerson = value.navigation_title.split(" · ", 1)[0];
    if (expectedNavigationPerson && navigationPerson !== expectedNavigationPerson) {
      context.addIssue({
        code: "custom",
        path: ["navigation_title"],
        message: `navigation_title person must equal ${expectedNavigationPerson}`,
      });
    }
    if (value.episode_number === null && value.numbering.status === "verified") {
      context.addIssue({
        code: "custom",
        path: ["numbering", "status"],
        message: "numbering.status cannot be verified when episode_number is null",
      });
    }
    if (value.episode_number !== null && value.numbering.status !== "verified") {
      context.addIssue({
        code: "custom",
        path: ["numbering", "status"],
        message: "numbering.status must be verified when episode_number is present",
      });
    }
    const youtubeVideoSource = value.sources.find(
      (source) => source.platform === "youtube" && source.kind === "video",
    );
    if (value.episode_number === null && youtubeVideoSource?.identifiers?.video_id) {
      const encodedVideoId = Array.from(youtubeVideoSource.identifiers.video_id)
        .map((character) => character.charCodeAt(0).toString(16).padStart(2, "0"))
        .join("");
      const expectedKey = `youtube-${encodedVideoId}`;
      if (value.episode_key !== expectedKey) {
        context.addIssue({
          code: "custom",
          path: ["episode_key"],
          message: `unnumbered YouTube episode_key must equal ${expectedKey}`,
        });
      }
    } else if (value.episode_key.startsWith("youtube-")) {
      context.addIssue({
        code: "custom",
        path: ["episode_key"],
        message: "YouTube episode_key requires a YouTube video source",
      });
    }
    if (isEpisodeWebPublishable(value.workflow) && !value.summary.source_transcript) {
      context.addIssue({
        code: "custom",
        path: ["summary", "source_transcript"],
        message: "publishable episodes require complete summary.source_transcript provenance",
      });
    }
    const selectedRuns = value.asr_runs.filter((run) => run.selection_status === "selected");
    if (isEpisodeWebPublishable(value.workflow) && selectedRuns.length !== 1) {
      context.addIssue({
        code: "custom",
        path: ["asr_runs"],
        message: "publishable episodes require exactly one selected ASR run",
      });
    }
    const selectedRun = selectedRuns[0];
    if (selectedRun) {
      if (selectedRun.engine !== value.transcript.engine) {
        context.addIssue({
          code: "custom",
          path: ["transcript", "engine"],
          message: "transcript.engine must match the selected ASR run",
        });
      }
      if (selectedRun.model !== value.transcript.model) {
        context.addIssue({
          code: "custom",
          path: ["transcript", "model"],
          message: "transcript.model must match the selected ASR run",
        });
      }
    }
    const summarySource = value.summary.source_transcript;
    if (summarySource?.selection_status === "selected" && summarySource.path !== value.transcript.path) {
      context.addIssue({
        code: "custom",
        path: ["summary", "source_transcript", "path"],
        message: "selected summary.source_transcript must match transcript.path",
      });
    }
    if (summarySource?.selection_status === "superseded" && summarySource.path === value.transcript.path) {
      context.addIssue({
        code: "custom",
        path: ["summary", "source_transcript", "path"],
        message: "superseded summary.source_transcript must differ from transcript.path",
      });
    }
    if (summarySource) {
      const matchingRuns = value.asr_runs.filter((run) => (
        run.engine === summarySource.engine
        && run.model === summarySource.model
        && run.selection_status === summarySource.selection_status
      ));
      if (matchingRuns.length !== 1) {
        context.addIssue({
          code: "custom",
          path: ["summary", "source_transcript"],
          message: "summary.source_transcript must match exactly one ASR run",
        });
      }
      if (
        summarySource.selection_status === "superseded"
        && matchingRuns[0]?.artifacts.transcript !== summarySource.path
      ) {
        context.addIssue({
          code: "custom",
          path: ["summary", "source_transcript", "path"],
          message: "superseded summary source must match its ASR run transcript artifact",
        });
      }
    }
  });

const showSchema = z
  .object({
    schema_version: z.literal(1),
    kind: z.literal("show"),
    id: z.string().regex(/^[a-z0-9]+$/u),
    title: z.string().min(1),
    aliases: z.array(z.string().min(1)),
    language: z.string().min(1),
    status: z.enum(["active", "inactive", "archived"]),
    formats: z.array(z.string().min(1)).min(1),
    topics: z.array(z.string().min(1)).min(1),
    sources: z.array(sourceSchema).min(1).refine(
      (sources) => sources.filter((source) => source.preferred === true).length === 1,
      "show sources must contain exactly one preferred source",
    ),
    last_verified_at: yamlDateSchema,
  })
  .strict();

const showOrder = [
  "zhangxiaojun",
  "sv101",
  "svvector",
  "latetalk",
  "luoyonghao",
  "moonuncle",
  "whynottv",
  "yiqitietalk",
];
const showOrderIndex = new Map(showOrder.map((id, index) => [id, index]));

export function compareShowOrder(
  left: Pick<ShowSummary, "id" | "title">,
  right: Pick<ShowSummary, "id" | "title">,
): number {
  const leftIndex = showOrderIndex.get(left.id);
  const rightIndex = showOrderIndex.get(right.id);
  if (leftIndex !== undefined || rightIndex !== undefined) {
    if (leftIndex === undefined) return 1;
    if (rightIndex === undefined) return -1;
    return leftIndex - rightIndex;
  }
  return left.title.localeCompare(right.title, "zh-CN") || left.id.localeCompare(right.id);
}

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

  if (fs.existsSync(resolvedPath)) {
    const realEpisodeRoot = fs.realpathSync.native(episodeRoot);
    const realResolvedPath = fs.realpathSync.native(resolvedPath);
    const realRelativeToEpisode = path.relative(realEpisodeRoot, realResolvedPath);
    if (
      realRelativeToEpisode === ""
      || realRelativeToEpisode.startsWith(`..${path.sep}`)
      || path.isAbsolute(realRelativeToEpisode)
    ) {
      throw new Error(`${label} must resolve inside the episode directory: ${relativePath}`);
    }
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
    sha256: value.sha256,
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
  const match = /^(\d{2}):([0-5]\d):([0-5]\d)$/u.exec(timestamp);
  if (!match) {
    throw new Error(`Invalid transcript timestamp: ${timestamp}`);
  }
  return Number(match[1]) * 3600 + Number(match[2]) * 60 + Number(match[3]);
}

export function timestampToId(timestamp: string): string {
  timestampToSeconds(timestamp);
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
  const linePattern = /^\[(\d{2}:[0-5]\d:[0-5]\d)\]\s+(.+?)\s{0,2}$/gmu;

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
    /^-\s+(\d{2}:[0-5]\d:[0-5]\d)\s+[—–-]\s+(.+)$/gmu,
    /^-\s+(?:\*\*)?\[(\d{2}:[0-5]\d:[0-5]\d)\](?:[^*]*\*\*)?\s*[—–-]?\s*(.+)$/gmu,
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
  searchAssets: {
    episodeRoot: string;
    episodeTitle: string;
    episodeLanguage: string;
    participants: z.infer<typeof participantSchema>[];
    summaryRaw: string;
    transcriptPath: string;
    transcriptRelativePath: string;
    transcriptTranslations: z.infer<typeof transcriptTranslationSchema>[];
  };
};

type ContentCatalog = {
  shows: ShowSummary[];
  episodeEntries: EpisodeCatalogEntry[];
};

export function compareEpisodePublicationOrder(
  publishedAtA: string,
  hrefA: string,
  publishedAtB: string,
  hrefB: string,
): number {
  return Date.parse(publishedAtB) - Date.parse(publishedAtA) || hrefA.localeCompare(hrefB);
}

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

function assertEpisodeDirectoryContract(
  metadata: z.infer<typeof episodeSchema>,
  folder: string,
  label: string,
) {
  if (metadata.slug !== folder) {
    throw new Error(
      `${label} slug ${JSON.stringify(metadata.slug)} does not match directory ${JSON.stringify(folder)}`,
    );
  }
  if (folder !== metadata.episode_key && !folder.startsWith(`${metadata.episode_key}-`)) {
    throw new Error(
      `${label} directory ${JSON.stringify(folder)} must start with episode_key ${JSON.stringify(metadata.episode_key)}`,
    );
  }
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
  episodeRoot,
  transcriptPath,
}: {
  metadata: z.infer<typeof episodeSchema>;
  showTitle: string;
  folder: string;
  summaryRaw: string;
  episodeRoot: string;
  transcriptPath: string;
}): EpisodeCatalogEntry {
  const publishedAt = metadata.published_at;
  const editorialTitle = extractMarkdownTitle(summaryRaw) ?? metadata.title;
  const normalizedTitle = normalizeTitle(editorialTitle);

  return {
    publishedAt,
    searchAssets: {
      episodeRoot,
      episodeTitle: metadata.title,
      episodeLanguage: metadata.language,
      participants: metadata.participants,
      summaryRaw,
      transcriptPath,
      transcriptRelativePath: metadata.transcript.path,
      transcriptTranslations: metadata.transcript.translations,
    },
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
      participants: metadata.participants,
      guests: metadata.participants.filter((participant) => participant.role === "guest"),
      hosts: metadata.participants.filter((participant) => participant.role === "host"),
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
  const episodeLocations = new Map<string, string>();
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
      assertEpisodeDirectoryContract(metadata, folder, `Episode ${metadata.id}`);
      if (metadata.show_id !== showId) {
        throw new Error(
          `Episode ${metadata.id} declares show ${metadata.show_id} but is stored under ${showId}`,
        );
      }
      const previousLocation = episodeLocations.get(metadata.id);
      if (previousLocation) {
        throw new Error(
          `Duplicate episode id ${metadata.id}: ${previousLocation} and ${readmePath}`,
        );
      }
      episodeLocations.set(metadata.id, readmePath);

      if (!isEpisodeWebPublishable(metadata.workflow)) continue;

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
      const summarySource = metadata.summary.source_transcript;
      if (!summarySource) {
        throw new Error(`Missing summary source transcript provenance for ${metadata.id}`);
      }
      const summarySourceTranscriptPath = resolveEpisodeAsset(
        episodeRoot,
        summarySource.path,
        `${metadata.id} summary source transcript path`,
      );
      if (!fs.existsSync(summaryPath)) {
        throw new Error(`Missing summary for ${metadata.id}: ${summaryPath}`);
      }
      if (!fs.existsSync(transcriptPath)) {
        throw new Error(`Missing transcript for ${metadata.id}: ${transcriptPath}`);
      }
      if (!fs.existsSync(summarySourceTranscriptPath)) {
        throw new Error(
          `Missing summary source transcript for ${metadata.id}: ${summarySourceTranscriptPath}`,
        );
      }

      const summary = readMarkdown(summaryPath);
      episodeEntries.push(episodeCardFromMetadata({
        metadata,
        showTitle: currentShow.title,
        folder,
        summaryRaw: summary.content,
        episodeRoot,
        transcriptPath,
      }));
    }
  }

  episodeEntries.sort((a, b) => compareEpisodePublicationOrder(
    a.publishedAt,
    a.card.href,
    b.publishedAt,
    b.card.href,
  ));

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
    .sort(compareShowOrder);

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
  assertEpisodeDirectoryContract(metadata, folder, `Episode ${metadata.id}`);
  if (metadata.show_id !== showId) return undefined;
  if (!isEpisodeWebPublishable(metadata.workflow)) return undefined;

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
  const summarySource = metadata.summary.source_transcript;
  if (!summarySource) {
    throw new Error(`Missing summary source transcript provenance for ${metadata.id}`);
  }
  const summarySourceTranscriptPath = resolveEpisodeAsset(
    episodeRoot,
    summarySource.path,
    `${metadata.id} summary source transcript path`,
  );
  // Runtime search assets are explicitly included by next.config.ts.
  if (!fs.existsSync(/* turbopackIgnore: true */ summaryPath)) {
    throw new Error(`Missing summary for ${metadata.id}: ${summaryPath}`);
  }
  if (!fs.existsSync(/* turbopackIgnore: true */ transcriptPath)) {
    throw new Error(`Missing transcript for ${metadata.id}: ${transcriptPath}`);
  }
  if (!fs.existsSync(/* turbopackIgnore: true */ summarySourceTranscriptPath)) {
    throw new Error(
      `Missing summary source transcript for ${metadata.id}: ${summarySourceTranscriptPath}`,
    );
  }

  const summary = readMarkdown(summaryPath);
  const transcript = readMarkdown(transcriptPath);
  const summarySourceTranscript = summarySourceTranscriptPath === transcriptPath
    ? transcript
    : readMarkdown(summarySourceTranscriptPath);
  if (summarySourceTranscript.sha256 !== summarySource.sha256) {
    throw new Error(
      `Summary source transcript SHA-256 mismatch for ${metadata.id}: ${summarySource.path}`,
    );
  }
  const sourceTranscriptTimestamps = new Set(
    [...summarySourceTranscript.content.matchAll(/^\[(\d{2}:[0-5]\d:[0-5]\d)\]/gmu)]
      .map((match) => match[1]),
  );
  for (const match of summary.content.matchAll(/\[(\d{2}:[0-5]\d:[0-5]\d)\]/gu)) {
    if (!sourceTranscriptTimestamps.has(match[1])) {
      throw new Error(
        `Summary timestamp ${match[1]} for ${metadata.id} is missing from ${summarySource.path}`,
      );
    }
  }
  const selectedRun = metadata.asr_runs.find((run) => run.selection_status === "selected");
  if (selectedRun) {
    const requiredArtifacts = ["raw", "refined", "transcript"] as const;
    const artifactNames = isQwenAsr(selectedRun.engine, selectedRun.model)
      ? [...requiredArtifacts, "aligned"] as const
      : requiredArtifacts;
    for (const artifactName of artifactNames) {
      const artifactPathValue = selectedRun.artifacts[artifactName];
      if (!artifactPathValue) {
        throw new Error(`Selected ASR run for ${metadata.id} is missing ${artifactName}`);
      }
      const artifactPath = resolveEpisodeAsset(
        episodeRoot,
        artifactPathValue,
        `${metadata.id} selected ASR ${artifactName} artifact`,
      );
      if (!fs.existsSync(/* turbopackIgnore: true */ artifactPath)) {
        throw new Error(
          `Missing selected ASR ${artifactName} artifact for ${metadata.id}: ${artifactPath}`,
        );
      }
    }
    const selectedTranscriptPath = resolveEpisodeAsset(
      episodeRoot,
      selectedRun.artifacts.transcript,
      `${metadata.id} selected ASR transcript artifact`,
    );
    if (readMarkdown(selectedTranscriptPath).sha256 !== transcript.sha256) {
      throw new Error(
        `Selected ASR transcript artifact is not byte-identical to transcript.path for ${metadata.id}`,
      );
    }
  }
  const publishedAt = metadata.published_at;
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

let searchDocumentsPromise: Promise<SearchEpisodeDocument[]> | undefined;

function getParticipantSearchTerms(
  participant: z.infer<typeof participantSchema>,
): string[] {
  const profile = participant.profile;
  return [
    participant.name,
    ...(participant.aliases ?? []),
    ...(profile ? [
      profile.headline,
      ...(profile.bio ? [profile.bio] : []),
      ...profile.affiliations.flatMap((affiliation) => [
        affiliation.organization,
        ...(affiliation.title ? [affiliation.title] : []),
      ]),
      ...profile.education.flatMap((education) => [
        education.institution,
        ...(education.credential ? [education.credential] : []),
        ...(education.field ? [education.field] : []),
      ]),
    ] : []),
  ];
}

async function buildSearchDocuments(): Promise<SearchEpisodeDocument[]> {
  const { episodeEntries } = await loadCatalog();

  return episodeEntries.map(({ card, searchAssets }) => {
    const transcript = readMarkdown(searchAssets.transcriptPath);
    const transcriptSegments = parseTranscript(transcript.content);
    const { bilingualTranscript } = loadTranscriptTranslations({
      episodeRoot: searchAssets.episodeRoot,
      episodeId: card.id,
      episodeLanguage: searchAssets.episodeLanguage,
      sourcePath: searchAssets.transcriptRelativePath,
      sourceSha256: transcript.sha256,
      sourceContent: transcript.content,
      sourceSegments: transcriptSegments,
      values: searchAssets.transcriptTranslations,
    });
    const episodeHaystack = [
      searchAssets.episodeTitle,
      card.navigationTitle,
      card.catalogKeyword,
      card.showTitle,
      ...searchAssets.participants.flatMap(getParticipantSearchTerms),
    ].join(" ");
    const readerSummary = getReaderFacingSummary(searchAssets.summaryRaw);
    const summarySnippet = readerSummary.replace(/[#*`>\[\]]/gu, "");

    return {
      id: card.id,
      title: card.navigationTitle,
      titleNormalized: searchAssets.episodeTitle.toLocaleLowerCase("zh-CN"),
      showTitle: card.showTitle,
      href: card.href,
      episodeHaystack: indexSearchText(episodeHaystack),
      summaryNormalized: readerSummary.toLocaleLowerCase("zh-CN"),
      summarySnippet: indexSearchText(summarySnippet),
      transcriptSegments: transcriptSegments.map(toSearchSegment),
      translationSegments: bilingualTranscript?.segments.map((segment) => ({
        id: segment.id,
        timestamp: segment.timestamp,
        content: indexSearchText(segment.translationText),
      })) ?? [],
    };
  });
}

export const buildSearchDocumentsForTesting = buildSearchDocuments;

function getSearchDocuments(): Promise<SearchEpisodeDocument[]> {
  if (!searchDocumentsPromise) {
    searchDocumentsPromise = buildSearchDocuments().catch((error: unknown) => {
      searchDocumentsPromise = undefined;
      throw error;
    });
  }
  return searchDocumentsPromise;
}

export const searchContent = createSearchContent(getSearchDocuments);

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
