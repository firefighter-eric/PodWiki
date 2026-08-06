import { CaretDown } from "@phosphor-icons/react/dist/ssr";
import { ReadingControls } from "@/components/reader-preferences";
import type { Chapter } from "@/lib/types";

export function MobileReaderTools({ chapters }: { chapters: Chapter[] }) {
  return (
    <div className="mobile-reader-tools">
      <details>
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
      <details>
        <summary>阅读设置 <CaretDown size={16} /></summary>
        <ReadingControls id="reading-settings-mobile" />
      </details>
    </div>
  );
}
