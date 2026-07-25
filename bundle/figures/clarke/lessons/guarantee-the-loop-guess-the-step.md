---
type: lesson
title: "Guarantee the loop, guess the step"
figure: clarke
works: [counterexample-guided-abstraction-refinement]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, algorithms-and-complexity]
tags: [lesson]
---
# Guarantee the loop, guess the step

**Lesson:** Inside the refinement loop sits a genuine optimization problem: among all the ways to split an over-coarse cluster so that the two conflicting groups of states are separated, find the one that creates the fewest new clusters, since abstract state count is what you are paying for. That problem is NP-hard, and the paper proves it rather than suspecting it. The response is not to solve it, nor to abandon the method, but to notice which guarantee the enclosing procedure actually needs. The loop requires only that each iteration strictly eliminates the spurious trace and does not lose soundness; it does not require that each iteration be minimal. So the optimum is dropped and a polynomial heuristic installed in its place, with correctness proved for the property the loop depends on.

What makes this more than pragmatism is the care taken about where the guarantee lives. The hardness proof is inspected to see what drives it, the driver turns out to be the states implicated in neither role, and under the condition that no such states exist the same polynomial algorithm is shown to produce the unique coarsest refinement — necessary and sufficient, both directions proved. So the heuristic is not a shrug; it is an exact algorithm for a characterized special case, used as an approximation outside it, with the boundary between the two regimes understood. The claim that it behaves well in general is then left to experiment, which is the honest place for that kind of claim.

The transferable habit is to separate, deliberately and explicitly, the invariant that must hold from the decision that may be guessed. In an iterative procedure the properties that need proof are usually soundness and progress; the per-step choice of *how* to advance is frequently free to be heuristic, and treating it as though it needed the same rigor is how tractable designs get talked out of existence. The inverse mistake is worse: leaving the invariant to intuition while polishing the step.

A programmer working this way asks of any loop, cache-eviction policy, scheduler, or incremental compiler: what must be true after every iteration regardless of the choice made, and what is merely a preference about which iteration to take next? Prove the first, measure the second. And when the ideal choice turns out to be intractable, look for the special case in which it becomes easy, because that case usually explains what the heuristic is approximating.

**Source:** [Counterexample-Guided Abstraction Refinement](../works/counterexample-guided-abstraction-refinement.md) — the refinement section, where finding the coarsest separating refinement is shown NP-hard, the hardness is traced to the states irrelevant to the failure, and a polynomial symbolic refinement algorithm is proved to give the unique coarsest answer when those states are absent and used as a heuristic otherwise.
