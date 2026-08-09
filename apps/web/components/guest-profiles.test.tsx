import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import { EpisodeReader } from "@/components/episode-reader";
import { GuestProfiles } from "@/components/guest-profiles";
import { EpisodeRouteLoading } from "@/components/route-loading";
import { getEpisode } from "@/lib/content";
import type { Participant } from "@/lib/types";

describe("GuestProfiles", () => {
  it("renders each profiled guest with semantic background details", () => {
    const guests: Participant[] = [
      {
        id: "lin-jieping",
        name: "林杰屏",
        role: "guest",
        profile: {
          headline: "半导体企业家与工程师",
          bio: "长期从事半导体设备研发与创业。",
          affiliations: [
            {
              organization: "Lam Research",
              title: "创始人",
              status: "former",
            },
            {
              organization: "MultiBeam",
              title: "创始人兼董事长",
              status: "current",
            },
          ],
          education: [
            {
              institution: "MIT",
              credential: "博士",
              field: "化学工程",
            },
          ],
          checkedAt: "2026-08-09",
        },
      },
      {
        id: "zhou-mo",
        name: "周默",
        role: "guest",
        profile: {
          headline: "AI 产业研究者",
          affiliations: [],
          education: [],
          checkedAt: "2026-08-08",
        },
      },
    ];

    const html = renderToStaticMarkup(createElement(GuestProfiles, { guests }));

    expect(html).toContain(
      '<section class="guest-profiles" aria-labelledby="guest-profiles-title">',
    );
    expect(html).toContain(
      '<h2 id="guest-profiles-title" class="sr-only">嘉宾背景</h2>',
    );
    expect(html).not.toContain("人物档案");
    expect(html.match(/<article class="guest-profile">/g)).toHaveLength(2);
    expect(html).toContain("林杰屏");
    expect(html).not.toContain("半导体企业家与工程师");
    expect(html).toContain("长期从事半导体设备研发与创业。");
    expect(html).toContain("Lam Research");
    expect(html).toContain("曾任");
    expect(html).toContain("MultiBeam");
    expect(html).toContain("现任");
    expect(html).toContain("MIT");
    expect(html).toContain("博士 · 化学工程");
    expect(html).toContain("资料核验于");
    expect(html).toContain('<time dateTime="2026-08-09">2026-08-09</time>');
    expect(html).toContain("“现任”均指截至该日");
    expect(html).toContain("AI 产业研究者");
    expect(html.indexOf("林杰屏")).toBeLessThan(html.indexOf("周默"));
  });

  it("does not repeat a headline that matches a structured affiliation", () => {
    const guests: Participant[] = [{
      id: "you-kaichao",
      name: "游凯超",
      role: "guest",
      profile: {
        headline: "Inferact 联合创始人兼首席科学家",
        affiliations: [{
          organization: "Inferact",
          title: "联合创始人兼首席科学家",
          status: "current",
        }],
        education: [],
        checkedAt: "2026-08-06",
      },
    }];

    const html = renderToStaticMarkup(createElement(GuestProfiles, { guests }));

    expect(html.match(/Inferact/g)).toHaveLength(1);
    expect(html.match(/联合创始人兼首席科学家/g)).toHaveLength(1);
    expect(html).toContain("现任");
  });

  it("does not render when no guest has a profile", () => {
    const html = renderToStaticMarkup(createElement(GuestProfiles, {
      guests: [{ id: "guest", name: "测试嘉宾", role: "guest" }],
    }));

    expect(html).toBe("");
  });

  it("places the profiles after the hero and before the reader body", async () => {
    const episode = await getEpisode("sv101", "247-sheng-ying");
    expect(episode).toBeDefined();
    const guest = episode!.guests[0];
    expect(guest).toBeDefined();

    const html = renderToStaticMarkup(createElement(EpisodeReader, {
      episode: {
        ...episode!,
        chapters: [],
        transcriptSegments: episode!.transcriptSegments.slice(0, 1),
        guests: [{
          ...guest!,
          profile: {
            headline: "AI 基础设施创业者",
            affiliations: [],
            education: [],
            checkedAt: "2026-08-09",
          },
        }],
      },
      view: "transcript",
    }));

    expect(html.indexOf('class="episode-hero"')).toBeLessThan(
      html.indexOf('class="guest-profiles"'),
    );
    expect(html.indexOf('class="guest-profiles"')).toBeLessThan(
      html.indexOf('id="full-transcript"'),
    );
  });

  it("reserves the guest profile region in the episode loading state", () => {
    const html = renderToStaticMarkup(createElement(EpisodeRouteLoading));

    expect(html.indexOf('class="episode-hero route-loading-hero"')).toBeLessThan(
      html.indexOf('class="route-loading-guest-profile"'),
    );
    expect(html.indexOf('class="route-loading-guest-profile"')).toBeLessThan(
      html.indexOf('class="route-loading-article"'),
    );
    expect(html).toContain('class="route-skeleton route-skeleton-guest-name"');
  });
});
