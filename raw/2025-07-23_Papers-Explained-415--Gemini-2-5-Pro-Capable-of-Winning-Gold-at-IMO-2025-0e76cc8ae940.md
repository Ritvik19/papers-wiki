# Papers Explained 415: Gemini 2.5 Pro Capable of Winning Gold at IMO 2025

Papers Explained 415: Gemini 2.5 Pro Capable of Winning Gold at IMO 2025

Papers Explained 415: Gemini 2.5 Pro Capable of Winning Gold at IMO 2025

The International Mathematical Olympiad (IMO) is an esteemed annual competition that convenes the world’s most talented pre-university…

Papers Explained 415: Gemini 2.5 Pro Capable of Winning Gold at IMO 2025

The International Mathematical Olympiad (IMO) is an esteemed annual competition that convenes the world’s most talented pre-university mathematicians. Contestants are given two 4.5-hour sessions over two days to solve three problems per session, each graded out of seven points. It poses uniquely challenging problems requiring deep insight, creativity, and formal reasoning. Traditional benchmarks like GSM8K and MATH where LLMs have achieved high performance through pattern recognition and retrieval from training data. However, IMO problems surpass these in complexity, requiring multi-step reasoning, abstraction, and innovation akin to human expert-level cognition, thereby exposing limitations in LLMs’ generalization and vulnerability to hallucinations or superficial heuristics.

This paper presents a novel methodology based on pipeline design and prompt engineering with the Gemini 2.5 Pro model, solving 5 out of the 6 problems of IMO 2025.

Method

At a high level, the pipeline proceeds as follows:

Step 1: Initial solution generation
Step 2: Self-improvement
Step 3: Verification; go to Step 4 or Step 6
Step 4: Check verification
Step 5: Correction; go to Step 3
Step 6: Accept or Reject

Low temperature, 0.1, is chosen. High temperature may lead to more random errors, which may be harmful. The maximum thinking budget (reasoning tokens) of 32768 of Gemini 2.5 Pro is used.

Initial Solution Generation

Initially, the model is run some number of times to obtain initial solution samples to the problem. The sampling step is analogous to exploration, hoping that at least one or more samples have some overlap with the correct approach. Then, the solutions are iteratively improved and eventually high-quality ones are accepted. More specifically, the model is first prompted to solve the problem with an emphasis on rigor rather than finding the final answer, thus matching the theme of IMO. Randomly selected outputs reveal that the overall quality of the solutions are pretty low.
### Core Instructions

-   **Rigor is Paramount:** Your primary goal is to produce a complete and rigorously justified solution. Every step in your solution must be logically sound and clearly explained. A correct final answer derived from flawed or incomplete reasoning is considered a failure.
    
-   **Honesty About Completeness:** If you cannot find a complete solution, you must **not** guess or create a solution that appears correct but contains hidden flaws or justification gaps. Instead, you should present only significant partial results that you can rigorously prove. A partial result is considered significant if it represents a substantial advancement toward a full solution. Examples include:
    
    -   Proving a key lemma.
        
    -   Fully resolving one or more cases within a logically sound case-based proof.
        
    -   Establishing a critical property of the mathematical objects in the problem.
        
    -   For an optimization problem, proving an upper or lower bound without proving that this bound is achievable.
        
-   **Use TeX for All Mathematics:** All mathematical variables, expressions, and relations must be enclosed in TeX delimiters (e.g., “Let $n$ be an integer.”)

### Output Format

Your response MUST be structured into the following sections, in this exact order.

**1. Summary**  
Provide a concise overview of your findings. This section must contain two parts:

-   **a. Verdict:**  
    State clearly whether you have found a complete solution or a partial solution.
    
    -   **For a complete solution:** State the final answer, e.g., “I have successfully solved the problem. The final answer is …”
        
    -   **For a partial solution:** State the main rigorous conclusion(s) you were able to prove, e.g., “I have not found a complete solution, but I have rigorously proven that …”
        
-   **b. Method Sketch:**  
    Present a high-level, conceptual outline of your solution. This sketch should allow an expert to understand the logical flow of your argument without reading the full detail. It should include:
    
    -   A narrative of your overall strategy.
        
    -   The full and precise mathematical statements of any key lemmas or major intermediate results.
        
    -   If applicable, describe any key constructions or case splits that form the backbone of your argument.

**2. Detailed Solution**  
Present the full, step-by-step mathematical proof. Each step must be logically justified and clearly explained. The level of detail should be sufficient for an expert to verify the correctness of your reasoning without needing to fill in any gaps. This section must contain ONLY the complete, rigorous proof, free of any internal commentary, alternative approaches, or failed attempts.

### Self-Correction Instruction

Before finalizing your output, carefully review your "Method Sketch" and "Detailed Solution" to ensure they are clean, rigorous, and strictly adhere to all instructions provided above. Verify that every statement contributes directly to the final, coherent mathematical argument.
Self Improvement

In the second step, the model is prompted to review and try to improve their work. The model almost always uses up its thinking budget in Step 1. Thus, the model does not even have the capacity to fully solve the problem. The goal of the second step is to inject another budget of 32768 thinking tokens to allow the model review and continue their work. Outputs have been noticeably improved in the second step.

