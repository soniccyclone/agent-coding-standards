---
type: lesson
title: "When the comparison you need is out of reach, grade it into weaker ones you can actually make"
figure: post
works: [recursively-enumerable-sets-of-positive-integers-and-their-decision-problems]
axes: [expressiveness, verifiability, primitive-count]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# When the comparison you need is out of reach, grade it into weaker ones you can actually make

The question driving Post's survey is whether two hard problems are hard in the *same* way, and he cannot answer it. What he does instead is build a graded family of ways one problem may lean on another, from the crudest — translate each question into exactly one question about the other problem and copy the answer — up through translations allowed to ask several questions and combine the answers by a fixed rule, then to that same freedom with no bound on how many questions, and finally to the fully general form where each question you ask may depend on the answers you have already received. Each rung is a genuinely different instrument, and results proved with one rung say nothing automatically about another. Against this ladder he can prove real separations: certain structurally thin problems provably do not support a translation of the hardest problem when the rule combining answers is bounded in size.

The reason the ladder is worth building rather than a consolation prize is that a graded family converts an unanswerable yes/no into a map. You learn which structural features of an object are responsible for which kind of hardness, because each rung fails for a different reason. And the rungs are cheap to define compared to answering the top question, so the ratio of insight to effort is excellent. The strong version of the question stays open; the ladder tells you where to look for its answer and, just as usefully, which candidate answers are already dead.

The discipline that makes this honest is the one Post applies to himself immediately after his own separation result. Having shown the thin sets escape reduction under the bounded instrument, he goes and *constructs the counterexample that ruins it* — a set of the same thin kind that the hardest problem does reduce to once the size bound on the combining rule is lifted. The separation was real, and it was also an artifact of the restriction. He does the same thing again at the end to kill a strengthening of his own definitions that he had just proposed. A distinction that appears only under a weakened instrument is not yet a distinction between the objects; it may be a fact about the instrument, and the only way to find out is to attack it with a stronger one yourself.

For a programmer this is the difference between a benchmark suite and a belief. When you cannot settle whether two designs really differ, define several concrete, weaker senses in which one could stand in for the other — same interface, same interface plus latency envelope, same behavior under a restricted query shape, full behavioral substitutability — and report per sense. Then, before you publish the difference you found, spend your next hour trying to make it vanish by loosening exactly the restriction that produced it. If the difference survives your own best attack, it is probably about the systems. If it evaporates, you learned about your measurement, which is worth knowing before someone else learns it for you.

**Source:** [Recursively Enumerable Sets of Positive Integers and Their Decision Problems](../works/recursively-enumerable-sets-of-positive-integers-and-their-decision-problems.md) — the sequence of sections defining progressively more permissive notions of reducibility, the non-reducibility theorem proved under the bounded notion, and the immediately following counterexample section that limits it.
