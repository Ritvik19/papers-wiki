# Sora 2

**Source**: `raw/sora-2/full-article.md`, `raw/sora-2-deploymentsafety/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

Sora 2 is OpenAI's video-and-audio generation model, released September 30, 2025 alongside a standalone iOS app called Sora. It follows the original Sora (February 2024), which OpenAI described as the "GPT-1 moment for video," the point where video generation first started to look plausible, with behaviors like object permanence emerging from scaled-up pretraining. Sora 2 is pitched as the "GPT-3.5 moment": it handles scenes prior video models struggled with, such as Olympic gymnastics routines or a physically accurate backflip on a paddleboard, and follows multi-shot instructions while keeping world state consistent across shots. OpenAI contrasts it with earlier "overoptimistic" video models that morphed objects to satisfy a prompt, such as a missed basketball shot teleporting into the hoop; in Sora 2, a missed shot instead rebounds off the backboard, which OpenAI frames as a mistake made by a physics-obeying model rather than a hallucination. The model also generates synchronized dialogue, sound effects, and background soundscapes, and can insert a real person, animal, or object into a generated scene from a short reference video.

The Sora app's headline feature is "cameo": a one-time video-and-audio identity verification lets a user insert themselves, or someone who has granted permission, into any Sora-generated scene. Each person controls their own likeness end to end, deciding who can use it, and can revoke access or remove any video containing it, including other users' drafts, at any time. The system card treats this as the model's biggest new risk area: nonconsensual use of a likeness and misleading generations, addressed at launch through invite-limited access, restrictions on uploading images of photorealistic people, and blocking any generation featuring a real person other than a consenting cameo user. All first-party outputs at general availability carry C2PA provenance metadata and a visible moving watermark on anything downloaded from sora.com or the app, on top of internal tools OpenAI uses to check whether content came from its own products.

Sora 2's safety stack builds on mitigations developed for Sora 1, GPT-4o image generation, and DALL·E, adding input classifiers that block a generation before it starts, output-stage CSAM classifiers, and a multimodal reasoning monitor that can still catch a violation if the input block was bypassed, plus stricter thresholds for any user who may be under 18 (under-13 users are barred from OpenAI products entirely). Child safety measures exclude CSAM from training data, partner with NCMEC, and run a dedicated scanning stack over all first- and third-party inputs and outputs. Teen-specific protections include daily generation limits, tighter likeness-use permissions, restriction of the public feed to under-18-appropriate content regardless of who is viewing, and parental controls that can override infinite-scroll limits, disable feed personalization, or manage direct messages. On the feed itself, OpenAI describes the recommender as instructable in natural language, biased toward people a user already follows and content useful as creative inspiration rather than time in feed, and paired with periodic wellbeing check-ins, as a response to concerns about doomscrolling and algorithmically sloptimized feeds.

Red-teaming for the system card ran thousands of adversarial prompts, drawn from OpenAI's external Red Team Network, through a helpful-only version of the video model across categories including sexual content, self-harm, violence and gore, political persuasion, and extremism, then graded each output for whether unsafe content was correctly blocked (`not_unsafe`) and whether benign content was incorrectly blocked (`not_overrefuse`). Results by category are in the table below. At launch, the Sora app was limited to the US and Canada, with web access at sora.com by invite, free with generous but compute-constrained limits, and an experimental higher-quality Sora 2 Pro model for ChatGPT Pro subscribers. As of April 26, 2026, the Sora product is no longer available.

## Key Claims

- Released September 30, 2025; a standalone iOS "Sora" app launched alongside the model.
- "Cameo" feature lets a user insert a verified likeness (video and audio) into any generated scene; likeness permissions are controlled entirely by the person whose likeness it is.
- No video-to-video generation and no text-to-video generation of public figures at launch; generations featuring a real person other than a consenting cameo user are blocked.
- C2PA provenance metadata on all first-party assets at general availability, plus a visible moving watermark on downloads from sora.com and the app.
- Teen protections include default daily generation limits, stricter character permissions, human moderator review of bullying reports, and parental controls.
- Under-13 users are prohibited from all OpenAI products; likely-under-18 users get stricter content and likeness-use thresholds.
- ChatGPT Pro users got access to an experimental Sora 2 Pro model on sora.com.
- The Sora product was discontinued as of April 26, 2026.

## Benchmarks

Red-team results from the system card, graded on `not_unsafe` (correctly blocking unsafe content) and `not_overrefuse` (not blocking benign content) at the output stage:

| Category | not_unsafe at output | not_overrefuse at output |
| --- | --- | --- |
| Adult nudity / sexual content without use of likeness | 96.04% | 96.20% |
| Adult nudity / sexual content with use of likeness | 98.40% | 97.60% |
| Self-harm | 99.70% | 94.60% |
| Violence and gore | 95.10% | 97.00% |
| Violative political persuasion | 95.52% | 98.67% |
| Extremism/hate | 96.82% | 99.11% |

## Figures

No article figures extracted; openai.com blocks direct HTML download so figures could not be downloaded, and WebFetch markdown does not preserve chart images.

## Entities

- [[OpenAI]]: developer of Sora 2 and operator of the Sora app.

## Questions & Gaps

- No firm date is given for API release or for the fate of Sora 1 Turbo continuity.
- No technical detail is given on how age prediction works, only that OpenAI plans continued investment in it.
- No official reason is stated in the raw sources for the product's April 2026 discontinuation.

## Related

- [[OpenAI]]
- [[Vision Language Models]]
- [[Safety and Alignment]]
- [[Preparedness Framework]]
