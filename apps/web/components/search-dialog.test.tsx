import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it, vi } from "vitest";
import { SearchDialog } from "@/components/search-dialog";
import { getEpisodes } from "@/lib/content";

vi.mock("next/navigation", () => ({
  useRouter: () => ({ push: vi.fn() }),
}));

describe("search dialog navigation", () => {
  it("renders selectable native links for result content", async () => {
    const [episode] = await getEpisodes();
    const html = renderToStaticMarkup(createElement(SearchDialog, {
      open: true,
      onClose: vi.fn(),
      recentEpisodes: [episode],
    }));

    expect(html).toContain(`href="${episode.href}"`);
    expect(html).toMatch(
      /<a[^>]*class="search-result selectable-content-link active"[^>]*draggable="false"/,
    );
    expect(html).not.toContain('<button id="search-option-0"');
  });
});
