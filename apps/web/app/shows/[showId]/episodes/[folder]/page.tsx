import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { EpisodeReader } from "@/components/episode-reader";
import { getEpisode, getEpisodeCards } from "@/lib/content";
import { getEpisodeDescription } from "@/lib/episode-label";

type EpisodePageProps = {
  params: Promise<{ showId: string; folder: string }>;
};

export const dynamicParams = false;

export async function generateStaticParams() {
  return (await getEpisodeCards()).map((episode) => ({
    showId: episode.showId,
    folder: episode.folder,
  }));
}

export async function generateMetadata({ params }: EpisodePageProps): Promise<Metadata> {
  const { showId, folder } = await params;
  const episode = await getEpisode(showId, folder);
  if (!episode) return {};

  const description = getEpisodeDescription(episode);
  const title = `${episode.navigationTitle} · PodWiki`;
  return {
    title: episode.navigationTitle,
    description,
    alternates: {
      canonical: episode.href,
    },
    openGraph: {
      type: "article",
      locale: "zh_CN",
      siteName: "PodWiki",
      title,
      description,
      url: episode.href,
      publishedTime: episode.publishedAt,
    },
    twitter: {
      card: "summary",
      title,
      description,
    },
  };
}

export default async function EpisodePage({ params }: EpisodePageProps) {
  const { showId, folder } = await params;
  const episode = await getEpisode(showId, folder);
  if (!episode) notFound();

  return <EpisodeReader episode={episode} view="summary" />;
}
