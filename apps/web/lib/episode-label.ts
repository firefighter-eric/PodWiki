export function getEpisodeLabel(episodeNumber: number | null) {
  return episodeNumber === null ? "特别访谈" : `第 ${episodeNumber} 期`;
}

export function getEpisodeDescription({
  showTitle,
  episodeNumber,
  subtitle,
}: {
  showTitle: string;
  episodeNumber: number | null;
  subtitle: string;
}) {
  return subtitle || `${showTitle}${getEpisodeLabel(episodeNumber)}播客总结与逐字稿`;
}
