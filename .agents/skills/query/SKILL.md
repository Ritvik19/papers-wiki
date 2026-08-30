---
name: query
description: Answer a question using only the contents of the wiki folder. Trigger when the user asks a question about their knowledge base, says "what do I know about X", "find pages about X", or "summarize X from the wiki". Do not trigger for ingest or lint tasks.
---

# Query Skill

## Input
A natural language question or topic from the user.

## Steps

### 1. Orient via the index
Read `wiki/index.md` first. Scan the descriptions to identify which pages 
are likely relevant. Do not guess — only proceed with pages that are 
plausibly related to the query.

### 2. Read relevant pages
Open each candidate page. Prioritize:
- Summary pages that directly cover the topic
- Concept/entity pages for key terms in the question
- Log entries if the question is about what was recently added

Read the `## Related` sections to discover additional pages worth checking. 
Follow at most 2 hops of links — don't spiral into the whole wiki.

### Step 2b. Collect relevant figures
While reading each relevant page, scan for image references in:
- The `## Figures` table
- Any inline `![caption](path)` tags in the body

For each image found, note:
- The file path
- Its caption
- Which claim or section it was attached to

Filter to only figures that are directly relevant to the query.
If a page has 6 figures but only 2 relate to the question, 
include only those 2. Do not dump every figure from every page.

### 3. Synthesize the answer
Write the answer in plain prose. Rules:
- Only use information found in `wiki/`. Do not use outside knowledge 
  unless the user explicitly asks you to supplement.
- Cite every claim: "According to [[Page Name]], ..."
- If two pages contradict each other, surface the contradiction explicitly 
  rather than silently picking one.
- If the wiki doesn't have enough information, say so clearly.

### 4. Surface gaps (optional but preferred)
After answering, note if the query revealed:
- A topic with no dedicated page yet
- A page that seems outdated or thin
- A connection between pages that isn't cross-linked yet

Offer to fix any of these: "Want me to create a concept page for X?" 
or "I noticed [[Page A]] and [[Page B]] aren't linked — should I add that?"

## Output format

```
## Output format

**Answer**
<prose answer with [[citations]] and inline figures where relevant>

Inline figures go immediately after the claim they support:
"The encoder uses stacked self-attention layers [[Summary Page]].
![Encoder architecture](../assets/paper/fig-2.png)
*Fig 2: Encoder stack from the original paper*"

**Sources consulted**
- [[Page 1]] — what it contributed
- [[Page 2]] — what it contributed

**Figures referenced**
| Figure | From | Caption |
|--------|------|---------|
| ![fig-1](../assets/paper/fig-1.png) | [[Page 1]] | <caption> |

**Gaps found** (if any)
- <description of missing or thin coverage>
```

## What not to do
- Do not modify any wiki pages during a query
- Do not hallucinate citations — if a page doesn't exist, say so
- Do not answer from memory if the wiki contradicts your training data; 

## Special case: figure queries
If the user asks to "show", "find", or "list" figures, diagrams, 
charts, or images about a topic:
1. Search wiki/assets/ for relevant subfolders
2. Read the ## Figures table on matching summary pages
3. Return a gallery-style response:

**Figures matching: <topic>**

![caption](../assets/paper/fig-1.png)
*From [[Summary Page]], page 4 — <caption>*

![caption](../assets/paper2/fig-3.png)  
*From [[Summary Page 2]], page 11 — <caption>*