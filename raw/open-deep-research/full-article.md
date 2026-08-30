Source URL: https://huggingface.co/blog/open-deep-research
Title: Open-source DeepResearch – Freeing our search agents

Hugging Face's logo Hugging Face 

* Models
* Datasets
* Spaces
* Buckets new
* Docs
* Enterprise
* Pricing
* * Website  
         * Tasks  
         * HuggingChat  
         * Collections  
         * Languages  
         * Organizations  
   * Community  
         * Blog  
         * Posts  
         * Daily Papers  
         * Hardware  
         * Learn  
         * Discord  
         * Forum  
         * GitHub  
   * Solutions  
         * Team & Enterprise  
         * Hugging Face PRO  
         * Enterprise Support  
         * Inference Providers  
         * Inference Endpoints  
         * Storage Buckets
* ---
* Log In
* Sign Up

 Back to Articles

#  Open-source DeepResearch – Freeing our search agents 

Published February 4, 2025 

Update on GitHub

 Upvote 1320 
* +1314

Aymeric Roucher's avatar 

Aymeric Roucher m-ric Follow 

Albert Villanova del Moral's avatar 

Albert Villanova del Moral albertvillanova Follow 

merve's avatar 

merve merve Follow 

Thomas Wolf's avatar 

Thomas Wolf thomwolf Follow 

Clémentine Fourrier's avatar 

Clémentine Fourrier clefourrier Follow 

## 

* TLDR
* Table of Contents
* What are Agent frameworks and why they matter?
* The GAIA benchmark
* Building an open Deep Research  
   * Using a CodeAgent  
   * Making the right tools 🛠️
* Results 🏅
* Community Reproductions
* Most important next steps

 TLDR 

Yesterday, OpenAI released Deep Research, a system that browses the web to summarize content and answer questions based on the summary. The system is impressive and blew our minds when we tried it for the first time.

One of the main results in the blog post is a strong improvement of performances on the General AI Assistants benchmark (GAIA), a benchmark we’ve been playing with recently as well, where they successfully reached near 67% correct answers on 1-shot on average, and 47.6% on especially challenging “level 3” questions that involve multiple steps of reasoning and tool usage (see below for a presentation of GAIA).

DeepResearch is composed of an LLM (which can be selected from the current list of LLMs provided by OpenAI, 4o, o1, o3, etc) and an internal “agentic framework” which guide the LLM to use tools like web search and organize its actions in steps. 

While powerful LLMs are now freely available in open-source (see e.g. the recent DeepSeek R1 model), OpenAI didn’t disclose much about the agentic framework underlying Deep Research…

So we decided to embark on a 24-hour mission to reproduce their results and open-source the needed framework along the way!

The clock is ticking, let’s go! ⏱️

##  Table of Contents 

* Open-source DeepResearch – Freeing our search agents  
   * TLDR  
   * Table of Contents  
   * What are Agent frameworks and why they matter?  
   * The GAIA benchmark  
   * Building an open Deep Research  
         * Using a CodeAgent  
         * Making the right tools 🛠️  
   * Results 🏅  
   * Community Reproductions  
   * Most important next steps

##  What are Agent frameworks and why they matter? 

> An Agent framework is a layer on top of an LLM to make said LLM execute actions (like browse the web or read PDF documents), and organize its operations in a series of steps. For a quick intro to agents, check this great interview by Andrew Ng and our introduction blog post to the smolagents library. For a more detailed dive in agents you can subscribe to our agents course that starts in just a few days: link here.

Almost everyone has already experienced how powerful LLMs can be simply by playing with chatbots.. However, what not everyone is aware of yet is that integrating these LLMs into agentic systems can give them real superpowers! 

Here is a recent example comparing the performance of a few frontier LLMs with and without an agentic framework (in this case the simple smolagents library) - using an agentic framework bumps performance by up to 60 points!

Benchmarks

In fact, OpenAI also highlighted in its release blogpost how Deep Research performed dramatically better than standalone LLMs on the knowledge-intensive "Humanity’s Last Exam" benchmark.

So, what happens when we integrate our current top LLM in an agentic framework, to work toward an `open-DeepResearch` ?

