Source URL: https://huggingface.co/blog/openenv-turing
Title: OpenEnv in Practice: Evaluating Tool-Using Agents in Real-World Environments

# OpenEnv in Practice: Evaluating Tool-Using Agents in Real-World Environments

Published February 12, 2026

Christian Washington, Ankit Jasuja, Santosh Sah (Turing), Lewis Tunstall, Ben Burtenshaw (Hugging Face)

AI agents often perform impressively in controlled research settings, yet struggle when deployed in real-world systems where they must reason across multiple steps, interact with real tools and APIs, operate under partial information, and recover from errors in stateful, permissioned environments, highlighting a persistent gap between research success and production reliability.

OpenEnv is an open-source framework from Meta and Hugging Face designed to address this by standardizing how agents interact with real environments. As part of this collaboration, Turing contributed a production-grade calendar management environment to study tool-using agents under realistic constraints such as access control, temporal reasoning, and multi-agent coordination.

## What is OpenEnv?

OpenEnv evaluates AI agents against real systems rather than simulations. It provides a standardized way to connect agents to real tools and workflows while preserving the structure needed for consistent, reliable evaluation. It uses a gym-oriented API (`reset`, `step`, `action`, `observations`) similar to OpenAI's Gymnasium, and a standard MCP tool-call interface, giving a consistent interface across domains from simulation to production. Environments maintain state across multiple actions, enabling long-horizon reasoning, and can connect directly to real APIs and tools such as browsers, code repositories, or calendars. This shifts evaluation from "can this work in a controlled demo?" to "can this operate reliably in the real world?"

## The Calendar Gym: a production-grade benchmark

Calendar systems are deceptively complex: real-world calendar management requires agents to reason over time, permissions, multiple users, and incomplete information, often across several dependent steps. Turing built a production-grade calendar environment called the Calendar Gym, exposing agents to Access Control Lists across users and calendars, limited visibility into other users' state, and multi-step workflows where actions must be chained in the correct order. Agents interact with a rich set of calendar operations (listing calendars, creating/modifying events and permissions) and must handle failed actions, incorrect assumptions, and missing permissions. Each session runs in an isolated environment for reliable comparisons across runs.

Example usage:

```python
from openenv_wrapper.client import MCPEnvClient
from openenv_wrapper.data_models import MCPAction

with MCPEnvClient.from_hub(base_url="TuringEnterprises/calendar-gym") as client:
    result = client.reset()
    result = client.step(MCPAction(action_type="ListToolsAction"))
    result = client.step(MCPAction(
        action_type="ToolCallAction",
        tool_name="calendars_list",
        arguments={}
    ))
    calendars = result.observation.tool_result["items"]
    result = client.step(MCPAction(
        action_type="ToolCallAction",
        tool_name="events_insert",
        arguments={
            "calendarId": "primary",
            "summary": "Team Sync",
            "start": {"dateTime": "2026-01-15T14:00:00Z"},
            "end": {"dateTime": "2026-01-15T15:00:00Z"},
        }
    ))
```

`ListToolsAction` returns each tool's name plus an input JSON schema, e.g. `calendars_list` (no arguments) and `events_insert` (requires `calendarId`, `summary`, `start`, `end`, each with typed sub-fields).

## What we learned

Evaluating agents in the Calendar Gym revealed patterns common across domains: agents perform well on individual, game-like actions, but reliability breaks down as tasks become longer, more ambiguous, and more constrained.

- **Multi-step reasoning is the primary bottleneck.** Agents struggle to correctly chain actions across longer workflows, suggesting benchmarks need to test sustained reasoning over multiple dependent steps, not just single tool calls.
- **Ambiguity significantly degrades performance.** Agents achieved close to 90% success on tasks with explicit calendar identifiers, but success dropped to roughly 40% when the same tasks were phrased with natural language descriptions. Stronger lookup and validation built into agent loops (rather than relying on the LLM to resolve references unaided) appears essential.
- **Correct tool choice isn't enough.** Across failed interactions, more than half of errors stemmed from malformed tool arguments or incorrect ordering, even when the right tool was selected; execution quality and structured feedback matter as much as tool selection.

These limitations are not unique to scheduling; they reflect broader issues that emerge whenever agents operate in changing systems over long periods, pointing toward evaluation frameworks that test permissions, partial observability, and multi-step workflows together.

## Appendix: common error cases in tool use

Three recurring failure modes when wiring MCP tools to real APIs:

1. **Schema validation errors** (missing/malformed arguments, e.g. missing `calendarId`, incorrect nesting of `start`/`end`, wrong types). Mitigation: provide one canonical example of a correct call in the prompt; return structured validation errors so the model can repair and retry.
2. **Permission/authorization errors (401/403)** (missing OAuth scopes, expired tokens, insufficient calendar access). Mitigation: clearly document required OAuth scopes; return structured, actionable remediation steps.
3. **Datetime/format errors (RFC3339 & timezone issues)** (missing timezone offset, non-RFC3339 format, mixing local time and UTC without an offset). Mitigation: standardize on RFC3339 with explicit timezone offsets and include a correct example in documentation.

For the full technical write-up on the Calendar Gym's design, benchmarking methodology, and quantitative results, see Turing's site; a clone of the Calendar Gym is available as a Hugging Face Space.
