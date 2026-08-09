const summaryH2 = /^##\s+(.+?)\s*$/gmu;
const expectedSummaryHeadings = [
  "一句话总结",
  "为什么值得听",
  "核心观点",
  ["5 分钟读完", "整体总结"],
  "主题导航",
  "阅读边界",
  "编辑记录（不对读者展示）",
] as const;
const expectedReaderHeadings = expectedSummaryHeadings.slice(0, -1);
const editorCopy = [
  /(?:状态\s*(?:为|：)|当前为|仍是).{0,12}(?:draft|reviewed|machine|草稿|未审核|待审核)/iu,
  /(?:\b(?:source_transcript|selection_status|lineage)\b|SHA-256|[a-f\d]{64})/iu,
  /(?:qwen-asr-transformers|mlx-audio|transcript\.(?:zh-CN|en)\.md|README(?:\.md)?)/iu,
  /(?:PodWiki|本稿|逐字稿|正式稿|\bASR\b)/iu,
  /机器(?:逐字稿|稿|初稿|转写|识别|翻译)/u,
  /(?:草稿|未审核|待审核|待校对|待回听|待核听|人工(?:审核|复核)|正式(?:审核|复核)|回听|核听|校对)/u,
  /`(?:draft|reviewed|machine|selected)`/iu,
  /frozen publisher metadata/iu,
];

function matchesExpectedHeading(actual: string, expected: string | readonly string[]): boolean {
  return typeof expected === "string" ? actual === expected : expected.includes(actual);
}

function assertHeadingStructure(
  markdown: string,
  expectedHeadings: readonly (string | readonly string[])[],
  label: string,
) {
  const headings = [...markdown.matchAll(summaryH2)];
  const structureIsValid = headings.length === expectedHeadings.length
    && headings.every((heading, index) => (
      matchesExpectedHeading(heading[1].trim(), expectedHeadings[index])
    ));
  if (!structureIsValid) {
    const actual = headings.map((heading) => heading[1].trim()).join(" → ") || "无二级标题";
    throw new Error(`${label} sections are missing or out of order: ${actual}`);
  }
  return headings;
}

export function assertReaderFacingSummary(markdown: string): void {
  assertHeadingStructure(markdown, expectedReaderHeadings, "Summary reader");
  const copyForAudit = markdown.replaceAll("ASR—LLM—TTS", "");
  const internalMatch = editorCopy
    .map((pattern) => pattern.exec(copyForAudit))
    .find((match) => match !== null);
  if (internalMatch) {
    throw new Error(`Summary reader content contains editor-only copy: ${internalMatch[0]}`);
  }
}

export function getReaderFacingSummary(markdown: string): string {
  const headings = assertHeadingStructure(markdown, expectedSummaryHeadings, "Summary reader");
  const readerSummary = markdown.slice(headings[0].index!, headings.at(-1)!.index).trim();
  assertReaderFacingSummary(readerSummary);

  return readerSummary;
}
