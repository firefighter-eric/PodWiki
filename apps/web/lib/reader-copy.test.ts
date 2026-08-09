import { describe, expect, it } from "vitest";
import { getEpisodes } from "@/lib/content";
import { getReaderFacingSummary } from "@/lib/reader-copy";

function validSummary({
  readerBoundary = "- 嘉宾陈述尚无独立材料支持。",
  editorRecord = "- 仍需回听并校对专有名词。",
}: {
  readerBoundary?: string;
  editorRecord?: string;
} = {}) {
  return `# 标题

> 状态：\`draft\`。来源 SHA-256：abc。

## 一句话总结

读者摘要。

## 为什么值得听

- 读者理由。

## 核心观点

| 主题 | 判断 |
| --- | --- |
| 示例 | 内容 |

## 5 分钟读完

完整内容。

## 主题导航

- [00:00:00] 开场

## 阅读边界

${readerBoundary}

## 编辑记录（不对读者展示）

${editorRecord}
`;
}

describe("getReaderFacingSummary", () => {
  it("keeps reader sections while removing repository status and editor records", () => {
    const readerSummary = getReaderFacingSummary(validSummary());

    expect(readerSummary).toContain("## 一句话总结");
    expect(readerSummary).toContain("## 阅读边界");
    expect(readerSummary).toContain("嘉宾陈述尚无独立材料支持");
    expect(readerSummary).not.toContain("状态：");
    expect(readerSummary).not.toContain("SHA-256");
    expect(readerSummary).not.toContain("编辑记录");
    expect(readerSummary).not.toContain("回听并校对");
  });

  it("accepts the legacy 整体总结 title in the otherwise strict structure", () => {
    expect(getReaderFacingSummary(validSummary().replace("## 5 分钟读完", "## 整体总结")))
      .toContain("## 整体总结");
  });

  it.each([
    ["missing start", validSummary().replace("## 一句话总结", "## One-line summary")],
    ["missing end", validSummary().replace("## 编辑记录（不对读者展示）", "## Notes")],
    ["legacy mixed boundary", validSummary().replace("## 阅读边界", "## 事实边界与待核实")],
    [
      "wrong order",
      validSummary().replace(
        "## 为什么值得听\n\n- 读者理由。\n\n## 核心观点",
        "## 核心观点\n\n| 主题 | 判断 |\n| --- | --- |\n| 示例 | 内容 |\n\n## 为什么值得听",
      ),
    ],
  ])("rejects a %s instead of exposing an ambiguous document", (_label, markdown) => {
    expect(() => getReaderFacingSummary(markdown)).toThrow(
      "Summary reader sections are missing or out of order",
    );
  });

  it.each([
    "状态为 draft，仍是草稿，待审核。",
    "本稿根据逐字稿整理，仍需回听。",
    "来源 qwen-asr-transformers，SHA-256 为 aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa。",
  ])("rejects editor workflow copy in reader sections: %s", (readerBoundary) => {
    expect(() => getReaderFacingSummary(validSummary({ readerBoundary }))).toThrow(
      "Summary reader content contains editor-only copy",
    );
  });

  it("keeps every published summary free of editor workflow copy", async () => {
    const episodes = await getEpisodes();
    const readerSummaries = episodes.map((episode) => getReaderFacingSummary(episode.summaryRaw));

    expect(readerSummaries).toHaveLength(73);
    expect(readerSummaries.every((summary) => summary.includes("## 阅读边界"))).toBe(true);
    expect(readerSummaries.every((summary) => !summary.includes("## 编辑记录"))).toBe(true);
  });
});
