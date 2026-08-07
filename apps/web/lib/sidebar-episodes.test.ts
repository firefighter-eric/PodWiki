import { describe, expect, it } from "vitest";
import { getSidebarEpisodes } from "@/lib/sidebar-episodes";

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
});
