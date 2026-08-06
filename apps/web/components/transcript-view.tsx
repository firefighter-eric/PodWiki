import Link from "next/link";
import type { Episode } from "@/lib/types";
import { TranscriptAnchorSync } from "@/components/transcript-anchor-sync";

export function TranscriptView({ episode }: { episode: Episode }) {
  return (
    <section id="full-transcript" className="transcript-view">
      <TranscriptAnchorSync />
      <div className="transcript-heading">
        <div>
          <p className="section-kicker">机器逐字稿 · {episode.transcriptSegments.length.toLocaleString("zh-CN")} 段</p>
          <h2>完整逐字稿</h2>
        </div>
        <Link href={`${episode.href}?view=summary`}>返回总结</Link>
      </div>
      <p className="transcript-notice">
        当前文本由语音识别生成，尚未完成说话人标注与逐句人工校对。时间码仅用于阅读定位。
      </p>
      <div className="transcript-lines">
        {episode.transcriptSegments.map((segment) => (
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
