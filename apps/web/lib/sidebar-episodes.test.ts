import { describe, expect, it } from "vitest";
import {
  getInitialSidebarScope,
  getSidebarCatalogScope,
  getSidebarEpisodeAriaLabel,
  getSidebarEpisodes,
  getSidebarShowTagLabel,
  getSidebarScopeShowId,
  retainSidebarScope,
  toSidebarEpisode,
} from "@/lib/sidebar-episodes";

const episodes = [
  { id: "show-b-new", showId: "show-b" },
  { id: "show-a-middle", showId: "show-a" },
  { id: "show-b-old", showId: "show-b" },
  { id: "show-a-oldest", showId: "show-a" },
] as const;

const shows = [
  { id: "show-a", href: "/shows/show-a" },
  { id: "show-b", href: "/shows/show-b" },
] as const;

describe("sidebar episode order", () => {
  it("uses compact show tag labels while keeping an automatic fallback", () => {
    const knownShows = [
      ["zhangxiaojun", "张小珺商业访谈录", "张小珺"],
      ["sv101", "硅谷101", "硅谷101"],
      ["svvector", "硅谷坐标 SV-Vector", "SV-Vector"],
      ["latetalk", "晚点聊 LateTalk", "LateTalk"],
      ["luoyonghao", "罗永浩的十字路口", "十字路口"],
      ["whynottv", "WhynotTV Podcast", "WhynotTV"],
      ["yiqitietalk", "一起铁TALK", "一起铁TALK"],
    ] as const;

    for (const [id, shortTitle, expected] of knownShows) {
      expect(getSidebarShowTagLabel({ id, shortTitle })).toBe(expected);
    }

    expect(getSidebarShowTagLabel({
      id: "new-show",
      shortTitle: "新播客",
    })).toBe("新播客");
  });

  it("keeps the global publication order instead of regrouping by show", () => {
    expect(getSidebarEpisodes(episodes).map((episode) => episode.id)).toEqual([
      "show-b-new",
      "show-a-middle",
      "show-b-old",
      "show-a-oldest",
    ]);
  });

  it("filters one show without changing its publication order", () => {
    expect(getSidebarEpisodes(episodes, "show-a").map((episode) => episode.id)).toEqual([
      "show-a-middle",
      "show-a-oldest",
    ]);
  });

  it("keeps person and topic first while omitting redundant filtered-show context", () => {
    const episode = {
      navigationTitle: "游凯超 · vLLM、开源治理与模型—Infra 协同",
      showTitle: "张小珺商业访谈录",
      publishedDate: "2026-07-28",
    };

    expect(getSidebarEpisodeAriaLabel(episode, true)).toBe(
      "游凯超 · vLLM、开源治理与模型—Infra 协同 · 张小珺商业访谈录 · 2026-07-28",
    );
    expect(getSidebarEpisodeAriaLabel(episode, false)).toBe(
      "游凯超 · vLLM、开源治理与模型—Infra 协同 · 2026-07-28",
    );
  });

  it("changes scope only on catalog routes, not while reading an episode", () => {
    expect(getSidebarCatalogScope("/shows", shows)).toBe("all");
    expect(getSidebarCatalogScope("/shows/show-a", shows)).toBe("show:show-a");
    expect(getSidebarCatalogScope("/shows/show-a/episodes/001", shows)).toBeUndefined();
    expect(getSidebarCatalogScope("/shows/show-a/episodes/001/transcript", shows))
      .toBeUndefined();
  });

  it("uses the episode owner only as the deterministic direct-link default", () => {
    expect(getInitialSidebarScope("/shows", shows)).toBe("all");
    expect(getInitialSidebarScope("/shows/show-a", shows)).toBe("show:show-a");
    expect(getInitialSidebarScope("/shows/show-b/episodes/001", shows)).toBe("show:show-b");
    expect(getInitialSidebarScope("/unknown", shows)).toBe("all");
    expect(getSidebarScopeShowId("all")).toBeUndefined();
    expect(getSidebarScopeShowId("show:show-a")).toBe("show-a");
  });

  it("retains the user-selected range across episode and transcript navigation", () => {
    let scope = getInitialSidebarScope("/shows", shows);
    scope = retainSidebarScope(
      scope,
      getSidebarCatalogScope("/shows/show-a/episodes/001", shows),
    );
    expect(scope).toBe("all");

    scope = retainSidebarScope(scope, getSidebarCatalogScope("/shows/show-a", shows));
    expect(scope).toBe("show:show-a");

    scope = retainSidebarScope(
      scope,
      getSidebarCatalogScope("/shows/show-a/episodes/001/transcript", shows),
    );
    expect(scope).toBe("show:show-a");
  });

  it("serializes only the fields used by the client sidebar", () => {
    expect(toSidebarEpisode({
      id: "show-a-001",
      showId: "show-a",
      showTitle: "Show A",
      navigationTitle: "人物 · 主题",
      publishedDate: "2026-08-08",
      href: "/shows/show-a/episodes/001",
      episodeNumber: 1,
      folder: "001",
      title: "发布者标题",
      catalogKeyword: "关键词",
      editorialTitle: "编辑标题",
      displayTitle: "编辑标题",
      subtitle: "",
      summaryIntro: "不应进入客户端壳层的长简介",
      participants: [],
      guests: [],
      hosts: [],
      workflow: {},
    })).toEqual({
      id: "show-a-001",
      showId: "show-a",
      showTitle: "Show A",
      navigationTitle: "人物 · 主题",
      publishedDate: "2026-08-08",
      href: "/shows/show-a/episodes/001",
    });
  });
});
