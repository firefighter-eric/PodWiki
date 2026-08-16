# Bilibili source handling

- Accept one canonical https://www.bilibili.com/video/<BVID>/ input per acquisition command. Reject
  multi-page inputs other than page 1 until page-specific storage exists.
- A BVID proves source identity, not podcast eligibility. Require affirmative publisher evidence
  that the exact video is a complete official episode of a verified podcast.
- Consume only the exact user-approved URL or frozen add manifest. Discovery and channel enumeration
  belong to $podwiki-scan-episodes; never expand the list during addition.
- For a multi-episode add, preserve the scan's canonical channel URL, mid, official season_id when
  present, collection title, frozen time, BVID list, and any feed GUID mappings. Record the source
  scan path and SHA-256.
- Remove queries and fragments from tracked URLs. Preserve BVID case in the URL and identifiers;
  use the lowercased BVID only in the documented unnumbered episode key.
- Use scripts/acquire_media.py so yt-dlp and public view/player metadata are captured together. Do
  not persist signed DASH URLs.
- Before an anonymous playurl fallback, require requested/view/player BVID, aid, cid, and page to be
  present and consistent. Require state == 0 and every payment, preview, charging-only, and upower
  access flag to be explicitly false. Missing access fields fail closed.
- no_reprint is provenance to record, not an access denial. Technical download availability is not
  processing authorization.
- Treat an empty anonymous subtitle list as no anonymous subtitle found, not proof that an
  authorized login context or burned-in picture has no subtitle. If a track is available in the
  actual authorized context, stop because subtitle import is unsupported.
- Authenticated access requires explicit authorization for the Bilibili identity and exact source
  or frozen manifest. Keep exports under ignored .cache/credentials/ and out of output, logs,
  sidecars, Markdown, and Git.
- Login does not authorize paid, membership-only, charging-only, private, regional, age-restricted,
  or otherwise restricted media.
