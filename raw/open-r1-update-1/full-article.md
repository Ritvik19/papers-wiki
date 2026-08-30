Source URL: https://huggingface.co/blog/open-r1/update-1
Title: Open-R1: Update #1

# Open-R1: Update #1

Team Article. Published February 2, 2025

Leandro von Werra, Lewis Tunstall, Quentin Gallouedec, Guilherme Penedo, Edward Beeching, Anton Lozhkov, Brigitte Tousignant, Daniel van Strien (open-r1)

It's been two weeks since the release of DeepSeek R1 and just a week since the open-r1 project started to replicate the missing pieces: the training pipeline and the synthetic data. This post summarizes progress, what the team learned about DeepSeek-R1, and cool projects the community has built.

## Progress after 1 week

### Evaluation

The first step in reproduction is verifying evaluation scores match. Reproduced MATH-500 results (HF lighteval vs. DeepSeek reported):

| Model | MATH-500 (HF lighteval) | MATH-500 (DeepSeek Reported) |
| --- | --- | --- |
| DeepSeek-R1-Distill-Qwen-1.5B | 81.6 | 83.9 |
| DeepSeek-R1-Distill-Qwen-7B | 91.8 | 92.8 |
| DeepSeek-R1-Distill-Qwen-14B | 94.2 | 93.9 |
| DeepSeek-R1-Distill-Qwen-32B | 95.0 | 94.3 |
| DeepSeek-R1-Distill-Llama-8B | 85.8 | 89.1 |
| DeepSeek-R1-Distill-Llama-70B | 93.4 | 94.5 |

DeepSeek-R1 responses in the OpenThoughts dataset are extremely long: average response length is ~6,000 tokens, with some responses over 20,000 tokens (roughly 10+ pages). This length will make GRPO training challenging since long completions require significant GPU memory for activations/gradients during the optimization step. An open-r1 evaluation leaderboard was created so the community can follow reproduction efforts.

### Training pipeline

GRPO (Group Relative Policy Optimization) was integrated into TRL (version 0.14), enabling training any model with one or multiple reward functions/models. The implementation integrates with DeepSpeed ZeRO 1/2/3 for scaled training and uses vLLM for fast generation (the primary bottleneck in online training).

```python
from datasets import load_dataset
from trl import GRPOConfig, GRPOTrainer

dataset = load_dataset("trl-lib/tldr", split="train")

def reward_len(completions, **kwargs):
    return [-abs(20 - len(completion)) for completion in completions]

training_args = GRPOConfig(output_dir="Qwen2-0.5B-GRPO", logging_steps=10)
trainer = GRPOTrainer(
    model="Qwen/Qwen2-0.5B-Instruct",
    reward_funcs=reward_len,
    args=training_args,
    train_dataset=dataset,
)
trainer.train()
```

There are still limitations around high memory usage; profiling and reduction work is ongoing.

### Synthetic data generation

R1's report showed the main model can generate synthetic reasoning traces that smaller fine-tuned models can learn from with similar gains. Scaling generation efficiently is the main challenge. On 2x 8xH100 nodes with vLLM, throughput was suboptimal (only 8 parallel requests, since GPU KV cache fills too quickly, triggering preemption). Switching to 4x 8xH100 nodes (32 GPUs total) left enough spare VRAM for 32 parallel requests with minimal rescheduling. Switching from batched inference to streaming requests (capping active requests at 500, launching a new one as soon as one completes) stabilized GPU utilization significantly versus waiting for the slowest request in a batch to finish.

### Outreach

Wide media interest followed: Lewis appeared live on CNN, Thom appeared on Bloomberg, Leandro discussed on NPR's Money Planet.

## What have we learned about DeepSeek-R1?

The second week after release saw significant market reactions and responses from AI labs (OpenAI's Sam Altman and Mark Chen, Anthropic's Dario Amodei commenting on export controls), plus multiple platforms (Dell, AWS Bedrock/SageMaker, Hyperbolic, Together AI, Fireworks AI) making DeepSeek models available.

On the proclaimed ~$5.5M training cost of V3/R1, back-of-envelope calculations from several researchers (Tom Goldstein, Reiner Pope, Lukas Beyer, SemiAnalysis) suggest the number is roughly the right order of magnitude, though the exact figure remains unverified pending a full reproduction.

Speculation surfaced (e.g. in the Financial Times) that DeepSeek may have used OpenAI outputs to train its models; the consequences of these allegations were unclear at the time of writing.

## Community

Numerous reproduction efforts appeared at smaller scale: Will Brown reproduced a minimal GRPO training curve with Llama 1B in TRL; TinyZero showed the "aha moment" for under $30 with a 3B base model; Philipp Schmid released a Mini-R1 tutorial reproducing the same effect; HKUST researchers showed emergence of reasoning with a 7B math model; the Evolving LLM lab started a multimodal R1 variant; and a project explored using R1 for graph extraction from text.

New datasets released by the community include `bespokelabs/Bespoke-Stratos-17k`, `open-thoughts/OpenThoughts-114k`, `cognitivecomputations/dolphin-r1`, `ServiceNow-AI/R1-Distill-SFT`, `NovaSky-AI/Sky-T1_data_17k`, and `Magpie-Align/Magpie-Reasoning-V2-250K-CoT-Deepseek-R1-Llama-70B`.

## What's next?

The team is finishing the training pipeline, testing it on smaller models, and using the scaled inference pipeline to generate high-quality datasets.
