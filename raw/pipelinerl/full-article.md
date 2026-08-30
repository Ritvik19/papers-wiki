Source URL: https://huggingface.co/blog/pipelinerl
Title: PipelineRL

# PipelineRL

Published April 25, 2025

Alexandre Piché, Rafael Pardinas, Ehsan Kamalloo, Dzmitry Bahdanau (ServiceNow)

ServiceNow open-sourced PipelineRL, an experimental RL implementation that tackles a fundamental challenge in large-scale reinforcement learning with LLMs: the trade-off between inference throughput and on-policy data collection. Its key innovation is inflight weight updates during RL training, allowing constantly high inference throughput while minimizing the lag between the weights used for rollouts and the most recently updated model weights, for fast and stable RL training.

The post shows that (1) inflight weight updates do not harm the training process, and (2) PipelineRL achieves competitive results compared to Open-Reasoner-Zero while using a simpler RL algorithm. It also presents the modular PipelineRL architecture that facilitates trying new inference/trainer combinations.

## Conventional RL vs PipelineRL

In conventional RL, there's a trade-off between high-throughput inference and on-policy data collection: inference servers need large batch sizes to be efficient, which means generating data for multiple policy-optimization steps, but each optimization step increases the lag between the current policy and the data collected with the (older) inference policy, progressively making the data more off-policy. On-policy learning requires data for a single optimization step, but producing small amounts of data with many GPUs is inefficient (small per-GPU batch size), and batch size further degrades as the inference server finishes short sequences and is left with only a few long ones in flight.

PipelineRL remedies this via inflight weight updates: weights in inference servers are updated after each optimizer step without ever stopping inference; inference is paused only for the brief time needed to receive the new weights. This lets the inference server constantly maintain the optimal batch size while keeping data on-policy or near on-policy, improving both GPU utilization and learning effectiveness.

## Results

PipelineRL was used to train 7B and 32B models on the Open-Reasoner-Zero dataset. Learning curves show PipelineRL matches or exceeds Open-Reasoner's performance on AIME 2024 and MATH 500. Notably, the RL implementation is much simpler than Open-Reasoner-Zero: it's a simplified GRPO variant without a value function. Trust region importance-weight clamping was not needed for stable training, nor was overlong-sequence filtering or reward shaping from the DAPO paper. The loss is normalized just by the number of sequences in the batch (equal weight per token), with no KL penalty and no entropy bonus (reference-model KL is supported but unused). Despite this simplicity, training was very stable.

Inflight weight updates mean sequence generation proceeds with stale keys/values in the KV cache computed with a previous model version; experiments indicate this does not adversely affect stability.

## Architecture

PipelineRL is modular, designed to take advantage of specialized inference and training software (SGLang, vLLM, NVIDIA Dynamo, DeepSpeed, FSDP, TorchTitan, FastLLM, etc.) via clear inference/training contracts.

**Inference contract:**
- Process group initialization: Trainer 0 sends `POST /init_process_group` to all inference servers at startup.
- Weight update trigger: after a learning step, Trainer 0 sends `POST /request_weight_update`, detailing order/shapes of weights about to be transferred via NCCL; inference servers pause and receive the broadcast.
- Chat completion: actor processes call inference LLMs via `POST /v1/chat/completion`.

**Trainer contract:** worker initialization (load/shard weights and optimizer state), forward pass (token log-likelihoods), backward step (accumulate gradient of the RL objective), optimizer step, and weight gathering/broadcasting (layer-by-layer after each optimizer step).

PipelineRL currently uses Hugging Face `accelerate` (choice of DeepSpeed or FSDP), though the team found its contract too flexible and plans to move to the stricter contract described above.

## Experimental details

Same hyperparameters for both 7B and 32B runs: batch size 4096, learning rate 1e-6, max 8192 generated tokens (vs. 16K allowed in OpenReasoner runs). Compute used: ~3.5 days on 2 nodes for the 7B model, ~6 days on 4 nodes for the 32B model.

## What's next

Planned work includes coroutines for more precise inference batch-size control, multi-modal support, and sequence-parallel training, plus more inference server/trainer integrations. `pipeline-rl` is intended to remain a hackable, fast reference implementation of GRPO with easily verifiable rewards rather than a framework supporting every algorithm and reward function. More analysis of how inflight weight updates affect training dynamics, and comparison with related asynchronous RL work for LLMs, is planned for a forthcoming paper.

## Acknowledgements

Alexandre Piché wrote the first synchronous version of the RL code while working on TapeAgents; Dzmitry Bahdanau refactored it to be asynchronous and distributed and implemented inflight weight updates; Rafael Pardinas implemented sequence packing; Ehsan Kamalloo ran experiments; Xiaoyin Chen helped with debugging. The team acknowledges prior RL-for-LLM implementations (TRL, OpenRLHF, veRL) and open-source reasoning projects (Simple-RL, DeepScaler, DAPO, OpenReasoner) for techniques that helped stabilize PipelineRL.
