import type { Metadata } from "next";
import { ShowCatalog } from "@/components/show-catalog";
import { getEpisodeCards, getShows } from "@/lib/content";

export const metadata: Metadata = { title: "全部节目" };

export default async function ShowsPage() {
  const [shows, episodes] = await Promise.all([getShows(), getEpisodeCards()]);
  return <ShowCatalog shows={shows} episodes={episodes} />;
}
