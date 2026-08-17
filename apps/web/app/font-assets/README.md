# PodWiki bundled webfonts

These WOFF2 assets reproduce the typography used by PodWiki on macOS without
depending on fonts installed on the visitor's operating system. The project
owner has confirmed that PodWiki has authorization to distribute these font
artifacts for web use. Do not reuse them outside PodWiki without obtaining
independent authorization from the applicable rights holders.

## Included faces

- `sf-pro-variable.woff2`: SF system font, normal width, variable weight and
  optical size.
- `pingfang-sc-{400,500,600,700}.woff2`: browser-compatible static instances of
  PingFang UI SC for regular through bold UI text. The browser fonts were
  rebuilt from CoreText outlines because the macOS system collection stores
  its outlines in an Apple-specific table that Chromium cannot parse.
- `georgia-regular.woff2` and `georgia-bold.woff2`: Georgia regular and bold.
- `songti-sc-regular.woff2` and `songti-sc-bold.woff2`: Songti SC regular and
  bold.
- `sf-mono-variable.woff2`: SF Mono, variable weight.

The Songti SC faces contain GB2312, the punctuation and symbol ranges used by
the reader, and every Unicode code point present in the current Web UI and
published content. This keeps all current PodWiki text covered while avoiding
the roughly 30 MB transfer cost of the complete regular and bold collections.
The PingFang UI SC faces follow the same current-content-plus-GB2312 coverage
policy and contain 7,083 mapped Unicode code points each.
