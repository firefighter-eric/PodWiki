import fs from "node:fs";
import { createHash } from "node:crypto";
import os from "node:os";
import path from "node:path";
import { describe, expect, it, vi } from "vitest";
import {
  compareEpisodePublicationOrder,
  compareShowOrder,
  getEpisode,
  getEpisodeCards,
  getEpisodes,
  getShows,
  pairTranscriptSegments,
  searchContent,
  timestampToId,
  timestampToSeconds,
} from "@/lib/content";
import type { TranscriptSegment } from "@/lib/types";
import { getCorePointTable, getMarkdownSection } from "@/lib/markdown";

type ContentModule = typeof import("@/lib/content");

type FixtureWorkflow = {
  metadata: "draft" | "verified";
  summary: "empty" | "outline" | "draft" | "reviewed";
  transcript: "not-started" | "source-acquired" | "machine" | "edited" | "reviewed" | "blocked";
};

type FixtureParticipantProfile = {
  headline: string;
  bio?: string;
  organization: string;
  title?: string;
  status: "current" | "former";
  institution: string;
  credential?: string;
  field?: string;
  checkedAt: string;
};

const publishedWorkflow: FixtureWorkflow = {
  metadata: "verified",
  summary: "draft",
  transcript: "machine",
};

function renderParticipantProfile(profile: FixtureParticipantProfile): string {
  return [
    "    profile:",
    `      headline: ${JSON.stringify(profile.headline)}`,
    ...(profile.bio ? [`      bio: ${JSON.stringify(profile.bio)}`] : []),
    "      affiliations:",
    `        - organization: ${JSON.stringify(profile.organization)}`,
    ...(profile.title ? [`          title: ${JSON.stringify(profile.title)}`] : []),
    `          status: ${profile.status}`,
    "      education:",
    `        - institution: ${JSON.stringify(profile.institution)}`,
    ...(profile.credential ? [`          credential: ${JSON.stringify(profile.credential)}`] : []),
    ...(profile.field ? [`          field: ${JSON.stringify(profile.field)}`] : []),
    `      checked_at: ${profile.checkedAt}`,
  ].join("\n");
}

function writeFixtureShow(repositoryRoot: string) {
  const showRoot = path.join(repositoryRoot, "shows", "example");
  fs.mkdirSync(path.join(showRoot, "episodes"), { recursive: true });
  fs.writeFileSync(path.join(showRoot, "README.md"), `---
schema_version: 1
kind: show
id: example
title: 示例播客
aliases: []
language: zh-CN
status: active
formats:
  - interview
topics:
  - testing
sources:
  - platform: website
    kind: show
    url: https://example.com/show
    preferred: true
last_verified_at: 2026-08-08
---

# 示例播客

用于内容加载测试。
`);
}

function writeFixtureEpisode({
  repositoryRoot,
  folder,
  episodeKey,
  id = `example:${episodeKey}`,
  workflow = publishedWorkflow,
  publishedAt = "2026-08-08T12:00:00+08:00",
  durationMs = 60_000,
  preferredSources = 1,
  writeSummary = true,
  writeTranscript = true,
  participantProfile,
}: {
  repositoryRoot: string;
  folder: string;
  episodeKey: string;
  id?: string;
  workflow?: FixtureWorkflow | { metadata: string; summary: string; transcript: string };
  publishedAt?: string;
  durationMs?: number;
  preferredSources?: number;
  writeSummary?: boolean;
  writeTranscript?: boolean;
  participantProfile?: FixtureParticipantProfile;
}) {
  const episodeRoot = path.join(repositoryRoot, "shows", "example", "episodes", folder);
  fs.mkdirSync(episodeRoot, { recursive: true });
  const sources = Array.from({ length: Math.max(1, preferredSources) }, (_, index) => `
  - platform: website
    kind: episode
    url: https://example.com/${folder}/${index + 1}
    preferred: ${index < preferredSources ? "true" : "false"}`).join("");
  const profile = participantProfile ? `\n${renderParticipantProfile(participantProfile)}` : "";
  const transcriptContent = `# 测试人物：测试主题

[00:00:00] 这是一条测试逐字稿。${"  "}
`;
  const transcriptSha256 = createHash("sha256").update(transcriptContent).digest("hex");
  fs.writeFileSync(path.join(episodeRoot, "README.md"), `---
schema_version: 1
kind: episode
id: "${id}"
show_id: example
episode_key: "${episodeKey}"
episode_number: null
slug: ${folder}
release_type: regular
numbering:
  status: unknown
  checked_at: 2026-08-08
  source: test-fixture
title: "测试人物：测试主题"
navigation_title: "测试人物 · 测试主题"
catalog_keyword: "测试"
published_at: "${publishedAt}"
duration_ms: ${durationMs}
language: zh-CN
participants:
  - id: test-person
    name: 测试人物
    role: guest${profile}
sources:${sources}
workflow:
  metadata: ${workflow.metadata}
  summary: ${workflow.summary}
  transcript: ${workflow.transcript}
summary:
  path: summary.zh-CN.md
  source_transcript:
    path: transcript.zh-CN.md
    engine: test-engine
    model: test-model
    selection_status: selected
    sha256: ${transcriptSha256}
transcript:
  path: transcript.zh-CN.md
  engine: test-engine
  model: test-model
  translations: []
asr_runs:
  - id: test-run
    selection_status: selected
    engine: test-engine
    model: test-model
    artifacts:
      raw: asr/test/raw.json
      refined: asr/test/refined.json
      transcript: asr/test/transcript.zh-CN.md
---

# 测试人物：测试主题
`);
  const asrRoot = path.join(episodeRoot, "asr", "test");
  fs.mkdirSync(asrRoot, { recursive: true });
  fs.writeFileSync(path.join(asrRoot, "raw.json"), "{}\n");
  fs.writeFileSync(path.join(asrRoot, "refined.json"), "{}\n");
  fs.writeFileSync(path.join(asrRoot, "transcript.zh-CN.md"), transcriptContent);
  if (writeSummary) {
    fs.writeFileSync(path.join(episodeRoot, "summary.zh-CN.md"), `# 测试人物：测试主题

## 一句话总结

这是一条测试总结。

## 为什么值得听

- 这是一条测试理由。

## 核心观点

| 主题 | 判断 |
| --- | --- |
| 测试 | 测试内容 |

## 5 分钟读完

这是测试正文。

## 主题导航

- [00:00:00] 测试开场

## 阅读边界

- 本页仅用于测试。

## 编辑记录（不对读者展示）

- 测试夹具记录。
`);
  }
  if (writeTranscript) {
    fs.writeFileSync(path.join(episodeRoot, "transcript.zh-CN.md"), transcriptContent);
  }
  return episodeRoot;
}

