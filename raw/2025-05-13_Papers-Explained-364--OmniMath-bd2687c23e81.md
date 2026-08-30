# Papers Explained 364: OmniMath

Papers Explained 364: OmniMath

Papers Explained 364: OmniMath

OmniMath is a comprehensive and challenging benchmark specifically designed to assess LLMs’ mathematical reasoning at the Olympiad level…

Papers Explained 364: OmniMath

OmniMath is a comprehensive and challenging benchmark specifically designed to assess LLMs’ mathematical reasoning at the Olympiad level. Unlike existing Olympiad-related benchmarks, the dataset focuses exclusively on mathematics and comprises a vast collection of 4428 competition-level problems with rigorous human annotation.
An overall illustration of Omni-MATH.
Data Collection and Annotation
The overall data collection and annotation process of Omni-MATH.
Sources: Problems and solutions were gathered from official competition websites (e.g., IMO, IMC), AoPS Wiki (verified solutions), and AoPS Forum (user-uploaded solutions).

Initial Filtering: Rules were applied to ensure data adhered to input/output formats.

Verification: Professional annotators (graduate and doctoral students) verified solutions:

Simple verification for official solutions from Contest Pages and AoPS Wiki.
Thorough verification for AoPS Forum solutions:
Initial screening narrowed down the dataset to 1100 problems.
Four annotators assessed the most frequent forum responses against expected outputs.
Cross-validation ensured reliability (92.7% accuracy initially, improved to 97.3% after further manual sampling).
The number of data in the construction process.The hierarchical data source of the Omni-MATH.
Difficulty Classification

Source: AoPS: Rating page, providing difficulty scores (0–10) for some problems.

GPT-4o for Missing Ratings: For problems without ratings, GPT-4o was prompted to assign difficulty scores based on in-context learning from existing ratings.
Difficulty distribution across contests.The difficulty distribution of Omni-MATH.
Domain Classification

Mathematical domains were organized into a hierarchical tree structure based on competition guidebooks. GPT-4o was used to classify problems into specific domains based on this hierarchy
The total domain tree of Omni-MATH.
Evaluation On Existing Llms

15 LLMs are selected for their strong mathematical reasoning capabilities. Prompts are formatted according to each model’s guidelines.
GPT-4o is used to evaluate the correctness of the model outputs.
Best-of-N (specifically RM@8 and RM@256) scaling is applied to Qwen2.5 models.
Main Result.
Qwen2.5-MATH-72b-Instruct and OpenAI o1-mini performed best in the vanilla and test-time scaled categories, respectively. OpenAI models significantly outperformed other models in overall accuracy.
Olympiad-level math problem-solving remains a significant challenge for all LLMs. Even the best-performing model (OpenAI o1-mini with test-time enhancement) achieved only 60.54% accuracy.
Open-source models like Qwen2.5-MATH outperformed GPT-4o in this specific task.
Models performed better in domains like algebra, calculus, and number theory, likely due to the greater prevalence of these topics in training datasets. Performance was weaker in discrete mathematics, likely due to the scarcity of related training data.
Best-of-N scaling techniques, while commonly used, did not consistently improve performance, suggesting limitations in the reward model’s ability to supervise complex mathematical tasks and/or the policy model’s ability to find correct solutions. However, OpenAI models with limited inference tokens still outperformed vanilla models, highlighting the need for more efficient test-time enhancement approaches.
The performance of the policy model under Pass@K and the proportion of correct COT.
While increasing the number of samples (K) improves the ability of the policy model to solve problems, a significant portion (33.8%) remains unsolved even with 32 samples.
As the number of samples increases, the proportion of correct COTs within the solved problems decreases, indicating increasing difficulty for the reward model to identify the correct reasoning path amidst the growing number of candidate traces. This suggests interference in RM selection.

Paper

Omni-MATH: A Universal Olympiad Level Mathematic Benchmark For Large Language Models 2410.07985

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on May 13, 2025.

Canonical link

Exported from Medium on May 4, 2026.
