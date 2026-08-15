# Xiaoyuzhou source handling

- Accept one canonical `https://www.xiaoyuzhoufm.com/episode/<episode-id>` source per
  acquisition command. Podcast pages identify shows but are not media-acquisition inputs.
  By default, do not enumerate them.
- Remove queries, fragments, and a trailing slash from the stored episode URL.
- The current adapter fetches only the anonymous public HTML page. It parses the `__NEXT_DATA__`
  document without executing JavaScript, sending cookies, or using login/session tokens, and
  rejects redirects, non-HTML responses, invalid UTF-8, and pages over the configured size limit.
  Repository policy permits a stateful path after the user explicitly authorizes the Xiaoyuzhou
  login identity and exact source or frozen-manifest scope, but that path must preserve every
  identity, access-state, enclosure, byte-count, duration, hash, and sidecar check below. Until
  such an adapter exists, report a technical blocker instead of treating login as forbidden or
  injecting credentials into the anonymous path.
- Require the requested `eid`, episode `eid`, episode `pid`, nested podcast `pid`,
  `mediaKey`, and media `id` to be present and mutually consistent.
- Require the media identity to have the form `<episode-pid>/<token>.m4a`, with a non-empty
  base64url token. Bind it to the episode's own `pid`, not the outer podcast page's PID;
  cross-posted episodes can legitimately belong to another podcast.
- Fail closed unless the episode is `NORMAL` and `FREE`, `isPrivateMedia` is false, and
  the media source is explicitly `PUBLIC`.
- Accept only an HTTPS M4A enclosure on `media.xyzcdn.net`; require the media URL and
  enclosure URL to match and its path to equal `/<media-id>`. Reject redirects, credentials,
  query strings, fragments, missing fields, paid, private, login-gated, or unknown access
  states instead of attempting a fallback.
- Hold deadlock-ordered locks for both the final audio and metadata sidecar until the audio
  is verified, promoted, and the sidecar is atomically written. Stream under an additional
  staging-output lock to a URL-bound partial file and require the final byte count to equal
  the published size. Persist an atomic checkpoint containing the URL,
  strong ETag, partial size, and SHA-256; rehash the prefix before every resume. When the
  response includes `Content-Length`, require it to match too. Resume only with `Range`,
  `If-Range`, HTTP 206, and an exact `Content-Range`; otherwise restart from byte zero. Ask
  for identity content encoding and reject encoded responses. Do not retry permanent 4xx or
  local filesystem errors.
- Download only the requested public episode by default. A bounded whole-podcast import is
  allowed only after the user explicitly authorizes one verified podcast. Anonymous discovery
  must be limited to that podcast, and its PID plus every canonical episode URL/eid must be
  frozen in a manifest before any media download. Do not add newly discovered episodes during
  the run. Validate each item independently as `NORMAL`, `FREE`, non-private, explicitly
  `PUBLIC`, and bound to the authorized podcast; reject and report mismatches or unknown
  states. Process the manifest sequentially with rate limiting, passing one episode URL to
  each acquisition command. The current anonymous adapter never uses cookies or tokens. A future
  authenticated adapter must keep exported credentials under ignored `.cache/credentials/` and
  out of output and artifacts. Never cross into another podcast or enumerate/acquire paid,
  membership-only, private, regional, or other restricted episodes.
- Verify the downloaded enclosure against its published byte size and duration, then
  record `eid`, `pid`, media identity, probe data, and SHA-256 in the source sidecar.
- Before reusing cached audio, verify its canonical URL and SHA-256 locally, then compare
  the refreshed `eid`, `pid`, and `media_id` with the sidecar. A metadata-only refresh keeps
  media fields only after that identity check plus a fresh probe, size, and duration check.
