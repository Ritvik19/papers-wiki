# Papers Explained 589: Weak to Strong On Policy Distillation

Papers Explained 589: Weak to Strong On Policy Distillation

Papers Explained 589: Weak to Strong On Policy Distillation

Weak-to-Strong On-Policy Distillation improves a strong student by distilling from multiple weak models. Specifically, it constructs a…

Papers Explained 589: Weak to Strong On Policy Distillation

Weak-to-Strong On-Policy Distillation improves a strong student by distilling from multiple weak models. Specifically, it constructs a proxy teacher in logit space from a contrast pair of a positive and a negative model, both smaller than the student and cheap to obtain. Their logit difference isolates the capability direction, which is then added to the student’s own base model. The resulting proxy teacher thus couples this direction while staying distributionally adjacent to the student. The student then distills it by minimizing the per-token reverse KL on its own rollouts.

The project is available on GitHub.

Method
Overview of W2S-OPD.
Improving a strong student with supervision from weaker models is inherently difficult, since the supervision sources are weaker than the student, direct distillation constrains the student to a lower-capability policy and degrades the general ability it already possesses. To this end, a directional perspective is adopted. Instead of imitating a weak model directly, the capability direction that separates a stronger positive model from a weaker negative model is isolated — a signal that is largely disentangled from model scale and hence transferable across scales — and this direction is re-anchored onto the student’s base model. The resulting proxy teacher is simultaneously equipped with the target domain capability and distributionally adjacent to the student, which stabilizes optimization and preserves the student’s general ability.

Proxy Teacher Synthesis and Distillation

Suppose the student πS is initialized from a strong base model, while the available weak models form a contrast pair: a positive model m+ and a weaker negative model m−. Specifically, m+ is obtained either by applying domain-specific RL to its initialization m−, or taken as a stronger base model than m−.

What the two weak models agree on reflects their shared, limited ability, so subtracting their logits cancels this common component and retains precisely the direction along which m+ improves over m−. Adding this capability direction onto the strong base model therefore yields a proxy teacher that combines it with the student’s general strength while staying distributionally close to the student.

Formally, at each position t, the three models are conditioned on the prefix st to obtain the logit scores zbase, z+, and z−, and synthesize the proxy teacher as:

where α ≥ 0 is an amplification coefficient controlling the strength of the injected capability direction, and thus trades off signal strength against distributional proximity.

Given the constructed proxy teacher, W2S-OPD instantiates the OPD objective:

Instantiations of Positive and Negative Models
The three instantiations of the contrast pair in W2S-OPD.
Pre-RL and post-RL: The positive model m+ is a domain expert obtained by applying RL to a small base model, and the negative model m− is its pre-RL initialization, whose difference isolates the domain skill acquired through RL. This is a cheaper way of reducing the cost of training domain experts at the student’s own scale.
Smaller and larger: The positive and negative models are two off-the-shelf base models of different sizes (e.g., Qwen3–4B and Qwen3–0.6B). Their difference isolates the capability that emerges purely from scale and requires no additional training. This signal is already available in released models and can be used for free to further improve the capability of frontier models.
Correct and wrong hints: The positive and negative models are a single base model conditioned on a correct and a wrong solution hint of the identical format, respectively. Since the hint-conditioning is shared, their difference cancels the style shift it induces and isolates the instance-level direction toward the correct solution. Needing only one small model and a reference solution, which token-level supervision efficiently.

Experiments

Benchmarks:

AIME24, AIME25, HMMT25 (Feb), HMMT25 (Nov).
HumanEval+, MBPP+, LiveCodeBench-V6.
GPQA-Diamond for scientific reasoning (OOD)
IFBench for instruction following (OOD)

Models:

Qwen3–8B in non-thinking mode is used as the student πS; a frozen copy of the same checkpoint serves as the anchor.
In the pre-RL / post-RL setting, the positive model m+ is a Qwen3–4B domain expert obtained by applying GRPO to the Qwen3–4B base, for 500 steps on the level-6 subset of DeepMath-103K for math reasoning and for 300 steps on Eurus-RL-Code for code generation, and the negative model m− is its pre-RL initialization, i.e., the original Qwen3–4B model.
In the smaller/larger setting, the positive and negative models are the off-the-shelf Qwen3–4B and Qwen3–0.6B base models, requiring no additional training.
In the contrastive-hint setting, the positive and negative models share the Qwen3–4B base model, conditioned on a correct and a wrong solution hint of the identical format, respectively.

Distillation from Pre-RL/Post-RL:
Results for Pre-RL / Post-RL contrast setting.Performance on the math and code benchmarks over training steps.
W2S-OPD matches or surpasses the domain teacher, outperforms both SFT and OPD, with 11.4% (math) and 3.7% (code) average improvements, and learns faster and more stably than OPD.
In multi-teacher distillation (merging math and code experts), W2S-OPD consistently leads to better performance than OPD across all benchmarks.

Distillation from Smaller/Larger Base Models:
Results for Smaller and Larger contrast setting.
Even proxy teachers constructed from two weak models can improve the stronger student, with 6.0% (math) and 1.2% (code) absolute improvement.

Distillation from Single Model with Correct/Wrong Hints:
Results for contrastive hints setting.
Using correct/wrong hints from a single weak model (Qwen3–4B) improves the student by 1.4% (math) and 1.1% (code).

Amplification Coefficient Analysis:
Performance on the math and code benchmarks with different α.
Moderate values of the amplification coefficient α yield the best performance; too small injects weak signals, while too large makes supervision hard and harms performance.

Out-of-domain Generalization:
Results for OOD generalization on GPQADiamond and IFBench.
W2S-OPD transfers distilled skills well to unseen domains, improving performance on GPQA-Diamond (from 38.9 to 56.5, 2.1% better than OPD) and IFBench (1.1% better than OPD), while OPD sometimes erodes general ability.

Types of Tokens Reinforced:
Distribution of the top-1% highest-∆ tokens over the eight Schoenfeld episodes.A case study that the three contrasts strengthen different reasoning tokens.
Post-RL and hint contrasts reinforce planning and monitoring steps (reasoning framework), while scale contrast focuses on analysis and implementation (core solving steps). Hint contrast also emphasizes answer token.
These complementary emphases allow the student to improve reasoning by distilling different reasoning patterns.

Paper

Weak-to-Strong On-Policy Distillation 2607.26246

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

By Ritvik Rastogi on August 6, 2026.

Canonical link

Exported from Medium on August 22, 2026.
