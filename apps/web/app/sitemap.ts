import type { MetadataRoute } from "next";
import { getEpisodeCards, getShows } from "@/lib/content";

const siteUrl = "https://podwiki.vercel.app";

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const [shows, episodes] = await Promise.all([getShows(), getEpisodeCards()]);
  const latestDateByShow = new Map<string, string>();

  for (const episode of episodes) {
    if (!latestDateByShow.has(episode.showId)) {
      latestDateByShow.set(episode.showId, episode.publishedDate);
    }
  }

  return [
    {
      url: `${siteUrl}/shows`,
      lastModified: episodes[0]?.publishedDate,
    },
    ...shows.map((show) => ({
      url: `${siteUrl}${show.href}`,
      lastModified: latestDateByShow.get(show.id),
    })),
    ...episodes.flatMap((episode) => [
      {
        url: `${siteUrl}${episode.href}`,
        lastModified: episode.publishedDate,
      },
      {
        url: `${siteUrl}${episode.href}/transcript`,
        lastModified: episode.publishedDate,
      },
    ]),
  ];
}
