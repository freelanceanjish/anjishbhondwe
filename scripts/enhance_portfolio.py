#!/usr/bin/env python3
"""Apply portfolio + LinkedIn integration enhancements."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://anjishbhondwe.com"
LI = "https://www.linkedin.com/in/anjish"
LI_UTM = f"{LI}?utm_source=anjishbhondwe&utm_medium=portfolio"
EMAIL = "freelanceanjish@gmail.com"

HEAD_EXTRA = f"""  <link rel="canonical" href="{SITE}/">
  <meta property="og:type" content="website">
  <meta property="og:description" content="Enterprise Agile CoE leader and IAPP-certified AI Governance Professional. EU AI Act readiness embedded in delivery for regulated financial services and innovators.">
  <meta property="og:image" content="{SITE}/profile.jpg">
  <meta property="og:url" content="{SITE}/">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Anjish Bhondwe | Enterprise Agile and AI Governance Leader">
  <meta name="twitter:description" content="Compliant Velocity: Agile delivery and EU AI Act governance for regulated enterprises.">
  <meta name="twitter:image" content="{SITE}/profile.jpg">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Anjish Bhondwe",
    "url": "{SITE}",
    "image": "{SITE}/profile.jpg",
    "jobTitle": "Director, Agile CoE and AI Governance Leader",
    "worksFor": {{ "@type": "Organization", "name": "iostring Technology and Consulting" }},
    "address": {{ "@type": "PostalAddress", "addressLocality": "Zaventem", "addressRegion": "Brussels", "addressCountry": "BE" }},
    "email": "{EMAIL}",
    "sameAs": ["{LI}"],
    "knowsAbout": ["EU AI Act", "AI Governance", "Scaled Agile", "SAFe", "Enterprise Agile CoE", "Digital Transformation", "Financial Services"]
  }}
  </script>"""

TRUST_STRIP = """
<!-- ── TRUST STRIP ── -->
<div class="trust-strip">
  <div class="smax trust-strip__inner reveal">
    <span class="trust-strip__item"><strong>AIGP</strong> · IAPP</span>
    <span class="trust-strip__sep">|</span>
    <span class="trust-strip__item"><strong>EU AI Act</strong> · Delft University</span>
    <span class="trust-strip__sep">|</span>
    <span class="trust-strip__item">KU Leuven AI Law · <strong>Completed Mar 2026</strong></span>
    <span class="trust-strip__sep">|</span>
    <span class="trust-strip__item">ICP-ACC · ICP-ENT · SAFe</span>
  </div>
</div>
"""

SERVICES_SECTION = """
<div class="grid-rule"></div>

<!-- ── SERVICES ── -->
<section id="services">
  <div class="smax">
    <div class="label reveal">How I engage</div>
    <h2 class="section-title reveal">Consulting <strong>Services</strong></h2>
    <p class="section-desc reveal">Focused mandates for regulated enterprises — from operating-model design through programme leadership to embedded governance.</p>
    <div class="services-grid reveal">
      <div class="service-card">
        <div class="service-card__num">01</div>
        <h3>Enterprise Agile CoE</h3>
        <p>Design and stand up Centres of Excellence with clear authority, coaching models, and executive-ready governance rhythms.</p>
        <p class="service-card__term">Typical engagement: 3–6 months</p>
      </div>
      <div class="service-card">
        <div class="service-card__num">02</div>
        <h3>EU AI Act Delivery Readiness</h3>
        <p>Embed compliance obligations into Agile artefacts, ceremonies, and backlog structure — not a parallel compliance workstream.</p>
        <p class="service-card__term">Typical engagement: 2–4 months</p>
      </div>
      <div class="service-card">
        <div class="service-card__num">03</div>
        <h3>Transformation Programme Leadership</h3>
        <p>Lead multi-team programmes under ECB, GDPR, and board scrutiny — including scaled onshore-offshore delivery at 50+ people.</p>
        <p class="service-card__term">Typical engagement: 6–12 months</p>
      </div>
      <div class="service-card">
        <div class="service-card__num">04</div>
        <h3>Executive Coaching &amp; PI Governance</h3>
        <p>Coach leaders and RTEs on flow, risk, and SteerCo reporting that satisfies regulators and delivery reality.</p>
        <p class="service-card__term">Typical engagement: ongoing advisory</p>
      </div>
    </div>
  </div>
