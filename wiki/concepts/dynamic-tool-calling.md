# Dynamic Tool Calling

**Type**: concept  
**Tags**: #concept

## Overview

**Dynamic tool calling** is a harness optimization where native tool descriptions are not loaded into every agent prompt upfront. Instead, the model looks up a tool's description the first time it needs that tool — the same lazy-loading pattern Cursor already uses for MCP servers. Common tools like read and edit stay hot in the prompt; less frequently used tools enter context only when actually invoked.

## Appearances

- [[Introducing Cursor Router]] — previewed in "What's next" alongside Cursor Router as another token-efficiency improvement in the agent harness.

## Notes

- Complements [[Cursor Router]] model routing: choosing the right model only helps if the harness itself stays lean.
- Parallel to MCP lookup pattern described in [[Continually Improving Our Agent Harness]] and [[Agent Harness]].

## Related

- [[Agent Harness]]
- [[Continually Improving Our Agent Harness]]
- [[Cursor Router]]
- [[Tool Call Reliability]]
