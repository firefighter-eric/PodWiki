"use client";

import { useEffect } from "react";

export function TranscriptAnchorSync() {
  useEffect(() => {
    let secondFrame = 0;
    const scrollToHash = () => {
      const id = decodeURIComponent(window.location.hash.slice(1));
      if (!id) return;
      const target = document.getElementById(id);
      target?.scrollIntoView({ block: "start" });
    };
    const firstFrame = window.requestAnimationFrame(() => {
      secondFrame = window.requestAnimationFrame(scrollToHash);
    });
    window.addEventListener("hashchange", scrollToHash);
    return () => {
      window.cancelAnimationFrame(firstFrame);
      window.cancelAnimationFrame(secondFrame);
      window.removeEventListener("hashchange", scrollToHash);
    };
  }, []);

  return null;
}
