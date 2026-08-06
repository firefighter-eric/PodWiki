import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { ChapterRail } from "@/components/chapter-rail";
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
    title: episode.displayTitle,
    description: getEpisodeDescription(episode),
  };
}

export default async function EpisodePage({ params, searchParams }: EpisodePageProps) {
  const [{ showId, folder }, query] = await Promise.all([params, searchParams]);
  const episode = await getEpisode(showId, folder);
  if (!episode) notFound();

  const rawView = Array.isArray(query.view) ? query.view[0] : query.view;
  const view: "summary" | "transcript" = rawView === "transcript" ? "transcript" : "summary";
  const guests = episode.guests.map((guest) => guest.name).join("、");
  const hosts = episode.hosts.map((host) => host.name).join("、");
  const transcriptStatus = episode.bilingualTranscript
    ? {
        machine: "总结初稿 · 中英对照含机器翻译（未审核）",
        edited: "总结初稿 · 中英对照译稿已编辑",
        reviewed: "总结初稿 · 中英对照译稿已审核",
      }[episode.bilingualTranscript.status]
    : "总结初稿 · 逐字稿由机器生成";

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
                <span>·</span>
                {getEpisodeLabel(episode.episodeNumber)}
                <span>·</span>
                {episode.durationLabel}
              </p>
            </div>
            <h1>{episode.displayTitle}</h1>
            {episode.subtitle ? <p className="episode-subtitle">{episode.subtitle}</p> : null}
            <p className="episode-byline">
              {guests ? <span>嘉宾：{guests}</span> : null}
              {hosts ? <span>主持人：{hosts}</span> : null}
              <time dateTime={episode.publishedAt}>{episode.publishedDate}</time>
            </p>
            <div className="episode-status">
              <span><i aria-hidden="true" />{transcriptStatus}</span>
              <span>基于仓库内容构建</span>
            </div>
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
