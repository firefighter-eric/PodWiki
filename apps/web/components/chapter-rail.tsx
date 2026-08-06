import type { Chapter } from "@/lib/types";

export function ChapterRail({
  chapters,
  activeTimestamp,
}: {
  chapters: Chapter[];
  activeTimestamp?: string;
}) {
  return (
    <aside id="chapter-list" className="chapter-rail" aria-label="章节目录">
      <p className="rail-title">章节目录</p>
      <nav>
        {chapters.map((chapter) => {
          const active = chapter.timestamp === activeTimestamp;
          return (
            <a
              key={`${chapter.timestamp}-${chapter.title}`}
              className={`chapter-link${active ? " active" : ""}`}
              href={chapter.href}
              aria-current={active ? "location" : undefined}
            >
              <time>{chapter.timestamp}</time>
              <span>{chapter.title}</span>
            </a>
          );
        })}
      </nav>
    </aside>
  );
}
