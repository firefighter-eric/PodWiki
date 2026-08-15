import type { EpisodeCard, ShowSummary, SidebarEpisode } from "@/lib/types";

export type SidebarScope = "all" | `show:${string}`;

const sidebarShowTagLabels: Readonly<Record<string, string>> = {
  zhangxiaojun: "张小珺",
  sv101: "硅谷101",
  svvector: "SV-Vector",
  latetalk: "LateTalk",
  luoyonghao: "十字路口",
  moonuncle: "月球大叔",
  whynottv: "WhynotTV",
  yiqitietalk: "一起铁TALK",
};

type SidebarShowRoute = {
  id: string;
  href: string;
};

export function getSidebarShowTagLabel(
  show: Pick<ShowSummary, "id" | "shortTitle">,
): string {
  return sidebarShowTagLabels[show.id] ?? show.shortTitle;
}

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