function rewriteFixtureReadme(
  filePath: string,
  transform: (readme: string) => string,
) {
  const readme = fs.readFileSync(filePath, "utf8");
  const updated = transform(readme);
  if (updated === readme) throw new Error(`Fixture rewrite made no change: ${filePath}`);
  fs.writeFileSync(filePath, updated);
}

function convertFixtureEpisodeToEnglish(episodeRoot: string) {
  const sourceContent = fs.readFileSync(path.join(episodeRoot, "transcript.zh-CN.md"), "utf8");
  const sourceSha256 = createHash("sha256").update(sourceContent).digest("hex");
  const translationSha256 = createHash("sha256").update(sourceContent).digest("hex");
  fs.writeFileSync(path.join(episodeRoot, "transcript.en.md"), sourceContent);
  fs.writeFileSync(path.join(episodeRoot, "asr", "test", "transcript.en.md"), sourceContent);
  rewriteFixtureReadme(path.join(episodeRoot, "README.md"), (readme) => readme
    .replace("language: zh-CN", "language: en")
    .replaceAll("transcript.zh-CN.md", "transcript.en.md")
    .replace(
      "  translations: []",
      `  translations:
    - language: zh-CN
      path: transcript.zh-CN.md
      source_language: en
      source_path: transcript.en.md
      alignment: segment
      status: machine
      generated_at: "2026-08-08T12:00:00Z"
      source_sha256: ${sourceSha256}
      sha256: ${translationSha256}`,
    ));
}

async function withFixtureRepository(
  setup: (repositoryRoot: string) => void,
  assertion: (content: ContentModule, repositoryRoot: string) => Promise<void>,
) {
  const repositoryRoot = fs.mkdtempSync(path.join(os.tmpdir(), "podwiki-content-"));
  const previousRoot = process.env.PODWIKI_REPOSITORY_ROOT;
  try {
    writeFixtureShow(repositoryRoot);
    setup(repositoryRoot);
    process.env.PODWIKI_REPOSITORY_ROOT = repositoryRoot;
    vi.resetModules();
    const content = await import("@/lib/content");
    await assertion(content, repositoryRoot);
  } finally {
    if (previousRoot === undefined) delete process.env.PODWIKI_REPOSITORY_ROOT;
    else process.env.PODWIKI_REPOSITORY_ROOT = previousRoot;
    vi.resetModules();
    fs.rmSync(repositoryRoot, { recursive: true, force: true });
  }
}

