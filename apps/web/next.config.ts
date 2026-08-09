import path from "node:path";
import type { NextConfig } from "next";

const repositoryRoot = path.resolve(process.cwd(), "../..");

const nextConfig: NextConfig = {
  outputFileTracingRoot: repositoryRoot,
  async redirects() {
    return [
      {
        source: "/shows/:showId/episodes/:folder",
        has: [
          {
            type: "query",
            key: "view",
            value: "transcript",
          },
        ],
        destination: "/shows/:showId/episodes/:folder/transcript",
        permanent: true,
      },
    ];
  },
  experimental: {
    optimizePackageImports: ["@phosphor-icons/react"],
  },
};

export default nextConfig;
