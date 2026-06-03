# Google Search Console API (optional, one-time setup)

Automated sitemap submission runs in GitHub Actions when `GOOGLE_SEARCH_CONSOLE_JSON` is set.

## 1. Google Cloud (as freelanceanjish@gmail.com)

1. [Google Cloud Console](https://console.cloud.google.com/) → create or pick a project.
2. **APIs & Services → Library** → enable **Google Search Console API**.
3. **IAM & Admin → Service accounts** → **Create service account** (any name).
4. **Keys → Add key → JSON** → download the file.

## 2. Search Console (same Google account)

1. Open [Users and permissions](https://search.google.com/search-console/users?resource_id=https%3A%2F%2Fanjishbhondwe.com%2F)
2. **Add user** → paste the service account email (e.g. `something@project-id.iam.gserviceaccount.com`)
3. Permission: **Owner** or **Full**

## 3. GitHub secret

1. Repo **Settings → Secrets and variables → Actions → New repository secret**
2. Name: `GOOGLE_SEARCH_CONSOLE_JSON`
3. Value: entire contents of the JSON key file (one line is fine)

Push to `main` or re-run the **Submit URLs to search engines** workflow. The job will call the API and submit `https://anjishbhondwe.com/sitemap.xml`.

## Without API (manual, ~30 seconds)

In [Search Console](https://search.google.com/search-console?resource_id=https%3A%2F%2Fanjishbhondwe.com%2F) → **Sitemaps** → enter `sitemap.xml` → **Submit**.

Google also reads `Sitemap:` from `https://anjishbhondwe.com/robots.txt` after verification.
