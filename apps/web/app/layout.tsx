import type { Metadata } from "next";
import { AppShell } from "@/components/app-shell";
import { getEpisodeCards, getShows } from "@/lib/content";
import "./globals.css";

export const metadata: Metadata = {
  title: {
    default: "PodWiki — 播客文字与总结",
    template: "%s · PodWiki",
  },
  description: "把长播客整理成可搜索、可定位、适合深度阅读的文字知识库。",
};

export default async function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  const [shows, episodes] = await Promise.all([getShows(), getEpisodeCards()]);

  return (
    <html lang="zh-CN" data-scroll-behavior="smooth">
      <body>
        <AppShell shows={shows} episodes={episodes}>
          {children}
        </AppShell>
      </body>
    </html>
  );
}
