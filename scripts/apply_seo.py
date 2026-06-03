#!/usr/bin/env python3
"""Apply consistent SEO meta and JSON-LD across portfolio HTML pages."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://anjishbhondwe.com"
OG_IMAGE = f"{SITE}/profile.jpg"
AUTHOR = "Anjish Bhondwe"

BLOG_DATES = {
    "blog-eu-ai-act.html": "2025-05-01",
    "blog-agile-transformations.html": "2025-06-01",
    "blog-ai-governance-agile.html": "2025-07-01",
    "blog-eu-ai-act-agile-coalesce.html": "2025-08-01",
}

SOCIAL_BLOCK = """
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta property="og:site_name" content="Anjish Bhondwe">
  <meta property="og:locale" content="en_GB">
  <meta property="og:image" content="{og_image}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@anjish">
  <meta name="twitter:creator" content="@anjish">
  <meta name="twitter:image" content="{og_image}">
"""

MARKER = "<!-- seo:social -->"


def has_marker(head: str) -> bool:
    return MARKER in head or 'property="og:site_name"' in head


def extract_title(html: str) -> str:
    m = re.search(r"<title>([^<]+)</title>", html, re.I)
    return m.group(1).strip() if m else ""


def extract_description(html: str) -> str:
    m = re.search(r'<meta name="description" content="([^"]*)"', html, re.I)
    return m.group(1).strip() if m else ""


def extract_canonical(html: str) -> str:
    m = re.search(r'<link rel="canonical" href="([^"]+)"', html, re.I)
    return m.group(1).strip() if m else ""


def article_headline(title: str) -> str:
    return re.sub(r"\s*—\s*Anjish Bhondwe\s*$", "", title).strip()


def json_ld_script(data: dict) -> str:
    return (
        '  <script type="application/ld+json">\n'
        + json.dumps(data, indent=2, ensure_ascii=False)
        + "\n  </script>"
    )


def inject_after_canonical(html: str, block: str) -> str:
    if has_marker(html):
        return html
    pattern = r'(<link rel="canonical" href="[^"]+"\s*/?>\s*)'
    if not re.search(pattern, html, re.I):
        pattern = r"(</head>)"
        return re.sub(pattern, block + r"\1", html, count=1, flags=re.I)
    return re.sub(pattern, r"\1" + block, html, count=1, flags=re.I)


def blog_seo_block(path: Path, html: str) -> str:
    title = extract_title(html)
    desc = extract_description(html)
    url = extract_canonical(html) or f"{SITE}/{path.name}"
    headline = article_headline(title)
    published = BLOG_DATES.get(path.name, "2025-01-01")

    article = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": headline,
        "description": desc,
        "author": {"@type": "Person", "name": AUTHOR, "url": SITE},
        "publisher": {
            "@type": "Person",
            "name": AUTHOR,
            "url": SITE,
            "logo": {"@type": "ImageObject", "url": OG_IMAGE},
        },
        "image": OG_IMAGE,
        "datePublished": published,
        "dateModified": published,
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "inLanguage": "en-GB",
        "about": ["EU AI Act", "AI Governance", "Enterprise Agile", "Digital Transformation"],
    }
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Blogs", "item": f"{SITE}/blogs.html"},
            {"@type": "ListItem", "position": 3, "name": headline, "item": url},
        ],
    }

    return f"""
{MARKER}
  <meta property="og:type" content="article">
  <meta property="og:title" content="{headline}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta property="article:author" content="{AUTHOR}">
  <meta property="article:published_time" content="{published}">
  <meta name="twitter:title" content="{headline}">
  <meta name="twitter:description" content="{desc}">
{SOCIAL_BLOCK.format(og_image=OG_IMAGE)}
{json_ld_script({"@context": "https://schema.org", "@graph": [article, breadcrumb]})}
"""


def hub_seo_block(
    html: str,
    og_type: str,
    schema: dict,
    *,
    og_title: str | None = None,
    og_desc: str | None = None,
    og_url: str | None = None,
) -> str:
    title = og_title or extract_title(html)
    desc = og_desc or extract_description(html)
    url = og_url or extract_canonical(html)

    return f"""
{MARKER}
  <meta property="og:type" content="{og_type}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
{SOCIAL_BLOCK.format(og_image=OG_IMAGE)}
{json_ld_script(schema)}
"""


def enhance_index(html: str) -> str:
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebSite",
                "@id": f"{SITE}/#website",
                "url": SITE,
                "name": "Anjish Bhondwe — Enterprise Agile & AI Governance",
                "description": extract_description(html),
                "publisher": {"@id": f"{SITE}/#person"},
                "inLanguage": "en-GB",
            },
            {
                "@type": "Person",
                "@id": f"{SITE}/#person",
                "name": "Anjish Bhondwe",
                "url": SITE,
                "image": OG_IMAGE,
                "jobTitle": [
                    "Director, Agile Centre of Excellence",
                    "AI Governance Leader",
                    "Enterprise Agile Coach",
                ],
                "worksFor": {
                    "@type": "Organization",
                    "name": "iostring Technology and Consulting",
                },
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": "Zaventem",
                    "addressRegion": "Brussels-Capital",
                    "postalCode": "1930",
                    "addressCountry": "BE",
                },
                "email": "mailto:freelanceanjish@gmail.com",
                "telephone": "+32-489-858-959",
                "sameAs": [
                    "https://www.linkedin.com/in/anjish",
                    "https://anjishbhondwe.com",
                ],
                "knowsAbout": [
                    "EU AI Act",
                    "AI Governance",
                    "IAPP AIGP",
                    "Scaled Agile",
                    "SAFe",
                    "Scrum@Scale",
                    "Enterprise Agile CoE",
                    "Digital Transformation",
                    "Financial Services Regulation",
                    "GDPR",
                    "DORA",
                ],
                "alumniOf": [
                    {"@type": "CollegeOrUniversity", "name": "Delft University of Technology"},
                    {"@type": "CollegeOrUniversity", "name": "KU Leuven"},
                ],
                "areaServed": ["BE", "NL", "DE", "GB", "EU"],
            },
            {
                "@type": "ProfessionalService",
                "@id": f"{SITE}/#services",
                "name": "Anjish Bhondwe Consulting",
                "url": SITE,
                "image": OG_IMAGE,
                "description": "Enterprise Agile CoE design, EU AI Act delivery readiness, and transformation programme leadership for regulated industries.",
                "areaServed": "Europe",
                "serviceType": [
                    "Enterprise Agile Coaching",
                    "AI Governance Consulting",
                    "EU AI Act Readiness",
                    "Digital Transformation Leadership",
                ],
                "provider": {"@id": f"{SITE}/#person"},
            },
        ],
    }

    html = re.sub(
        r'<script type="application/ld\+json">.*?</script>',
        json_ld_script(graph),
        html,
        count=1,
        flags=re.S,
    )

    extras = """
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="geo.region" content="BE-BRU">
  <meta name="geo.placename" content="Brussels">
  <meta property="og:site_name" content="Anjish Bhondwe">
  <meta property="og:locale" content="en_GB">
  <meta name="twitter:site" content="@anjish">
