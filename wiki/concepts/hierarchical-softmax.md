# Hierarchical Softmax

**Type**: concept  
**Tags**: #concept

## Overview

**Hierarchical softmax** (Morin & Bengio, AISTATS 2005) replaces flat vocabulary [[Softmax]] with a **binary tree** over words. Each word is a leaf; its probability equals the product of binary decisions (sigmoids) along the root-to-leaf path. Training updates only O(log V) nodes per example instead of O(V).

## Appearances

- [[Learning Word Embedding]] — Fig. 3 (Xin Rong); path probability formula; Huffman and WordNet tree heuristics; training vs inference cost asymmetry.
- [[Yoshua Bengio]] — Co-author of original hierarchical probabilistic neural language model paper.

## Path probability

For output word w_O given input w_I, let n(w_O, k) be the k-th node on the path from root to leaf w_O, with depth L(w_O).

**Single node decision** (σ = sigmoid):

p(turn right | w_I, n) = σ(v_n'^T v_{w_I})

p(turn left | w_I, n) = σ(−v_n'^T v_{w_I})

**Word probability**:

p(w_O | w_I) = ∏_{k=1}^{L(w_O)} σ( I_turn(n(w_O,k), n(w_O,k+1)) · v_{n(w_O,k)}'^T v_{w_I} )

**I_turn** = +1 if n(w_O,k+1) is the **left** child of n(w_O,k); −1 if **right** child.

Each internal node n has its own learned vector v_n' (analogous to columns of W′ but structured by tree).

## Complexity

| Phase | Flat softmax | Hierarchical softmax |
|-------|--------------|-------------------|
| Training per example | O(V) | O(log V) path nodes |
| Parameters | V output vectors | V leaves + (V−1) internal nodes |
| Inference (argmax word) | O(V) | O(V) worst case without pruning |

At **prediction** time you generally do not know which leaf to follow—you may still need to evaluate many paths unless the application reveals the target word (training does).

## Tree construction

| Strategy | Idea | Tradeoff |
|----------|------|----------|
| **Huffman coding** | Short paths for high-frequency words | Fast training signal for common tokens; frequency-only semantics |
| **WordNet / clustering** | Semantically related words share branches | Better quality possible; requires external resource or offline clustering |
| Random balanced tree | Simple | Usually worse than Huffman |

Tree quality materially affects perplexity and embedding quality—bad trees lengthen paths for common words or split related words far apart.

## Relation to Word2Vec

Word2Vec C implementation offered hierarchical softmax as an alternative to [[Negative Sampling]]. In practice **NEG won** for speed and simplicity (no tree maintenance, no per-node extra parameters). Hierarchical softmax remains pedagogically important and appears in older language model literature.

## Related

- [[Softmax]]
- [[Word2Vec]]
- [[Skip-Gram]]
- [[Negative Sampling]]
- [[Yoshua Bengio]]
- [[Learning Word Embedding]]
