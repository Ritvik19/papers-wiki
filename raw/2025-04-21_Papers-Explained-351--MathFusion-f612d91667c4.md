# Papers Explained 351: MathFusion

Papers Explained 351: MathFusion

Papers Explained 351: MathFusion

MathFusion is a novel framework that enhances mathematical reasoning through cross-problem instruction synthesis. MathFusion implements…

Papers Explained 351: MathFusion

MathFusion is a novel framework that enhances mathematical reasoning through cross-problem instruction synthesis. MathFusion implements this through three fusion strategies:

sequential fusion: chains related problems to model solution dependencies
parallel fusion: combines analogous problems to reinforce conceptual understanding
conditional fusion: creates context-aware selective problems to enhance reasoning flexibility.

By applying these strategies, a new dataset, MathFusionQA, is generated.

The project is available on Github.

MathFusion
The overview of MathFusion.
Given two mathematical problems PA and PB from the original mathematical training set, MathFusion synthesizes a new mathematical problem PF by fusing these two problems.
PA: During one day, there are 4 boat trips through the lake.
The boat can take up to 12 people during one trip. 
How many people can the boat transport in 2 days?

PB: The school is organizing a trip to the museum. 
4 buses were hired to take the children and teachers to their destination. 
The second bus has twice the number of people on it as the first bus. 
The third bus has 6 fewer people than the second bus. 
The fourth bus has 9 more people than the first bus. 
If the first bus has 12 people, how many people are going to the museum in total?
Problem Pair Construction

To construct problem pairs for fusion, for each problem PA, a suitable problem PB needs to be identified. A straightforward approach is to select a problem PB that shares the same type and similar context with PA. Formally, the problem pair set Dp pair is defined as:

SIM(PA, PB) is the inner product of the embeddings of PA and PB using OpenAI embedding API text-embedding-3-large

Sequential Fusion

Sequential fusion constructs a new mathematical problem Pseq by establishing solution dependencies between two original problems PA and PB through shared variables, where the answer of PA becomes a prerequisite for solving PB.
# Role: Mathematical Problem Merger
## Profile
Your role is to merge "#Problem 1#" and "#Problem 2#" into a combined problem.
## Guidelines
Step 1: Identify input and output variables in both problems. 
Determine mathematical relationships and constraints in each problem. 
Locate variables between "#Problem 1#" and "#Problem 2#" that can form sequential dependencies.
Step 2: Formulate a comprehensive plan to merge the two problems by using "#Problem 1#"’s output variable to replace an input variable of "#Problem 2#"’s. 
Merge contextual elements by embedding both problems within a unified real-world scenario or extended narrative, aligning units and measurement systems.
Step 3: Create a single "#Combined Problem#" where solving "#Problem 1#" is a prerequisite for "#Problem 2#".
Explicitly state variable dependencies and which variable is replaced. Adjust numerical ranges to maintain arithmetic consistency. 
The "#Combined Problem#" should contain no supplementary explanation or note.
## Output Format
Please reply strictly in the following format:
#Elements Identified#:
#Plan#:
#Combined Problem#:
## Input
### #Problem 1#
{problem1}
### #Problem 2#
{problem2}
## OutputP seq: The school has organized a trip to a museum and
needs to transport children and teachers. First, calculate
how many people can be transported by a boat over 2 days,
with 4 boat trips each day, and each trip can carry up to 12
people. Let this total be the number of people in the first
bus. The second bus has twice the number of people on the
first bus, the third bus has 6 fewer people than the second
bus, and the fourth bus has 9 more people than the first bus.
How many people are going to the museum in total?
Parallel Fusion

Analogous problems often share common mathematical concepts and essences. Parallel fusion leverages this by synthesizing Ppara through the

integration of two conceptually analogous problems PA and PB , thereby creating a new problem that encapsulates their shared mathematical essence. This approach emphasizes the conceptual relationships between problems rather than their sequential dependencies.

