# YouTube source handling

- Accept one canonical `https://www.youtube.com/watch?v=<video-id>` source. Normalize
  `youtu.be` links and remove tracking parameters.
- Disable playlists even when a playlist query is present.
- Check publisher subtitles and automatic captions in the actual authorized access context before
  acquiring audio. The repository does not yet provide a subtitle importer, so stop and report
  that unsupported branch when a track is available instead of silently falling through to audio
  ASR.
- Use `scripts/acquire_media.py` for anonymous public media and keep the output under
  `.cache/media/`.
- Stop after verified metadata/media. The tracked episode schema does not yet define YouTube
  source identifiers or a stable key for unnumbered videos, so full ingestion is unsupported.
- An existing browser session or cookies may be used when the user explicitly authorizes the
  YouTube login identity and exact video scope. The authenticated acquisition path must preserve
  the same metadata, subtitle, access-state, media-probe, hash, and sidecar contract; the current
  `scripts/acquire_media.py` path remains anonymous. Keep exported credentials only under ignored
  `.cache/credentials/` and never expose them in output or tracked artifacts. Authentication does
  not authorize age-restricted, paid, members-only, private, regional, or other restricted media.
- Preserve the publisher URL; do not commit downloaded audio or video.
