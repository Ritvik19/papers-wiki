Source URL: https://huggingface.co/blog/apriel-h1
Title: Apriel-H1: The Surprising Key to Distilling Efficient Reasoning Models

# Apriel-H1: The Surprising Key to Distilling Efficient Reasoning Models

Published November 19, 2025

Torsten Scholak, Oleksiy Ostapenko, Raymond Li, Luke Kumar, Joel Lamy-Poirier (ServiceNow-AI)

ServiceNow converted its 15B reasoning model to a Mamba hybrid, achieving 2.1x throughput with minimal quality loss. The key: a non-obvious insight about what data to distill on.

When MiniMax published their M2 post-mortem in October explaining why they abandoned efficient attention at 230B scale, the narrative briefly became "efficient attention is dead." Within days, Kimi Linear proved otherwise; the real lesson is that it depends on your constraints. ServiceNow's constraint: they had a strong 15B reasoning model and needed to make it efficient without starting over, with no budget for 20T-token pretraining or day-one architectural co-design. The question: can you retrofit efficiency into an existing model through distillation? The answer is yes, but only if you ignore intuition about what data to use.

## What was built

The Apriel-H1 family: seven checkpoints spanning 25-40 Mamba layers (out of 50 total), showing the complete efficiency-quality frontier. The flagship, Apriel-H1-15b-Thinker-SFT, achieves 2.1x throughput with minimal quality loss after 76.8B training tokens:

| Benchmark | Full-attention teacher | Apriel-H1-15b-Thinker-SFT |
| --- | --- | --- |
| MATH500 | 0.90 | 0.92 |
| MTBench | 8.30 | 8.58 |
| GSM8k | 0.97 | 0.95 |
| GPQA | 0.59 | 0.55 |
| AIME24 | 0.70 | 0.65 |

The complete efficiency frontier: the flagship H-30-SFT (Apriel-H1-15b-Thinker-SFT) used 76.8B total tokens for 2.1x throughput at 0.76 average score; the more aggressively converted H-40 variant used 136.5B tokens for 3.4x throughput. For reference, NVIDIA's Nemotron-Nano-9B-v2 achieves 4.6x at 0.77 score but required training from scratch with orders of magnitude more compute.

## The non-obvious insight

The initial assumption was that distilling on pretraining data, rounded out with some SFT, would work, since the new Mamba layers have never seen data and need to learn general-purpose token mixing from scratch. That didn't work; distilled hybrids lost reasoning quality, sometimes dramatically, whether using pure pretraining data or a pretraining/SFT mix.

What actually worked: high-quality reasoning traces from the teacher's SFT dataset. Distilling a reasoning model isn't about transferring general next-token prediction (the base model already has that); what's being preserved is the teacher's specific, fragile multi-step reasoning patterns, which emerge from attention mechanisms like retrieval heads and induction heads connecting premises to conclusions many steps later. Replacing attention with Mamba's linear recurrence disrupts these mechanisms, and the hybrid must discover new paths to the same reasoning outcomes, which requires explicit examples where reasoning structure is visible and correct: multi-step math proofs, coding tasks with clear logical dependencies, scientific analysis with detailed explanatory chains. Pretraining data is too noisy and diffuse for the reasoning signal to survive.

The team also used reverse KL divergence (temperature 1) rather than forward KL for distillation, which won consistently: since training happens on problems where the teacher has high confidence and clear structure, reverse KL's mode-seeking behavior encourages the student to commit to those high-confidence predictions. The overall principle: match your distillation data to the capability you're preserving, not the capability you're building.

## Staged distillation procedure

1. **Identify least-important layers.** A Leave-One-Out (LOO) analysis on MMLU (remove each layer, replace with identity, measure the drop) ranks layers by importance. The bottom 25 are replaced with Mamba-in-Llama (MIL) initialized mixers and distilled end-to-end, producing the H-25 checkpoint.
2. **Progressive conversion beyond 25 layers.** LOO breaks down past 25 layers, since layers unimportant in isolation become critical in combination. A dynamic heuristic, MIL-Mamba-Replacement (MMR), initializes a Mamba mixer with MIL for each remaining attention layer, runs 100 training steps, and records the distillation loss; layers converging to lower loss are judged "easier" to replace. Conversion proceeds incrementally: 25 → 27 → 30 → 34 → 37 → 40 Mamba layers, with each checkpoint distilled from the previous.
3. **End-to-end training on SFT data.** After reaching the target Mamba layer count, a final SFT pass runs until reasoning performance stabilizes; after 55.9B distillation tokens and 20.9B SFT tokens, this produced the final Apriel-H1-15b-Thinker-SFT model.

## Fast-LLM

Built on Fast-LLM, ServiceNow's open-source (Apache 2.0) training framework, whose core principle is that transformer decoder blocks should be modular: attention and Mamba are different implementations of the same "mixing" interface and can be swapped freely via config, e.g.:

```yaml
decoder:
  type: "pattern"
  blocks:
    attention_block:
      mixer: {type: "attention", heads: 32, head_groups: 8, head_size: 128}
      mlp: {type: "gated", activation: "silu"}
    mamba_block:
      mixer: {type: "mamba", d_inner: 4096, state_size: 16, dt_rank: 16}
      mlp: {type: "gated", activation: "silu"}
  num_blocks: 50
  pattern: ["attention_block", "attention_block", "mamba_block", ...]
```

For Apriel-H1-15b-Thinker-SFT: 30 `mamba_block` and 20 `attention_block`, placed by importance. Distillation is configured the same way, via `distillation_model: teacher` and `distillation_loss_implementation: reverse_kl`.

## FAQs (selected)

- **Why release all checkpoints?** Optimal depends on constraints; H-30 offers the best balance, H-40 maximizes throughput for latency-critical workloads.
- **Why only Mamba-1?** Proven distillation track record, strong empirical performance, and simple to implement, letting the team focus on the data question first.
- **Why not MOHAWK's multi-stage procedure?** It showed no significant advantage over Mamba-in-Llama initialization plus knowledge distillation in preliminary experiments.
- **Why only SFT the H-30 model?** To validate that distilled hybrids can be improved via standard post-training; other checkpoints are pure distillation but can be fine-tuned similarly.
- **Why not explore RL?** Scoping decision, to isolate whether reasoning transfers via knowledge distillation alone (yes); RL is expected to close remaining quality gaps in future iterations.

## Production reality

Apriel-H1 is implemented in Hugging Face Transformers (a new model class with interchangeable attention and Mamba layers) and vLLM (using recent Mamba cache operations for continuous batching, prefix caching, and chunked prefill); the vLLM plugin was pending final legal approval to open-source at time of writing. Deploying hybrids today still has rough edges: tooling is maturing fast but isn't turnkey, and teams should expect to write custom code and validate numerical behavior carefully.

## Citation

```bibtex
@article{apriel-h1-2025,
  title={Apriel-H1: Towards Efficient Enterprise Reasoning Models},
  author={SLAM Lab, ServiceNow},
  journal={arXiv preprint arXiv:2511.02651},
  year={2025}
}
```
