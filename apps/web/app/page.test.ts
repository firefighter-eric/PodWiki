import { beforeEach, describe, expect, it, vi } from "vitest";
import HomePage from "@/app/page";
import { permanentRedirect } from "next/navigation";

vi.mock("next/navigation", () => ({
  permanentRedirect: vi.fn(),
}));

describe("root route", () => {
  beforeEach(() => {
    vi.mocked(permanentRedirect).mockClear();
  });

  it("permanently redirects the canonical entry to the show catalog", () => {
    HomePage();
    expect(permanentRedirect).toHaveBeenCalledWith("/shows");
  });
});
