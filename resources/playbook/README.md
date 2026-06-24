# Enterprise Agile Enablement — Study Bible & Playbook

Standalone resource for agile coaches stepping into enterprise delivery enablement roles. **Not part of the public portfolio site.**

## Download

**[Enterprise-Agile-Enablement-Study-Bible-and-Playbook.pdf](./Enterprise-Agile-Enablement-Study-Bible-and-Playbook.pdf)**

## Contents

| Part | Focus |
|------|--------|
| **Part I — Study Bible** | Mindset shift, capability map, 30/60/90 learning plan, operating model sketches, framework mix, red flags |
| **Part II — Leadership Playbook** | 8-step rollout, diagnosis, half-day workshop, SteerCo scripts, first 90 days, templates |

## Regenerate PDF

```bash
google-chrome --headless=new --disable-gpu --no-sandbox \
  --user-data-dir=/tmp/chrome-pdf-profile \
  --run-all-compositor-stages-before-draw \
  --virtual-time-budget=15000 \
  --print-to-pdf=Enterprise-Agile-Enablement-Study-Bible-and-Playbook.pdf \
  file://$(pwd)/enterprise-agile-enablement-playbook.html
```

Source HTML: `enterprise-agile-enablement-playbook.html`