**A quick note:** We’ll benchmark our results on the same GAIA challenge but keep in mind that this is a work in progress. DeepResearch is a massive achievement and its open reproduction will take time. In particular, full parity will require improved browser use and interaction like OpenAI Operator is providing, i.e. beyond the current text-only web interaction we explore in this first step.

Let’s first understand the scope of the challenge: GAIA.

##  The GAIA benchmark 

GAIA is arguably the most comprehensive benchmark for agents. Its questions are very difficult and hit on many challenges of LLM-based systems. Here is an example of a hard question:

> Which of the fruits shown in the 2008 painting "Embroidery from Uzbekistan" were served as part of the October 1949 breakfast menu for the ocean liner that was later used as a floating prop for the film "The Last Voyage"? Give the items as a comma-separated list, ordering them in clockwise order based on their arrangement in the painting starting from the 12 o'clock position. Use the plural form of each fruit.

You can see this question involves several challenges:

* Answering in a constrained format,
* Using multimodal capabilities (to extract the fruits from the image),
* Gathering several pieces of information, some depending on others:  
   * Identifying the fruits on the picture  
   * Finding which ocean liner was used as a floating prop for “The Last Voyage”  
   * Finding the October 1949 breakfast menu for the above ocean liner
* Chaining together a problem-solving trajectory in the correct order.

Solving this requires both high-level planning abilities and rigorous execution, which are two areas where LLMs struggle when used alone.

So it’s an excellent test set for agent systems!

On GAIA’s public leaderboard, GPT-4 does not even reach 7% on the validation set when used without any agentic setup. On the other side of the spectrum, with Deep Research, OpenAI reached 67.36% score on the validation set, so an order of magnitude better! (Though we don’t know how they would actually fare on the private test set.)

Let’s see if we can do better with open source tools!

##  Building an open Deep Research 

###  Using a CodeAgent 

The first improvement over traditional AI agent systems we’ll tackle is to use a so-called “code agent”. As shown by Wang et al. (2024), letting the agent express its actions in code has several advantages, but most notably that **code is specifically designed to express complex sequences of actions**.

Consider this example given by Wang et al.:

Code Agent

This highlights several advantages of using code:

* Code actions are **much more concise** than JSON.  
   * Need to run 4 parallel streams of 5 consecutive actions ? In JSON, you would need to generate 20 JSON blobs, each in their separate step; in Code it’s only 1 step.  
   * On average, the paper shows that Code actions require 30% fewer steps than JSON, which amounts to an equivalent reduction in the tokens generated. Since LLM calls are often the dimensioning cost of agent systems, it means your agent system runs are \~30% cheaper.
* Code enables to re-use tools from common libraries
* Better performance in benchmarks, due to two reasons:  
   * More intuitive way to express actions  
   * Extensive exposure of LLMs to code in training

The advantages above were confirmed by our experiments on the agent\_reasoning\_benchmark.

From building `smolagents` we can also cite a notable additional advantage, which is a better handling of state: this is very useful for multimodal tasks in particular. Need to store this image/audio/other for later use? No problem, just assign it as a variable in your state and you can re-use it 4 steps later if needed. In JSON you would have to let the LLM name it in a dictionary key and trust the LLM will later understand that it can still use it.

###  Making the right tools 🛠️ 

Now we need to provide the agent with the right set of tools. 

**1.** A web browser. While a fully fledged web browser interaction like Operator will be needed to reach full performance, we started with an extremely simple text-based web browser for now for our first proof-of-concept. You can find the code here

**2.** A simple text inspector, to be able to **read a bunch of text file format**, find it here.

These tools were taken from the excellent Magentic-One agent by Microsoft Research, kudos to them! We didn’t change them much, as our goal was to get as high a performance as we can with the lowest complexity possible.

Here is a short roadmap of improvements which we feel would really improve these tools’ performance (feel free to open a PR and contribute!):

* extending the number of file formats which can be read.
* proposing a more fine-grained handling of files.
* replacing the web browser with a vision-based one, which we’ve started doing here.

##  Results 🏅 

In our 24h+ reproduction sprint, we’ve already seen steady improvements in the performance of our agent on GAIA!

We’ve quickly gone up from the previous SoTA with an open framework, around 46% for Magentic-One, to our current performance of 55.15% on the validation set.

