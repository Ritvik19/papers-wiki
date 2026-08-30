---
Source URL: https://deploymentsafety.openai.com/gpt-live
Fetched via: WebFetch (canonical raw is full-article.html via curl; this is the markdown sibling)
---

# GPT-Live System Card - OpenAI Deployment Safety Hub

GPT-Live-1 and GPT-Live-1 mini are a new generation of voice models designed to make conversations with AI feel more natural and intelligent. They are full-duplex: they can listen and respond continuously instead of waiting for a clearly defined turn to end, following pauses, interruptions, and changes in pace, deciding in the moment whether to respond or keep listening. GPT-Live-1 is the default voice model for paid users; GPT-Live-1 mini is the default for free users.

Key safety points: the models were trained to respond safely using the same infrastructure as OpenAI's flagship models; when they delegate more complex work to other models, the resulting work reflects the safety training of the underlying delegate model. System-level safety integrations are designed to be on par with the existing text-model safety stack, plus new voice-specific safeguards: inputs and generated outputs are checked as the conversation unfolds, and when potentially unsafe content is detected, the system can steer or interrupt the response, play a spoken safety message, provide text support resources, or end the voice conversation in higher-risk cases. The same monitoring, review, and enforcement infrastructure used for text models applies to GPT-Live.

## Evaluations

Newly developed evaluations use real audio examples from users who opted to share voice interactions to improve models, processed through privacy/eligibility safeguards (permission checks, deletion/opt-out status, PII scrubbing, de-identification) before transcription, response generation, and safety grading. Compared against the models powering Advanced Voice Mode (AVM).

**Voice-Native Evaluations: Production Prompts** (adversarially selected, not prevalence-weighted): GPT-Live models generally provide equal or better safety performance than AVM models. GPT-Live-1 shows a slight (not statistically significant) regression on emotional reliance (0.88 → 0.82); GPT-Live-1 mini shows a slight regression on sexual content (0.97 → 0.95).

**Voice-Native Evaluations: Synthetic Prompts** (audio synthesized from safety-policy-grounded text targeting specific categories and edge cases): GPT-Live models uniformly provide equal or better safety performance than AVM models on these adversarially selected prompts.

Internal and external red-teamers across languages stress-tested safety training with no system-level mitigations, across categories including child-coded voice, impersonation, speaker identification, sensitive train identification, self-harm, emotional reliance, scams/manipulation, and audio-specific perturbations. Early findings prioritized mitigation work on sexual content, emotional reliance, and self-harm, while validating some areas as policy-compliant by default (voice cloning, impersonation). Follow-up rounds validated the mitigations as robust.

## Preparedness Framework

The Safety Advisory Group determined that neither GPT-Live-1 nor GPT-Live-1 mini, when operating without delegation, could plausibly be considered High in any Tracked Category (Biological and Chemical Risk, AI Self-Improvement, Cybersecurity).

- **Biological/Chemical**: when GPT-Live delegates to flagship models, the experience inherits those models' safeguards; automated monitors may interrupt/end calls when potentially harmful conversations are detected or degrade the experience for repeated abuse, with actor-level enforcement where necessary.
- **Cybersecurity**: delegated work receives the safeguards of the model it's delegated to; GPT-Live's own cybersecurity risk is highly constrained at launch since it lacks broad independent tool access and has no code execution capability. Safeguards posture will be reassessed before enabling additional tools.
- **AI Self-Improvement**: evals were not run, since GPT-Live-1 and GPT-Live-1 mini are less capable than GPT-5.5 Thinking across several intelligence evaluations.
