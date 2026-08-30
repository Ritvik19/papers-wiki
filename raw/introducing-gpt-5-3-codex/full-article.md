---
Source URL: https://openai.com/index/introducing-gpt-5-3-codex/
Fetched via: WebFetch (curl returns 403 on openai.com/index/*)
Date: February 5, 2026
---

# Introducing GPT‑5.3‑Codex

Expanding Codex across the full spectrum of professional work on a computer.

GPT‑5.3‑Codex is OpenAI's most capable agentic coding model to date. It advances both the frontier coding performance of GPT‑5.2‑Codex and the reasoning and professional knowledge capabilities of GPT‑5.2, together in one model, which is also 25% faster. This enables long-running tasks involving research, tool use, and complex execution; users can steer and interact with the model while it works, without losing context.

GPT‑5.3‑Codex is OpenAI's first model that was instrumental in creating itself: the Codex team used early versions to debug its own training, manage its own deployment, and diagnose test results and evaluations.

## Frontier agentic capabilities

Sets a new industry high on SWE-Bench Pro and Terminal-Bench, with strong performance on OSWorld and GDPval.

### Coding

Achieves state-of-the-art performance on SWE-Bench Pro (four languages, more contamination-resistant than SWE-bench Verified which is Python-only) and far exceeds the previous state of the art on Terminal-Bench 2.0, using fewer tokens than any prior model.

### Web development

Combining frontier coding, aesthetic improvements, and compaction, the model built two complete games (a racing game and a diving game) autonomously over millions of tokens using preselected generic follow-up prompts like "fix the bug" or "improve the game." It also better understands intent on underspecified prompts for everyday websites, defaulting to more functional, production-ready output than GPT‑5.2‑Codex.

### Beyond coding

Built to support the full software lifecycle: debugging, deploying, monitoring, writing PRDs, editing copy, user research, tests, metrics, and non-coding work like slide decks and spreadsheet analysis. Matches GPT‑5.2 on GDPval (well-specified knowledge-work tasks across 44 occupations). Shows far stronger computer-use capability than previous GPT models on OSWorld-Verified (humans score ~72%).

## An interactive collaborator

The Codex app now provides frequent updates during long-running work, letting users interact in real time (ask questions, discuss approaches, steer) rather than waiting for a final output.

## How Codex was used to train and deploy GPT‑5.3‑Codex

The research team used Codex to monitor and debug the training run, track patterns during training, and analyze interaction quality. The engineering team used Codex to optimize the harness, identify context-rendering bugs, root-cause low cache hit rates, and dynamically scale GPU clusters for traffic surges. During alpha testing, researchers used Codex to build custom regex classifiers and data pipelines to analyze usage patterns.

## Securing the cyber frontier

GPT‑5.3‑Codex is the first model classified as **High capability** for cybersecurity-related tasks under the Preparedness Framework, and the first directly trained to identify software vulnerabilities. OpenAI has no definitive evidence it can automate cyberattacks end-to-end but is taking a precautionary approach with its most comprehensive cybersecurity safety stack to date: safety training, automated monitoring, trusted access for advanced capabilities, and enforcement pipelines including threat intelligence. Some elevated-cyber-risk requests may be automatically routed from GPT‑5.3‑Codex to GPT‑5.2. Launching Trusted Access for Cyber (pilot program) and expanding the private beta of Aardvark (security research agent). Committing $10M in API credits to accelerate cyber defense, building on a $1M Cybersecurity Grant Program launched in 2023.

## Availability

Available with paid ChatGPT plans across the Codex app, CLI, IDE extension, and web; running 25% faster due to infrastructure and inference-stack improvements. Co-designed for, trained with, and served on NVIDIA GB200 NVL72 systems.

## Appendix: benchmarks

| Eval | GPT‑5.3‑Codex (xhigh) | GPT‑5.2‑Codex (xhigh) | GPT‑5.2 (xhigh) |
| --- | --- | --- | --- |
| SWE-Bench Pro (Public) | 56.8% | 56.4% | 55.6% |
| Terminal-Bench 2.0 | 77.3% | 64.0% | 62.2% |
| OSWorld-Verified | 64.7% | 38.2% | 37.9% |
| GDPval (wins or ties) | 70.9% | - | 70.9% (high) |
| Cybersecurity Capture The Flag Challenges | 77.6% | 67.4% | 67.7% |
| SWE-Lancer IC Diamond | 81.4% | 76.0% | 74.6% |
