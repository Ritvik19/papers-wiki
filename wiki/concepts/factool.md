# FacTool

**Type**: concept  
**Tags**: #concept

## Overview

FacTool (Chern et al. 2023) is a **multi-task, multi-domain factuality detection framework** that extends atomic-fact verification to tasks beyond open-ended text generation. While FActScore focuses on biographical/prose generation verified against Wikipedia, FacTool handles knowledge-based QA, **code generation**, **math problem solving**, and **scientific literature review** — each requiring different external verification tools.

## Motivation

LLM factuality failures are not limited to factual prose: models also hallucinate in code (writing plausible but broken programs), in math (stating incorrect derivations), and in science (fabricating paper references). A single unified fact-checking pipeline should work across all these output types.

## Four-Step Pipeline

```
Step 1 – Claim Extraction
  Prompt an LLM to extract all verifiable claims from the model output.
  Output: a list of atomic, self-contained claims.

Step 2 – Query Generation
  Convert each claim into a list of queries appropriate for external tools.
  Format varies by task:
    → Knowledge QA:   search engine query strings
    → Code:           unit test cases / code snippets to execute
    → Math:           test cases that would reveal incorrect answers
    → Science:        paper titles / author queries for Google Scholar

Step 3 – Tool Querying & Evidence Collection
  Execute queries against appropriate external tools:
    → Knowledge QA:   search engine (e.g., Google)
    → Code:           code interpreter / sandbox execution
    → Math:           code interpreter for verification
    → Science:        Google Scholar

Step 4 – Agreement Verification
  For each claim, assign a binary factuality label (True / False)
  based on the level of support from the collected evidence.
```

## Task-Specific Verification Tools

| Task | Claims | Tool | Verification Method |
|------|--------|------|---------------------|
| Knowledge-based QA | Factual assertions | Search engine | NLI / semantic match with retrieved passages |
| Code generation | Code correctness claims | Code interpreter | Execute unit tests; check pass/fail |
| Math problem solving | Mathematical claims | Code interpreter | Generate + run test cases (not direct claims) |
| Scientific literature | Paper/author existence | Google Scholar | Search for paper titles; check existence |

## Key Differentiator vs. FActScore / SAFE

| Property | FActScore | SAFE | FacTool |
|----------|-----------|------|---------|
| Tasks | Long-form prose | Long-form prose | QA, Code, Math, Science |
| Knowledge source | Wikipedia | Google Search | Task-specific tools |
| Verification | LLM + retrieval | Agentic search | Tool execution (including code) |
| Code verification | ❌ | ❌ | ✅ |
| Math verification | ❌ | ❌ | ✅ (via test cases) |

## Appearances

- [[Extrinsic Hallucinations in LLMs]] — presented as the most versatile factuality detection framework, extending hallucination checking to code and math domains.

## Notes

- For **code**, FacTool generates unit tests rather than checking claims directly — an indirect but executable form of fact-checking that matches how engineers verify code.
- For **math**, test case generation (not symbolic verification) is used — pragmatic but limited for symbolic/algebraic correctness.
- The pipeline is **LLM-heavy**: claim extraction and query generation both require LLM calls, meaning the verifier inherits some of the generator's hallucination risk. This is a known limitation of LLM-as-a-judge approaches.

## Related

- [[FActScore]]
- [[SAFE]]
- [[SelfCheckGPT]]
- [[Extrinsic Hallucination]]
- [[Evaluation and Benchmarks]]
