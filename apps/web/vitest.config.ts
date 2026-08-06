import { defineConfig } from "vitest/config";
import { fileURLToPath } from "node:url";

export default defineConfig({
  resolve: {
    alias: {
      "server-only": fileURLToPath(new URL("./test/server-only.ts", import.meta.url)),
      "@": new URL("./", import.meta.url).pathname,
    },
  },
  test: {
    environment: "node",
    include: ["**/*.test.ts"],
  },
});
