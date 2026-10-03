import path from "node:path";
import { globSync as tinyGlobSync } from "tinyglobby";

// Next's getRootDirs uses only globSync(string, { onlyDirectories: true }).
// Preserve absolute paths and literal roots without expanding descendants.
export function globSync(pattern, options = {}) {
  if (typeof pattern !== "string") {
    throw new TypeError("Next root directory patterns must be strings");
  }

  return tinyGlobSync(pattern, {
    ...options,
    absolute: path.isAbsolute(pattern),
    expandDirectories: false,
  }).map((entry) =>
    entry.endsWith("/") && entry.length > path.parse(entry).root.length
      ? entry.slice(0, -1)
      : entry,
  );
}