This bump in performance is due mostly to letting our agents write their actions in code! Indeed, when switching to a standard agent that writes actions in JSON instead of code, performance of the same setup is instantly degraded to 33% average on the validation set.

Here is the final agentic system.

We’ve set up a live demo here for you to try it out!

However, this is only the beginning, and there are a lot of things to improve! Our open tools can be made better, the smolagents framework can also be tuned, and we’d love to explore the performance of better open models to support the agent.

We welcome the community to come join us in this endeavour, so we can leverage the power of open research together to build a great open-source agentic framework! It would allow anyone to run a DeepResearch-like agent at home, with their favorite models, using a completely local and customized approach!

##  Community Reproductions 

While we were working on this and focusing on GAIA, other great open implementations of Deep Research emerged from the community, specifically from 

* dzhng,
* assafelovic,
* nickscamara,
* jina-ai and
* mshumer.

Each of these implementations use different libraries for indexing data, browsing the web and querying LLMs. In this project, we would like to **reproduce the benchmarks presented by OpenAI (pass@1 average score), benchmark and document our findings with switching to open LLMs (like DeepSeek R1), using vision LMs, benchmark traditional tool calling against code-native agents.**

##  Most important next steps 

OpenAI’s Deep Research is probably boosted by the excellent web browser that they introduced with Operator.

So we’re tackling that next! In a more general problem: we’re going to build GUI agents, i.e. “agents that view your screen and can act directly with mouse & keyboard”. If you’re excited about this project, and want to help everyone get access to such cool capabilities through open source, we’d love to get your contribution!

We’re also hiring a full time engineer to help us work on this and more, apply if you’re interested 🙂

* To get started with Open Deep Research, try the examples here.
* Check the smolagents repo.
* Read more about smolagents docs, introduction blog post.

##  Models mentioned in this article 1

deepseek-ai/DeepSeek-R1  Text Generation •  685B • Updated Mar 27, 2025 •  9.08M •  13.5k 

##  Datasets mentioned in this article 2

cais/hle  Benchmark • Updated Jan 20 • 2.5k •  31.2k •  859 

gaia-benchmark/GAIA  Viewer • Updated Oct 28, 2025 • 932 •  14.5k •  719 

##  Spaces mentioned in this article 1

 Running on CPU Upgrade Agents 613 GAIA Leaderboard 🦾 613 Submit and view GAIA model evaluation leaderboard 

##  Papers mentioned in this article 1

Executable Code Actions Elicit Better LLM Agents  Paper • 2402.01030 • Published Feb 1, 2024 •  195 

More Articles from our Blog

agentssmolagentsnlp Our Transformers Code Agent beats the GAIA benchmark 🏅  100 July 1, 2024 

agentsllmsguide Harness, Scaffold, and the AI Agent Terms Worth Getting Right  132 May 25, 2026 

### Community

sfield

Feb 4, 2025 

DeepSeek's reasoning skills are probably particularly useful for something like this. But in my mind, particularly for academic research type tasks, the propaganda baked into the model is a non-starter. I tested out the new  
DeepSeek-R1-Distill-Llama-70B-Uncensored-v2-Unbiased model yesterday. It was a very crude test, but I was quite impressed. I'm a newb over here, so take this as a light suggestion, just in case its helpful, nothing more.

See translation 

* 3 replies
· 

👍

4

4

+

TGAI87

Feb 5, 2025 

Yep I'm very impressed with it too. Follows direction exceptionally well, and corrects (intentional) mistakes. Going to try to get it working nicely on my RTX 4090 with offloading. 

See translation 

 Expand 2 replies 

ElanInPhilly

Feb 5, 2025 

This sounds pretty interesting, so I up voted based on description. However, the demo implementation definitely needs attention and work. Now, on several occasions, after long waits in 100+ user queues, I repeatedly get "Error in generating model output:  
litellm.ContextWindowExceededError: litellm.BadRequestError: ContextWindowExceededError: OpenAIException - Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 419624 tokens. Please reduce the length of the messages.", 'type': 'invalid\_request\_error', 'param': 'messages', 'code': 'context\_length\_exceeded'}}". So this seems pretty basic, \*. \* the demo definitely to be crafted so the model can handle the correct token limits at the right time and place. Absent that ....

