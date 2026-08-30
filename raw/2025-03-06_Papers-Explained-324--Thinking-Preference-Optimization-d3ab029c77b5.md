# Papers Explained 324: Thinking Preference Optimization

Papers Explained 324: Thinking Preference Optimization

Papers Explained 324: Thinking Preference Optimization

Thinking Preference Optimization (ThinkPO) utilizes readily available or easily obtainable short CoT reasoning responses as rejected…

Papers Explained 324: Thinking Preference Optimization

Thinking Preference Optimization (ThinkPO) utilizes readily available or easily obtainable short CoT reasoning responses as rejected answers and long CoT responses as chosen answers for the same question. It then applies direct preference optimization to encourage the model to favor longer reasoning outputs.

Training Pipeline

The training process in Thinking Preference Optimization consists of two stages: Reasoning SFT (Supervised Fine-Tuning) stage and Reasoning DPO (Direct Preference Optimization) stage.

In the Reasoning SFT stage, long-reasoning responses are collected for each question to construct the dataset Dsft. The base model is then fine-tuned on Dsft to acquire advanced reasoning capabilities, which helps to prepare the model for the next stage.

In the second stage, the model is further encouraged to generate extended reasoning using the Direct Preference Optimization (DPO) approach. First, the long-reasoning data from the initial stage is used as the chosen responses. Then, a smaller model with normal Reasoning ability is utilized to generate shorter reasoning responses as rejected samples. To ensure data quality, both long and short reasoning responses undergo filtering, including correctness validation. This process results in the dataset Ddpo. Finally, the model trained in the first stage is fine-tuned on Ddpo using DPO, encouraging the model to generate longer outputs while enhancing its reasoning ability.

Data Curation

The dataset Dsft = {(q,olong)}N is based on a bespoke stratos dataset. DeepSeek-R1 was used as the teacher reasoning model instead of QwQ-32B-Preview to generate long reasoning response olong and GPT-4o-mini is employed in place of Sky-thought T1’s parsing logic to filter out incorrect mathematical solutions.

For the dataset Ddpo = {(q, olong, oshort)}N, it was collected in the following manner: For each question q in Dsft, Qwen2.5-Math-7B-Instruct ias used to generate a short reasoning response oshort, pairing it with the long reasoning response olong in Dsft. The samples where Qwen2.5-Math-7B-Instruct’s answer matched DeepSeek R1’s answer are retained, resulting in 8,080 samples. Additionally, 2,000 samples where Qwen2.5-Math-7B-Instruct’s answer differed from DeepSeek R1’s but adhered to the correct response format, including more output distribution, are included in Ddpo. All of these combined samples consequently form the final dataset Ddpo.

Evaluation

Effectiveness of ThinkPO

The fine-tuned model achieves scores comparable to Bespoke-Stratos-7B, it shows improvements on almost all datasets, validating the effectiveness of ThinkPO in enhancing LLM reasoning ability.

ThinkPO can Continually Improve Reasoning Ability of Public Distilled Models

ThinkPO training improved the accuracy of both models across most of the five datasets tested.
Bespoke-Stratos-7B showed accuracy improvements on all datasets except MATH500, with notable improvements of around 5% on Olympiad Bench Math and GPQA-Diamond.
DeepSeek-R1-Distill-Qwen-7B showed consistent or slightly improved accuracy, except for a decline on AIME2024. Its accuracy on MATH500 improved from 87.4% to 91.2%.
The average response length increased for both models, suggesting enhanced reasoning capacities, aligning with the test-time scaling principle. DeepSeek-R1-Distill-Qwen-7B’s response length increased by ~500 tokens on MATH500, while Bespoke-Stratos-7B’s increased by ~1000 tokens.

ThinkPO Works for Different-Size Models

Increasing model size generally leads to improved accuracy across datasets after SFT.
ThinkPO consistently improves performance across all model sizes (3B, 7B, 14B).
ThinkPO leads to a 1–2% accuracy improvement on Math500 for all models.
The 3B model shows improvement on all five datasets after ThinkPO, while the 7B and 14B models improve on four datasets.
ThinkPO demonstrates generalizability and robustness by being effective across different model scales.

Paper

Thinking Preference Optimization 2502.13173

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on March 6, 2025.

Canonical link

Exported from Medium on May 4, 2026.
