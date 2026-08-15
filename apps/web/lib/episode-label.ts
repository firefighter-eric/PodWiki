import type { EpisodeReleaseType } from "@/lib/types";

export function getEpisodeLabel(
  episodeNumber: number | null,
  releaseType: EpisodeReleaseType,
) {
  if (episodeNumber !== null) return `第 ${episodeNumber} 期`;
  return {
    regular: null,
    special: "特别访谈",
    bonus: "加更",
  }[releaseType];
}

export function getEpisodeDescription({
  showTitle,
  episodeNumber,
  releaseType,
  subtitle,
}: {
  showTitle: string;
  episodeNumber: number | null;
  releaseType: EpisodeReleaseType;
  subtitle: string;
}) {
  const label = getEpisodeLabel(episodeNumber, releaseType);
  return subtitle || `${showTitle}${label ?? ""}播客总结与逐字稿`;
}
