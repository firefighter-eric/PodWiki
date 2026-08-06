import { ArrowSquareOut } from "@phosphor-icons/react/dist/ssr";
import Link from "next/link";
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
  return (
    <aside className="right-rail" aria-label="阅读辅助信息">
      <section className="right-section source-section">
        <h2>内容来源</h2>
        <p>{episode.showTitle}</p>
        <p>第 {episode.episodeNumber ?? episode.episodeKey} 期 · {episode.publishedDate}</p>
        <p className="source-note">
          {episode.summarySourceTranscript?.selectionStatus === "superseded"
            ? "总结基于归档 Whisper 稿；时间码已近邻映射到当前逐字稿。"
            : "内容依据发布页与当前机器逐字稿整理，关键信息仍需人工核查。"}
        </p>
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
            <a key={href} href={href} className={href === "#related-transcript" ? "active" : undefined}>
              {label}
            </a>
          )) : (
            <>
              <a className="active" href="#full-transcript">完整逐字稿</a>
              <Link href={`${episode.href}?view=summary`}>返回总结</Link>
            </>
          )}
          <a href="#chapter-list">章节目录</a>
        </nav>
      </section>
    </aside>
  );
}