See translation 

👍

7

7

+

Reply

jonwondo

Feb 5, 2025 

I'm getting the same errors as the person above on the demo site. Must be a bug as I tried different prompts and had to wait \~1hr for each one due to the queue:  
Error in generating model output:  
litellm.ContextWindowExceededError: litellm.BadRequestError: ContextWindowExceededError: OpenAIException - Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 709582 tokens. Please reduce the length of the messages.", 'type': 'invalid\_request\_error', 'param': 'messages', 'code': 'context\_length\_exceeded'}}

See translation 

👍

6

6

+

Reply

raidhon

Feb 5, 2025 

Very cool thanks! I think OpenAI already hate Open Source :)))))  
Products that are trying so hard to monetize are created in one day.

See translation 

👍

4

4

+

Reply

shtefcs

Feb 5, 2025 

•

edited Feb 5, 2025 

This is a big step toward more capable AI agents. At Automatio.ai, we're working on integrating similar autonomous web agents to streamline data extraction and web automation, letting users build powerful scrapers without coding. The challenge is making sure these agents can navigate complex websites reliably. How do you see open-source AI helping bridge the gap between research prototypes and real-world automation?

See translation 

👍

1

1

+

Reply

MS100

Feb 5, 2025 

Amazing. I am so interested in participating.

See translation 

Reply

Kumala3

Feb 5, 2025 

I am currently exploring Open-Source alternatives to OpenAI DeepResearch as it's a really great product, one of the most useful since ChatGPT was launched in 2022 for me, as the results of research are incredible high-quality not just simple research with "search" function.  
I've decided to try out this Open Deep Research via Hugging face space and ran into issue with the returned output exceeded 128K token limit:  
image.png

See translation 

👍

1

1

+

Reply

Kumala3

Feb 5, 2025 

@albertvillanova @clefourrier  Is there any way to resolve this issue or maybe set the instruction to set the output token limit to ensure it doesn't throw errors and works appropriately even with certain limitations?  
PS. Working with limits is MUCH better than not working at all.

See translation 

👍

1

1

+

Reply

mrsmirf

Feb 5, 2025 

Can we get a readme with instructions

See translation 

👍

3

3

+

Reply

derekalia

Feb 6, 2025 

I tried running this locally but got a couple of errors with the run.py command after installing the requirements. Maybe you guys should add a readme to get this setup. <https://github.com/huggingface/smolagents/blob/gaia-submission-r1/examples/open%5Fdeep%5Fresearch/run.py>

See translation 

* 3 replies
· 

mrsmirf

Feb 6, 2025 

Yeah I got errors too. Not sure if I need to install the entire repo, what to install, etc. But, I tried and have not gotten it to run.

See translation 

👀

3

3

+

 Expand 2 replies 

Dikeshwar

Feb 6, 2025 

how to see future

Reply

TGAI87

Feb 6, 2025 

Cursor is able to set this up nicely (and expand on it); just ensure you add the smolagents docs and direct it to the specific open deep research docs within the git repo under src. 

See translation 

* 1 reply
· 

👍

2

2

+

Agenciarc360

Feb 7, 2025 

fale mais meu amigo.... 

See translation 

RocketNinja

Feb 6, 2025 

Hey guys! The demo is down :/

See translation 

👍

9

9

👀

1

1

🧠

1

1

+

Reply

Scrign29

Feb 7, 2025 

impossible d’accéder à la démo.

See translation 

Reply

griged

Feb 7, 2025 

•

edited Feb 7, 2025 

I attempted a side by side comparison between your tool and the for pay Gemini Advanced 1.5 Pro with Deep Research for a particularly interesting and challenging task, but it is difficult to benchmark the results. Gemini did an overall poor - average job, but only after many manual additional prompts.

Initial prompt:  
"what are the highest judgements received by tenants for claims relating to either negligent or intentional infliction of emotional distress in the last 10 years, against landlords in Massachusetts?"  
result - it couldn't find anything  
 I further revised the workflow with prompts such as  
"Please note it may also be in landlord lawsuits against tenants, where tenants win in counter claim"

