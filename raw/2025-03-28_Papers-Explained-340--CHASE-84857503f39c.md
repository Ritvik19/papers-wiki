# Papers Explained 340: CHASE

Papers Explained 340: CHASE

Papers Explained 340: CHASE

CHallenging AI with Synthetic Evaluations (CHASE) is a unified framework to synthetically generate challenging problems using LLMs without…

Papers Explained 340: CHASE

CHallenging AI with Synthetic Evaluations (CHASE) is a unified framework to synthetically generate challenging problems using LLMs without human involvement. For a given task, the approach builds a hard problem in a bottom-up manner from simpler components. The framework decomposes the generation process into independently verifiable sub-tasks, thereby ensuring a high level of quality and correctness. CHASE is implemented to create evaluation benchmarks across three diverse domains:

document-based question answering
repository-level code completion
math reasoning

CHASE Framework and Benchmarks

The high-level ideas behind the CHASE framework.

If a complex problem is first synthesized and then its corresponding solution is obtained from the generating LLM, that problem is inherently solvable by that LLM. However, the goal is to craft problems that are challenging even for the model which generates them. A different approach is taken where a simpler problem-solution pair is either generated or started with, and then a challenging context is built bottom-up. The problem’s context is made challenging by systematically hiding components of the solution or reasoning such that they need to be either extracted from a long context or inferred based on given information.

Pipelines use two different LLMs: the generator G and verifier V and are designed to break down the generation process into simpler sub-tasks. Each individual LLM in the pipeline performs a simpler, specific function in the generation process.

This grants more control over each step of the generation process. Each step can be treated as a task by itself and the corresponding inference parameters can be optimized individually. This also allows for better management of the complexity and diversity of the generated data depending on requirements.

This also facilitates fine-grained verification. LLMs that are not part of the generation process are deployed to check the correctness and quality of the generated data at each step. LLMs can be relied upon for verification because the framework makes each verification task smaller and simpler compared to the main task of generating or solving the problem being crafted.

CHASE-QA is a document-grounded question answering task consisting of 671 problems. Each example in CHASE-QA consists of a set of documents and a question- answer pair.
CHASE-CODE is a repository-level code completion benchmark consisting of 500 problems. Given a repository of Python functions, the task is to implement a new function based on a set of objectives. Data is created for two domains:

data pre-processing operations such as dataframe manipulation, string processing, etc.,
algorithms such as graph operations, array manipulations, etc.

CHASE-MATH consists of 500 grade-school level math word problems involving only basic arithmetic operations.

CHASE-QA

Generating diverse scenarios

G generates diverse and realistic scenarios defined by a (persona, collection name) tuple. This represents a specific user type searching within a defined set of documents.
The process is bootstrapped with 5 manually annotated scenarios.
G then uses its own generated scenarios as prompts to create further scenarios, expanding the dataset.
System Prompt: You are an expert generator of data.
---
You are a research scientist. 
You want to make data to test an advanced question answering system.
Give me 5 examples of real-life scenarios where a USER PERSONA may seek information in a COLLECTION OF DOCS. 
Do not consider educational or historical scenarios.
Some examples are:
USER PERSONA: College student
COLLECTION OF DOCS: Intranet on the university website
USER PERSONA: Intern doctor at a hospital
COLLECTION OF DOCS: Encyclopedia of diseases
USER PERSONA: Immigrant in NYC
COLLECTION OF DOCS: Laws on renting and subletting
USER PERSONA: HR manager at a top law firm
COLLECTION OF DOCS: Court and newspaper records
USER PERSONA: Scientist at an NGO
COLLECTION OF DOCS: Government website for Income Tax
Answer in the following format:
USER PERSONA:
COLLECTION OF DOCS:
Generating question-answer (QA) pairs