</section>
"""

CASE_AND_LI = f"""
    <div class="case-highlights reveal">
      <div class="case-card">
        <div class="case-card__client">KBC Bank</div>
        <p class="case-card__outcome">Led scaled Agile delivery for <strong>Europe's first blockchain-based digital coin (Kate Coin)</strong> under ECB regulatory constraints.</p>
        <a class="case-card__link" href="#experience">View experience →</a>
      </div>
      <div class="case-card">
        <div class="case-card__client">HealthRFID</div>
        <p class="case-card__outcome">Business Analyst consulting in Australia on <strong>regulated biologic supply chain</strong> and RFID-enabled platform delivery.</p>
        <a class="case-card__link" href="#experience">View experience →</a>
      </div>
      <div class="case-card">
        <div class="case-card__client">Education Horizons</div>
        <p class="case-card__outcome">Drove platform adoption from <strong>below 30% to above 80%</strong> through Agile transformation and AWS delivery practices.</p>
        <a class="case-card__link" href="#experience">View experience →</a>
      </div>
    </div>
    <div class="clients-linkedin-cta reveal">
      <p>Shorter perspectives, frameworks, and regulatory commentary on LinkedIn.</p>
      <a class="btn-primary" href="{LI_UTM}" target="_blank" rel="noopener noreferrer">Follow on LinkedIn →</a>
    </div>
"""

BLOGS_STRIP = """
    <p class="section-desc reveal" style="margin-top:var(--s2)">Long-form analysis lives on this site — LinkedIn carries shorter commentary and debate.</p>
    <div class="onsite-blogs reveal">
      <a class="onsite-blog-card featured" href="blog-eu-ai-act-agile-coalesce.html">
        <span class="onsite-blog-card__tag">★ Featured</span>
        <h3 class="onsite-blog-card__title">EU AI Act + Agile Delivery: How They Technically Coalesce</h3>
        <p class="onsite-blog-card__desc">Nine obligations mapped to Agile artefacts — compliance as engineering specification.</p>
        <span class="onsite-blog-card__link">Read on site →</span>
      </a>
      <a class="onsite-blog-card" href="blog-eu-ai-act.html">
        <h3 class="onsite-blog-card__title">EU AI Act: Governance Pillars &amp; What Organisations Must Do Now</h3>
        <span class="onsite-blog-card__link">Read on site →</span>
      </a>
      <a class="onsite-blog-card" href="blog-ai-governance-agile.html">
        <h3 class="onsite-blog-card__title">Embedding AI Governance Into Agile Delivery from Day One</h3>
        <span class="onsite-blog-card__link">Read on site →</span>
      </a>
      <a class="onsite-blog-card" href="blogs.html">
        <h3 class="onsite-blog-card__title">All blogs &amp; deep-dives</h3>
        <span class="onsite-blog-card__link">View full library →</span>
      </a>
    </div>
    <div class="articles-divider reveal">
      <span>Also on LinkedIn</span>
    </div>
"""

CONTACT_FORM_BLOCK = f"""
        <div class="contact-form-wrap reveal reveal-d1">
          <h3 class="contact-form-title">Send a message</h3>
          <form id="portfolio-contact-form" class="portfolio-form" novalidate>
            <div class="form-row-2">
              <div class="form-field">
                <label for="cf-name">Name *</label>
                <input type="text" id="cf-name" name="name" required autocomplete="name">
              </div>
              <div class="form-field">
                <label for="cf-email">Email *</label>
                <input type="email" id="cf-email" name="email" required autocomplete="email">
              </div>
            </div>
            <div class="form-field">
              <label for="cf-company">Organisation</label>
              <input type="text" id="cf-company" name="company" autocomplete="organization">
            </div>
            <div class="form-field">
              <label for="cf-type">Inquiry type</label>
              <select id="cf-type" name="inquiry">
                <option value="Transformation / Agile CoE">Transformation / Agile CoE</option>
                <option value="EU AI Act readiness">EU AI Act readiness</option>
                <option value="Programme leadership">Programme leadership</option>
                <option value="Speaking">Speaking engagement</option>
                <option value="Other">Other</option>
              </select>
            </div>
            <div class="form-field">
              <label for="cf-message">Message *</label>
              <textarea id="cf-message" name="message" rows="4" required></textarea>
            </div>
            <button type="submit" class="btn-primary" style="width:100%;justify-content:center">Send message →</button>
            <p class="form-hint">Opens your email client with a pre-filled message — no backend required.</p>
          </form>
        </div>
