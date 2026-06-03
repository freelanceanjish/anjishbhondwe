#!/usr/bin/env python3
"""Request indexing for priority URLs via Google Indexing API (service account)."""
from __future__ import annotations

import json
import os
import sys

SITE = "https://anjishbhondwe.com"
PRIORITY_URLS = [
    f"{SITE}/",
    f"{SITE}/blogs.html",
    f"{SITE}/blog-eu-ai-act-agile-coalesce.html",
    f"{SITE}/blog-eu-ai-act.html",
    f"{SITE}/blog-ai-governance-agile.html",
    f"{SITE}/blog-agile-transformations.html",
    f"{SITE}/work.html",
]
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def main() -> int:
    raw = os.environ.get("GOOGLE_SEARCH_CONSOLE_JSON", "").strip()
    if not raw:
        print(
            "Skip: GOOGLE_SEARCH_CONSOLE_JSON not set — cannot call Google Indexing API. "
            "IndexNow submission covers Bing/Yandex.",
        )
        return 0

    try:
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
    except ImportError:
        print("Install: pip install google-api-python-client google-auth", file=sys.stderr)
        return 1

    info = json.loads(raw)
    creds = service_account.Credentials.from_service_account_info(info, scopes=SCOPES)
    service = build("indexing", "v3", credentials=creds, cache_discovery=False)

    for url in PRIORITY_URLS:
        body = {"url": url, "type": "URL_UPDATED"}
        try:
            service.urlNotifications().publish(body=body).execute()
            print(f"Indexing API requested: {url}")
        except Exception as e:
            print(f"Failed {url}: {e}", file=sys.stderr)
            return 1

    print(f"Google Indexing API: {len(PRIORITY_URLS)} URLs submitted.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