"There may be some useful results there, but . regenerate following my two stated criteria of "in the last 10 years" and "In Massachusetts" and afterwards try to assess why your process missed this obvious mistake in its final output, and share with me your self analysis"

"please consider a few ways that your filtering can be expanded while still satisfying my criteria. 1\. There are various statutory frameworks within which "negligent infliction of emotional distress" or "intentional infliction of emotional distress" can be brought. It could be in the context of Chapter 93A consumer protection, it could be in the context of M.G.L. c. 186, §14 , in particular when in counter claim in an eviction matter. 2\. Those landmark older cases can be very helpful if you search cases that cite them, in particular simon vs. solomon and Haddad v. Gonzalez. 3\. It is more diffiult to find regular cases than binding case law, a few suggestions, certain trial courts like the Western Division of the Massachusetts Housing court publishes it's 'court reporter' which is basically a data dump of almost all of their case rulings. 3\. You were wise to scrape masscases.com as it has unpublished as well as published decisions which are of interest to me, and they use a scrape friendly URL scheme. judyrecords.com, trellis.law, docketalarm all chose to allow being crawled by google for purposes of appearing in google search results. The information I seek can almost always be inferred purely from the information made available to google, for example {massachusetts emotional distress tenant site:trellis.law} without the {} braces returns many cases. Please try again"

"Rader v Odermatt is an excellent example of a case matching my criteria. The tenant prevailed in counter claim, and was even awarded duplicative damages, normally discouraged and rare. Try to assess how you missed this case, output a revised list but also output your self analysis in your work flow"

I have omitted the self-analysis provided by Google, it was generally correct but as it recognized on its own, it failed to apply weights properly to my revisions. The other major hurdle of course is that for quazi-legal, sometimes technical, and due to outright politcal bias, most lower court, which in a way means "real cases", are very hard to find and even harder to scrape. I tried prompting with scraping strategies but in the end hardly any meaningful results were found. I had a certain results ready to assess its effectiveness. Unfortunetly your tool gave me the same error as stated by others upon just the first prompt

See translation 

Reply

m-ric

Article author Feb 7, 2025 

The demo's up again!

* 1 reply
· 

❤️

4

4

+

karelwar

Feb 7, 2025 

Not for a long time :(

Screenshot_20250207_213738_Brave.jpg

See translation 

pulkitmehtawork

Feb 9, 2025 

I was able to run run.py locally .. please check solution at <https://github.com/huggingface/smolagents/issues/501>.. i have mentioned steps there . 

See translation 

Reply

onedayatime

Feb 9, 2025 

I read everything from A-Z. Thanks for this

See translation 

Reply

serkan90

Feb 11, 2025 

buffer 

Reply

inbuss

Feb 13, 2025 

I'd love to read a good README.md of this open\_deep\_research folder, how to use and tweak that example :)

See translation 

👀

1

1

+

Reply

CodePhyt

Feb 16, 2025 

amazing

Reply

ngxson

Feb 17, 2025 

📻 🎙️ Hey, I made a podcast about this blog post, check it out!

_This podcast is generated via ngxson/kokoro-podcast-generator, using DeepSeek-R1 and Kokoro-TTS_

See translation 

* 1 reply
· 

👍

1

1

+

shtefcs

Feb 17, 2025 

This is cool. 

Tamar

Feb 20, 2025 

Hey Great blog post! I noticed you published the models tested for the Gaia/Math benchmarking—thanks for sharing that.

I was wondering if you could let me know which server you used to run the models? I’m currently using vLLM, but it seems like it doesn’t yet support tool\_choice="required". To make it work, I had to tweak the model code to force it to return a tool for execution.

Thanks in advance for any insights!

See translation 

Reply

prabhu130986

Feb 23, 2025 

i've tried to run the agent in my local setup and i would say, its pretty impressive. i tried the same questions from Openai's deep research page (<https://openai.com/index/introducing-deep-research/>), just to compare the workflow and output. 

The plan of action it created was neat and executed all the workflow steps one by one, though there were some errors in between, but that didnt break the progress. Finally it gave the final recommendation based on all the gathered data. 

Attached is the result of using gpt-4o model. using o1 model will definitely give a better inference.  
plan.jpg  
final-answer.jpg

See translation 

🔥

1

1

+

Reply

vinayp27

Feb 27, 2025 

Can we add something that searches arxiv and pubmed articles and then presents the research. I think it would be a great start

See translation 

* 3 replies
· 

👍

2

2

+

shtefcs

Mar 5, 2025 

Like a scraper that will gather data from resesrch articles and feed into DeepSeek? 

See translation 

 Expand 2 replies 

huytofu92

Mar 5, 2025 

Another bullet fired at closedAI it seems :))

