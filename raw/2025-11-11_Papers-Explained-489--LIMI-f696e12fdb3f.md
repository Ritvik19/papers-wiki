# Papers Explained 489: LIMI

Papers Explained 489: LIMI

Papers Explained 489: LIMI

Agency is defined as the emergent capacity of AI systems to function as autonomous agents — actively discovering problems, formulating…

Papers Explained 489: LIMI

Agency is defined as the emergent capacity of AI systems to function as autonomous agents — actively discovering problems, formulating hypotheses, and executing solutions through self-directed engagement with environments and tools.

Current approaches assume that more data yields better agency, following traditional scaling laws from language modeling. LIMI (Less Is More for Intelligent Agency) demonstrates that agency follows radically different development principles. Using only 78 carefully designed training samples, LIMI achieves 73.5% on AgencyBench, dramatically outperforming state-of-the-art models: Kimi-K2-Instruct (24.1%), DeepSeek-V3.1 (11.9%), Qwen3–235B-A22B-Instruct (27.5%), and GLM-4.5 (45.1%).

The dataset and model are available at HuggingFace.

Preliminary

The development of agentic intelligence is primarily tested through complex, multi-step challenges referred to as “long-horizon tasks.” These tasks require sustained cognitive effort and strategic coordination over extended interaction sequences. A single user query can encompass multiple interconnected subtasks across planning, execution, and collaboration.
An example of the user query.
Such tasks demand sophisticated integration of several capabilities:

Autonomous Task Execution: The ability to carry out tasks independently.
Multi-step Reasoning: Processing information and making decisions over multiple stages.
Collaborative Problem-Solving: Working effectively with humans or other agents to achieve a goal.

These tasks exhibit specific characteristics that distinguish them:

Temporal Complexity: Involve multi-round interactions, requiring coherent state tracking and cumulative reasoning.
Strategic Planning Capabilities: Decompose complex objectives into manageable sub-goals and adapt strategies based on environmental feedback.
Tool Orchestration: Require coordinated use of multiple systems with integrated result processing, essential for real-world agentic tasks.
Collaborative Communication: Ensures effective human-AI coordination throughout extended problem-solving processes, differentiating agentic intelligence from passive AI systems that merely respond to individual queries.

These complex tasks are relevant across diverse domains, including software development and scientific research.

To validate their approach, the authors focus on two fundamental domains that collectively span the majority of knowledge work scenarios and require the full spectrum of agentic capabilities:

Vibe Coding

Represents collaborative software development where LLMs or agents work alongside human developers in natural, context-rich environments. The complexity lies in a holistic understanding of development contexts and principled decision-making under evolving requirements. It demands:

Code understanding and generation across existing codebases.
Development environment navigation through complex tool ecosystems.
Iterative problem solving through debugging and optimization cycles.
Collaborative communication for technical coordination.

Research Workflows

Encompasses scenarios where agents navigate complex scientific processes, for example: Literature search, data analysis, experiment design, and insight generation. It requires sophisticated reasoning, spanning from creative hypothesis generation to rigorous analytical execution. It demands:

Information synthesis from diverse sources.
Experimental design with appropriate methodologies.
Data analysis and interpretation of complex results.
Knowledge communication across different stakeholder formats.

Dataset Construction
LIMI Data Construction Pipeline.
Each complete interaction is defined as a tuple (qi, τi), where qi is a query and τi is a trajectory.

Query (qi): The foundational natural language specification from the user articulating the desired objective. Queries range from software development requirements (vibe coding) to research tasks (scientific workflows) and establish both the starting point and success criteria.

Trajectory (τi): Captures the subsequent collaborative sequence following the initial query, represented as {ai,1, . . . , ai,ni}. Each action ai,j is one of three fundamental interaction types:

Model Reasoning (mi,j): The agentic model’s output demonstrating understanding, analysis, planning, and decision-making.
Model Tool Calling (ti,j): Structured tool invocations executed by the model to interact with external environments and accomplish subtasks.
Environment Observation (oi,j): Results and outputs from tool executions, user feedback, and clarifications that inform subsequent model reasoning cycles.
j maintains temporal ordering, and ni is the total number of actions for query i resolution.

Query Pool Construction

The query collection strategy combines authentic real-world scenarios with systematically expanded coverage to ensure both ecological validity and sufficient training diversity for agentic intelligence development.

Real-world Query Collection 60 queries were collected from actual scenarios encountered by professional developers and researchers in collaborative environments. The domains covered software development and research workflows. A substantial portion of the research queries are derived from real academic papers.

GitHub PR-based Query Synthesis A pipeline using GPT-5 (OpenAI) was developed to synthesize additional queries from GitHub Pull Requests (PRs) to expand the pool while maintaining authenticity.

Repository Selection: Repositories with >10,000 GitHub stars were chosen for high-quality, well-maintained codebases.
Domain Diversification: Ensured comprehensive coverage across diverse software development domains (frontend, backend, deployment, debugging, code optimization), selecting 100 repositories.
Complexity Filtering: PRs filtered based on unified diff patch token count (below 1,200 tokens) and excluded those only modifying Markdown files, focusing on substantive code changes.
Scale and Sampling: 1,000 PRs collected per repository from 100 selected repositories, then 100 PRs randomly sampled from each for query synthesis.
Quality Assurance: Four PhD students in computer science evaluated synthesized queries for semantic alignment with corresponding PR content.

