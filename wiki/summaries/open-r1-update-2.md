# Open R1: Update #2

**Source**: `raw/open-r1-update-2/full-article.md` (448 KB), `raw/open-r1-update-2/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

Two weeks into [[Open-R1: A Fully Open Reproduction of DeepSeek-R1]], the headline release is OpenR1-Math-220k: a large-scale math reasoning dataset generated on 512 H100s in collaboration with Numina, built on their new NuminaMath 1.5 problem set. The team prompted DeepSeek-R1 for two answers per problem across 400k NuminaMath 1.5 problems (800k reasoning traces total), using a 16k-token generation limit. Switching the generation backend from vLLM to SGLang nearly doubled throughput, from 15 to 25 generations per hour per H100, enabling 300k solutions per day across the cluster.

Filtering combined Math-Verify (a rule-based math-expression checker, improved to version 0.5.2 during this work to fix parsing edge cases like text-only answers, answer lists, multiple boxed answers, and ordered tuples) with Llama-3.3-70B-Instruct as a secondary judge for otherwise-unverifiable ground truth answers, recovering 28,000 additional correct examples. The final dataset has 220k verified problems, split into a `default` subset (94k, best SFT performance) and an `extended` subset (131k, including simpler `cn_k12` problems that hurt SFT performance slightly). Fine-tuning Qwen2.5-Math-7B-Instruct on the `default` split for 3 epochs (RoPE-extended to 32k context) produced OpenR1-Qwen-7B, which came close to matching DeepSeek-R1-Distill-Qwen-7B on MATH-500/AIME24/AIME25 and beat OpenThinker-7B. A reward-model reranking experiment (Qwen2.5-Math-RM-72B scoring extracted final answers) did not outperform picking a random correct generation.

Community highlights covered in this update include GRPO applied directly to base (non-instruct) models achieving surprising GSM8k gains, Unsloth's memory optimizations enabling 15B-parameter GRPO training on 15GB VRAM, DoRA converging faster than LoRA/full fine-tuning, GRPO reward functions for non-verifiable domains like poetry, the newly released and immediately-leaked-in-part AIME 2025 benchmark, latent-space reasoning research (recurrent models scaling test-time compute without generating "thinking" tokens), and a shift toward small high-quality reasoning datasets (s1K's 1,000 examples, LIMO's 817 examples) as an alternative to DeepSeek's 600k-trace distillation scale. The update also surveys "budget forcing" (extending/truncating CoT length by appending "Wait" or an end-of-thinking token) and Cosine Reward shaping (rewarding shorter CoT for correct answers, longer CoT for wrong ones, with a repetition penalty against reward hacking).

## Key Claims

- OpenR1-Math-220k: 800k R1 reasoning traces generated on 512 H100s running locally, 180k traces/day; SGLang nearly doubled per-GPU throughput vs vLLM (25 vs 15 generations/hour/H100).
- Math-Verify rule-based filtering found at least one correct answer for 55% of the 400k problems; Llama-3.3-70B-Instruct judging recovered 28,000 additional correct examples from previously-rejected samples.
- Final dataset: 220k verified problems (`default` 94k, best SFT performance; `extended` 131k, includes simpler `cn_k12` sources, slightly worse SFT performance).
- OpenR1-Qwen-7B (fine-tuned on `default` split) vs DeepSeek-Distill-Qwen-7B vs OpenThinker-7B: MATH-500 90.6 / 91.6 / 89.6; AIME24 36.7 / 43.3 / 30.0; AIME25 40 / 40 / 33.3.
- Reward-model reranking of multiple correct generations (Qwen2.5-Math-RM-72B) did not improve over selecting one random correct generation in training ablations.
- s1K (1,000 curated examples) and LIMO (817 examples) both showed strong reasoning gains from small, carefully curated SFT sets rather than large-scale distillation.

## Figures

No figures were extracted for this ingest; benchmark tables above are preserved as markdown, and the dataset-composition and CoT-length charts are described inline but not downloaded, per this batch's no-figure-download policy.

## Entities

- [[Hugging Face]] — publishes the update and runs the open-r1 project.
- [[DeepSeek]] — source model (DeepSeek-R1) for the distilled reasoning traces.

## Questions & Gaps

- The post's claim that "the final dataset consists of 220k problems" combining Math-Verify (220k) and the 28k LLM-recovered examples was questioned in the comments as arithmetically ambiguous; the authors clarified Llama verification was only applied to the `default` subset, not merged additively into a single combined total.
- No ablation is given for RM-based reranking using the full reasoning trace (rather than just the extracted final answer), which the authors flag as a possible improvement.

## Related

- [[Open R1: Update #1]] — prior update, covering evaluation reproduction and GRPO landing in TRL.
- [[Open R1: Update #3]] — next update, covering the CodeForces-CoTs dataset and OlympicCoder models.
- [[GRPO]]
- [[Reasoning Models]]
- [[Synthetic Data]]
