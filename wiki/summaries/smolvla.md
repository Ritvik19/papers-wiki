# SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data

**Source**: `raw/smolvla/full-article.md` (420 KB), `raw/smolvla/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

SmolVLA is Hugging Face's compact (450M parameter) open-source Vision-Language-Action (VLA) model for robotics, trained entirely on public, community-shared LeRobot datasets rather than proprietary data, and designed to run on consumer hardware including a single GPU, CPU, or a MacBook. It targets the same democratization goal as SmolLM/SmolVLM: give robotics researchers a capable, reproducible baseline instead of a model locked behind private data and expensive infrastructure.

Architecturally, SmolVLA pairs a SmolVLM2-based Vision-Language Model (a SigLIP vision encoder plus a SmolLM2 language decoder) with a separate ~100M-parameter action expert, a compact transformer trained with a flow-matching objective that directly predicts continuous action sequences rather than autoregressively decoding discrete action tokens. The VLM encodes camera images, the language instruction, and the robot's sensorimotor state (projected into a single token) into contextual features; the action expert then generates chunks of future robot actions conditioned on those features, with its hidden size reduced to 75% of the VLM's to stay lightweight. Three efficiency choices define the design: visual token reduction (PixelShuffle compresses a 512x512 image into 64 tokens instead of 1024, and only the global image is used at runtime even though the VLM was pretrained with image tiling), layer skipping (the action expert only attends to VLM features up to half the total layers, halving compute with minimal quality loss), and interleaved cross-/self-attention in the action expert (cross-attention conditions actions on perception, causal self-attention enforces temporal smoothness).

The model also introduces an asynchronous inference stack that decouples action execution from action prediction: while the robot executes its current action chunk, it already streams the latest observation to a remote Policy Server for the next chunk, with an early-trigger threshold, decoupled control/inference threads, and chunk-fusion stitching to avoid jitter between chunks. Pretraining data comes from 487 curated, quality-filtered LeRobot community datasets on the SO100 robotic arm (about 10 million frames, roughly an order of magnitude smaller than other VLA benchmark datasets but more behaviorally diverse), cleaned up with an LLM-based task-annotation rewriter (Qwen2.5-VL-3B-Instruct) and a manually standardized camera-naming scheme.

## Key Claims

- SmolVLA-450M matches or exceeds larger VLAs and strong baselines like ACT on both simulation benchmarks (LIBERO, Meta-World) and real-world tasks (SO100, SO101), despite using under 30k training episodes, an order of magnitude fewer than other VLAs.
- Asynchronous inference is about 30% faster than synchronous inference (9.7s vs 13.75s to complete a task) and completes roughly 2x more tasks in a fixed time window (19 vs 9 cubes), at similar task success rates (~78% for both modes).
- Pretraining on the 487-dataset LeRobot community mixture raises SO100 success from 51.7% (no pretraining) to 78.3%, a +26.6 point absolute gain; multitask finetuning adds further task-transfer gains on top.
- Action expert hidden size is fixed at 75% of the VLM's hidden size as an efficiency/performance balance point.
- Visual tokens are capped at 64 per frame via PixelShuffle regardless of input resolution, and the action expert only uses VLM features up to half the total layer depth.

## Figures

No figures were extracted for this ingest; the source article's architecture diagram, asynchronous-inference-stack diagram, and simulation/real-world benchmark tables are referenced inline in the summary above but not downloaded, per this batch's no-figure-download policy.

## Entities

- [[Hugging Face]] — publishes the blog and the LeRobot framework SmolVLA is built on.

## Questions & Gaps

- The post does not report absolute parameter counts or architecture details for the baseline VLAs it compares against (Pi0, GR00T, Diffusion Policy, ACT) beyond naming them.
- Cross-embodiment transfer is questioned directly in the article's comment section (whether SO100/SO101-trained SmolVLA generalizes to different-DOF arms like Franka or a Unitree G1 humanoid); the authors do not provide a definitive answer in the post itself.
- No ablation isolates how much of the efficiency gain comes from layer skipping versus visual token reduction versus the interleaved attention design individually.

## Related

- [[nanoVLM: The simplest repository to train your VLM in pure PyTorch]] — related from-scratch VLM training project reusing the same SmolLM2/SigLIP-family lineage.
- [[Papers Explained 176 - Smol LM]] — SmolLM2 and SmolVLM2, the language and vision-language backbones SmolVLA's VLM component is built on.
- [[Papers Explained 346 - SmolVLM]] — the SmolVLM architecture line that SmolVLA's VLM backbone (SmolVLM2) descends from.
- [[Vision Language Models]] — topic page for multimodal model coverage.
- [[Hugging Face]]
