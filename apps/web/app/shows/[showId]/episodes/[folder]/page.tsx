import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { ChapterRail } from "@/components/chapter-rail";
import { EpisodeHeroTitle } from "@/components/episode-navigation-title";
import { MobileReaderTools } from "@/components/mobile-reader-tools";
import { ReaderPreferences } from "@/components/reader-preferences";
import { ReaderTabs } from "@/components/reader-tabs";
import { RightRail } from "@/components/right-rail";
import { SummaryView } from "@/components/summary-view";
import { TranscriptView } from "@/components/transcript-view";
import { getEpisode, getEpisodes } from "@/lib/content";
import { getEpisodeDescription, getEpisodeLabel } from "@/lib/episode-label";

type EpisodePageProps = {
  params: Promise<{ showId: string; folder: string }>;
  searchParams: Promise<{ view?: string | string[] }>;
};

export async function generateStaticParams() {
  return (await getEpisodes()).map((episode) => ({
    showId: episode.showId,
    folder: episode.folder,
  }));
}

export async function generateMetadata({ params }: EpisodePageProps): Promise<Metadata> {
  const { showId, folder } = await params;
  const episode = await getEpisode(showId, folder);
  if (!episode) return {};
  return {
    title: episode.navigationTitle,
    description: getEpisodeDescription(episode),
  };
}

export default async function EpisodePage({ params, searchParams }: EpisodePageProps) {
  const [{ showId, folder }, query] = await Promise.all([params, searchParams]);
  const episode = await getEpisode(showId, folder);
  if (!episode) notFound();

  const rawView = Array.isArray(query.view) ? query.view[0] : query.view;
  const view: "summary" | "transcript" = rawView === "transcript" ? "transcript" : "summary";
  const episodeLabel = getEpisodeLabel(episode.episodeNumber, episode.releaseType);
  const guests = episode.guests.map((guest) => guest.name).join("、");
  const hosts = episode.hosts.map((host) => host.name).join("、");

  return (
    <ReaderPreferences>
      <div className={`reader-grid reader-grid-${view}`}>
        {view === "transcript" ? <ChapterRail chapters={episode.chapters} /> : null}

        <main id="main-content" className="reader-main" tabIndex={-1}>
          <div className="reader-view-toolbar">
            <ReaderTabs href={episode.href} view={view} />
          </div>
          <MobileReaderTools
            chapters={episode.chapters}
            showChapters={view === "transcript"}
          />
          <header className="episode-hero">
            <div className="episode-kicker-row">
              <p className="episode-kicker">
                {episode.showTitle}
                {episodeLabel ? (
                  <>
                    <span>·</span>
                    {episodeLabel}
                  </>
                ) : null}
                <span>·</span>
                {episode.durationLabel}
              </p>
            </div>
            <EpisodeHeroTitle title={episode.navigationTitle} />
            <p className="episode-byline">
              {guests ? <span>嘉宾：{guests}</span> : null}
              {hosts ? <span>主持人：{hosts}</span> : null}
              <time dateTime={episode.publishedAt}>{episode.publishedDate}</time>
            </p>
          </header>

          {view === "summary" ? (
            <SummaryView episode={episode} />
          ) : (
            <TranscriptView episode={episode} />
          )}
        </main>

        <RightRail episode={episode} view={view} />
      </div>
    </ReaderPreferences>
  );
}
