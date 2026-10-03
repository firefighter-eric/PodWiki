# Next ESLint root directory glob adapter

The targeted npm override replaces only `@next/eslint-plugin-next`'s `fast-glob`
dependency. The plugin uses `globSync(string, { onlyDirectories: true })` in
`get-root-dirs`; no other fast-glob API is needed.

`braces` has no patched release for
[GHSA-vfj7-8cjw-p6xm](https://github.com/advisories/GHSA-vfj7-8cjw-p6xm).
This adapter uses tinyglobby without the affected braces dependency. It preserves
absolute input paths, strips directory suffixes, and disables tinyglobby's
automatic descendant expansion so a literal root still selects that root.

`lib/eslint-root-dirs.test.ts` exercises the installed Next plugin with default,
literal, glob, array, brace, and normalized Windows path settings. This adapter
is scoped to that API; it is not a general fast-glob replacement. Remove the
override once Next ships a dependency chain that passes the unchanged audit.
