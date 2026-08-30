---
name: query-interactive
description: Build a source-grounded interactive HTML/CSS/JS teaching artifact from the wiki, saved under artifacts/. Trigger when the user asks for a visual, interactive, diagram-heavy, quiz-backed, or learning-guide style explanation from the wiki; wants an HTML mini-site or explainer; or says to save to artifacts/. Do not trigger for normal wiki Q&A (use query), ingest, or lint.
---

# Query Interactive Skill

Answer from `wiki/` only, following the same integrity rules as the `query` skill (`.agents/skills/query/SKILL.md`), but deliver the result as a **static interactive teaching artifact** under `artifacts/` instead of, or in addition to, long chat prose.

The artifact should help the reader build a mental model, not just display notes. Use source-grounded explanations, diagrams, figures, snippets, mental-model callouts, warnings, and lightweight interactions to teach what the wiki actually says.

## Input

A natural language question or topic, plus any UI preferences the user states (e.g. dark mode, focus on one paper).

## Artifact Modes

Choose one mode before writing. State the mode briefly in `meta.json` and in the final chat reply.

### Focused explainer

Use for ordinary visual questions with a bounded topic. The artifact should answer the question directly with 3-6 sections, diagrams or figures, a source list, and any contradictions or gaps.

### Learning guide

Use when the user asks for a teaching guide, walkthrough, quiz, or broad conceptual explanation. The artifact should include:

- A plain-language "why this matters" section
- A big-picture map of the topic
- Concept cards for the key ideas
- Mental-model callouts
- Warning or key-insight boxes
- Source-labeled snippets or quotes
- A short quiz with answer explanations tied to wiki pages

### Large topic mode

Use when the topic spans too many wiki pages for a reliable single artifact. Do not pretend to cover everything deeply. Instead:

- Inventory the relevant pages and clusters
- Prioritize the most central pages and flows
- Teach the highest-priority concepts first
- Include an explicit "Coverage gaps" or "What is not covered yet" section
- Record pending sections or pages in `meta.json`

## Steps

### 1. Orient via the index

Read `wiki/index.md` first. Scan the descriptions to identify which pages are likely relevant. Do not guess; only proceed with pages that are plausibly related to the query.

### 2. Read relevant pages

Open each candidate page. Prioritize:

- Summary pages that directly cover the topic
- Concept/entity pages for key terms in the question
- Log entries if the question is about what was recently added

Read the `## Related` sections to discover additional pages worth checking. Follow at most **2 hops** of links; do not spiral into the whole wiki.

While reading, maintain a source inventory:

- Page title and path
- One-line summary of what the page contributes
- Key claims that may appear in the artifact
- Relevant concepts, mechanisms, or flows
- Figures and captions
- Contradictions or tensions with other pages
- Gaps, thin coverage, or missing cross-links

### 2b. Collect relevant figures

While reading each relevant page, scan for image references in:

- The `## Figures` table
- Any inline `![caption](path)` tags in the body

For each image found, note:

- The file path (as stored in the wiki, usually relative to `wiki/`, e.g. `assets/.../fig-1.png`)
- Its caption
- Which claim or section it supports

**Filter** to only figures that are directly relevant to the query. If a page has many figures but only a few apply, include only those; do not dump every figure from every page.

### 2c. Validate figure fidelity (required)

Before wiring images into the artifact, verify each candidate figure actually matches its caption and intended claim:

- Open the image file itself (not just markdown captions).
- Check whether it is a true diagram/chart crop vs a full PDF page capture.
- Check for filename-caption mismatches (e.g., file labeled as "verification example" but showing a benchmark table page).
- If a mismatch exists, **do not** blindly use the wiki filename as canonical for the visual claim. Keep textual claims grounded in wiki text, but source the visual from the correct region of the source paper (see 4c).

### 3. Extract teaching structure

Before writing HTML, identify:

- The core question the artifact answers
- The "why": what problem, claim, or distinction matters
- The 4-8 key concepts the reader must understand
- The most important mechanism, argument chain, or end-to-end flow
- Decision points, boundaries, limitations, or scope caveats
- Common misconceptions the artifact should prevent
- Contradictions or tensions between pages, if any

Then outline sections that mirror a rigorous answer:

1. Overview / question restatement
2. Why this matters
3. Big-picture map
4. Key mechanisms and claims, grouped by subtopic
5. Critical flow or comparison
6. Contradictions, tensions, or limits, if any
7. Sources, figures, and gaps

For learning-guide mode, include a quiz section after the main teaching content.

**Diagrams:** Plan at least one visual per major section:

- Prefer existing wiki figures via `<img src="...">` (see paths below).
- Otherwise add inline SVG, simple CSS diagrams, or ASCII-in-`<pre>` only when it clarifies structure and remains grounded in wiki text.
- Do not invent quantitative results or diagrams that the wiki does not support.

