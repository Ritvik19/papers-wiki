# Papers Explained: TinyGSM

Papers Explained: TinyGSM

Papers Explained: TinyGSM

TinyGSM is a synthetic dataset of 12.3M grade school math problems paired with Python solutions, generated fully by GPT-3.5. After…

Papers Explained: TinyGSM

TinyGSM is a synthetic dataset of 12.3M grade school math problems paired with Python solutions, generated fully by GPT-3.5. After finetuning on TinyGSM, a duo of a 1.3B generation model and a 1.3B verifier model can achieve 81.5% accuracy, outperforming existing models that are orders of magnitude larger and rivaling the performance of the GPT-3.5 “teacher” model (77.4%).

Methodology

The math concepts in the GSM8K dataset are elementary and within standard grade-school curricula, but the challenges posed by the natural language problem statement introduce an additional layer of complexity to the task. Sampled from the GSM8K training set, each problem variant contains both a question and the corresponding solution written in Python. Using code allows leverage of a Python interpreter, circumventing language models’ known limitation regarding numerical calculations and code execution. To enhance robustness, synthetic problems were generated whose questions contain irrelevant information. This is achieved by augmenting the GSM-IC dataset, which is an augmentation of GSM8K specifically designed to introduce irrelevant context (IC) to the question statement. These GSM-IC variants constitute approximately one third of TinyGSM. The resulting synthetic dataset contains 12.3M problems. To encourage diversity, temperature sampling is used and the prompt is specified to encourage the problem variants to be grammatically diverse and contain multiple steps.
The prompt template for generating TinyGSM.The prompt template for generating question variants based on GSM8K.The prompt template for generating question variants based on GSM8K-IC.
The synthetic data in TinyGSM is filtered by removing problems that are too short, lack numbers, or have code solutions that are not executable. The dataset does not check for the correctness of questions or solutions since there is no ground truth available. Although filtering by majority vote (self-consistency) can be effective, the authors did not use this because GPT-3.5-turbo’s generations are only consistent on easy problems; applying this filter would exclude challenging problems and make the dataset too easy and less useful.
Results on GSM8K.Results on GSM8K.
The Phi-1.5 125M, 350M and 1.3B models are finetuned on TinyGSM. The 1.3B model reaches 68.2% accuracy.

Increasing the amount of synthetic data can significantly improve model performance, but after a certain point, adding more data yields diminishing returns, with only marginal gains in performance.

Even if a small language model matches the quality of the synthetic data creator, the ceiling for test accuracy remains set by that creator.

To further improve performance, the authors suggest using a verifier, i.e. leveraging multiple generations and selecting the best possible one.

The main challenge: without labels, it’s hard to define “best.” Self-selection approaches do not always work well because confident or consistent answers may still be wrong. Inspired by previous research, the authors propose training a separate verifier model to predict the correctness of each candidate answer.

The training data consists of the SLM’s generations on the labeled GSM8K training set questions, paired with the binary labels indicating whether a generation leads to the correct numerical answer. Forty-eight generations are sampled for each training set question. Note that this is the only time where the GSM8K training set is directly utilized in training.

The verifier is trained with a sequence-to-sequence task, where the binary label on the entire sequence is used to supervise each token. This approach improves consistently over training with a sequence classification task. The verifier model is initialized to be the same as the SLM, with an additional prediction head shared across all positions.

Including data generated using various temperatures and different checkpoints improves the performance of the verifier. The training data for the verifier is generated from checkpoints at 1k, 6k, and 12k steps, and both training and testing data use a mixture of data generated with temperature 0.5 and 0.7.

Evaluation
Pass@1 results on GSM8K test set with verifiers.
While the best accuracy is achieved with configuration with largest sizes, the verifier size seems to play a bigger role than the generation model size.
The effect of model size scaling is surprisingly mild. Increasing the base generation model from 125M (Phi-1.5-tiny) to 1.3B (Phi-1.5) only gives a 6% boost.
On the other hand, the verifier seems to be much more parameter efficient. For example, 125M generation model + 1.3B verifier can achieve 76.1%, while 1.3B generation model + 125M verifier gets only 71.7%.
While one verifier is trained for each generative model, verifiers transfer reasonably well across models. For example, a 1.3B model was able to reach 78.1% with a 350M verifier trained on generations from a 350M model.

Paper

TinyGSM: achieving >80% on GSM8k with small language models 2312.09241

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

View original.

Exported from Medium on August 22, 2026.
