# Show-specific scan policies

Read the selected show README first. Its tracked sources establish identity and current URLs. Apply
the most restrictive rule among that README, `docs/content-standard.md`, and this file.

## Strict Bilibili dialogue policy

For `zhangxiaojun` and `sv101`, an update candidate must be a newly published, complete, long-form
dialogue podcast on the show's official Bilibili channel.

- Bilibili is the required discovery surface.
- RSS, Xiaoyuzhou, Apple Podcasts, websites, and other platforms are identity or cross-check
  sources only. An RSS-only release is not an update candidate.
- Exclude general programs, news or analysis segments, talks, conference speeches, livestreams,
  clips, previews, excerpts, and multi-person roundtables even when they appear on the official
  channel or in the audio feed.
- Require evidence for both `complete episode` and `long-form dialogue`; a title or tag containing
  `视频播客`, `播客`, `访谈`, or `EP` is not enough by itself.
- If the official Bilibili listing cannot be traversed for the declared window, the scan is
  `partial` or `blocked`; another platform cannot convert it into `complete` or `no updates`.

This policy controls future update scans. It does not retroactively relabel existing repository
episodes.

## Other current shows

For `latetalk`, `luoyonghao`, `moonuncle`, `svvector`, and `whynottv`, require the exact item to be
published as a complete episode of the verified podcast. The official Bilibili source is the
preferred discovery surface where the show README marks it preferred; RSS, publisher websites,
Xiaoyuzhou, and Apple Podcasts provide identity and exact-item cross-checks. Show formats already
recorded in the README may be eligible, but ordinary uploads from a mixed channel are not.

For `yiqitietalk`, the official Xiaoyuzhou podcast page is the required discovery surface. Admit
only episodes bound to that podcast that are publicly visible and later pass the add workflow's
`NORMAL`, `FREE`, non-private, `PUBLIC` checks.

For any future show, stop with `needs-review` until its README provides affirmative podcast identity
and a preferred publisher source. A YouTube-backed show additionally needs the official channel ID
and a publisher-maintained playlist explicitly scoped to complete podcast episodes; once recorded,
that playlist is the required discovery surface and the publisher website/RSS are identity or
cross-check sources. Do not invent a policy by copying a superficially similar show.