Given a scenario, G generates a realistic information-seeking question that the persona might ask about the specified document collection.
G also generates the corresponding answer to the question. These answers are designed to be complex, composed of multiple points or ideas.
Crucially, G also generates outlines (title and abstract) for a set of documents that collectively contain the complete answer. The answer points are distributed across these different documents.
System Prompt: You are an expert generator of data. 
Do not use "**" to start lines or denote points.
---
You are a research scientist. 
You want to make data to test an advanced question answering system.
Give me an example question and corresponding answer that a {USER PERSONA} may ask that compulsorily requires searching a {COLLECTION OF DOCS}. 
Make questions that cannot be answered directly with general knowledge but necessarily require some uncommon information that is present in some documents. 
The answer must be very specific and written in bullet points, so that it is easier to objectively evaluate. 
Depending on the question, the answer can have anything between 3-6 bullet points without any sub-points.
The answer to the question you create must be scattered across different documents (at least 3).
Assign each point of the answer to a specific document in which that point will be discussed. 
You may assign multiple points to the same document, but each point must only be assigned to a single document. 
You must state the title and answer points assigned for each of the documents.
Answer in the following format:
Question: <Question>
Answer: <Answer>
Document 1 Title: <Title>
Document 1 Answer points assigned: <Points>
Document 2 Title: <Title>
Document 2 Answer points assigned: <Points>
and so on...
Generating irrelevant information

To increase the difficulty of the retrieval task, G generates additional QA pairs for each original question.
These new questions are designed to have answers that are similar in type to the original answer, but are ultimately irrelevant to the original question.
This mimics the real-world challenge of sifting through related but unhelpful information.
V is used to verify the irrelevance of these generated QA pairs. It is prompted with the original question and each of the supposedly irrelevant information points to confirm that they do not contribute to answering the original question.
System Prompt: You are an expert generator of data. 
Do not use "**" to start lines or denote points.
---
You are a research scientist. 
You want to make hard data to test an advanced question answering system. 
You are given a question that a {USER PERSONA} might want answered, along with the corresponding answer, and information of documents from {COLLECTION OF DOCS} that are important for answering that question.
Original Question: {QUESTION}
Original Answer: {ANSWER}
Original Documents Information: {DOCS INFORMATION}

You must generate an adversarial question, adversarial answer, and corresponding adversarial documents that ask for something different but on similar topics or type so that it is difficult to answer the original question. Examples of how adversarial questions should look like are provided below:

Original Question: What are the best activities to do in Montreal, Canada during the winter season?
Adversarial Question: What activities should I look at when visiting Tokyo during the summer?
[Redacted]
Also provide an answer to the adversarial question, which is similar in style to the original answer, but differs significantly in information or specifics. 
The answer points for the adversarial question should be written in context of that adversarial question, so that they cannot be confused with the original question. 
Note that none of the points appearing in the original answer should be present in the answer to the adversarial question.
The answer to the adversarial question you craft must be scattered across different documents (at least 3) separate from the original answer documents. 
Assign each point of the adversarial answer to a specific document in which that point will be discussed. 
You may assign multiple points to the same adversarial document, but each point must only be assigned to a single adversarial document.
You must state the title and adversarial answer points assigned for each of the adversarial documents.
These adversarial documents should not have any overlapping information with the original answer documents.
Answer in the following format:
[Redacted]System Prompt: You are an expert at verifying data.
---
You are given a question and an answer. 
You must check whether the answer is even partially relevant for answering the question. 
If the answer is not relevant at all, output “False” to “Relevance”.
Otherwise, if and only if the answer discusses information that is at least partially necessary to answer the question, output “True”.
Question: {QUESTION}
Answer:
{IRRELEVANT ANSWERS}
Give output in the following format:
Relevance: True/False
Generating documents

