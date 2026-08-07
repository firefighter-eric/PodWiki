import type { EpisodeCard, SidebarEpisode } from "@/lib/types";

export type SidebarScope = "all" | `show:${string}`;

type SidebarShowRoute = {
  id: string;
  href: string;
};

export function getSidebarCatalogScope(
  pathname: string,
  shows: readonly SidebarShowRoute[],
): SidebarScope | undefined {
  if (pathname === "/shows") return "all";
  const show = shows.find((candidate) => pathname === candidate.href);
  return show ? `show:${show.id}` : undefined;
}

export function getInitialSidebarScope(
  pathname: string,
  shows: readonly SidebarShowRoute[],
): SidebarScope {
  const catalogScope = getSidebarCatalogScope(pathname, shows);
  if (catalogScope) return catalogScope;

  const episodeShow = shows.find((show) =>
    pathname.startsWith(`${show.href}/episodes/`),
  );
  return episodeShow ? `show:${episodeShow.id}` : "all";
}

export function getSidebarScopeShowId(scope: SidebarScope): string | undefined {
  return scope === "all" ? undefined : scope.slice("show:".length);
}

export function retainSidebarScope(
  currentScope: SidebarScope,
  catalogScope: SidebarScope | undefined,
): SidebarScope {
  return catalogScope ?? currentScope;
}

export function toSidebarEpisode(episode: EpisodeCard): SidebarEpisode {
  return {
    id: episode.id,
    showId: episode.showId,
    showTitle: episode.showTitle,
    navigationTitle: episode.navigationTitle,
    publishedDate: episode.publishedDate,
    href: episode.href,
  };
}

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
