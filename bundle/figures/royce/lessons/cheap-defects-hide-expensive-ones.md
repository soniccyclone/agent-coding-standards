---
type: lesson
title: "Match the detector to the defect class, cheapest first, because trivial errors hide serious ones"
figure: royce
works: [managing-the-development-of-large-software-systems]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Match the detector to the defect class, cheapest first, because trivial errors hide serious ones

**Lesson:** Royce's treatment of testing is really an argument about ordering, built on the observation that defects fall into classes with wildly different costs to find. Most errors, by count, are the crudely visible kind: a dropped sign, a missing factor, a branch to the wrong address. The cheapest detector for those is a second person reading the analysis and the code who did not write it. He is blunt about not spending machine time on what an eye catches. In 1970 the machine was the expensive resource and the human the cheap one, and that ratio has since inverted, but the structural claim survives the inversion intact: each class of defect has a detector that is best suited to it, and using an ill-matched detector wastes the expensive resource whichever one that currently is.

The reason the cheap sweep has to come first is not tidiness. A mass of small errors obscures the few large ones, so the expensive investigations return nothing useful until the noise floor has been cleared. Debugging a serious design fault while a hundred typos are still firing is not slower merely by the time the typos consume, it is systematically misleading, because every symptom has too many candidate causes. Ordering verification cheapest-detector-first is what makes the later, harder checks legible at all.

His acceptance criterion is worth noticing for the kind of thing it is. Every logic path exercised at least once against checked numbers, and he says he would refuse delivery without it, while conceding in the same breath that people will call this infeasible on a large program. That is not a proof of correctness and he does not pretend it is. It is a mechanical, structural criterion defined over the program's own branching, and its virtue is that whether you finished it is checkable by somebody other than you. Where proof is unavailable, a criterion whose completion can be audited beats a subjective judgment that testing was adequate.

The habit: sequence checks by the cost of their detector rather than by the severity of what they might find, treat independent reading as a distinct instrument rather than a weaker substitute for execution, and prefer acceptance conditions a second party can confirm you actually met.

**Source:** [Managing the Development of Large Software Systems](../works/managing-the-development-of-large-software-systems.md) — the "plan, control and monitor testing" corrective, with its ordering of second-party visual inspection before machine checkout, the point about simple errors obscuring big mistakes, and the every-logic-path delivery condition.