For each QA pair (including both the original and the irrelevant ones), G generates full-length documents.
These documents discuss the assigned answer points (from step 2) along with other irrelevant information, creating a realistic, cluttered context.
Two verification steps using V ensure data quality:
Completeness: V checks that all parts of the ground-truth answer are present across the generated documents.
No Leakage: V checks that the documents do not contain any information relevant to the original question except for the pre-defined ground-truth answer points. This prevents accidental inclusion of the answer in irrelevant documents.
System Prompt: You are an expert data generator. 
Following the instruction, you must generate long and correct documents.
---
You need to generate the documents for an example of a retrieval based Question Answering Task.
The task consists of n documents provided in English text that consist of information about different topics and a question.
To answer the question correctly compulsorily requires using some of the information in some subset of the documents provided.
Given below is a situation faced by {USER PERSONA} when searching {COLLECTION OF DOCS}. 
The question-answer pair is:
Question: {QUESTION}
Answer: {ANSWER}
Given below are the assigned answer points for each document.
{DOCS INFORMATION}
Your job is to create long documents according to this information. 
For each document, first create 10-12 unique other points that are in no way related to the topic of the question and answer (different points for each document).
These points should discuss very different things about a similar but different topic. 
Then use these points along with the assigned answer points to create a long document (at least 700 words long). 
The assigned answer points must be discussed taking into account the question. 
You must only discuss about these points and nothing else. 
Change the order of the points so that the answer points are embedded inside the document. 
Assign an appropriate title to the document. 
Do not summarize or conclude the document in the end.
Additionally, ensure that the documents you create do not have any information related to the following irrelevant question-answer pairs. 
You should create documents that discuss topics that are completely different from the following information.
{IRRELEVANT QUESTIONS ANSWERS}
Give output in the following format:
Document 1:
Title: <Title>
Question: {QUESTION}
Answer points assigned [Only these points must be covered with respect to the question]: <Points>
Other unrelated points created: <Points>
Text:
<Document Text>
[Redacted]
and so on...System Prompt: You are an expert at verifying data.
---
You are given a document followed by a question and some answer points. You must check whether there are any additional major points in the document that provide relevant information for answering the question that are currently missing from the answer. Follow these instructions:
1. Do not look for exact phrases or explicit mentions since the answer can have points that are a paraphrase of the same broad information.
2. It is ok if the document provides more specifics or details about the points already in the answer or if it discusses them in more depth by introducing related information so you can ignore that.
3. Check if the document introduces a new “major” idea or point that is crucial for answering the question and is not at all mentioned in the answer and is not an extension of the existing points in the answer.
4. Your job is not to check if the question can be sufficiently answered. You should ignore if the document or answer points are missing any points that are needed in the answer to the question.

If the document is not introducing major new points pertaining to the answer, output “False” to “Presence of Extra Points” without giving any explanation. 
Otherwise, if and only if the document discusses major additional points that are necessary to answer the question, output “True” and mention only the extra major points discussed.
Document:
{Document}
Question: {QUESTION}
Answer Points:
{ANSWER}
Give output in the following format:
Presence of Extra Points: True/False
Extra Points Mentioned (if any):System Prompt: You are an expert at verifying data.
---
You are given a document followed by a question and an answer point. You must check two things:
1. Presence: Is the point mentioned in the document?
2. Relevance: Is the point discussed in a manner such that it can be used to partially answer the question?
Document:
{DOCUMENT}
Question: {QUESTION}
Answer Point:
{ANSWER POINT}
Give output in the following format:
Presence: True/False
Explanation for Presence:
Relevance: True/False
Explanation for Relevance:
Setup

