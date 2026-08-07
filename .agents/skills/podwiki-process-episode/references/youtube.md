# YouTube source handling

- Accept one canonical `https://www.youtube.com/watch?v=<video-id>` source. Normalize
  `youtu.be` links and remove tracking parameters.
- Disable playlists even when a playlist query is present.
- Check publisher subtitles and automatic captions before acquiring audio. The repository
  does not yet provide a subtitle importer, so stop and report that unsupported branch when a
  public track exists instead of silently falling through to audio ASR.
- Use `scripts/acquire_media.py` for public media and keep the output under `.cache/media/`.
- Stop after verified metadata/media. The tracked episode schema does not yet define YouTube
  source identifiers or a stable key for unnumbered videos, so full ingestion is unsupported.
- Do not use browser cookies or bypass age, account, payment, or membership controls in this
  workflow. A separately authorized source still requires a separate documented process.
- Preserve the publisher URL; do not commit downloaded audio or video.
