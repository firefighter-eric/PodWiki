# Xiaoyuzhou source handling

- Accept one canonical https://www.xiaoyuzhoufm.com/episode/<24-hex-eid> input per acquisition
  command. Podcast pages identify shows but are not media-acquisition inputs.
- Consume only exact approved URLs. Podcast enumeration belongs to $podwiki-scan-episodes.
- Remove query, fragment, and trailing slash from the tracked episode URL.
- The anonymous adapter parses the public __NEXT_DATA__ document without JavaScript, cookies, or
  tokens. It rejects redirects, non-HTML, invalid UTF-8, and oversized pages.
- Require requested eid, episode eid/pid, nested podcast pid, mediaKey, and media id to be present
  and mutually consistent.
- Require media identity <episode-pid>/<token>.m4a with a non-empty base64url token. Bind it to the
  episode's own pid; syndicated episodes can belong to another podcast.
- Fail closed unless the episode is NORMAL and FREE, isPrivateMedia is false, and media source is
  explicitly PUBLIC.
- Accept only an HTTPS M4A enclosure on media.xyzcdn.net whose path equals /<media-id>. Reject
  credentials, queries, fragments, redirects, unknown restriction state, or mismatched enclosure.
- Stream to URL-bound ignored staging with atomic checkpoints. On resume, rehash the partial prefix
  and require Range, If-Range, HTTP 206, and exact Content-Range; otherwise restart at byte zero.
- Require final byte count, published duration, ffprobe values, and SHA-256 before writing the
  sidecar or reusing cache.
- Authenticated access requires explicit authorization for the Xiaoyuzhou identity and exact source
  or frozen manifest, plus an adapter that preserves all identity/access/enclosure/hash checks.
  Until then, report a technical blocker rather than injecting credentials into the anonymous path.
- Keep all credential material under ignored .cache/credentials/ and out of output and artifacts.
  Never cross into another podcast or access paid, private, membership-only, regional, or otherwise
  restricted episodes.
