# Papers Explained 577: MAI-Thinking-1

Papers Explained 577: MAI-Thinking-1

Papers Explained 577: MAI-Thinking-1

MAI-Thinking-1 is a large reasoning model with 35B active/1T parameters, trained from scratch, on 30T tokens of exclusively clean…

Papers Explained 577: MAI-Thinking-1

MAI-Thinking-1 is a large reasoning model with 35B active/1T parameters, trained from scratch, on 30T tokens of exclusively clean, non-synthetic, human-generated data, with no distillation from third-party or open-source models. Its development follows three principles:

capabilities must be learned, not inherited
simplicity is sustainable
scientific rigor avoids shortcuts

The process includes successive improvements in architecture, data, and reinforcement learning optimized for sustained, log-linear gains.

Pre‐training

Model Architecture
Overview of the MAI-Base-1 architecture.
MAI-Base-1 uses a decoder-only Transformer. Each layer features RMSNorm at both the input and output, right before residual addition. The model does not use any biases. Input and output embedding weights are tied.

The model uses the o200k_base tokenizer (vocabulary size: 200,019) for better integration with tools, even though some in-house trained tokenizers showed performance improvement.

The model implements periodic attention, following Gemma 3: five local attention layers are paired with one global attention layer. Group-query attention is used with 8 KV heads and 128 per-head dimension. Local attention layers use rotary position encoding (RoPE), sliding window size of 512, base frequency 10,000. Global attention layers use no positional encoding, which is comparable to RoPE but more efficient.

For the feed-forward layer in each block, the model alternate between MoE layers and dense feed-forward networks (FFN). The first feed-forward layer is always dense. SwiGLU is used for all dense and MoE feed-forward layers.

The LatentMoE Design is adopted from NVIDIA: a shared down-projection occurs before all-to-all dispatch, then latent representations are projected back after combining. Routing is based on the original representation; each compressed representation can be routed to 8 of 512 experts via softmax gating.

The model uses global-batch load balancing loss, aggregating expert frequencies over data-parallel workers and micro-batches of the same global batch.

Pre Training Data
Pipeline for processing HTML pre-training data.
MAI-Base-1 is trained on a mixture of publicly available and licensed human-generated data, covering web, public GitHub code, books, academic papers, news, multilingual text, and domain-specific materials. The choice is made not to use language-model-generated synthetic data for pre-training, and an effort is made to avoid and remove AI-generated content within collected data sources.

Data Sources

For web data, a proprietary crawler is used that respects the Robots Exclusion Protocol (robots.txt) and related meta-tag and HTML controls. Sources that violate Microsoft Responsible AI policies or appear on the Office of the United States Trade Representative (USTR) Notorious Markets list are excluded. The training corpus also includes datasets acquired from third-party providers through commercial agreements. Prior to training, the entire corpus is processed using PII-risk and safety filtering.
Knowledge cut off dates for the training data sources.
HTML Extraction

Source-specific structured parsers are used for standardized formats such as HTML or XML, where schema-aware parsing enables accurate conversion into textual representations.
Hand-crafted extractors, implemented with tools such as BeautifulSoup, are applied to domains that exhibit consistent structure but are not well handled by our general heuristics, or where the value and volume of content justify additional engineering effort.
LLM- and agent-based processing is employed for domains requiring targeted extraction, normalization, or semantic filtering beyond what deterministic rules can provide.
Training on raw content is used when further processing risks discarding important information. For example, Wikipedia’s bespoke markup language, wikitext.

Deduplication

Boilerplate removal: Web HTML pages often contain repeated boilerplate text. Using line-occurrence statistics within and across documents, elements such as headers, navigation bars, footers, sidebars, and redundant paragraphs introduced by parsing artifacts are removed.
Exact duplicates: Identical content can appear multiple times due to republication across sites or repeated snapshots caused by system-level faults. Remove all exact byte-level and hash-level duplicates.
Fuzzy duplicates: MinHash Locality-Sensitive Hashing (LSH) based fuzzy deduplication is applied with a similarity threshold of 0.8.
Templated web pages: Many sites generate pages from a shared template with only minor lexical variation (e.g., “calculator” web pages with raw arithmetic tables). Skeletonize each page to its most frequent tokens and perform fuzzy deduplication over these templates to eliminate large families of near-identical pages.
Semantic duplication: Documents produced independently can still be highly similar due to shared context or canonical problem formulations. This is especially common in code datasets, where well-known programming exercises recur across homework sets, exams, interviews, and competitions. An Qwen3-Embedding-0.6B model is used to identify semantically similar documents and retain only a limited number of representatives per cluster.

