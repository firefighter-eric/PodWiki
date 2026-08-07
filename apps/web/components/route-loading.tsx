const showRows = ["long", "medium", "short", "medium"] as const;
const articleRows = ["long", "medium", "long", "short"] as const;

function Skeleton({ className = "" }: { className?: string }) {
  return <span className={`route-skeleton ${className}`} />;
}

export function ShowRouteLoading() {
  return (
    <main
      id="main-content"
      className="catalog-page route-loading route-loading-catalog"
      aria-busy="true"
      tabIndex={-1}
    >
      <p className="sr-only" role="status">正在载入节目…</p>

      <div className="route-loading-visual" aria-hidden="true">
        <header className="catalog-header route-loading-catalog-header">
          <div className="route-loading-catalog-intro">
            <Skeleton className="route-skeleton-kicker" />
            <Skeleton className="route-skeleton-show-title" />
            <Skeleton className="route-skeleton-copy route-skeleton-copy-long" />
            <Skeleton className="route-skeleton-copy route-skeleton-copy-medium" />
          </div>
          <div className="route-loading-tally">
            <Skeleton className="route-skeleton-tally-number" />
            <Skeleton className="route-skeleton-tally-label" />
          </div>
        </header>

        <section className="route-loading-list">
          <div className="catalog-section-heading route-loading-heading">
            <Skeleton className="route-skeleton-section-title" />
            <Skeleton className="route-skeleton-count" />
          </div>
          {showRows.map((length, index) => (
            <div className="route-loading-show-row" key={`${length}-${index}`}>
              <Skeleton className={`route-skeleton-person route-skeleton-${length}`} />
              <Skeleton className="route-skeleton-meta" />
              <Skeleton className={`route-skeleton-topic route-skeleton-${length}`} />
              <span className="route-loading-copy-lines">
                <Skeleton className="route-skeleton-copy route-skeleton-copy-long" />
                <Skeleton className="route-skeleton-copy route-skeleton-copy-medium" />
              </span>
              <Skeleton className="route-skeleton-arrow" />
            </div>
          ))}
        </section>
      </div>
    </main>
  );
}

export function EpisodeRouteLoading() {
  return (
    <div
      className="episode-reader route-loading route-loading-episode"
      aria-busy="true"
    >
      <p className="sr-only" role="status">正在载入单集…</p>

      <div className="reader-grid reader-grid-summary route-loading-visual">
        <main
          id="main-content"
          className="reader-main"
          tabIndex={-1}
        >
          <div className="route-loading-reader" aria-hidden="true">
            <div className="reader-view-toolbar route-loading-toolbar">
              <Skeleton className="route-skeleton-tabs" />
            </div>
            <header className="episode-hero route-loading-hero">
              <Skeleton className="route-skeleton-kicker" />
              <Skeleton className="route-skeleton-episode-title" />
              <Skeleton className="route-skeleton-episode-subtitle" />
              <div className="route-loading-byline">
                <Skeleton />
                <Skeleton />
                <Skeleton />
              </div>
            </header>
            <section className="route-loading-article">
              {articleRows.map((length, index) => (
                <div className="route-loading-paragraph" key={`${length}-${index}`}>
                  {index === 0 || index === 2 ? (
                    <Skeleton className="route-skeleton-article-title" />
                  ) : null}
                  <Skeleton className="route-skeleton-copy route-skeleton-copy-long" />
                  <Skeleton className={`route-skeleton-copy route-skeleton-copy-${length}`} />
                </div>
              ))}
            </section>
          </div>
        </main>

        <aside className="right-rail route-loading-rail" aria-hidden="true">
          <Skeleton className="route-skeleton-rail-title" />
          <Skeleton className="route-skeleton-copy route-skeleton-copy-long" />
          <Skeleton className="route-skeleton-copy route-skeleton-copy-medium" />
          <div className="route-loading-rail-divider" />
          <Skeleton className="route-skeleton-rail-title" />
          <Skeleton className="route-skeleton-rail-control" />
          <Skeleton className="route-skeleton-rail-control" />
        </aside>
      </div>
    </div>
  );
}
