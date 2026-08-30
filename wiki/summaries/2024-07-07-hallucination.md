# Extrinsic Hallucinations in LLMs

**Source**: `raw/2024-07-07-hallucination/full-article.md` (canonical HTML, 111 KB); `raw/2024-07-07-hallucination/full-article.md` (markdown view)  
**Ingested**: 2026-05-21  
**Tags**: #summary

## Summary

Lilian Weng's July 2024 post narrows the broad term "hallucination" to *extrinsic hallucination*: cases where a language model generates content that is fabricated and ungrounded by either the provided context (in-context hallucination) or world knowledge encoded in pre-training data (extrinsic hallucination). To avoid extrinsic hallucination, LLMs must be (1) factual and (2) calibrated to refuse or hedge when they do not know an answer.

The article diagnoses two root causes. First, pre-training data at web scale inevitably contains stale, missing, or incorrect information that the model may memorize by maximizing log-likelihood. Second, supervised fine-tuning and RLHF for instruction following can introduce new knowledge that the model cannot reliably absorb at fine-tuning compute scale; Gekhman et al. (2024) showed that examples with *Unknown* knowledge are learned much slower, and once learned, they cause the model to hallucinate—the best dev performance is obtained when the model learns most *Known* examples but very few *Unknown* ones.

Detection methods span four families. *Retrieval-augmented evaluation* (FactualityPrompt, FActScore, SAFE, FacTool) decomposes model output into atomic facts and verifies each against a knowledge base or search engine. SAFE showed 72% agreement with humans and 76% win rate at 20× lower cost. *Sampling-based detection* (SelfCheckGPT) checks consistency across multiple black-box samples without needing external knowledge. *Calibration-based evaluation* (TruthfulQA, SelfAware, CalibratedMath, Kadavath et al.) measures whether models assign calibrated probability to correct answers; RLHF fine-tuning degrades calibration but higher sampling temperature partially restores it. *Indirect query* methods (Agrawal et al.) detect hallucinated references by checking auxiliary facts rather than a direct truthfulness query, exploiting the lower likelihood that multiple samples agree on consistent secondary details of a fabricated reference.

Anti-hallucination approaches form four clusters. *RAG+Editing* (RARR, FAVA) retroactively retrieves supporting documents and edits model outputs to correct unsupported claims. *Retrieval+Selection* (RR / Rethinking with Retrieval, Self-RAG, RECITE) generates multiple reasoning paths and selects the most knowledge-consistent answer, or trains a model to emit special reflection tokens guiding retrieval. *Inference-time intervention* (CoVe, factual nucleus sampling, ITI / Inference-Time Intervention) steers generation by verification, restricting nucleus sampling to factual tokens, or editing internal attention head activations toward a "truthful" probe direction. *Fine-tuning for factuality* (GopherCite, WebGPT, FLAME) trains models with attribution or factual reward signals so they learn to cite supporting documents or refuse uncertain answers.

## Key Claims

- Pre-training data volume makes complete factuality verification intractable; models memorize incorrect information by log-likelihood maximization.
- Fine-tuning on new knowledge that the base model does not already "know" increases hallucination rate; *MaybeKnown* examples benefit generalization more than *HighlyKnown* examples.
- FActScore decomposes long-form generation into atomic facts; retrieval-augmented validation consistently outperforms non-context LLM judges.
- SAFE (Wei et al. 2024) uses an agentic multi-step search loop (F1@K metric) and beats human annotators at 20× lower cost.
- SelfCheckGPT needs only black-box access: consistency across stochastic samples flags factual mistakes without a knowledge base.
- Larger models are better calibrated on multiple-choice questions (Kadavath et al.); RLHF degrades calibration; adversarial benchmarks like TruthfulQA reveal larger models can be *less* truthful due to common misconceptions.
- Indirect queries (asking for auxiliary details) better distinguish hallucinated references than direct truthfulness queries.
- RARR achieves better preservation–attribution balance than baseline RAG approaches using a two-stage research+revision loop.
- Self-RAG trains a single model to emit retrieval and critique reflection tokens, outperforming always-retrieve baselines without test-time modifications.
- RECITE generates relevant passages from model parametric memory, then conditions answer generation on them (retrieval from memory vs. retrieval from index); comparable to BM25 retrieval on common topics.
- CoVe generates a verification plan, answers each question **independently** (draft absent from context), then revises — the independence step is what makes it effective vs. naive self-revision.
- Factual nucleus sampling dynamically decays the nucleus probability p within each sentence: p_t = max(ω, p·λ^(t−1)), concentrating later-token sampling near-greedily where factual entities appear.
- ITI probes for a "truthfulness" direction via linear probes on attention head activations and shifts inference-time activations toward that direction; most heads are uninformative — only a sparse subset is useful.
- GopherCite and WebGPT train models with factual reward signals to produce cited, attributable responses; RL adds only limited benefit over the SFT/BC baseline in both systems.
- FLAME shows RLHF *degrades* factuality (human raters prefer long, detailed answers); FActScore-as-reward DPO restores factuality without introducing Unknown-knowledge hallucinations.
- FactTune-FS (DPO with FActScore-graded preferences, no human annotation) achieves the best factuality improvement among factuality fine-tuning variants.