"""


def patch_index():
    p = ROOT / "index.html"
    t = p.read_text()

    # Meta 16 -> 13
    t = t.replace("16+ years", "13+ years")
    t = t.replace("16<span>+</span>", "13<span>+</span>")
    t = t.replace("With over <strong>16 years", "With <strong>13+ years")
    t = re.sub(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="Anjish Bhondwe — Enterprise Agile CoE leader and IAPP-certified AI Governance Professional (AIGP). 13+ years in regulated financial services. EU AI Act readiness embedded in delivery. Based in Brussels.">',
        t,
        count=1,
    )

    if "rel=\"canonical\"" not in t:
        t = t.replace(
            '<meta name="author" content="Anjish Bhondwe">',
            '<meta name="author" content="Anjish Bhondwe">\n' + HEAD_EXTRA,
        )
        t = re.sub(
            r'<meta property="og:image" content="profile\.jpg">\s*\n\s*<meta property="og:url"[^>]+>\n',
            "",
            t,
        )

    # Nav
    t = t.replace('<li><a href="#expertise">Expertise</a></li>', '<li><a href="#services">Services</a></li>\n    <li><a href="#expertise">Expertise</a></li>')
    t = t.replace(
        '<a class="nav-cta" href="#contact">Let\'s Connect</a>',
        f'<a class="nav-linkedin" href="{LI_UTM}" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn profile">in</a>\n  <a class="nav-cta" href="#contact">Let\'s Connect</a>',
    )
    for menu in ('<div id="mobile-menu">',):
        if menu in t and "#services" not in t.split("mobile-menu")[1][:800]:
            t = t.replace(
                '<li><a href="#about">About</a></li>\n    <li><a href="#expertise">Expertise</a></li>',
                '<li><a href="#about">About</a></li>\n    <li><a href="#services">Services</a></li>\n    <li><a href="#expertise">Expertise</a></li>',
                1,
            )
    if "nav-linkedin" not in t.split("mobile-menu")[0]:
        pass
    t = t.replace(
        '<li><a href="#contact">Contact</a></li>\n  </ul>\n</div>',
        f'<li><a href="{LI_UTM}" target="_blank" rel="noopener noreferrer">LinkedIn</a></li>\n    <li><a href="#contact">Contact</a></li>\n  </ul>\n</div>',
        1,
    )

    # Hero
    t = t.replace(
        '<p class="hero-title">Director, Agile CoE',
        '<p class="hero-offer reveal">I help regulated enterprises build <strong>Agile CoEs</strong> and <strong>EU AI Act–ready delivery</strong> — without compliance theatre.</p>\n      <p class="hero-title">Director, Agile CoE',
    )
    t = re.sub(
        r'<p class="hero-desc">\s*I build.*?failure is simply not an option</strong>\.\s*</p>',
        """<p class="hero-desc">
        I build <strong>Compliant Velocity</strong>: Agile delivery engines for AI that meet the EU AI Act by design.
        With <strong>13+ years</strong> embedded inside complex European Financial Services, I lead high-stakes transformations
        where <strong>failure is simply not an option</strong>.
      </p>
      <p class="hero-availability">Available for advisory and programme leadership · Brussels &amp; Benelux · Remote across Europe</p>""",
        t,
        flags=re.DOTALL,
    )
    t = t.replace(
        '<div class="hero-buttons">\n        <a class="btn-primary" href="#contact">Work With Me</a>\n        <a class="btn-ghost" href="#experience">View Experience</a>\n      </div>',
        f"""<div class="hero-buttons">
        <a class="btn-primary" href="#contact">Work With Me</a>
        <a class="btn-ghost btn-linkedin" href="{LI_UTM}" target="_blank" rel="noopener noreferrer">Connect on LinkedIn</a>
        <a class="btn-ghost" href="#experience">View Experience</a>
      </div>""",
    )

    if "trust-strip" not in t:
        t = t.replace("</section>\n\n<div class=\"grid-rule\"></div>\n\n<!-- ── ABOUT ── -->", "</section>\n" + TRUST_STRIP + "\n<div class=\"grid-rule\"></div>\n\n<!-- ── ABOUT ── -->", 1)

    # About text
    old_about = """        <p>I am currently deepening this expertise through
        <strong>AI Regulation: Navigating The EU AI Act at Delft University of Technology</strong>, alongside
        studies in <strong>AI Regulation and Law at KU Leuven</strong> and IAPP membership. I help
        organisations build Agile delivery practices fully ready for the EU AI Act before it lands as a crisis.</p>"""
    new_about = """        <p>I am an <strong>IAPP-certified AI Governance Professional (AIGP)</strong> and am currently studying
        <strong>AI Regulation: Navigating The EU AI Act at Delft University of Technology, Netherlands</strong>.
        I completed <strong>AI Regulation and Law at KU Leuven</strong> in <strong>March 2026</strong>. I help
        organisations build Agile delivery practices fully ready for the EU AI Act before it lands as a crisis.</p>"""
    if old_about in t:
        t = t.replace(old_about, new_about)
    t = t.replace(
        "With over <strong>13+ years embedded inside complex European, UK, and Swiss Financial Services</strong>",
        "With <strong>13+ years embedded inside complex European, UK, and Swiss Financial Services</strong>",
    )

    if 'id="services"' not in t:
        t = t.replace(
            "</section>\n\n<div class=\"grid-rule\"></div>\n\n<!-- ── EXPERTISE ── -->",
            "</section>\n" + SERVICES_SECTION + "\n<div class=\"grid-rule\"></div>\n\n<!-- ── EXPERTISE ── -->",
            1,
        )

    # Cases + linkedin after clients footnote
    if "case-highlights" not in t:
        t = t.replace(
            '<p class="clients-footnote reveal">Representative clients and partners from programmes delivered across Europe, South Africa, North America, and Australia.</p>',
            '<p class="clients-footnote reveal">Representative clients and partners from programmes delivered across Europe, South Africa, North America, and Australia.</p>\n' + CASE_AND_LI,
        )

    # Articles onsite blogs
    if "onsite-blogs" not in t:
        t = t.replace(
            '<h2 class="section-title reveal">Published <strong>Articles</strong></h2>\n    <div class="articles-grid">',
            '<h2 class="section-title reveal">Thought <strong>Leadership</strong></h2>\n' + BLOGS_STRIP + '\n    <div class="articles-grid">',
        )

    # Credentials
    t = t.replace(
        '<div class="edu-school">Delft University of Technology</div>\n          <div class="edu-wip">Currently learning online</div>',
        '<div class="edu-school">Delft University of Technology, Netherlands</div>\n          <div class="edu-wip">Currently learning</div>',
    )
    t = t.replace(
        """        <div class="edu-item active">
          <div class="edu-deg">AI Regulation and Law</div>
          <div class="edu-school">KU Leuven</div>
          <div class="edu-year">2025 / 2026 · Belgium</div>
        </div>""",
        """        <div class="edu-item">
          <div class="edu-deg">AI Regulation and Law</div>
          <div class="edu-school">KU Leuven, Belgium</div>
          <div class="edu-year">Completed · March 2026</div>
        </div>""",
    )
    t = t.replace(
        '<div class="cert-wip">In progress, June / July 2026</div>',
        '<div class="edu-year">Completed</div>',
    )

    # Contact
    t = t.replace("https://linkedin.com/in/anjish", LI_UTM)
    t = t.replace("anjish.bhondwe@gmail.com", EMAIL)
    if "portfolio-contact-form" not in t:
        t = t.replace(
            '<a class="btn-primary" href="mailto:freelanceanjish@gmail.com" style="margin-top:1.5rem;display:inline-flex">Start the Conversation</a>',
            f"""<div class="contact-actions">
          <a class="btn-primary" href="mailto:{EMAIL}?subject=Discovery%20call%20with%20Anjish%20Bhondwe" style="display:inline-flex">Book a discovery call</a>
          <a class="btn-ghost btn-linkedin" href="{LI_UTM}" target="_blank" rel="noopener noreferrer" style="display:inline-flex">Connect on LinkedIn</a>
        </div>""" + CONTACT_FORM_BLOCK,
        )
    t = t.replace("<p>2025 Anjish", "<p>2026 Anjish")
    t = t.replace(
        '<p class="contact-desc">I engage where complexity is high',
        '<p class="contact-desc">I engage where complexity is high and execution must be precise — across financial services, health technology, and regulated industries in Europe and beyond.',
    )
    # fix double "and beyond" if applied twice
    t = t.replace("in Europe and beyond. and execution", "in Europe and beyond. I engage where complexity is high and execution")

    p.write_text(t)
    print("index.html patched")


def patch_html_file(path: Path):
    if not path.exists():
        return
    t = path.read_text()
    t = t.replace("https://anjish.io/", SITE + "/")
    t = t.replace("http://anjish.io/", SITE + "/")
    t = t.replace("anjish.io", "anjishbhondwe.com")
    t = t.replace("https://linkedin.com/in/anjish", LI_UTM)
    t = t.replace("http://linkedin.com/in/anjish", LI_UTM)
    t = t.replace("anjish.bhondwe@gmail.com", EMAIL)
    t = t.replace("16+ Years Experience", "13+ Years Experience")
    t = t.replace("16+ years", "13+ years")
    path.write_text(t)
    print(f"patched {path.name}")


def patch_sitemap():
    p = ROOT / "sitemap.xml"
    urls = [
        ("", "weekly", "1.0"),
        ("blogs.html", "weekly", "0.9"),
        ("blog-eu-ai-act.html", "monthly", "0.85"),
        ("blog-eu-ai-act-agile-coalesce.html", "monthly", "0.85"),
        ("blog-ai-governance-agile.html", "monthly", "0.85"),
        ("blog-agile-transformations.html", "monthly", "0.8"),
        ("work.html", "monthly", "0.8"),
        ("insights.html", "weekly", "0.75"),
        ("contact.html", "yearly", "0.6"),
    ]
    body = "\n".join(
        f"""  <url>
    <loc>{SITE}/{u}</loc>
    <changefreq>{cf}</changefreq>
    <priority>{pr}</priority>
  </url>"""
        for u, cf, pr in urls
    )
    p.write_text(
        f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{body}
</urlset>
"""
    )
    print("sitemap.xml updated")


