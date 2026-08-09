import type { MetadataRoute } from "next";
import { getEpisodeCards, getShows } from "@/lib/content";

const siteUrl = "https://podwiki.vercel.app";

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const [shows, episodes] = await Promise.all([getShows(), getEpisodeCards()]);

  return [
    {
      url: `${siteUrl}/shows`,
    },
    ...shows.map((show) => ({
      url: `${siteUrl}${show.href}`,
    })),
    ...episodes.flatMap((episode) => [
      {
        url: `${siteUrl}${episode.href}`,
      },
      {
        url: `${siteUrl}${episode.href}/transcript`,
      },
    ]),
  ];
}