Filtering and Categorization of Data

Across sources, data that is unlikely to contribute positively to training is first removed, including spam, restricted or policy-sensitive content, and other source-specific noise. The remaining data is then categorized into interpretable buckets, such as quality tiers, language groups, topical categories, educational value, educational level, source type, and domain-specific subcorpora.

Leveraging metadata signals, such as domain names, filenames, repository metadata, PDF creator and producer fields, and document-level metadata.
Source-specific heuristics, such as web text-quality filters, OCR-artifact filters, math-aware filters for STEM content, and path- or content-based filters for generated code.
Learned classifiers, including fastText-style classifiers and embedding-based models for language, topic, educational value, educational level, quality, and other semantic attributes.
Prompted LLMs, used selectively for higher-value or more ambiguous decisions such as section-level extraction, quality judging, and nuanced topic labeling.
Manual exploration and labeling, used to identify failure modes, validate filtering precision, audit high-impact source categories, and construct training data for classifiers and LLM judges.

Data Mixture for Training

The final mix contained large proportions of math and coding data (300B math tokens, code making up 16.4T tokens), while web and PDF data were used less per epoch, and multilingual data was very selectively downsampled For Mid-Training, No new data sources are introduced: instead, a higher-quality subset is selected and re-weighted for longer context. Proportions are adjusted: 35% STEM/math, 55% code, 10% background sources.
Rank non-invariance in data mixture scaling.
Attention initialization: Upon initialization, the attention softmax is close to uniform, which effectively performs average pooling over tokens subject to the causal constraint. This behavior reduces the diversity in token representations and can lead to highly imbalanced routing in subsequent MoE layers, increasingly so with depth. To address this, the attention output is initialized to zero, achieved by setting the output RMSNorm gains to zero. This means the model initially behaves like a stack of feedforward layers applied to individual tokens, while the cross-token interactions captured by the attention layers gradually kick in over the course of training.

The Reinforcement Learning Climb

The RL climb starts from a checkpoint with no prior exposure to reasoning traces. The model therefore has to develop its reasoning abilities from scratch, making long-term training stability a central challenge. This is enabled via three mechanisms:

Two simple but crucial adjustments to GRPO.
Self-distillation for resuming RL climbs after crashes or updates to the base policy.
Infrastructure improvements that eliminate numerical mismatch between training and inference.
Overview of the RL climbs.
To enable parallel development, three domain-specific specialist models are trained for:

STEM and competitive code
Agentic coding and tool use
Helpfulness and safety

The specialist models are subsequently consolidated into a single model using supervised finetuning. A final lightweight RL climb turns this consolidated model into MAI-Thinking-1, a model that performs strongly across all domains.

Reinforcement Learning Recipe

The reinforcement learning climb starts from a policy πθ. For a prompt q, the rollout policy samples a group of G responses y1:G, and each response yi receives a scalar reward Ri = R(q, yi). The reward function R is domain-dependent; typically, it is either based on executing code or feedback from a prompted AI judge or a trained reward model. The training objective is derived from GRPO with token-level policy gradient:

where P (Q) is the distribution over all prompts and πold denotes the policy used to generate the rollouts. For response yi and token position t, the importance-sampling ratio is:

The response-level advantage Ai = (Ri − mean(R1:G))/ std(R1:G) is shared across all tokens in response yi.

Two modifications are applied to this objective

Adaptive entropy control: dynamically adjusts the upper clip bound to maintain a target policy entropy.

Separate lower and upper clip bounds are used. These are parametrized using a single base hyperparameter ϵ, which controls the base trust-region width, together with an entropy-dependent relaxation k of the clipping upper bound.

The current policy’s entropy is dynamically adjusted using a simple integral controller. At each training step, the target policy’s per-token entropy is estimated via an importance-weighted estimator.

Given a target entropy H⋆, the controller updates k with a step size δ ∈ R+ after each step:

Intuitively, when entropy is too low, increasing k widens the upper clipping bound, allowing the policy to increase the probability of alternative tokens more aggressively. When entropy is sufficiently high, k is decreased to tighten the trust region. k is initialized with 0, so that the clipping bounds 1 − ϵ and (1 − ϵ)−1 are multiplicative inverses, making the initial clipping interval symmetric in log-ratio space.

