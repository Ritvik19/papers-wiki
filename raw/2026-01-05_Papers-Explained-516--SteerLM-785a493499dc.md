# Papers Explained 516: SteerLM

Papers Explained 516: SteerLM

Papers Explained 516: SteerLM

SteerLM is a supervised fine-tuning method that empowers end-users to control responses during inference. It conditions responses to…

Papers Explained 516: SteerLM

SteerLM is a supervised fine-tuning method that empowers end-users to control responses during inference. It conditions responses to conform to an explicitly defined multi-dimensional set of attributes, thereby empowering a steerable AI capable of generating helpful and high-quality responses while maintaining customizability.

Methodology
SteerLM Overview.
Step 1. Attribute Prediction Model

Similar to the reward model in RLHF, the Attribute Prediction Model in SteerLM is designed to predict human preference of model responses to improve model alignment. Compared to a monolithic reward signal in RLHF, the attribute prediction model can be used to predict various attributes that are considered to be important in generating good Responses. The Open Assistant (OASST) dataset D is used, where each sample contains a prompt x, a response y as well as a set of attributes v. To model these attributes, each attribute (originally a float between 0 and 1) is first scaled into an integer between 0 and 9.

The attributes selected look like quality:6,toxicity:0,humor:9,creativity:0,violence:0,helpfulness:5,not_appropriate:0.

Conditioning on x and y, v is the target output for the language model.

Step 2. Annotating Datasets using Attribute Prediction Model

Samples are annotated by greedily decoding the value attributes for pairs of prompts and responses using the Attribute Prediction Model, in order to construct the attribute annotated dataset D′.

Step 3. Attribute Conditioned SFT

Attribute-conditioned SFT is an extension of regular SFT that enables incorporating reward signal information through attribute labels. This allows learning from both high and low quality responses. It only requires an offline annotated dataset, rather than online sampling and evaluation of responses like in RLHF. Using the attribute-annotated train datasets D′, a model is trained to generate a response y, conditioning on the value attributes v and the prompt x. The loss function is:

Step 4. Bootstrapping with High Quality Samples

Step 4a: Generating Diverse High-Quality Responses

Identify High-Quality Attribute Combinations: The method starts by identifying attribute value combinations from the training data that correspond to the highest quality (value 9). This creates a subset of attribute strings representing high-quality responses.
Sample Attribute Strings: A high-quality attribute string (v′) is uniformly sampled from this subset.
Generate Responses: Prompts from the training data are combined with the sampled attribute string (v′) and used to generate multiple responses using Attribute Conditioned Supervised Fine-Tuning (AC-SFT). Top-k sampling (k=50) is employed to ensure diversity in the generated responses. This results in a dataset D′′ containing prompts and their corresponding generated responses.

Step 4b: Attribute Prediction and Second Round of AC-SFT

Attribute Prediction: The Attribute Prediction Model is used to predict attribute values (v′′) for the generated responses (y′) using greedy sampling. This creates a dataset D′′′ containing prompts, generated responses, and their predicted attribute values.
Bootstrap Training: The generated responses (y′) and their predicted attributes (v′′) from D′′′ are used to perform a second round of Attribute-conditioned SFT. This effectively allows the model to learn from its own generated responses, further refining its ability to produce high-quality outputs.

Experiments

Training Datasets

OASST: The Open Assistant dataset was used to train the Attribute Prediction Model, as well as to perform Attribute Condition SFT. This dataset contains 13 human-labeled attributes for each response with a score ranging from 0 to 1. Seven of these attributes were chosen that are most relevant for guiding the language model to align with human preferences: quality, toxicity, violence, helpfulness, creativity, humor, and inappropriateness. Other attributes such as hate_speech, lang_mismatch, and pii (personal identifiable information) are not useful to steer at inference time since these are attributes that always want to keep as False.

HH-RLHF: The Helpful and Harmless — Reinforcement Learning from Human Feedback dataset does not provide human labeled attribute values. In order to improve the diversity of prompts and responses, the trained Attribute Prediction model is utilized to annotate the responses.

M-SID: The Model Self-Identification Dataset is a small set of 910 prompt-response pairs used to answer questions relating to identity such as “Who are you?” and “Who created you?”. This dataset is also included as part of Attribute Conditioned SFT training.

Base Model

SteerLM 43B: The 43B base language model was trained on a diverse corpus encompassing various multilingual data sources, including web crawl, news articles, books, scientific publications from arXiv, and code repositories. Having been trained with 1.1 trillion tokens, it is comparable to LLaMA’s 30B and 65B models, which were trained on 1.4 trillion tokens. This base model is designed for general-purpose language understanding tasks and does not have any domain-specific fine-tuning. This base model is utilized as the backbone for both Attribute Prediction and Attribute Conditioned SFT.

SteerLM 13B: The SteerLM methodology is applied to a popular, widely-available model: Llama 2 13B base model.

Training details

The training of both the Attribute Prediction Model and Attribute Conditioned Supervised Fine-Tuning Model involved 5 epochs, with a maximum sequence length of 4096 tokens. The selection of the optimal Attribute Prediction model checkpoint was determined based on the lowest loss observed on the validation set, while the optimal checkpoint for the Attribute Conditioned SFT model was selected based on the highest validation quality observed on holdout validation sets.

Evaluation
Automatic evaluation.
SteerLM 43B and 13B outperform all baselines in GPT-4 automatic scoring, with 43B being the top model.
Elo Ratings for Models based on Automatic and Human Evaluation.
SteerLM 43B is clearly strongest under automatic evaluation, with a 74 Elo point advantage over the next-best baseline (Guanaco 65B).
Human raters also prefer SteerLM 43B overall; its advantage over baselines is smaller than in automatic evaluation but still substantial (≈59 Elo points over ChatGPT 3.5).
Automatic evaluation with GPT-4 tends to favor longer, more token-diverse responses, which likely contributes to SteerLM 43B’s larger Elo advantage in automatic vs. human evaluation.

Paper

SteerLM: Attribute Conditioned SFT as an (User-Steerable) Alternative to RLHF 2310.05344

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on January 5, 2026.

Canonical link

Exported from Medium on May 4, 2026.
