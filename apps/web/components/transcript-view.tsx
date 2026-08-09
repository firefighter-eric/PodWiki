import Link from "next/link";
import type { Episode } from "@/lib/types";
import { TranscriptAnchorSync } from "@/components/transcript-anchor-sync";

export function TranscriptView({ episode }: { episode: Episode }) {
  const bilingualTranscript = episode.bilingualTranscript;
  const segmentCount = bilingualTranscript?.segments.length ?? episode.transcriptSegments.length;

  return (
    <section id="full-transcript" className="transcript-view">
      <TranscriptAnchorSync />
      <div className="transcript-heading">
        <div>
          <p className="section-kicker">
            {segmentCount.toLocaleString("zh-CN")} 段
          </p>
          <h2>{bilingualTranscript ? "中英对照逐字稿" : "完整逐字稿"}</h2>
        </div>
        <Link href={episode.href}>返回总结</Link>
      </div>
      <div className={`transcript-lines${bilingualTranscript ? " bilingual-transcript-lines" : ""}`}>
        {bilingualTranscript ? bilingualTranscript.segments.map((segment) => (
          <p key={segment.id} id={segment.id} className="transcript-line bilingual-transcript-line">
            <a
              href={`#${segment.id}`}
              tabIndex={-1}
              aria-label={`定位到 ${segment.timestamp}`}
            >
              {segment.timestamp}
            </a>
            <span className="transcript-pair">
              <span className="transcript-source" lang="en">{segment.sourceText}</span>
              <span className="transcript-translation" lang="zh-CN">{segment.translationText}</span>
            </span>
          </p>
        )) : episode.transcriptSegments.map((segment) => (
          <p key={segment.id} id={segment.id} className="transcript-line">
            <a
              href={`#${segment.id}`}
              tabIndex={-1}
              aria-label={`定位到 ${segment.timestamp}`}
            >
              {segment.timestamp}
            </a>
            <span>{segment.text}</span>
          </p>
        ))}
      </div>
    </section>
  );
}