Outer ratio clip caps the unclipped branches of the objective to prevent gradient-norm explosions. The GRPO objective deliberately leaves two cases unclipped: (a) advantage is negative and the new policy assigns higher probability than the old (i.e. Ai < 0 and ri,t > 1), and (b) advantage is positive and the new policy assigns lower probability (Ai > 0 and ri,t < 1). The original motivation is to leave the policy unbounded when it corrects itself in the right direction, only bounding moves that exploit the advantage estimate. In practice, it is found that these unclipped branches sometimes led to catastrophic gradient norm spikes. This is addressed by adding a hard outer clip that is applied to all branches:

Reward Design

R_task denotes the task-specific reward, R_lang is a language-consistency reward, and R_len is a length penalty. The coefficients wlang and wlen are scalar hyperparameters.

As context lengths increase during RL, models begin producing foreign-language tokens within their CoTs. These mixed language CoTs correlate with spikes in log-probability divergence between the training and inference policies, ultimately destabilizing training.

where non-english(yi) is the number of non-English words in the CoT of response yi and α is a per-word penalty.

The length penalty is defined as :

where ρ_q is the pass rate of problem q and ℓmax is the maximum rollout length. The penalty depends on both response length and problem difficulty. Hard problems with low pass rates receive weaker penalties, allowing the model to explore longer reasoning traces. Easy problems receive stronger penalties, encouraging concise and cost-efficient reasoning by removing redundant loops and hedging behavior.

Sampling Strategy

For each problem q in the training set, a group of rollouts is generated from the current inference model. To reduce inference cost, an early exit strategy is used: first, Gearly < G responses are sampled and their empirical pass rate is computed, i.e., the fraction of responses with positive reward. If the early pass rate lies in an acceptable range [ρ early min, ρ early max] = [0.05, 0.8], the full G responses are sampled; otherwise, the problem is discarded. After all G responses are generated, a second pass-rate filter [ρmin, ρmax] = [0.1, 0.8] is applied to the full group. Only problems whose full pass rate falls in this range are used for training.

Top-p (p = 0.97) sampling using πold is employed to sample rollouts y1:G. Continuing to backpropagate through logits corresponding to tokens outside the sampled nucleus can lead to catastrophic off-policy mismatch, causing divergence within a few training steps. To prevent this, these tokens are excluded during training by reusing the top-p truncation mask from rollout sampling to set the logits of all excluded tokens to −∞ prior to softmax computation. Top-p masking substantially reduces policy divergence during RL training, at the cost of additional overhead for mask storage and replay.

Self‐Distillation

Self Distillation involves collecting rollouts (samples of model behavior) during RL training, then conducting supervised fine-tuning (SFT) on a mid-trained checkpoint using these rollouts. The resulting self-distilled model is used as the starting point for continued RL training. It serves the following puposes:

Allowing the shift from initial task-specific prompt formatting to a standardized chat format, by updating the SFT data.
Recovering from RL run failures, particularly in cases where early RL instability causes divergence. Self-distillation helps transfer progress to a new climb.
Carrying progress forward when new pre-training / mid-training checkpoints become available, thus supporting the continual improvement of model generations.

Key findings:

About 1 million (O(1M)) reasoning traces are enough for the student to match the teacher’s performance and retain stability; more data gives little benefit and can overly constrain exploration in later RL.
Including reasoning traces that lead to incorrect answers works as well as using only successful traces, but in practice, training is restricted to successful traces since RL produces plenty of these.
Using traces from later checkpoints in the RL climb is important, as early checkpoint traces degrade performance and using only the final checkpoint reduces post-RL performance.
Collecting traces from multiple strong checkpoints provides useful diversity, aiding exploration and avoiding resampling.
When limited by token budget, increasing prompt diversity (variety in prompts) is more useful than simply adding more traces for each prompt.
Simple random sampling of traces beats biased selection approaches like shortest-trace sampling or filtering.

STEM Climb

STEM climb operates on pairs of verifiable data: To produce the task-specific reward Rtask(q, yi), the model’s final answer is extracted from yi and either compared to a ground truth using a formal verifier such as SymPy, an AI judge, or, in the case of competitive coding, the model-produced code snippet is run against a suite of problem-specific test cases. Millions of documents were processed, producing the STEM Mix dataset with more than 5M samples that is used for STEM climb.
Distribution of our STEM Mix dataset by original problem format and subject taxonomy.

Pipeline for extracting (q, a) pairs from textbooks and academic PDFs for STEM Mix.

The STEM data pipeline processes mixed raw sources (textbooks, academic PDFs, forum discussions, competition archives, vendor problems) into (question, answer) pairs using a composable, stage-based, asynchronous architecture.

