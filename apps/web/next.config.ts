import path from "node:path";
import type { NextConfig } from "next";

const repositoryRoot = path.resolve(process.cwd(), "../..");

const nextConfig: NextConfig = {
  outputFileTracingRoot: repositoryRoot,
  outputFileTracingIncludes: {
    "/*": ["../../shows/**/*.md"],
  },
  experimental: {
    optimizePackageImports: ["@phosphor-icons/react"],
  },
};

export default nextConfig;
