# Standards Body for Frontier AI

**Type**: concept  
**Tags**: #concept

## Overview

The **Standards Body for Frontier AI** is a proposed institutional governance mechanism for frontier artificial intelligence, articulated by [[Demis Hassabis]] in July 2026. Modelled on the Financial Industry Regulatory Authority (FINRA) public-private self-regulatory organization (SRO) blueprint, it establishes a federally overseen, industry-funded body with an independent technical board to evaluate frontier-class models, conduct pre-release security testing, mandate baseline technical safeguards, and coordinate industry-wide responses to catastrophic risks.

## Governance & Institutional Architecture

- **SRO Model**: Combines statutory federal oversight with industry agility, avoiding the rigidity of purely bureaucratic agencies while establishing legally enforceable market access standards.
- **Board Composition**: Comprises independent technical experts, AI safety researchers, and open-source ecosystem representatives.
- **Funding & Compute Resources**: Primarily funded through industry contributions to ensure the body can afford world-class technical staff and the massive compute clusters necessary to perform independent capability and red-teaming evaluations.
- **Partnerships**: Collaborates closely with US federal agencies, US National Laboratories (for national security, nuclear, and CBRN evaluations), and accredited third-party auditing firms.

## Core Mechanisms

### 1. Dynamic Frontier-Class Thresholds
Models qualify as "Frontier-class" based on objective capability thresholds evaluated against a battery of regularly updated benchmarks. Organizations developing such models are designated "Frontier Labs." Smaller models, academic research, and early-stage startups below the threshold are exempt to protect innovation. The framework applies uniformly across both proprietary and open-weight models, regardless of geographic origin.

### 2. Two-Stage Pre-Release Review Gate
- **Phase 1 (Voluntary Pilot)**: Frontier labs voluntarily provide access to candidate models for evaluation up to 30 days prior to public deployment.
- **Phase 2 (Mandatory Formalization)**: Passing the Standards Body's security and safety evaluation becomes a legal requirement for deploying frontier models in the US market.
- **Post-Release Vulnerability Response**: Coordinates rapid vulnerability disclosure and patch verification for deployed systems.

### 3. High-Risk Capability & Agentic Evaluations
- **National Security & CBRN**: Rigorous empirical testing for weaponization, chemical/biological/radiological/nuclear design assistance, and critical infrastructure cyberattacks.
- **Agentic Evasion & Deception**: Specialized sandboxed tests for autonomous guardrail circumvention, sycophancy, strategic deception, and unmonitored subagent spawning.
- **Technical Safeguards Mandates**: Requires digital provenance watermarking (e.g. [[Introducing SynthID Text]]) on generated media and human-readable, un-obfuscated output tokens for reasoning chains ([[Chain of Thought Monitorability]]).

### 4. Held-Out Evaluations & Anti-Overfitting
To prevent benchmark saturation and "teaching to the test," benchmarks are reviewed quarterly, with saturated evaluations deprecated. The Standards Body creates and maintains private held-out test suites inaccessible to frontier lab training pipelines.

### 5. Coordinated Development Slowdown
The Standards Body holds the explicit authority to ratchet up safety requirements or coordinate a synchronized pause or slowdown in development across all Frontier Labs if unmanageable systemic or alignment risks are identified.

## Comparison with Existing Governance Frameworks

| Mechanism | Internal Lab Frameworks (e.g. [[Preparedness Framework]], [[Responsible Scaling Policy]]) | Proposed Standards Body for Frontier AI |
|---|---|---|
| **Enforcement** | Voluntary self-regulation; internal safety advisory committees | Federally overseen SRO; mandatory US market deployment gate |
| **Evaluations** | Lab-designed internal red-teaming and benchmark audits | Independent, held-out benchmarks + National Labs & third-party auditors |
| **Market Scope** | Applies only to the single lab's products | Applies to all Frontier Labs (open or closed, domestic or international) |
| **Coordination** | Unilateral deployment or delay decisions | Centralized mechanism to coordinate industry-wide slowdowns if needed |

## Related

- [[A Framework for Frontier AI and the Dawning of a New Age]] — Source policy essay by Demis Hassabis.
- [[Demis Hassabis]] — Author and Google DeepMind CEO.
- [[Google DeepMind]] — Research lab leadership proposing the model.
- [[Safety and Alignment]] — Master topic page for AI alignment and governance.
- [[Preparedness Framework]] — OpenAI's internal risk tracking and capability thresholds.
- [[Responsible Scaling Policy]] — Anthropic's ASL deployment criteria.
- [[Chain of Thought Monitorability]] — Alignment research requiring legible reasoning traces.
- [[Introducing SynthID Text]] — Digital provenance and watermarking infrastructure.
- [[Financial Industry Regulatory Authority]] — SRO regulatory blueprint.
