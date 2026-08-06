# Bilibili source handling

- Accept one `https://www.bilibili.com/video/<BVID>/` source and reject multi-page inputs
  other than page 1 until page-specific storage is implemented.
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
- If no public subtitle exists and the source is publicly accessible, acquire only the audio
  needed for local processing.
- Do not infer processing authorization from technical download availability; stay within
  the user's authorized scope.
- Do not process paid, membership-only, charging-only, regional, or login-gated media without
  a separately authorized workflow.