Hierarchical parsing: Converts raw documents into initial (q, a) pairs. It:

Uses OCR (vision-language model or OCR services) as needed.
Chunks documents, discards non-STEM pages, and removes boilerplate.
Builds a structural hierarchy, fixes cross-references, numbering, and split-page artifacts.
An LLM identifies question and answer spans to yield candidate (q, a) pairs.

QA pairing: For sources where questions and answers are separated (e.g., exercises and answer keys), questions are matched to answers by structure and semantic similarity, with LLM selection and validation of best pairs.

Curation: Processes for quality and consistency using LLM-based classification and annotation, including:

Verifiability (dropping unverifiable items)
Question type classification (open-ended, multiple-choice, proofs)
Taxonomy assignment (fine-grained STEM topics)
PII detection and removal

Additional curation:

Detects and drops pairs where the answer is trivially contained in the question (“answer leakage”).
Rewrites multiple-choice and proofs into open-ended forms (with a three-pass consensus check). Items not reaching consensus are dropped.
Cleans up extraneous text or irrelevant references.

Scoring: Assesses difficulty and correctness:

Problems are solved multiple times by four model tiers. Pass rates inform difficulty brackets.
For hard problems, a blind judge compares model consensus vs. ground-truth answers. Suspect ground-truths are dropped if not preferred; genuinely hard items are kept.

Competitive Coding Data:

Uses a specialized pipeline due to the need for precise test cases, targeting sources and vendors (removing need for normal STEM pipeline extraction/filtering).
Each problem includes reference solutions verified by test cases, covering various algorithms and programming topics.
Dataset totals 160k problems, supports 17 languages, and includes runtime and memory constraints.

Deduplication and Decontamination (p.39):

Both STEM and coding datasets are deduplicated against themselves, benchmarks, and in-house evaluations.
Exact: SHA-256 hashes to remove exact duplicates.
Lexical fuzzy: n-gram shingling with MinHash LSH to find near-duplicates (using Jaccard similarity).
Vector: Lightweight model embeds and compares using cosine similarity.

Agentic Climb

The focus is on two agentic domains: software engineering (SWE), which involves executable software-engineering environments built from real repositories; and general tool use, which involves calling structured tools in multi-step tasks. In practice, a mixture of both agentic- and reasoning-focused STEM tasks is jointly climbed, including a competitive coding mixture. Inclusion of STEM tasks helps to stabilize the RL climb and shows positive transfer to multi-step software engineering and tool-calling performance. Conversely, the agentic tasks transferred neither positively nor negatively to STEM-related single-pass performance.
Agentic loop and multi-step orchestration in RL training.
Agentic multi-step RL uses the same core objective as the single-step reasoning RL recipe but extends rollouts from a single sampled response to a trajectory of policy steps and environment steps (observations). Each RL environment consists of a task specification, a Sandbox Execution Environment (SEE) session for executing tools, and a set of verifiable or judged rewards for evaluating task completion while tracking environment state. At each policy step, the model can emit tool calls or produce a final answer. Tool calls are executed inside the SEE session, and their outputs are appended to the context before the next policy step. The complete trajectory is then graded for correctness, after which credit assignment is applied uniformly across all tokens from all policy steps.

Software Engineering

Each environment is a deterministic, ready-to-use container image of a codebase at a specific commit, pre-installed with all dependencies. A problem statement and unit tests are provided; models interact by reading/editing files, running shell commands, and navigating the repo.

Data Collection:

Start with 102M public GitHub PRs.
Filter: Only merged PRs to main; under 15 files changed; must involve both code and test changes (tests used as hidden eval). Split out code vs. test changes.
Further filter for PRs linked to issues (GitHub, Jira, etc.), yielding 4.87M PRs with linked issue.

Automatic Environment Building:

Use an LLM agent to analyze the PR, create Docker files, and validate by running all tests. Discard on any dependency / environment failure.

Reference Grading Extraction:

Test suite runs on the base commit, first applying only test changes (pre-fix), then both test and code changes (post-fix).
Tests that go from failing to passing (F2P) provide the main issue-resolution signal (the model must patch to flip these).
Tests that always pass (P2P) are used to check for regressions.
Discard problems without F2P tests

Verification:

Re-validate the constructed environment, again running the grader to confirm correct/incorrect patches are scored properly.
Discard environments with non-deterministic tests or those that fail due to further sandbox infrastructure issues.

Quality Filtering and Rewriting:

