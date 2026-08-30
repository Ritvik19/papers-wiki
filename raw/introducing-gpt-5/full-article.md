---
Source URL: https://openai.com/index/introducing-gpt-5/
Fetched via: WebFetch (curl returns 403 on openai.com/index/*)
Date: August 7, 2025
---

# Introducing GPT‑5

Our smartest, fastest, most useful model yet, with built-in thinking that puts expert-level intelligence in everyone's hands.

We are introducing GPT‑5, our best AI system yet. GPT‑5 is a significant leap in intelligence over all our previous models, featuring state-of-the-art performance across coding, math, writing, health, visual perception, and more. It is a unified system that knows when to respond quickly and when to think longer to provide expert-level responses. GPT‑5 is available to all users, with Plus subscribers getting more usage, and Pro subscribers getting access to GPT‑5 pro, a version with extended reasoning for even more comprehensive and accurate answers.

## One unified system

GPT‑5 is a unified system with a smart, efficient model that answers most questions, a deeper reasoning model (GPT‑5 thinking) for harder problems, and a real‑time router that quickly decides which to use based on conversation type, complexity, tool needs, and explicit intent (for example, if you say "think hard about this" in the prompt). The router is continuously trained on real signals, including when users switch models, preference rates for responses, and measured correctness, improving over time. Once usage limits are reached, a mini version of each model handles remaining queries. In the near future, OpenAI plans to integrate these capabilities into a single model.

## A smarter, more widely useful model

GPT‑5 not only outperforms previous models on benchmarks and answers questions more quickly, but is more useful for real-world queries. Significant advances were made in reducing hallucinations, improving instruction following, and minimizing sycophancy, while leveling up GPT‑5's performance in three of ChatGPT's most common uses: writing, coding, and health.

### Coding

GPT‑5 is OpenAI's strongest coding model to date. It shows particular improvements in complex front‑end generation and debugging larger repositories. It can often create beautiful and responsive websites, apps, and games with an eye for aesthetic sensibility in just one prompt. Early testers also noted its design choices, with a much better understanding of things like spacing, typography, and white space.

### Creative expression and writing

GPT‑5 is OpenAI's most capable writing collaborator yet, able to help steer and translate rough ideas into compelling, resonant writing with literary depth and rhythm. It more reliably handles writing that involves structural ambiguity, such as sustaining unrhymed iambic pentameter or free verse that flows naturally, combining respect for form with expressive clarity.

### Health

GPT‑5 is OpenAI's best model yet for health-related questions, empowering users to be informed about and advocate for their health. The model scores significantly higher than any previous model on HealthBench, an evaluation published earlier in 2025 based on realistic scenarios and physician-defined criteria. Compared to previous models, it acts more like an active thought partner, proactively flagging potential concerns and asking questions to give more helpful answers. Importantly, ChatGPT does not replace a medical professional.

## Evaluations

GPT‑5 is much smarter across the board, as reflected by its performance on academic and human-evaluated benchmarks, particularly in math, coding, visual perception, and health. It sets a new state of the art across math (94.6% on AIME 2025 without tools), real-world coding (74.9% on SWE-bench Verified, 88% on Aider Polyglot), multimodal understanding (84.2% on MMMU), and health (46.2% on HealthBench Hard). With GPT‑5 pro's extended reasoning, the model also sets a new SOTA on GPQA, scoring 88.4% without tools.

All SWE-bench evaluation runs use a fixed subset of n=477 verified tasks which have been validated on OpenAI's internal infrastructure.

GPT‑5 shows significant gains in benchmarks that test instruction following and agentic tool use. The model excels across a range of multimodal benchmarks, spanning visual, video-based, spatial, and scientific reasoning.

GPT‑5 is also OpenAI's best performing model on an internal benchmark measuring performance on complex, economically valuable knowledge work. When using reasoning, GPT‑5 is comparable to or better than experts in roughly half the cases, while outperforming o3 and ChatGPT Agent, across tasks spanning over 40 occupations including law, logistics, sales, and engineering.

Methodology: results for GPT‑4o reflect the most recent version of the model in ChatGPT as of August 2025. All models are evaluated at high "reasoning effort" settings.

## Faster, more efficient thinking

GPT‑5 gets more value out of less thinking time. In evaluations, GPT‑5 (with thinking) performs better than OpenAI o3 with 50-80% less output tokens across capabilities, including visual reasoning, agentic coding, and graduate-level scientific problem solving.

GPT‑5 was trained on Microsoft Azure AI supercomputers.

## Building a more robust, reliable, and helpful model

### More accurate answers to real-world queries

GPT‑5 is significantly less likely to hallucinate than previous models. With web search enabled on anonymized prompts representative of ChatGPT production traffic, GPT‑5's responses are ~45% less likely to contain a factual error than GPT‑4o, and when thinking, GPT‑5's responses are ~80% less likely to contain a factual error than OpenAI o3.

New evaluations were added to stress-test open-ended factuality using LongFact (concepts and objects) and FActScore. Across these benchmarks, "GPT‑5 thinking" shows a sharp drop in hallucinations, about six times fewer than o3.

### More honest responses

Alongside improved factuality, GPT‑5 (with thinking) more honestly communicates its actions and capabilities to the user, especially for tasks which are impossible, underspecified, or missing key tools. To test this, all images were removed from the prompts of the multimodal benchmark CharXiv, and OpenAI o3 still gave confident answers about non-existent images 86.7% of the time, compared to just 9% for GPT‑5.

When reasoning, GPT‑5 more accurately recognizes when tasks can't be completed. On a large set of conversations representative of real production ChatGPT traffic, deception rates were reduced from 4.8% for o3 to 2.1% for GPT‑5 reasoning responses.

### Safer, more helpful responses

GPT‑5 advances the frontier on safety. In the past, ChatGPT relied primarily on refusal-based safety training: based on the user's prompt, the model should either comply or refuse. This works well for explicitly malicious prompts but struggles with unclear user intent or dual-use domains such as virology, where a benign request can be safely completed at a high level but might enable a bad actor if completed in detail.

For GPT‑5, OpenAI introduced a new form of safety training called **safe completions**, which teaches the model to give the most helpful answer possible while staying within safety boundaries. Sometimes that means partially answering a question or only answering at a high level. If the model needs to refuse, GPT‑5 is trained to transparently explain why, and to provide safe alternatives.

### Reducing sycophancy and refining style

GPT‑5 is less effusively agreeable, uses fewer unnecessary emojis, and is more subtle and thoughtful in follow-ups compared to GPT‑4o. Earlier in 2025, an update to GPT‑4o unintentionally made the model overly sycophantic; that change was rolled back and OpenAI worked to understand and reduce the behavior with new evaluations and training adjustments. In targeted sycophancy evaluations, GPT‑5 reduced sycophantic replies from 14.5% to less than 6%.

### More ways to customize ChatGPT

GPT‑5 is significantly better at instruction following, with a corresponding improvement in its ability to follow custom instructions. A research preview of four new preset personalities (Cynic, Robot, Listener, Nerd) was launched for all ChatGPT users, opt-in and adjustable in settings.

### Comprehensive safeguards for biological risk

OpenAI decided to treat the "GPT‑5 thinking" model as High capability in the Biological and Chemical domain under the Preparedness Framework, and implemented safeguards to minimize the associated risks, completing 5,000 hours of red-teaming with partners like CAISI and UK AISI. While there is no definitive evidence the model could meaningfully help a novice create severe biological harm, OpenAI takes a precautionary approach: threat modeling, safe-completions training, always-on classifiers and reasoning monitors, and enforcement pipelines.

## GPT‑5 pro

For the most challenging tasks, GPT‑5 pro replaces OpenAI o3‑pro: a variant of GPT‑5 that thinks for longer using scaled but efficient parallel test-time compute. In evaluations on over 1000 economically valuable, real-world reasoning prompts, external experts preferred GPT‑5 pro over "GPT‑5 thinking" 67.8% of the time, with 22% fewer major errors.

## Availability and access

GPT‑5 is the new default in ChatGPT, replacing GPT‑4o, OpenAI o3, OpenAI o4-mini, GPT‑4.1, and GPT‑4.5 for signed-in users. Pro subscribers get unlimited access to GPT‑5 and access to GPT‑5 Pro. Once free users reach their GPT‑5 usage limits, they transition to GPT‑5 mini.
