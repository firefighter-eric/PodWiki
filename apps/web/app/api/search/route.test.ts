import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { afterEach, describe, expect, it, vi } from "vitest";

afterEach(() => {
  vi.restoreAllMocks();
  vi.resetModules();
});

describe("search API route", () => {
  it("serves the generated index from an empty working directory", async () => {
    const emptyWorkingDirectory = fs.mkdtempSync(path.join(os.tmpdir(), "podwiki-search-cwd-"));
    const readFileSync = vi.spyOn(fs, "readFileSync");
    const readdirSync = vi.spyOn(fs, "readdirSync");
    vi.spyOn(process, "cwd").mockReturnValue(emptyWorkingDirectory);

    try {
      vi.resetModules();
      const { GET } = await import("@/app/api/search/route");
      const response = await GET(new Request(
        `https://podwiki.example/api/search?q=${encodeURIComponent("田渊栋")}`,
      ));
      const results = await response.json() as Array<{ id: string }>;

      expect(response.status).toBe(200);
      expect(results).toContainEqual(expect.objectContaining({
        id: "latetalk:178:episode",
      }));
      const sourceReads = [...readFileSync.mock.calls, ...readdirSync.mock.calls]
        .flatMap(([file]) => typeof file === "string" ? [file] : [])
        .filter((file) => file.split(path.sep).includes("shows"));
      expect(sourceReads).toEqual([]);
    } finally {
      fs.rmSync(emptyWorkingDirectory, { recursive: true, force: true });
    }
  }, 15_000);
});