GPT-4o is used as the generator G, and GPT-4o-mini as the verifier V. Five hundred unique scenarios are sampled. For each scenario, 2 QA pairs are generated. For each of the resulting 1000 unique QA pairs, irrelevant information is obtained by generating 4 similar QA pairs. The corresponding documents containing the ground-truth answer as well as irrelevant information are then generated for each of the 1000 examples. To increase the complexity of the resulting benchmark, rejection sampling is carried out. GPT-4o-mini is evaluated twice on the task, and randomly discarded half of the problems on which it was correct both times. This yielded the final benchmark of 671 examples.
System Prompt: You are an expert at answering questions based on documents.
---
You are given some documents followed by a question. 
You need to generate the answer for that question. 
Provide the answer in bullet points, so that it is easier to objectively evaluate. 
Answering the question correctly requires information from multiple documents. 
You must only generate the points necessary for answering the question, without mentioning anything irrelevant to the question.
If you find no relevant information in the documents for answering the question, you must only generate “No relevant information found in the documents.” and nothing else.
Documents: {DOCUMENTS}
Question: {QUESTION}
Answer:System Prompt: You are an expert evaluator.
---
You are given a question, irrelevant answers, the ground-truth answer, and a prediction. 
You need to evaluate whether the prediction is correct by matching against the ground truth answer. 
Do not look for exact phrases or words since the prediction can have points that are a paraphrase of the same information. 
Based on the question, check for the presence of the same ideas or main points in the prediction as in the ground-truth answer. 
All the main points in the ground-truth answer must be mentioned in the prediction. 
The order of points mentioned is irrelevant. 
It is allowed for the prediction to elaborate or provide more specifics or details over the major points in the ground-truth answer. 
However, the prediction should not contain additional major points that are contradictory or irrelevant for answering the question. 
Importantly, the prediction must not discuss any of the points mentioned in the “irrelevant answers”. 
The first word in your response must be either True or False. 
If False, explain why you think the prediction is wrong in detail.
Question: {QUESTION}
Irrelevant Answers: {IRRELEVANT ANSWERS}
Ground-truth Answer: {GROUND TRUTH ANSWER}
Prediction: {PREDICTION}
Result:
CHASE-CODE

Generating Python functions

G generates diverse Python functions for a specific domain (e.g., algorithms, data pre-processing). This starts with 3 annotated examples as a bootstrap, and G then uses its own generated functions as prompts for creating more. V verifies the correctness of these helper functions by generating and executing code that calls them with sample inputs.
System Prompt: You are an expert generator of code data.
---
You are a research scientist. 
You want to make data to test an advanced code generation system. 
You are given a domain. 
Assume that there is a large python code base ’C’ with at least 10 python files on that domain.
Domain: {DOMAIN}
You need to create 5 functions in this codebase for achieving various objectives. 
First define the parameters that will be input to the function. 
Then define the objective of the function. 
The objective must consist of 3-4 sub-goals, each of which must involve complex logic that make it very difficult to implement the function. 
However, each sub-goal must be well-specified such that there is only one way to implement the sub-goal. 
Then based on the objective, you need to create a single function (do not create other functions inside this).
Some examples are:
Parameters:
- data: pandas.DataFrame
- k: int
Objectives:
- In the dataframe “data”, find the “frequency” of occurence of rows that have at least one string field
with the number of letters divisible by “k”.
[redacted]
Function “filter k frequency” in file “string filters.py”:
```python
import pandas as pd

def filter_k_frequency ( data , k ) :
    [ redacted ]
    return frequency , filtered_df
```
Now you need to create 5 unique, diverse, and complex functions. Answer in the following format:
Function <Number>:
Parameters:
- <para name>: <data type>
...
Objectives:
- <sub goal>
...
Function “function name” in file “file name.py”:
<import statements>

<function definition>System Prompt: You are an expert tester of code systems.
---
You are given a function in a file. You need to check whether the function correctly executes.
{FUNCTION}
Follow these instructions:
1. You must output only a single long python code.
2. First initialize the input parameters for the function in python code. If the function reads data from files, you should create and store the necessary files with sample data in the corresponding filepath in the python code.
3. Finally, call the function with the input parameters. 

Give output in the following format:
```
# Import statements if required
import <>
...

# Import function from file
from < filename > import < function_name >
# Initialize input parameters
< param1 > = < value1 >
...
# Call function with input parameters
return_ < variable1 > , return_ < variable2 > , ... = < function_name >( < param1 > , <param2 > , ...)
```
Generating problem statement and answer code

To create a single problem, n helper functions are randomly sampled. G is prompted to create a complex “answer code” function that uses at least k of these “relevant” helper functions, along with additional logic. Simultaneously, G generates a natural language problem statement describing the objective of the answer code. V then performs two verification steps:

