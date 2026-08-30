# Model Disproves Discrete Geometry Conjecture

**Source**: `raw/model-disproves-discrete-geometry-conjecture/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

For nearly 80 years, mathematicians worked on the planar unit distance problem: given n points in the plane, how many pairs of them can be exactly distance 1 apart. Paul Erdos posed the question in 1946, and it was later described as one of the best known and simplest to state problems in combinatorial geometry. The long-standing belief was that square-grid constructions were essentially optimal for maximizing the number of unit-distance pairs. An internal OpenAI model disproved that conjecture, producing an infinite family of examples that give a polynomial improvement over the square-grid bound. A group of external mathematicians checked the proof and wrote a companion paper explaining the argument.

The proof came from a new general-purpose reasoning model, not a system trained specifically for mathematics or aimed at this problem. It was produced while OpenAI tested the model on a collection of Erdos problems as part of a broader effort to evaluate whether advanced models can contribute to frontier research. OpenAI describes this as the first time a prominent open problem central to a subfield of mathematics has been solved autonomously by AI. The proof draws on algebraic number theory (a different area of mathematics) applied to an elementary geometric question.

Let u(n) be the largest possible number of unit-distance pairs among n points. A line gives n-1 pairs, a square grid gives about 2n, and the previously best-known construction (a rescaled square grid) gives n^(1+C/loglog(n)) for a constant C, growth only slightly faster than linear. Erdos conjectured an upper bound of n^(1+o(1)). The new result disproves this: for infinitely many n, the proof constructs configurations with at least n^(1+delta) unit-distance pairs for a fixed delta greater than 0. The original AI proof did not give an explicit value for delta; a subsequent refinement by Princeton mathematician Will Sawin showed that delta = 0.014 works. The best known lower bound had been essentially unchanged since 1946, and the best known upper bound, O(n^(4/3)), dates to a 1984 result by Spencer, Szemeredi, and Trotter.

Erdos's original lower-bound construction used the Gaussian integers, which have unique factorization into primes. The new argument instead uses more complicated algebraic number fields with richer symmetries, drawing on tools such as infinite class field towers and Golod-Shafarevich theory to show that the required number fields exist. These tools were already well known to algebraic number theorists but had not previously been connected to this geometric question. Fields medalist Tim Gowers called the result "a milestone in AI mathematics." Number theorist Arul Shankar said the paper "demonstrates that current AI models go beyond just helpers to human mathematicians, they are capable of having original ingenious ideas, and then carrying them out to fruition." Mathematician Thomas Bloom wrote in the companion note that the result shows number-theoretic constructions have more to say about these geometric questions than expected, and predicted similar AI-driven results in other open problems in discrete geometry.

## Key Claims

- The planar unit distance problem, posed by Erdos in 1946, asks for the maximum number of unit-distance pairs among n points in the plane.
- An OpenAI reasoning model (general-purpose, not math-specialized) disproved the conjecture that square-grid constructions are essentially optimal, by constructing an infinite family of counterexamples.
- For infinitely many n, the new construction gives at least n^(1+delta) unit-distance pairs for a fixed delta > 0, beating Erdos's conjectured upper bound of n^(1+o(1)).
- The original AI proof left delta unspecified; Will Sawin later showed delta = 0.014 works.
- The best known upper bound remains O(n^(4/3)), from Spencer, Szemeredi, and Trotter (1984).
- The proof method replaces Erdos's use of Gaussian integers with richer algebraic number fields, using infinite class field towers and Golod-Shafarevich theory.
- The proof was checked by external mathematicians, who also wrote a companion paper on the argument and its significance.
- OpenAI frames this as the first time a prominent open problem central to a subfield of mathematics has been solved autonomously by AI.

## Figures

No article figures extracted; openai.com blocks direct HTML download so figures could not be downloaded, and WebFetch markdown does not preserve chart images.

## Entities

- [[OpenAI]]: the model that produced the proof was developed and tested internally at OpenAI.

## Questions & Gaps

- The source does not name the specific model (for example, which GPT version) beyond describing it as "a new general-purpose reasoning model."
- The source does not detail how many other Erdos problems were attempted alongside this one, or what the outcomes were.
- It is unclear how much of the proof-checking and write-up work by the external mathematicians involved further AI assistance versus purely manual verification.

## Related

- [[OpenAI]]
- [[Evaluation and Benchmarks]]
- [[Reasoning Models]]
- [[New Result in Theoretical Physics]]: another case of an OpenAI reasoning model contributing an original result to an established research field.
- [[Ten Advances in Mathematics and Theoretical Computer Science]]: Aug 2026 announcement broadening OpenAI's math-research claims to ten problems via the internal [[Astra]] model; uses different model branding and verification depth.
