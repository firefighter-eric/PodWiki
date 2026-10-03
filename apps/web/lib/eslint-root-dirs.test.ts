import fs from "node:fs";
import { createRequire } from "node:module";
import os from "node:os";
import path from "node:path";
import { afterEach, beforeEach, describe, expect, it } from "vitest";

const require = createRequire(import.meta.url);
const { getRootDirs } = require("@next/eslint-plugin-next/dist/utils/get-root-dirs") as {
  getRootDirs: (context: {
    cwd: string;
    settings: { next?: { rootDir?: string | string[] } };
  }) => string[];
};

describe("Next ESLint root directory discovery with the glob override", () => {
  let fixture: string;

  beforeEach(() => {
    fixture = fs.mkdtempSync(path.join(os.tmpdir(), "podwiki-eslint-roots-")).replaceAll("\\", "/");
    for (const directory of ["apps/reader", "apps/editor", "packages/site"]) {
      fs.mkdirSync(path.join(fixture, directory), { recursive: true });
    }
    fs.writeFileSync(path.join(fixture, "apps", "README.md"), "fixture");
  });

  afterEach(() => {
    fs.rmSync(fixture, { recursive: true, force: true });
  });

  it("retains the working directory when no rootDir is configured", () => {
    expect(getRootDirs({ cwd: fixture, settings: {} })).toEqual([fixture]);
  });

  it("selects a literal root without expanding descendant directories", () => {
    expect(getRootDirs({
      cwd: fixture,
      settings: { next: { rootDir: fixture } },
    })).toEqual([fixture]);
  });

  it("expands monorepo root globs while excluding files", () => {
    const relativeFixture = path.relative(process.cwd(), fixture).replaceAll("\\", "/");
    for (const root of [fixture, relativeFixture]) {
      const roots = getRootDirs({
        cwd: fixture,
        settings: { next: { rootDir: `${root}/apps/*` } },
      });

      expect(roots.sort()).toEqual([
        `${root}/apps/editor`,
        `${root}/apps/reader`,
      ]);
    }
  });

  it("supports arrays, brace patterns, and normalized Windows separators", () => {
    const roots = getRootDirs({
      cwd: fixture,
      settings: {
        next: {
          rootDir: [
            `${fixture}/apps/{reader,editor}`.replaceAll("/", "\\"),
            `${fixture}/packages/site`,
          ],
        },
      },
    });

    expect(roots.sort()).toEqual([
      `${fixture}/apps/editor`,
      `${fixture}/apps/reader`,
      `${fixture}/packages/site`,
    ]);
  });
});