It generates test code to check the execution correctness of the answer code.
It verifies the sufficiency of the problem statement by prompting itself with the problem statement and relevant helper functions, checking if its generated code is semantically equivalent to the original answer code.
System Prompt: You are an expert generator of code data.
---
You are a research scientist. You want to make data to test an advanced code generation system.
Below, you are given 10 functions from a codebase “C” in the domain of {DOMAIN}.
Parameters:
- data: pandas.DataFrame
- k: int
Objectives:
- In the dataframe “data”, find the “frequency” of occurence of rows that have at least one string field
with the number of letters divisible by “k”.
[redacted]
Function “filter k frequency” in file “string filters.py”:
```
import pandas as pd
def filter_k_frequency ( data , k ) :
    [ redacted ]
    return frequency , filtered_df
```    
[redacted]
You need to create a complex function that calls at least 4 (but not more than 6) of these functions to achieve various objectives. 
Apart from just calling these functions, it should also implement some other pieces of complex logic. 
You first need to define the parameters that will be input to the function. 
Then you need to define the objective of the function. 
Follow these instructions for creating the objective:
1. The objective must consist of 6-8 sub-goals. Each sub-goal must be detailed and well-specified such that there is only one way to implement the sub-goal.
2. VERY IMPORTANT: The objective must not explicitly specify which functions should be called.
3. Always give names for variables you are talking about in the objective.
4. You must explicitly mention what parameters are to be used for a specific sub-goal by the name of the parameter.
5. Whenever a variable is obtained that must be returned by the function, you must explicitly state that in the sub-goal.
6. At least 2 of the sub-goals must involve some complex logic, apart from just calling helper functions that make it very difficult to implement the function.

Once you write down the objective, you need to create the function that achieves this objective.
Import the required functions from the codebase “C” and use them in your function.
You must give output in the following format:
[redacted]System Prompt: You are an expert programmer.
---
You are given a codebase with some files and functions in the domain of params[0]. 
You need to write a single python function to achieve the objectives specified in the problem statement. 
You may call the functions in the codebase when necessary. 
Do not give any examples of usage or any explanations.
Codebase:
{RELEVANT FUNCTIONS}
Problem Statement:
{PROBLEM STATEMENT}
Give output in the following format:
```
# Import statements if required
import <>
...
# Import necessary helper functions from their files
from < filename > import < function_name >
# Define the function
def < function_name >( < param1 > , < param2 > , ...) :
    # Your code here
    ...
    return < return_variable >
```    
Generating test code

G generates Python test code for the answer code. This test code independently implements the answer code’s logic, initializes the answer function with sample values, and compares the results with its own implementation. The generated test code is executed, and examples are discarded if the test code fails to execute or the answer code fails the test.
System Prompt: You are an expert tester of code systems.
---
You are given a function. 
You need to define an input-output test case for that function to exhaustively test all scenarios.
{ANSWER FUNCTION}
Follow these instructions:
1. You must output only a single long python code.
2. First initialize the input parameters for the function in python code. If the function reads data from files, you should create and store the necessary files with sample data in the corresponding filepath in the python code. Call the function and assign the return values to variables named as return <variable name>.
3. Then write new code to implement the exact logic of the function. This way, you need to simulate step-by-step how the values of the input parameters will be used to obtain the final return values. Call these values as correct <variable name>.
4. Finally, and most importantly use assert statements to compulsorily check if the returned outputs of the function (return <variable name> variables) match with the ones you computed yourself (correct <variable name> variables).
Give output in the following format:
```
# Import statements if required
import <>
...
# Import function from file
from < filename > import < function_name >
...
# Initialize input parameters
< param1 > = < value1 >
...
# Call function with input parameters
return_ < variable1 > , return_ < variable2 > , ... = $< function_name >( < param1 > , < param2 > , ...)
# Step -by - step run - through of function to obtain intermediate outputs :
# Step 1
# Explanation : <>
< Code for step -1 >
[ redacted ]

# Final Expected Output :
correct_ < variable1 > = < value1 >
...
# Assert statements ( compulsory ) to check if the function returns the correct
values :
assert return_ < variable1 > == correct_ < variable1 >
...
```
Building code repository

