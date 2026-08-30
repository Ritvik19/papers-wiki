# CUA-World

#entity

CUA-World is the benchmark-and-training collection introduced by [[Gym-Anything]], built to evaluate [[Computer-use Agents]] on realistic software rather than only short consumer-style desktop tasks. It packages more than 10,000 tasks across 200 software applications and three operating systems, with train/test splits and a harder long-horizon split designed to expose failure modes in current agents.

## Overview

The benchmark's defining move is breadth with occupational grounding. Software is selected using a GDP-grounded pipeline that starts from U.S. occupation data, expands into software discovery, filters for sandboxable GUI applications, and then balances economic weight with strategic and domain diversity. That makes [[CUA-World]] less like a narrow benchmark for browser or OS automation and more like a slice of real digital work across medicine, science, engineering, finance, enterprise systems, and education.

Verification is also more ambitious than simple end-state checks. Tasks use checklist-based grading with privileged information extracted from setup scripts, so a verifier can judge whether the agent actually completed the intended workflow and whether integrity constraints were respected. The long-horizon split, CUA-World-Long, remains difficult even for strong frontier agents, which is one reason the page is useful alongside [[RL Environments]] and [[Agentic AI]] rather than only as a benchmark artifact.

## Notes

- The paper reports 10K-plus tasks across 200 software applications on Linux, Windows, and Android.
- CUA-World-Long contains one harder long-horizon task per software, often exceeding 500 interaction steps.
- The strongest frontier result reported in the paper is 27.5% pass rate on CUA-World-Long.
- A test-time audit pass improves Gemini-3-Flash from 11.5% to 14.0% on the long split.
- Distillation from successful trajectories into a 2B vision-language model beats models about twice its size.

## Related

- [[Gym-Anything]]
- [[Computer-use Agents]]
- [[RL Environments]]
- [[Agentic AI]]
- [[Vision Language Models]]
