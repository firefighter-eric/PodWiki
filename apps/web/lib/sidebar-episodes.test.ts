import { describe, expect, it } from "vitest";
import {
  getSidebarEpisodeAriaLabel,
  getSidebarEpisodes,
} from "@/lib/sidebar-episodes";

const episodes = [
  { id: "show-b-new", showId: "show-b" },
  { id: "show-a-middle", showId: "show-a" },
  { id: "show-b-old", showId: "show-b" },
  { id: "show-a-oldest", showId: "show-a" },
] as const;

describe("sidebar episode order", () => {
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
});
