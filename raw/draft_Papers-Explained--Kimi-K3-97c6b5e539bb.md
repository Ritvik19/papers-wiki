# Papers Explained: Kimi K3

Papers Explained: Kimi K3

Papers Explained: Kimi K3

Kimi K3 is a 2.8T parameter Mixture-of-Experts model with 104 billion activated parameters, native vision capabilities, and a…

Papers Explained: Kimi K3

Kimi K3 is a 2.8T parameter Mixture-of-Experts model with 104 billion activated parameters, native vision capabilities, and a 1-million-token context window. Kimi K3 is built on Kimi Delta Attention and Attention Residuals, which improve information flow across sequence length and model depth. Together with Stable LatentMoE, which effectively activates 16 of 896 routed experts per token, and refined training and data recipes, these advances yield an approximately 2.5× improvement in overall scaling efficiency over Kimi K2.

The model is available at HuggingFace.

Model Architecture
The Kimi K3 architecture.
The Kimi K3 architecture is designed to scale information flow along three complementary dimensions: sequence length, network depth, and model width.

Along the sequence dimension, Hybrid Attention combines three Kimi Delta Attention (KDA) layers with one Gated MLA layer in each block, providing an efficient mechanism for long-context token mixing while retaining selective high-capacity attention.
Along the depth dimension, Attention Residuals (AttnRes) enable each module to selectively retrieve representations from the embedding, the current block, and preceding blocks, extending information access beyond conventional sequential residual accumulation.
Along the width dimension, each attention layer is followed by a Stable LatentMoE layer that performs sparse channel mixing, effectively activating 16 of 896 routed experts for each token.
For native vision, MoonViT-V2 encodes images and videos, and a lightweight projector maps the resulting visual features into the shared embedding space before backbone processing.

Together with Per-Head Muon, these components provide a unified architecture for scaling information flow across tokens, layers, and channels.
Architectural comparison between Kimi K2 and Kimi K3.
Pre Training

Kimi K3 is pre-trained on a curated corpus spanning four primary text domains: Web Text, Code, Mathematics, and Knowledge together with a large-scale vision corpus. The vision data covers captions, interleaved image–text documents, OCR, perception, video, and visual coding data.

Each text data domain is filtered by a combination of rule-based heuristics, classifier-based quality scoring, and deduplication, with domain-specific sampling rates determined by ablation studies on smaller models. Following the rephrasing recipe of Kimi K2, knowledge and mathematics corpora are rephrased with style and perspective-diverse prompting, chunk-wise autoregressive generation, and fidelity verification against the source documents.

The vision corpus follows the taxonomy of Kimi K2.5, combining open-source collections with in-house pipelines for filtering, synthesis, and deduplication. During training, coordinate supervision is provided in both absolute and normalized ([0,1]) formats, enabling precise and resolution-robust localization. In addition to classical text-captioned images, programmatic multimodal data is substantially scaled up, coupling code snippets with their rendered visuals across domain-specific formats including SVG, 3D assets, Webpage, Game, and CAD schematics.

Kimi K3 adopts a native multimodal training strategy in which language and vision are jointly optimized from the start of training, rather than grafting a vision encoder onto a pre-trained language model through a post-hoc alignment stage. Under this paradigm, visual and textual tokens are interleaved within a single next-token prediction objective, enabling the shared backbone to learn unified multimodal representations from the outset.

The model is optimized using the Per-Head Muon optimizer together with the weight-clipping mechanism introduced in Kimi K2, while adopting Quantile Balancing for MoE load balancing. A cosine learning rate schedule is used with a 1% linear warmup. Weight decay is set to 0.1 throughout.

Kimi K3 uses no explicit positional embedding (NoPE), and instead encodes positional information implicitly through the recurrent gating and decay mechanism of KDA. As a result, the model extrapolates directly to 1M-token contexts without any positional-encoding modification, such as RoPE rescaling or interpolation.

The context window grows from 8K to 64K tokens during pre-training, and from 256K to 1M tokens during the cooldown phase.

Post Training

Supervised Fine-Tuning

The SFT dataset for Kimi K3 is expanded, substantially broadening its coverage of complex agentic tasks. Data trajectories are synthesized using domain-specialized models from the prior Kimi series, followed by multi-stage verification and human-in-the-loop annotation. To represent these complex agentic trajectories consistently, all data is serialized using an XTML-based chat template (eXtensible Token Markup Language). In addition, quantization-aware training (QAT) is applied from the SFT stage onward, with MXFP4 weights and MXFP8 activations.

Reinforcement Learning

