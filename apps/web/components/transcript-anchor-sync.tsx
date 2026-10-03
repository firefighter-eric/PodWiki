"use client";

import { useEffect } from "react";

const alignmentDelays = [0, 120, 300, 600, 1000] as const;

export function decodeTranscriptAnchor(hash: string): string | undefined {
  const encodedId = hash.replace(/^#/u, "");
  if (!encodedId) return undefined;
  try {
    return decodeURIComponent(encodedId);
  } catch {
    return undefined;
  }
}

export function TranscriptAnchorSync() {
  useEffect(() => {
    let animationFrame: number | undefined;
    let alignmentEnabled = false;
    const timers: number[] = [];
    const passiveOptions = { passive: true } as const;

    const cancelPendingAlignment = () => {
      if (animationFrame !== undefined) window.cancelAnimationFrame(animationFrame);
      animationFrame = undefined;
      timers.splice(0).forEach((timer) => window.clearTimeout(timer));
    };

    const scrollToHash = () => {
      if (!alignmentEnabled) return;
      const id = decodeTranscriptAnchor(window.location.hash);
      if (!id) return;
      const target = document.getElementById(id);
      target?.scrollIntoView({ block: "start", behavior: "instant" });
    };

    const scheduleAlignment = () => {
      if (!alignmentEnabled || animationFrame !== undefined) return;
      animationFrame = window.requestAnimationFrame(() => {
        animationFrame = undefined;
        scrollToHash();
      });
    };

    // Deferred paragraphs and font swaps can change offsets after the timers finish.
    const layoutObserver = new ResizeObserver(scheduleAlignment);

    const stopAlignment = () => {
      alignmentEnabled = false;
      cancelPendingAlignment();
      layoutObserver.disconnect();
    };

    const alignToHash = () => {
      stopAlignment();
      const id = decodeTranscriptAnchor(window.location.hash);
      const target = id ? document.getElementById(id) : null;
      if (!target) return;
      alignmentEnabled = true;
      layoutObserver.observe(target.closest(".transcript-lines") ?? target);
      alignmentDelays.forEach((delay) => {
        const timer = window.setTimeout(scheduleAlignment, delay);
        timers.push(timer);
      });
      void document.fonts.ready.then(scheduleAlignment);
    };

    alignToHash();
    document.fonts.addEventListener("loadingdone", scheduleAlignment);
    window.addEventListener("hashchange", alignToHash);
    window.addEventListener("wheel", stopAlignment, passiveOptions);
    window.addEventListener("touchstart", stopAlignment, passiveOptions);
    window.addEventListener("pointerdown", stopAlignment, passiveOptions);
    window.addEventListener("keydown", stopAlignment);

    return () => {
      stopAlignment();
      document.fonts.removeEventListener("loadingdone", scheduleAlignment);
      window.removeEventListener("hashchange", alignToHash);
      window.removeEventListener("wheel", stopAlignment);
      window.removeEventListener("touchstart", stopAlignment);
      window.removeEventListener("pointerdown", stopAlignment);
      window.removeEventListener("keydown", stopAlignment);
    };
  }, []);

  return null;
}
