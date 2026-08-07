import { NoteBlank, Quotes } from "@phosphor-icons/react/dist/ssr";
import Link from "next/link";
import { getTranscriptHref } from "@/lib/reader-routes";

export function ReaderTabs({ href, view }: { href: string; view: "summary" | "transcript" }) {
  return (
    <nav className="reader-tabs" aria-label="内容视图">
      <Link href={href} aria-current={view === "summary" ? "page" : undefined}>
        <NoteBlank size={16} />
        总结
      </Link>
      <Link href={getTranscriptHref(href)} aria-current={view === "transcript" ? "page" : undefined}>
        <Quotes size={16} />
        逐字稿
      </Link>
    </nav>
  );
}
