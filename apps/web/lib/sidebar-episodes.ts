import type { EpisodeCard } from "@/lib/types";

export function getSidebarEpisodes<T extends { showId: string }>(
  episodes: readonly T[],
  showId?: string,
): readonly T[] {
  return showId ? episodes.filter((episode) => episode.showId === showId) : episodes;
}

type SidebarEpisodeLabel = Pick<
  EpisodeCard,
  "navigationTitle" | "publishedDate" | "showTitle"
>;

export function getSidebarEpisodeAriaLabel(
  episode: SidebarEpisodeLabel,
  includeShowTitle: boolean,
): string {
  return [
    episode.navigationTitle,
    ...(includeShowTitle ? [episode.showTitle] : []),
    episode.publishedDate,
  ].join(" · ");
}