For each example, a repository of Python files is created. This repository includes the relevant helper functions distributed across different files, along with m randomly sampled irrelevant Python functions from a pre-generated set. This adds complexity to the problem, requiring understanding of a larger code context to identify the relevant functions for a given problem statement.

Setup

GPT-4o-mini is used as G, and Gemini-1.5-Flash as V. Generating challenging problems requires many iterations due to potential errors in generated code. For each domain, 500 executable helper functions are initially sampled. Then, using n = 10 random helper functions, G generates problem statements and answer code using at least k = 4 of them, aiming for 1000 examples per domain. Up to 10 test codes are generated per example, keeping only those where a test code passes. Problem statement correctness is also verified. This yields 290 algorithm examples and 300 data pre-processing examples. GPT-4o-mini is used for rejection sampling, discarding about half of the correctly solved problems. This results in a final benchmark of 500 examples (250 per domain). Each example’s repository contains m = 100 irrelevant helper functions distributed across 10 Python files.
System Prompt: You are an expert programmer. You must output only python code.
---
You are given a codebase. 
You need to write a single python function to achieve the objectives specified in the problem statement. 
In your function, you should call some of the functions in the codebase to achieve specific objectives. 
Do not give any examples of usage or any explanations.
Codebase:
{CODEBASE}
Problem Statement:
{PROBLEM STATEMENT}
Give output in the following format:
```
# Import statements if required
import <>
...
# Import necessary helper functions from their files
from < filename > import < function_name >
# Define the function
def < function_name >( < param1 > , < param2 > , ...) :
    # Your code here
    ...
    return < return_variable >
```    
CHASE-MATH

Breaking down seed MWP

A seed MWP is characterized by the tuples = (p,a) where p is the problem, and a is the answer. G is prompted to break down p into two parts: the context c, which provides all the information, and the question q, which asks about some unknown quantity.
System Prompt: You are an expert mathematician.
---
You are a research scientist. 
Your task is to create a hard math word problem to test an advanced math reasoning system. 
For that, you are given the following problem:
Q: {QUESTION}
A: {ANSWER}
Your job is to first divide up the problem into the “context” and the “question statement”. 
Isolate the quantity that the problem is inquiring about by looking at the final question statement and the rest of the information provided becomes the context. 
Also form a brief answer statement by phrasing the answer in a complete sentence. Do not include the answer statement in the context.
Give output in the following format only:
Original context [without question statement]: <>
Question statement: <>
Original answer: <>
Original answer statement: <>
Create continuation of MWP

A seed MWP s0 = (p0,a0) is used to prompt G to build a new problem which is a continuation of the previous problem. G should output a new problem s1 = (p1, a1), where the context of p1, i.e., c1 assumes a0 as given information (without explicitly stating it).
System Prompt: You are an expert mathematician.
---
You are a research scientist. 
Your task is to create a hard math word problem to test an advanced math reasoning system. 
For that, you are given the following problem:
Context: {CONTEXT}
Question statement: {QUESTION STATEMENT}
Answer: {ANSWER}
Answer statement: {ANSWER STATEMENT}

You need to further continue the problem over the answer quantity, by introducing a scenario and new question where you need to perform one more operation (such as +,-,/,*, etc.) over this quantity to get the final answer. 
Crucially, the new context must not mention the original answer - it still has to be inferred based on previous information. 
Do not make any calculation or inference in the new context. 
Try to make the new context challenging. 
Also provide a complete reasoning of how you reached the new answer (never round down or round up decimals).
Give output in the following format only:
New operation over original answer: <>
New context [Do not mention original answer]: <>
New question statement: <>
New answer reasoning: <>
New answer [Number only]: <>
Combining seed MWP with its continuation

By combining the seed problem with its continuation, we get a new MWP s = (p, a) with a higher reasoning depth, where the context c of the combined problem p is a concatenation of the contexts of the seed problem and the continuation c = c0 · c1. The question for the combined problem will be the one generated by the model, i.e., q1, and the answer a = a1.

