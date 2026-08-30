# CodeMender

**Type**: tool  
**Tags**: #entity

## Overview

**CodeMender** is Google's code-security agent system that orchestrates multiple specialized models to find, validate, and patch software vulnerabilities at scale. It pairs agent infrastructure with **Gemini 3.5 Flash Cyber**, a fine-tuned variant of [[Gemini 3.5 Flash]] built for cybersecurity workflows.

## Appearances

- [[Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber]] — CodeMender uses multiple 3.5 Flash Cyber agents to produce a single combined vulnerability report; competitive frontier performance on CyberGym at lower per-token cost than larger models. Deployment is limited to a pilot for governments and trusted partners due to dual-use risk.

## Notes

- Not generally available via the public Gemini API; access is restricted to mitigate offensive misuse while giving defenders a head start on critical vulnerabilities.
- Builds on Flash-series efficiency for high-volume security scanning and patching workflows.

## Related

- [[DeepMind]] — develops CodeMender and Gemini Flash Cyber.
- [[Gemini 3.5 Flash]] — base model for the Flash Cyber fine-tune.
- [[Code Models]] — code security and vulnerability detection context.
- [[Safety and Alignment]] — restricted deployment for dual-use cyber capabilities.
- [[Agentic AI]] — multi-agent orchestration for combined security reports.
