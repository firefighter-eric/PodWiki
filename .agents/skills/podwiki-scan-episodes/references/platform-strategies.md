# Platform discovery strategies

Use only the sections needed for the selected show's sources.

## RSS

- Fetch the publisher feed URL from the show README with redirects enabled and record the final URL,
  HTTP status, content type, retrieval time, `ETag`, and `Last-Modified` when present.
- Parse the complete returned XML document. Record item `guid`, `link`, `title`, `pubDate`, enclosure
  URL/type/length, explicit episode number, duration, and description when present.
- Treat a publisher GUID as the stable identity inside that feed. Apple requires episode GUIDs to
  be unique and unchanged, and unique enclosures for each episode:
  <https://podcasters.apple.com/support/823-podcast-requirements>.
- Use conditional requests on repeat scans when safe, but retain the prior complete body when a
  server returns `304`. Apple recommends `ETag` or `Last-Modified` support:
  <https://podcasters.apple.com/4115-technical-updates-for-hosting-providers>.
- A feed can be truncated. Absence of an old item does not prove deletion or full-history coverage.
  The RSS 2.0 item/GUID/enclosure semantics are documented at
  <https://www.rssboard.org/rss-specification>.
- Under a Bilibili-required show policy, use RSS only to identify and cross-check a Bilibili item.
  Never promote an RSS-only item to `eligible-new`.

## Bilibili

- Discover only on the official channel or an official collection named by the show policy. A
  mixed account is not an episode feed.
- Prefer a rendered browser view or other current publisher-visible listing that exposes ordering
  and pagination. Traverse until the declared coverage boundary is crossed.
- The public space page, an extractor, and a search engine can disagree. CAPTCHA HTML, HTTP 412/352,
  an empty shell, missing pagination, or a client-specific block means incomplete coverage, not an
  empty channel.
- Treat general web search as lead generation only. Validate every found BVID against the official
  uploader, publication metadata, show identity, and complete-episode evidence.
- Canonicalize to `https://www.bilibili.com/video/<BVID>/`. Preserve BVID case in the URL and
  metadata; compare BVIDs case-insensitively only for repository duplicate detection.
- Use metadata-only intake for exact candidates. Require consistent BVID/aid/cid/page identity and
  public access state. Do not let technical download availability decide podcast eligibility.
- Use an existing logged-in session only after the user explicitly authorizes the Bilibili identity
  and exact show/scope. Keep credentials under ignored `.cache/credentials/`, never print them, and
  do not use them to access paid, member-only, private, regional, or otherwise restricted content.

## Xiaoyuzhou

- Use the exact official podcast page from the show README as the discovery surface. Enumerate the
  visible episode list and any documented pagination until the coverage boundary is crossed.
- Canonicalize candidates to `https://www.xiaoyuzhoufm.com/episode/<24-hex-eid>`.
- Validate exact candidates with metadata-only intake. Require episode/podcast identity consistency;
  the add workflow later enforces `NORMAL`, `FREE`, non-private, explicitly `PUBLIC`, enclosure, and
  media identity checks.
- A podcast page rendered with a finite initial list is not proof of full-history coverage unless
  the listing end or total is verifiable.
- Do not cross into a syndicated episode's owning podcast merely because it appears in a list.

## Apple Podcasts and publisher websites

- Use these pages to prove podcast identity, locate the canonical publisher feed, and corroborate
  show metadata.
- Prefer the publisher RSS feed for timely enumeration. Apple notes that new episodes may take up to
  24 hours to appear in search or personalized surfaces, so catalog/search absence is not a fresh
  negative result.
- Do not use a directory's episode ordering as an official episode number.

## Search engines and cached pages

- Use results only to find a possible canonical publisher URL.
- Never use result count, absence, snippets, cached dates, or ranking as completeness evidence.
- Reject third-party reposts, commentary, summaries, and collaboration uploads unless the selected
  show's publisher also identifies the exact source as its official complete episode under project
  policy.