See translation 

👍

1

1

+

Reply

deleted

Mar 6, 2025 

yes

Reply

Moza05

Mar 7, 2025 

This comment has been hidden 

milyiyo

Mar 10, 2025 

The demo is not working :(

<https://m-ric-open-deep-research.hf.space/>

See translation 

Reply

CodePhyt

Mar 20, 2025 

•

edited Mar 20, 2025 

i will find a way to make every tech out there opensource and bring opensource humaniy into this world 

See translation 

🤗

1

1

+

Reply

OMAP3530

Mar 26, 2025 

@m-ric  Hi, I am trying to leverage the `VisitTool` that is based on `SimpleTextBrowser` to fetch page content from URL. But I find it may returns `error 403 Enable JavaScript and cookies to continue` for some URLs like <https://www.businessresearchinsights.com/market-reports/software-resellers-market-117159>. So I am wondering how does Open DR handle such issues when generating final report or doing the analysis. just skip it or any other to fetch content snippet from the page via `GoogleSearchTool`?

See translation 

Reply

elly99

Oct 21, 2025 

Can autonomous agents learn to reflect on their own epistemic trajectory?  
Inspired by the need for cognitive scaffolding, I’ve built MarCognity-AI  
<https://huggingface.co/elly99/MarCognity-AI>  
— a metacognitive framework that encodes reasoning before response.  
It doesn’t just optimize for retrieval. It encodes conceptual regret, ethical thresholds, and the discomfort of premature synthesis.  
Could we imagine agents that track the cognitive cost of each query?  
That learn not just from relevance — but from reflection? I’d love to explore how this scaffolding could reshape autonomous research — not with answers, but with architecture.

See translation 

Reply

Roman1902

Dec 8, 2025 

"What a fascinating read! It’s impressive how Hugging Face’s “Open Deep Research” project brings open-source spirit to cutting-edge research agents — by combining large language models with an “agentic framework” that can autonomously browse the web, gather info, and synthesize structured answers. I appreciate how you walk through the rationale behind agent frameworks, discuss the performance metrics (like the jump in the GAIA benchmark), and outline both the current results and the path forward for community contribution. 

I also recently read a related article: <https://mobisoftinfotech.com/resources/blog/ai-development/llm-api-pricing-guide>  
 — that post gives a clear breakdown of how usage patterns, token counts, and model choices affect LLM API costs in practical deployments.

Seeing Open Deep Research as an open-source, transparent alternative alongside a guide that helps with realistic cost estimation gives a really balanced view: you show how to build powerful AI tools and how to plan for their usage sustainably."

See translation 

Reply

EditPreview

Upload images, audio, and videos by dragging in the text input, pasting, or clicking here.

Tap or paste here to upload images

 Comment 

· Sign up or log in to comment

 Upvote 1320 
* +1308

##  Models mentioned in this article 1

deepseek-ai/DeepSeek-R1  Text Generation •  685B • Updated Mar 27, 2025 •  9.08M •  13.5k 

##  Datasets mentioned in this article 2

cais/hle  Benchmark • Updated Jan 20 • 2.5k •  31.2k •  859 

gaia-benchmark/GAIA  Viewer • Updated Oct 28, 2025 • 932 •  14.5k •  719 

##  Spaces mentioned in this article 1

 Running on CPU Upgrade Agents 613 GAIA Leaderboard 🦾 613 Submit and view GAIA model evaluation leaderboard 

##  Papers mentioned in this article 1

Executable Code Actions Elicit Better LLM Agents  Paper • 2402.01030 • Published Feb 1, 2024 •  195 

 System theme 

Company

TOS Privacy About Careers 

Website

Models Datasets Spaces Pricing Docs