Iteratively increase reasoning depth

Reasoning depth of a given seed MWP is increased by creating new continuations in an iterative manner. Each new continuation is formed after the ith iteration becomes the seed problem for the (i + 1)th iteration. The final problem after j successful iterations, i.e., with a reasoning depth of j + 1, is given by context c = c0 · c1 . . . cj, question qj, and answer a = aj.

Since each new problem created by G has a low reasoning depth of the same difficulty as the problems in the seed datasets, their correctness is verified using a non-identical ensemble of verifier models {V1, V2, . . . , Vn}, each of which performs well on the seed dataset. Each Vk is prompted with the generated context ci and question qi and checks whether the prediction is the same as the generated answer ai. If this fails for any verifier, si is discarded and the process begins again with si−1 as the seed MWP.
System Prompt: You are an expert mathematician. Your final statement must be of the form ’The answer is <answer>’.
---
Solve the final math word problem given below by thinking step-by-step. 
You should always work with exact numbers - never round down or round up decimals based on context. 
Give the final answer in the end by saying “The answer is <number>”.

Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?
A: There are 15 trees originally. Then there were 21 trees after some more were planted. So there must have been 21 - 15 = 6. The answer is 6.
Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?
A: There are originally 3 cars. 2 more cars arrive. 3 + 2 = 5. The answer is 5.
Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?
A: Originally, Leah had 32 chocolates. Her sister had 42. So in total they had 32 + 42 = 74. After eating 35, they had 74 - 35 = 39. The answer is 39.
Q: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?
A: Jason started with 20 lollipops. Then he had 12 after giving some to Denny. So he gave Denny 20 - 12 = 8. The answer is 8.
Q: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?
A: Shawn started with 5 toys. If he got 2 toys each from his mom and dad, then that is 4 more toys. 5 + 4 = 9. The answer is 9.
Q: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?
A: There were originally 9 computers. For each of 4 days, 5 more computers were added. So 5 * 4 = 20 computers were added. 9 + 20 is 29. The answer is 29.
Q: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?
A: Michael started with 58 golf balls. After losing 23 on tuesday, he had 58 - 23 = 35. After losing 2 more, he had 35 - 2 = 33 golf balls. The answer is 33.
Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?
A: Olivia had 23 dollars. 5 bagels for 3 dollars each will be 5 x 3 = 15 dollars. So she has 23 - 15 dollars left. 23 - 15 is 8. The answer is 8.
Q: {QUESTION}
A:System Prompt: You are an expert mathematician. Your final statement must be of the form ’The answer is <answer>’.
---
You need to solve the given math word problem. 
You should break down the problem sentence by sentence, and solve each sentence, one at a time, from start to finish until you get the final answer.
You should always work with exact numbers - never round down or round up decimals based on context. 
Give the final answer in the end by saying “The answer is <number>”.
Given below are illustrations of solving sentence-by-sentence:
Q: In a store, an Uno Giant Family Card costs $12. 
    When Ivan bought ten pieces, he was given a discount of $2 for each. 
    The store has a 8% sales tax added to all purchases. 
    Ivan decides to save 25% of this expenditure for a future vacation. 
    After saving, Ivan instead decides to split this amount between two of his friends who are always helping him out. 
    One of the friends decided to split their received amount equally among the five children in Ivan’s neighborhood who helped him move the previous day. 
    How much will each child receive?
A:  Sentence 1: Uno card costs $12.
    Sentence 2: Ivan bought 10 cards and there was a discount of $2 each. So, 10 * $12 = $120 total cost of cards and, 10 * $2 = $20 discount.
    Sentence 3: Sales tax is 8% of ($120 - $20 = $100). So, 8% of $100 = $8.
    Sentence 4: Ivan saves 25% of ($100 + $8) = $108. So, 25% of $108 = $27.
    Sentence 5: Ivan splits $27 between 2 friends. So, $27 / 2 = $13.50 each.
    Sentence 6: One friend splits $13.50 among 5 children. So, $13.50 / 5 = $2.70 each.
    The answer is 2.70.
