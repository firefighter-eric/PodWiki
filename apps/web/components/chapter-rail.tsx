import type { Chapter } from "@/lib/types";
import { getTranscriptHref } from "@/lib/reader-routes";

export function ChapterRail({ chapters, episodeHref }: { chapters: Chapter[]; episodeHref: string }) {
  return (
    <aside id="chapter-list" className="chapter-rail" aria-label="章节目录">
      <p className="rail-title">章节目录</p>
      <nav>
        {chapters.map((chapter) => (
          <a
            key={`${chapter.timestamp}-${chapter.title}`}
            className="chapter-link selectable-content-link"
            href={getTranscriptHref(episodeHref, chapter.href)}
            draggable={false}
          >
            <time>{chapter.timestamp}</time>
            <span>{chapter.title}</span>
          </a>
        ))}
      </nav>
    </aside>
  );
}
