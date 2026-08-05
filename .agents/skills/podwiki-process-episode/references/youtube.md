# YouTube source handling

- Accept one canonical `https://www.youtube.com/watch?v=<video-id>` source. Normalize
  `youtu.be` links and remove tracking parameters.
- Disable playlists even when a playlist query is present.
- Check publisher subtitles and automatic captions before acquiring audio. Record which kind
  supplied the transcript.
- Use `scripts/acquire_media.py` for public media and keep the output under `.cache/media/`.
- Do not use browser cookies, bypass age/account/payment controls, or process members-only
  content without explicit authorization.
- Preserve the publisher URL; do not commit downloaded audio or video.
