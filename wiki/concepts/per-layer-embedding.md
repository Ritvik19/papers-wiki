# Per-Layer Embedding

**Type**: concept  
**Tags**: #concept

## Overview

**Per-Layer Embedding (PLE)** is an architectural technique introduced in Google's [[Papers Explained 586: Gemma 4]] (specifically in the E2B and E4B models) that augments standard token embeddings with distinct layer-wise representation vectors for every token in the vocabulary. By offloading these parameters to flash memory and retrieving only active token vectors in a single lookup, PLE anchors representations to initial token identities across deep Transformer layers without increasing active GPU VRAM footprint.

## Mechanism

1. **Dimensionality & Parameter Storage**:
   - In standard Transformers, a single token embedding table of dimension $d_{\text{model}}$ (e.g., 1536 in E2B, 2056 in E4B) is projected into layer 1.
   - PLE defines auxiliary layer-specific embeddings with a reduced dimensionality $d_{\text{PLE}} = 256$ across all layers (e.g., $262,144 \text{ vocab} \times 35 \text{ layers} \times 256 \text{ dim}$).
   - The full table is maintained in flash storage. Because only the embeddings corresponding to active input tokens are retrieved at inference, VRAM is preserved.

2. **Single-Lookup Retrieval**:
   - During the initial prefill/inference phase, the system retrieves the entire set of layer-wise embeddings for each input token in a single batch operation, avoiding repeated disk/flash lookups as subsequent layers execute.

3. **Gating & Layer Integration**:
   - Between decoder blocks, a learned gating mechanism determines relative weighting over the retrieved 256-dimensional representation.
   - The gated vector is projected up to the main model dimension $d_{\text{model}}$, normalized (RMSNorm), and integrated additively with the output of the preceding decoder block.

4. **Token Identity Preservation**:
   - As tokens pass through many self-attention and MLP blocks, contextual mixing can obscure original lexical identity. PLE injects a pure, layer-tailored token identity signal at each step, preventing representation drift.

5. **Effective vs. Total Parameters**:
   - Models utilizing PLE report **Effective Parameter Counts** (e.g., E2B has 2.3B effective parameters out of 5B total; E4B has 4.5B effective out of 8B total), where the non-effective parameter surplus resides in flash memory.

## Appearances

- [[Papers Explained 586: Gemma 4]] — Introduces PLE for Gemma 4 E2B and E4B edge models.
- [[Gemma 4 Technical Report]] — Formal specification of flash-resident layer-wise embedding tables and gating math.
- [[Gemma 4]] — Open-weights launch highlighting E2B and E4B edge deployment efficiency.

## Related

- [[Model Compression and Efficiency]]
- [[KV Cache]]
- [[Large Language Models]]
- [[Embedding and Retrieval]]
- [[Gemma 4]]
