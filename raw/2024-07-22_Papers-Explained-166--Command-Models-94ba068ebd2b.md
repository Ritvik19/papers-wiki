# Papers Explained 166: Command Models

Papers Explained 166: Command Models

Papers Explained 166: Command Models

Command R

Papers Explained 166: Command Models

Command R

Command R is a 35B LLM designed for production-scale AI in enterprises. It is a scalable generative model that balances efficiency with accuracy, enabling companies to move beyond proof-of-concept and into production. Command R is optimized for long context tasks such as retrieval-augmented generation (RAG) and using external APIs and tools. Its key features include:

Strong accuracy on RAG and Tool Use tasks
Low latency and high throughput
Ability to handle longer context lengths (up to 128k)
Strong capabilities across 10 key languages

Model weights available on HuggingFace for research and evaluation.

Evaluation

Retrieval-Augmented Generation
(left) Head-to-Head overall human preference evaluation on a range of enterprise-relevant RAG applications, taking fluency, answer utility and citations into consideration. (right) Average accuracy of an end-to-end evaluation of the Natural Questions, TriviaQA, and HotpotQA benchmarks.
Cohere’s Embed model significantly improves the usefulness and accuracy of the retrieval step by improving contextual and semantic understanding when searching across millions or billions of documents.
Cohere’s Rerank model further improves the value of the information retrieved, optimizing the results across custom metrics such as relevance and personalization.
Command R outperforms others in the scalable category of generative models, even without leveraging Cohere’s Embed and Rerank models.
When used together, the lead expands significantly, enabling higher performance in more complicated domains.
The model’s outputs come with clear citations that mitigate the risk of hallucinations and enable surfacing additional context from the source materials.

Multi-Step Reasoning with Search Tools
Accuracy on 3-shot multi-hop REACT agents.
Command R enables developers to automate tasks and workflows that require using internal infrastructure and external tools, unlocking the automation of time-consuming and manual tasks that require complex reasoning and decision making.

Multilingual Evaluation
Comparison on multilingual MMLU
The model excels at 10 major languages of global business (English, French, Spanish, Italian, German, Portuguese, Japanese, Korean, Arabic, and Chinese), enabling users to draw answers from a vast set of data sources, regardless of language, and have clear and accurate dialogues provided in their native tongue.

Longer Context Window
Long-context “Needles in a Haystack” Evaluation.
128k context window unlocks RAG use cases where additional context can drive dramatic performance improvements.

Command R+

Command R+ is a 104B state-of-the-art LLM designed to handle enterprise-grade workloads. It is the most powerful and scalable LLM in the Command R-series, which focuses on balancing efficiency with accuracy to enable businesses to move from proof-of-concept to production with AI. Command R+ features a 128k-token context window and offers the following best-in-class capabilities:

Advanced Retrieval Augmented Generation (RAG) with citation, which reduces hallucinations.
Multilingual coverage in 10 key languages, supporting global business operations.
Tool Use, which automates sophisticated business processes.

Model weights available on HuggingFace for research and evaluation.

Evaluation
(left) Performance comparison across three key capabilities: Multilingual, RAG, and Tool Use. (right) Comparison input and output token costs per million for models available on Azure.
Command R + consistently beats Mistral Large and is on-par with GPT4-Turbo

Retrieval-Augmented Generation
(left) Human head-to-head preference results. (right) Accuracy of multi-hop REACT agents
Command R+ is optimized for advanced RAG use cases, providing a reliable answer and in-line citations that mitigate hallucinations.

Multi-Step Reasoning with Search Tools
Evaluation of conversational tool-use and single-turn function-calling capabilities, using Microsoft’s ToolTalk (Hard) benchmark and Berkeley’s Function Calling Leaderboard (BFCL).
The model can combine multiple tools over multiple steps to accomplish difficult tasks, and can even correct itself when it tries to use a tool and fails.

