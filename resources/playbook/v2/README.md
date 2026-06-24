# Enterprise Agile Enablement — Playbook v2

Leadership-grade pack for agile coaches stepping into enterprise delivery enablement roles. **Not linked from the public portfolio.**

## Download (after merge)

| Document | File | Audience |
|----------|------|----------|
| **Full pack** | [00-Full-Pack-Combined.pdf](./00-Full-Pack-Combined.pdf) | Everyone |
| **Executive Brief** | [01-Executive-Brief.pdf](./01-Executive-Brief.pdf) | Sponsors, transformation board |
| **Practitioner Playbook** | [02-Practitioner-Playbook.pdf](./02-Practitioner-Playbook.pdf) | Agile coaches, CoE leads (~40 pp) |
| **Workshop Kit** | [03-Workshop-Kit.pdf](./03-Workshop-Kit.pdf) | Facilitators running operating model workshops |
| **SteerCo Pack** | [04-SteerCo-Pack.pdf](./04-SteerCo-Pack.pdf) | Leadership reporting cadence |

**Raw GitHub download (main):**  
`https://github.com/freelanceanjish/anjishbhondwe/raw/main/resources/playbook/v2/00-Full-Pack-Combined.pdf`

## What's new in v2

| v1 (8 pp) | v2 |
|-----------|-----|
| Single compressed guide | Four-document pack |
| Theory + scripts | + Executive brief, business case, case evidence |
| Basic workshop agenda | Full facilitator kit with canvas + fillable templates |
| SteerCo bullets | Slide mock-ups, metric dictionary, quarterly narratives |
| No proof points | Anonymised tier-1 bank + greenfield CoE cases |

## Regenerate PDFs

```bash
cd resources/playbook/v2
./build-pdfs.sh
```

Requires Google Chrome (headless). Installs `pypdf` and `reportlab` automatically if needed.

Footers (`Anjish Bhondwe · anjishbhondwe.com`) are stamped onto every page after render via `stamp_pdf_footer.py` — Chrome CSS footers are not used.

## Source files

- `01-executive-brief.html`
- `02-practitioner-playbook.html`
- `03-workshop-kit.html`
- `04-steerco-pack.html`
- `styles/print.css`

v1 remains at `resources/playbook/` for reference.
