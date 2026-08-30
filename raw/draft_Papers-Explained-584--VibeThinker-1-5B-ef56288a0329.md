# Papers Explained 584: VibeThinker-1.5B

Papers Explained 584: VibeThinker-1.5B

Papers Explained 584: VibeThinker-1.5B

VibeThinker-1.5B, a 1.5B-parameter dense model developed using an innovative post-training methodology centered on the “Spectrum-to-Signal…

Papers Explained 584: VibeThinker-1.5B

VibeThinker-1.5B, a 1.5B-parameter dense model developed using an innovative post-training methodology centered on the “Spectrum-to-Signal Principle (SSP)”, systematically enhances output diversity by first employing a “Two-Stage Diversity-Exploring Distillation” in the SFT phase to generate a broad spectrum of solutions, followed by the “MaxEnt-Guided Policy Optimization (MGPO)” framework in the RL phase to amplify the correct signal.

Methodology

The Spectrum-to-Signal Principle for SFT-RL Synergy
The Training Pipeline of VibeThinker-1.5B.
The “Spectrum-to-Signal Principle (SSP)” is a theoretical framework that redefines the roles of and the synergy between SFT and RL. In SSP, the two stages are assigned distinct, complementary objectives.

The Spectrum Phase (SFT): The primary goal of SFT is not to converge on a single optimal answer, but to generate a rich and diverse “spectrum” of plausible solutions. This phase maximizes the model’s Pass@K metric, effectively creating a broad “candidate space” of correct answers. A model with high Pass@K provides a richer foundation for exploration, thereby raising the upper bound of what RL can achieve.
The Signal Phase (RL): The role of RL is then to identify and amplify the correct “signal” from within this pre-established spectrum. By receiving reward signals, the RL phase learns to increase the generation probability of the most correct and effective answers from the diverse pool provided by the SFT phase.

This principle posits that an SFT checkpoint optimized for diversity (Pass@K) is a superior prerequisite for RL, as it presents the RL algorithm with a more fertile ground for optimization compared to a narrow, Pass@1-optimized model.

Diversity-Exploring Distillation

To implement the spectrum phase of SSP, a two-stage methodology is proposed: “Domain-Aware Diversity Probing” to identify specialist models, followed by “Expert Model Fusion” to synthesize a unified, diversity-maximized SFT model.

The knowledge space is first partitioned into 𝑁 distinct subdomains, S = {𝑆1, 𝑆2, . . . , 𝑆𝑁}. For each subdomain 𝑆𝑖, a capable LLM is employed to automatically construct a specialized probing set, 𝐷𝑖 = {(𝑞𝑖 𝑗, 𝑎𝑖 𝑗) | 𝑗 = 1, . . . , |𝐷𝑖|}, where 𝑞𝑖 𝑗 is a problem and 𝑎𝑖 𝑗 its ground-truth answer. During SFT training, intermediate model checkpoints 𝑀𝑡 (saved every 𝑘 steps) are periodically evaluated on each probing set 𝐷𝑖 using the Pass@K metric, yielding a score 𝑃𝑖(𝑡). The checkpoint that maximizes this metric for a given subdomain is selected as the specialist model M∗i.

M∗i. = arg max_𝑡 𝑃𝑖 (𝑡)

This process yields a set of 𝑁 diversity-maximizing specialist models, {𝑀∗1, 𝑀∗2, . . . , 𝑀∗𝑁}, each excelling at generating diverse solutions within its respective subdomain.

Having identified the specialist models, they are synthesized into a single, comprehensive SFT model optimized for the spectrum phase. This fused model, MSFTMerge, is constructed as a weighted linear combination of the specialist model parameters, where the weights 𝑤𝑖 are non-negative and sum to unity. In the implementation for VibeThinker-1.5B, an unweighted averaging scheme is employed where 𝑤𝑖 = 1/𝑁 for all 𝑖, ensuring equitable integration of the diverse capabilities from all subdomains.

MaxEnt-Guided Policy Optimization (MGPO)

MaxEnt-Guided Policy Optimization (MGPO) is a novel framework that leverages information-theoretic principles to dynamically identify and prioritize the most pedagogically valuable problems for on-policy learning. This process induces a binary distribution over the outcomes (correct vs. incorrect) for question 𝑞. Let 𝑝𝑐 (𝑞) be the empirical probability of a correct answer, derived from the 𝐺 rollouts:

