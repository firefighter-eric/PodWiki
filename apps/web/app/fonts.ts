import localFont from "next/font/local";

const sfPro = localFont({
  src: "./font-assets/sf-pro-variable.woff2",
  display: "swap",
  adjustFontFallback: false,
  preload: true,
  variable: "--font-sf-pro",
  weight: "1 1000",
});

const pingFangSC = localFont({
  src: [
    { path: "./font-assets/pingfang-sc-400.woff2", weight: "400", style: "normal" },
    { path: "./font-assets/pingfang-sc-500.woff2", weight: "500", style: "normal" },
    { path: "./font-assets/pingfang-sc-600.woff2", weight: "600", style: "normal" },
    { path: "./font-assets/pingfang-sc-700.woff2", weight: "700", style: "normal" },
  ],
  display: "swap",
  adjustFontFallback: false,
  preload: false,
  variable: "--font-pingfang-sc",
});

const georgia = localFont({
  src: [
    { path: "./font-assets/georgia-regular.woff2", weight: "400", style: "normal" },
    { path: "./font-assets/georgia-bold.woff2", weight: "700", style: "normal" },
  ],
  display: "swap",
  adjustFontFallback: false,
  preload: true,
  variable: "--font-georgia",
});

const songtiSC = localFont({
  src: [
    { path: "./font-assets/songti-sc-regular.woff2", weight: "400", style: "normal" },
    { path: "./font-assets/songti-sc-bold.woff2", weight: "700", style: "normal" },
  ],
  display: "swap",
  adjustFontFallback: false,
  preload: false,
  variable: "--font-songti-sc",
});

const sfMono = localFont({
  src: "./font-assets/sf-mono-variable.woff2",
  display: "swap",
  adjustFontFallback: false,
  preload: false,
  variable: "--font-sf-mono",
  weight: "295 900",
});

export const fontVariables = [
  sfPro.variable,
  pingFangSC.variable,
  georgia.variable,
  songtiSC.variable,
  sfMono.variable,
].join(" ");
