import { writeFile } from "node:fs/promises";

import { expect, test } from "@playwright/test";

test("renders Chinese headings with the self-hosted serif font on Windows", async ({
  page,
}, testInfo) => {
  expect(process.platform).toBe("win32");

  await page.goto("/shows");
  await expect(page).toHaveTitle(/全部节目/u);
  await page.evaluate(() => document.fonts.ready);

  const heading = page.locator(".catalog-intro h1");
  await expect(heading).toBeVisible();

  const session = await page.context().newCDPSession(page);
  await session.send("DOM.enable");
  await session.send("CSS.enable");
  const documentNode = await session.send("DOM.getDocument") as {
    root: { nodeId: number };
  };
  const headingNode = await session.send("DOM.querySelector", {
    nodeId: documentNode.root.nodeId,
    selector: ".catalog-intro h1",
  }) as { nodeId: number };
  const platformFonts = await session.send("CSS.getPlatformFontsForNode", {
    nodeId: headingNode.nodeId,
  }) as {
    fonts: Array<{
      familyName: string;
      glyphCount: number;
      isCustomFont: boolean;
      postScriptName: string;
    }>;
  };

  const renderedFontNames = platformFonts.fonts
    .map((font) => `${font.familyName} ${font.postScriptName}`)
    .join("\n");
  expect(renderedFontNames).toContain("Noto Serif SC");
  expect(platformFonts.fonts.some((font) => (
    font.isCustomFont && `${font.familyName} ${font.postScriptName}`.includes("Noto Serif SC")
  ))).toBe(true);

  const screenshotPath = testInfo.outputPath("podwiki-font-windows.png");
  const proofPath = testInfo.outputPath("font-proof.json");
  await page.screenshot({ path: screenshotPath, fullPage: true });
  const proof = {
    runnerPlatform: process.platform,
    userAgent: await page.evaluate(() => navigator.userAgent),
    computedFontFamily: await heading.evaluate(
      (element) => getComputedStyle(element).fontFamily,
    ),
    renderedFonts: platformFonts.fonts,
  };
  await writeFile(proofPath, `${JSON.stringify(proof, null, 2)}\n`, "utf8");

  await testInfo.attach("windows-font-rendering", {
    path: screenshotPath,
    contentType: "image/png",
  });
  await testInfo.attach("windows-font-proof", {
    path: proofPath,
    contentType: "application/json",
  });
});
