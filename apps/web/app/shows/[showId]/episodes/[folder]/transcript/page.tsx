import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { EpisodeReader } from "@/components/episode-reader";
import { getEpisode, getEpisodeCards } from "@/lib/content";
import { getEpisodeDescription } from "@/lib/episode-label";

type TranscriptPageProps = {
  params: Promise<{ showId: string; folder: string }>;
};

export const dynamicParams = false;

export async function generateStaticParams() {
  return (await getEpisodeCards()).map((episode) => ({
    showId: episode.showId,
    folder: episode.folder,
  }));
}

export async function generateMetadata({ params }: TranscriptPageProps): Promise<Metadata> {
  const { showId, folder } = await params;
  const episode = await getEpisode(showId, folder);
  if (!episode) return {};

  const description = getEpisodeDescription(episode);
  const transcriptTitle = `${episode.navigationTitle} · 逐字稿`;
  const canonical = `${episode.href}/transcript`;
  return {
    title: transcriptTitle,
    description,
    alternates: {
      canonical,
    },
    openGraph: {
      type: "article",
      locale: "zh_CN",
      siteName: "PodWiki",
      title: `${transcriptTitle} · PodWiki`,
      description,
      url: canonical,
      publishedTime: episode.publishedAt,
    },
    twitter: {
      card: "summary",
      title: `${transcriptTitle} · PodWiki`,
      description,
    },
  };
}

export default async function TranscriptPage({ params }: TranscriptPageProps) {
  const { showId, folder } = await params;
  const episode = await getEpisode(showId, folder);
  if (!episode) notFound();

  return <EpisodeReader episode={episode} view="transcript" />;
}