Reinforcement learning is scaled across three broad domains, each encompassing a wide spectrum of sub-tasks, and a single expert is trained for each domain at every reasoning effort level:

general tasks, spanning general experience, vision, reasoning, faithfulness, search capabilities, and knowledge work tasks.
general agents, spanning long-horizon assistant tasks, deep research, and paragraph-level writing.
coding agents, spanning software engineering (SWE), coding experience, kernel tasks, and web development.

To mitigate the long-tail latency that intensifies in long-horizon tasks, the partial rollout scheme from the synchronous RL framework is extended. During the rollout phase of each iteration, K completions are sampled for each of N prompts, maintaining an active workload of N × K trajectories. Rather than waiting for all rollouts to terminate, the generation phase pauses as soon as a fraction λ ∈ (0, 1) of trajectories completes (i.e., λN K), allowing policy optimization to proceed without execution stragglers. Paused rollouts are enqueued and prioritized for resumption at the start of the next iteration, powered by the sandbox infrastructure. Once all K responses for a prompt complete, they are immediately dispatched for policy optimization, which follows the algorithm in Kimi K2.5.

Under this partial rollout scheme, an individual long-horizon trajectory naturally spans multiple iterations, introducing data staleness that threatens training stability. The policy optimization algorithm inherently tolerates such an extreme off-policy regime through a per-token regularization. By constraining policy updates within a localized neighborhood, this regularization enables the algorithm to robustly handle highly stale data and sustains training stability.

To fine-tune reasoning effort while maximizing token efficiency, a per-problem budget control mechanism is implemented during RL. Each problem x is associated with an initial token budget b0(x) estimated from the cold-start model, and the task reward is overridden with −1 for trajectories whose total token budget T(y) exceeds a scaled threshold τ·b0(x). For general tasks, T(y) measures the number of thinking tokens, whereas for agentic tasks, T(y) accounts for the cumulative output tokens, including both reasoning traces and tool-call arguments. Training follows a stage-wise curriculum over the budget multiplier τ. A max-budget variant is first trained with a relatively large τ, while still capping the maximum budget to suppress excessive overthinking. τ is then annealed to smaller values to obtain the high- and low-effort expert models. The adjustment of τ is configured per domain under human-in-the-loop guidance. Trajectories produced by the resulting experts at all reasoning levels are jointly collected for supervised fine-tuning and multi-teacher on-policy distillation.

For non-verifiable general tasks, an Agentic Generative Reward Model is adopted which follows a mandatory protocol:

read the outcome, product, or text output
generate a rubric
score each candidate against the rubric
record the rubric-assigned scores in a scorepad.

Multi-Teacher On-Policy Distillation

Multi-Teacher On-Policy Distillation (MOPD) is adopted to consolidate domain-specialized capabilities across varying reasoning efforts into a unified model. During training, for a given domain d and a sampled reasoning effort level e ∈ {low, high, max}, optimization is guided by the corresponding teacher model π(d,e) among the nine experts. Given an input query x and the prefix response y<t, the per-token OPD reward evaluated on yt between the teacher π(d,e) and the student πθ is defined as:

where sg(·) denotes the stop-gradient operator, and Rmax > 0 is a clipping threshold to constrain extreme advantage signals, thereby stabilizing RL training. This dense reward signal seamlessly integrates into our RL framework, naturally enabling infrastructure-level optimizations such as partial rollout training for long-horizon tasks.

RL Task Synthesis and Agentic Environments

Unified White-Box RL Environment

Training with a single fixed agent harness can cause a model to overfit to a particular tool schema, system prompt, context management mechanism, or interaction protocol. To address this, a unified white-box RL environment is developed that represents an agent harness as a collection of configurable, composable modules, including tool interfaces, system prompts, context management strategies, skills, memories, subagents, and other components. Thus, the environment can instantiate mainstream harnesses such as Kimi Code, Claude Code, Codex, OpenClaw, and Hermes, as well as entirely new ones.

Knowledge-Graph-Guided Task Synthesis
Overview of knowledge-graph-guided task synthesis.
A self-evolving, hierarchically organized knowledge graph is constructed and expanded recursively by agents through web-scale exploration.

Expansion starts from coarse-grained seeds. Agents explore, identify related concepts to minimize duplication, and continually add finer nodes until atomicity is reached (directed acyclic graph, edges from coarse to fine).

Nodes are sampled individually/combined for targeted domain/task distribution. Keywords from sampled nodes and ancestral context guide searches, and retrieved materials are synthesized into training tasks by agents.

Verifiable Problems in Agentic Environments

