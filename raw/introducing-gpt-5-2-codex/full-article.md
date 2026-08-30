---
Source URL: https://openai.com/index/introducing-gpt-5-2-codex/
Fetched via: WebFetch (curl returns 403 on openai.com/index/*)
Date: December 18, 2025
---

# Introducing GPT‑5.2‑Codex

The most advanced agentic coding model for professional software engineering and defensive cybersecurity.

GPT‑5.2‑Codex is a version of GPT‑5.2 further optimized for agentic coding in Codex: improvements on long-horizon work through context compaction, stronger performance on large code changes (refactors, migrations), improved performance in Windows environments, and significantly stronger cybersecurity capabilities.

A security researcher using GPT‑5.1‑Codex‑Max with Codex CLI found and responsibly disclosed a vulnerability in React that could lead to source code exposure, illustrating how model improvements translate into cybersecurity capability jumps. GPT‑5.2‑Codex has stronger cybersecurity capabilities than any prior OpenAI model; it does not reach 'High' cyber capability under the Preparedness Framework, but OpenAI is designing deployment with future capability growth in mind, including invite-only trusted access to more permissive models for vetted defensive-security professionals.

## Pushing the frontier on real-world software engineering

Builds on GPT‑5.2's professional knowledge-work strengths and GPT‑5.1‑Codex‑Max's frontier agentic coding and terminal-using capabilities: better long-context understanding, reliable tool calling, improved factuality, native compaction. Achieves state-of-the-art performance on SWE-Bench Pro and Terminal-Bench 2.0, and is much more effective in native Windows environments. Stronger vision performance improves interpretation of screenshots, technical diagrams, charts, and UI surfaces during coding sessions.

## Advancing the cyber frontier

Charting performance on a core cybersecurity evaluation over time shows a sharp jump starting with GPT‑5‑Codex, another large jump with GPT‑5.1‑Codex‑Max, and a third jump with GPT‑5.2‑Codex. OpenAI plans and evaluates as though each new model could reach 'High' cybersecurity capability under the Preparedness Framework. GPT‑5.2‑Codex has not yet reached that threshold but additional safeguards were added in the model and product, detailed in the system card. The Professional Capture-the-Flag (CTF) eval measures multi-step, professional-level cybersecurity challenges in a Linux environment.

### Real-world cyber capability example

On December 11, 2025, the React team published three security vulnerabilities affecting apps built with React Server Components. Andrew MacPherson, a principal security engineer at Privy (a Stripe company), was using GPT‑5.1‑Codex‑Max with Codex CLI to reproduce and study a different critical React vulnerability disclosed the week prior (React2Shell, CVE-2025-55182). After zero-shot attempts failed, he shifted to iterative prompting, then guided Codex through standard defensive-security workflows (local test environment, attack-surface reasoning, fuzzing). Codex surfaced unexpected behaviors that led, over one week, to discovery of previously unknown vulnerabilities, responsibly disclosed to the React team.

## Empowering cyberdefense through trusted access

OpenAI is developing a trusted-access pilot, initially invite-only for vetted security professionals with a track record of responsible disclosure and organizations with a clear professional cybersecurity use case, to remove friction for legitimate dual-use defensive work.

## Availability

Released in all Codex surfaces for paid ChatGPT users; API access for GPT‑5.2‑Codex planned in coming weeks.
