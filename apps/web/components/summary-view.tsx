import Link from "next/link";
import { findNearestTranscriptSegment, findRelatedSegments } from "@/lib/content";
import {
  getCorePointDetails,
  getCorePointTable,
  getCorePoints,
  getExtendedSummary,
  getFirstTimestamp,
  getMarkdownSection,
  markdownToHtml,
} from "@/lib/markdown";
import { getTranscriptHref } from "@/lib/reader-routes";
import type { Episode } from "@/lib/types";

function getSummaryStatusCopy(episode: Episode): string | undefined {
  if (episode.workflow.summary === "draft" && episode.workflow.transcript === "machine") {
    return "本页总结基于机器逐字稿整理，当前为草稿；尚待人工核听、专有名词校对与事实复核。";
  }
  if (episode.workflow.summary === "draft") {
    return "本页总结当前为草稿；尚待人工核听与事实复核。";
  }
  if (episode.workflow.transcript === "machine") {
    return "本页所用逐字稿由机器生成；尚待人工核听与校对。";
  }
  return undefined;
}

export async function SummaryView({ episode }: { episode: Episode }) {
  const oneLine = getMarkdownSection(episode.summaryRaw, "一句话总结");
  const whyRead = getMarkdownSection(episode.summaryRaw, "为什么值得听");
  const coreSection = getMarkdownSection(episode.summaryRaw, "核心观点");
  const corePoints = getCorePoints(episode.summaryRaw);
  const corePointTable = getCorePointTable(episode.summaryRaw);
  const corePointDetails = getCorePointDetails(episode.summaryRaw);
  const highlightedPoint = corePoints.find((point) => point.title.includes("第一性原理")) ?? corePoints[0];
  const targetTimestamp = getFirstTimestamp(highlightedPoint?.body ?? episode.summaryRaw);
  const targetSegment = targetTimestamp
    ? findNearestTranscriptSegment(episode.transcriptSegments, targetTimestamp)
    : undefined;
  const relatedSegments = findRelatedSegments(episode, targetTimestamp);
  const extended = getExtendedSummary(episode.summaryRaw);
  const statusCopy = getSummaryStatusCopy(episode);
  const [oneLineHtml, whyReadHtml, corePointDetailsHtml, extendedHtml] = await Promise.all([
    markdownToHtml(oneLine, episode.href, episode.transcriptSegments),
    markdownToHtml(whyRead, episode.href, episode.transcriptSegments),
    markdownToHtml(
      corePointTable ? corePointDetails : coreSection,
      episode.href,
      episode.transcriptSegments,
    ),
    markdownToHtml(extended, episode.href, episode.transcriptSegments),
  ]);

  return (
    <div className="summary-view prose">
      {statusCopy ? (
        <aside className="summary-status-note" aria-label="内容状态">
          <strong>内容状态</strong>
          <span>{statusCopy}</span>
        </aside>
      ) : null}

      <section id="one-line" className="summary-section">
        <h2>一句话总结</h2>
        <div dangerouslySetInnerHTML={{ __html: oneLineHtml }} />
      </section>

      <section id="why-read" className="summary-section">
        <h2>为什么值得听</h2>
        <div dangerouslySetInnerHTML={{ __html: whyReadHtml }} />
      </section>

      <section id="core-points" className="summary-section core-points-summary">
        <h2>核心观点</h2>
        {corePointTable ? (
          <div className="core-points-table-wrap">
            <table className="core-points-table">
              <caption className="sr-only">本期核心观点逻辑表</caption>
              <thead>
                <tr>
                  {corePointTable.columns.map((column) => <th key={column} scope="col">{column}</th>)}
                </tr>
              </thead>
              <tbody>
                {corePointTable.rows.map((row, rowIndex) => (
                  <tr key={`${row[0]}-${rowIndex}`}>
                    {row.map((cell, cellIndex) => (
                      <td key={`${cellIndex}-${cell}`} data-label={corePointTable.columns[cellIndex]}>
                        {cell}
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : null}
        {corePointDetailsHtml ? (
          <div
            className="core-point-details markdown-body"
            dangerouslySetInnerHTML={{ __html: corePointDetailsHtml }}
          />
        ) : null}
      </section>

      {extended ? (
        <section
          id="extended-reading"
          className="extended-summary markdown-body"
          dangerouslySetInnerHTML={{ __html: extendedHtml }}
        />
      ) : null}

      <section id="related-transcript" className="related-transcript">
        <div className="related-heading">
          <h2>相关逐字稿</h2>
          {targetTimestamp ? <span>定位到 <strong>{targetTimestamp}</strong></span> : null}
        </div>
        <div className="related-lines">
          {relatedSegments.map((segment) => (
            <a
              key={segment.id}
              className={`selectable-content-link${segment.id === targetSegment?.id ? " highlighted" : ""}`}
              href={getTranscriptHref(episode.href, segment.id)}
              draggable={false}
            >
              <time>{segment.timestamp}</time>
              <span>{segment.text}</span>
            </a>
          ))}
        </div>
        <Link
          className="full-transcript-link"
          href={getTranscriptHref(episode.href)}
          prefetch={false}
        >
          查看完整逐字稿（共 {episode.transcriptSegments.length.toLocaleString("zh-CN")} 段） →
        </Link>
      </section>
    </div>
  );
}
