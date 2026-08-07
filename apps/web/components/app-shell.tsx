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
import dynamic from "next/dynamic";
import Link from "next/link";
import { usePathname } from "next/navigation";
import {
  useCallback,
  useEffect,
  useLayoutEffect,
  useRef,
  useState,
  useSyncExternalStore,
} from "react";
import { EpisodeSidebarTitle } from "@/components/episode-navigation-title";
import type { ShowSummary, SidebarEpisode } from "@/lib/types";
import {
  getInitialSidebarScope,
  getSidebarCatalogScope,
  getSidebarEpisodeAriaLabel,
  getSidebarEpisodes,
  getSidebarScopeShowId,
  retainSidebarScope,
} from "@/lib/sidebar-episodes";

const sidebarStorageKey = "podwiki.sidebar.v1";
const SearchDialog = dynamic(() =>
  import("@/components/search-dialog").then((module) => module.SearchDialog),
);

type AppShellProps = {
  shows: ShowSummary[];
  episodes: SidebarEpisode[];
  children: React.ReactNode;
};

function sidebarIsCollapsed(): boolean {
  return window.localStorage.getItem(sidebarStorageKey) === "collapsed";
}

function syncSidebarDocumentState() {
  document.documentElement.dataset.sidebarState = sidebarIsCollapsed()
    ? "collapsed"
    : "expanded";
}

function preserveSelectableLinkText(event: React.MouseEvent<HTMLDivElement>) {
  if (
    event.detail === 0
    || event.metaKey
    || event.ctrlKey
    || event.shiftKey
    || event.altKey
    || !(event.target instanceof Element)
  ) return;

  const link = event.target.closest<HTMLAnchorElement>("a.selectable-content-link");
  if (!link || !event.currentTarget.contains(link)) return;

  const selection = window.getSelection();
  if (!selection || selection.isCollapsed) return;

  if (
    (selection.anchorNode && link.contains(selection.anchorNode))
    || (selection.focusNode && link.contains(selection.focusNode))
  ) {
    event.preventDefault();
  }
}