"""
    if 'name="geo.region"' not in html:
        html = html.replace(
            '<meta name="twitter:image"',
            extras + '  <meta name="twitter:image"',
            1,
        )

    # Normalize title before fonts comment
    html = re.sub(
        r"\s*<title>[^<]+</title>\s*\n\s*<!-- IBM Plex",
        "\n  <title>Anjish Bhondwe | Enterprise Agile CoE &amp; EU AI Act Governance (Brussels)</title>\n\n  <!-- IBM Plex",
        html,
        count=1,
    )
    return html


def enhance_work(html: str) -> str:
    if 'property="og:image"' not in html:
        html = html.replace(
            '<meta property="og:url"',
            f'<meta property="og:type" content="website">\n'
            f'  <meta property="og:image" content="{OG_IMAGE}">\n'
            f'  <meta property="og:url"',
            1,
        )
    block = hub_seo_block(
        html,
        "website",
        {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "name": "Work & Impact — Anjish Bhondwe",
            "description": extract_description(html),
            "url": f"{SITE}/work.html",
            "isPartOf": {"@type": "WebSite", "url": SITE},
        },
        og_url=f"{SITE}/work.html",
    )
    return inject_after_canonical(html, block) if not has_marker(html) else html


def enhance_contact(html: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Contact Anjish Bhondwe for enterprise Agile CoE, EU AI Act readiness, and transformation leadership. Email, phone, and LinkedIn — Brussels, Belgium.">
  <meta name="robots" content="noindex, follow">
  <link rel="canonical" href="{SITE}/">
  <meta http-equiv="refresh" content="0; url={SITE}/#contact">
  <title>Contact — Anjish Bhondwe</title>
  <script>location.replace("{SITE}/#contact");</script>
</head>
<body>
  <p>Redirecting to <a href="{SITE}/#contact">contact on anjishbhondwe.com</a>…</p>
</body>
</html>
"""


def main() -> None:
    index = (ROOT / "index.html").read_text(encoding="utf-8")
    (ROOT / "index.html").write_text(enhance_index(index), encoding="utf-8")

    for name in BLOG_DATES:
        path = ROOT / name
        html = path.read_text(encoding="utf-8")
        path.write_text(inject_after_canonical(html, blog_seo_block(path, html)), encoding="utf-8")

    for name, schema_type, schema_name in [
        ("blogs.html", "Blog", "Blogs — Anjish Bhondwe"),
        ("insights.html", "CollectionPage", "Insights — Anjish Bhondwe"),
    ]:
        path = ROOT / name
        html = path.read_text(encoding="utf-8")
        schema = {
            "@context": "https://schema.org",
            "@type": schema_type,
            "name": schema_name,
            "description": extract_description(html),
            "url": extract_canonical(html),
            "author": {"@type": "Person", "name": AUTHOR, "url": SITE},
            "isPartOf": {"@type": "WebSite", "url": SITE},
        }
        path.write_text(
            inject_after_canonical(html, hub_seo_block(html, "website", schema)),
            encoding="utf-8",
        )

    work = (ROOT / "work.html").read_text(encoding="utf-8")
    (ROOT / "work.html").write_text(enhance_work(work), encoding="utf-8")

    (ROOT / "contact.html").write_text(enhance_contact(""), encoding="utf-8")

    print("SEO applied to all pages.")


if __name__ == "__main__":
    main()
