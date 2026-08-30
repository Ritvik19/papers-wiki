# Papers Explained 139: Gorilla

Papers Explained 139: Gorilla

Papers Explained 139: Gorilla

Gorilla is retrieve-aware finetuned LLaMA-7B model, specifically for API calls. It substantially mitigates the issue of hallucination…

Papers Explained 139: Gorilla

Gorilla is retrieve-aware finetuned LLaMA-7B model, specifically for API calls. It substantially mitigates the issue of hallucination, commonly encountered when prompting LLMs directly. To evaluate the model’s ability, APIBench, a comprehensive dataset consisting of HuggingFace, TorchHub, and TensorHub APIs is also introduced. The successful integration of the retrieval system with Gorilla demonstrates the potential for LLMs to use tools more accurately, keep up with frequently updated documentation, and consequently increase the reliability and applicability of their outputs.

Methodology

Data Collection

Data is collected from various sources, specifically HuggingFace’s Model Hub, PyTorch Hub, and TensorFlow Hub Models. These sources contain a large number of machine learning models.

Filtering Models: To ensure data quality, top 20 models are selected from each of seven domains (multimodal data, computer vision, natural language processing, audio, tabular data, and reinforcement learning). This filtering resulted in a reduced dataset.

Data Processing: The information for each of the selected models is converted into a structured JSON format, including fields such as domain, framework, functionality, API name, API call, and more. This structured data is used for analysis.

Instruction Generation: GPT-4 is used to generate synthetic instruction data. This model is provided with in-context examples and API documentation to generate real-world use cases that utilize the APIs. Importantly, the model is instructed not to include explicit API names or hints in the generated instructions.

Data Expansion: From the six examples (instruction-API pairs) created for each of the three model hubs, a total of 10 instruction-API pairs are generated for each of the 1,645 API data points. This expanded dataset is used for the research.

Gorilla

API Call with Constraints: API calls often come with limitations or constraints. These constraints require the LLM not only to understand what the API call is supposed to do but also to categorize the calls based on different constraint parameters. Common constraints for machine learning API calls include parameter size and minimum accuracy requirements. These constraints add complexity to the LLM’s understanding, as it must interpret both the user’s request and the embedded constraints.

Retriever-Aware Training: To train the LLM effectively, an instruction-tuned dataset is used, which includes an additional reference to API documentation. This reference is meant to teach the LLM to use the provided documentation to answer the user’s query effectively. It helps the LLM adapt to changes in the API documentation, improves performance through in-context learning, and reduces errors related to generating incorrect information. Surprisingly, augmenting an LLM with retrieval methods doesn’t always lead to better performance and can, in some cases, hinder it.

Gorilla Inference: During inference, users provide prompts in natural language. These prompts can be simple task descriptions or vague goals. Gorilla, the LLM model, can operate in two modes: zero-shot and with retrieval.

In zero-shot mode, the user’s prompt is directly given to Gorilla, which returns the API call needed to accomplish the task or goal without further tuning.
In retrieval mode, a retriever (BM25 or GPT-Index) first retrieves the most up-to-date API documentation from the API Database. This documentation is then combined with the user’s prompt, including a reference message. The concatenated input is then fed to Gorilla to determine the API to be invoked.

Verifying APIs

Inductive Program Synthesis is a technique where a program is automatically generated to meet certain test cases or requirements.

While inductive program synthesis works well with regular code, it faces challenges when dealing with API calls. It’s difficult to ensure the correctness of API calls using test cases alone. For example, when classifying an image, there are many possible models and configurations, making it hard to verify if the API being used is functionally equivalent to a reference API through unit tests.

To evaluate the performance of a model that uses APIs, the functional equivalence of the APIs are compared using a dataset collected. An AST (Abstract Syntax Tree) Subtree matching strategy is employed to trace which API calls the model is using. It involves comparing the structure of the ASTs for API calls, including their arguments. This matching process helps determine if an API call in the dataset matches the reference API being examined.

Experiment Setup

Baselines

GPT-4 (gpt-4–0314 checkpoint)
GPT-3.5-turbo (gpt-3.5-turbo-0301 checkpoint)
Claude (claude-v1 checkpoint)
LLaMA-7B

Retrievers

Zero-shot scenarios involve no retriever, with the user’s natural language prompt as the only input to the model.
For BM25, each API is treated as a separate document, and the user’s query is used for retrieval to fetch the top-1 relevant API, which is then concatenated with the user’s prompt for LLMs.
GPT-Index, similar to BM25, treats each API call as an individual document, retrieves the most relevant one for a user query, and appends it to the user prompt.
An Oracle retriever is used for two purposes: performance improvement evaluation and aiding users who know which API to use but need help invoking it. This retriever is appended to the user’s prompt with a specific format.

Results

AST Accuracy on API call

Experiments involve testing different models for AST accuracy.
Reported metrics include overall accuracy, error due to hallucination, and error due to selecting the wrong API call.
TorchHub and TensorHub models are evaluated using AST tree accuracy score.
For HuggingFace, models (except Gorilla) are evaluated based on their ability to provide correct domain names.

Finetuning without Retrieval

Lightly fine-tuned Gorilla outperforms all models in a zero-shot scenario. It achieves a 20.43% improvement over GPT-4 and a 10.75% improvement over ChatGPT.
Compared to other open-source models like LLAMA, the improvement is as significant as 83%. This suggests that fine-tuning is more effective than retrieval.
Fine-tuning without a retriever and using a ground truth retriever at evaluation time doesn’t significantly improve performance; it’s only 0.88% worse in TensorHub and 0.97% better in HuggingFace.
Adding BM25 or GPT-Index as retrievers during evaluation leads to significant performance drops: 21.50% in Torch Hub and 47.57% in HuggingFace.
These results indicate that using a non-optimal retriever during test time can sometimes misguide the model and result in more errors.

Finetuning with Retrieval

Incorporating a ground truth retriever in the finetuning process leads to significantly better results: 12.37% improvement in Torch Hub. 23.46% improvement in HuggingFace.
However, current retrievers still have a substantial performance gap compared to ground truth retriever at evaluation time: GPT-Index results in a 29.20% accuracy degradation. BM25 results in a 52.27% accuracy degradation.
Despite the retriever’s limitations, finetuning with retriever is still a preferable method when a better retriever is available.
In cases where a good retriever is not available, zero-shot finetuning might be the preferred choice.

Hallucination with LLM

Zero-shot prompting with LLMs (GPT-4/GPT-3.5) for API calls leads to dire hallucination errors.
Surprisingly, GPT-3.5 has fewer hallucination errors than GPT-4 when used in TorchHub, HuggingFace, and TensorFlow Hub.
This finding holds true across different retrieval methods: 0-shot, BM25, GPT-Index, and the oracle.
This suggests that RLHF (Reinforcement Learning from Human Feedback) plays a crucial role in making the model more truthful.

Test-Time Documentation Change

Gorilla’s retriever-aware training helps LLMs stay updated and relevant despite changes in the documentation, thus effectively adapting to changes in APIs and model registries.

API Call with Constraints

Accuracy drop with constraints observed across all models.
Gorilla’s performance: Matches GPT-3.5 with retrievals (BM25, GPTIndex), highest accuracy in Zero-shot.

Paper

Gorilla: Large Language Model Connected with Massive APIs 2305.15334

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on May 20, 2024.

Canonical link

Exported from Medium on May 4, 2026.