where I(·) is the indicator function. According to the principle of maximum entropy, this distribution is most “uninformed” or uncertain when its entropy is maximized. For a binary distribution, the maximum entropy occurs when 𝑝𝑐 (𝑞) = 0.5. In this state, the model is completely uncertain about the correct answer; it is neither consistently correct nor consistently wrong. This state of maximum uncertainty represents a problem with optimal “exploratory value”. Such a problem lies at the very edge of the model’s current capabilities, making it an ideal candidate for policy optimization.

A targeted weighting scheme explicitly measures and penalizes deviation from the ideal maximum-entropy state, called Entropy Deviation Regularization 𝐷ME (𝑝𝑐 (𝑞)∥𝑝0). It is defined as the Kullback-Leibler (KL) divergence between the observed accuracy 𝑝𝑐 (𝑞) and the target maximum-entropy distribution 𝑝0 = 0.5:

Using this distance, a weighting function, 𝑤ME, assigns the highest weight to questions where the accuracy is closest to 0.5 and exponentially suppresses the weight as the accuracy moves towards 0 or 1:

This weighting function is applied directly to the advantage term within the GRPO objective. The updated advantage for each rollout 𝑗 in a group for question 𝑞 is:

Training Data

VibeThinker-1.5B is based on Qwen2.5-Math-1.5B, released in September 2024 and it’s training primarily used publicly available open-source datasets, supplemented by a small amount of proprietary synthetic data to enhance domain-specific coverage and robustness. To prevent information leakage and ensure genuine generalization, rigorous data decontamination procedures were applied in both the Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) stages. These procedures included:

Text Standardization and Preprocessing: Texts were normalized by removing irrelevant punctuation, symbols, and unifying letter cases to reduce noise and improve matching accuracy.
Semantic Decontamination: 10-gram matching was used to identify and exclude training samples that overlapped semantically with evaluation sets. Reducing n-gram length increased sensitivity to local semantic similarities, making decontamination more stringent. These steps significantly reduced risks of information leakage, ensuring model evaluations (e.g. mathematical reasoning and code generation benchmarks) accurately reflected true generalization and reasoning capabilities.

Evaluation
Performance of VibeThinker-1.5B on Core Benchmarks.
VibeThinker-1.5B significantly outperforms its base model Qwen2.5-Math-1.5B across all domains (e.g., AIME25: 74.4 vs. 4.3; HMMT25: 50.4 vs. 0.6; LiveCodeBench V5: 55.9 vs. 0; GPQA: 46.7 vs. 16.4).
Outperforms 3B SmolLM and Qwen3–1.7B on math and coding benchmarks (e.g., AIME25: 74.4 vs. 36.7/36.8; HMMT25: 50.4 vs. 26.0; LiveCodeBench V5: 55.1 vs. 27.6; V6: 51.1 vs. 26.9)
Performance of VibeThinker-1.5B on Core Benchmarks.
Despite having 10–100x fewer parameters, VibeThinker-1.5B matches or exceeds larger proprietary and open-source models on complex mathematics benchmarks, and is consistently superior to DeepSeek R1 across all datasets.
It offers scores comparable to Gemini 2.5 Flash and O3-mini-Medium, and superior to Magistral Medium and Claude Opus 4 on AIME24 and AIME25.
VibeThinker-1.5B achieves coding benchmark scores comparable to Magistral Medium and Claude Opus 4, but a slightly larger gap exists compared to mathematical benchmarks, attributed to the base model’s limited code pre-training.
A substantial gap of 20–40 points remains between VibeThinker-1.5B and leading large models, highlighting intrinsic limitations of small-scale models in broad domain knowledge.
Performance of VibeThinker-1.5B on Core Benchmarks.
VibeThinker-1.5B surpasses much larger non-reasoning models on challenging math benchmarks and most code benchmarks, showing the reasoning potential of well-designed small models.
Still lagging in encyclopedic knowledge (GPQA) compared to larger models, confirming a persistent limitation.

Paper

Tiny Model, Big Logic: Diversity-Driven Optimization Elicits Large-Model Reasoning Ability in VibeThinker-1.5B 2511.06221

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

View original.

Exported from Medium on June 21, 2026.
