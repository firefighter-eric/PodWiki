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
    ?? "浏览 PodWiki 已收录的节目，进入任意一期阅读结构化总结与完整逐字稿。";
  const collectionLabel = selectedShow
    ? `${episodes.length} 期内容`
    : `${episodes.length} 期内容，来自 ${shows.length} 档播客`;
  const previewEpisodesByShow = new Map<string, EpisodeCard[]>();
  if (!selectedShow) {
    for (const episode of episodes) {
      const showEpisodes = previewEpisodesByShow.get(episode.showId) ?? [];
      if (showEpisodes.length >= 3) continue;
      showEpisodes.push(episode);
      previewEpisodesByShow.set(episode.showId, showEpisodes);
    }
  }

  return (
    <main
      id="main-content"
      className={`catalog-page${selectedShow ? "" : " home-catalog-page"}`}
      tabIndex={-1}
    >
      <header className="catalog-header">
        <div className="catalog-intro">
          <p className="section-kicker">PodWiki · 播客知识库</p>
          <h1>{title}</h1>
          <p>{description}</p>
        </div>
        <p className="catalog-tally" aria-label={collectionLabel}>
          <strong>{episodes.length}</strong>
          <span>
            期深度内容
            {!selectedShow ? <small>来自 {shows.length} 档播客</small> : null}
          </span>
        </p>
      </header>

      {!selectedShow ? (
        <section className="podcast-preview-section" aria-labelledby="podcast-preview-title">
          <div className="catalog-section-heading">
            <h2 id="podcast-preview-title">按播客浏览</h2>
            <span>{shows.length} 档</span>
          </div>
          <div className="podcast-preview-grid">
            {shows.map((show) => (
              <article key={show.id} className="podcast-preview-card">
                <header className="podcast-preview-header">
                  <span className="podcast-preview-rule" aria-hidden="true" />
                  <small>{show.episodeCount} 期节目</small>
                  <h3>
                    <Link className="selectable-content-link" href={show.href} draggable={false}>
                      {show.title}
                      <ArrowRight size={18} aria-hidden="true" />
                    </Link>
                  </h3>
                  <p>{show.description}</p>
                </header>
                <ol className="podcast-preview-episodes">
                  {(previewEpisodesByShow.get(show.id) ?? []).map((episode) => {
                    const { name, topic } = splitEpisodeNavigationTitle(episode.navigationTitle);
                    return (
                      <li key={episode.id}>
                        <Link
                          className="podcast-preview-episode selectable-content-link"
                          href={episode.href}
                          draggable={false}
                          aria-label={`${show.title} · ${episode.navigationTitle} · ${episode.publishedDate}`}
                        >
                          <span className="podcast-preview-meta">
                            <strong>{name}</strong>
                            <time dateTime={episode.publishedDate}>{episode.publishedDate}</time>
                          </span>
                          <span className="podcast-preview-topic" title={topic}>{topic}</span>
                        </Link>
                      </li>
                    );
                  })}
                </ol>
                <Link className="podcast-preview-all" href={show.href}>
                  查看全部 {show.episodeCount} 期
                  <ArrowRight size={16} aria-hidden="true" />
                </Link>
              </article>
            ))}
          </div>
        </section>
      ) : null}

      <section
        className={`episode-catalog${selectedShow ? "" : " catalog-recent"}`}
        aria-labelledby="episode-list-title"
      >
        <div className="catalog-section-heading">
          <h2 id="episode-list-title">{selectedShow ? "节目单集" : "最近更新"}</h2>
          <span>{episodes.length} 期</span>
        </div>
        <div className="episode-list">
          {episodes.map((episode) => {
            const { name, topic } = splitEpisodeNavigationTitle(episode.navigationTitle);
            if (selectedShow) {
              return (
                <Link
                  key={episode.id}
                  href={episode.href}
                  className="episode-card show-episode-card selectable-content-link"
                  draggable={false}
                  aria-label={`${episode.navigationTitle} · ${episode.showTitle} · ${episode.publishedDate}`}
                >
                  <strong className="show-episode-person">{name}</strong>
                  <small className="show-episode-meta">
                    {episode.showTitle} · <time dateTime={episode.publishedDate}>{episode.publishedDate}</time>
                  </small>
                  <span className="show-episode-title">{topic}</span>
                  <span className="show-episode-intro" title={episode.summaryIntro}>
                    {episode.summaryIntro}
                  </span>
                  <ArrowRight size={20} aria-hidden="true" />
                </Link>
              );
            }

            return (
              <Link
                key={episode.id}
                href={episode.href}
                className="episode-card selectable-content-link"
                draggable={false}
              >
                <span className="episode-keyword">{episode.catalogKeyword}</span>
                <span className="episode-card-copy">
                  <small>{episode.showTitle} · {episode.publishedDate}</small>
                  <strong>{name}</strong>
                  <span>{topic}</span>
                </span>
                <ArrowRight size={20} aria-hidden="true" />
              </Link>
            );
          })}
        </div>
      </section>
    </main>
  );
}
