import { expect, test, type Page } from "@playwright/test";

const episodePath = "/shows/latetalk/episodes/178-tian-yuandong";
const legacyEpisodePath = "/shows/luoyonghao/episodes/002-he-xiaopeng";

function watchConsole(page: Page) {
  const failures: string[] = [];
  page.on("console", (message) => {
    if (message.type() === "error" || message.type() === "warning") {
      failures.push(`${message.type()}: ${message.text()}`);
    }
  });
  page.on("pageerror", (error) => failures.push(`pageerror: ${error.message}`));
  return () => expect(failures).toEqual([]);
}

async function openSearch(page: Page) {
  const viewport = page.viewportSize();
  if (viewport && viewport.width <= 960) {
    await page.keyboard.press("Control+K");
  } else {
    await page.getByRole("button", { name: "搜索全文" }).click();
  }
  await expect(page.getByRole("dialog", { name: "搜索全文" })).toBeVisible();
}

test("renders the complete summary, disclosure, and searchable fact boundary", async ({
  page,
  request,
}) => {
  const assertConsoleIsClean = watchConsole(page);
  const rootResponse = await request.get("/", { maxRedirects: 0 });
  expect(rootResponse.status()).toBe(308);

  await page.goto(episodePath);
  await expect(page).toHaveTitle(/田渊栋 · RSI 与 AI 自进化路径/u);
  await expect(page.getByLabel("内容状态")).toContainText("基于机器逐字稿整理，当前为草稿");
  await expect(page.locator("#why-read li")).toHaveCount(4);
  await expect(page.getByRole("heading", {
    name: /RSI 变得可做，关键不是概念新/u,
  })).toBeVisible();
  await expect(page.getByText("嘉宾主张", { exact: true }).first()).toBeVisible();
  await expect(page.getByRole("heading", { name: "事实边界与待核实" })).toBeVisible();
  await expect(page.getByText(/一百五十人临界点/u).first()).toBeVisible();

  const searchResponse = await request.get(
    `/api/search?q=${encodeURIComponent("一百五十人临界点")}`,
  );
  expect(searchResponse.ok()).toBe(true);
  const searchResults = await searchResponse.json() as Array<{ section: string }>;
  expect(searchResults.some((result) => result.section === "总结")).toBe(true);

  if (page.viewportSize()?.width === 390) {
    const hasHorizontalOverflow = await page.evaluate(
      () => document.documentElement.scrollWidth > document.documentElement.clientWidth,
    );
    expect(hasHorizontalOverflow).toBe(false);
  }
  assertConsoleIsClean();
});

test("keeps the keyboard-active search result inside the scroll viewport and restores focus", async ({
  page,
}) => {
  const assertConsoleIsClean = watchConsole(page);
  await page.goto(episodePath);
  await openSearch(page);

  const input = page.getByRole("combobox", { name: "搜索全文" });
  await input.fill("AI");
  const resultList = page.getByRole("listbox", { name: "全文搜索结果" });
  await expect.poll(() => resultList.getByRole("option").count()).toBeGreaterThan(10);

  for (let index = 0; index < 10; index += 1) {
    await input.press("ArrowDown");
  }

  const activeOption = resultList.locator('[role="option"][aria-selected="true"]');
  await expect(activeOption).toHaveAttribute("id", "search-option-10");
  await expect.poll(() => resultList.evaluate((element) => element.scrollTop)).toBeGreaterThan(0);
  const activeIsVisible = await activeOption.evaluate((element) => {
    const optionRect = element.getBoundingClientRect();
    const listRect = element.parentElement?.getBoundingClientRect();
    return Boolean(
      listRect
      && optionRect.top >= listRect.top - 1
      && optionRect.bottom <= listRect.bottom + 1,
    );
  });
  expect(activeIsVisible).toBe(true);

  await input.press("Escape");
  const returnTarget = page.viewportSize()?.width && page.viewportSize()!.width <= 960
    ? page.getByRole("button", { name: "打开节目导航" })
    : page.getByRole("button", { name: "搜索全文" });
  await expect(returnTarget).toBeFocused();
  assertConsoleIsClean();
});

test("traps and restores focus for the 390px navigation drawer", async ({ page }, testInfo) => {
  test.skip(testInfo.project.name !== "chromium-mobile-390", "mobile-only navigation behavior");
  const assertConsoleIsClean = watchConsole(page);
  await page.goto(episodePath);

  const trigger = page.getByRole("button", { name: "打开节目导航" });
  await trigger.click();
  const drawer = page.getByRole("dialog", { name: "节目导航" });
  await expect(drawer).toBeVisible();
  await expect(page.getByRole("button", { name: "关闭节目导航" })).toBeFocused();
  await expect(page.locator(".app-surface")).toHaveAttribute("inert", "");

  await page.keyboard.press("Escape");
  await expect(trigger).toBeFocused();
  await expect(drawer).not.toBeVisible();
  assertConsoleIsClean();
});

test("wraps long inline provenance hashes at 390px", async ({ page }, testInfo) => {
  test.skip(testInfo.project.name !== "chromium-mobile-390", "mobile-only overflow regression");
  const assertConsoleIsClean = watchConsole(page);
  await page.goto(legacyEpisodePath);

  await expect(page.locator("code").filter({
    hasText: "fd05b043c445188b206259145dfba480fc8cd1c3cc308f99052220ecd83d0e0d",
  })).toBeVisible();
  const hasHorizontalOverflow = await page.evaluate(
    () => document.documentElement.scrollWidth > document.documentElement.clientWidth,
  );
  expect(hasHorizontalOverflow).toBe(false);
  assertConsoleIsClean();
});

test("removes spatial search motion when the user requests reduced motion", async ({ page }) => {
  const assertConsoleIsClean = watchConsole(page);
  await page.emulateMedia({ reducedMotion: "reduce" });
  await page.goto(episodePath);
  expect(await page.evaluate(() => matchMedia("(prefers-reduced-motion: reduce)").matches)).toBe(true);

  await openSearch(page);
  const dialog = page.getByRole("dialog", { name: "搜索全文" });
  await expect(dialog).toHaveCSS("transform", "none");
  const spatialKeyframes = await dialog.evaluate((element) => (
    element.getAnimations({ subtree: true }).flatMap((animation) => {
      const effect = animation.effect;
      if (!(effect instanceof KeyframeEffect)) return [];
      return effect.getKeyframes().flatMap((keyframe) => (
        typeof keyframe.transform === "string" && keyframe.transform !== "none"
          ? [keyframe.transform]
          : []
      ));
    })
  ));
  expect(spatialKeyframes).toEqual([]);
  assertConsoleIsClean();
});

test("keeps preferences interactive when localStorage throws SecurityError", async ({
  page,
}, testInfo) => {
  test.skip(testInfo.project.name !== "chromium-desktop", "desktop sidebar control is required");
  const assertConsoleIsClean = watchConsole(page);
  await page.addInitScript(() => {
    const blocked = () => {
      throw new DOMException("Access denied", "SecurityError");
    };
    Object.defineProperty(Storage.prototype, "getItem", { configurable: true, value: blocked });
    Object.defineProperty(Storage.prototype, "setItem", { configurable: true, value: blocked });
  });
  await page.goto(episodePath);

  const collapse = page.getByRole("button", { name: "收起节目栏" });
  await collapse.click();
  await expect(page.getByRole("button", { name: "展开节目栏" })).toBeVisible();
  assertConsoleIsClean();
});