### 3b. Required teaching components

Use these components as needed. Learning-guide mode should include all of them; focused explainers should include the ones that clarify the answer.

#### Concept cards

```html
<div class="concept-card">
  <h4>Concept name</h4>
  <p>Plain-language explanation tied to <code>[[Wiki Page]]</code>.</p>
</div>
```

#### Mental-model callouts

```html
<div class="mental-model">
  <strong>Mental model:</strong> A useful analogy that builds intuition without adding unsupported claims.
</div>
```

#### Warning / key-insight boxes

```html
<div class="warning-box">
  <strong>Key insight:</strong> A non-obvious limitation, distinction, or misconception from the wiki.
</div>
```

#### Source-labeled snippets or quotes

For code-like content, wiki excerpts, paper claims, or definitions, include a visible source label. Keep snippets short and real.

```html
<div class="code-label">wiki/Page Name.md - section or claim</div>
<blockquote>
  Short source-grounded excerpt or paraphrase, with the page name visible nearby.
</blockquote>
```

#### Flow diagrams

Use CSS or inline SVG. Keep labels short and grounded in the wiki.

```html
<div class="flow-diagram">
  <span class="flow-accent">Step 1</span> -> Description<br>
  <span class="flow-accent">Step 2</span> -> Description<br>
</div>
```

#### Quiz for learning guides

Use 5-10 multiple-choice questions. Each question should test understanding, not recall alone.

Question mix:

- Structure: where a concept lives in the wiki
- Logic: what a mechanism or claim implies
- Boundary: what the wiki says is out of scope or limited
- Comparison: how two regimes, papers, or concepts differ
- Application: which pages/concepts to inspect first for a new question

Each answer must reveal an explanation that cites the relevant wiki page. If using JavaScript, store results in localStorage with a key scoped to the artifact, for example `papers-wiki-artifact:<slug>:quiz`.

```html
<div class="quiz-card" data-quiz="q1">
  <h4>Q1 - Concept</h4>
  <p class="question">Question text?</p>
  <ul class="quiz-options">
    <li onclick="selectAnswer(this,'q1',false)">Wrong answer</li>
    <li onclick="selectAnswer(this,'q1',true)">Correct answer</li>
    <li onclick="selectAnswer(this,'q1',false)">Wrong answer</li>
  </ul>
  <div class="quiz-explanation" id="q1-exp">
    Explanation grounded in <code>[[Wiki Page]]</code>.
  </div>
</div>
```

### 3c. Default visual style ("Google Wikipedia")

Unless the user asks for a different style, render artifacts with a "Google-Wikipedia" look:

- Clean light theme, white content surfaces, subtle gray borders.
- Sticky top header with brand + search bar.
- Left contents rail, central article body, optional right infobox rail on large screens.
- Serif-style article headings (Wikipedia-like), sans-serif body (Google-like UI feel).
- Minimal shadows; prioritize borders, spacing, and readability over decorative effects.
- Keep interactions simple and native (tabs, details, small buttons), no framework dependency.

This style should be reusable across artifacts so outputs feel consistent.

### 4. Build the files

Create a directory:

`artifacts/<YYYY-MM-DD>-<short-slug>/`

Use today's date and a short kebab-case slug derived from the topic.

Write:

- **`index.html`** (required): semantic HTML, navigable sections, skip link, in-page TOC, `<figure>` + `<figcaption>`, meaningful `alt` text from captions, and source labels.
- **`meta.json`** (required): machine-readable summary of query, mode, sources, figures, gaps, and verification notes.
- **`styles.css`** and **`app.js`** (optional): vanilla CSS/JS only. Prefer inline CSS/JS for single-file portability when the artifact is small.
- **`figures/`** (optional): local crops or generated images used by the artifact.
- **`build_figures.py`** (optional): deterministic regeneration script when local crops are created.

**Default scaffold:** Start by copying the repo scaffold:

`artifacts/_scaffold/papers-wiki/` -> `artifacts/<YYYY-MM-DD>-<short-slug>/`

Then replace placeholders in `index.html`, add teaching components, and add `figures/` assets when needed.

### 4b. Image paths

Pages live under `artifacts/<slug>/`. Wiki assets live under `wiki/assets/`. From `index.html`, reference figures as:

```text
../../wiki/assets/<rest-of-path>
```

Example: wiki markdown `assets/paper-explained-144-granite-code-models/fig-2.png` -> `../../wiki/assets/paper-explained-144-granite-code-models/fig-2.png`.

### 4c. When figures are full-page captures or mislabeled

If the wiki image is a full PDF page (or appears mismatched with its caption), create local cropped assets under:

`artifacts/<YYYY-MM-DD>-<short-slug>/figures/`