export function AppShell({ shows, episodes, children }: AppShellProps) {
  const pathname = usePathname();
  const catalogScope = getSidebarCatalogScope(pathname, shows);
  const [sidebarScopeState, setSidebarScopeState] = useState(() => ({
    catalogScope,
    retainedScope: getInitialSidebarScope(pathname, shows),
  }));
  if (catalogScope !== sidebarScopeState.catalogScope) {
    setSidebarScopeState({
      catalogScope,
      retainedScope: retainSidebarScope(sidebarScopeState.retainedScope, catalogScope),
    });
  }
  const sidebarScope = catalogScope ?? sidebarScopeState.retainedScope;
  const subscribeToSidebar = useCallback((callback: () => void) => {
    const handleChange = () => {
      syncSidebarDocumentState();
      callback();
    };
    window.addEventListener("storage", handleChange);
    window.addEventListener("podwiki-sidebar-change", handleChange);
    return () => {
      window.removeEventListener("storage", handleChange);
      window.removeEventListener("podwiki-sidebar-change", handleChange);
    };
  }, []);
  const collapsed = useSyncExternalStore(
    subscribeToSidebar,
    sidebarIsCollapsed,
    () => false,
  );
  const [mobileOpen, setMobileOpen] = useState(false);
  const [searchOpen, setSearchOpen] = useState(false);
  const [searchLoaded, setSearchLoaded] = useState(false);
  const mobileTriggerRef = useRef<HTMLButtonElement>(null);
  const searchReturnFocusRef = useRef<HTMLElement | null>(null);
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
  const selectedShowId = getSidebarScopeShowId(sidebarScope);
  const selectedShow = shows.find((show) => show.id === selectedShowId);
  const visibleEpisodes = getSidebarEpisodes(episodes, selectedShow?.id);
  const showShortTitleById = new Map(shows.map((show) => [show.id, show.shortTitle]));

  useLayoutEffect(() => {
    syncSidebarDocumentState();
  }, []);

  useEffect(() => {
    const handleShortcut = (event: KeyboardEvent) => {
      if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") {
        event.preventDefault();
        searchReturnFocusRef.current = isMobile
          ? mobileTriggerRef.current
          : document.activeElement instanceof HTMLElement ? document.activeElement : null;
        setMobileOpen(false);
        setSearchLoaded(true);
        setSearchOpen(true);
      }
    };
    window.addEventListener("keydown", handleShortcut);
    return () => window.removeEventListener("keydown", handleShortcut);
  }, [isMobile]);

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

  const openSearch = () => {
    searchReturnFocusRef.current = isMobile
      ? mobileTriggerRef.current
      : document.activeElement instanceof HTMLElement ? document.activeElement : null;
    setMobileOpen(false);
    setSearchLoaded(true);
    setSearchOpen(true);
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
    <>
      <a
        className="skip-link"
        href="#main-content"
        inert={searchOpen || (isMobile && mobileOpen) ? true : undefined}
      >
        跳到正文
      </a>
      <div
        className={`app-shell${collapsed ? " sidebar-collapsed" : ""}`}
        inert={searchOpen ? true : undefined}
        onClickCapture={preserveSelectableLinkText}
      >
        <button
          ref={mobileTriggerRef}
          className="mobile-nav-trigger icon-button"
          type="button"
          aria-label="打开节目导航"
          aria-expanded={mobileOpen}
          aria-controls="global-sidebar"
          inert={mobileOpen ? true : undefined}
          onClick={() => setMobileOpen(true)}
        >
          <List size={22} weight="regular" />
        </button>

        {mobileOpen ? (
          <button
            className="sidebar-scrim"
            type="button"
            aria-hidden="true"
            tabIndex={-1}
            onClick={closeMobile}
          />
        ) : null}

        <aside
          ref={sidebarRef}
          id="global-sidebar"
          className={`global-sidebar${mobileOpen ? " mobile-open" : ""}`}
          aria-label="节目导航"
          role={isMobile ? "dialog" : undefined}
          aria-modal={isMobile && mobileOpen ? true : undefined}
          aria-hidden={isMobile && !mobileOpen ? true : undefined}
          inert={isMobile && !mobileOpen ? true : undefined}
          onKeyDown={handleSidebarKeyDown}
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
              onClick={openSearch}
            >
              <MagnifyingGlass size={19} />
              <span className="sidebar-label">搜索全文</span>
              <kbd className="sidebar-shortcut" aria-label="快捷键 Command K 或 Control K">
                ⌘/Ctrl K
              </kbd>
            </button>

            <nav className="show-navigation" aria-label="播客与单集">
              <div className="sidebar-section-heading sidebar-label">
                <p>播客来源</p>
                <span>{shows.length} 档</span>
              </div>
              <div className="show-filter-list">
                <Link
                  className={`show-row all-shows-row selectable-content-link${sidebarScope === "all" ? " active" : ""}`}
                  href="/shows"
                  draggable={false}
                  aria-label="全部播客来源"
                  aria-current={pathname === "/shows" ? "page" : sidebarScope === "all" ? "location" : undefined}
                  onClick={(event) => {
                    if (!event.defaultPrevented) setMobileOpen(false);
                  }}
                >
                  <span className="all-shows-icon" aria-hidden="true">
                    <SquaresFour size={22} />
                  </span>
                  <span className="show-copy sidebar-label">
                    <strong>全部节目</strong>
                    <small>{totalEpisodes} 期内容</small>
                  </span>
                </Link>
                {shows.map((show) => {
                  const active = selectedShowId === show.id;
                  return (
                    <Link
                      key={show.id}
                      className={`show-row source-show-row selectable-content-link${active ? " active" : ""}`}
                      href={show.href}
                      draggable={false}
                      aria-label={`${show.title}，${show.episodeCount} 期内容`}
                      aria-current={pathname === show.href ? "page" : active ? "location" : undefined}
                      onClick={(event) => {
                        if (!event.defaultPrevented) setMobileOpen(false);
                      }}
                    >
                      <span className="source-show-mark" aria-hidden="true" />
                      <span className="show-copy sidebar-label">
                        <strong>{show.shortTitle}</strong>
                        <small>{show.episodeCount} 期内容</small>
                      </span>
                    </Link>
                  );
                })}
              </div>

              <div className="sidebar-section-heading episode-list-heading sidebar-label">
                <p>{selectedShow ? "节目单集" : "全部单集"}</p>
                <span>{visibleEpisodes.length} 期</span>
              </div>
              <div className="episode-nav-list">
                <section
                  className="episode-show-group"
                  aria-label={selectedShow ? `${selectedShow.title}单集` : "全部单集，按发布日期倒序"}
                >
                  <ul>
                    {visibleEpisodes.map((episode) => {
                      const active = pathname === episode.href
                        || pathname === `${episode.href}/transcript`;
                      return (
                        <li key={episode.id}>
                          <Link
                            ref={active ? activeEpisodeRef : undefined}
                            className={`episode-nav-row selectable-content-link${active ? " active" : ""}`}
                            href={episode.href}
                            draggable={false}
                            aria-label={getSidebarEpisodeAriaLabel(
                              episode,
                              selectedShow === undefined,
                            )}
                            aria-current={active ? "page" : undefined}
                            onClick={(event) => {
                              if (!event.defaultPrevented) setMobileOpen(false);
                            }}
                          >
                            <EpisodeSidebarTitle
                              title={episode.navigationTitle}
                              publishedDate={episode.publishedDate}
                              showTitle={selectedShow
                                ? undefined
                                : showShortTitleById.get(episode.showId) ?? episode.showTitle}
                            />
                          </Link>
                        </li>
                      );
                    })}
                  </ul>
                </section>
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
        </aside>

        <div
          className="app-surface"
          inert={isMobile && mobileOpen ? true : undefined}
        >
          {children}
        </div>
      </div>

      {searchLoaded ? (
        <SearchDialog
          open={searchOpen}
          onClose={() => setSearchOpen(false)}
          recentEpisodes={episodes.slice(0, 8)}
          returnFocusRef={searchReturnFocusRef}
        />
      ) : null}
    </>
  );
}
