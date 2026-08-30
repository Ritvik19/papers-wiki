# Verifier-Bounded Learning

#concept

Verifier-Bounded Learning describes training regimes whose ceiling is set by what a verifier or reward model can reliably grade, rather than by a fixed teacher distribution.

In [[On SFT RL and On-Policy Distillation]], this idea distinguishes [[Reinforcement Learning]] from teacher-bounded methods such as [[Supervised Fine-Tuning]] and [[On-Policy Distillation]]. RL can in principle exceed a teacher when the verifier can recognize better behavior than the teacher can demonstrate.

[[Papers Explained: Reward Hacking in Rubric-Based RL]] adds a sharper warning: the ceiling is not just verifier accuracy, but also rubric coverage. Stronger verifiers reduce [[Verifier Exploitation]], yet a policy can still perform worse under rubric-free holistic judging when the rubric over-rewards visible completeness and under-specifies absence-based quality failures.

## Related

- [[On SFT RL and On-Policy Distillation]]
- [[Reinforcement Learning]]
- [[Policy Gradient]]
- [[Reasoning Models]]
- [[Evaluation and Benchmarks]]
- [[Papers Explained: Reward Hacking in Rubric-Based RL]]
- [[Rubric-Based Reinforcement Learning]]
- [[Verifier Exploitation]]
- [[Reward Hacking]]
- [[Papers Explained - Likelihood-Based Reward Designs for General LLM Reasoning]]
- [[Papers Explained 227 - RAGAS]]
- [[Papers Explained 283 - Tulu V3]]
- [[Papers Explained 289 - V-STaR]]
- [[Papers Explained 306 - Critique Fine-Tuning]]
- [[Papers Explained 332 - Aya Vision]]
- [[Papers Explained 337 - Logic-RL]]
- [[Papers Explained 340 - CHASE]]
