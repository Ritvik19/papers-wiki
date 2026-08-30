# Command A Reasoning: Enterprise-grade control for AI agents

**URL**: https://cohere.com/blog/command-a-reasoning  
**Published**: 2025-08-21  
**Author**: Cohere

Securely powering enterprise applications with exceptional reasoning performance, efficiency, and controllability.

---

Today, we're introducing Command A Reasoning, our most advanced model for enterprise reasoning tasks. From agentic workflows to end-to-end systems, it outperforms leading privately deployable models in its class, including gpt-oss-120b, DeepSeek-R1 0528, and Mistral Magistral Medium.

Command A Reasoning is purpose-built for enterprise needs, offering highly secure, efficient, and scalable deployment options. For low footprint deployments, it can run on a single H100 or A100 with a context length of 128k. For latency optimized deployments on two or more GPUs the context length scales to 256k. This configurability ensures organizations can make the most of the hardware available to them. The model's long context length makes it ideal for document-heavy workflows and complex multi-step agentic use cases.

Customers can set a token budget to directly manage compute usage and control costs. This eliminates the need to maintain separate reasoning and non-reasoning models, since Command A Reasoning can be used for tasks which require maximum accuracy or configured for greater speed and throughput when efficiency is the main priority.

Command A Reasoning is the core generative model powering North, our secure agentic AI platform. This empowers organizations to deploy custom AI agents and automations on-premises, backed by our most capable reasoning model.

## Agentic and multilingual reasoning benchmarks

Command A Reasoning delivers leading results across key agentic benchmarks. It also performs strongly across a range of important business languages, enabling global enterprises to leverage agents with consistent quality.

## Exceptional deep research agent

Command A Reasoning excels at powering end-to-end systems involving chained and hierarchical agents and leveraging the most relevant tools to accomplish tasks. A great example is our Deep Research system, which outperforms similar capabilities from all other leading AI labs.

Deep Research is designed to tackle the complex, in-depth questions that demand more than a quick search. It delivers detailed, well-sourced reports in minutes, which would typically take an employee hours. Our system uses a multi-agent architecture, powered by Command A Reasoning that breaks down the user request into smaller research topics. Then, multiple AI agents work in parallel, searching and analyzing information from a wide array of sources. Finally, the system consolidates the verified findings into a single, well-structured report that directly addresses the original user request. Deep Research is coming soon to North.

## Powering North, Cohere's flagship enterprise AI platform

North enables enterprises that prioritize data security to deploy AI agents and automations at scale within their own infrastructure. On human evaluation scores for a representative set of daily tasks at work, Command A Reasoning consistently outperforms Command A. For customers, these gains translate into more reliable agents, reduced manual intervention, and delivery of highly accurate, actionable results.

Command A Reasoning unlocks business applications across industries, combining strong performance, high accuracy, and scalable efficiency. Its low hardware requirements make it practical for private deployments on a single H100 or A100.

The model optimizes compute usage and costs through a user-controlled token budget, enabling seamless adjustment between mission-critical precision and high-throughput tasks. This eliminates the need for separate reasoning and non-reasoning models, allowing enterprises to maximize GPU efficiency and dynamically allocate resources.

In North's internal evaluations, adjusting the reasoning budget shows a smooth progression in performance from efficient responses at zero reasoning to more in-depth responses at higher reasoning levels. Even with zero reasoning enabled, Command A Reasoning outperforms Command A.

Safety is foundational to how we train and evaluate all our models, including Command A Reasoning. This means striking the best balance between ensuring the model doesn't over-refuse valid requests, and preventing the purposeful propagation of harmful and malicious content online. We focus on five key areas: Child sexual exploitation and abuse (CSEA), self-harm, violence and hate, sexual content, and conspiracy theories.

Command A Reasoning is available today on the Cohere platform and for research use on Hugging Face. If you are interested in private or on-prem deployments, please contact our sales team for bespoke pricing.

---

### Footnotes

**[1]** We run all models with their highest available reasoning setting. On BFCL, we evaluate command-a-reasoning using the Function Calling (FC) setting. For competitors, we report their score on the official BFCL leaderboard if available, or otherwise benchmark them using the official BFCL codebase, reporting the highest of their prompted and FC evaluation settings. On Tau-bench, we report the average of the pass^1 score over 10 runs for command-a-reasoning. For competitors, where available, we take the officially reported numbers (R1-0528, GPT-oss) otherwise we run the tool-use api against the official tau-bench implementation, reporting the average pass^1 over 10 runs. In all cases, we report the average of airline and retail. On M-tau-bench, we run all models against and report the average score across Ja, Ko, Ar, Es, Fr, and En for both retail and airline, across 10 runs.

**[2]** Our deep research agent is a hierarchical web-search agent which breaks a problem down into multiple subproblems, and recursively researches each with a sub-agent. When all subagents have finished, we take their subreports and generate a final report with a number of steps of iterative refinement, making sure our final report is strong. We use an internally developed agent and web search, leveraging our expertise in retrieval, reranking, retrieval-augmented generation and agents. We report the RACE scores for competitor models on the english questions by rerunning the official RACE evaluation on their english deep research reports on the DeepResearchBench leaderboard website.

**[3]** Annotators were asked to rate their satisfaction score based on a comprehensive internally-developed rubric, summarizing aspects of response quality, appropriateness, correctness and latency. The total evaluation set is composed of 112 questions, and each answer is annotated by 6 annotators before we aggregate their scores.

**[4]** This evaluation uses an automatic correctness score utilizing LlamaIndex, with respect to known correct reference answers.
