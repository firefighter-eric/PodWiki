type EpisodeNavigationTitleProps = {
  title: string;
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
