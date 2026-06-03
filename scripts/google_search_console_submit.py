#!/usr/bin/env python3
"""Submit sitemap to Google Search Console via API (service account)."""
from __future__ import annotations

import json
import os
import sys

SITE_URL = "https://anjishbhondwe.com/"
SITEMAP_URL = "https://anjishbhondwe.com/sitemap.xml"
SCOPES = ["https://www.googleapis.com/auth/webmasters"]


def main() -> int:
    raw = os.environ.get("GOOGLE_SEARCH_CONSOLE_JSON", "").strip()
    if not raw:
        print(
            "Skip: GOOGLE_SEARCH_CONSOLE_JSON not set. "
            "Add a GCP service account key as a GitHub secret to enable GSC API submits.",
            file=sys.stderr,
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
    service = build("searchconsole", "v1", credentials=creds, cache_discovery=False)

    service.sitemaps().submit(siteUrl=SITE_URL, feedpath=SITEMAP_URL).execute()
    print(f"Submitted sitemap to Google Search Console: {SITEMAP_URL}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
