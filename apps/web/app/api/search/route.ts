import { NextResponse } from "next/server";
import { searchContent } from "@/lib/content";

export const runtime = "nodejs";

export async function GET(request: Request) {
  const query = new URL(request.url).searchParams.get("q")?.slice(0, 80) ?? "";
  const results = await searchContent(query);
  return NextResponse.json(results, {
    headers: { "Cache-Control": "private, no-store" },
  });
}
