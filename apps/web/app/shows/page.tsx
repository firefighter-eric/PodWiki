import type { Metadata } from "next";
import { ShowCatalog } from "@/components/show-catalog";
import { getEpisodeCards, getShows } from "@/lib/content";

const description = "浏览 PodWiki 已收录的节目，进入任意一期阅读结构化总结与完整逐字稿。";

export const metadata: Metadata = {
  title: "全部节目",
  description,
  alternates: {
    canonical: "/shows",
  },
  openGraph: {
    type: "website",
    locale: "zh_CN",
    siteName: "PodWiki",
    title: "全部节目 · PodWiki",
    description,
    url: "/shows",
  },
  twitter: {
    card: "summary",
    title: "全部节目 · PodWiki",
    description,
  },
};

export default async function ShowsPage() {
  const [shows, episodes] = await Promise.all([getShows(), getEpisodeCards()]);
  return <ShowCatalog shows={shows} episodes={episodes} />;
}
