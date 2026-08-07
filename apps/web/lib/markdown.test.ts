import { describe, expect, it } from "vitest";
import { markdownToHtml } from "@/lib/markdown";

describe("markdownToHtml", () => {
  it("keeps safe links while removing executable URL protocols", async () => {
    const html = await markdownToHtml(
      [
        "[站内链接](/shows)",
        "[安全外链](https://example.com)",
        "时间码 [00:01:02]",
        "[脚本链接](javascript:alert(1))",
        "[数据链接](data:text/html,<script>alert(1)</script>)",
      ].join("\n\n"),
      "/shows/example/episodes/1",
    );

    expect(html).toContain('href="/shows"');
    expect(html).toContain('href="https://example.com"');
    expect(html).toContain(
      'href="/shows/example/episodes/1/transcript#t-00-01-02"',
    );
    expect(html).not.toContain("javascript:");
    expect(html).not.toContain("data:text/html");
    expect(html).not.toContain("<script");
  });

  it("keeps generated heading anchors and GFM tables", async () => {
    const html = await markdownToHtml(
      [
        "## 核心观点",
        "",
        "| 维度 | 判断 |",
        "| --- | --- |",
        "| 路线 | 先验证 |",
      ].join("\n"),
      "/shows/example/episodes/1",
    );

    expect(html).toContain("<h2 id=\"user-content-核心观点\">核心观点</h2>");
    expect(html).toContain("<table>");
    expect(html).toContain("<th>维度</th>");
  });
});
