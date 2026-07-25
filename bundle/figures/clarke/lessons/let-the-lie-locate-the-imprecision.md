---
type: lesson
title: "Let the false answer locate the imprecision"
figure: clarke
works: [counterexample-guided-abstraction-refinement, model-checking-algorithmic-verification-and-debugging]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Let the false answer locate the imprecision

**Lesson:** Choosing how coarse a model to reason with used to be a human act requiring insight, and it was the bottleneck: too coarse and you drown in false alarms, too fine and you cannot compute. The reframing here is to stop choosing at all. Start with whatever crude model can be extracted mechanically from the program's own control structure, and then let each false alarm pay for exactly the precision needed to eliminate it. The refinement is not guided by a person's model of what matters; it is guided by the specific way the current abstraction misled you.

The mechanism deserves attention because it shows what "guided by the failure" actually requires. A reported failing trace is replayed against the real system one step at a time, and if it dies, the step where it died identifies a single cluster of concrete states that was doing two contradictory jobs: some of its members are genuinely reachable but cannot continue along the reported trace, while others could continue but are not reachable. The cluster inherited the reachability of the first group and the outgoing transition of the second, and that splice is the lie. Refinement means splitting exactly that cluster so the two groups no longer share an abstract identity. Nothing else in the model is touched, and states in the same cluster that are implicated in neither role can be assigned to either side without consequence.

So the loop converts a diagnostic artifact into a control signal. Precision is not a global dial but a local expenditure, made only at the point where coarseness demonstrably caused a wrong answer, and only enough to invalidate that particular wrong answer. Each iteration is strictly more precise, so the process cannot cycle, and it terminates either by proving the property, by finding a real defect, or by exhausting the budget. In the reported industrial case a design that no available checker could handle was verified after three such steps, with most of its variables abstracted away.

A programmer who absorbs this stops trying to get the level of detail right in advance. Build the crudest model that could possibly answer the question, run it, and treat every false positive as a specific instruction about where the model needs to be sharper. The pattern recurs far beyond verification: coarse-to-fine profiling, progressively narrowing bisection, static analyses tuned by the false positives they emit. What makes it work in every case is that the wrong answer contains enough structure to say *where* it went wrong, which is a property you have to design for rather than hope for.

**Source:** [Counterexample-Guided Abstraction Refinement](../works/counterexample-guided-abstraction-refinement.md) — the overview of the three-step loop and the refinement section that classifies the concrete states inside a failure state as dead-end, bad, or irrelevant and defines refinement as separating the first two. The Turing lecture summarizes the same loop diagrammatically and notes its adoption in software checkers built on it.
