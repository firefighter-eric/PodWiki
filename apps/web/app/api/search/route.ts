import { NextResponse } from "next/server";
import { searchContent } from "@/lib/search";

export const runtime = "nodejs";

export async function GET(request: Request) {
  const query = new URL(request.url).searchParams.get("q")?.slice(0, 80) ?? "";
  const results = await searchContent(query);
  return NextResponse.json(results, {
    headers: {
      "Cache-Control": "public, max-age=0, s-maxage=300, stale-while-revalidate=86400",
    },
  });
}
