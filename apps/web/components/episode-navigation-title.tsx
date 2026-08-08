type EpisodeNavigationTitleProps = {
  title: string;
};

type EpisodeSidebarTitleProps = EpisodeNavigationTitleProps & {
  publishedDate: string;
  showTitle?: string;
};

const navigationTitleSeparator = " · ";

export function splitEpisodeNavigationTitle(title: string): {
  name: string;
  topic: string;
} {
  const separatorIndex = title.indexOf(navigationTitleSeparator);
  if (separatorIndex < 1) return { name: title, topic: "" };
  return {
    name: title.slice(0, separatorIndex),
    topic: title.slice(separatorIndex + navigationTitleSeparator.length),
  };
}

export function EpisodeNavigationTitle({ title }: EpisodeNavigationTitleProps) {
  const { name, topic } = splitEpisodeNavigationTitle(title);
  if (!topic) {
    return <span className="episode-navigation-title">{title}</span>;
  }

  return (
    <span className="episode-navigation-title">
      <span className="episode-navigation-name">
        {name}
      </span>
      <span className="episode-navigation-topic">
        {navigationTitleSeparator}{topic}
      </span>
    </span>
  );
}

export function EpisodeHeroTitle({ title }: EpisodeNavigationTitleProps) {
  const { name, topic } = splitEpisodeNavigationTitle(title);

  return (
    <>
      <h1>{name}</h1>
      {topic ? <p className="episode-subtitle">{topic}</p> : null}
    </>
  );
}

export function EpisodeSidebarTitle({
  title,
  publishedDate,
  showTitle,
}: EpisodeSidebarTitleProps) {
  const { name, topic } = splitEpisodeNavigationTitle(title);

  return (
    <span className="episode-nav-copy sidebar-label">
      <span className="episode-nav-meta">
        <span className="episode-nav-identity">
          <strong className="episode-nav-name">{name}</strong>
          {showTitle ? (
            <>
              <span className="episode-nav-source-separator" aria-hidden="true">·</span>
              <small className="episode-nav-source" title={showTitle}>{showTitle}</small>
            </>
          ) : null}
        </span>
        <time dateTime={publishedDate}>{publishedDate}</time>
      </span>
      {topic ? (
        <span className="episode-nav-topic" title={topic}>{topic}</span>
      ) : null}
    </span>
  );
}
