---
name: ingest
description: Process a new source document into the wiki. Trigger when the user says "ingest [file]", "ingest [url]", "add this to the wiki", or "process [file]". Do not trigger for general questions or edits to existing pages.
---

# Ingest Skill

## Input
The user provides one of:
- A file path inside `inbox/`. Example: `ingest inbox/paper.pdf`
- A URL to a public web article. Example: `ingest https://example.com/blog/post`
- An already-saved file inside `raw/` (when the source has previously been partially ingested or staged outside `inbox/`).

Pick the path that matches the input and continue with the corresponding "Step 1" branch below. The downstream steps (extract, write wiki pages, update index/log) are shared.

## Steps

### 1a. Read the source from `inbox/` (file path input)
Read the full contents of the file at the given path in `inbox/`.
Confirm the file is a new ingest candidate and derive the destination path in `raw/`.

### 1b. Fetch the source from a URL (URL input)
Derive a stable kebab-case slug from the article (typically the URL's last path segment, lowercased and de-duped). Examples: a Cursor blog post at
`cursor.com/blog/continually-improving-agent-harness` becomes `continually-improving-agent-harness`; an X article gets a `<author>-<title>` slug as in Step 3c.

Create `raw/<slug>/` and save the canonical artifact:

- `raw/<slug>/full-article.md` — readable markdown extraction. Fetch HTML with `curl -fsSL` (or WebFetch) into a **temp file only**, convert to markdown (pandoc, WebFetch markdown, or html-to-text), then write `full-article.md`. **Do not** keep `full-article.html` in `raw/`.

Do not store unrelated assets (fonts, scripts, avatars, OpenGraph/preview images, navigation chrome). Only article figures referenced from the article body should be saved (see Step 3b).

If the page requires authentication, JavaScript rendering, or a headless browser to load (e.g. paywalled or SPA-only content), tell the user before fetching and ask them to either provide a saved browser export under `inbox/` or grant explicit permission to use a heavier renderer.

### 1c. Continue from a partially-ingested `raw/` artifact (recovery input)
If the source already lives under `raw/<slug>/` from a prior incomplete ingest:
- Treat the existing files as canonical and do not refetch unless the user asks.
- Audit which downstream artifacts are missing (wiki summary page, concept stubs, figures, index/log entries, cross-references) and complete only what is missing.
- Record the recovery in `log.md` as a follow-up row referencing the original ingest row, rather than overwriting history.

### 2. Move the source into `raw/`
For inbox-file inputs, move the file from `inbox/` to `raw/` before creating wiki content. For URL inputs, the artifacts are already written into `raw/<slug>/` in Step 1b. For recovery inputs, the source already lives in `raw/`.
After the move (or initial save):
- Treat the file in `raw/` as the canonical source of record
- Do not modify the file contents in `raw/`
- Use the `raw/` path in all wiki metadata, logs, and follow-up references

Exception for browser exports: if the inbox source is a saved web page export with a companion assets directory, you may use the export as a staging source to create a clean canonical raw artifact. 
Preserve only the cleaned article body as markdown; do not keep unused browser runtime files, avatars, preloaded JavaScript bundles, fonts, or unrelated page chrome unless the user explicitly asks for a forensic copy of the original export.

Large source binaries (PDF, MP4) may be kept locally under `raw/` but are gitignored after ingest. Record the local path and any public URL on the wiki summary page; extracted figures still go to `wiki/assets/`.

### 3. Extract & discuss
Briefly surface to the user:
- The 3-5 most important ideas or claims
- Any entities (people, orgs, tools, concepts) worth tracking
- Whether anything contradicts or extends existing wiki pages
Ask the user if they want to emphasize or deprioritize anything before writing.

### Step 3b. Extract & save images
Scan the source document for any embedded images, figures, diagrams, 
charts, or screenshots.

For each image found:
1. Extract it and save to `wiki/assets/<source-slug>/fig-<N>.webp`
   (use `.gif` or `.svg` only when the source requires animation or vector fidelity)
2. Generate a short descriptive filename alias based on what the image 
   shows — store this in a local mapping for use in the summary page.
   Example: fig-1.webp → "transformer-architecture-overview"
3. Write a one-line caption describing what the image shows.

Image extraction strategy by file type:
- **PDF**: use `pdfimages` or `pymupdf` to extract embedded images 
  page by page. Note the page number alongside each image.
- **DOCX / PPTX**: unzip the file and pull images from `word/media/` 
  or `ppt/media/`.
- **Markdown / HTML**: copy any locally referenced images; 
  note any remote URLs.
- **Fetched web article (URL ingest)**: parse the fetched HTML (temp file or in-memory) for
  `<img>`, `<figure>`, `<source>`, and `srcSet` URLs that sit inside the article
  body. Download each unique article figure (and dark-mode variant when
  present) into `wiki/assets/<slug>/fig-<N>.webp` only — do not create
  `raw/<slug>/images/`. Reference figures from wiki pages as
  `../assets/<slug>/fig-<N>.webp`. Suffix dark-mode variants
  `fig-<N>-dark.webp` so the light version remains the canonical reference.
  Skip avatar images,
  navigation chrome, OpenGraph/preview images, related-post thumbnails, and
  CDN-rewritten next/image URLs that resolve to those assets. If the markdown
  export of the same source did not surface the figures (common for SPA-rendered
  pages), prefer the figures discovered in the HTML and treat them as the
  authoritative figure set.
- **X/Twitter article browser export**: treat the export as a noisy rendered
  source. Extract longform article blocks in document order, save
  `raw/<source-slug>/full-article.md`, and save article figures only to
  `wiki/assets/<source-slug>/fig-<N>.webp`. Exclude profile photos, avatars,
  scripts, fonts, and unrelated `X_files/` assets from the final raw directory.
  If the export contains remote media URLs, download those images and store them
  with the same `fig-<N>` convention instead of linking to remote media.
- **Scanned PDFs with no extractable images**: rasterize the relevant 
  page as a PNG using `pdftoppm` at 150dpi and save it as a figure.

If no images are found, skip this step and note 
"No images found" in the log entry.

### Step 3c. X/Twitter article cleanup
When ingesting an X/Twitter article from a local browser export:

1. Derive a stable slug from the author and title, for example
   `will-brown-on-sft-rl-on-policy-distillation`.
2. Create `raw/<source-slug>/full-article.md` as the canonical readable raw
   source with article title, author/date metadata, source URL, and body in
   document order.
3. Create `wiki/assets/<source-slug>/` with exactly the figures referenced by
   the wiki summary. Do not create `raw/<source-slug>/images/`.
4. Remove or skip unused export artifacts before finishing:
   - `browser-export/`, `X_files/`, scripts, fonts, preloads
   - profile/avatar images
   - images not referenced by the wiki summary
5. In wiki pages and `log.md`, reference `raw/<source-slug>/full-article.md`, not a
   removed browser-export path.

### Step 3d. Fetched web article cleanup
When ingesting a public web article via URL (Step 1b):

1. Confirm `raw/<slug>/full-article.md` exists. Note its byte size and the source URL in the wiki summary.
2. Verify the markdown contains the article body, not a login wall or a
   skeleton SPA shell. A reliable check: search for a known phrase from the
   user's request or the page title. If the body is missing, stop and ask the
   user for a saved browser export instead of silently writing wiki pages from
   incomplete extraction.
3. Discover article figures from the fetched HTML (see Step 3b's "Fetched web article"
   bullet). Save them under `wiki/assets/<slug>/fig-<N>.webp` only. Do not download avatars,
   OpenGraph images, related-post thumbnails, fonts, or scripts.
4. Reference `raw/<slug>/full-article.md` as the canonical raw source in the wiki summary page.
5. In `log.md`, list the markdown path. Note which figures were saved and how many.

### 4. Create the summary page
Create `wiki/summaries/<slug>.md` where `<slug>` is a kebab-case version of 
the source title.

Page format:
```
# <Title>

**Source**: `raw/<filename>` (or `raw/<slug>/full-article.md` for URL ingests)  
**Ingested**: <YYYY-MM-DD>  
**Tags**: #summary

## Summary
2–4 paragraph synthesis of the source in your own words.

## Key Claims
- Bullet list of the most important factual claims or arguments.

## Figures
| Figure | Caption | Page |
|--------|---------|------|
| ![fig-1](../assets/<source-slug>/fig-1.webp) | <caption> | <page no.> |
| ![fig-2](../assets/<source-slug>/fig-2.webp) | <caption> | <page no.> |

> Reference figures inline in the text above using 
> ![caption](../assets/<source-slug>/fig-N.webp) wherever the figure 
> is directly relevant to a claim.

## Entities
- [[Entity Name]] — one line on why it's relevant here.

## Questions & Gaps
- Anything the source left unanswered or unclear.

## Related
- [[Page Name]] — why it's related.
```

### 5. Update or create entity/concept pages
For each significant entity or concept mentioned:
- If a page already exists in `wiki/`: open it, add a new section or 
  update existing content, note the new source.
- If no page exists: create `wiki/concepts/<slug>.md` or 
  `wiki/entities/<slug>.md` using the format below.

Entity page format:
```
# <Entity Name>

**Type**: person | org | tool | concept  
**Tags**: #entity

## Overview
1–2 sentence description.

## Appearances
- [[Summary Page]] — what role this entity played there.

## Notes
Anything notable: contradictions, evolution over time, open questions.

## Related
- [[Other Entity]]
```

### 6. Update `wiki/index.md`
Append a new row to the index table:

```
| [[<Page Title>]] | #summary | <one-line description> | <YYYY-MM-DD> |
```

If the index table doesn't exist yet, create it with headers:
```
| Page | Tags | Description | Added |
|------|------|-------------|-------|
```

### 7. Append to `wiki/log.md`
Add a timestamped entry at the top of the log:

```
## <YYYY-MM-DD> — Ingested: <Source Title>

- Created: [[<summary page>]]
- Updated: [[Page A]], [[Page B]]
- New entities: [[Entity 1]], [[Entity 2]]
- Images extracted: <N> saved to wiki/assets/<source-slug>/
- Contradictions flagged: <none | description>
```

## Output
Tell the user:
- How many pages were created
- How many existing pages were updated  
- Any contradictions found
- Any gaps or follow-up questions worth exploring
```
