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
  ASR. Freeze the publisher English `json3` and metadata sidecar. Assign consecutive events to
  Codex Luna subagents (`gpt-6-luna`) for one-to-one Chinese translation under the runbook.
  Use the following command to import the assembled translation.

~~~bash
uv run --no-sync python scripts/import_youtube_captions.py \
  --url <canonical-video-url> \
  --episode-dir shows/<show-id>/episodes/<episode-folder> \
  --metadata-json .cache/<episode>/metadata.json \
  --source-json3 .cache/<episode>/source.en.json3 \
  --translation-segments-json .cache/<episode>/translation.zh-CN.json
~~~

- The importer selects `json3`, preserves the exact publisher payload in tracked `raw.json`,
  validates every event's start/end against the Chinese machine-translation track, writes a
  non-Qwen `refined.json`, promotes a byte-identical English root transcript, and generates the
  segment-aligned Chinese root translation. Any missing track, empty event, timing drift, or source
  identity mismatch fails closed. Keep both transcript and translation states `machine`.
- Record both source hashes, every original event index and timestamp, generation time, and
  `engine: codex-subagent`, `model: gpt-6-luna`, `model_revision: null`, and
  `model_version_visibility: not-exposed`. Use `--replace-translation` to preserve existing raw
  and English bytes.
- Re-import an existing event-aligned `zh-Hans-en` platform translation with the original frozen
  `--metadata-json`, `--source-json3`, and `--translation-json3` inputs. The importer revalidates
  the canonical URL, public/non-live state, video ID, channel ID, and caption alignment. It
  rejects inputs outside `.cache/`.
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
