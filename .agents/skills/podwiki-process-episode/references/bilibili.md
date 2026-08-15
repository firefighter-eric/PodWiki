# Bilibili source handling

- Accept one `https://www.bilibili.com/video/<BVID>/` source as the technical input and reject
  multi-page inputs other than page 1 until page-specific storage is implemented. A canonical
  BVID identifies a source; it does not prove that the source is a podcast episode.
- Before media acquisition or tracked episode creation, require affirmative publisher evidence
  that the exact video is a complete official episode of a verified podcast. Public availability,
  duration, interview format, or a title containing `EP` is insufficient. If the proof is absent
  or ambiguous, stop after metadata-only intake and reject the video from PodWiki ingestion.
- Treat a Bilibili account as a mixed publishing surface, not as a podcast. For an explicitly
  authorized bounded podcast import, first freeze only an official publisher season identified
  as full podcast episodes, or videos exactly matched to a public podcast feed. Under
  `.cache/intake/<show-id>/manifest.json`, record the canonical channel URL and `mid`,
  `season_id` when present, collection title, frozen time, allowlist count, and canonical BVID
  URLs. Feed-matched entries also record the canonical feed URL and each BVID's GUID and episode
  URL mapping. Never admit the channel's other uploads merely because they are long or
  conversational; exclude clips, livestreams, events, courses, talks, product videos, and
  ordinary commentary unless the same complete item is officially published as an episode of
  the verified podcast.
- Remove queries and fragments from the stored canonical URL.
- Use `scripts/acquire_media.py` so yt-dlp and Bilibili's public view/player metadata are
  captured together. Do not persist temporary DASH URLs.
- If yt-dlp hits the known public-page `Unable to extract initial state` compatibility
  failure, the acquisition script may fall back to the official anonymous playurl API.
  Other extractor and transport failures must remain errors.
- Before that fallback, require the requested BVID, view BVID/aid/cid/page, and player
  BVID/aid/cid to be present and mutually consistent. Require `state == 0` and every
  payment, preview, charging-only, or upower access flag to be explicitly `0`/`false`;
  reject missing fields. `no_reprint` is a provenance boundary to record, not an access
  denial, and `download` is not authorization. Never persist the signed DASH URL.
- Record BVID, aid, cid, and page from verified metadata.
- Treat an empty anonymous subtitle list as "no public subtitle found", not proof that a
  login-visible or hard-burned subtitle does not exist.
- The repository does not yet provide a public-subtitle importer. When an anonymous subtitle
  track exists, stop and report that unsupported branch; do not silently ignore it and start
  audio ASR.
- If no public subtitle exists and the source is publicly accessible, acquire only the audio
  needed for local processing.
- Do not infer processing authorization from technical download availability; stay within
  the user's authorized scope.
- Do not process paid, membership-only, charging-only, regional, or login-gated media without
  a separately authorized workflow.
