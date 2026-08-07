import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { ShowCatalog } from "@/components/show-catalog";
import { getEpisodeCards, getShow, getShows } from "@/lib/content";

type ShowPageProps = { params: Promise<{ showId: string }> };

export const dynamicParams = false;

export async function generateStaticParams() {
  return (await getShows()).map((show) => ({ showId: show.id }));
}

export async function generateMetadata({ params }: ShowPageProps): Promise<Metadata> {
  const show = await getShow((await params).showId);
  if (!show) return {};

  const title = `${show.title} · PodWiki`;
  return {
    title: show.title,
    description: show.description,
    alternates: {
      canonical: show.href,
    },
    openGraph: {
      type: "website",
      locale: "zh_CN",
      siteName: "PodWiki",
      title,
      description: show.description,
      url: show.href,
    },
    twitter: {
      card: "summary",
      title,
      description: show.description,
    },
  };
}

export default async function ShowPage({ params }: ShowPageProps) {
  const { showId } = await params;
  const [show, shows, episodes] = await Promise.all([
    getShow(showId),
    getShows(),
    getEpisodeCards(showId),
  ]);
  if (!show) notFound();
  return <ShowCatalog shows={shows} episodes={episodes} selectedShow={show} />;
}
