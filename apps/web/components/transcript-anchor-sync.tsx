"use client";

import { useEffect } from "react";

const alignmentDelays = [0, 120, 300, 600, 1000] as const;

export function TranscriptAnchorSync() {
  useEffect(() => {
    const animationFrames: number[] = [];
    const timers: number[] = [];
    const passiveOptions = { passive: true } as const;

    const cancelPendingAlignment = () => {
      animationFrames.splice(0).forEach((frame) => window.cancelAnimationFrame(frame));
      timers.splice(0).forEach((timer) => window.clearTimeout(timer));
    };

    const scrollToHash = () => {
      const id = decodeURIComponent(window.location.hash.slice(1));
      if (!id) return;
      const target = document.getElementById(id);
      target?.scrollIntoView({ block: "start" });
    };

    const alignToHash = () => {
      cancelPendingAlignment();
      alignmentDelays.forEach((delay) => {
        const timer = window.setTimeout(() => {
          animationFrames.push(window.requestAnimationFrame(scrollToHash));
        }, delay);
        timers.push(timer);
      });
    };

    alignToHash();
    window.addEventListener("hashchange", alignToHash);
    window.addEventListener("wheel", cancelPendingAlignment, passiveOptions);
    window.addEventListener("touchstart", cancelPendingAlignment, passiveOptions);
    window.addEventListener("pointerdown", cancelPendingAlignment, passiveOptions);
    window.addEventListener("keydown", cancelPendingAlignment);

    return () => {
      cancelPendingAlignment();
      window.removeEventListener("hashchange", alignToHash);
      window.removeEventListener("wheel", cancelPendingAlignment);
      window.removeEventListener("touchstart", cancelPendingAlignment);
      window.removeEventListener("pointerdown", cancelPendingAlignment);
      window.removeEventListener("keydown", cancelPendingAlignment);
    };
  }, []);

  return null;
}