where P ′ A and P ′ B denote the potentially modified problems from PA and PB, respectively, for the fused problem P para F . The function Φ encompasses various operations, such as algebraic composition and the enforcement of constraint satisfiability, to rigorously integrate the underlying mathematical structures.
# Role: Mathematical Problem Synthesizer
## Profile Your role is to organically integrate "#Problem 1#" and "#Problem 2#" to create a novel problem that requires advanced synthesis of their mathematical essence.
## Guidelines
Step 1: Conduct deep structural analysis of both problems by identifying their fundamental mathematical operations, contextual frameworks, and cognitive patterns. 
Extract the underlying logical architectures while preserving their distinctive solution pathways.
Step 2: Develop an innovative fusion mechanism by discovering non-obvious mathematical connections between the problems’ core concepts. 
Construct a multidimensional scenario that naturally embeds both original contexts through temporal sequencing, spatial superposition, or conceptual analogy.
Engineer hybrid parameters that inherit characteristics from both source problems while introducing emergent properties.
Step 3: Formulate the synthesized problem through strategic recombination of mathematical elements, ensuring the new problem requires concurrent application of both original solution strategies. 
Introduce controlled complexity through cross-domain constraints and self-verification mechanisms that establish mathematical consistency with both source problems’ answers.
## Output Format
Please reply strictly in the following format:
#Core Elements#:
#Synthesis Method#:
#New Problem#:
## Input
### #Problem 1#
{problem1}
### #Problem 2#
{problem2}
## OutputP para: A school organizes a field trip to a museum and hires
4 buses and a boat. The boat makes 2 trips in one day, with
a capacity of 12 people per trip. Each bus has a different
number of people: the first bus bus has 12 people ... the
fourth bus has 9 more people than the first bus.
Calculate the total number of people transported by the
boat and the buses over the course of 2 days. How many
people can the boat and buses transport in total for the trip?
Conditional Fusion

Conditional fusion synthesizes Pcond by integrating PA and PB into a cohesive real-world scenario, where the final solution is derived through contextual comparison or selection of outcomes from PA and PB.

Γ is a comparison function that contrasts PA and PB based on predefined logical or contextual rules
# Role: Problem Integrator
## Profile
Create a real-world problem where the solution requires solving both "#Problem 1#" and "#Problem 2#" independently.
**Ensure the the final answer is either from "#Problem 1#" or "#Problem 2#", depends on the "#New Question#"**.
## Guidelines
Step 1: Analyze "#Problem 1#" and "#Problem 2#" and make sure that the output variables they ask about are of the same type. 
If they are different (for example, one asks about time and the other asks about price), modify one of the problem so that it asks about the same variable as the other.
Step 2: Design a unified problem scenario that combines "#Problem 1#" and "#Problem 2#". Introduce a "#New Question#", which must be related with both "#Problem 1#" and "#Problem 2#". 
Ensure that final answer of the "#New Question#" must either come from "#Problem 1#" or "#Problem 2#". 
This means that the "#New Question#" should be an **comparison** and **selection** of the previous answers, not their **combination**. 
There are some examples for the "#New Question#":
1. Who sells the most items?
2. How much money does the top earner make?
3. Which is the cheaper plan?
4. Someone has 200 dollor, which item can he afford?
Step 3: Provide the "#New Problem#", which combine "#Problem 1#", "#Problem 2#", and "#New Question#" in a unified real-world scenario.
Don’t contain solution of "#Problem 1#" and "#Problem 2#" in "#New Problem#". 
Avoid using the phrases "#Problem 1#" and "#Problem 2#" in the generated "#New Problem#".
## Output Format
Please reply strictly in the following format:
#Analysis#:
#New Question#:
#New Problem#:
## Input
### #Problem 1#
{problem1}
### #Problem 2#
{problem2}
## OutputP cond: A local community is organizing two different outings. 
For a lake excursion, a boat operates 4 trips a day
with a capacity of 12 people per trip. They plan to run this
boat service for 2 days. Meanwhile, a school is arranging
a trip to the museum with 4 buses. The first bus has 12
people, the second bus has twice as many people as the
first, the third bus has 6 fewer people than the second, and
the fourth bus has 9 more people than the first bus. Given
these arrangements, which mode of transportation has a
larger capacity for transporting people?
MathFusionQA Dataset

GPT-4o-mini is used to fuse the problems and generate the corresponding solutions.
Comparison between MathFusionQA and previous mathematical datasets.
Evaluation

DeepSeekMath7B, Mistral-7B, Llama3–8B are fine-tuned on MathFusionQA for 3 epochs.

Zero-shot performance evaluation on in-domain benchmarks (GSM8K, MATH) and out-of-domain benchmarks (CollegeMath, DeepMind-Mathematics, OlympiadBench-Math, TheoremQA).
Performance comparison on mathematical benchmarks.
All three fusion strategies significantly improve performance compared to training on the standard combined GSM8K and MATH datasets, demonstrating effectiveness in both in-domain and out-of-domain generalization.
Sequential and parallel fusion strategies generally outperform conditional fusion, potentially because conditional fusion doesn’t require the same level of mathematical transformation.
Combining all three fusion strategies leads to further performance improvements, especially for weaker base models. This suggests that each strategy captures unique aspects of problem fusion.
MathFusion models achieve competitive performance and high data efficiency compared to existing top-performing models, even with the same data size. They outperform models like RefAug and achieve comparable results to MetaMath and DART-Math, demonstrating strong generalization ability.

Paper

MathFusion: Enhancing Mathematic Problem-solving of LLM through Instruction Fusion 2503.16212

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on April 21, 2025.

Canonical link

Exported from Medium on May 4, 2026.
