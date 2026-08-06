import { ArrowSquareOut } from "@phosphor-icons/react/dist/ssr";
import Link from "next/link";
import { getEpisodeLabel } from "@/lib/episode-label";
import type { Episode } from "@/lib/types";
import { ReadingControls } from "@/components/reader-preferences";

const summaryNavigation = [
  ["#one-line", "一句话总结"],
  ["#why-read", "为什么值得读"],
  ["#core-points", "核心观点"],
  ["#extended-reading", "5 分钟读完"],
  ["#related-transcript", "相关逐字稿"],
] as const;

export function RightRail({ episode, view }: { episode: Episode; view: "summary" | "transcript" }) {
  const episodeLabel = getEpisodeLabel(episode.episodeNumber);

  return (
    <aside className="right-rail" aria-label="阅读辅助信息">
      <section className="right-section source-section">
        <h2>内容来源</h2>
        <p>{episode.showTitle}</p>
        <p>{episodeLabel} · {episode.publishedDate}</p>
        {episode.preferredSource ? (
          <a href={episode.preferredSource.url} target="_blank" rel="noreferrer">
            查看原始来源 <ArrowSquareOut size={15} />
          </a>
        ) : null}
      </section>

      <section className="right-section">
        <h2>阅读设置</h2>
        <ReadingControls id="reading-settings" />
      </section>

      <section className="right-section page-navigation">
        <h2>页面导航</h2>
        <nav>
          {view === "summary" ? summaryNavigation.map(([href, label]) => (
            <a key={href} href={href}>{label}</a>
          )) : (
            <>
              <a className="active" href="#full-transcript">
                {episode.bilingualTranscript ? "中英对照逐字稿" : "完整逐字稿"}
              </a>
              <Link href={`${episode.href}?view=summary`}>返回总结</Link>
            </>
          )}
        </nav>
      </section>
    </aside>
  );
}
