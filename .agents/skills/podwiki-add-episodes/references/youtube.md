# YouTube source handling

- Accept one canonical https://www.youtube.com/watch?v=<video-id> source. Normalize youtu.be links,
  remove tracking and playlist parameters, and disable playlists.
- Consume only the exact user-approved video; channel and playlist discovery are out of scope.
- Require the exact, case-sensitive `video_id` plus the official `channel_id`. When the candidate
  came from a scan manifest, also require its official podcast `playlist_id` and exact playlist
  membership evidence.
- For an unnumbered episode, encode the video ID's 11 ASCII bytes as 22 lowercase hexadecimal
  characters and use `youtube-<hex>` as the stable episode key. The tracked identifier remains the
  original video ID; playlist order never becomes an episode number.
- Check publisher subtitles and automatic captions in the actual authorized context before audio
  ASR. If a publisher English track and an event-aligned `zh-Hans-en` automatic translation are
  both available, import them with:

~~~bash
env UV_CACHE_DIR=.cache/uv uv run --no-sync python scripts/import_youtube_captions.py \
  --url <canonical-video-url> \
  --episode-dir shows/<show-id>/episodes/<episode-folder>
~~~

- The importer selects `json3`, preserves the exact publisher payload in tracked `raw.json`,
  validates every event's start/end against the Chinese machine-translation track, writes a
  non-Qwen `refined.json`, promotes a byte-identical English root transcript, and generates the
  segment-aligned Chinese root translation. Any missing track, empty event, timing drift, or source
  identity mismatch fails closed. Keep both transcript and translation states `machine`.
- If both JSON3 tracks and the `acquire_media.py --metadata-only` sidecar are already frozen under
  `.cache/`, but a retry is rate-limited, pass `--metadata-json`, `--source-json3`, and
  `--translation-json3` together. The importer revalidates the canonical URL, public/non-live
  state, video ID, channel ID, and caption alignment; it rejects inputs outside `.cache/`.
- If a subtitle exists but this exact import contract cannot consume it, stop. Do not ignore it and
  silently run audio ASR. When no supported subtitle exists, local Qwen audio ASR is allowed under
  the normal backend contract.
- Use scripts/acquire_media.py for anonymous public metadata/media and keep output under .cache/.
- A tracked YouTube video source uses `platform: youtube`, `kind: video`, canonical watch URL, and
  `identifiers.video_id` plus `identifiers.channel_id`.
- Authenticated access requires explicit authorization for the YouTube identity and exact video.
  Preserve the same metadata, subtitle, access-state, media-probe, hash, and sidecar contract.
- Keep credentials under ignored .cache/credentials/ and never expose them. Authentication does not
  authorize age-restricted, paid, member-only, private, regional, or otherwise restricted media.
