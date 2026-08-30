# Open-Source DeepResearch - Freeing Our Search Agents

**Source**: `raw/open-deep-research/full-article.html`, `raw/open-deep-research/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

A Hugging Face post documenting a 24-hour sprint to open-source-reproduce OpenAI's Deep Research (a web-browsing agent that summarizes and answers questions from live search) on the GAIA benchmark, a difficult multi-step, multi-tool agentic QA benchmark. GAIA questions typically require chaining several sub-tasks with dependencies (e.g. identifying objects in an image, resolving a historical reference, then retrieving and filtering a specific document), and expose why plain LLMs struggle without an agentic framework: GPT-4 without tooling scores under 7% on GAIA's validation set, versus OpenAI's reported 67.36% with the full Deep Research system.

The team's key architectural choice was a "code agent" from the `smolagents` library: instead of having the LLM emit actions as JSON tool calls (the conventional agent-framework pattern), the agent writes and executes Python code directly to express its actions. Citing prior work (Wang et al., 2024), the post argues code actions are more concise (avoiding one JSON blob per action when several parallel/sequential steps are needed, cutting token usage ~30%), let the agent reuse standard library tooling, and handle multi-step state more naturally (e.g. an image loaded mid-trajectory can just be assigned to a variable and reused later, rather than requiring the LLM to invent and remember a dictionary key). The agent's toolset, a simple text-based web browser and a text-file inspector, was adapted from Microsoft Research's Magentic-One agent with minimal changes, in the interest of maximizing performance for minimal added complexity.

The resulting open agent reached 55.15% on GAIA's validation set, a jump from the prior open-framework state of the art (~46%, Magentic-One) and a large gap above a JSON-action version of the same setup (33% when the same agent is forced to write actions as JSON rather than code), isolating the code-agent design as the primary driver of the improvement. The team explicitly frames this as a starting point rather than parity with OpenAI's system, since Deep Research's full capability likely depends on more sophisticated browser interaction (comparable to OpenAI's Operator) beyond the simple text-only browser used here; GUI-capable "agents that view your screen and act with mouse & keyboard" are flagged as the next major investment. A companion, later HF post ([[Harness, Scaffold, and the AI Agent Terms Worth Getting Right]]) revisits and formalizes several terms this post uses informally (agent, agentic framework, code agent).

## Key Claims

- GAIA benchmark gap: GPT-4 without an agentic framework scores under 7% on GAIA validation; OpenAI's Deep Research reports 67.36% (near 1-shot average) and 47.6% on especially hard "level 3" multi-step questions.
- The reproduction's key design choice is a "code agent" (via `smolagents`) that writes Python code for its actions rather than JSON tool calls; cited prior work reports ~30% fewer steps/tokens for code actions vs. JSON on average.
- Result: 55.15% on GAIA validation with the code-agent setup, up from the prior open-framework best of ~46% (Magentic-One); the same setup forced to emit JSON actions instead of code drops to 33%, isolating the code-agent choice as the main performance driver.
- Toolset (simple text-based web browser, text-file inspector) is adapted from Microsoft Research's Magentic-One agent with minimal modification.
- The team explicitly does not claim parity with OpenAI's Deep Research, citing its own text-only browser as a known gap versus OpenAI Operator-level browser interaction; building GUI/mouse-keyboard-capable agents is named as the top next priority.
- Several community reproductions of Deep Research-style agents emerged concurrently from outside Hugging Face (cited: dzhng, assafelovic, nickscamara, jina-ai, mshumer), each using different indexing/browsing/LLM-querying stacks.

## Figures

No figures were extracted for this ingest, per this batch's no-figure-download policy; the benchmark comparison chart and code-agent diagram referenced in the post were not downloaded.

## Entities

- [[Hugging Face]] — runs the sprint and builds/publishes the `smolagents` library and reproduction.
- [[OpenAI]] — original Deep Research system being reproduced.
- [[Microsoft]] — Microsoft Research's Magentic-One agent supplies the initial web-browser and text-inspector tools.
- [[DeepSeek]] — DeepSeek R1 is cited as a contemporaneous open reasoning model the team planned to evaluate as the agent's backing LLM.

## Questions & Gaps

- No private-test-set score is available for either OpenAI's Deep Research or this reproduction, only public validation-set numbers, so the reported gap could shift on held-out data.
- The post does not report which specific LLM backed the 55.15% GAIA result, framing the number as a snapshot from an actively-improving, still-in-progress system.

## Related

- [[Harness, Scaffold, and the AI Agent Terms Worth Getting Right]] — later HF post formalizing the agent/harness/scaffold vocabulary used informally here.
