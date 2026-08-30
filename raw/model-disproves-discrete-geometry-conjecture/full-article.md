---
Source URL: https://openai.com/index/model-disproves-discrete-geometry-conjecture/
Fetched via: WebFetch (curl returns 403 on openai.com/index/*)
Date: May 20, 2026
---

# An OpenAI model has disproved a central conjecture in discrete geometry

For nearly 80 years, mathematicians studied the **planar unit distance problem**: given \(n\) points in the plane, how many pairs can be exactly distance 1 apart? First posed by Paul Erdős in 1946, described in the 2005 book *Research Problems in Discrete Geometry* as "possibly the best known (and simplest to explain) problem in combinatorial geometry."

Since Erdős's original work, the prevailing belief was that "square grid" constructions were essentially optimal for maximizing unit-distance pairs. An internal OpenAI model disproved this longstanding conjecture, providing an infinite family of examples yielding a polynomial improvement. The proof was checked by a group of external mathematicians, who also wrote a companion paper explaining the argument and its significance.

The proof came from a new general-purpose reasoning model, not a system trained specifically for mathematics or targeted at this problem; it was produced as part of a broader effort evaluating whether advanced models can contribute to frontier research, testing the model on a collection of Erdős problems. This is described as the first time a prominent open problem central to a subfield of mathematics has been solved autonomously by AI, and it draws on techniques from a different area of mathematics (algebraic number theory) applied to an elementary geometric question.

Fields medalist Tim Gowers called the result "a milestone in AI mathematics." Number theorist Arul Shankar said the paper "demonstrates that current AI models go beyond just helpers to human mathematicians – they are capable of having original ingenious ideas, and then carrying them out to fruition."

## The unit distance problem

Let \(u(n)\) be the largest possible number of unit-distance pairs among \(n\) points. A line gives \(n-1\) pairs; a square grid gives about \(2n\); the previously best-known construction (a rescaled square grid) gives \(n^{1+C/\log\log(n)}\) for a constant \(C\), growth only slightly faster than linear since the exponent term tends to 0. Erdős conjectured an upper bound of \(n^{1+o(1)}\). The new result disproves this: for infinitely many \(n\), the proof constructs configurations with at least \(n^{1+\delta}\) unit-distance pairs for a fixed \(\delta > 0\) (the original AI proof did not give an explicit \(\delta\), but a subsequent refinement by Princeton's Will Sawin showed \(\delta = 0.014\) works).

The best known lower bound had been essentially unchanged since 1946; the best upper bound, \(O(n^{4/3})\), dates to Spencer, Szemerédi, and Trotter (1984) and remained essentially unchanged despite later refinements.

## New techniques from algebraic number theory

Erdős's original lower bound used the Gaussian integers (\(a+bi\), with unique factorization into primes). The new argument replaces these with more complicated algebraic number fields with richer symmetries that create many more unit-length differences, using tools such as infinite class field towers and Golod–Shafarevich theory to show the required number fields exist. These concepts were well known to algebraic number theorists but had not previously been connected to this geometric question.

## Reception

Mathematician Thomas Bloom, in the companion note: "this shows that there is a lot more that number theoretic constructions have to say about these sorts of questions than we suspected... No doubt many algebraic number theorists will be taking a close look at other open problems in discrete geometry in the coming months." He adds: "the coming months and years will see similar successes in many other areas of mathematics, where long-standing open problems are resolved by an AI revealing unexpected connections."

## Why this matters

Better mathematical reasoning can make AI a stronger research partner: holding together difficult lines of thought, connecting ideas across distant areas of knowledge, surfacing promising paths experts may not have prioritized, and helping with problems otherwise too complex or time-intensive to tackle. Those abilities matter beyond mathematics, in biology, physics, materials science, engineering, and medicine, and are part of the longer-term path toward more automated research. Human judgment remains essential: people choose which problems matter, interpret results, and decide what to pursue next.
