#!/usr/bin/env python3
"""Notify search engines of sitemap URLs via IndexNow and legacy pings."""
from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE_HOST = "anjishbhondwe.com"
SITE = f"https://{SITE_HOST}"
INDEXNOW_KEY = "2e00a7f3b9c14d6e8f0a1b2c3d4e5f6"
KEY_FILE = f"{INDEXNOW_KEY}.txt"
SITEMAP = ROOT / "sitemap.xml"

INDEXNOW_ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
    "https://yandex.com/indexnow",
]

PING_ENDPOINTS = [
    ("Yandex", f"https://webmaster.yandex.com/ping?sitemap={SITE}/sitemap.xml"),
]


def load_urls() -> list[str]:
    tree = ET.parse(SITEMAP)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [el.text.strip() for el in tree.findall(".//sm:loc", ns) if el.text]
    if not urls:
        urls = [el.text.strip() for el in tree.findall(".//{*}loc") if el.text]
    return urls


def http_request(url: str, *, method: str = "GET", data: bytes | None = None, headers: dict | None = None) -> tuple[int, str]:
    req = urllib.request.Request(url, data=data, method=method, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, resp.read(500).decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        body = e.read(500).decode("utf-8", errors="replace") if e.fp else ""
        return e.code, body


def verify_key_live() -> bool:
    key_url = f"{SITE}/{KEY_FILE}"
    status, body = http_request(key_url)
    ok = status == 200 and INDEXNOW_KEY in body
    print(f"Key file {key_url}: HTTP {status} {'OK' if ok else 'FAIL'}")
    return ok


def submit_indexnow(urls: list[str]) -> None:
    payload = {
        "host": SITE_HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{SITE}/{KEY_FILE}",
        "urlList": urls,
    }
    body = json.dumps(payload).encode("utf-8")
    headers = {"Content-Type": "application/json; charset=utf-8"}

    for endpoint in INDEXNOW_ENDPOINTS:
        status, resp = http_request(endpoint, method="POST", data=body, headers=headers)
        label = "OK" if status in (200, 202) else "WARN"
        print(f"IndexNow {endpoint}: HTTP {status} {label}")
        if status not in (200, 202) and resp:
            print(f"  {resp[:200]}")


def ping_sitemaps() -> None:
    encoded = urllib.parse.quote(f"{SITE}/sitemap.xml", safe="")
    for name, url in PING_ENDPOINTS:
        status, _ = http_request(url)
        print(f"Ping {name}: HTTP {status}")


def main() -> int:
    if not SITEMAP.exists():
        print(f"Missing {SITEMAP}", file=sys.stderr)
        return 1

    urls = load_urls()
    print(f"Submitting {len(urls)} URLs from sitemap…")

    if not verify_key_live():
        print("Key file not live yet — deploy site first, then re-run.", file=sys.stderr)
        return 2

    submit_indexnow(urls)
    ping_sitemaps()
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