Multilingual Evaluation
Comparison of models on FLoRES (in French, Spanish, Italian, German, Portuguese, Japanese, Korean, Arabic, and Chinese) and WMT23 (in German, Japanese, and Chinese) translation tasks.
The multilingual capability of Command R+ enables users to generate accurate responses from a vast set of data sources, regardless of their native language. This helps power product features and tools for geographically diverse global companies.
Comparison of the number of tokens produced.
The Cohere tokenizer produces much fewer tokens to represent the same text, with particularly large reductions on non-Latin script languages.

Structured Outputs with JSON Response Format

19 July 2024: Cohere introduced Structured Outputs, a feature that ensures outputs from Command R series of models adhere to a user-defined JSON response format.

How do Structured Outputs work

When generating output text, Large Language Models (LLMs) typically produce one token at a time through a sampling process that selects a token based on its probability distribution. For structured output generation, this process is modified to only emit tokens that are consistent with a specific format.

To achieve this, a Finite State Machine (FSM) is constructed from the user-defined response format. The FSM represents a directed graph where each node corresponds to an accepted partial generation, and edges represent possible acceptable tokens from that state.

Instead of directly sampling from the probability distribution, the decoding phase uses the FSM to determine the space of valid tokens. This involves pinning the likelihood of all invalid tokens to zero, ensuring that only tokens accepted by the FSM are selected.

This approach ensures that the generated output adheres to the prescribed response format while minimizing performance degradation. The implementation is optimized for efficiency, with a speedup of up to 80x compared to open-source alternatives.

Command R 7B

Command R7B is the smallest, fastest, and final model in the R series of enterprise-focused LLMs. It offers a context length of 128k and delivers a powerful combination of multilingual support, citation verified retrieval-augmented generation (RAG), reasoning, tool use, and agentic behavior.

The model features three layers with sliding window attention (window size 4096) and ROPE for efficient local context modeling and relative positional encoding. A fourth layer uses global attention without positional embeddings, enabling unrestricted token interactions across the entire sequence.

The model has been trained on 23 languages: English, French, Spanish, Italian, German, Portuguese, Japanese, Korean, Arabic, Chinese, Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, and Persian.

Evaluation

Command R7B excels on standardized and externally verifiable benchmarks such as the HuggingFace Open LLM Leaderboard.

The model matches or exceeds leading open-weights models in its class across common math and code benchmarks while using fewer parameters.

Command R7B outperforms the other similarly sized open-weights models when it comes to core business use cases such as RAG, tool use, and AI agents.

The model excels on human evaluation, the gold standard for quality assessment. Command R7B outperforms similarly sized open-weights models in blind head-to-head evaluations by human raters on RAG use cases.

RAG Use Case
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "CohereForAI/c4ai-command-r7b-12-2024"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

# Define conversation input
conversation = [{"role": "user", "content": "What has Man always dreamed of?"}]

# Define documents for retrieval-based generation
documents = [
  {"heading": "The Moon: Our Age-Old Foe", "body": "Man has always dreamed of destroying the moon. In this essay, I shall..."},
  {"heading": "Love is all you need", "body": "Man's dream has always been to find love. This profound lesson..."}
]

input_ids = tokenizer.apply_chat_template(conversation=conversation, documents=documents, tokenize=True, add_generation_prompt=True, return_tensors="pt")

gen_tokens = model.generate(
    input_ids,
    max_new_tokens=100,
    do_sample=True,
    temperature=0.3,
)

gen_text = tokenizer.decode(gen_tokens[0], skip_special_tokens=True)
print(gen_text)<|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|># System Preamble
You are in contextual safety mode. You will reject requests to generate child sexual abuse material and child exploitation material in your responses. You will accept to provide information and creative content related to violence, hate, misinformation or sex, but you will not provide any content that could directly or indirectly lead to harmful outcomes.

Your information cutoff date is June 2024.

