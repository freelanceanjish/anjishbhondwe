# Leaseweb — Agile Team Manager Application

Tailored application documents for the **Agile Team Manager** role (Product Engineering) at Leaseweb, Amsterdam.

| File | Description |
| --- | --- |
| `anjish-bhondwe-cv-leaseweb.pdf` | CV (A4, 2 pages) — ready to send |
| `anjish-bhondwe-cv-leaseweb.html` | Editable source for the CV |
| `anjish-bhondwe-cover-letter-leaseweb.pdf` | Cover letter (A4, 1 page) — ready to send |
| `anjish-bhondwe-cover-letter-leaseweb.html` | Editable source for the cover letter |

## Editing and regenerating the PDFs

The HTML files are self-contained (no external assets). To edit, change the `.html`
file and regenerate the PDF with headless Chrome:

```bash
google-chrome --headless=new --no-pdf-header-footer \
  --print-to-pdf=anjish-bhondwe-cv-leaseweb.pdf \
  "file://$PWD/anjish-bhondwe-cv-leaseweb.html"
```

The documents are tailored to Leaseweb's stated expectations: Scrum facilitation,
coaching and mentoring, people management / performance appraisals, raising team
maturity, partnering with the Product Owner, organisational transparency, and
hands-on technical involvement with cloud/hosting/infrastructure.