Several thousand high-quality synthetic queries were generated. 18 queries were strategically sampled to match vibe coding and research workflows, ensuring optimal coverage.

Trajectory Collection for Training Dataset

To generate training trajectories demonstrating optimal agentic behavior, a sophisticated execution environment enabling authentic human-AI collaboration is required. SII CLI was chosen due to:

Comprehensive tool integration for both vibe coding and research workflows.
Detailed trajectory logging capabilities.
Flexible human-AI collaboration interfaces.
Robust support for complex multi-step tasks requiring coordinated tool usage.
SII CLI provides a comprehensive toolkit for software development, research activities, and information processing within a unified interface.

Four PhD student annotators served as human collaborators, working with GPT-5 as the agentic model. The methodology employed an iterative collection approach, continuously gathering trajectories until successful completion for each query qi. Trajectories capture extensive interaction sequences, with the longest reaching 152k tokens, demonstrating depth and complexity. The average trajectory length is 42.4k tokens.

Experiment Setup

Both GLM-4.5 and GLM-4.5-Air are fine-tuned using the training dataset. To assess the quality and effectiveness of the data curation strategy, comparative experiments are conducted by fine-tuning GLM-4.5 on three alternative datasets: CC-Bench-trajectories, AFM-WebAgent-SFT-Dataset, and AFM-CodeAgent-SFT-Dataset. Evaluation is performed against a diverse set of state-of-the-art foundation models to ensure comprehensive comparison: GLM-4.5, GLM-4.5-Air, Qwen3–235B-A22B-Instruct, DeepSeek-V3.1, and Kimi-K2-Instruct.

Evaluation Benchmarks

AgencyBench, designed for assessing agentic capabilities in collaborative scenarios, Contains carefully curated tasks reflecting the complexity and collaborative nature of real-world agentic scenarios across vibe coding and research workflows:
Agency Bench Task Overview.
Metrics:

First-Turn Functional Completeness (FTFC): Percentage of requirements correctly implemented in the initial response.
Success Rate (SR@R): Percentage of queries successfully completed within R allocated rounds.
Remaining Chances (RC@R): Average number of unused rounds when queries are successfully completed, measuring computational efficiency.

To assess capabilities beyond core domains, models are evaluated on established benchmarks:

Tool Use: tau2-bench-airline and tau2-bench-retail
Code Generation: evalplus-humaneval and evalplus-mbpp.
Data Science & Code Generation: DS-1000.
Scientific Computing: SciCode.

Evaluation
Comparison of models on AgencyBench.
LIMI significantly outperforms all baseline models on AgencyBench, achieving an average score of 73.5%.
LIMI shows a substantial improvement in first-turn functional completeness (FTFC) on AgencyBench, achieving 71.7% compared to the best baseline’s 37.8%.
LIMI demonstrates superior task completion reliability on AgencyBench, with a 74.6% success rate compared to the strongest baseline’s 47.4%.
LIMI significantly outperformed GLM-4.5-Code on AgencyBench, achieving 73.5% performance compared to 47.8%, despite using 128 times fewer training samples (78 vs. 10,000).
LIMI-Air (106B) significantly outperforms GLM-4.5-Air, with AgencyBench performance increasing from 17.0% to 34.3% (a 17.3 percentage point improvement).
LIMI (355B) significantly outperforms GLM-4.5, improving from 45.1% to 73.5%.
The consistent improvement across different model scales suggests that the strategic data curation methodology captures fundamental patterns of agentic behavior that transfer effectively regardless of model capacity.
Performance comparison across generalization benchmarks.
LIMI’s superiority extends across established benchmarks spanning tool use, coding, and scientific computing domains, with an average performance of 57.2%.
LIMI achieves high performance on coding benchmarks (EvalPlus-HumanEval: 92.1%, EvalPlus-MBPP: 82.3%) and competitive results on tool use tasks (TAU2-bench-airline: 34.0%, TAU2-bench-retail: 45.6%).
The consistent performance advantages across diverse evaluation domains demonstrate that the data curation approach yields broad improvements in model capabilities.
LIMI establishes itself as the new state-of-the-art for agentic intelligence across multiple evaluation dimensions.
LIMI outperformed GLM-4.5-Code, GLM-4.5-Web and GLM-4.5-CC across tool use, coding, and scientific computing tasks, despite using significantly fewer samples.
Performance comparison on generalization benchmarks without CLI environment access.
LIMI maintains a competitive advantage even without tool access, achieving 50.0% average performance compared to GLM-4.5’s 48.7%.
LIMI outperforms all external baseline models (GLM-4.5, Kimi-K2-Instruct, DeepSeek-V3.1, and Qwen3–235B-A22B-Instruct) in the tool-free evaluation.
LIMI shows a 7.2 percentage point improvement when tools are available (57.2% with CLI access vs. 50.0% without).

Paper

LIMI: Less is More for Agency 2509.17567

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on November 11, 2025.

Canonical link

Exported from Medium on May 4, 2026.