Not all passing environments are high-quality: many have vague or underspecified statements.
Deploy an agent to score and potentially rewrite problem statements, inspecting for clarity, test quality, leakage risks, and feasibility, to better match the tests but not overspecify or leak too much info.
Only 265,617 environments (5.5% of initial 4.87M) pass all stages, covering 94,044 repositories.

Handling Failures and Synthetic Data:

Many failed validation due to bad problem specs or weak test coverage, not executability.
Inspired by BugPilot, SWE-Smith, and SWE-Mirror, the pipeline reuses valid executable environments to generate new synthetic problems and tests, helping to expand training data.

Prevention of Reward Hacking:

Internet search: Since solutions are in public PRs, network access is disabled or restricted in containers.
Local git history search: To stop agents from finding solution commits in git logs, the pipeline “time travels” the repository, deleting all commits after the base.
Tampering with tests: Before grading, all agent-edited test files are reset.

General Tool Use

These environments are more diverse than SWE RL environments, both in tools and application domains. Each problem is set up as an interactive environment using “mocked backends” to simulate real API or MCP behavior. Every problem comprises:

A user query
A set of available tools (with detailed schemas)
An initial state for the environment
A grader for evaluation

Unlike SWE settings (few tools), these tool-use tasks might involve over 50 tools at once, mirroring rich real-world interactions and necessitating efficient tool selection and generalization over many scenarios.

Training data includes both: Human-curated environments. Synthetic environments generated by a dedicated tool-calling task framework.

Synthetic Environment Generation involves:

Environment Bootstrapping: Generates tool descriptions, implementations, and seeds related database entries.
Task Creation: Samples realistic tool-call paths, instantiates relevant entities, and produces user requests.
Verification and Refinement: Executes previously generated actions, removes similar tasks, and iteratively critiques and refines outputs.

Persona generation (environment-specific) introduces further diversity to synthesized tasks.
Some tasks are written such that tools are described but not actually needed, to reduce unnecessary tool use.

Over 150 unique environments and 130,000 distinct tasks are synthesized.

Training employs both environment-specific and generic cross-environment graders.

Environment-specific graders: Assess based on final environment state, tool usage patterns, and task answers.
Synthetic environments: Grading is further decomposed, an LLM judge breaks down tasks to sub-tasks and grades each independently.
Cross-environment graders: Incentivize efficient tool usage (e.g., parallel usage where possible, avoidance of duplicates, correct parameter use).

This nuanced reward structure guides better generalization and efficiency.

Helpfulness and Safety Climb

This climb differs from the other climbs in that it focuses on tasks where performance is not as objectively defined and machine-verifiable. Compared to the other climbs, the helpfulness and safety climb combines a more diverse set of reward types to guide subjective aspects of model behavior. A combination of a reward model trained on human preference data, AI judge feedback (typically rubric-guided), and additional verifiable rewards is used to form an aggregate reward signal.

The reward model is based on a post-trained version of MAI-Base-1, which is fine-tuned to predict human preferences expressed as text tokens. It is trained exclusively on human preference data collected with human annotators from several vendors. For a context c and k-way side-by-side with responses y1, …, yk, and corresponding scores s1, . . . , sk ∈ [1; 5], the input to the reward model is

c <|im_sep|> y1 <|im_sep|> y2 <|im_sep|> …<|im_sep|> yk <|im_sep|>

where the training objective is the sequence s1 . . . sk, trained via SFT.

The reward model is applied cyclically: For a given context c and k responses y1, . . . , yk, the reward model is prompted k times on the response permutations (y1, . . . , yk), (y2, . . . , yk, y1), . . . , (yk, y1, . . . , yk−1). For each of these k inference calls, only the first token is decoded and the full probability distribution for this token is examined.

The reward signal RRM(c, yi) is then set to the probability of yi being scored as the highest quality (si = 5).

AI judges are employed for feedback that can be adapted quickly and customized to any given context.

Verifiable rewards are employed to improve capabilities in areas such as instruction following where adherence to a constraint can be checked directly.

When optimizing these rewards for helpfulness and safety climbing, two challenges arise.

The different types of rewards occupy different scales and are not directly comparable.
The reward distribution is itself context-dependent, narrow for some prompts and wide for others.

These challenges are addressed with two complementary strategies, applied selectively based on the context:

Lexicographic reward shaping is used for one set of contexts, where lower-importance rewards become active only when all rollouts in a group score equally on higher-importance rewards.
Gated reward application is used for other contexts, where higher importance rewards must satisfy a minimum level of performance before lower-importance rewards are applied at all.