## Figures

| Figure | Caption |
|--------|---------|
| ![fig-25](../assets/2024-07-07-hallucination/fig-25.webp) | Knowledge categorization of closed-book QA examples based on how likely the model outputs correct answers (Known/Unknown taxonomy) — Gekhman et al. 2024 |
| ![fig-24](../assets/2024-07-07-hallucination/fig-24.webp) | Train and dev performance over time when fine-tuning on half Known, half Unknown examples — Unknown examples learned much slower |
| ![fig-23](../assets/2024-07-07-hallucination/fig-23.webp) | Evaluation framework for FactualityPrompt benchmark (Lee et al. 2022) |
| ![fig-22](../assets/2024-07-07-hallucination/fig-22.webp) | Factuality estimation: retrieval-augmented vs non-context LLM across FActScore variants |
| ![fig-13](../assets/2024-07-07-hallucination/fig-13.webp) | SAFE overview: agentic multi-step search loop for verifying atomic facts |
| ![fig-12](../assets/2024-07-07-hallucination/fig-12.webp) | F1@K long-form factuality results for mainstream models (Wei et al. 2024) |
| ![fig-15](../assets/2024-07-07-hallucination/fig-15.webp) | SelfCheckGPT overview: consistency checking against multiple stochastic samples |
| ![fig-14](../assets/2024-07-07-hallucination/fig-14.webp) | SelfAware accuracy by instruct-GPT model size on answerable vs unanswerable questions |
| ![fig-17](../assets/2024-07-07-hallucination/fig-17.webp) | Calibration curves for models of various sizes: larger models better calibrated |
| ![fig-19](../assets/2024-07-07-hallucination/fig-19.webp) | Direct vs indirect query for checking hallucinated reference generation |
| ![fig-09](../assets/2024-07-07-hallucination/fig-09.webp) | RARR (Retrofit Attribution using Research and Revision) illustration |
| ![fig-02](../assets/2024-07-07-hallucination/fig-02.webp) | FAVA: retriever + editor model for factuality verification with augmented knowledge |
| ![fig-11](../assets/2024-07-07-hallucination/fig-11.webp) | RR (Rethinking with Retrieval) performance on commonsense, temporal, and tabular reasoning |
| ![fig-26](../assets/2024-07-07-hallucination/fig-26.webp) | Self-RAG overview: model retrieves documents in parallel and critiques its own generation |
| ![fig-10](../assets/2024-07-07-hallucination/fig-10.webp) | RECITE: Recitation-Augmented Generation using parametric memory |
| ![fig-01](../assets/2024-07-07-hallucination/fig-01.webp) | CoVe: Chain-of-Verification — plan questions, answer independently, revise |
| ![fig-21](../assets/2024-07-07-hallucination/fig-21.webp) | Factual nucleus sampling: restricts sampling nucleus to factually-consistent tokens |
| ![fig-08](../assets/2024-07-07-hallucination/fig-08.webp) | ITI (Inference-Time Intervention): probing and shifting attention head activations |
| ![fig-06](../assets/2024-07-07-hallucination/fig-06.webp) | GopherCite demo-generation examples |
| ![fig-07](../assets/2024-07-07-hallucination/fig-07.webp) | GopherCite results: factuality and supporting evidence scores |
| ![fig-16](../assets/2024-07-07-hallucination/fig-16.webp) | WebGPT-RL: training GPT-3 to browse the web and produce attributed answers |
| ![fig-03](../assets/2024-07-07-hallucination/fig-03.webp) | FLAME results: factuality fine-tuning with NLI-based reward |
| ![fig-04](../assets/2024-07-07-hallucination/fig-04.webp) | FLAME framework architecture |
| ![fig-05](../assets/2024-07-07-hallucination/fig-05.webp) | FacTool framework for evaluating factuality across task types |
| ![fig-18](../assets/2024-07-07-hallucination/fig-18.webp) | Calibration results under task distribution shifts (Lin et al. 2022) |
| ![fig-20](../assets/2024-07-07-hallucination/fig-20.webp) | Fine-tuning new knowledge results (Gekhman et al. 2024) |

