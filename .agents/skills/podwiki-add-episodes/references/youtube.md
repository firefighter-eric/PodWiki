# YouTube source handling

- Accept one canonical https://www.youtube.com/watch?v=<video-id> source. Normalize youtu.be links,
  remove tracking and playlist parameters, and disable playlists.
- Consume only the exact user-approved video; channel and playlist discovery are out of scope.
- Check publisher subtitles and automatic captions in the actual authorized context before media.
  Stop when a track exists because subtitle import is unsupported.
- Use scripts/acquire_media.py for anonymous public metadata/media and keep output under .cache/.
- Stop after verified metadata or media. PodWiki has not defined tracked YouTube source identifiers
  or a stable unnumbered episode key, so full episode ingestion is unsupported.
- Authenticated access requires explicit authorization for the YouTube identity and exact video.
  Preserve the same metadata, subtitle, access-state, media-probe, hash, and sidecar contract.
- Keep credentials under ignored .cache/credentials/ and never expose them. Authentication does not
  authorize age-restricted, paid, member-only, private, regional, or otherwise restricted media.