Instruction Following and Steerability

The IF dataset spans constraints, scenarios, and complexity levels, blending synthetic data and expert human annotations.

Synthetic Data Generation starts with LLM-guided instruction using a manually curated constraint taxonomy. Scenarios cover multilingual, short/extended dialogues, system/developer/user messages, and 40+ domains (coding, writing, analysis, travel). Adversarial cases with conflicting instructions help train hierarchy respect. All scenarios get critique/rewrite for naturalness, rubric alignment, and groundedness.

Quality is assured by rounds of filtering using quality heuristics, complexity filters, rejection sampling. Rubrics validated for self-containment, unambiguity, alignment; prompts screened for safety. Difficulty controlled via pass-rate analysis.

Safety

Taxonomy targets two failure modes: unsafe compliance (should decline, but complies) and over-refusal (declines legitimate requests). Each candidate is annotated against policy taxonomy and assigned to one of two prompt categories:

Harmful Prompts: Requests where some/all help is disallowed. Response: full/partial refusal (declining unsafe portion, offering safe alternatives).
Borderline Prompts: Requests touching sensitive domains but answerable within policy. Response: “do-not-refuse” bounded, helpful answer; no hedging/refusal.
Sources of harmful and borderline prompts.
Honesty

Honesty means correct responses when the model “knows,” appropriate hedging when uncertain. Model shouldn’t over-hedge: balance factual precision and informativeness.

Diverse, manually curated vendor data, PII-filtered Copilot logs, and synthetic data is used spanning:

Established factual queries: Precise verification against reference answers.
Challenging factual queries: Long-tail/obscure topics; reference labels via search-augmented verification.
False-premise queries: Question contains incorrect presupposition; no correct affirmative answer exists. Includes boundary cases to press for factual integrity and hedging only when lacking knowledge.

Reference labels generated offline per RL example via retrieval-augmented generation/verification. LLM judge scores responses by factuality and confidence, producing five categories:

CONFIDENT_CORRECT,
UNCONFIDENT_CORRECT,
NOT_ATTEMPTED,
UNCONFIDENT_INCORRECT,
CONFIDENT_INCORRECT.

Style

Style guide: warmth without sycophancy, scannable structure, tone calibrated to context (not user mirroring). Also covers emojis, formality level, math/code notation, general text density.
Examples of target behavior descriptions from our style guide.
Data is style graded with PII-filtered Copilot logs, vendor-written contexts (static and interactive), and Arena conversations. Covers low-to-medium difficulty prompts (excludes complex instruction, coding, math, STEM). Prompts classified by user intent (creative writing, practical guidance, information-seeking, chit-chat); active collection in model-weak areas.

Consolidating Capabilities into a Single Model

The consolidation into a single model occurs in two stages. The SFT stage reuses the self-distillation pipeline applied to each of the specialist teachers, though the three teachers require different filtering and rejection sampling strategies. For the STEM and agentic teachers, rollouts are sampled across multiple checkpoints of each climb, prioritizing later checkpoints. Multiple correct rollouts per context are kept, and only light filtering is applied to remove degenerate CoTs. For the helpfulness and safety teacher, LLM judges and heuristic filters are used to score traces on style, structure, and known defects in addition to correctness.

The final stage of lightweight RL further improves safety, over-refusals, and style. The recipe is based on the Helpfulness and Safety Climb with a few changes to maintain reasoning performance. Training occurs at a maximum sequence length of 128k tokens, and a small proportion of STEM and coding data is retained in the RL mixture; both are found to be important, as reasoning performance on complex tasks otherwise degrades slowly over the climb.

Evaluation
Post-trained model evaluation results on STEM and agentic coding public benchmarks.Post-trained model evaluation results on various public benchmarks.
MAI-Thinking-1 delivers consistently strong, competitive performance across a wide range of benchmark categories, though it does not lead the field overall.
The model outperforms Claude Sonnet 4.6 on AIME 2025 and approaches Claude Opus 4.6 performance on SWE-Bench Pro.
On most benchmarks covering general capabilities (knowledge, instruction following, long context, safety, honesty, health, tool calling), MAI-Thinking-1 performs comparably with Sonnet 4.6.
Terminal-Bench performance reflects the model’s capacity to generalize from broader agentic training, not targeted environment-specific training.

Paper

MAI-Thinking-1: Building a Hill-Climbing Machine

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

View original.

Exported from Medium on June 13, 2026.
