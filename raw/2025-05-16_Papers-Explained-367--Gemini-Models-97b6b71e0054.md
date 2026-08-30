# Papers Explained 367: Gemini Models

Papers Explained 367: Gemini Models

Papers Explained 367: Gemini Models

Gemini 2.0 Flash

Papers Explained 367: Gemini Models

Gemini 2.0 Flash

Gemini 2.0 Flash is a new, more powerful large language model (LLM) building upon the success of its predecessor, Gemini 1.5 Flash. It boasts enhanced performance, faster response times, and new capabilities centered around multimodal input and output, agentic experiences, and improved developer tools.

Multimodal Input and Output: Beyond text, Gemini 2.0 Flash supports input and output in various modalities, including:

Input: Images, video, and audio.

Output:

Natively generated images mixed with text.
Steerable text-to-speech (TTS) multilingual audio with 8 high-quality voices, various languages, and accents.

Native Tool Use: A foundational capability for building agentic experiences, Gemini 2.0 Flash can natively call tools like:

Google Search: Enabling more factual and comprehensive answers, increased traffic to publishers, and improved information retrieval through parallel searches and combining results from multiple sources.
Code Execution: Allowing for direct execution of code within the model’s workflow.
Third-Party User-Defined Functions: Expanding the model’s capabilities through custom integrations.

Coding Agents: Gemini 2.0 Flash powers coding agents capable of executing tasks on behalf of developers. Research shows a 51.8% achievement rate on SWE-bench Verified, indicating strong performance in real-world software engineering tasks. This is achieved through code execution tools and the ability to sample hundreds of potential solutions, selecting the best based on unit tests and the model’s judgment.

Image Generation Capabilities: Gemini 2.0 Flash excels in generating and manipulating images through:

Conversational image editing with multi-turn dialogues for iterative refinement and exploration.
Leveraging world knowledge and reasoning for creating detailed and realistic imagery.
Accurate rendering of long text sequences, surpassing leading competitive models in internal benchmarks.

Gemini 2.0 Flash Lite

Gemini 2.0 Flash-Lite is the latest addition to Google’s Gemini 2.0 Flash model family, designed for production use and offering significant improvements in performance and cost-effectiveness for developers. It empowers developers to build a wide range of applications. Here are some examples of how developers are using it:

Voice AI: Enables the development of responsive and natural-sounding conversational AI and voice assistants due to its fast Time-to-First-Token (TTFT) and ability to handle complex instructions and integrate with other systems through function calling. Daily, a company building voice and multimodal conversational agents, uses Gemini 2.0 Flash-Lite in their Pipecat framework to create a system that can detect voicemail systems and tailor messages accordingly.
Data Analytics: Facilitates advanced data analysis by providing reliable structured outputs and extended context capabilities. Dawn, a company focused on AI product monitoring, utilizes Gemini 2.0 Flash-Lite to significantly reduce search times in massive datasets, cut costs by over 90%, and improve reliability in production monitoring. They leverage the model’s semantic monitoring capabilities to analyze user interactions and identify anomalies or hidden problems.
Video Editing: Transforms video editing workflows by enabling AI-driven tasks through its long-context capabilities. Mosaic uses Gemini 2.0 Flash-Lite to power multimodal editing agents that can automate time-consuming tasks, such as clipping YouTube Shorts from long-form videos, significantly reducing editing time. The affordability of the model makes large context windows more accessible for these types of AI video editing tasks.

Gemini 2.5 Pro

Gemini 2.5 Pro is Google’s most advanced AI model designed for complex tasks, boasting enhanced reasoning and coding capabilities. It’s built upon the foundation of previous Gemini models, inheriting their native multimodality and long context window.

Enhanced Reasoning: Gemini 2.5 Pro excels in tasks requiring advanced reasoning. It leads in math and science benchmarks like GPQA and AIME 2025 without relying on costly test-time techniques. It achieves a state-of-the-art 18.8% score on Humanity’s Last Exam, a dataset designed to assess the limits of human knowledge and reasoning. This enhanced reasoning stems from the model’s ability to “think” before responding, analyzing information, drawing logical conclusions, and incorporating context.
Advanced Coding: A significant improvement over Gemini 2.0, 2.5 Pro demonstrates proficiency in creating visually appealing web apps, agentic code applications, code transformation, and editing. It scores 63.8% on SWE-Bench Verified, a leading industry standard for evaluating agentic code, using a custom agent setup. It can even generate executable code for a video game from a single-line prompt.
Native Multimodality: It can process and understand various data types including text, audio, images, video, and code repositories.
Long Context Window: Ships with a 1 million token context window (with a 2 million token window coming soon), enabling comprehension of vast datasets and complex problems drawing from diverse information sources. This expanded context window improves performance compared to earlier Gemini versions.
Thinking Model: Gemini 2.5 models are classified as “thinking models.” This signifies their ability to reason through problems step-by-step before providing a response, leading to improved accuracy and performance. This “thinking” capability is being integrated into all future Gemini models.

Gemini 2.5 Flash

Gemini 2.5 Flash is a new, fully hybrid reasoning model offered in preview. It builds upon the foundation of Gemini 2.0 Flash, but with significant improvements in reasoning capabilities while maintaining a focus on speed and cost-efficiency.

Hybrid Reasoning Model: This is the first Gemini model that allows developers to explicitly control the “thinking” process. This means developers can choose to enable or disable the model’s reasoning capabilities based on the specific needs of their application.
Thinking Budget: Developers can set a “thinking budget” to manage the trade-off between quality, cost, and latency. This budget determines the maximum number of tokens the model can generate during its internal reasoning process. A higher budget potentially leads to better quality answers but may increase cost and latency. Importantly, the model won’t necessarily use the entire budget; it will only use what it needs based on the complexity of the prompt. The budget can range from 0 to 24,576 tokens.
Adaptive Thinking: Even with a defined budget, Gemini 2.5 Flash is trained to assess the complexity of a given prompt and adjust its thinking time accordingly. It dynamically determines how much “thinking” is required to generate an appropriate response, ensuring efficient resource utilization.

Cost-Effective: Gemini 2.5 Flash is designed to be the most cost-efficient thinking model, offering the best price-to-performance ratio. Even with thinking turned off (budget set to 0), it can still provide performance improvements over the previous version, Gemini 2.0 Flash.

Performance on Complex Tasks: On tasks requiring multi-step reasoning (e.g., math problems, research analysis), Gemini 2.5 Flash excels. Its thinking process allows for more accurate and comprehensive answers. It performs strongly on Hard Prompts in LMArena, second only to Gemini 2.5 Pro.

Paper

Introducing Gemini 2.0: our new AI model for the agentic era
Start building with Gemini 2.0 Flash and Flash-Lite
Experiment with Gemini 2.0 Flash native image generation
Gemini 2.5: Our most intelligent AI model
Start building with Gemini 2.5 Flash

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on May 16, 2025.

Canonical link

Exported from Medium on May 4, 2026.