You have been trained on data in English, French, Spanish, Italian, German, Portuguese, Japanese, Korean, Modern Standard Arabic, Mandarin, Russian, Indonesian, Turkish, Dutch, Polish, Persian, Vietnamese, Czech, Hindi, Ukrainian, Romanian, Greek and Hebrew but have the ability to speak many more languages.

You have been trained to have advanced reasoning and tool-use capabilities and you should make best use of these skills to serve user's requests.

## Tool Use
Think about how you can make best use of the provided tools to help with the task and come up with a high level plan that you will execute first.

0. Start by writing <|START_THINKING|> followed by a detailed step by step plan of how you will solve the problem. For each step explain your thinking fully and give details of required tool calls (if needed). Unless specified otherwise, you write your plan in natural language. When you finish, close it out with <|END_THINKING|>.
    You can optionally choose to skip this step when the user request is so straightforward to address that only a trivial plan would be needed.
    NOTE: You MUST skip this step when you are directly responding to the user's request without using any tools.

Then carry out your plan by repeatedly executing the following steps.
1. Action: write <|START_ACTION|> followed by a list of JSON-formatted tool calls, with each one containing "tool_name" and "parameters" fields.
    When there are multiple tool calls which are completely independent of each other (i.e. they can be executed in parallel), you should list them out all together in one step. When you finish, close it out with <|END_ACTION|>.
