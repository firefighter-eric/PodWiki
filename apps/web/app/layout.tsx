import type { Metadata } from "next";
import { AppShell } from "@/components/app-shell";
import { fontVariables } from "@/app/fonts";
import { getEpisodeCards, getShows } from "@/lib/content";
import { toSidebarEpisode } from "@/lib/sidebar-episodes";
import "./globals.css";

export const metadata: Metadata = {
  metadataBase: new URL("https://podwiki.vercel.app"),
  title: {
    default: "PodWiki — 播客文字与总结",
    template: "%s · PodWiki",
  },
  description: "把长播客整理成可搜索、可定位、适合深度阅读的文字知识库。",
  alternates: {
    canonical: "/shows",
  },
  openGraph: {
    type: "website",
    locale: "zh_CN",
    siteName: "PodWiki",
    title: "PodWiki — 播客文字与总结",
    description: "把长播客整理成可搜索、可定位、适合深度阅读的文字知识库。",
    url: "/shows",
  },
  twitter: {
    card: "summary",
    title: "PodWiki — 播客文字与总结",
    description: "把长播客整理成可搜索、可定位、适合深度阅读的文字知识库。",
  },
};

const preHydrationPreferencesScript = `(function(){var root=document.documentElement;try{root.dataset.sidebarState=localStorage.getItem("podwiki.sidebar.v1")==="collapsed"?"collapsed":"expanded"}catch(error){}try{var stored=JSON.parse(localStorage.getItem("podwiki.reader.v1")||"{}");root.dataset.readerFontSize=["small","medium","large"].includes(stored.fontSize)?stored.fontSize:"medium";root.dataset.readerMeasure=["narrow","standard","wide"].includes(stored.measure)?stored.measure:"standard"}catch(error){root.dataset.readerFontSize="medium";root.dataset.readerMeasure="standard"}})()`;

export default async function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  const [shows, episodes] = await Promise.all([getShows(), getEpisodeCards()]);

  return (
    <html
      lang="zh-CN"
      className={fontVariables}
      data-scroll-behavior="smooth"
      data-sidebar-state="expanded"
      data-reader-font-size="medium"
      data-reader-measure="standard"
      suppressHydrationWarning
    >
      <head>
        <script dangerouslySetInnerHTML={{ __html: preHydrationPreferencesScript }} />
      </head>
      <body>
        <AppShell shows={shows} episodes={episodes.map(toSidebarEpisode)}>
          {children}
        </AppShell>
      </body>
    </html>
  );
}
