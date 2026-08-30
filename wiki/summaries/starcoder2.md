# StarCoder2 and The Stack v2

**Source**: `raw/starcoder2/full-article.html` (209 KB), `raw/starcoder2/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

BigCode's launch post for StarCoder2, an open code LLM family in 3B, 7B, and 15B sizes, trained on The Stack v2, a new, much larger permissively-licensed code dataset derived from the Software Heritage archive. BigCode is a collaboration jointly led by Hugging Face and ServiceNow; each StarCoder2 size was trained by a different partner: the 3B model by ServiceNow, the 7B model by Hugging Face, and the flagship 15B model by NVIDIA (using NeMo on NVIDIA-accelerated infrastructure). All three sizes share the same architectural recipe: Grouped Query Attention, a 16,384-token context window with 4,096-token sliding-window attention, and Fill-in-the-Middle (FIM) training.

The Stack v2 itself is the dataset headline, roughly 10x the size of The Stack v1 across every measure, with improved language/license detection and repository-grouped organization that lets models train with cross-file repository context:

| | The Stack v1 | The Stack v2 |
|---|---|---|
| Full | 6.4TB | 67.5TB |
| Deduplicated | 2.9TB | 32.1TB |
| Training dataset | ~200B tokens | ~900B tokens |

StarCoder2-15B trains on 4T+ tokens across 600+ programming languages; the 3B and 7B models train on 3T+ and 3.5T+ tokens respectively across 17 languages. The post reports StarCoder2-15B as best-in-class for its size, matching 33B+ models on many evaluations, and StarCoder2-3B as matching the performance of the original StarCoder-15B at a fifth of the size.

## Key Claims

- The Stack v2 is roughly 10x The Stack v1 by both raw size (67.5 TB vs. 6.4 TB) and training-token count (~900B vs. ~200B tokens).
- StarCoder2-15B trains on 4T+ tokens / 600+ languages; StarCoder2-3B and -7B train on 3T+/3.5T+ tokens across 17 languages each.
- StarCoder2-15B reported to match the evaluation performance of 33B+ parameter models; StarCoder2-3B reported to match the original StarCoder-15B.
- Shared architecture across all three sizes: Grouped Query Attention, 16,384-token context, 4,096-token sliding-window attention, Fill-in-the-Middle objective.
- Released under the BigCode OpenRAIL-M v1 license agreement, with accompanying tooling: a full-text search tool over the pretraining dataset and a "membership test" tool to check whether a given code snippet was present in training data.

## Figures

No figures were extracted for this ingest, per this batch's no-figure-download policy; the post's evaluation bar charts (StarCoder2-15B vs. 33B+ models; StarCoder2-3B vs. StarCoder-15B) are referenced above but not downloaded.

## Entities

- [[Hugging Face]] — co-leads BigCode; trained the 7B model.
- [[NVIDIA]] — trained the 15B model using NeMo.
- [[ServiceNow]] — co-leads BigCode; trained the 3B model.

## Questions & Gaps

- The post itself gives no further detail on ServiceNow's training setup for the 3B model beyond attribution; see [[Apriel-H1: The Surprising Key to Distilling Efficient Reasoning Models]] and other ServiceNow items from the reasoning/RL batch for more on that lab's work.
- No specific benchmark numbers (HumanEval, MBPP, etc.) are given in this post itself; those appear in the companion [[StarCoder2-Instruct: Fully Transparent and Permissive Self-Alignment for Code Generation]] post and the linked technical paper, not archived here.
- The post links to a "Big Code Models Leaderboard" Space and a "StarCoder2 Search" Space for exploring training-data membership, neither of which was captured beyond the reference.

## Related

- [[StarCoder2-Instruct: Fully Transparent and Permissive Self-Alignment for Code Generation]] — the instruction-tuned follow-up built directly on the StarCoder2-15B base model released here.
- [[Paper Explained 144 - Granite Code Models]] — contemporaneous IBM code-model family; comparable era and target use case.
- [[Papers Explained 62 - Code Llama]] — comparable-era code-specialized LLM family from Meta.
- [[Hugging Face]]
- [[NVIDIA]]
- [[Code Models]]
- [[Large Language Models]]
