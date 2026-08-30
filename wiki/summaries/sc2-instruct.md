# StarCoder2-Instruct: Fully Transparent and Permissive Self-Alignment for Code Generation

**Source**: `raw/sc2-instruct/full-article.html` (190 KB), `raw/sc2-instruct/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

A BigCode post introducing StarCoder2-15B-Instruct-v0.1, described as the first entirely self-aligned code LLM: no human annotations, no distilled data from proprietary teacher LLMs (like GPT-4), just [[StarCoder2 and The Stack v2|StarCoder2]]-15B generating and validating its own instruction-tuning data. The pipeline (branded Self-OSS-Instruct / SelfCodeAlign) runs in three stages. First, seed functions are mined from The Stack v1: Python functions with docstrings are filtered by a Pyright type-checker (removing static errors), decontaminated against benchmark solutions/prompts via exact string match, quality-filtered by using StarCoder2-15B itself as a judge (yes/no on docstring quality via 7-shot prompting), and near-deduplicated with MinHash/LSH, reducing 5M candidate functions to 250K seeds.

Second, instructions are generated via in-context learning with 16 few-shot examples: StarCoder2-15B first extracts "code concepts" (e.g., pattern matching, data type conversion) present in each seed function, then generates a coding task incorporating those concepts, yielding 238K instructions. Third, responses are self-validated rather than distilled: for each instruction, the model samples 10 candidate (natural-language response, test) pairs at temperature 0.7, executes the generated test in a sandbox, and keeps only responses that pass: 2.4M total generations, 500K passing, deduplicated down to a final 50K-instruction SFT dataset with one randomly-selected passing response each.

## Key Claims

- StarCoder2-15B-Instruct scores 72.6 on HumanEval, surpassing CodeLlama-70B-Instruct's 72.0 despite StarCoder2-15B-Instruct being under a quarter of the parameter count.
- On LiveCodeBench, the self-aligned model outperforms OpenCodeInterpreter-SC2-15B (the same base model fine-tuned on GPT-3.5/4-distilled data). The post frames this as evidence a model can learn more effectively from data within its own output distribution than from a distribution shifted by a teacher model.
- On EvalPlus, StarCoder2-15B-Instruct is reported as the top-performing permissive LLM at its scale, outperforming larger models including Grok-1, Command-R+, and DBRX, while closely matching Snowflake Arctic (480B) and Mixtral-8x22B-Instruct.
- It is described as the first code LLM with a fully transparent, permissive pipeline to exceed a 70 HumanEval score, and drastically outperforms OctoCoder, the prior state of the art for transparent permissive pipelines.
- Data-pipeline yield: 5M candidate Python functions -> 250K filtered seeds -> 238K generated instructions -> 2.4M candidate responses -> 500K execution-verified -> 50K final deduplicated SFT examples.
- Released fully open: the instruction-tuned model, the self-alignment pipeline code, and the generated instruction-tuning dataset are all published (`bigcode/self-oss-instruct-sc2-exec-filter-50k`).

## Figures

No figures were extracted for this ingest; benchmark comparisons against CodeLlama-70B-Instruct, Grok-1, DBRX, Snowflake Arctic, Mixtral-8x22B, Gemini Pro, and Mistral Large are preserved as prose claims above (the source post presents these as narrative rather than a single table), per this batch's no-figure-download policy.

## Entities

- [[Hugging Face]] — co-hosts BigCode and the model/dataset release.

## Questions & Gaps

- The post does not give exact numeric scores for every comparison model mentioned (Gemini Pro, Mistral Large, Snowflake Arctic); several claims ("surpassing," "comparable to") are qualitative in the source text.
- The citation for the full methodology (SelfCodeAlign, arXiv:2410.24198) postdates this blog post's stated publication date (April 2024) by several months, suggesting the paper was published after the initial release and later attached as the canonical citation.
- No discussion of failure modes or limitations of self-validated responses (e.g., a model could generate a weak self-test that a subtly wrong solution still passes). The sandbox execution is presented as a sufficient quality bar.

## Related

- [[StarCoder2 and The Stack v2]] — the base model and pretraining dataset this instruction-tuned release builds directly on.
- [[Papers Explained 128 - WizardCoder]] and [[Papers Explained 133 - Rho-1]] — other code/data-quality-focused training recipes in the same era.
- [[Hugging Face]]
- [[Code Models]]
- [[Synthetic Data]]
