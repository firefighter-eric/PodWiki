import Link from "next/link";

export default function NotFound() {
  return (
    <main id="main-content" className="not-found-page" tabIndex={-1}>
      <p>404</p>
      <h1>这一页还没有收录</h1>
      <Link href="/shows">返回全部节目</Link>
    </main>
  );
}
