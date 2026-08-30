---
name: lint
description: Audit the wiki for structural problems and inconsistencies. Trigger when the user says "lint the wiki", "check the wiki", "clean up the wiki", or "audit the wiki". Do not trigger for ingesting or querying.
---

# Lint Skill

## Input
No specific input needed. Operates on the entire `wiki/` directory.

## Steps

Run all checks below in order. Collect all findings before making any edits. 
Then present a summary to the user and ask for approval before writing changes.

---

### Check 1 — Broken internal links
Scan every `.md` file in `wiki/` for `[[Page Name]]` references.
For each reference, check whether a file with that name exists in `wiki/`.
Flag every link that points to a non-existent page.

Report format:
```
Broken links:
- [[Missing Page]] referenced in: wiki/concepts/foo.md, wiki/summaries/bar.md
```

Fix (with approval): either create stub pages for the missing targets, 
or remove the broken links — ask the user which they prefer.

---

### Check 2 — Index completeness
Read `wiki/index.md`. Get the list of all pages it references.
Then list every `.md` file in `wiki/` recursively.
Flag any file that exists on disk but is missing from the index.
Flag any index entry that points to a non-existent file.

Report format:
```
Missing from index: wiki/concepts/new-thing.md
Dead index entries: [[Old Page]] (file not found)
```

Fix (with approval): update `wiki/index.md` to add missing entries 
and remove dead ones.

---

### Check 3 — Pages missing required sections
Every wiki page should have: a title (H1), a `## Summary` or `## Overview` 
section, and a `## Related` section.

Scan all pages and flag any that are missing one or more of these.

Report format:
```
Incomplete pages:
- wiki/entities/foo.md — missing ## Related
- wiki/summaries/bar.md — missing ## Summary
```

Fix (with approval): add placeholder sections to incomplete pages.

---

### Check 4 — Contradiction detection
Read all pages. Look for explicit contradiction markers such as:
- "contradicts [[X]]"
- "conflicts with"
- "disagrees with"
- Claims that appear in multiple pages but with different values 
  (dates, numbers, names)

This is a best-effort scan, not exhaustive. Flag what you find.

Report format:
```
Potential contradictions:
- [[Page A]] says X; [[Page B]] says Y — same topic, different claims
```

Do not auto-resolve contradictions. Present them to the user for review.

---

### Check 5 — Orphaned pages
Find any page in `wiki/` that is not referenced by any other page 
(not in the index, not linked from any `## Related` section).

Report format:
```
Orphaned pages (no inbound links):
- wiki/concepts/forgotten-topic.md
```

Fix (with approval): suggest which existing pages should link to the 
orphan, or ask if it should be deleted.

---

### Check 6 — Log freshness
Read `wiki/log.md`. Check the most recent entry date.
If the most recent entry is older than 30 days, flag it as a reminder 
that the wiki may not reflect recent activity.

Report format:
```
Log last updated: <date> (<N> days ago)
Consider ingesting new sources if knowledge has accumulated.
```

---

### Check 7 — Image integrity
This check has two parts.

#### Part A — Broken image references
Scan every `.md` file in `wiki/` for inline image tags `![...](...)` 
and `## Figures` table entries.
For each image path referenced, verify the file exists in `wiki/assets/`.
Flag any reference pointing to a missing file.

Report format:
```
Broken image references:
- wiki/summaries/foo.md → ../assets/foo/fig-3.png (file not found)
```

Fix (with approval): remove the broken reference and add a note 
"[image missing — re-run $reingest raw/<source> to restore]"

#### Part B — Orphaned assets
List every file under `wiki/assets/` recursively.
For each file, check whether any `.md` file in `wiki/`, any file in
`artifacts/`, or any `raw/<slug>/full-article.html` references it.
Flag files that are not referenced anywhere.
Also flag any `raw/<slug>/images/` directories as storage violations (figures
belong only in `wiki/assets/`).

Report format:
```
Orphaned assets (not referenced by any page):
- wiki/assets/old-paper/fig-2.png
- wiki/assets/old-paper/fig-4.png
```

Fix (with approval): delete orphaned asset files. 
If an entire `wiki/assets/<slug>/` folder is orphaned, 
check whether a corresponding summary page exists before deleting — 
the page may exist but simply be missing its ## Figures section, 
in which case flag it under Check 3 instead of deleting the assets.

#### Part C — Summaries with no figures despite having a raw source
For every page in `wiki/summaries/`, check whether:
1. A corresponding file exists in `raw/`
2. That raw file is a PDF, DOCX, or PPTX (types likely to contain images)
3. No `wiki/assets/<slug>/` folder exists for it

Flag these as candidates for re-ingestion.

Report format:
```
Summaries likely missing figures (raw source is image-bearing format):
- wiki/summaries/paper.md ← raw/paper.pdf (no assets folder found)
  Suggestion: run $reingest raw/paper.pdf
```

Do not auto-fix this. Present to the user for manual review.

---

## Output

Present a single report before making any changes:

```
Wiki Lint Report — <YYYY-MM-DD>
================================
Pages scanned: <N>
Assets scanned: <N>
Issues found: <N>

[Check 1] Broken links: <N found>
  ...details...

[Check 2] Index completeness: <N found>
  ...details...

[Check 3] Incomplete pages: <N found>
  ...details...

[Check 4] Contradictions: <N found>
  ...details...

[Check 5] Orphaned pages: <N found>
  ...details...

[Check 6] Log freshness:
  ...details...

[Check 7] Image integrity:
  Broken image references: <N found>
    ...details...
  Orphaned assets: <N found>
    ...details...
  Summaries missing figures: <N found>
    ...details...

---
Ready to apply fixes for checks 1, 2, 3, 5, and 7A/7B.
Checks 4 and 7C require your review — no auto-fix.
Proceed? (yes / pick specific checks / no)
```

Wait for user confirmation before writing any file changes.