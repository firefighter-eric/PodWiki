import localFont from "next/font/local";
import { Noto_Sans_SC } from "next/font/google";

const sfPro = localFont({
  src: "./font-assets/sf-pro-variable.woff2",
  display: "swap",
  adjustFontFallback: false,
  preload: true,
  variable: "--font-sf-pro",
  weight: "1 1000",
});

const notoSansSC = Noto_Sans_SC({
  weight: "variable",
  display: "swap",
  preload: false,
  variable: "--font-noto-sans-sc",
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
  notoSansSC.variable,
  georgia.variable,
  songtiSC.variable,
  sfMono.variable,
].join(" ");