Preferred workflow:

1. Locate the source PDF from wiki `## Source` (`raw/...pdf`).
2. Use PDF-native clipping (preferred) to export accurate crops:
   - Use PyMuPDF (`fitz`) and clip by figure/image bounding boxes.
   - For multi-panel figures, crop exact panels (e.g., top-right / bottom-left) only when they truly correspond to the cited claim.
3. Save deterministic filenames in `figures/` and reference them from `index.html` via:
   - `figures/<name>.png`
4. Optionally add a small `build_figures.py` script in the artifact folder so crops can be regenerated.

When this fallback is used, document it briefly in the artifact (footer or sources section), including that visuals came from PDF crops rather than raw wiki PNG filenames.

### 4d. Required metadata

Write **`meta.json`** in the same folder:

```json
{
  "query": "<user question>",
  "created": "<ISO-8601 date>",
  "mode": "focused-explainer|learning-guide|large-topic",
  "sources": [
    {
      "title": "<wiki page title>",
      "path": "wiki/<Page Name>.md",
      "contribution": "<what this page contributed>"
    }
  ],
  "figures": [
    {
      "path": "../../wiki/assets/...",
      "caption": "<caption>",
      "verified": true,
      "note": "<crop or fidelity note>"
    }
  ],
  "concepts": ["<concept>", "..."],
  "flows": ["<flow or argument chain>", "..."],
  "quiz": {
    "included": false,
    "questionCount": 0,
    "localStorageKey": null
  },
  "gaps": ["<missing or thin coverage>", "..."],
  "largeTopic": {
    "enabled": false,
    "pendingPages": [],
    "pendingSections": []
  }
}
```

### 4e. Writing and verification strategy

- Use file-edit/write tools for generated files when practical.
- If using a terminal, avoid fragile huge shell heredocs for full HTML documents. Prefer copying the scaffold, editing files directly, or using a small script with safe chunks.
- Verify every generated HTML file exists, has non-zero size, starts with `<!DOCTYPE html>`, and ends with `</html>`.
- Verify `meta.json` is valid JSON.
- Ensure the artifact works from `file://` without required CDN scripts.
- After verification, optionally open `artifacts/<YYYY-MM-DD>-<short-slug>/index.html` with the OS default browser when the user asked for an artifact to be created.

### 5. Content rules (wiki-only)

- Only use information found in `wiki/`. Do not use outside knowledge unless the user explicitly asks you to supplement.
- Tie sections to sources: show page titles in a sidebar, footer, source cards, or source labels. `[[Page Name]]` links are not required inside HTML, but page names must be visible.
- Every substantive claim should be traceable to at least one wiki page.
- If two pages contradict each other, include a dedicated **Contradictions** section. Do not hide the tension.
- If the wiki lacks enough information, state that clearly in the artifact and in the chat reply.
- Do not modify any files under `wiki/` during this workflow.

### 6. Quality checklist

Before replying, check:

- The artifact mode is recorded in `meta.json`.
- `index.html` has a clear title, overview, navigation, source list, and gaps section when gaps exist.
- Learning-guide mode includes concept cards, mental models, warnings, source-labeled snippets or quotes, and a quiz.
- Large topic mode includes visible uncovered or pending areas.
- Every claim is grounded in `wiki/` pages.
- Figures are verified, or replaced with accurate local crops.
- Figure paths work from the generated `index.html`.
- `meta.json` lists sources, figures, concepts, flows, gaps, and quiz metadata.
- The artifact has no required framework or CDN dependency.
- The artifact opens from `file://`.

### 7. Chat reply

After writing files, reply briefly with:

- **Path** to open: `artifacts/<YYYY-MM-DD>-<short-slug>/index.html`
- **Mode used**: focused explainer, learning guide, or large topic
- **One-paragraph summary** of what the artifact covers
- **Sources consulted** (wiki page titles)
- **Figures used** (short list)
- **Gaps found** (optional): missing pages, thin coverage, missing cross-links, or intentionally uncovered large-topic areas

## What not to do

- Do not modify any files under `wiki/` during this workflow.
- Do not hallucinate citations, snippets, figures, quiz answers, or relationships.
- Do not rely on CDNs for core layout or diagrams by default (inline SVG / local CSS preferred).
- Do not assume a figure filename is correct without checking the actual image content.
- Do not create a project-wide `cognitive-coverage/` system unless the user explicitly asks for that. This skill's default output remains `artifacts/<YYYY-MM-DD>-<short-slug>/`.
- Do not bury contradictions or weak evidence in metadata only. Surface them in the artifact.

## Relationship to query

- Use **`query`** for normal answers in chat.
- Use **`query-interactive`** when the user wants a **saved, diagram-heavy, interactive** explainer under `artifacts/`.
