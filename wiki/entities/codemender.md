# CodeMender

**Type**: tool  
**Tags**: #entity

## Overview

**CodeMender** is Google's code-security agent system that orchestrates multiple specialized models to find, validate, and patch software vulnerabilities at scale. It pairs agent infrastructure with **Gemini 3.5 Flash Cyber**, a fine-tuned variant of [[Gemini 3.5 Flash]] built for cybersecurity workflows.

## Appearances

- [[Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber]] — CodeMender uses multiple 3.5 Flash Cyber agents to produce a single combined vulnerability report; competitive frontier performance on CyberGym at lower per-token cost than larger models. Deployment is limited to a pilot for governments and trusted partners due to dual-use risk.
- [[Gemini 3.8 Flash and 3.8 Flash Cyber]] — **Gemini 3.8 Flash Cyber** supersedes 3.5 Flash Cyber as Google's defender-focused cyber model, deployed via the **[[Fairwind Program]]** rather than CodeMender alone.

## Notes

- Not generally available via the public Gemini API for Cyber variants; access is restricted to mitigate offensive misuse.
- **Fairwind Program** (Sep 2026) is the successor trusted-access channel for 3.8 Flash Cyber; CodeMender pilot used 3.5 Flash Cyber.
- Builds on Flash-series efficiency for high-volume security scanning and patching workflows.

## Related

- [[DeepMind]] — develops CodeMender and Gemini Flash Cyber.
- [[Gemini 3.5 Flash]] — base model for the Flash Cyber fine-tune.
- [[Code Models]] — code security and vulnerability detection context.
- [[Safety and Alignment]] — restricted deployment for dual-use cyber capabilities.
- [[Fairwind Program]] — trusted-defender access for 3.8 Flash Cyber.