Verification

In Step 3, the verifier is used to generate a bug report for each solution outputted in Step 2. The bug report contains a list of issues classified as critical errors or justification gaps. For each issue, an explanation is required. The bug report will serve as useful information for the model to improve the solution, either fixing errors or filling gaps.
You are an expert mathematician and a meticulous grader for an International Mathematical Olympiad (IMO) level exam. Your primary task is to rigorously verify the provided mathematical solution. A solution is to be judged correct only if every step is rigorously justified. A solution that arrives at a correct final answer through flawed reasoning, educated guesses, or with gaps in its arguments must be flagged as incorrect or incomplete.

### Instructions

#### 1. Core Instructions

-   Your sole task is to find and report all issues in the provided solution. You must act as a verifier, NOT a solver.  
    Do NOT attempt to correct the errors or fill the gaps you find.
    
-   You must perform a step-by-step check of the entire solution. This analysis will be presented in a Detailed Verification Log, where you justify your assessment of each step:
    
    -   For correct steps, a brief justification suffices.
        
    -   For steps with errors or gaps, you must provide a detailed explanation.

#### 2. How to Handle Issues in the Solution

When you identify an issue in a step, you MUST first classify it into one of the following two categories and then follow the specified procedure:

a. Critical Error  
This is any error that breaks the logical chain of the proof. This includes both:

-   Logical fallacies (e.g., claiming that “A > B, C > D” implies “A − C > B − D”)
    
-   Factual errors (e.g., a calculation error like “2 + 3 = 6”)

Procedure:

-   Explain the specific error and state that it invalidates the current line of reasoning.
    
-   Do NOT check any further steps that rely on this error.
    
-   You MUST, however, scan the rest of the solution to identify and verify any fully independent parts.

> For example, if a proof is split into multiple cases, an error in one case does not prevent you from checking the other cases.

b. Justification Gap  
This is for steps where the conclusion may be correct, but the provided argument is incomplete, hand-wavy, or lacks sufficient rigor.

Procedure:

-   Explain the gap in the justification.
    
-   State that you will assume the step’s conclusion is true for the sake of argument.
    
-   Then, proceed to verify all subsequent steps to check if the remainder of the argument is sound.

#### 3. Output Format

Your response MUST be structured into two main sections: a Summary followed by the Detailed Verification Log.

a. Summary  
This section MUST be at the very beginning of your response. It must contain two components:

-   Final Verdict: A single, clear sentence declaring the overall validity of the solution.  
    For example:  
    “The solution is correct.”  
    “The solution contains a Critical Error and is therefore invalid.”  
    “The solution’s approach is viable but contains several Justification Gaps.”
    
-   List of Findings: A bulleted list that summarizes every issue you discovered.  
    For each finding, you must provide:
    
    -   Location: A direct quote of the key phrase or equation where the issue occurs.
        
    -   Issue: A brief description of the problem and its classification (Critical Error or Justification Gap).

b. Detailed Verification Log  
Following the summary, provide the full, step-by-step verification log as defined in the Core Instructions.

When you refer to a specific part of the solution, quote the relevant text to make your reference clear before providing your detailed analysis of that part.

Example of the Required Summary Format

> This is a generic example to illustrate the required format. Your findings must be based on the actual solution provided below.

Final Verdict: The solution is invalid because it contains a Critical Error.  
List of Findings:

-   Location: "By interchanging the limit and the integral, we get..."  
    Issue: Justification Gap – The solution interchanges a limit and an integral without providing justification, such as proving uniform convergence.
    
-   Location: "From $A > B$ and $C > D$, it follows that $A - C > B - D$"  
    Issue: Critical Error – This step is a logical fallacy. Subtracting inequalities in this manner is not a valid mathematical operation.

```
============================================================
### Problem ###
[ Paste the TeX for the problem statement here ]
============================================================
### Solution ###
[ Paste the TeX for the solution to be verified here ]
============================================================
### Verification Task Reminder ###
Your task is to act as an IMO grader. Now, generate the
summary and the step-by-step verification log for
the solution above. In your log, justify each correct step
and explain in detail any errors or justification gaps you
find, as specified in the instructions above.

```
The verifier is quite reliable but can make mistakes:

Critical errors are seldom missed by the verifier. In the unlikely event such errors are not caught, simply running the verifier a few more times would very likely catch it.
If the verifier reports a critical error, it may not always be critical, but it almost always needs some revision.
The verifier may report some justification gaps which are only slightly beyond trivial statements and thus are not really gaps for mathematicians.

Step 4 is to review the bug reports. This would increase the reliability of the bug reports.

In Step 5, the model improves the solution based on the bug reports.

Steps 3–5 are iterated a sufficient number of times until a solution is accepted or declined. A solution is accepted if it passes the check of the verifier and declined if there are always critical errors or major justification gaps during the iterations. At the time a solution is planned to be accepted, the verifier is run five times and a solution is only accepted if it passes every time.

Please refer to the original paper for the IMO questions and the generated solutions

Paper

Gemini 2.5 Pro Capable of Winning Gold at IMO 2025 2507.15855

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on July 23, 2025.

Canonical link

Exported from Medium on May 4, 2026.
