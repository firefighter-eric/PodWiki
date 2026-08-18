# PodWiki bundled webfonts

These WOFF2 assets provide PodWiki's Latin, serif Chinese, and code typography.
The project owner has confirmed that PodWiki has authorization to distribute
these font artifacts for web use. Do not reuse them outside PodWiki without
obtaining independent authorization from the applicable rights holders.

Chinese UI text is deliberately not bundled here. Apple platforms use the
native `PingFang SC` face, while other platforms fall back to the official
Noto Sans SC webfont loaded through `next/font/google`. Next.js downloads that
font at build time and serves it from the PodWiki deployment; browsers do not
contact Google at runtime.

## Included faces

- `sf-pro-variable.woff2`: SF system font, normal width, variable weight and
  optical size.
- `georgia-regular.woff2` and `georgia-bold.woff2`: Georgia regular and bold.
- `songti-sc-regular.woff2` and `songti-sc-bold.woff2`: Songti SC regular and
  bold.
- `sf-mono-variable.woff2`: SF Mono, variable weight.

The Songti SC faces contain GB2312, the punctuation and symbol ranges used by
the reader, and every Unicode code point present in the current Web UI and
published content. This keeps all current PodWiki text covered while avoiding
the roughly 30 MB transfer cost of the complete regular and bold collections.
