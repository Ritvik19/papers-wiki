# Open R1: Update #3

**Source**: `raw/open-r1-update-3/full-article.md` (400 KB), `raw/open-r1-update-3/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

Third [[Open-R1: A Fully Open Reproduction of DeepSeek-R1]] update, shifting focus from math to competitive-programming (code) reasoning. The team released `open-r1/codeforces`, a dataset of 10k+ CodeForces problems (roughly 3k not present in DeepMind's earlier CodeContests dataset), with editorials for ~60% of problems and three official solutions each; and `open-r1/codeforces-cots`, close to 100k DeepSeek-R1-generated chain-of-thought solutions in C++ and Python for those problems. Fine-tuning Qwen2.5-Coder-Instruct 7B and 32B on this dataset produced OlympicCoder-7B and OlympicCoder-32B.

A key motivating finding was a "code verifiability crisis": CodeForces caps publicly displayed test cases at ~500 characters, so datasets built only from those test cases (including DeepMind's CodeContests) systematically miss the harder tests used for real judging; 7 R1-generated solutions that passed all public tests failed when actually submitted to CodeForces. This pushed the team toward the International Olympiad in Informatics (IOI), whose full test sets are released under a permissive CC-BY license. They processed IOI 2020-2024 problems into per-subtask prompts, built custom grading infrastructure (`huggingface/ioi`), and evaluated 40+ leading reasoning models on IOI 2024 under real contest submission-limit conditions (50 submissions per problem, using a round-robin submission strategy similar to OpenAI's o1-IOI evaluation). OlympicCoder-32B outperformed o1-mini and DeepSeek-R1 (the model it was distilled from) under the 50-submission setting, though no model reached the medal threshold.

The post also documents five SFT lessons from training on R1 traces: (1) sample packing hurts performance on long reasoning traces, since answers can get split across chunk boundaries; (2) a larger learning rate (4e-5 vs the usual 2e-5) gave nearly 10 points on LiveCodeBench per doubling; (3) including problem editorials alongside R1's generated solutions did not help, and slightly hurt; (4) prefilling the assistant response with `<think>` is necessary to reliably trigger long CoT on out-of-domain queries, since otherwise the model reverts to base-instruct behavior outside its training distribution; (5) 8-bit optimizers (`paged_adamw_8bit` + FSDP) were needed to scale training context to 22,528 tokens on the 32B model, since `transformers`/`trl` lacked context parallelism at the time. Separately, TRL's GRPO trainer gained generation reuse (reusing a batch of rollouts across multiple gradient steps, denoted mu, with 2-4 recommended) and per-reward-function weighting.

## Key Claims

- `open-r1/codeforces`: 10k+ problems, ~3k not in DeepMind's CodeContests; editorials for ~60% of problems, 3 official solutions each.
- `open-r1/codeforces-cots`: ~100k DeepSeek-R1-generated C++/Python solutions across those problems.
- CodeForces displays only ~500-character test cases publicly; 7 sample R1 solutions that passed all public tests failed every full test-set submission on the real platform.
- OlympicCoder-32B outperforms o1-mini and DeepSeek-R1 (its own distillation source) on IOI 2024 under the 50-submission-limit contest setting; no evaluated model reached the medal (50th percentile) threshold.
- SFT lessons: sample packing hurts reasoning-trace training; 4e-5 learning rate beats the usual 2e-5 by ~10 points/doubling on LiveCodeBench; including editorials does not help; `<think>`-prefill is required to reliably trigger long CoT outside the training distribution; 8-bit optimizers were needed to reach 22,528-token context on the 32B model without OOM.
- Best training recipe: Qwen2.5 Coder Instruct 7B/32B, 10 epochs, effective batch size 128, LR 4e-5, cosine decay to 10% of peak, context 32,768 (7B) / 22,528 (32B).
- TRL GRPO gained generation reuse (mu, recommended 2-4) and configurable per-reward-function weighting (`reward_weights`).

## Figures

No figures were extracted for this ingest; the IOI medal-threshold chart, packing-vs-no-packing ablation, and learning-rate ablation are described inline but not downloaded, per this batch's no-figure-download policy.

## Entities

- [[Hugging Face]] — publishes the update and runs the open-r1 project.
- [[DeepSeek]] — source model (DeepSeek-R1) for the distilled reasoning traces.

## Questions & Gaps

- The post notes Python solutions were not blended into training (only C++), and speculates this would boost performance further, but doesn't test it.
- `transformers`/`trl` context-parallelism support is flagged as missing infrastructure rather than solved; the 8-bit-optimizer workaround still leaves ~9% of CodeForces-CoTs traces truncated at 32B scale.

## Related

- [[Open R1: Update #2]] — prior update, covering the OpenR1-Math-220k dataset.
- [[Open R1: Update #4]] — next update, covering the DeepSeek-V3-0324 model release.
- [[GRPO]]
- [[Reasoning Models]]
- [[Code Models]]
