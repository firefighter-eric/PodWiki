import { describe, expect, it } from "vitest";
import { getWebVisibleSummaryMarkdown } from "@/lib/summary-visibility";

describe("getWebVisibleSummaryMarkdown", () => {
  it("removes the fact-boundary section from the public summary", () => {
    const markdown = [
      "## 5 分钟读完",
      "",
      "公开正文。",
      "",
      "## 主题导航",
      "",
      "- 公开导航",
      "",
      "## 事实边界与待核实",
      "",
      "- 内部核验说明",
    ].join("\n");

    expect(getWebVisibleSummaryMarkdown(markdown)).toBe([
      "## 5 分钟读完",
      "",
      "公开正文。",
      "",
      "## 主题导航",
      "",
      "- 公开导航",
    ].join("\n"));
  });

  it("supports the 事项 heading variant without removing later sections", () => {
    const markdown = [
      "## 整体总结",
      "",
      "公开正文。",
      "",
      "## 事实边界与待核实事项",
      "",
      "- 内部核验说明",
      "",
      "## 延伸阅读",
      "",
      "继续公开。",
    ].join("\n");

    expect(getWebVisibleSummaryMarkdown(markdown)).toBe([
      "## 整体总结",
      "",
      "公开正文。",
      "",
      "## 延伸阅读",
      "",
      "继续公开。",
    ].join("\n"));
  });

  it.each([
    "证据、推断与人工审核边界",
    "证据、推断与人工复核边界",
  ])("removes the %s heading variant", (heading) => {
    const markdown = `## 主题导航\n\n- 公开导航\n\n## ${heading}\n\n- 内部核验说明`;
    expect(getWebVisibleSummaryMarkdown(markdown)).toBe("## 主题导航\n\n- 公开导航");
  });

  it("leaves unrelated summary headings unchanged", () => {
    const markdown = [
      "## 事实说明",
      "",
      "正文里提到待核实不应被删除。",
      "",
      "### 事实边界与待核实",
      "",
      "三级标题也应保留。",
    ].join("\n");
    expect(getWebVisibleSummaryMarkdown(markdown)).toBe(markdown);
  });
});
