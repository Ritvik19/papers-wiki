# GPT-5.2

**Source**: `raw/introducing-gpt-5-2/full-article.md`, `raw/gpt-5-system-card-update-gpt-5-2/full-article.md`, `raw/gpt-5-2-for-science-and-math/full-article.md`, `raw/introducing-gpt-5-2-codex/full-article.md`, `raw/gpt-5-2-codex-system-card/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

OpenAI released GPT-5.2 on December 11, 2025, framed around professional knowledge work: spreadsheets, presentations, code, image understanding, long context, tool use, and multi-step projects. The headline result is [[GDPval]], an internal benchmark of well-specified knowledge-work tasks across 44 occupations, where GPT-5.2 Thinking wins or ties industry professionals 70.9% of the time, up from 38.8% for GPT-5 Thinking (GPT-5.1 is not listed separately on this metric in the announcement) and GPT-5.2 Pro reaches 74.1%. On a related internal benchmark of junior investment-banking spreadsheet-modeling tasks, GPT-5.2 Thinking's average score rose from 59.1% (GPT-5.1) to 68.4%. Coding also advanced: 55.6% on SWE-Bench Pro and a new high of 80.0% on SWE-bench Verified, with early partners including Windsurf, Cognition, JetBrains, and Augment Code reporting state-of-the-art agentic coding results. On long context, GPT-5.2 Thinking reaches near 100% accuracy on OpenAI MRCRv2's four-needle variant out to 256k tokens, and on abstract reasoning GPT-5.2 Pro becomes the first model to cross 90% on ARC-AGI-1 (Verified) while GPT-5.2 Thinking sets a new chain-of-thought state of the art of 52.9% on ARC-AGI-2 (Verified).

A companion post the same day, "Advancing science and math with GPT-5.2," goes deeper on the model's mathematical and scientific reasoning: 93.2% on GPQA Diamond for GPT-5.2 Pro (92.4% for Thinking) and a new state of the art of 40.3% on FrontierMath Tier 1 through 3 for Thinking. It also documents a case study in which GPT-5.2 Pro helped resolve a 2019 open problem in statistical learning theory, posed at COLT 2019, about whether more training data reliably reduces expected error for a Gaussian model with known mean and unknown standard deviation. GPT-5.2 Pro produced a proof when asked to solve the open problem directly, which the paper's authors then verified and had reviewed by outside experts, with follow-up questions extending the result to higher dimensions and other statistical models.

The system card update for GPT-5.2 states its safety mitigation approach is largely unchanged from GPT-5 and GPT-5.1, while the main announcement reports continued improvement on sensitive conversations: mental health scores of 0.995 (Instant) and 0.915 (Thinking), both up from 0.883 and 0.684 for the respective GPT-5.1 models, alongside comparable gains on emotional reliance and self-harm evaluations. OpenAI also began rolling out an age-prediction model to automatically apply content protections for users likely to be under 18.

A week after the main launch, on December 18, 2025, OpenAI introduced GPT-5.2-Codex, a coding-optimized version with stronger long-horizon performance through context compaction and, notably, a sharp jump in cybersecurity capability. The announcement cites a real example: a security researcher using the prior model, GPT-5.1-Codex-Max, found and responsibly disclosed a vulnerability in React. GPT-5.2-Codex does not reach High cybersecurity capability under the Preparedness Framework, but OpenAI says it is designing for that eventuality, including an invite-only trusted-access pilot for vetted defensive-security professionals.

## Key Claims

- GDPval (wins or ties vs industry professionals): 70.9% (GPT-5.2 Thinking) and 74.1% (GPT-5.2 Pro), versus 38.8% for GPT-5 Thinking.
- SWE-bench Verified 80.0%, SWE-Bench Pro (public) 55.6% for GPT-5.2 Thinking, both new highs at launch.
- GPQA Diamond: 92.4% (Thinking) and 93.2% (Pro); FrontierMath Tier 1-3: 40.3% (Thinking), a new state of the art.
- ARC-AGI-1 (Verified): GPT-5.2 Pro is the first model to cross 90%, up from 87% (o3-preview) at roughly 390x lower cost; ARC-AGI-2 (Verified): 52.9% (Thinking) and 54.2% (Pro).
- OpenAI MRCRv2 four-needle accuracy is near 100% out to 256k tokens for GPT-5.2 Thinking.
- Mental health evaluation score improved from 0.883 (GPT-5.1 Instant) to 0.995 (GPT-5.2 Instant), and from 0.684 (GPT-5.1 Thinking) to 0.915 (GPT-5.2 Thinking).
- GPT-5.2 Pro helped resolve a COLT 2019 open problem on learning-curve monotonicity for maximum likelihood estimators, later verified by the paper's human authors.
- GPT-5.2-Codex does not reach High cybersecurity capability but is described as having stronger cybersecurity capability than any prior OpenAI model; retains High biology designation.
- Pricing: `gpt-5.2` / `gpt-5.2-chat-latest` at $1.75 input / $14 output per 1M tokens; `gpt-5.2-pro` at $21 input / $168 output.
- A new `xhigh` reasoning effort level was introduced alongside GPT-5.2. Built in collaboration with NVIDIA and Microsoft on Azure data centers using H100, H200, and GB200-NVL72 GPUs.

## Benchmarks

| Category | Eval | GPT-5.2 Thinking | GPT-5.2 Pro | GPT-5.1 Thinking |
| --- | --- | --- | --- | --- |
| Professional | GDPval (wins or ties) | 70.9% | 74.1% | 38.8% (GPT-5) |
| Professional | Investment banking spreadsheet tasks (internal) | 68.4% | 71.7% | 59.1% |
| Coding | SWE-Bench Pro (public) | 55.6% | - | 50.8% |
| Coding | SWE-bench Verified | 80.0% | - | 76.3% |
| Coding | SWE-Lancer IC Diamond | 74.6% | - | 69.7% |
| Long context | OpenAI MRCRv2, 8 needles, 128k-256k | 77.0% | - | 29.6% |
| Vision | CharXiv reasoning (no tools) | 82.1% | - | 67.0% |
| Tool usage | Tau2-bench Telecom | 98.7% | - | 95.6% |
| Academic | GPQA Diamond (no tools) | 92.4% | 93.2% | 88.1% |
| Academic | HLE (no tools) | 34.5% | 36.6% | 25.7% |
| Academic | AIME 2025 (no tools) | 100.0% | 100.0% | 94.0% |
| Abstract reasoning | ARC-AGI-1 (Verified) | 86.2% | 90.5% | 72.8% |
| Abstract reasoning | ARC-AGI-2 (Verified) | 52.9% | 54.2% (high) | 17.6% |

Mental health evaluations (higher is better):

| Eval | GPT-5.2 Instant | GPT-5.1 Instant | GPT-5.2 Thinking | GPT-5.1 Thinking |
| --- | --- | --- | --- | --- |
| Mental health | 0.995 | 0.883 | 0.915 | 0.684 |
| Emotional reliance | 0.938 | 0.945 | 0.955 | 0.785 |
| Self-harm | 0.938 | 0.925 | 0.963 | 0.937 |

## Preparedness Framework / Safety

The GPT-5.2 system card update states the model's comprehensive safety mitigation approach is largely the same as GPT-5's and GPT-5.1's; it introduces no new risk designation of its own in this update. The main announcement reports continued work on sensitive conversations, building on the safe-completions research introduced with GPT-5, with fewer undesirable responses on mental health, self-harm, and emotional reliance evaluations than either GPT-5.1 or GPT-5. OpenAI began rolling out an age-prediction model to automatically apply content protections for users likely to be under 18.

The GPT-5.2-Codex addendum evaluates the model as very capable in cybersecurity without crossing the High threshold under the Preparedness Framework, but frames this as a near-term risk: OpenAI states it plans and evaluates as though each new Codex model could reach High cybersecurity capability, and points to a real-world case, a React vulnerability found and responsibly disclosed by a security researcher using GPT-5.1-Codex-Max with Codex CLI, as evidence of how quickly model improvements translate into cybersecurity capability jumps. GPT-5.2-Codex keeps the High biology designation used across the GPT-5 family and does not reach High capability on AI self-improvement. OpenAI is building a trusted-access pilot, initially invite-only, for vetted security professionals with a track record of responsible disclosure.

## Figures

No article figures extracted; openai.com blocks direct HTML download so figures could not be downloaded, and WebFetch markdown does not preserve chart images. Benchmark data is preserved above as markdown tables instead.

## Entities

- [[OpenAI]] — publisher of GPT-5.2, its system card update, the science-and-math follow-up, GPT-5.2-Codex, and its system card.
- [[NVIDIA]] — GB200-NVL72 GPUs used in training and serving GPT-5.2, per the announcement's infrastructure note.
- [[Microsoft]] — Azure data centers hosting GPT-5.2 training and inference alongside NVIDIA hardware.

## Questions & Gaps

- The GDPval comparison in the main announcement lists GPT-5.1 Thinking's score as "38.8% (GPT-5)," which reads as a labeling inconsistency in the source rather than a GPT-5.1-specific figure; it is reproduced here as written.
- GPT-5.2-Codex's own capability benchmarks (SWE-Bench Pro, Terminal-Bench 2.0 numbers specific to this model) are described qualitatively in the announcement rather than tabulated; the system card confirms the risk designation without adding new capability numbers.
- API access timing for GPT-5.2-Codex was described only as "planned in coming weeks" as of the announcement.

## Related

- [[OpenAI]]
- [[GPT-5.1]]
- [[GPT-5.3]]
- [[Large Language Models]]
- [[Reasoning Models]]
- [[Code Models]]
- [[Agentic AI]]
- [[Evaluation and Benchmarks]]
- [[Long Context]]
- [[GDPval]]
- [[Preparedness Framework]]
