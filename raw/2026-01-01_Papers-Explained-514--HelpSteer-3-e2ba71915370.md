# Papers Explained 514: HelpSteer 3

Papers Explained 514: HelpSteer 3

Papers Explained 514: HelpSteer 3

The techniques used to train models for inference-time scaling require tasks to have answers that can be verified, limiting their…

Papers Explained 514: HelpSteer 3

The techniques used to train models for inference-time scaling require tasks to have answers that can be verified, limiting their application to domains such as math, coding and logical reasoning. Inspired from from how humans make first attempts, ask for detailed feedback from others and make improvements based on such feedback across a wide spectrum of open-ended endeavors, HelpSteer3 data is collected to train dedicated Feedback and Edit Models that are capable of performing inference-time scaling for open-ended general-domain tasks. In this setup, one model generates an initial response, which are given feedback by a second model, that are then used by a third model to edit the response.

Dataset

Prompts are drawn from ShareGPT for Coding and Multilingual prompts (as in HelpSteer2) and WildChat for General and STEM prompts (approx. 1M prompts), chosen to reduce overlap with HelpSteer2.

Safety and privacy filtering:

Prompts/responses with harmful content, illegal activities, profanity, bias/stereotyping are filtered out.
Annotators are instructed to skip tasks that slip through the filter or contain PII (name, address, SSN, email, phone, etc.).

For each prompt, two responses are generated using a diverse set of models: Nemotron 4 340B Instruct, Mistral Large 2, Mistral 7B-Instruct-v0.3, Mixtral 8x22B Instruct, Mixtral 8x7B Instruct, Mistral NeMo 12B, Codestral 22B, Gemma 2 (2B, 9B, 27B), Gemma 2B, Phi 3 (Mini, Small, Medium), IBM Granite (8B, 34B), Snowflake Arctic

Generation settings:

Temperature: 0
Top p: 0.9
Max tokens: 3072

Larger models are prioritized for generating more responses, but a range of sizes/capabilities is included to improve compatibility of Feedback and Edit models.

Multi-turn prompts are included to support Feedback–Edit loops for follow-up prompts. Instead of using ChatGPT assistant turns from ShareGPT/WildChat, intermediate assistant turns are generated using the same set of models.

Annotators provide free-text feedback on the overall helpfulness of the last assistant response in a conversation, usually 2–10 sentences (50–250 words) startling with “The response is {not / slightly / partially / mostly / perfectly} helpful”. Feedback is consolidated per task and sent to separate pools of annotators who edit responses based on the feedback.

Three datasets are constructed from the collected data.

Feedback Demonstration

This dataset trains models to imitate human feedback given a user prompt and a model response.

Retain only the three feedback entries per response that agree most (to filter outliers).
Remove prompts where these three still show large disagreement (e.g., one says “perfectly helpful” and another “slightly helpful”), as this suggests misunderstanding or oversight.
Using multiple feedback per response:

Increases diversity of possible model outputs.
Reduces overfitting to a single feedback style.

Edit Demonstration

This dataset trains models to generate edited responses given a user prompt, a model response, and a set of feedback.

Filter out feedback that starts with “The model response is perfectly helpful” because such feedback contains no improvement suggestions.
Exclude feedback that was not actually used in the editing process, Each edit annotator writes a change summary describing their edits. Llama-3.3–70B-Instruct is prompted to check whether the change summary addresses the issues mentioned in each feedback.
To teach order-independence of feedback, All permutations of the linearized feedback set are included.

Edit Preference

This dataset trains a model to distinguish good edits from unsatisfactory edits.

Two types of unsatisfactory edits:

Bad edits not based on feedback:

Edits reflect the annotator’s own opinion rather than the provided feedback (details in Appendix C).
These were common in early annotation.
Tasks with both a bad edit and a later good edit (reworked to follow feedback) are identified.

No-op edits:

Edited response simply copies the original response.
Not seen in human annotations but observed in a model trained only on Edit Demonstration.
Likely due to token-level loss in supervised fine-tuning: copying minimizes loss because most tokens are preserved in human edits.

Edit Preference dataset pairs each Good Edit with an unsatisfactory edit. The two unsatisfactory types are included in a 1:1 ratio.
Descriptive Statistics for Feedback and Edit Demonstration datasets.Descriptive statistics for Edit Preference data.
Experiments

Ten feedback per initial response are generated with a temperature of 0.7 and top p of 0.9. Any feedback which finds the initial response ‘perfectly helpful’ is excluded, since such feedback does not contain information relating to improvement(s) for the Edit model to make. Out of the remaining feedback, up to 3 feedback are randomly chosen for generating an edit of the initial response. The edited response is then greedily generated conditioned on the prompt, initial response, and feedback.

The Llama 3.3 70B Instruct model is used to initialize Feedback and Edit Supervised Fine-Tuning (SFT) model training. The Edit Reward Model (RM) and Reinforcement Learning (RL) model are initialized from the Edit SFT Model. Each dataset is split into 95% train and 5% validation.

Feedback SFT: SFT is performed on the Feedback Demonstration dataset for 1 epoch.
Edit SFT: SFT is performed on the Edit Demonstration dataset for 1 epoch.
Edit RM: Bradley-Terry modeling is performed on the Edit Preference dataset for 1 epoch.
Edit RL: REINFORCE Leave One Out is performed on the Edit SFT model guided by the Edit RM for 1 epoch.

The helpfulness of models to general-domain prompts is measured using three popular metrics: AlpacaEval 2.0 Length Controlled, GPT-4-Turbo MT Bench and Arena Hard.
Applying Feedback and Edit models with various Instruct models.
Using Feedback + Edit to perform inference-time scaling on both Llama-3.1-Nemotron-70B-Instruct and Llama-3.3–70B-Instruct model substantially improves performance across MT Bench, AlpacaEval and Arena Hard.
Llama-3.1-Nemotron-70B-Instruct is the strongest open-source 70B model based on Arena Hard, AlpacaEval 2.0 LC, and MT Bench. Feedback + Edit further enhances this already strong baseline, reinforcing the value of the method for top-tier open-source models.

Paper

HelpSteer3: Human-Annotated Feedback and Edit Data to Empower Inference-Time Scaling in Open-Ended General-Domain Tasks 2505.11475

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on January 1, 2026.

Canonical link

Exported from Medium on May 4, 2026.
