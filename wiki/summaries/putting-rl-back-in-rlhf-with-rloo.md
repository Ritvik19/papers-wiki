# Putting RL Back in RLHF

**Source**: `raw/putting-rl-back-in-rlhf-with-rloo/full-article.md` (172 KB), `raw/putting-rl-back-in-rlhf-with-rloo/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

Hugging Face introduces the RLOO (REINFORCE Leave-One-Out) Trainer in TRL, based on Cohere's Ahmadian et al. (2024) paper revisiting RLHF fundamentals. RLOO is positioned as a simpler, cheaper alternative to PPO for online RLHF: PPO needs four models in memory (policy, reference policy, reward model, value model), while RLOO drops the value model entirely, needing only three. This cuts GPU memory by roughly 50-70% depending on model size and makes RLOO run 2x faster than PPO at 1B parameters and up to 3x faster at 6.9B, while matching or beating PPO on response win rate (judged by GPT-4) and consistently beating offline methods like DPO.

Mechanically, RLOO differs from PPO in two ways. First, it treats the entire generated completion as a single action rather than modeling each token as a separate action; since only the end-of-sequence token typically receives a true (sparse) reward under PPO's per-token formulation, RLOO instead attributes that reward to the whole completion. Second, it uses the plain REINFORCE loss (log-prob of the action times (reward minus baseline)) instead of PPO's clipped-ratio objective with a learned value baseline from Generalized Advantage Estimation. The baseline itself is computed cheaply and without any value network: for K sampled completions per prompt, each completion's baseline is the mean reward of the other K-1 completions for the same prompt (leave-one-out), which the post shows can be vectorized as `baseline = (rewards.sum(0) - rewards) / (K - 1)`. The post also demonstrates, with a minimal PyTorch example, that REINFORCE's loss is mathematically a special case of the (unclipped) PPO loss, since the log-probability term is implicitly present in PPO's importance-sampling ratio even though it isn't written explicitly.

Validating the TRL implementation on Pythia 1B and 6.9B (using SFT/reward models from prior TL;DR summarization work, evaluated with vLLM and GPT-4-as-judge), the 6.9B RLOO checkpoint reached a 78.7% preferred rate at k=2, exceeding the original paper's own best-reported numbers (77.9% at k=4, 74.2% at k=2); the 1B checkpoint reached a 40.1% win rate versus the SFT checkpoint's 21.3%. The post also surfaces a numerical stability caveat: response log-probs computed during generation differ slightly from log-probs recomputed during the training forward pass under `bf16` precision, and this discrepancy is much more damaging to RLOO than to PPO, since RLOO's importance ratio is computed over the summed log-probs of the entire completion rather than per-token. In practice, PPO's clipping nulled gradients for about 3% of batch data from this numerical noise, while RLOO nulled 20-40%, even though RLOO should theoretically null 0% of batch data outside of mini-batch reuse; this was traced to `bf16` numerical instability rather than genuine policy drift, since the clipping ratio didn't change materially with more gradient steps per batch.

## Key Claims

- RLOO drops the value model from PPO's 4-model memory footprint, needing only 3 (policy, reference, reward model); this cuts GPU memory ~50-70% versus PPO depending on model size.
- RLOO trains 2x faster than PPO at 1B parameters and up to 3x faster at 6.9B parameters.
- RLOO's baseline for each of K sampled completions is the mean reward of the other K-1 completions for the same prompt (leave-one-out), computed without any learned value network.
- REINFORCE's loss is a special case of the (unclipped) PPO loss; the log-probability gradient term is implicit in PPO's importance-sampling ratio even without an explicit REINFORCE-style log-prob multiplication.
- Empirically, the 6.9B RLOO checkpoint reaches 78.7% GPT-4-judged preferred rate at k=2 on TL;DR summarization, exceeding the original RLOO paper's own best-reported 77.9% (k=4) and 74.2% (k=2); the 1B checkpoint reaches 40.1% win rate vs. 21.3% for the SFT baseline.
- `bf16` numerical noise between generation-time and training-time log-probs nulls gradients for ~3% of PPO's batch but 20-40% of RLOO's batch, because RLOO's importance ratio is computed over the full-completion summed log-prob rather than per-token.

## Figures

No figures were extracted for this ingest; the PPO-vs-RLOO memory/speed comparison charts and training-progress screenshots from Weights & Biases are described inline but not downloaded, per this batch's no-figure-download policy. All code snippets (vectorized baseline computation, REINFORCE-as-PPO-special-case demo, `RLOOTrainer` usage, and the bf16/fp16/fp32 log-prob stability comparison) are preserved in the source markdown.

## Entities

- [[Hugging Face]] — publishes the post and maintains TRL, where the `RLOOTrainer` ships.
- [[Cohere]] — Ahmadian et al.'s RLOO paper, which this TRL implementation is based on.

## Questions & Gaps

- The post flags the `bf16` log-prob mismatch as an open issue (linking to a `transformers` GitHub issue) rather than a resolved one; no fix is presented, only characterization of its worse impact on RLOO than PPO.
- No comparison is given between RLOO and GRPO (which shares the leave-one-out-style baseline idea but predates widespread TRL support at the time of this 2024 post).

## Related

- [[GRPO]]
- [[Reinforcement Learning Topic]]
- [[Keep the Tokens Flowing: Lessons From 16 Open-Source RL Libraries]] — later survey of async RL infrastructure that references RLOO/PPO-style critic-free training as a broader industry trend.
