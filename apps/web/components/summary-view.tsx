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
import { getReaderFacingSummary } from "@/lib/reader-copy";
import { getTranscriptHref } from "@/lib/reader-routes";
import type { Episode } from "@/lib/types";

export async function SummaryView({ episode }: { episode: Episode }) {
  const readerSummary = getReaderFacingSummary(episode.summaryRaw);
  const oneLine = getMarkdownSection(readerSummary, "一句话总结");
  const whyRead = getMarkdownSection(readerSummary, "为什么值得听");
  const coreSection = getMarkdownSection(readerSummary, "核心观点");
  const corePoints = getCorePoints(readerSummary);
  const corePointTable = getCorePointTable(readerSummary);
  const corePointDetails = getCorePointDetails(readerSummary);
  const highlightedPoint = corePoints.find((point) => point.title.includes("第一性原理")) ?? corePoints[0];
  const targetTimestamp = getFirstTimestamp(highlightedPoint?.body ?? readerSummary);
  const targetSegment = targetTimestamp
    ? findNearestTranscriptSegment(episode.transcriptSegments, targetTimestamp)
    : undefined;
  const relatedSegments = findRelatedSegments(episode, targetTimestamp);
  const extended = getExtendedSummary(readerSummary);
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
