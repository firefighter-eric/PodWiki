import { CaretDown } from "@phosphor-icons/react/dist/ssr";
import { ReadingControls } from "@/components/reader-preferences";
import type { Chapter } from "@/lib/types";

export function MobileReaderTools({
  chapters,
  showChapters,
}: {
  chapters: Chapter[];
  showChapters: boolean;
}) {
  return (
    <div className="mobile-reader-tools">
      {showChapters && chapters.length > 0 ? (
        <details className="mobile-chapter-tool" name="reader-tools">
          <summary>章节目录 <CaretDown size={16} /></summary>
          <nav aria-label="移动端章节目录">
            {chapters.map((chapter) => (
              <a key={`${chapter.timestamp}-${chapter.title}`} href={chapter.href}>
                <time>{chapter.timestamp}</time>
                <span>{chapter.title}</span>
              </a>
            ))}
          </nav>
        </details>
      ) : null}
      <details name="reader-tools">
        <summary>阅读设置 <CaretDown size={16} /></summary>
        <ReadingControls id="reading-settings-mobile" />
      </details>
    </div>
  );
}
