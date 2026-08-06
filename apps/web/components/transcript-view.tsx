import Link from "next/link";
import type { Episode } from "@/lib/types";
import { TranscriptAnchorSync } from "@/components/transcript-anchor-sync";

export function TranscriptView({ episode }: { episode: Episode }) {
  const bilingualTranscript = episode.bilingualTranscript;
  const segmentCount = bilingualTranscript?.segments.length ?? episode.transcriptSegments.length;
  const translationStatus = bilingualTranscript
    ? {
        machine: "机器翻译 · 未审核",
        edited: "机器翻译 · 已编辑",
        reviewed: "中文译稿 · 已审核",
      }[bilingualTranscript.status]
    : undefined;

  return (
    <section id="full-transcript" className="transcript-view">
      <TranscriptAnchorSync />
      <div className="transcript-heading">
        <div>
          <p className="section-kicker">
            {bilingualTranscript ? "英文原稿 + 中文译稿" : "机器逐字稿"}
            {" · "}{segmentCount.toLocaleString("zh-CN")} 段
          </p>
          <h2>{bilingualTranscript ? "中英对照逐字稿" : "完整逐字稿"}</h2>
        </div>
        <Link href={`${episode.href}?view=summary`}>返回总结</Link>
      </div>
      <p className="transcript-notice">
        {bilingualTranscript ? (
          <>
            <strong>{translationStatus}</strong>
            英文原稿由语音识别生成，中文译文按相同时间码逐行对齐；原稿与译稿均请结合音频复核。
          </>
        ) : (
          <>当前文本由语音识别生成，尚未完成说话人标注与逐句人工校对。时间码仅用于阅读定位。</>
        )}
      </p>
      <div className={`transcript-lines${bilingualTranscript ? " bilingual-transcript-lines" : ""}`}>
        {bilingualTranscript ? bilingualTranscript.segments.map((segment) => (
          <p key={segment.id} id={segment.id} className="transcript-line bilingual-transcript-line">
            <a href={`#${segment.id}`} aria-label={`定位到 ${segment.timestamp}`}>
              {segment.timestamp}
            </a>
            <span className="transcript-pair">
              <span className="transcript-source" lang="en">{segment.sourceText}</span>
              <span className="transcript-translation" lang="zh-CN">{segment.translationText}</span>
            </span>
          </p>
        )) : episode.transcriptSegments.map((segment) => (
          <p key={segment.id} id={segment.id} className="transcript-line">
            <a href={`#${segment.id}`} aria-label={`定位到 ${segment.timestamp}`}>
              {segment.timestamp}
            </a>
            <span>{segment.text}</span>
          </p>
        ))}
      </div>
    </section>
  );
}
