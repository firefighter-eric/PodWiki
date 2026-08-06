"use client";

import { ArrowRight, MagnifyingGlass, X } from "@phosphor-icons/react";
import { AnimatePresence, m } from "motion/react";
import { useRouter } from "next/navigation";
import {
  useDeferredValue,
  useEffect,
  useMemo,
  useRef,
  useState,
} from "react";
import type { EpisodeCard, SearchResult } from "@/lib/types";

type SearchDialogProps = {
  open: boolean;
  onClose: () => void;
  recentEpisodes: EpisodeCard[];
};

type CommandItem = {
  id: string;
  title: string;
  meta: string;
  snippet: string;
  href: string;
};

export function SearchDialog({ open, onClose, recentEpisodes }: SearchDialogProps) {
  const router = useRouter();
  const inputRef = useRef<HTMLInputElement>(null);
  const dialogRef = useRef<HTMLDivElement>(null);
  const previousFocusRef = useRef<HTMLElement | null>(null);
  const [query, setQuery] = useState("");
  const deferredQuery = useDeferredValue(query.trim());
  const [searchState, setSearchState] = useState<{
    query: string;
    status: "idle" | "loading" | "ready" | "failed";
    results: SearchResult[];
  }>({ query: "", status: "idle", results: [] });
  const [activeIndex, setActiveIndex] = useState(0);
  const [composing, setComposing] = useState(false);

  useEffect(() => {
    if (!open) return;
    previousFocusRef.current = document.activeElement as HTMLElement | null;
    const previousOverflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    window.setTimeout(() => inputRef.current?.focus(), 0);
    return () => {
      document.body.style.overflow = previousOverflow;
      window.requestAnimationFrame(() => previousFocusRef.current?.focus());
    };
  }, [open]);

  useEffect(() => {
    if (!open || !deferredQuery) return;

    const controller = new AbortController();
    const timeout = window.setTimeout(async () => {
      setSearchState({ query: deferredQuery, status: "loading", results: [] });
      try {
        const response = await fetch(`/api/search?q=${encodeURIComponent(deferredQuery)}`, {
          signal: controller.signal,
        });
        if (!response.ok) throw new Error("Search request failed");
        setSearchState({
          query: deferredQuery,
          status: "ready",
          results: (await response.json()) as SearchResult[],
        });
        setActiveIndex(0);
      } catch (error) {
        if (!(error instanceof DOMException && error.name === "AbortError")) {
          setSearchState({ query: deferredQuery, status: "failed", results: [] });
        }
      }
    }, 180);

    return () => {
      window.clearTimeout(timeout);
      controller.abort();
    };
  }, [deferredQuery, open]);

  const stateMatchesQuery = searchState.query === deferredQuery;
  const loading = Boolean(deferredQuery) && (!stateMatchesQuery || searchState.status === "loading");
  const failed = Boolean(deferredQuery) && stateMatchesQuery && searchState.status === "failed";

  const items = useMemo<CommandItem[]>(() => {
    if (deferredQuery) {
      const currentResults = searchState.query === deferredQuery ? searchState.results : [];
      return currentResults.map((result) => ({
        id: result.id,
        title: result.title,
        meta: `${result.showTitle} · ${result.section}${result.timestamp ? ` · ${result.timestamp}` : ""}`,
        snippet: result.snippet,
        href: result.href,
      }));
    }
    return recentEpisodes.map((episode) => ({
      id: episode.id,
      title: episode.displayTitle,
      meta: `${episode.showTitle}${episode.episodeNumber ? ` · 第 ${episode.episodeNumber} 期` : ""}`,
      snippet: episode.subtitle || `${episode.publishedDate} · ${episode.durationLabel}`,
      href: episode.href,
    }));
  }, [deferredQuery, recentEpisodes, searchState]);

  const currentIndex = Math.min(activeIndex, Math.max(0, items.length - 1));

  const navigate = (item: CommandItem | undefined) => {
    if (!item) return;
    onClose();
    router.push(item.href);
  };

  const handleKeyDown = (event: React.KeyboardEvent<HTMLDivElement>) => {
    if (event.key === "Escape") {
      event.preventDefault();
      onClose();
      return;
    }
    if (event.key === "Tab") {
      const focusable = dialogRef.current?.querySelectorAll<HTMLElement>(
        'button:not([disabled]), input:not([disabled]), a[href]',
      );
      if (!focusable?.length) return;
      const first = focusable[0];
      const last = focusable[focusable.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
      return;
    }
    if (composing || items.length === 0) return;
    if (event.key === "ArrowDown") {
      event.preventDefault();
      setActiveIndex((index) => (index + 1) % items.length);
    } else if (event.key === "ArrowUp") {
      event.preventDefault();
      setActiveIndex((index) => (index - 1 + items.length) % items.length);
    } else if (event.key === "Enter" && document.activeElement === inputRef.current) {
      event.preventDefault();
      navigate(items[currentIndex]);
    }
  };

  return (
    <AnimatePresence>
      {open ? (
        <m.div
          className="search-overlay"
          role="presentation"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.16 }}
          onMouseDown={(event) => {
            if (event.target === event.currentTarget) onClose();
          }}
        >
          <m.div
            ref={dialogRef}
            className="search-dialog"
            role="dialog"
            aria-modal="true"
            aria-labelledby="search-title"
            initial={{ opacity: 0, y: -12, scale: 0.985 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: -8, scale: 0.99 }}
            transition={{ duration: 0.18, ease: [0.2, 0.8, 0.2, 1] }}
            onKeyDown={handleKeyDown}
          >
            <div className="search-box">
              <MagnifyingGlass size={22} aria-hidden="true" />
              <label id="search-title" className="sr-only" htmlFor="global-search">搜索全文</label>
              <input
                ref={inputRef}
                id="global-search"
                value={query}
                maxLength={80}
                placeholder="搜索节目、嘉宾、观点或逐字稿…"
                autoComplete="off"
                role="combobox"
                aria-expanded="true"
                aria-controls="search-results"
                aria-activedescendant={items[currentIndex] ? `search-option-${currentIndex}` : undefined}
                onChange={(event) => {
                  setQuery(event.target.value);
                  setActiveIndex(0);
                }}
                onCompositionStart={() => setComposing(true)}
                onCompositionEnd={() => setComposing(false)}
              />
              <button className="icon-button" type="button" aria-label="关闭搜索" onClick={onClose}>
                <X size={19} />
              </button>
            </div>

            <div className="search-result-header">
              <span>{deferredQuery ? "搜索结果" : "最近更新"}</span>
              <span aria-live="polite">
                {loading ? "正在查找…" : deferredQuery ? `${items.length} 条` : ""}
              </span>
            </div>

            <div id="search-results" className="search-results" role="listbox">
              {loading ? (
                <p className="search-state" aria-hidden="true">正在搜索…</p>
              ) : null}
              {failed ? <p className="search-state">搜索暂时不可用，请稍后再试。</p> : null}
              {!failed && deferredQuery && !loading && items.length === 0 ? (
                <p className="search-state">没有找到相关内容，试试人物名或更短的关键词。</p>
              ) : null}
              {!failed && items.map((item, index) => (
                <button
                  key={item.id}
                  id={`search-option-${index}`}
                  className={`search-result${index === currentIndex ? " active" : ""}`}
                  type="button"
                  role="option"
                  aria-selected={index === currentIndex}
                  onMouseMove={() => setActiveIndex(index)}
                  onClick={() => navigate(item)}
                >
                  <span className="search-result-copy">
                    <small>{item.meta}</small>
                    <strong>{item.title}</strong>
                    <span>{item.snippet}</span>
                  </span>
                  <ArrowRight size={18} aria-hidden="true" />
                </button>
              ))}
            </div>

            <p className="search-help">↑↓ 选择 · Enter 打开 · Esc 关闭</p>
          </m.div>
        </m.div>
      ) : null}
    </AnimatePresence>
  );
}
