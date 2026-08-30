# New Result in Theoretical Physics

**Source**: `raw/new-result-theoretical-physics/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

A preprint titled "Single-minus gluon tree amplitudes are nonzero" shows that a type of particle interaction many physicists expected could not occur can in fact arise under specific conditions. The paper is authored by Alfredo Guevara (Institute for Advanced Study), Alex Lupsasca (Vanderbilt University and OpenAI), David Skinner (University of Cambridge), Andrew Strominger (Harvard University), and Kevin Weil (OpenAI), and was posted to arXiv on behalf of OpenAI.

The work concerns scattering amplitudes for gluons, the particles that carry the strong nuclear force. At tree level (Feynman diagrams with no quantum loops), many gluon amplitudes take unexpectedly simple forms, which points to deeper structure in quantum field theory. One configuration had generally been treated as having zero amplitude: when one gluon has negative helicity and the remaining n-1 gluons have positive helicity, standard textbook arguments that assume generic particle momenta conclude the tree-level amplitude must vanish. The preprint shows this conclusion does not hold everywhere. In a specific, precisely defined slice of momentum space called the half-collinear regime, a special but mathematically well-defined momentum alignment, the amplitude does not vanish, and the paper computes it in that regime. This raises further questions, including whether analogous amplitudes exist for gravitons.

The final formula for the amplitude (equation 39 in the preprint) was first conjectured by GPT-5.2 Pro. The human authors had worked out the amplitude by hand for integer n up to n = 6, producing very complicated expressions (equations 29 through 32) from a Feynman diagram expansion whose complexity grows superexponentially with n. GPT-5.2 Pro reduced the complexity of these expressions (equations 35 through 38), spotted a pattern in them, and proposed a formula valid for all n. An internal scaffolded version of GPT-5.2 then spent about 12 hours reasoning through the problem, independently arrived at the same formula, and produced a formal proof of its validity. The equation was subsequently verified analytically against the Berends-Giele recursion relation, a standard method for building multi-particle tree amplitudes from smaller pieces, and checked against the soft theorem, which constrains how an amplitude behaves as a particle becomes soft. With GPT-5.2's help, the amplitudes have already been extended from gluons to gravitons, with further generalizations planned.

Physicist Nima Arkani-Hamed (Institute for Advanced Study) noted that in this area of physics, expressions calculated by textbook methods often look complicated but turn out to have a simple underlying form, and that finding such simple formulas has long seemed like a task computers might eventually automate. Nathaniel Craig (UC Santa Barbara) described the paper as journal-level research that advances the frontiers of theoretical physics, and said that by pairing GPT-5.2 with human domain experts, it provides a template for validating LLM-driven insights.

## Key Claims

- The preprint proves that single-minus gluon tree amplitudes, long assumed to vanish under generic momenta, are nonzero in the half-collinear regime, and computes the amplitude there.
- GPT-5.2 Pro first conjectured the general formula (equation 39) after reducing complicated hand-derived expressions for n up to 6 and spotting a pattern.
- An internal scaffolded version of GPT-5.2 independently reasoned through the problem for about 12 hours, arrived at the same formula, and produced a formal proof.
- The formula was checked against the Berends-Giele recursion relation and the soft theorem.
- The result has already been extended from gluon amplitudes to graviton amplitudes.
- The paper is posted to arXiv on behalf of OpenAI and co-authored by two OpenAI-affiliated physicists alongside academic researchers from IAS, Vanderbilt, Cambridge, and Harvard.

## Figures

No article figures extracted; openai.com blocks direct HTML download so figures could not be downloaded, and WebFetch markdown does not preserve chart images.

## Entities

- [[OpenAI]]: two of the preprint's authors are OpenAI-affiliated, and GPT-5.2 (in both its Pro and scaffolded-reasoning forms) produced the core result.

## Questions & Gaps

- The source does not describe in detail what the "internal scaffolded version of GPT-5.2" consisted of, beyond that it reasoned for about 12 hours.
- The precise mathematical definition of the half-collinear regime is not given in the source beyond the phrase "a special but mathematically well-defined momentum alignment."
- It is unclear how much iteration or human steering was involved between GPT-5.2 Pro's initial conjecture and the final verified formula.

## Related

- [[OpenAI]]
- [[Reasoning Models]]
- [[Model Disproves Discrete Geometry Conjecture]]: another case of an OpenAI reasoning model producing an original result checked by outside domain experts.
