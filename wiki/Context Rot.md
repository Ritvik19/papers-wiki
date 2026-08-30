# Context Rot

#concept

Context rot is the degradation in language-model performance as input length grows, even on tasks that look trivial at short context lengths. The corpus has both a benchmarking treatment of the phenomenon in [[Papers Explained 445 - Context Rot]] and an operational treatment in [[Continually Improving Our Agent Harness]], where Cursor uses the term to describe what happens to a coding agent when failed tool calls and other mistakes accumulate inside a single session.

## Two Senses In The Corpus

[[Papers Explained 445 - Context Rot]] is the empirical foundation. It evaluates 18 LLMs (including GPT-4.1, Claude 4, Gemini 2.5, and Qwen3 variants) and shows that performance grows increasingly unreliable as input length grows, contradicting the common assumption that long-context models process context uniformly. Needle-in-a-Haystack scores stay near-perfect, but more semantic, distractor-laden, or structurally complex tasks degrade non-uniformly with length. This is the long-context-evaluation sense.

[[Continually Improving Our Agent Harness]] uses "context rot" in a more operational sense for agent transcripts. Failed tool calls do not vanish; they remain in the conversation, waste tokens, and bias later decisions. Even when the agent self-corrects, the residue of the failure pulls the model toward worse subsequent choices. This is a major reason why [[Tool Call Reliability]] is treated as a load-bearing harness signal at Cursor: every additional nine of reliability is a reduction in operational context rot.

## Implications For Harness Design

Both senses point in the same direction: more text in context does not mean more capability. Modern [[Agent Harness]] designs respond to this in two ways. First, they keep the static base of the context window small and rely on [[Dynamic Context]] for the rest, so the agent only pays for context that turns out to be necessary. Second, they invest in tool-call reliability and error classification so the transcript stays clean and short over the life of a session.

## Related

- [[Papers Explained 445 - Context Rot]]
- [[Continually Improving Our Agent Harness]]
- [[Agent Harness]]
- [[Long Context]]
- [[Dynamic Context]]
- [[Tool Call Reliability]]
- [[Context Anxiety]]
- [[Evaluation and Benchmarks]]