Kimi K3 is trained on verifiable tasks: multi-step information search (planning, evidence gathering, producing verifiable answers); professional workflows (e.g., investment banking, data analysis, legal practice, decomposing requests, tool operation in sandbox, deliverables over many steps). Visual reasoning tasks are multi-step, with a Python interpreter sandbox. The agent manipulates images, performs computations, verifies results, and learns iteratively to improve complex visual reasoning

Kernel Optimization Tasks

To enhance GPU kernel optimization, a large task suite is constructed ranging from single-operator to fused mega-kernels, using repositories like Flash Linear Attention.

The suite covers diverse GPU programming approaches (CUDA, Triton, CuTe DSL, Gluon, ThunderKittens, TileLang), architectures, and numerical formats (BF16, FP8, FP4).

Rewards: PyTorch reference checks correctness; performances are scored vs expert implementation (matching gets 0.5, hardware roofline pushes reward toward 1), zero reward for excessive error.

A hacking-detection system penalizes reward-hacking strategies (e.g., CUDA graph replay, input caching, precision reduction), extended as new hacks appear.

Personal Assistant Tasks

Mock implementations of popular apps (Gmail, Notion, Slack, Canvas) are developed for realistic, reproducible, large-scale simulation without API/rate limits.

Complex tasks mimic professional workflows (HR, legal, finance), set in persistent environments spanning multiple simulated days, dozens of interdependent events, thousands of tool calls, millions of tokens.

Events have deterministic or LLM-based evaluation criteria. The workspace is built by agents searching and transforming web materials into a task-relevant environment.

The RL framework is extended to model complex event streams and world-state transitions for such living environments.

Autonomous Execution Tasks (AET)

AETs train long-horizon agent intelligence via verify-in-the-loop optimization: tasks specify initial state, goal, tool-based action space, budgets, independent verifiers.

Agents see objectives, context, constraints, verification interfaces, not trajectories or procedures. They must autonomously do task decomposition, tool selection, planning, error recovery, termination; rewards are given by verifier evaluation of the final state.

Multiple verifier types support diverse environments (black-box system replication, quantitative discovery, tax auditing). Agents iterate by submitting solutions, receiving feedback, and refining strategies.

Reward hacking is mitigated via agent-verifier isolation, public diagnostic/hidden scenario verifiers, penalty rewards, limited submission budgets.

Web Development Tasks

Expert-curated suite covers typical web development, from single-line to multi-paragraph specs. Artifacts include websites, games, 3D/WebGL scenes, visualizations, SVGs, full-stack apps. Each task runs in a containerized sandbox, rolled out under diverse scaffolds to prevent overfitting.

Rewards: deterministic checks (functional testing, structural/pixel similarity), zeroed if the build fails or output is faked; model judging (code inspection, output analysis by models.

Evaluations
Performance comparison of Kimi K3 against proprietary and open-source models.
Kimi K3 closely trails the top proprietary models Claude Fable 5 and GPT-5.6 Sol, but consistently outperforms Claude Opus 4.8, GPT-5.5, and GLM-5.2 across almost all benchmarks.

Reasoning & Knowledge:

Competitive performance at the graduate level (scoring 93.5% on GPQA Diamond).
However, Kimi K3 lags on research-level tasks, such as HLE-Full and CritPt, suggesting ongoing challenges at the higher end of reasoning.

Coding:

Delivers state-of-the-art performance on ProgramBench (77.8%) and SWE-Marathon (42.0%, 7 points ahead of Claude Fable 5).
Nearly matches GPT-5.6 Sol on Terminal-Bench 2.1 (88.3% vs 88.8%).
Consistently ranks ahead of Claude Opus 4.8 and GPT-5.5 on coding benchmarks, second only to Claude Fable 5 on long-horizon tasks like FrontierSWE.

Agentic:

Achieves leading results on multiple agentic benchmarks — BrowseComp (91.2%), DeepSearchQA (95.0% F1), ResearchRubrics (76.2%), MCPMark-Verified (94.5%), AutomationBench (30.8%), SpreadsheetBench 2 (34.8%), τ 3-Banking (33.4%), Harvey Lab-AA (94.6%).
Only trails Claude Fable 5 in a few Elo-rated knowledge-work suites, but remains competitive elsewhere.

Vision:

Strong multimodal (vision-language) capabilities, enhanced by Python tool augmentation (e.g., Math-Vision: 94.3% to 97.8%, ZeroBench-main: 23.0% to 41.0%).
Achieves top or near-top results: highest on OmniDocBench (91.1%), second on WorldVQA (51.0%), ties Claude Fable 5 on ZeroBench-main.

Paper

Kimi K3: Open Frontier Intelligence 2607.24653

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

View original.

Exported from Medium on August 22, 2026.
