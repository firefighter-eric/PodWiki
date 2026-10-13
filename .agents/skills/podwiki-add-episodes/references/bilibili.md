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
  authorized login context or burned-in picture has no subtitle.
- Authenticated access requires explicit authorization for the Bilibili identity and exact source
  or frozen manifest. Keep exports under ignored .cache/credentials/ and out of output, logs,
  sidecars, Markdown, and Git.
- Login does not authorize paid, membership-only, charging-only, private, regional, age-restricted,
  or otherwise restricted media.

## Import an authenticated AI subtitle

Before starting a batch, verify that the authorized browser backend can export a network
**response body** to an ignored file. Resource inventory alone is insufficient: `pageAssets`
may report an AI subtitle as `other`, while its bundle operation cannot export that JSON.
An unrelated or unauthenticated browser backend does not inherit the existing login context.
If body export is unavailable, report an acquisition-tool blocker before creating tracked files;
do not classify visible subtitles as absent or silently use ASR.

1. In the authorized existing browser session, confirm the exact BVID page is logged in and the
   player exposes an active Chinese subtitle. Do not inspect or export cookies, local storage,
   passwords, or unrelated browser state.
2. Activate the Chinese track, then inspect only resources already loaded by that page. Select the
   exact `aisubtitle.hdslb.com/bfs/ai_subtitle/` response associated with the current aid/cid.
3. Save the response body, not its signed URL, to
   `.cache/intake/<BVID>/subtitle.zh-CN.ai.json`. Never print or persist `auth_key`, cookies, account
   identifiers, or browser-profile paths. The signed URL is temporary transport context and must
   not enter shell history, logs, sidecars, Markdown, raw artifacts, or Git.
4. Keep the anonymous metadata intake sidecar for the same canonical URL, then import:

~~~bash
uv run --no-sync python scripts/import_bilibili_subtitles.py \
  --url https://www.bilibili.com/video/<BVID>/ \
  --episode-dir shows/<show-id>/episodes/<episode-folder> \
  --metadata-json .cache/intake/<BVID>/source.metadata.json \
  --subtitle-json .cache/intake/<BVID>/subtitle.zh-CN.ai.json \
  --access-context authenticated
~~~

The importer accepts only a public-free single-page source and a Chinese `AIsubtitle` payload. It
binds BVID/aid/cid/page and uploader metadata, rejects duplicate/non-finite JSON, non-monotonic or
empty segments, and subtitle tracks whose first or last cue is more than 30 seconds from the media
edge. It writes tracked `asr/bilibili-subtitles/{raw.json,refined.json,transcript.zh-CN.md}` plus a
byte-identical root transcript. Record engine `bilibili-subtitles`, model
`bilibili-ai-subtitle-zh`, acquisition method `platform-ai-subtitle`, and machine status.

If no supported track exists in the actual authorized context, record that result and use public
audio plus local Qwen. If a different Bilibili subtitle format appears, stop rather than coercing it
through this importer.

## Transport signatures and diagnosis

Canonicalization applies to the tracked **episode source URL**, not the temporary subtitle
transport request. Keep the publisher-issued subtitle request intact inside the authorized
browser/backend memory. In particular, do not remove `auth_key` before requesting its body.
Not storing a signed URL is different from stripping its authorization parameters in transit.
Prefer exporting the response already loaded after selecting Chinese: this avoids expired links,
repeated CDN requests, and exporting browser credentials.

For an operator-assisted fallback, `scripts/fetch_bilibili_subtitle_body.py` accepts an intact
temporary URL only through a hidden interactive terminal prompt. It does not discover tracks,
read cookies, create signatures, or prove which video an otherwise anonymous subtitle body belongs
to. The operator must bind the URL to the exact current video's active Chinese track. Follow the
command and limitations in `docs/python-scripts.md`; never paste the temporary URL into chat,
command arguments, environment variables, or files. Live validation is still required.

When a browser backend supports a network response handle, select the exact response internally
and export only its `response-body` to `.cache/intake/<BVID>/subtitle.zh-CN.ai.json`. Do not print
the request list, request headers, signed URL, or response headers. If request discovery returns
signed URLs, filter its result inside the tool orchestration process and expose only opaque
response indices/handles and non-sensitive identity checks; never save the discovery result.
Confirm that the backend is the same authorized session and that requests belong to the current
canonical video after its Chinese track was selected. Validate the captured body with the importer;
a resource handle, screenshot, or successfully written HTML error page is not a completed capture.

Classify failures separately:

| Observation | Meaning and next step |
| --- | --- |
| Anonymous list is empty and requires login | Subtitle availability in the authorized session is unknown. |
| Chinese subtitle visibly plays but JSON export is unsupported | Acquisition-tool blocker; the website is still supplying captions. |
| A request after removing `auth_key` returns 403 | Invalid comparison with the original authorized request; cannot establish an interface change or subtitle absence. |
| A fresh, intact publisher-issued request fails | Record only status/error category; reselect the track once to obtain a fresh response, then stop if it still fails. Do not fabricate or repair signatures. |
| Captured JSON fails language, identity, cue or edge checks | Keep the failed input ignored and report validation failure; do not mark intake complete. |

Use a newly captured, importer-validated Chinese body as the live acceptance check for any changed
acquisition method. Until that succeeds, label the method unverified; do not promise permanent
availability or treat an old successful episode as current end-to-end proof.
