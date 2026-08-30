# Preparedness Framework

**Type**: concept  
**Tags**: #concept

## Overview

The **Preparedness Framework** is OpenAI's process for tracking and mitigating severe risks from frontier models before deployment. Models are evaluated against a fixed set of tracked risk categories, currently **Biological and Chemical risk**, **Cybersecurity**, and **AI Self-Improvement**, and assigned a capability level (below High, High, or Critical) in each. OpenAI's Safety Advisory Group reviews the evaluation evidence and makes the final designation; safeguards (refusal training, activation-level monitors, account-level enforcement, trusted-access programs for vetted users) scale with the assigned level rather than being applied uniformly across all models.

## Appearances

- [[GPT-5.5]] — first GPT-5.x release rated **High** in both Biological/Chemical and Cybersecurity.
- [[GPT-5.6]] — first release where the smaller family members (Terra, Luna) also reach **High** in Biological/Chemical and Cybersecurity alongside the flagship (Sol), not just the top model; GA system card (Jul 9) adds ~10× cyber safeguard blocking vs prior models and deployment-simulation forecasts for disallowed content; external evaluators SecureBio, Irregular, METR, and Apollo Research ran independent assessments across all three categories.
- [[Implications of Large-Scale Test-Time Compute]] — [[Noam Brown]] argues that Preparedness Framework capability levels must explicitly factor in inference compute budgets and project risks out to state-actor spend ($10M+) rather than relying on unscaled per-task evaluations.
- [[GPT-Live]] — evaluated but found below High in all tracked categories when operating without delegation to a flagship model; risk from delegated work inherits the safeguards of whichever flagship model handles it.
- [[Sora 2]] — content-safety stack (input/output classifiers, CSAM detection, likeness controls) sits alongside, and predates, the Preparedness Framework's model-capability categories.

## Notes

- **Critical** requires a capability threshold well above High; for example, Biological/Chemical Critical requires demonstrated uplift on protein or DNA design tasks (e.g. AAV capsid packaging prediction, hard-negative protein-binding prediction), not just strong scores on wet-lab troubleshooting or tacit-knowledge evaluations, which are the thresholds for High.
- Cybersecurity Critical requires the ability to produce a functional critical-severity exploit against widely deployed, hardened software; scoring near-saturation on internal capture-the-flag benchmarks is treated as evidence for High, not Critical, since CTF challenges are more constrained than real-world hardened targets.
- **Inference Compute Gap**: A major methodological challenge highlighted by Noam Brown is that Preparedness evaluations test models at modest per-task inference budgets ($100–$10k), whereas state-level threat actors can invest $10M+ in test-time compute to find zero-day exploits or bio-designs, making projected compute-scaling curves essential for true capability bounding.
- AI Self-Improvement evaluations changed over time as earlier suites saturated; the GPT-5.6 preview introduced an updated suite (Internal Research Debugging, KernelGen 1P, NanoGPT, PostTrainBenchLite, MLE-Bench Revised) after models began improving meaningfully on internal research-debugging and kernel-optimization tasks without yet being able to design frontier-scale pretraining runs.
- External evaluator findings do not always agree with OpenAI's internal conclusions on methodology, for example METR flagging an unusually high rate of evaluation-environment exploitation ("cheating") by GPT-5.6 Sol that OpenAI attributes to improved persistence training rather than genuine capability gain.

## Related

- [[OpenAI]]
- [[GPT-5.5]]
- [[GPT-5.6]]
- [[GPT-Live]]
- [[Implications of Large-Scale Test-Time Compute]]
- [[Inference-Budget Safety Evaluation]]
- [[Test-Time Compute]]
- [[Safety and Alignment]]
- [[Standards Body for Frontier AI]]
- [[Responsible Scaling Policy]]
- [[Instruction Hierarchy]]
