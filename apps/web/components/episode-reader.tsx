import { ChapterRail } from "@/components/chapter-rail";
import { EpisodeHeroTitle } from "@/components/episode-navigation-title";
import { MobileReaderTools } from "@/components/mobile-reader-tools";
import { ReaderPreferences } from "@/components/reader-preferences";
import { ReaderTabs } from "@/components/reader-tabs";
import { RightRail } from "@/components/right-rail";
import { SummaryView } from "@/components/summary-view";
import { TranscriptView } from "@/components/transcript-view";
import { getEpisodeLabel } from "@/lib/episode-label";
import type { Episode } from "@/lib/types";

export type ReaderView = "summary" | "transcript";

export function EpisodeReader({ episode, view }: { episode: Episode; view: ReaderView }) {
  const episodeLabel = getEpisodeLabel(episode.episodeNumber, episode.releaseType);
  const guests = episode.guests.map((guest) => guest.name).join("、");
  const hosts = episode.hosts.map((host) => host.name).join("、");

  return (
    <ReaderPreferences>
      <div className={`reader-grid reader-grid-${view}`}>
        {view === "transcript" ? (
          <ChapterRail chapters={episode.chapters} episodeHref={episode.href} />
        ) : null}

        <main id="main-content" className="reader-main" tabIndex={-1}>
          <div className="reader-view-toolbar">
            <ReaderTabs href={episode.href} view={view} />
          </div>
          <MobileReaderTools
            chapters={episode.chapters}
            episodeHref={episode.href}
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
