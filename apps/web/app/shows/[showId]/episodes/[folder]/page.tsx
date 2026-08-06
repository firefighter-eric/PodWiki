import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { ChapterRail } from "@/components/chapter-rail";
import { MobileReaderTools } from "@/components/mobile-reader-tools";
import { ReaderPreferences } from "@/components/reader-preferences";
import { ReaderTabs } from "@/components/reader-tabs";
import { RightRail } from "@/components/right-rail";
import { SummaryView } from "@/components/summary-view";
import { TranscriptView } from "@/components/transcript-view";
import { getEpisode, getEpisodes, timestampToSeconds } from "@/lib/content";
import { getCorePoints, getFirstTimestamp } from "@/lib/markdown";

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
    description: episode.subtitle || `${episode.showTitle}第 ${episode.episodeKey} 期播客总结与逐字稿`,
  };
}

export default async function EpisodePage({ params, searchParams }: EpisodePageProps) {
  const [{ showId, folder }, query] = await Promise.all([params, searchParams]);
  const episode = await getEpisode(showId, folder);
  if (!episode) notFound();

  const rawView = Array.isArray(query.view) ? query.view[0] : query.view;
  const view: "summary" | "transcript" = rawView === "transcript" ? "transcript" : "summary";
  const corePoints = getCorePoints(episode.summaryRaw);
  const highlightedPoint = corePoints.find((point) => point.title.includes("第一性原理")) ?? corePoints[0];
  const targetTimestamp = getFirstTimestamp(highlightedPoint?.body ?? episode.summaryRaw);
  const targetSeconds = targetTimestamp ? timestampToSeconds(targetTimestamp) : 0;
  const activeChapter = episode.chapters.reduce<(typeof episode.chapters)[number] | undefined>(
    (active, chapter) => (chapter.seconds <= targetSeconds ? chapter : active),
    episode.chapters[0],
  );
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
      <div className="reader-grid">
        <ChapterRail
          chapters={episode.chapters}
          activeTimestamp={view === "summary" ? activeChapter?.timestamp : episode.chapters[0]?.timestamp}
        />

        <main id="main-content" className="reader-main" tabIndex={-1}>
          <MobileReaderTools chapters={episode.chapters} />
          <header className="episode-hero">
            <div className="episode-kicker-row">
              <p className="episode-kicker">
                {episode.showTitle}
                <span>·</span>
                {episode.episodeNumber ? `第 ${episode.episodeNumber} 期` : "特别访谈"}
                <span>·</span>
                {episode.durationLabel}
              </p>
              <ReaderTabs href={episode.href} view={view} />
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
