# Anjish Bhondwe — Portfolio

> Digital Transformation Lead · Enterprise Agile Coach · AI Strategist

Multi-file, data-driven, SEO-optimised portfolio site. Zero build tools required — pure HTML, CSS, and ES Modules.

---

## 🗂 File Structure

```
portfolio/
├── index.html              ← Home (hero, expertise, projects, insights, clients)
├── work.html               ← Full case studies / impact projects
├── insights.html           ← Articles & thought leadership
├── contact.html            ← Contact form + direct info
├── sitemap.xml             ← SEO sitemap (update domain after deploy)
├── robots.txt              ← Search engine crawl rules
│
├── css/
│   ├── variables.css       ← Design tokens (colors, fonts, spacing)
│   ├── base.css            ← Reset, typography, global utilities
│   └── components.css      ← All UI component styles
│
├── js/
│   ├── main.js             ← Home page entry point
│   ├── cursor.js           ← Custom cursor behaviour
│   ├── nav.js              ← Navigation (scroll, mobile, active state)
│   ├── animations.js       ← IntersectionObserver reveal animations
│   ├── components.js       ← DOM renderers (pulls from data files)
│   └── data/
│       ├── expertise.js    ← Expertise areas data
│       ├── projects.js     ← Impact case studies data
│       ├── insights.js     ← Articles / thought leadership data
│       └── clients.js      ← Client logos / names data
│
└── images/
    ├── kbc.png
    ├── hsbc.png
    ├── ubs.png
    ├── standard-bank.png
    ├── colruyt.jpeg
    ├── uplight.jpeg
    └── education-horizons.jpg
```

---

## 🚀 Deploy to GitHub Pages

### Option A — GitHub Pages (recommended, free)

1. Create a new repo: `github.com/new` → name it `anjish.github.io` (or any name)
2. Upload all files (maintain folder structure)
3. Go to **Settings → Pages → Source** → select `main` branch, root `/`
4. Your site is live at `https://yourname.github.io/` (or custom domain)

### Option B — Custom Domain

1. Add a `CNAME` file containing your domain (e.g. `anjish.io`)
2. In your domain registrar, point DNS to GitHub Pages IPs:
   ```
   185.199.108.153
   185.199.109.153
   185.199.110.153
   185.199.111.153
   ```
3. Enable HTTPS in repo Settings → Pages

### Option C — Netlify (drag & drop)

1. Go to [netlify.com](https://netlify.com) → New site → Drag folder
2. Done. Auto HTTPS, custom domain support.

---

## ✏️ How to Update Content

### Add a new project / case study

Edit `js/data/projects.js` — add a new object to the array:

```js
{
  id: 'my-new-project',
  org: 'Client Name',
  period: '2024 – Present · Location',
  title: 'Project Title',
  description: 'What you did and why it mattered.',
  logo: 'images/client-logo.png',
  logoAlt: 'Client Name',
  metrics: [
    { num: '40%', label: 'Improvement metric' },
    { num: '6mo', label: 'Delivery time' },
    // up to 4 metrics
  ],
  tags: ['Tag1', 'Tag2'],
  link: 'https://link-to-case-study.com',
  linkLabel: 'Read More',
  featured: true
}
```

### Add a new article

Edit `js/data/insights.js` — add a new object:

```js
{
  id: 'my-article',
  topic: 'AI Strategy',
  title: 'Article Title',
  excerpt: 'A short description of the article.',
  date: '2025',
  readTime: '5 min',
  url: 'https://linkedin.com/...',
  tags: ['AI', 'Strategy']
}
```

### Add a new client logo

1. Place image in `images/` folder
2. Edit `js/data/clients.js` — add:
```js
{ id: 'client-id', name: 'Client Name', logo: 'images/logo.png', type: 'image' }
```

### Update contact details

Edit the contact info in `contact.html` directly (phone, email, LinkedIn).

---

## 🎨 Theming

All design tokens are in `css/variables.css`:
- `--clr-gold` — primary accent colour
- `--clr-cyan` — secondary accent
- `--clr-bg` — background
- `--font-display` — heading font (Cormorant Garamond)
- `--font-body` — body font (Plus Jakarta Sans)

---

## 🔍 SEO Checklist

After deploying:
- [ ] Update `<link rel="canonical">` URLs in all HTML files to your actual domain
- [ ] Update `sitemap.xml` `<loc>` values to your domain
- [ ] Update `robots.txt` Sitemap URL
- [ ] Update JSON-LD `"url"` fields in `index.html`
- [ ] Submit sitemap to [Google Search Console](https://search.google.com/search-console)
- [ ] Add an `og-cover.jpg` (1200×630px) to `images/` for social sharing previews

---

## 📄 License

© Anjish Bhondwe. All rights reserved.
