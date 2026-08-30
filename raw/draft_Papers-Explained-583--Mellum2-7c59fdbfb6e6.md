# Papers Explained 583: Mellum2

Papers Explained 583: Mellum2

Papers Explained 583: Mellum2

Mellum 2 is an open-weight 12B-parameter Mixture-of-Experts (MoE) language model with 2.5B active parameters per token, specialized in…

Papers Explained 583: Mellum2

Mellum 2 is an open-weight 12B-parameter Mixture-of-Experts (MoE) language model with 2.5B active parameters per token, specialized in software engineering, spanning code generation and editing, debugging, multi-step reasoning, tool use and function calling, agentic coding, and conversational programming assistance, and it is the successor to the completion-focused 4B dense Mellum model. Its pre-training spans approximately 10.6 trillion tokens through a three-phase curriculum that progressively shifts the mixture from diverse web data toward curated code and mathematical content (code ratio 23 % → 42 % → 59 %).

The models are available at HuggingFace.

Model Architecture

Mellum 2 is a decoder-only Transformer that closely follows the Qwen3-MoE recipe:

Backbone: 28 transformer layers, hidden dimension 2,304, with pre-RMSNorm (𝜖 = 10−6) and SiLU-gated MLPs.
Attention: 32 query heads and 4 KV heads (GQA, head dimension 128), QK-Norm applied to the query and key projections, and RoPE with base 𝜃 = 500,000.
Sliding window attention: a 3:1 SWA pattern in which 3 out of every 4 layers use a sliding window of 1,024 tokens and the remaining layer uses full attention.
Mixture-of-Experts: 64 routed experts per layer with 8 active per token (top-8 routing), expert intermediate size 896, and no shared expert.
Multi-Token Prediction: a single MTP transformer layer trained with loss weight 𝛼 = 0.1, used as a draft model for speculative decoding and removed at evaluation time.
Embeddings: untied input/output embeddings over a 98,304-token vocabulary; native context length 8,192 tokens (extended to 131,072 in long-context training).

This configuration totals ∼12B parameters with ∼2.5B active per token.
Architecture configuration of Mellum 2.
Pre-Training

Training Data

The pre-training corpus comprises approximately 10.6 trillion tokens drawn from diverse sources and is organised in three broad categories: web and general knowledge, source code, and mathematical content.

The code data includes raw, permissively licensed source code files collected from public repositories and deduplicated at the file level, web pages containing code extracted from Common Crawl, and a suite of synthetic and derived code datasets. The derived datasets augment raw code with natural language annotations including code summarizations, functionality extensions, translations between programming languages, test generation, commit messages, and task descriptions. Synthetic code datasets covering question answering, code rewriting, code review, transpilation, and educational explanations are also included.

The web data component includes large-scale synthetic web corpora derived from Common Crawl, educational web content, educational PDFs, multilingual reasoning and QA datasets, and curated knowledge sources including SFT data, STEM instruction data, rewrites of Wikipedia pages, and synthetically generated encyclopedic articles.

Mathematical data includes math-focused SFT data, math-oriented web content at multiple quality tiers, permissively licensed math textbooks, and math instruction-tuning data.

A custom tokenizer with a vocabulary size of 98,304 tokens, specifically designed to provide strong coverage of programming language tokens and technical terminology, is used.

Training Curriculum

Following the “web early, curated late” paradigm, pre-training is organized into three phases that progressively shift from diverse web content toward high-quality code and mathematical data. The phase boundaries are aligned with the Warmup-Stable-Decay (WSD) learning rate schedule.

Phase 1: Foundation Building (∼6.18T tokens, 58%) establishes broad linguistic capabilities and foundational code understanding using predominantly web data. The mix is approximately 70% web and general knowledge, 23% code, and 6% math.

Phase 2: Quality Uplift (∼2.79T tokens, 26.2%). The second phase shifts toward higher-quality data, with significant code upsampling to 42%. High-quality curated datasets, including SFT data, reasoning QA, STEM instruction data, and knowledge-aligned articles, are introduced in this phase rather than Phase 1, as curated data is more effective during stable learning rate than during warmup. New synthetic code datasets covering question answering, code rewriting, and educational explanations are added. The raw code corpus enters its second epoch.

Phase 3: Capability Sharpening (∼1.69T tokens, 15.9%) maximizes coding and mathematical capability during learning rate decay, when the model is most sensitive to data quality. Code reaches 59% of the mix. Additional synthetic code datasets covering code review and cross-language transpilation are introduced. The raw code corpus enters its third epoch. Web content is reduced to only the highest-quality curated sources.
Three-phase pre-training curriculum.
A multi-stage quality filtering pipeline is applied toA multi-stage quality filtering pipeline is applied to the raw data:

