# Introducing Command A: Max performance, minimal compute

**Source URL**: https://cohere.com/blog/command-a  
**Published**: 2025-03-13  
**Author**: Cohere

Today, we’re introducing Command A, a new state-of-the-art generative model optimized for demanding enterprises that require fast, secure, and high-quality AI. Command A delivers maximum performance with minimal hardware costs when compared to leading proprietary and open-weights models, such as GPT-4o and DeepSeek-V3. For private deployments, Command A excels on business-critical agentic and multilingual tasks, while‬ being deployable on just two GPUs, compared to other models that typically require as many as 32.

In head-to-head human evaluation across business, STEM, and coding tasks, Command A matches or outperforms its larger and slower competitors – while offering superior throughput and increased efficiency. Human evaluations matter because they test on real-world enterprise data and situations.  *Head-to-head human evaluation win rates on enterprise tasks. All examples are blind-annotated by specially trained human annotators, assessing enterprise-focused accuracy, instruction following, and style. Throughput comparisons are between Command A on the Cohere platform, GPT-4o and Deepseek-V3 (TogetherAI) as reported by Artificial Analysis.*

Across a range of standard benchmarks Command A provides strong performance on instruction following, SQL, agentic, and tool tasks.*Performance evaluated across academic benchmarks (MMLU, MATH, IFEval), agents benchmarks (BFCL, and Taubench), and coding benchmarks (MBPPPlus, SQL, and RepoQA). Methodology and further details are provided at the bottom in a footnote [1].*

## **Scalable efficiency **

We focused on building Command A as efficiently as possible, while also making it as efficient to serve in production as possible. With a serving footprint of just two A100s or H100s, it requires far less compute than other comparable models on the market. This is especially important for private deployments. 

Impractically large models lead to poor latency. When you just want correct answers quickly, Command A is the best choice. In fact, Command A can deliver tokens at a rate of up to 156 tokens/sec which is 1.75x higher than GPT-4o and 2.4x higher than DeepSeek-V3. Private deployments of Command A can be up to 50% cheaper than API-based access.*Command A tokens per second and time to first token is superior to GPT-4o and DeepSeek-V3 for both long and short context requests. *

## **Enterprise-ready capabilities **

We designed Command A with business needs in mind. Its 256k context length (2x most leading models) can handle much longer enterprise documents. Other key features include Cohere’s advanced retrieval-augmented generation (RAG) with verifiable citations, agentic tool use, enterprise-grade security, and strong multilingual performance.*Head-to-head human evaluation win rates comparing Command A and GPT-4o on enterprise RAG use-cases. All examples are at least 3-way blind-annotated by specially trained human annotators, assessing fluency, faithfulness, and response utility.*

We understand that global companies need capabilities across regions. Command A offers expanded enterprise-level support for the 23 languages spoken by the majority of the world's population. We performed an extensive human evaluation and found users strongly preferred Command A over DeepSeek-V3 across most languages on a range of business use cases.*Head-to-head human evaluation win rates on enterprise tasks across 8 languages. All examples are blind-annotated by specially trained human annotators, assessing enterprise-focused accuracy, instruction following, and style.*

In particular, Command A is much better than GPT-4o or DeepSeek-V3 at consistently answering with content in the requested language, for example answering in the relevant Arabic dialect of the user.  *Arabic cross-lingual line-level pass-rate (LPR) on the prompts from Marchisio et al., 2024 and average ADI2 score over monolingual prompts in 4 Arabic dialects (Egyptian, Saudi, Syrian, Moroccan) from Robinson et al., 2024.*

## **Powering AI agents at scale‬**

AI is only as good as the data you give it. With that in mind, Command A securely delivers accurate‬ responses to questions based on your internal company information. In practice, customers use this‬ for tasks such as sourcing relevant HR policies by office location, reviewing legal regulations, and‬ ‭analyzing long financial reports.

The next generation of Cohere models will help power a range of AI applications for customers‬ ‭across industries like finance, healthcare, manufacturing, energy, and the public sector. In particular, they will seamlessly integrate with‬‭ [North‬‭](https://cohere.com/blog/north-eap), our secure AI agents platform to unlock the full potential of‬ your company data and people with AI agents. Our fully integrated technology stack enables full‬ ‭customization of the product for customers to suit their unique business needs.‬

North securely leverages enterprise tools like CRM and ERP software, as well as connects to internal company databases and external web search services. This enables you to build agents that take‬ ‭action for you behind the secured firewalls of your enterprise systems.‬
            
                
                
                    
                        
                            
                        
                    
                
                
                    
                        
                            
                                
                            
                        
                        
                            
                                
                                
                            
                        
                        0:00
                        
                            /1:46
                        
                        
                        1×
                        
                            
                                
                            
                        
                        
                            
                                
                            
                        
                        
                    
                
            
            
        

## **Availability **

Command A is available today on the [Cohere platform](https://dashboard.cohere.com/welcome/login?redirect_uri=%2Fplayground%2Fchat%3Fmodel%3Dcommand-a-03-2025), for research use on [Hugging Face](https://huggingface.co/CohereForAI/c4ai-command-a-03-2025), and coming soon to major cloud providers. If you are interested in private or on-prem deployments please contact our [sales team](https://cohere.com/contact-sales). 

Cohere API Pricing
Input Tokens
Output Tokens

Command A
$2.50 / 1M
$10.00 / 1M

[1]BFCL: Performance on the BFCL-v3 benchmark on March 12, 2025. Where available, scores are taken from the public leaderboard, and otherwise using a best-effort internal evaluation using the official codebase. For competitors, we report the higher of their BFCL ‘prompted’ or ‘function-calling’ score. We report the Overall score which tests tool-use in diverse, real-world environments.

Taubench: Performance on the Taubench benchmark. Where available, scores are taken from the public repository leaderboard, and otherwise use a best-effort internal evaluation using the official codebase. We report the pass@1 scores on the Retail and Airline tasks which evaluate tool-use agents in multi-turn customer support use cases.

Academic: Performance across academic benchmarks that span general knowledge (MMLU), math performance (MATH), and instruction following (IFEval). We find that Command-A performs approximately at the level of, or exceeds the performance of, GPT-4o and DeepSeek-V3.

Coding: We note that Command-A demonstrates particularly strong performance on SQL benchmarks (average of BirdBench, Spider Dev, and Spider Test), and at the level of GPT-4o across use cases for MBPPlus (Python programing). Finally, we note its superior performance on repository-level question-answering in longer contexts (RepoQA).