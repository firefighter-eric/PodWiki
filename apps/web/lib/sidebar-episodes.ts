export function getSidebarEpisodes<T extends { showId: string }>(
  episodes: readonly T[],
  showId?: string,
): readonly T[] {
  return showId ? episodes.filter((episode) => episode.showId === showId) : episodes;
}
