# Wiki Schema

## Layers
- `inbox/` — drop zone for documents waiting to be ingested.
- `raw/` — canonical home for ingested source documents. Once a document is moved here by ingest, do not modify it. Text/HTML/markdown only; do not store extracted figures here.
- `index.md` — master catalog, one-line summary per page.
- `log.md` — append-only ingest log.
- `wiki/` — content pages only; you own and maintain this entirely.
- `wiki/assets/` — single canonical store for all extracted figures (`wiki/assets/<source-slug>/fig-N.<ext>`). Wiki pages and `raw/<slug>/full-article.html` reference this path; figures are not duplicated under `raw/`.
- `artifacts/` — generated interactive explainers (HTML/CSS/JS); not canonical wiki content; safe to delete or regenerate; do not use as ingest sources.
- `.agents/skills/` — repo-local workflow skills for ingest, query, query-interactive, and lint; keep these aligned with this schema.

## Storage policy
- Figures live only in `wiki/assets/`. Ingest saves images there once; `raw/` HTML may link to `../../wiki/assets/<slug>/...` but must not keep a parallel `raw/<slug>/images/` copy.
- Large binaries (PDFs, MP4) are gitignored after ingest metadata is captured; keep them locally outside version control if needed.
- Run `python3 scripts/reduce_storage.py` to prune duplicate raw images, orphan assets, and compress figures.

## Skill Routing
When a task matches ingest, query, query-interactive, or lint, read the corresponding repo-local
skill in `.agents/skills/<name>/SKILL.md` and follow it alongside this file.

## Page Format
Every page must have:
- Title, one-paragraph summary
- Body with cross-references using [[Page Name]] links
- `## Related` section at the bottom
- Tags: #concept, #entity, #summary, or #topic

## On Ingest (when told "ingest [file]")
1. Read the file in `inbox/`
2. Move it into `raw/`
3. Briefly discuss key takeaways
4. Create a new page in `wiki/`
5. Update root `index.md` and root `log.md`
6. Update any existing pages that relate or contradict

## On Query
1. Read root `index.md` first to orient
2. Drill into relevant pages
3. Answer citing specific wiki pages
4. Offer to fill gaps with new pages if needed

For a **visual / interactive** explainer saved under `artifacts/`, follow `.agents/skills/query-interactive/SKILL.md` instead of (or after) a prose-only answer.

## On Lint (when told "lint the wiki")
1. Scan all pages in `wiki/` for broken [[links]]
2. Check root `index.md` is complete
3. Check root `log.md` remains append-only
4. Flag contradictions across pages
