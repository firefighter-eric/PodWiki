function splitHref(href: string) {
  const hashIndex = href.indexOf("#");
  return {
    beforeHash: hashIndex >= 0 ? href.slice(0, hashIndex) : href,
    hash: hashIndex >= 0 ? href.slice(hashIndex) : "",
  };
}

export function getTranscriptHref(episodeHref: string, anchorSource?: string): string {
  const baseHref = canonicalizeReaderHref(episodeHref).replace(/\/$/u, "");
  const hashIndex = anchorSource?.indexOf("#") ?? -1;
  const anchor = hashIndex >= 0
    ? anchorSource?.slice(hashIndex + 1)
    : anchorSource?.replace(/^#/u, "");

  return `${baseHref}/transcript${anchor ? `#${anchor}` : ""}`;
}

export function canonicalizeReaderHref(href: string): string {
  const { beforeHash, hash } = splitHref(href);
  const queryIndex = beforeHash.indexOf("?");
  if (queryIndex < 0) return href;

  const pathname = beforeHash.slice(0, queryIndex);
  const searchParams = new URLSearchParams(beforeHash.slice(queryIndex + 1));
  const view = searchParams.get("view");
  if (view !== "summary" && view !== "transcript") return href;

  searchParams.delete("view");
  const search = searchParams.size > 0 ? `?${searchParams.toString()}` : "";
  const canonicalPathname = view === "transcript"
    ? `${pathname.replace(/\/$/u, "")}/transcript`
    : pathname;

  return `${canonicalPathname}${search}${hash}`;
}
