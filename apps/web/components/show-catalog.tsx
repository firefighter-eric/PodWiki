import { ArrowRight } from "@phosphor-icons/react/dist/ssr";
import Link from "next/link";
import { splitEpisodeNavigationTitle } from "@/components/episode-navigation-title";
import type { EpisodeCard, ShowSummary } from "@/lib/types";

export function ShowCatalog({
  shows,
  episodes,
  selectedShow,
}: {
  shows: ShowSummary[];
  episodes: EpisodeCard[];
  selectedShow?: ShowSummary;
}) {
  const title = selectedShow?.title ?? "全部节目";
  const description = selectedShow?.description
    ?? "浏览 PodWiki 已收录的节目，进入任意一期阅读结构化总结与完整机器逐字稿。";

  return (
    <main id="main-content" className="catalog-page" tabIndex={-1}>
      <header className="catalog-header">
        <p className="section-kicker">PodWiki · 播客知识库</p>
        <h1>{title}</h1>
        <p>{description}</p>
      </header>

      {!selectedShow ? (
        <section className="show-grid" aria-label="节目列表">
          {shows.map((show) => (
            <Link key={show.id} href={show.href} className="show-card">
              <span>
                <small>{show.episodeCount} 期节目</small>
                <strong>{show.title}</strong>
                <span>{show.description}</span>
              </span>
              <ArrowRight size={21} aria-hidden="true" />
            </Link>
          ))}
        </section>
      ) : null}

      <section className="episode-catalog" aria-labelledby="episode-list-title">
        <div className="catalog-section-heading">
          <h2 id="episode-list-title">{selectedShow ? "节目单集" : "最近更新"}</h2>
          <span>{episodes.length} 期</span>
        </div>
        <div className="episode-list">
          {episodes.map((episode) => (
            <Link key={episode.id} href={episode.href} className="episode-card">
              <span className="episode-keyword">{episode.catalogKeyword}</span>
              <span className="episode-card-copy">
                <small>{episode.showTitle} · {episode.publishedDate}</small>
                <strong>{episode.guests.map((guest) => guest.name).join("、")}</strong>
                <span>{splitEpisodeNavigationTitle(episode.navigationTitle).topic}</span>
              </span>
              <ArrowRight size={20} aria-hidden="true" />
            </Link>
          ))}
        </div>
      </section>
    </main>
  );
}
