"use client";

import {
  CaretLeft,
  CaretRight,
  GearSix,
  List,
  MagnifyingGlass,
  SquaresFour,
  X,
} from "@phosphor-icons/react";
import { LazyMotion, domAnimation, m } from "motion/react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useCallback, useEffect, useRef, useState, useSyncExternalStore } from "react";
import type { EpisodeCard, ShowSummary } from "@/lib/types";
import { SearchDialog } from "@/components/search-dialog";

const sidebarStorageKey = "podwiki.sidebar.v1";

type AppShellProps = {
  shows: ShowSummary[];
  episodes: EpisodeCard[];
  children: React.ReactNode;
};

export function AppShell({ shows, episodes, children }: AppShellProps) {
  const pathname = usePathname();
  const subscribeToSidebar = useCallback((callback: () => void) => {
    const handleChange = () => callback();
    window.addEventListener("storage", handleChange);
    window.addEventListener("podwiki-sidebar-change", handleChange);
    return () => {
      window.removeEventListener("storage", handleChange);
      window.removeEventListener("podwiki-sidebar-change", handleChange);
    };
  }, []);
  const collapsed = useSyncExternalStore(
    subscribeToSidebar,
    () => window.localStorage.getItem(sidebarStorageKey) === "collapsed",
    () => false,
  );
  const [mobileOpen, setMobileOpen] = useState(false);
  const [searchOpen, setSearchOpen] = useState(false);
  const mobileTriggerRef = useRef<HTMLButtonElement>(null);
  const sidebarRef = useRef<HTMLElement>(null);
  const activeEpisodeRef = useRef<HTMLAnchorElement>(null);
  const subscribeToMobileViewport = useCallback((callback: () => void) => {
    const media = window.matchMedia("(max-width: 960px)");
    media.addEventListener("change", callback);
    return () => media.removeEventListener("change", callback);
  }, []);
  const isMobile = useSyncExternalStore(
    subscribeToMobileViewport,
    () => window.matchMedia("(max-width: 960px)").matches,
    () => false,
  );
  const isReaderRoute = pathname.includes("/episodes/");
  const totalEpisodes = shows.reduce((total, show) => total + show.episodeCount, 0);

  useEffect(() => {
    const handleShortcut = (event: KeyboardEvent) => {
      if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") {
        event.preventDefault();
        setSearchOpen(true);
      }
    };
    window.addEventListener("keydown", handleShortcut);
    return () => window.removeEventListener("keydown", handleShortcut);
  }, []);

  useEffect(() => {
    if (!mobileOpen || !isMobile) return;
    const animationFrame = window.requestAnimationFrame(() => {
      sidebarRef.current?.querySelector<HTMLElement>(".mobile-close")?.focus();
    });
    return () => window.cancelAnimationFrame(animationFrame);
  }, [isMobile, mobileOpen]);

  useEffect(() => {
    if (isMobile && !mobileOpen) return;
    const animationFrame = window.requestAnimationFrame(() => {
      activeEpisodeRef.current?.scrollIntoView({ block: "nearest" });
    });
    return () => window.cancelAnimationFrame(animationFrame);
  }, [isMobile, mobileOpen, pathname]);

  useEffect(() => {
    if (!mobileOpen || !isMobile) return;
    const previousOverflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    return () => {
      document.body.style.overflow = previousOverflow;
    };
  }, [isMobile, mobileOpen]);

  const toggleCollapsed = () => {
    window.localStorage.setItem(sidebarStorageKey, collapsed ? "expanded" : "collapsed");
    window.dispatchEvent(new Event("podwiki-sidebar-change"));
  };

  const closeMobile = () => {
    setMobileOpen(false);
    window.setTimeout(() => mobileTriggerRef.current?.focus(), 0);
  };

  const handleSidebarKeyDown = (event: React.KeyboardEvent<HTMLElement>) => {
    if (!mobileOpen || !isMobile) return;
    if (event.key === "Escape") {
      event.preventDefault();
      closeMobile();
      return;
    }
    if (event.key !== "Tab") return;
    const focusable = sidebarRef.current?.querySelectorAll<HTMLElement>(
      'button:not([disabled]), a[href]',
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
  };

  return (
    <LazyMotion features={domAnimation}>
      <a className="skip-link" href="#main-content">跳到正文</a>
      <div className={`app-shell${collapsed ? " sidebar-collapsed" : ""}`}>
        <button
          ref={mobileTriggerRef}
          className="mobile-nav-trigger icon-button"
          type="button"
          aria-label="打开节目导航"
          aria-expanded={mobileOpen}
          aria-controls="global-sidebar"
          onClick={() => setMobileOpen(true)}
        >
          <List size={22} weight="regular" />
        </button>

        {mobileOpen ? (
          <m.button
            className="sidebar-scrim"
            type="button"
            aria-label="关闭节目导航"
            onClick={closeMobile}
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
          />
        ) : null}

        <m.aside
          ref={sidebarRef}
          id="global-sidebar"
          className={`global-sidebar${mobileOpen ? " mobile-open" : ""}`}
          aria-label="节目导航"
          aria-hidden={isMobile && !mobileOpen ? true : undefined}
          inert={isMobile && !mobileOpen ? true : undefined}
          onKeyDown={handleSidebarKeyDown}
          layout
          transition={{ duration: 0.2, ease: [0.2, 0.8, 0.2, 1] }}
        >
          <div className="sidebar-header">
            <Link
              className="wordmark"
              href="/shows"
              aria-label="PodWiki 首页"
              onClick={() => setMobileOpen(false)}
            >
              <span className="wordmark-full">PodWiki</span>
              <span className="wordmark-short" aria-hidden="true">P</span>
            </Link>
            <button
              className="collapse-button icon-button desktop-collapse"
              type="button"
              aria-label={collapsed ? "展开节目栏" : "收起节目栏"}
              aria-expanded={!collapsed}
              aria-controls="sidebar-content"
              onClick={toggleCollapsed}
            >
              {collapsed ? <CaretRight size={18} /> : <CaretLeft size={18} />}
            </button>
            <button
              className="collapse-button icon-button mobile-close"
              type="button"
              aria-label="关闭节目导航"
              onClick={closeMobile}
            >
              <X size={18} />
            </button>
          </div>

          <div id="sidebar-content" className="sidebar-content">
            <button
              className="search-trigger"
              type="button"
              aria-label="搜索全文"
              onClick={() => {
                setMobileOpen(false);
                setSearchOpen(true);
              }}
            >
              <MagnifyingGlass size={19} />
              <span className="sidebar-label">搜索全文</span>
              <kbd className="sidebar-shortcut">⌘K</kbd>
            </button>

            <nav className="show-navigation" aria-label="播客单集">
              <div className="sidebar-section-heading sidebar-label">
                <p>具体单集</p>
                <span>{episodes.length} 期</span>
              </div>
              <Link
                className={`show-row all-shows-row${pathname === "/shows" ? " active" : ""}`}
                href="/shows"
                aria-label="全部节目"
                aria-current={pathname === "/shows" ? "page" : undefined}
                onClick={() => setMobileOpen(false)}
              >
                <span className="all-shows-icon" aria-hidden="true">
                  <SquaresFour size={24} />
                </span>
                <span className="show-copy sidebar-label">
                  <strong>全部节目</strong>
                  <small>{totalEpisodes} 期节目</small>
                </span>
              </Link>

              <div className="episode-nav-list">
                {shows.map((show) => {
                  const showEpisodes = episodes.filter((episode) => episode.showId === show.id);
                  const headingId = `episode-group-${show.id}`;
                  return (
                    <section key={show.id} className="episode-show-group" aria-labelledby={headingId}>
                      <h2 id={headingId} className="episode-show-heading sidebar-label">
                        <span>{show.shortTitle}</span>
                        <small>{showEpisodes.length}</small>
                      </h2>
                      <ul>
                        {showEpisodes.map((episode) => {
                          const active = pathname === episode.href;
                          const episodeLabel = episode.episodeNumber === null
                            ? "特访"
                            : `#${String(episode.episodeNumber).padStart(3, "0")}`;
                          return (
                            <li key={episode.id}>
                              <Link
                                ref={active ? activeEpisodeRef : undefined}
                                className={`episode-nav-row${active ? " active" : ""}`}
                                href={episode.href}
                                aria-label={`${show.title} ${episodeLabel} ${episode.navigationTitle}`}
                                aria-current={active ? "page" : undefined}
                                onClick={() => setMobileOpen(false)}
                              >
                                <span className="episode-nav-index" aria-hidden="true">
                                  {episodeLabel}
                                </span>
                                <span className="episode-nav-copy sidebar-label">
                                  <strong>{episode.navigationTitle}</strong>
                                  <small>{episode.publishedDate} · {episode.durationLabel}</small>
                                </span>
                              </Link>
                            </li>
                          );
                        })}
                      </ul>
                    </section>
                  );
                })}
              </div>
            </nav>
          </div>

          {isReaderRoute ? (
            <a
              className="sidebar-settings"
              href="#reading-settings"
              aria-label="阅读设置"
              onClick={() => setMobileOpen(false)}
            >
              <GearSix size={20} />
              <span className="sidebar-label">阅读设置</span>
              <CaretRight className="sidebar-label settings-caret" size={18} />
            </a>
          ) : null}
        </m.aside>

        <div className="app-surface">{children}</div>
      </div>

      <SearchDialog
        open={searchOpen}
        onClose={() => setSearchOpen(false)}
        recentEpisodes={episodes.slice(0, 8)}
      />
    </LazyMotion>
  );
}