def patch_contact_redirect():
    p = ROOT / "contact.html"
    p.write_text(
        f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url={SITE}/#contact">
  <link rel="canonical" href="{SITE}/#contact">
  <title>Contact — Anjish Bhondwe</title>
  <script>location.replace("{SITE}/#contact");</script>
</head>
<body>
  <p>Redirecting to <a href="{SITE}/#contact">contact section</a>…</p>
</body>
</html>
"""
    )
    print("contact.html redirect")


def patch_main_js():
    p = ROOT / "main.js"
    t = p.read_text()
    form_handler = """
/* ── CONTACT FORM (mailto) ── */
const contactForm = document.getElementById('portfolio-contact-form');
contactForm?.addEventListener('submit', e => {
  e.preventDefault();
  const name = document.getElementById('cf-name')?.value?.trim() || '';
  const from = document.getElementById('cf-email')?.value?.trim() || '';
  const company = document.getElementById('cf-company')?.value?.trim() || '';
  const inquiry = document.getElementById('cf-type')?.value || '';
  const message = document.getElementById('cf-message')?.value?.trim() || '';
  const subject = encodeURIComponent(`Portfolio inquiry: ${inquiry}`);
  const body = encodeURIComponent(
    `Name: ${name}\\nEmail: ${from}\\nOrganisation: ${company}\\nInquiry: ${inquiry}\\n\\n${message}`
  );
  window.location.href = `mailto:freelanceanjish@gmail.com?subject=${subject}&body=${body}`;
});
"""
    if "portfolio-contact-form" not in t:
        t = t.rstrip() + "\n" + form_handler
    t = re.sub(
        r"/\* ── CLIENT LOGOS.*?\}\);\n",
        "/* client cards: styled via CSS */\n",
        t,
        flags=re.DOTALL,
    )
    p.write_text(t)
    print("main.js patched")


def main():
    patch_index()
    for name in [
        "blog-agile-transformations.html",
        "blog-ai-governance-agile.html",
        "blog-eu-ai-act-agile-coalesce.html",
        "blog-eu-ai-act.html",
        "blogs.html",
        "insights.html",
        "work.html",
    ]:
        patch_html_file(ROOT / name)
    patch_sitemap()
    patch_contact_redirect()
    patch_main_js()


if __name__ == "__main__":
    main()