[redacted]
Q:  Carly is trying to get in shape to try out for the soccer team. 
    She starts by running 2 miles a week.
    The second week, she runs twice as long plus 3 extra miles per week. 
    The third week she runs 9/7 as much as she ran the second week. 
    The week after that, she sprains her ankle and has to reduce her running time by 5 miles this week compared to the previous week. 
    After a few weeks of recovering from her ankle injury, Carly starts to feel better and decides to gradually increase her running time.
    She starts with a shorter routine that is one quarter of the amount she ran the week she was injured.
    After a week of intense training, Carly decides to boost her speed and endurance by increasing her weekly running routine to 2.5 times longer. 
    Carly is planning increase the weekly routine by 5 times now. 
    How much is Carly planning to run every week?
A:  Sentence 1: Nothing to solve.
    Sentence 2: Carly runs 2 miles a week.
    Sentence 3: Carly runs 2 * 2 + 3 = 7 miles in the second week.
    Sentence 4: Carly runs 9/7 * 7 = 9 miles in the third week.
    Sentence 5: Carly reduces her running time by 5 miles this week. So, 9 - 5 = 4 miles.
    Sentence 6: Nothing to solve.
    Sentence 7: Carly starts with 1/4 of 4 miles = 1 mile.
    Sentence 8: Carly increases her running routine to 2.5 times longer. So, 1 * 2.5 = 2.5 miles.
    Sentence 9: Carly wants to make her long run 5 times as long. So, 2.5 * 5 = 12.5 miles.
    The answer is 12.5.
Q: {QUESTION}
A:
Setup

GPT-4o-mini is used as the generator G, and an ensemble of Gemini-1.5-Flash and Llama-3.1–70B as the verifier V. Many of the model generated problems would fail at various stages of verification, so it is faster and cheaper to query the smaller models.

2.3k seed problems are taken from the test sets of GSM8k and SVAMP. The maximum and minimum reasoning depth are set at 8 and 2 respectively. For each problem, 15 iterations are performed to generate a problem continuation.

This process is carried out 3 times. In this manner, around 1500 problems are generated. Rejection sampling is then carried out and roughly 75% of the problems that GPT-4o-mini could solve are discarded. In the end, a total of 500 challenging MWPs are produced.

Evaluation
The performance of various LLMs on all 3 domains of the CHASE benchmark.
LLMs struggle with CHASE benchmarks: Even the best-performing LLMs showed relatively low accuracy on all three CHASE benchmarks, indicating significant room for improvement in LLM reasoning capabilities.
CHASE differentiates LLM performance: The CHASE benchmarks effectively distinguish the performance of different LLMs, unlike standard benchmarks where performance tends to be similar.
Gemini models excel in long-context reasoning: Gemini models outperformed other LLMs on the long-context benchmarks (CHASE-QA and CHASE-CODE), demonstrating their strength in this area.
Targeted performance differences observed: The benchmarks revealed specific strengths and weaknesses of different LLMs, such as GPT-4o’s proficiency in data pre-processing within CHASE-CODE.
Suspected contamination of existing math benchmarks: Large performance discrepancies between weaker and stronger LLMs on CHASE-MATH compared to existing benchmarks suggest potential contamination in those benchmarks.
Performance of LLMs on data generated by direct prompting approaches without using CHASE.
Direct prompting yields easier data: Directly prompting LLMs to generate challenging data resulted in easier datasets compared to those generated by CHASE.

Performance declines with increasing context: LLM performance decreased with increasing context size on both CHASE-QA and CHASE-CODE.
LLM judging is reliable: GPT-4o’s judgements showed high agreement with human annotators on CHASE-QA.

Limited benefit from fine-tuning with weak model data: Fine-tuning smaller models with data generated by weaker models resulted in only marginal performance improvements on CHASE-MATH.

Paper

How to Get Your LLM to Generate Challenging Problems for Evaluation 2502.14678

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on March 28, 2025.

Canonical link

Exported from Medium on May 4, 2026.
