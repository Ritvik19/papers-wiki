# Supervised Fine-Tuning

#concept

Supervised Fine-Tuning, or SFT, is a post-training method where a model learns from fixed example completions, usually supplied by humans, a dataset, or a teacher model.

In [[On SFT RL and On-Policy Distillation]], SFT is described as cheap and effective when the student is far below the teacher, but limited by the fixed sampling distribution used to construct the dataset. Unlike [[Reinforcement Learning]], SFT does not automatically compound improvements into future training samples.

[[Reinforcement Learning from Human Feedback]] positions SFT as the first post-training stage (instruction tuning) before preference optimization; the book argues SFT memorizes demonstrations while RL generalizes from contrastive completion-level feedback.

[[Papers Explained: SFT Conflicts, RL Coexists]] systematically compares SFT and RL across multi-task reasoning settings. It proves that multi-stage SFT leads to severe performance collapse (-23.1% below the base model) and single-task SFT degrades untrained tasks (-5.1%) due to large parameter norms, non-sparse updates, and dense norm-limited [[Gradient Interference]].

## Related

- [[Reinforcement Learning from Human Feedback]]
- [[Post-Training]]
- [[RLHF]]
- [[On SFT RL and On-Policy Distillation]]
- [[Papers Explained: SFT Conflicts, RL Coexists]]
- [[Task Coexistence]]
- [[Gradient Interference]]
- [[Parallel-RL]]
- [[Model Distillation]]
- [[Reinforcement Learning]]
- [[Synthetic Data]]
- [[Large Language Models]]
- [[Papers Explained - Advancing Search Augmented Language Models]]
- [[Papers Explained - Composer 2]]
- [[Papers Explained - Likelihood-Based Reward Designs for General LLM Reasoning]]
- [[Papers Explained - Sarvam 30B and Sarvam 105B]]
- [[Papers Explained 02 - BERT]]
- [[Papers Explained 08 - DeBERTa]]
- [[Papers Explained 11 - Layout LM v2]]
- [[Papers Explained 12 - LiLT]]