Heuristic filtering: Checks are applied on line length, entropy, comment ratio, and AST parseability for code data. Samples with fewer than 82 unique tokens are filtered to eliminate degenerate sequences with abnormally low lexical diversity, which are identified as a source of periodic training loss drops.
Classifier-based filtering: Quality classifiers at multiple tiers are used to stratify web data by quality, enabling phase-appropriate data selection.
Deduplication: MinHash-based near-deduplication [37] at the file level for code data. For web data, intra-phase deduplication is applied, while cross-phase repetition is intentional and aligned with the curriculum design.

High-quality data is scarce, so it is repeated. Small curated code datasets (summarization, test generation, translation, commit messages, algorithmic solutions) are shown across all three phases, and the raw code corpus is seen for three epochs, contributing roughly 958B tokens. No dataset is repeated more than 4× over the full run, which is found to be the point where further repetition stops yielding gains.

In addition to standard left-to-right next-token prediction, Mellum 2 is trained with a Fill-in-the-Middle (FIM) objective. Documents selected for FIM are split into a (prefix, middle, suffix) triple at two uniformly sampled positions and reformatted with sentinel tokens. A 50/50 split between the Prefix–Suffix–Middle (PSM) and Suffix–Prefix–Middle (SPM) orderings is used in all phases.

The fraction of training documents transformed into FIM examples varies across the curriculum to match the data composition of each phase. In Phase 1, the FIM rate is 50% and is applied to all data, exposing the model to bidirectional context early when the mix is dominated by web and general-knowledge text. In Phase 2, the FIM rate is reduced to 10% so that the high-quality curated code, reasoning, and instruction data introduced in this phase is consumed primarily under the standard left-to-right objective. In Phase 3, the FIM rate is restored to 50%, but the transformation is restricted to source-code files only; non-code data (curated web, math, reasoning) continues to be trained with next-token prediction.

Training Setup

The Muon optimizer is used, it applies orthogonalization-based updates to hidden layers while using Adam for embedding and output layers.
Training schedule for Mellum 2.
The learning rate warms up linearly over 2,000 steps to a peak of 3 × 10−4, holds at peak through Phases 1 and 2, then decays linearly to zero over Phase 3 (∼49,306 steps, approximately 15% of total training).

The global batch size ramps linearly from 2,048 to 4,096 sequences during the initial phase of training. At full batch size, each step processes approximately 33.6M tokens (4,096 × 8,192).

BF16 is used as the base precision with FP8 hybrid mixed-precision training. Gradient reduction is performed in FP32 to maintain numerical stability.

For the MoE routing, global auxiliary load-balancing loss with a coefficient of 10⁻³ is used, combined with a router z-loss of 10⁻³ for training stability. The router operates in FP32 precision. Both per-sequence and global-batch balancing strategies were explored, with global-batch balancing being chosen for its flexibility, despite per-sequence balancing producing slightly better loss on short runs. Dropless routing (no expert capacity factor) is adopted, which avoids token dropping entirely.

Documents are combined into fixed-length 8,192-token training sequences using best-fit packing, which minimizes intra-document truncation relative to the standard concatenate-and-chunk approach.
Optimizer and training hyperparameters.
Long Context Extension

YaRN is adopted for context extension, but it is applied selectively rather than uniformly across the network. Specifically, the YaRN frequency re-mapping is applied only to the global (full-attention) layers, leaving the sliding window layers with their original RoPE parameters. Applying YaRN only to the global layers outperforms both (i) a uniform RoPE base (𝜃) bump on all layers and (ii) leaving 𝜃 unchanged. Intuitively, the sliding window layers operate on a fixed local span and therefore do not require frequency re-mapping, while the global layers are the only ones that must extrapolate to the new sequence length.

The training data for the extension stage combines a rebalanced version of the Phase 3 pre-training mix with a portion of agentic SFT data, which naturally contains long-context examples. To preserve the in-IDE completion capability at long contexts, FIM-formatted examples with repository-level context are also injected into the extension mix.

Post Training

Supervised Fine-Tuning

Two SFT variants of Mellum 2 are trained:

Instruct: a general-purpose assistant that produces answers directly, without an externalized chain of thought. Loss is computed on every assistant turn in the conversation, with all other tokens masked, and any reasoning fields present in the source data are discarded.
Thinking: a reasoning-augmented assistant that emits an internal chain of thought before its final answer. Only the final assistant turn, together with its reasoning trace, contributes to the loss. To amplify the effective signal on multi-turn data, each multi-turn conversation is unfolded by sliding the loss target across successive assistant turns, producing up to five training samples per source conversation.

After tokenization, sequences are packed to the full 131,072-token training length; samples that would not fit cleanly into a pack are dropped rather than truncated. Both variants reuse the pre-training optimizer and precision stack and keep the Multi-Token Prediction head active throughout SFT.

The SFT mix can be grouped into the following broad categories:

General chat and instruction-following. Single- and multi-turn conversational data covering open-domain questions, reading-comprehension QA, multiple-choice items, and short-form instruction-following.
Single-turn coding. Code generation, editing, explanation, and translation prompts spanning multiple programming languages, with dedicated splits for C++, Python, C#, JavaScript and TypeScript competitive programming.
Agentic coding. Long-horizon interactive agent trajectories (early and revised generations), including SWE-style repository-level edit tasks. These supply the model with patterns for navigating a codebase, planning multi-step edits, and verifying intermediate results.
Tool use and function calling. Tool-augmented conversations covering general function-calling formats, Bash execution, a clarification tool, and search tools. The mix teaches both schema-faithful tool invocation and recovery from tool errors.
Reasoning traces. Chain-of-thought-bearing examples that populate the reasoning field used by the thinking variant. These cover math, code, and general reasoning; they are filtered out at processing time for the instruct variant.
Safety. Refusal and safe-response data drawn from a permissively licensed safety corpus, included to reduce harmful completions without degrading helpfulness on benign code prompts.
Identity examples. A small set of self-identification dialogues is oversampled (3×) so that the model reliably introduces itself as Mellum 2 rather than its upstream architectures.
Supervised fine-tuning configuration.
Reinforcement Learning

RL is run twice, once per SFT variant. Both stages use a variation of GRPO with a few adjustments that have become standard across recent open RL systems:

The loss is token-level: every valid generated token contributes equally to the gradient, as recommended by DAPO and Dr. GRPO.
Advantages are computed per prompt group with a leave-one-out baseline and without standard-deviation normalization, again following Dr. GRPO.
𝐺 responses are sampled per prompt, oversampled by roughly 1.5×, and prompt groups whose within-group reward variance is zero are discarded, an approximate version of the dynamic-sampling step from DAPO.
The PPO surrogate uses an asymmetric clip range [1 − 𝜖low, 1 + 𝜖high], the “clip-higher” setting introduced by DAPO, which lets positive-advantage updates flow more freely than negative ones.
The policy is not anchored to the reference with a KL term.

The per-token log-probabilities differences between train and inference is quantified as :

If 𝜌𝑡 is much larger or smaller than 1, a few outlying tokens could dominate the training gradients, leading to instability. To guard against this per-token IcePop truncation is used: For each token, only keep its contribution to the loss if 𝜌𝑡 falls inside a set interval [𝛼, 𝛽], otherwise, drop the token’s contribution entirely.

Putting the pieces together, the per-step loss minimised by the trainer is:

Two reward-shaping rules on top of the verifier’s raw score:

Soft Overlong Penalty (from DAPO):

Applied to responses just below the maximum allowed length.
Rewards are linearly interpolated between the raw score at the lower buffer edge and a set minimum (“floor”) at the length cap.
Responses that exceed the cap are dropped from traini

Concision Penalty (ARLCP-style):

Targets non-thinking responses that started to include inline reasoning without the delimiters, which contradicts the deployment contract for brief Instruct models.
Such reasoning is often marked with specific trigger words (e.g., “wait”, “actually”, “hmm”, “let me think”).
A multiplicative penalty is applied: shrinking the reward for correct responses, in proportion to the number of trigger words used.
Per-stage RL hyperparameters.
Data: Two RL data mixes are built: Instruct and Thinking. Both use public RLVR releases and proprietary additions, covering six capability domains: code, math, agentic tool use, instruction following, reasoning, and knowledge. The mixes are similar in size and share most sources. The main difference is that the Thinking mix replaces part of the pure-math data with a harder, long-form math subset, making it more difficult overall.

Code domain uses three main sources:

Competitive programming problems and tests.
Math-with-code dataset with Jupyter-style Python execution for code generation and evaluation (also counted under Math).
Proprietary realistic coding tasks in twelve languages (Python, Java, PHP, TypeScript, C#, JavaScript, JSX, Rust, Kotlin, Go, C++, CSS) covering different work types. Each task has a test suite used to define the reward signal.

Math is the largest single block in both mixes: 60,000 prompts (23%) in Instruct and 72,000 prompts (28%) in Thinking. It consists of three styles:

Pure math with no tools (from OLMo-3 Instruct RL for Instruct, OLMo-3 Thinking RL for Thinking).
Math with calculator tools (from Nemotron’s math-advanced-calculations release).
Math-with-code execution using the Python execution tool.

Agentic tool use includes:

xLAM-style function-calling RLVR data, single-step tool selection from an OpenAI-format registry.
Workplace-assistant benchmark, personal assistant tool use in a managed session.
Accounts for 14% (Instruct) and 12% (Thinking).

Instruction following involves:

Generic verifiable instruction-following dataset (machine-graded).
Structured-output dataset graded by JSON-schema validation.
Calendar-scheduling agent.
Sourced from Nemotron’s public RLVR release. Contributes 19% (Instruct) and 21% (Thinking).

Reasoning uses reasoning-gym, a public library of around 100 procedurally generated reasoning tasks (logic, sequences, spatial, simple games) with task-specific verifiers. This makes up 13% of both mixes.

Knowledge is covered by a multi-domain MCQA pool (physics, biology, math, humanities, computer science, engineering, chemistry, and more). This is the smallest domain: 9% (Instruct) and 4% (Thinking), and is intentionally downsampled to avoid harming instruction-following quality.
RL data mix composition by capability domain.
Evaluation

Pre Training
Pre-training evaluation results.
Despite activating only 2.5B parameters per token, Mellum 2 is competitive with 7B dense models on many benchmarks and exceeds them on several reasoning and code tasks (MMLU-Pro, BBH, GSM8K, MBPP, CRUXEval).

Instruct
Post-training evaluation, instruct (no-thinking) variants.
Coding:

Mellum 2-RL leads on EvalPlus with 78.4%, outperforming Qwen3.5–9B (71.8) and Seed-Coder-8B (73.8).
On LiveCodeBench v6, Mellum 2 instruct variant scores 37.2, trailing Qwen3.5–4B and 9B (51.0/63.7), but matches or beats other 7–14B baselines.
MultiPL-E: Mellum 2 is mid-pack, with Seed-Coder-8B (77.0) and Ministral-3–14B (71.5) ahead, due to their cross-lingual breadth.

Tool Use:

BFCL v3 (multi-turn function-calling): Mellum 2 instruct variant rises from 43.1 to 66.3 after RL, improving dramatically.
BFCL v4 (agentic tasks): No specific instruct scores reported, but RL improves tool use capabilities.

Math:

AIME: Mellum 2 scores 29.9 (SFT instruct) and 41.7 (RL instruct); RL provides substantial gains.

Knowledge:

MMLU-Redux: Mellum 2 achieves 78.1 (instruct), behind Qwen3.5–9B (91.1).
GPQA Diamond: Mellum 2 instruct scores 40.9 vs. Qwen3.5–9B’s 79.8.

Conversational:

Generic conversational benchmarks (IFEval, MixEval): Mellum 2 sits in the middle of the pack.
BS-Bench: Mellum 2 scores 14–24, well below Qwen3.5 series (56–70), due to compliance tendencies.

Safety:

HarmBench: Mellum 2-SFT is the safest instruct model with 8.4%, far safer than Ministral-3–14B (56.5) and Seed-Coder-8B (40.0).
XSTest: Mellum 2 trails largest baselines by about ten points, indicating over-refusal of some prompts.

Thinking
Post-training evaluation, thinking/reasoning variants.
Coding:

LiveCodeBench v6: Mellum 2-SFT-Thinking reaches 75.1 (top score in panel), 6.8 points ahead of Qwen3.5–9B-Thinking.
Algorithmic reasoning is fully realized with explicit thinking budget; function synthesis transfers from pre-training.

Tool Use:

BFCL v3: Mellum 2 thinking variant increases from 60.5 to 69.4 after RL, overtakes Qwen3.5–9B-Thinking (68.5).
BFCL v4 (agentic web-search & memory): Mellum 2-RL-Thinking leads at 45.6, outperforming Qwen3.5 family (42.9 / 42.7).

Math:

AIME: Mellum 2 moves from 20.0 (SFT-Thinking) to 58.4 (RL-Thinking); RL provides massive gains in reasoning trace.
GSM-Plus: Mellum 2 achieves 87.0 in RL-Thinking, close to Qwen3.5–9B-Thinking’s 90.7.

Knowledge:

MMLU-Redux: Mellum 2 scores 86.2 (thinking), behind Qwen3.5–9B (91.1).
GPQA Diamond: Mellum 2-Thinking scores 57.6 vs. Qwen3.5–9B’s 79.8 . Conversational:
JetBrains internal pairwise win-rate: Mellum 2-RL-Thinking leads at 69.5%, best among all (Ministral-3–14B-Thinking at 63.8, Qwen3.5–9B-Thinking at 56.7).
Generic benchmarks (IFEval, MixEval): Mellum 2 is mid-pack; code-aware prompts favor Mellum 2, broad chat favors Qwen3.5.
BS-Bench: Mellum 2 continues low scores (compliance vs. push-back), 14–24 vs. Qwen3.5’s 56–70.

Safety:

HarmBench: RL variant of Mellum 2 regresses to 23.1% harmful rate, worse than SFT but better than some baselines; indicates known alignment tax.
XSTest: Mellum 2 thinking variant over-refuses some safe prompts (trailing by ten points); item for joint optimization in future releases.

Paper

Mellum2 Technical Report 2605.31268

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

View original.

Exported from Medium on June 21, 2026.
