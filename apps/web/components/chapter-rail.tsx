import type { Chapter } from "@/lib/types";

export function ChapterRail({ chapters }: { chapters: Chapter[] }) {
  return (
    <aside id="chapter-list" className="chapter-rail" aria-label="章节目录">
      <p className="rail-title">章节目录</p>
      <nav>
        {chapters.map((chapter) => (
          <a
            key={`${chapter.timestamp}-${chapter.title}`}
            className="chapter-link"
            href={chapter.href}
          >
            <time>{chapter.timestamp}</time>
            <span>{chapter.title}</span>
          </a>
        ))}
      </nav>
    </aside>
  );
}