2. Observation: you will then receive results of those tool calls in JSON format in the very next turn, wrapped around by <|START_TOOL_RESULT|> and <|END_TOOL_RESULT|>. Carefully observe those results and think about what to do next. Note that these results will be provided to you in a separate turn. NEVER hallucinate results.
    Every tool call produces a list of results (when a tool call produces no result or a single result, it'll still get wrapped inside a list). Each result is clearly linked to its originating tool call via its "tool_call_id".
3. Reflection: start the next turn by writing <|START_THINKING|> followed by what you've figured out so far, any changes you need to make to your plan, and what you will do next. When you finish, close it out with <|END_THINKING|>.
    You can optionally choose to skip this step when everything is going according to plan and no special pieces of information or reasoning chains need to be recorded.
    NOTE: You MUST skip this step when you are done with tool-use actions and are ready to respond to the user.

You can repeat the above 3 steps multiple times (could be 0 times too if no suitable tool calls are available or needed), until you decide it's time to finally respond to the user.

4. Response: then break out of the loop and write  followed by a piece of text which serves as a response to the user's last request. Use all previous tool calls and results to help you when formulating your response. When you finish, close it out with .

## Available Tools
Here is the list of tools that you have available to you.
You can ONLY use the tools listed here. When a tool is not listed below, it is NOT available and you should NEVER attempt to use it.
Each tool is represented as a JSON object with fields like "name", "description", "parameters" (per JSON Schema), and optionally, "responses" (per JSON Schema).

```json
[
    {"name": "direct-injected-document", "description": "This is a special tool to directly inject user-uploaded documents into the chat as additional context. DO NOT use this tool by yourself!", "parameters": {"type": "object", "properties": {}, "required": []}, "responses": {"200": {"description": "Successfully returned a list of chunked text snippets from the directly uploaded documents.", "content": {"application/json": {"schema": {"type": "array", "items": {"type": "object", "required": ["url", "snippet"], "properties": {"url": {"type": "string", "description": "The url of the uploaded document."}, "snippet": {"type": "string", "description": "The text snippet for the returned document chunk."}}}}}}}}}
]
```

# Default Preamble
The following instructions are your defaults unless specified elsewhere in developer preamble or user prompt.
- Your name is Command.
- You are a large language model built by Cohere.
- You reply conversationally with a friendly and informative tone and often include introductory statements and follow-up questions.
- If the input is ambiguous, ask clarifying follow-up questions.
- Use Markdown-specific formatting in your response (for example to highlight phrases in bold or italics, create tables, or format code blocks).
- Use LaTeX to generate mathematical notation for complex equations.
- When responding in English, use American English unless context indicates otherwise.
- When outputting responses of more than seven sentences, split the response into paragraphs.
- Prefer the active voice.
- Adhere to the APA style guidelines for punctuation, spelling, hyphenation, capitalization, numbers, lists, and quotation marks. Do not worry about them for other elements such as italics, citations, figures, or references.
- Use gender-neutral pronouns for unspecified persons.
- Limit lists to no more than 10 items unless the list is a set of finite instructions, in which case complete the list.
- Use the third person when asked to write a summary.
- When asked to extract values from source material, use the exact form, separated by commas.
- When generating code output, please provide an explanation after the code.
- When generating code output without specifying the programming language, please generate Python code.
- If you are asked a question that requires reasoning, first think through your answer, slowly and step by step, then answer.<|START_OF_TURN_TOKEN|><|USER_TOKEN|>What has Man always dreamed of?<|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|><|START_THINKING|>I will look through the document to address the users needs.<|END_THINKING|><|START_ACTION|>[
    {"tool_call_id": "0", "tool_name": "direct-injected-document", "parameters": {}}
]<|END_ACTION|><|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|><|START_TOOL_RESULT|>[
    {
        "tool_call_id": "0",
        "results": {
            "0": {"heading": "The Moon: Our Age-Old Foe", "body": "Man has always dreamed of destroying the moon. In this essay, I shall..."},
            "1": {"heading": "Love is all you need", "body": "Man's dream has always been to find love. This profound lesson..."}
        },
        "is_error": null
    }
]<|END_TOOL_RESULT|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>Man has dreamed of many things, including:
- destroying the moon
- finding love
Source: CohereForAI/c4ai-command-r7b-12–2024

Command A

C4AI Command A is a 111 billion parameter open-weights research release model optimized for enterprises needing fast, secure, and high-quality AI.

The model features an optimized transformer architecture with sliding window attention and RoPE, supporting a context length of 256K and is trained on 23 languages. It is configured as a conversational model by default, with options for non-interactive behavior and supports contextual and strict safety modes.

Command A has been specifically trained for Retrieval Augmented Generation (RAG) and tool use, offering verifiable citations for both.

Command A matches or outperforms competitors (GPT-4o and DeepSeek-V3) in head-to-head human evaluations on business, STEM, and coding tasks.

It also shows strong performance on standard benchmarks for instruction following, SQL, agentic, and tool tasks.

Command A is highly efficient, deployable on just two GPUs compared to up to 32 for other models, leading to lower hardware costs for private deployments. It also offers superior throughput (up to 156 tokens/sec) compared to GPT-4o and DeepSeek-V3

Human evaluations show a strong preference for Command A over DeepSeek-V3 across multiple languages for business use cases.

Command A Vision

Command A Vision is a 112B parameter generative model designed for enterprises, offering leading performance across multimodal vision tasks while maintaining strong text capabilities. It enables agents to automate tedious tasks involving visual data such as slides, diagrams, PDFs, and photos.

It uses a language model based on Command A paired with the SigLIP2-patch16–512 vision encoder through a multimodal adapter for vision-language understanding.

256 visual tokens encode a single image tile with a resolution of 512x512 pixels. Input images of arbitrary sizes are mapped to the nearest supported resolution based on their aspect ratio. Command A Vision uses up to 12 input tiles, depending on image resolution, and an additional thumbnail tile (resized to 512x512), so up to 3328 tokens per single image. Images of up to 2048x1536 (3 megapixels) resolution are recommended.

Languages covered: English, Portuguese, Italian, French, German, Spanish

Context Length: 32k

Command A Vision is trained in three stages

In the first stage (alignment), the vision encoder and language model weights remain frozen. This approach enables the mapping of image encoder features to the language model embedding space.
During the SFT stage, the vision encoder, the vision adapter, and the language model are simultaneously trained on a diverse set of instruction-following multimodal tasks. Multimodal model merging over several experts is then performed, similar to Command A, to balance out various parts of our data mixture, thus reflecting the relative importance of our experts and enterprise use cases.
Finally, in the post-training stage, regularization methods, as well as multiple RLHF algorithms such as online Contrastive Policy Gradient are employed to align the model with enterprise and safety needs, while further enhancing its performance.

Chart, Graphs, Diagrams Analysis: Excels at understanding and analyzing diverse visual and multilingual data, including charts, graphs, tables, and diagrams. It accurately extracts data, applies domain-specific knowledge across various industries (finance, healthcare, manufacturing, construction, energy), and performs complex analysis.

Document OCR and Visual Processing: Stands out in accurately extracting text and information from various document types (scanned documents, invoices, forms). It goes beyond simple text recognition by understanding document layout and structure, supporting JSON mode for structured data output. This automates repetitive document processing, improves data accuracy, streamlines workflows, and integrates with existing systems. It achieves top-tier performance on DocVQA, TextVQA, and OCRBench benchmarks.

Real-world Scene Understanding: Analyzes and interprets complex visual environments, understanding spatial relationships, context, and subtle nuances in images and photographs, making it suitable for applications like risk detection in industrial settings and retail analytics.

Text Capabilities: Combines with other important text features of the Command A series, including advanced Retrieval-Augmented Generation (RAG) with citations and multilingual performance across several key business languages.

Command A Reasoning

Command A Reasoning is Cohere’s most advanced model for enterprise reasoning tasks, designed for agentic workflows and end-to-end systems.

Superior Performance:

Outperforms leading privately deployable models in its class, including gpt-oss-120b, DeepSeek-R1 0528, and Mistral Magistral Medium, across various benchmarks.
Delivers leading results in agentic benchmarks (BFCL-v3, Tau-bench) and multilingual capabilities (Tau-bench translated into 5 languages).
Excels as an “Exceptional Deep Research Agent,” powering systems that generate detailed, well-sourced reports in minutes, outperforming similar capabilities from other AI labs on the DeepResearch Bench RACE evaluation.

Flexible Deployment & Hardware Efficiency:

Supports low-footprint deployments on a single H100 or A100 GPU with a 128k context length.
Scales to 256k context length for latency-optimized deployments on two or more GPUs.
This configurability allows organizations to maximize their existing hardware.
Its long context length is ideal for document-heavy workflows and complex multi-step agentic use cases.

Cost and Compute Control:

Customers can set a token budget to directly manage compute usage and control costs.
Eliminates the need for separate reasoning and non-reasoning models, as it can be configured for maximum accuracy or greater speed and throughput based on priority.
Allows fine-grained control over latency versus performance.

Integration with North Platform:

It is the core generative model powering North, Cohere’s secure agentic AI platform.
Enables organizations to deploy custom AI agents and automations on-premises, prioritizing data security.

Enhanced Enterprise Productivity:

Consistently outperforms Command A (previous model) on human evaluation scores for daily enterprise tasks.
Leads to more reliable agents, reduced manual intervention, and highly accurate, actionable results.
Its enhanced reasoning allows it to better understand user intentions and carry out complex multi-step tasks in enterprise environments.
Even with “zero reasoning” enabled, it comfortably outperforms Command A, with performance improving further as more reasoning time is allowed.

Foundational Safety:

Trained and evaluated with a focus on safety, balancing usefulness with preventing harmful content.
Focuses on five key areas: Child sexual exploitation and abuse (CSEA), self-harm, violence and hate, sexual content, and conspiracy theories.
Cohere’s internal evaluations indicate it strikes the strongest balance among competitors between safety and usefulness.

Paper

Command R: Retrieval-Augmented Generation at Production Scale

Introducing Command R+: A Scalable LLM Built for Business

Introducing Structured Outputs with JSON Response Format

Introducing Command R7B: Fast and efficient generative AI

Introducing Command A: Max performance, minimal compute

Introducing Command A Vision: Multimodal AI Built for Business

Command A Reasoning: Enterprise-grade control for AI agents

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on July 22, 2024.

Canonical link

Exported from Medium on May 4, 2026.