describe("PodWiki content loader", () => {
  it("builds the lightweight episode catalog without reading transcript Markdown", async () => {
    vi.resetModules();
    const content = await import("@/lib/content");
    const readFileSync = vi.spyOn(fs, "readFileSync");

    try {
      const cards = await content.getEpisodeCards();
      const markdownReads = readFileSync.mock.calls.flatMap(([file]) => (
        typeof file === "string" && file.endsWith(".md") ? [path.resolve(file)] : []
      ));

      expect(cards).toHaveLength(131);
      expect(markdownReads.some((file) => path.basename(file).startsWith("summary."))).toBe(true);
      expect(markdownReads.filter((file) => path.basename(file).startsWith("transcript."))).toEqual([]);
    } finally {
      readFileSync.mockRestore();
    }
  });

  it("keeps valid unfinished episodes out of the web catalog", async () => {
    await withFixtureRepository((repositoryRoot) => {
      writeFixtureEpisode({
        repositoryRoot,
        folder: "001-complete",
        episodeKey: "001",
      });
      writeFixtureEpisode({
        repositoryRoot,
        folder: "002-outline",
        episodeKey: "002",
        workflow: {
          metadata: "verified",
          summary: "outline",
          transcript: "not-started",
        },
        writeSummary: false,
        writeTranscript: false,
      });
    }, async (content) => {
      await expect(content.getEpisodeCards()).resolves.toEqual([
        expect.objectContaining({ id: "example:001" }),
      ]);
      await expect(content.getEpisode("example", "002-outline")).resolves.toBeUndefined();
    });
  });

  it("allows documented candidate ASR runs on unfinished episodes", async () => {
    await withFixtureRepository((repositoryRoot) => {
      const episodeRoot = writeFixtureEpisode({
        repositoryRoot,
        folder: "001-candidate",
        episodeKey: "001",
        workflow: {
          metadata: "draft",
          summary: "empty",
          transcript: "not-started",
        },
        writeSummary: false,
        writeTranscript: false,
      });
      rewriteFixtureReadme(
        path.join(episodeRoot, "README.md"),
        (readme) => readme
          .replace(/  source_transcript:\n(?:    .+\n){5}/u, "  source_transcript: null\n")
          .replace(
            "  - id: test-run\n    selection_status: selected",
            "  - id: test-run\n    selection_status: candidate",
          ),
      );
    }, async (content) => {
      await expect(content.getEpisodeCards()).resolves.toEqual([]);
    });
  });

  it("fails when an episode marked for web publication is missing an asset", async () => {
    await withFixtureRepository((repositoryRoot) => {
      writeFixtureEpisode({
        repositoryRoot,
        folder: "001-missing-summary",
        episodeKey: "001",
        writeSummary: false,
      });
    }, async (content) => {
      await expect(content.getEpisodeCards()).rejects.toThrow("Missing summary for example:001");
    });
  });

  it("rejects invalid episode metadata before publishing it", async () => {
    const invalidCases = [
      {
        label: "RFC 3339 publication timestamp",
        overrides: { publishedAt: "2026-08-08" },
      },
      {
        label: "positive duration",
        overrides: { durationMs: 0 },
      },
      {
        label: "stable id",
        overrides: { id: "example:different" },
      },
      {
        label: "stable episode key format",
        overrides: { episodeKey: "bad_key" },
      },
      {
        label: "workflow enum",
        overrides: {
          workflow: { metadata: "verified", summary: "published", transcript: "machine" },
        },
      },
      {
        label: "one preferred source",
        overrides: { preferredSources: 2 },
      },
      {
        label: "a preferred source is required",
        overrides: { preferredSources: 0 },
      },
    ] as const;

    for (const { label, overrides } of invalidCases) {
      await withFixtureRepository((repositoryRoot) => {
        writeFixtureEpisode({
          repositoryRoot,
          folder: "001-invalid",
          episodeKey: "001",
          ...overrides,
        });
      }, async (content) => {
        await expect(content.getEpisodeCards(), label).rejects.toThrow();
      });
    }
  });

  it("rejects publishable episodes that drift from the full metadata contract", async () => {
    const invalidCases = [
      {
        label: "schema kind",
        transform: (readme: string) => readme.replace("kind: episode", "kind: article"),
      },
      {
        label: "directory slug",
        transform: (readme: string) => readme.replace("slug: 001-contract", "slug: other-folder"),
      },
      {
        label: "release type",
        transform: (readme: string) => readme.replace("release_type: regular", "release_type: interview"),
      },
      {
        label: "trailer exclusion",
        transform: (readme: string) => readme.replace("release_type: regular", "release_type: trailer"),
      },
      {
        label: "numbering relation",
        transform: (readme: string) => readme.replace("  status: unknown", "  status: verified"),
      },
      {
        label: "numbering source",
        transform: (readme: string) => readme.replace("  source: test-fixture\n", ""),
      },
      {
        label: "participant id",
        transform: (readme: string) => readme.replace("  - id: test-person\n", "  - name: 测试人物\n")
          .replace("    name: 测试人物\n    role: guest", "    role: guest"),
      },
      {
        label: "participant role",
        transform: (readme: string) => readme.replace("    role: guest", "    role: observer"),
      },
      {
        label: "navigation title participant precedence",
        transform: (readme: string) => readme.replace(
          'navigation_title: "测试人物 · 测试主题"',
          'navigation_title: "错误人物 · 测试主题"',
        ),
      },
      {
        label: "HTTPS source URL",
        transform: (readme: string) => readme.replace(
          "url: https://example.com/001-contract/1",
          "url: http://example.com/001-contract/1",
        ),
      },
      {
        label: "summary source provenance",
        transform: (readme: string) => readme.replace(
          /  source_transcript:\n(?:    .+\n){5}/u,
          "  source_transcript: null\n",
        ),
      },
      {
        label: "summary source hash",
        transform: (readme: string) => readme.replace(
          /    sha256: [0-9a-f]{64}/u,
          "    sha256: invalid",
        ),
      },
      {
        label: "selected ASR run",
        transform: (readme: string) => readme.replace(
          /asr_runs:\n(?:  .+\n|    .+\n|      .+\n)+/u,
          "asr_runs: []\n",
        ),
      },
      {
        label: "Qwen aligned artifact",
        transform: (readme: string) => readme
          .replaceAll("test-engine", "qwen-asr-transformers")
          .replaceAll("test-model", "Qwen/Qwen3-ASR-1.7B"),
      },
      {
        label: "Xiaoyuzhou identifiers",
        transform: (readme: string) => readme.replace(
          /sources:\n[\s\S]*?\nworkflow:/u,
          `sources:
  - platform: xiaoyuzhou
    kind: episode
    url: https://www.xiaoyuzhoufm.com/episode/6a5f4d33a3fec224d5a1136a
    preferred: true
    identifiers:
      eid: 6a5f4d33a3fec224d5a1136a
      pid: 6951e312febad13106eb017e
workflow:`,
        ),
      },
      {
        label: "Xiaoyuzhou source kind",
        transform: (readme: string) => readme.replace(
          /sources:\n[\s\S]*?\nworkflow:/u,
          `sources:
  - platform: xiaoyuzhou
    kind: audio
    url: https://www.xiaoyuzhoufm.com/episode/6a5f4d33a3fec224d5a1136a
    preferred: true
    identifiers:
      eid: 6a5f4d33a3fec224d5a1136a
      pid: 6951e312febad13106eb017e
      media_id: 6951e312febad13106eb017e/test.m4a
workflow:`,
        ),
      },
      {
        label: "canonical Xiaoyuzhou URL",
        transform: (readme: string) => readme.replace(
          /sources:\n[\s\S]*?\nworkflow:/u,
          `sources:
  - platform: xiaoyuzhou
    kind: episode
    url: https://www.xiaoyuzhoufm.com/episode/6a5f4d33a3fec224d5a1136a?utm_source=test
    preferred: true
    identifiers:
      eid: 6a5f4d33a3fec224d5a1136a
      pid: 6951e312febad13106eb017e
      media_id: 6951e312febad13106eb017e/test.m4a
workflow:`,
        ),
      },
      {
        label: "Bilibili identifiers",
        transform: (readme: string) => readme.replace(
          /sources:\n[\s\S]*?\nworkflow:/u,
          `sources:
  - platform: bilibili
    kind: video
    url: https://www.bilibili.com/video/BV1darmBcE4A/
    preferred: true
    identifiers:
      bvid: BV1darmBcE4A
      aid: "115909138055436"
      page: 1
workflow:`,
        ),
      },
    ];

    for (const { label, transform } of invalidCases) {
      await withFixtureRepository((repositoryRoot) => {
        const episodeRoot = writeFixtureEpisode({
          repositoryRoot,
          folder: "001-contract",
          episodeKey: "001",
        });
        rewriteFixtureReadme(path.join(episodeRoot, "README.md"), transform);
      }, async (content) => {
        await expect(content.getEpisodeCards(), label).rejects.toThrow();
      });
    }
  });

  it("requires every show to declare exactly one preferred source", async () => {
    await withFixtureRepository((repositoryRoot) => {
      writeFixtureEpisode({
        repositoryRoot,
        folder: "001-complete",
        episodeKey: "001",
      });
      rewriteFixtureReadme(
        path.join(repositoryRoot, "shows", "example", "README.md"),
        (readme) => readme.replace("    preferred: true\n", ""),
      );
    }, async (content) => {
      await expect(content.getShows()).rejects.toThrow("preferred source");
    });
  });

  it("enforces the complete show metadata and source schema", async () => {
    const invalidCases = [
      (readme: string) => readme.replace("status: active", "status: unknown"),
      (readme: string) => readme.replace("formats:\n  - interview", "formats: []"),
      (readme: string) => readme.replace("topics:\n  - testing", "topics: []"),
      (readme: string) => readme.replace("platform: website", "platform: publisher-platform"),
      (readme: string) => readme.replace("https://example.com/show", "http://example.com/show"),
      (readme: string) => readme.replace("    preferred: true", "    preferred: true\n    invented: value"),
      (readme: string) => readme.replace("last_verified_at: 2026-08-08", "last_verified_at: someday"),
    ];

    for (const transform of invalidCases) {
      await withFixtureRepository((repositoryRoot) => {
        rewriteFixtureReadme(
          path.join(repositoryRoot, "shows", "example", "README.md"),
          transform,
        );
      }, async (content) => {
        await expect(content.getShows()).rejects.toThrow();
      });
    }
  });

  it("rejects a summary source transcript whose bytes no longer match its SHA-256", async () => {
    await withFixtureRepository((repositoryRoot) => {
      const episodeRoot = writeFixtureEpisode({
        repositoryRoot,
        folder: "001-complete",
        episodeKey: "001",
      });
      fs.appendFileSync(path.join(episodeRoot, "transcript.zh-CN.md"), "篡改内容\n");
    }, async (content) => {
      await expect(content.getEpisode("example", "001-complete")).rejects.toThrow(
        "Summary source transcript SHA-256 mismatch",
      );
    });
  });

  it("rejects summary timestamps absent from the declared source transcript", async () => {
    await withFixtureRepository((repositoryRoot) => {
      const episodeRoot = writeFixtureEpisode({
        repositoryRoot,
        folder: "001-complete",
        episodeKey: "001",
      });
      fs.appendFileSync(path.join(episodeRoot, "summary.zh-CN.md"), "\n证据见 [00:00:42]。\n");
    }, async (content) => {
      await expect(content.getEpisode("example", "001-complete")).rejects.toThrow(
        "Summary timestamp 00:00:42",
      );
    });
  });

  it("requires the selected ASR transcript artifact to remain byte-identical", async () => {
    await withFixtureRepository((repositoryRoot) => {
      const episodeRoot = writeFixtureEpisode({
        repositoryRoot,
        folder: "001-complete",
        episodeKey: "001",
      });
      fs.appendFileSync(
        path.join(episodeRoot, "asr", "test", "transcript.zh-CN.md"),
        "篡改内容\n",
      );
    }, async (content) => {
      await expect(content.getEpisode("example", "001-complete")).rejects.toThrow(
        "Selected ASR transcript artifact is not byte-identical",
      );
    });
  });

  it("rejects duplicate stable episode ids across folders", async () => {
    await withFixtureRepository((repositoryRoot) => {
      writeFixtureEpisode({
        repositoryRoot,
        folder: "001-first",
        episodeKey: "001",
      });
      writeFixtureEpisode({
        repositoryRoot,
        folder: "001-second",
        episodeKey: "001",
      });
    }, async (content) => {
      await expect(content.getEpisodeCards()).rejects.toThrow("Duplicate episode id example:001");
    });
  });

  it("rejects an episode asset symlink that resolves outside its episode", async (context) => {
    await withFixtureRepository((repositoryRoot) => {
      const episodeRoot = writeFixtureEpisode({
        repositoryRoot,
        folder: "001-symlink",
        episodeKey: "001",
        writeSummary: false,
      });
      const outsideSummary = path.join(repositoryRoot, "outside-summary.md");
      fs.writeFileSync(outsideSummary, "# Outside\n");
      try {
        fs.symlinkSync(outsideSummary, path.join(episodeRoot, "summary.zh-CN.md"));
      } catch (error) {
        const code = (error as NodeJS.ErrnoException).code;
        if (code === "EPERM" || code === "EACCES") {
          context.skip("This environment cannot create symbolic links");
        }
        throw error;
      }
    }, async (content) => {
      await expect(content.getEpisodeCards()).rejects.toThrow(
        "summary path must resolve inside the episode directory",
      );
    });
  });

  it("accepts the exact English source and zh-CN translation contract", async () => {
    await withFixtureRepository((repositoryRoot) => {
      const episodeRoot = writeFixtureEpisode({
        repositoryRoot,
        folder: "001-english",
        episodeKey: "001",
      });
      convertFixtureEpisodeToEnglish(episodeRoot);
    }, async (content) => {
      await expect(content.getEpisode("example", "001-english")).resolves.toMatchObject({
        language: "en",
        transcriptTranslations: [{
          language: "zh-CN",
          path: "transcript.zh-CN.md",
          sourceLanguage: "en",
          sourcePath: "transcript.en.md",
        }],
      });
    });
  });

  it("rejects translation metadata outside the fixed zh-CN contract", async () => {
    const invalidCases = [
      ["translation language", "    - language: zh-CN", "    - language: zh-Hans"],
      ["translation path", "      path: transcript.zh-CN.md", "      path: translation.zh-CN.md"],
      ["source language", "      source_language: en", "      source_language: en-US"],
      ["source path", "      source_path: transcript.en.md", "      source_path: source.en.md"],
    ] as const;

    for (const [label, current, replacement] of invalidCases) {
      await withFixtureRepository((repositoryRoot) => {
        const episodeRoot = writeFixtureEpisode({
          repositoryRoot,
          folder: "001-english",
          episodeKey: "001",
        });
        convertFixtureEpisodeToEnglish(episodeRoot);
        rewriteFixtureReadme(
          path.join(episodeRoot, "README.md"),
          (readme) => readme.replace(current, replacement),
        );
      }, async (content) => {
        await expect(content.getEpisodeCards(), label).rejects.toThrow();
      });
    }
  });

  it("loads only the requested episode body and its translation assets", async () => {
    vi.resetModules();
    const content = await import("@/lib/content");
    const readFileSync = vi.spyOn(fs, "readFileSync");
    const folder = "bili-bv1dzsczfemv-li-mu";

    try {
      const episode = await content.getEpisode("sv101", folder);
      const markdownReads = readFileSync.mock.calls.flatMap(([file]) => (
        typeof file === "string" && file.endsWith(".md") ? [path.resolve(file)] : []
      ));
      const episodeReads = markdownReads.filter((file) => (
        file.includes(`${path.sep}episodes${path.sep}`)
      ));
      const targetSuffix = path.join("shows", "sv101", "episodes", folder);

      expect(episode?.bilingualTranscript?.segments.length).toBeGreaterThan(0);
      expect(episodeReads.length).toBeGreaterThan(0);
      expect(episodeReads.every((file) => file.includes(targetSuffix))).toBe(true);
      expect(episodeReads.map((file) => path.basename(file))).toEqual(expect.arrayContaining([
        "README.md",
        "summary.zh-CN.md",
        "transcript.en.md",
        "transcript.zh-CN.md",
      ]));
    } finally {
      readFileSync.mockRestore();
    }
  });

  it("loads every current show and episode from the repository", async () => {
    const shows = await getShows();
    const episodes = await getEpisodes();
    expect(shows.map((show) => show.id)).toEqual([
      "zhangxiaojun",
      "sv101",
      "svvector",
      "latetalk",
      "luoyonghao",
      "moonuncle",
      "whynottv",
      "yiqitietalk",
    ]);
    expect(episodes).toHaveLength(131);
    expect(Object.fromEntries(shows.map((show) => [show.id, show.episodeCount]))).toEqual({
      zhangxiaojun: 30,
      sv101: 9,
      svvector: 11,
      latetalk: 16,
      luoyonghao: 36,
      moonuncle: 4,
      whynottv: 5,
      yiqitietalk: 20,
    });
    expect(shows.every((show) => show.episodeCount > 0)).toBe(true);
    expect(episodes.every((episode) => episode.summaryRaw && episode.transcriptSegments.length > 0)).toBe(true);
    const publishedTimes = episodes.map((episode) => Date.parse(episode.publishedAt));
    expect(publishedTimes).toEqual(publishedTimes.toSorted((a, b) => b - a));
  });

  it("uses the episode href as a deterministic publication-time tie breaker", () => {
    const publishedAt = "2026-08-08T12:00:00+08:00";
    const episodes = [
      { href: "/shows/b/episodes/2" },
      { href: "/shows/a/episodes/1" },
    ];

    expect(episodes.toSorted((a, b) => compareEpisodePublicationOrder(
      publishedAt,
      a.href,
      publishedAt,
      b.href,
    ))).toEqual([
      { href: "/shows/a/episodes/1" },
      { href: "/shows/b/episodes/2" },
    ]);
  });

  it("places unknown shows after the curated order with a stable fallback", () => {
    const shows = [
      { id: "unknown-b", title: "乙播客" },
      { id: "latetalk", title: "晚点聊 LateTalk" },
      { id: "unknown-a", title: "甲播客" },
      { id: "sv101", title: "硅谷101" },
    ];

    expect(shows.toSorted(compareShowOrder).map((show) => show.id)).toEqual([
      "sv101",
      "latetalk",
      "unknown-a",
      "unknown-b",
    ]);
  });

  it("keeps official nullable episode numbering intact", async () => {
    const episode = await getEpisode(
      "zhangxiaojun",
      "bili-bv1nb3u6teru-liao-heng",
    );
    expect(episode?.episodeNumber).toBeNull();
    expect(episode?.releaseType).toBe("special");
    expect(episode?.episodeKey).toBe("bili-bv1nb3u6teru");

    const unnumberedRegularEpisode = await getEpisode(
      "sv101",
      "bili-bv1wk3i6nedq-ye-qiyi",
    );
    expect(unnumberedRegularEpisode?.episodeNumber).toBeNull();
    expect(unnumberedRegularEpisode?.releaseType).toBe("regular");
  });

  it("provides concise person-topic titles for every navigation item", async () => {
    const episodes = await getEpisodeCards();

    for (const episode of episodes) {
      const guestNames = episode.guests.map((guest) => guest.name).join("、");
      const participantNames = episode.participants
        .filter((participant) => participant.role === "participant")
        .map((participant) => participant.name)
        .join("、");
      const hostNames = episode.hosts.map((host) => host.name).join("、");
      const navigationNames = guestNames || participantNames || hostNames;
      expect(navigationNames).not.toBe("");
      expect(episode.navigationTitle).toMatch(/^.+ · .+$/u);
      expect(episode.navigationTitle.startsWith(`${navigationNames} · `)).toBe(true);
      expect(episode.navigationTitle.length).toBeLessThanOrEqual(40);
      expect(episode.summaryIntro.length).toBeGreaterThan(0);
      expect(episode.summaryIntro).not.toContain("##");
      expect(episode.summaryIntro).not.toMatch(/\[(?:\d{2}:){2}\d{2}\]/u);
      expect(episode.catalogKeyword).toBe(episode.catalogKeyword.trim());
      expect(episode.catalogKeyword.length).toBeGreaterThan(0);
      expect(episode.catalogKeyword.length).toBeLessThanOrEqual(20);
      expect(episode.catalogKeyword).not.toMatch(/^(?:#|第\s*\d+|特访|特别)/u);
    }

    expect(episodes.find((episode) => episode.folder === "247-sheng-ying")?.catalogKeyword)
      .toBe("SGLang");
    expect(episodes.find((episode) => episode.folder === "140-yao-shunyu")?.catalogKeyword)
      .toBe("OpenAI");
  });

  it("returns summary and timestamped transcript search results", async () => {
    const results = await searchContent("第一性原理");
    expect(results.some((result) => result.section === "总结")).toBe(true);
    expect(results.some((result) => result.section === "逐字稿" && result.timestamp)).toBe(true);

    const episodes = await getEpisodes();
    for (const result of results) {
      const episode = episodes.find((candidate) => result.id.startsWith(`${candidate.id}:`));
      expect(episode).toBeDefined();
      expect(result.title).toBe(episode?.navigationTitle);
    }
  });

  it("indexes reader-facing fact-boundary copy in web search results", async () => {
    await withFixtureRepository((repositoryRoot) => {
      const episodeRoot = writeFixtureEpisode({
        repositoryRoot,
        folder: "001-hidden-facts",
        episodeKey: "001",
      });
      fs.writeFileSync(path.join(episodeRoot, "summary.zh-CN.md"), `# 测试人物：测试主题

## 一句话总结

公开总结关键词。

## 为什么值得听

- 公开阅读理由。

## 核心观点

| 主题 | 判断 |
| --- | --- |
| 测试 | 公开观点 |

## 5 分钟读完

公开正文。

## 主题导航

- [00:00:00] 测试开场

## 阅读边界

- 内部核验关键词。

## 编辑记录（不对读者展示）

- 测试夹具记录。
`);
    }, async (content) => {
      expect(await content.searchContent("公开总结关键词")).toContainEqual(
        expect.objectContaining({ section: "总结" }),
      );
      expect(await content.searchContent("内部核验关键词")).toContainEqual(
        expect.objectContaining({ section: "总结" }),
      );
    });
  });

  it("builds search documents from formal content without reading ASR intermediates", async () => {
    vi.resetModules();
    const content = await import("@/lib/content");
    const readFileSync = vi.spyOn(fs, "readFileSync");

    try {
      const results = await content.searchContent("第一性原理");
      const markdownReads = readFileSync.mock.calls.flatMap(([file]) => (
        typeof file === "string" && file.endsWith(".md") ? [path.resolve(file)] : []
      ));

      expect(results.length).toBeGreaterThan(0);
      expect(markdownReads.some((file) => file.includes(`${path.sep}asr${path.sep}`))).toBe(false);
      expect(markdownReads.some((file) => path.basename(file).startsWith("transcript."))).toBe(true);
    } finally {
      readFileSync.mockRestore();
    }
  });

  it("indexes curated catalog keywords", async () => {
    const results = await searchContent("OpenAI");
    expect(results).toContainEqual(expect.objectContaining({
      id: "zhangxiaojun:140:episode",
      title: "姚顺宇 · 模型进展、Coding 与研究方法",
    }));
    expect(await searchContent("openai")).toBe(results);
  });

  it("loads and indexes guest profile companies and schools", async () => {
    await withFixtureRepository((repositoryRoot) => {
      writeFixtureEpisode({
        repositoryRoot,
        folder: "001-profile",
        episodeKey: "001",
        participantProfile: {
          headline: "人工智能产业研究者",
          bio: "长期研究技术产品与组织。",
          organization: "星河科技",
          title: "首席研究员",
          status: "current",
          institution: "远山大学",
          credential: "博士",
          field: "计算机科学",
          checkedAt: "2026-08-09",
        },
      });
    }, async (content) => {
      const episode = await content.getEpisode("example", "001-profile");
      expect(episode?.guests[0]?.profile).toEqual({
        headline: "人工智能产业研究者",
        bio: "长期研究技术产品与组织。",
        affiliations: [{
          organization: "星河科技",
          title: "首席研究员",
          status: "current",
        }],
        education: [{
          institution: "远山大学",
          credential: "博士",
          field: "计算机科学",
        }],
        checkedAt: "2026-08-09",
      });

      for (const query of ["星河科技", "远山大学"]) {
        const results = await content.searchContent(query);
        expect(results).toContainEqual(expect.objectContaining({
          id: "example:001:episode",
          section: "单集",
          snippet: expect.stringContaining(query),
        }));
      }
    });
  });

  it("caps broad search queries at 24 ranked results", async () => {
    const results = await searchContent("AI");
    expect(results).toHaveLength(24);
  });

  it("loads and strictly pairs the English transcript with its Chinese machine translation", async () => {
    const episode = await getEpisode("sv101", "bili-bv1dzsczfemv-li-mu");
    const translation = episode?.transcriptTranslations[0];
    const bilingual = episode?.bilingualTranscript;

    expect(episode?.language).toBe("en");
    expect(translation).toMatchObject({
      language: "zh-CN",
      sourceLanguage: "en",
      sourcePath: "transcript.en.md",
      path: "transcript.zh-CN.md",
      alignment: "segment",
      status: "machine",
    });
    expect(bilingual?.segments).toHaveLength(episode?.transcriptSegments.length ?? 0);
    expect(bilingual?.segments.every((segment, index) => (
      segment.timestamp === episode?.transcriptSegments[index]?.timestamp
      && segment.sourceText === episode?.transcriptSegments[index]?.text
      && Boolean(segment.translationText)
    ))).toBe(true);
  });

  it("indexes Chinese transcript translations with their source timestamp anchors", async () => {
    const results = await searchContent("端到端延迟必须很低");
    expect(results).toContainEqual(expect.objectContaining({
      section: "译稿",
      timestamp: "00:00:56",
      href: expect.stringContaining("bili-bv1dzsczfemv-li-mu/transcript#t-00-00-56"),
      snippet: expect.stringContaining("端到端延迟必须很低"),
    }));
  });

  it("rejects a translation whose timestamp order diverges from its source", () => {
    const segment = (timestamp: string, text: string): TranscriptSegment => ({
      timestamp,
      seconds: 0,
      text,
      id: timestampToId(timestamp),
    });
    expect(() => pairTranscriptSegments(
      [segment("00:00:00", "source one"), segment("00:00:02", "source two")],
      [segment("00:00:00", "译文一"), segment("00:00:03", "译文二")],
      "test translation",
    )).toThrow("test translation timestamp mismatch at segment 2");
  });

  it("creates stable timestamp anchors", () => {
    expect(timestampToId("01:37:13")).toBe("t-01-37-13");
    expect(timestampToSeconds("99:59:59")).toBe(359_999);
    expect(() => timestampToSeconds("100:00:00")).toThrow("Invalid transcript timestamp");
    expect(() => timestampToSeconds("00:60:00")).toThrow("Invalid transcript timestamp");
    expect(() => timestampToSeconds("00:00:60")).toThrow("Invalid transcript timestamp");
  });

  it("maps every chapter to a real transcript anchor", async () => {
    const episodes = await getEpisodes();
    for (const episode of episodes) {
      const ids = new Set(episode.transcriptSegments.map((segment) => segment.id));
      expect(episode.chapters.length).toBeGreaterThan(1);
      for (const chapter of episode.chapters) {
        expect(ids.has(chapter.href.split("#")[1])).toBe(true);
      }
    }
    const target = await getEpisode("zhangxiaojun", "145-hong-lide");
    expect(target?.chapters.some((chapter) => chapter.timestamp === "02:51:16")).toBe(true);
  });

  it("extracts all reader summary sections", async () => {
    const episodes = await getEpisodes();
    for (const episode of episodes) {
      expect(getMarkdownSection(episode.summaryRaw, "一句话总结")).not.toBe("");
      expect(getMarkdownSection(episode.summaryRaw, "核心观点")).not.toBe("");
      const table = getCorePointTable(episode.summaryRaw);
      expect(table, episode.id).toBeDefined();
      expect(table!.columns.length, episode.id).toBeGreaterThanOrEqual(2);
      expect(table!.rows.length, episode.id).toBeGreaterThanOrEqual(3);
      expect(table!.rows.every((row) => row.length === table!.columns.length), episode.id).toBe(true);
    }
  });
});
