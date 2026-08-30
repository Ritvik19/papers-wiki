---
Source URL: https://openai.com/index/new-result-theoretical-physics/
Fetched via: WebFetch (curl returns 403 on openai.com/index/*)
Date: February 13, 2026
---

# GPT‑5.2 derives a new result in theoretical physics

A new preprint shows that a type of particle interaction many physicists expected would not occur can in fact arise under specific conditions. The preprint, titled "Single-minus gluon tree amplitudes are nonzero," is authored by Alfredo Guevara (Institute for Advanced Study), Alex Lupsasca (Vanderbilt University and OpenAI), David Skinner (University of Cambridge), Andrew Strominger (Harvard University), and Kevin Weil (OpenAI) on behalf of OpenAI, and posted to arXiv.

The work concerns **scattering amplitudes** for gluons (particles carrying the strong nuclear force). At tree level (diagrams with no quantum loops), many gluon amplitudes take unexpectedly simple forms, revealing deeper structure in quantum field theory. One configuration, however, had generally been treated as having zero amplitude: when one gluon has negative helicity and the remaining \(n-1\) gluons have positive helicity, standard textbook arguments (assuming generic particle momenta) suggest the tree-level amplitude must vanish.

The preprint shows this conclusion is too strong. In a specific, precisely defined slice of momentum space called the **half-collinear regime** (a special but mathematically well-defined momentum alignment), the amplitude does not vanish, and the paper computes it in that regime. This opens questions for future work, including analogous amplitudes for gravitons.

## Methodology

The final formula (Eq. 39 in the preprint) was first conjectured by **GPT‑5.2 Pro**. The human authors had worked out amplitudes by hand for integer \(n\) up to \(n=6\), obtaining very complicated expressions (Eqs. 29–32) from a Feynman diagram expansion whose complexity grows superexponentially in \(n\). GPT‑5.2 Pro greatly reduced the complexity of these expressions (Eqs. 35–38), then spotted a pattern and posited a formula valid for all \(n\).

An internal scaffolded version of GPT‑5.2 then spent roughly 12 hours reasoning through the problem, independently arriving at the same formula and producing a formal proof of its validity. The equation was subsequently verified analytically to solve the Berends-Giele recursion relation (a standard method for building multi-particle tree amplitudes from smaller pieces) and checked against the soft theorem (which constrains amplitude behavior as a particle becomes soft).

With GPT‑5.2's help, the amplitudes have already been extended from gluons to gravitons, with further generalizations planned.

## Reception

Nima Arkani-Hamed (Institute for Advanced Study): "It happens frequently in this part of physics that expressions for some physical observables, calculated using textbook methods, look terribly complicated, but turn out to be very simple... 'finding a simple formula' has always been fiddly, and also something that I have long felt might be automatable by computers. It looks like across a number of domains we are beginning to see this happen."

Nathaniel Craig (UC Santa Barbara): "This is clearly journal-level research advancing the frontiers of theoretical physics... By coupling GPT‑5.2 with human domain experts, the paper provides a template for validating LLM-driven insights and satisfies what we expect from rigorous scientific inquiry."
