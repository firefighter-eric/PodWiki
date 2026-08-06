import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { ShowCatalog } from "@/components/show-catalog";
import { getEpisodeCards, getShow, getShows } from "@/lib/content";

type ShowPageProps = { params: Promise<{ showId: string }> };

export async function generateMetadata({ params }: ShowPageProps): Promise<Metadata> {
  const show = await getShow((await params).showId);
  return show ? { title: show.title, description: show.description } : {};
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