## Entities

- [[Lilian Weng]] — author; post published July 7, 2024 on lilianweng.github.io.
- [[FActScore]] — atomic-fact factuality metric; validates each atomic fact against Wikipedia via retrieval (Min et al. 2023).
- [[SAFE]] — Search-Augmented Factuality Evaluator; agentic multi-step search + F1@K metric (Wei et al. 2024).
- [[FacTool]] — multi-task factuality detection; extends fact-checking to code, math, and literature review (Chern et al. 2023).
- [[TruthfulQA]] — adversarially constructed 817-question benchmark; inverse scaling (larger = less truthful) (Lin et al. 2021).
- [[SelfCheckGPT]] — zero-resource black-box hallucination detection via stochastic sample consistency (Manakul et al. 2023).
- [[RARR]] — Retrofit Attribution using Research and Revision; two-stage research+revision attribution without retraining (Gao et al. 2022).
- [[Self-RAG]] — trains a model to emit Retrieve / ISREL / ISSUP / ISUSE reflection tokens for adaptive retrieval and self-critique (Asai et al. 2024).
- [[CoVe]] — Chain-of-Verification; four-step plan/verify/revise; Factored+Revise variant is best (Dhuliawala et al. 2023).
- [[RECITE]] — Recitation-Augmented Generation; parametric memory as retrieval mechanism; comparable to BM25 on common topics (Sun et al. 2023).
- [[Factual Nucleus Sampling]] — decaying nucleus p within sentences (p_t = max(ω, p·λ^(t−1))) to protect late-token factual entities (Lee et al. 2022).
- [[ITI]] — Inference-Time Intervention; sparse attention head probing + activation shift toward truthfulness direction (Li et al. 2023).
- [[GopherCite]] — few-shot + context stuffing demonstrations + RL from human preferences; selective prediction via RM threshold (Menick et al. 2022).
- [[FLAME]] — Factuality-Aware Alignment; SFT + FActScore-as-reward DPO; RLHF degrades factuality finding (Lin et al. 2024).
- [[Papers Explained 123 - WebGPT]] — GPT-3 + web browser + RL; cited answers; RL adds limited benefit over behavior cloning baseline (Nakano et al. 2022).

## Questions & Gaps

- The post was written in July 2024; it predates the wave of reasoning models (o1, DeepSeek-R1) and their specific hallucination patterns. How do chain-of-thought reasoning models change the hallucination landscape?
- The "hallucination tax" of RL fine-tuning (see [[Papers Explained 457 - Hallucination Tax of Reinforcement Finetuning]]) was published 2025; it directly extends the Gekhman et al. finding here.
- ITI and factual nucleus sampling are inference-time methods; how do they compose with RAG?
- SAFE's F1@K metric trade-off between precision (factual) and recall (length) leaves open questions about optimal K values for different task types.

## Related

- [[Reward Hacking in Reinforcement Learning]] — Weng's companion 2024 post; sycophancy overlaps with hallucination under adversarial graders.
- [[Evaluation and Benchmarks]] — TruthfulQA, FActScore, SAFE, SelfAware, LongFact benchmarks discussed here extend the wiki's eval coverage.
- [[Safety and Alignment]] — hallucination as an alignment failure; RLHF calibration degradation discussed.
- [[Papers Explained 457 - Hallucination Tax of Reinforcement Finetuning]] — extends Gekhman et al. 2024 finding; RL fine-tuning degrades refusal behavior.
- [[Papers Explained 123 - WebGPT]] — WebGPT is one of the anti-hallucination methods discussed here.
- [[Reinforcement Learning from Human Feedback]] — RLHF shown to degrade calibration and factuality.
- [[Large Language Models]] — root discussion of LLM factuality.
- [[Lilian Weng]] — author.
- [[Extrinsic Hallucination]] — core concept this post defines and surveys.
- [[FActScore]] | [[SAFE]] | [[FacTool]] | [[SelfCheckGPT]] — detection frameworks.
- [[RARR]] | [[Self-RAG]] | [[RECITE]] — RAG-based mitigations.
- [[CoVe]] | [[Factual Nucleus Sampling]] | [[ITI]] — inference-time mitigations.
- [[FLAME]] | [[GopherCite]] — factuality fine-tuning approaches.
