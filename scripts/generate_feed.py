#!/usr/bin/env python3
"""Generate Atom feed for blog posts (helps crawlers discover new content)."""
from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://anjishbhondwe.com"
AUTHOR = "Anjish Bhondwe"


def blog_entry(path: Path) -> dict | None:
    html = path.read_text(encoding="utf-8")
    title_m = re.search(r"<title>([^<]+)</title>", html, re.I)
    if not title_m:
        return None
    title = re.sub(r"\s*—\s*Anjish Bhondwe\s*$", "", title_m.group(1).strip())
    desc_m = re.search(r'<meta name="description" content="([^"]*)"', html, re.I)
    desc = desc_m.group(1) if desc_m else title
    date_m = re.search(r'class="hero-date">([^<]+)<', html)
    updated = "2026-01-01T00:00:00Z"
    if date_m:
        label = date_m.group(1).strip()
        try:
            updated = datetime.strptime(label, "%B %Y").strftime("%Y-%m-01T00:00:00Z")
        except ValueError:
            pass
    return {
        "title": title,
        "link": f"{SITE}/{path.name}",
        "id": f"{SITE}/{path.name}",
        "updated": updated,
        "summary": desc,
    }


def main() -> None:
    entries = []
    for path in sorted(ROOT.glob("blog-*.html"), reverse=True):
        item = blog_entry(path)
        if item:
            entries.append(item)

    updated = max((e["updated"] for e in entries), default="2026-06-03T00:00:00Z")
    lines = [
        '<?xml version="1.0" encoding="utf-8"?>',
        '<feed xmlns="http://www.w3.org/2005/Atom">',
        f"  <title>{escape(AUTHOR)} — Blog</title>",
        f"  <link href=\"{SITE}/blogs.html\"/>",
        f"  <id>{SITE}/</id>",
        f"  <updated>{updated}</updated>",
        f"  <author><name>{escape(AUTHOR)}</name></author>",
    ]
    for e in entries:
        lines += [
            "  <entry>",
            f"    <title>{escape(e['title'])}</title>",
            f"    <link href=\"{e['link']}\"/>",
            f"    <id>{e['id']}</id>",
            f"    <updated>{e['updated']}</updated>",
            f"    <summary>{escape(e['summary'])}</summary>",
            "  </entry>",
        ]
    lines.append("</feed>\n")
    out = ROOT / "feed.xml"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out} ({len(entries)} entries)")


if __name__ == "__main__":
    main()
