# Small Recursive Transformers

**Tags**: #concept

Small recursive transformers are compact transformer models that improve on puzzle-style reasoning by repeatedly refining an internal latent state and answer over multiple steps—rather than emitting a final answer in a single forward pass. They are specialized grid/puzzle solvers, not general-purpose text LLMs.

## Overview

The Hierarchical Reasoning Model (HRM) showed that very small transformers (~4 blocks, dual modules) can rank highly on ARC-AGI-1 by recursive self-refinement with selective backprop and a learned halting mechanism. Follow-ups include Mixture-of-Recursions (MoR) and the Tiny Recursive Model (TRM, Oct 2025): a 7M-parameter, 2-layer transformer that alternates (1) computing a latent reasoning state from question+answer and (2) updating the answer from that state, for up to 16 refinement steps with gradient flow through the full recursion.

TRM simplifies HRM (single 2-layer stack, binary cross-entropy stop signal instead of explicit halting) and reports stronger Sudoku/ARC performance. Surprising ablations: 2 layers generalize better than 4 on Sudoku, and replacing self-attention with MLP can help on small fixed-length grids. Training cost was under ~$500 (4× H100, ~2 days). Inputs/outputs are discrete grids (ARC, Sudoku, Maze), not text sequences.

Raschka positions these as "pocket calculators" vs generalist LLMs—potential future **tools** inside agent systems for structured reasoning niches (physics, biology grids), not replacements for GPT-class models.

## Appearances

- [[Beyond Standard LLMs]] — TRM/HRM comparison, ARC leaderboard context, and agent-tool outlook.

## Notes

- Extension to textual QA is plausible but not demonstrated in the cited TRM work.
- Contrasts with test-time scaling in large reasoning LLMs (more tokens per problem) rather than tiny iterative refinement.

## Related

- [[Reasoning Models]]
- [[Beyond Standard LLMs]]
- [[Agentic AI]]
