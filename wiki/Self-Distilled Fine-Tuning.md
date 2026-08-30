# Self-Distilled Fine-Tuning

#concept

Self-Distilled Fine-Tuning, or SDFT, uses a model as its own teacher while conditioning the teacher path on privileged demonstrations or examples.

In [[On SFT RL and On-Policy Distillation]], SDFT is contrasted with [[On-Policy Self-Distillation]] because demonstrations may shift the teacher distribution less aggressively than giving the teacher the ground-truth answer. Its ceiling may still depend heavily on demonstration quality.

## Appearances

- [[Papers Explained 581: Rubric-Guided Self-Distillation]] — same-checkpoint teacher conditioned on rubric criteria distills into unconditioned student; extends self-distillation to rubric-graded domains without verifiers at train time.

## Related

- [[On SFT RL and On-Policy Distillation]]
- [[Model Distillation]]
- [[Supervised Fine-Tuning]]
- [[Rubric-Guided Self-Distillation]]
- [[On-Policy Distillation]]
