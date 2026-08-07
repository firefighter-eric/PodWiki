# Xiaoyuzhou source handling

- Accept one canonical `https://www.xiaoyuzhoufm.com/episode/<episode-id>` source.
  Podcast pages identify shows but are not media-acquisition inputs.
- Remove queries, fragments, and a trailing slash from the stored episode URL.
- Fetch only the anonymous public HTML page. Parse its `__NEXT_DATA__` document without
  executing JavaScript, sending cookies, or using login/session tokens.
- Require the requested `eid`, episode `eid`, episode `pid`, nested podcast `pid`,
  `mediaKey`, and media `id` to be present and mutually consistent.
- Fail closed unless the episode is `NORMAL` and `FREE`, `isPrivateMedia` is false, and
  the media source is explicitly `PUBLIC`.
- Accept only an HTTPS M4A enclosure on `media.xyzcdn.net`; require the media URL and
  enclosure URL to match. Reject missing, paid, private, login-gated, or unknown access
  states instead of attempting a fallback.
- Download only the requested public episode. Never crawl or batch-download a podcast,
  and never use a token to enumerate or acquire paid/private episodes.
- Verify the downloaded enclosure against its published byte size and duration, then
  record `eid`, `pid`, media identity, probe data, and SHA-256 in the source sidecar.
