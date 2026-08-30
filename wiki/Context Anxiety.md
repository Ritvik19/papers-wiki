# Context Anxiety

#concept

Context anxiety is a Cursor-coined term, introduced in [[Continually Improving Our Agent Harness]], for a model behavior where the agent starts refusing work and hedging that the task seems too big as its context window fills up. Cursor encountered the behavior in at least one production model and reduced it through prompt adjustments at the [[Agent Harness]] layer rather than waiting for a model retraining cycle.

## Where It Sits

Context anxiety is a sibling phenomenon to [[Context Rot]] from [[Papers Explained 445 - Context Rot]]: both are degradation modes that emerge as input length grows. Context rot describes accuracy and reliability falling off as input length scales, even on simple tasks, while context anxiety describes a softer, behavioral failure where the model proactively refuses or hedges instead of attempting the work. Both are reasons why the modern Cursor harness keeps the static base small and prefers [[Dynamic Context]] retrieval.

The Cursor article frames context anxiety as a quirk that the harness can mitigate. It is one of several model-specific behaviors the team identifies during early-access tuning and addresses with custom prompting before the model ships in production.

## Related

- [[Continually Improving Our Agent Harness]]
- [[Agent Harness]]
- [[Context Rot]]
- [[Papers Explained 445 - Context Rot]]
- [[Long Context]]
- [[Dynamic Context]]
