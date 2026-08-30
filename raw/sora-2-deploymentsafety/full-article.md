---
Source URL: https://deploymentsafety.openai.com/sora-2
Fetched via: WebFetch (canonical raw is full-article.md via curl; this is the markdown sibling)
---

# Sora 2 System Card - OpenAI Deployment Safety Hub

Sora 2 is OpenAI's video and audio generation model, building on the original Sora with more accurate physics, sharper realism, synchronized audio, enhanced steerability, and expanded stylistic range. Available via sora.com, a standalone iOS Sora app, and (later) the API.

Sora 2's advanced capabilities raise new risks, including nonconsensual use of likeness and misleading generations. OpenAI worked with internal red teamers to identify challenges and inform mitigations, taking an iterative approach: initial access via limited invitations, restricting image uploads featuring a photorealistic person and all video uploads, and stringent safeguards/moderation thresholds on content involving minors.

## Safety stack

Builds on learnings from Sora 1 and mitigations developed for GPT-4o Image Generation and DALL·E, plus Sora-2-specific safeguards:

- **Input (prompt) blocking**: text/image classifiers block generation if a prompt is flagged as violating policy.
- **Output blocking**: after generation, CSAM classifiers and a safety-focused reasoning monitor (a multimodal reasoning model custom-trained to reason about content policies) block outputs that violate policy if input blocks were circumvented.
- **Increased safeguards for minors**: stricter mitigations for users who may be under 18, limiting age-inappropriate content creation; under-13 users are prohibited from all OpenAI products.

Usage Policies prohibit: violating others' privacy (including likeness use without permission); threatening, harassing, or defaming others, non-consensual intimate imagery, or content inciting violence/suffering; impersonation, scams, or fraud; and exploiting, endangering, or sexualizing minors. Enforcement combines in-app reporting, automation, and human review, with penalties/content removal and user notification.

## Provenance

For general availability: C2PA metadata on all first-party assets (verifiable origin via industry standard), a visible moving watermark on videos downloaded from sora.com/the app, and internal detection tools to assess whether content was created by OpenAI's products.

## Key risk areas

- **Harmful or inappropriate outputs**: automated detection scanning video frames, scene descriptions, and audio transcripts; proactive detection, user reporting, and stricter thresholds for the social feed.
- **Misuse of likeness & deceptive content**: no video-to-video generation at launch, no text-to-video generation of public figures, blocking generations with real people other than consenting users via the "cameo" likeness-control feature; classifiers against non-consensual nudity/racy output, graphic violence, or fraud-enabling output.
- **Child safety**: excludes CSAM from training data, partners with NCMEC, and scans all inputs/outputs (first- and third-party) with a dedicated CSAM safety stack.
- **Teen safety**: additional moderation thresholds for likely-under-18 users; tighter thresholds on generations from images/videos where a classifier detects a potential minor; public feed restricted to under-18-appropriate content regardless of viewer age; stricter privacy defaults, likeness-use limits, unwanted-contact protections, and parental controls for teens.

## Red teaming and evaluations

External testers from OpenAI's Red Team Network tested content generation across violative categories (sexual content, nudity, extremism, self-harm, wrongdoing, violence/gore, political persuasion) plus youth-safety and likeness-use policies, probing violative uploads, testing media generation, attempting jailbreaks, and stress-testing product-level safeguards.

Thousands of adversarial prompts from targeted red-teaming were categorized by use case/policy, run through a helpful-only version of the video model, then graded on `not_unsafe` (recall of blocking unsafe content) and `not_overrefuse` (avoiding false blocks on benign content):

| Category | not_unsafe at output | not_overrefuse at output |
| --- | --- | --- |
| Adult Nudity / Sexual Content Without Use of Likeness | 96.04% | 96.20% |
| Adult Nudity / Sexual Content With Use of Likeness | 98.40% | 97.60% |
| Self-Harm | 99.70% | 94.60% |
| Violence and Gore | 95.10% | 97.00% |
| Violative Political Persuasion | 95.52% | 98.67% |
| Extremism/Hate | 96.82% | 99.11% |

OpenAI plans continued investment in age prediction and provenance features, with ongoing fine-tuning and monitoring as usage develops.
