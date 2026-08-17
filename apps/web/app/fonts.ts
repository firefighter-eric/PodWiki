import { Noto_Serif_SC } from "next/font/google";

export const notoSerifSC = Noto_Serif_SC({
  display: "swap",
  fallback: ["serif"],
  preload: false,
  variable: "--font-noto-serif-sc",
  weight: "variable",
});
