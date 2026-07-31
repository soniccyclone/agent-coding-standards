---
type: lesson
title: "Split cases at the point the branch appears, and expand whichever term occurs least"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [cognitive-load, verifiability]
subdomains: [formal-methods-and-verification, algorithms-and-complexity]
tags: [lesson]
---
# Split cases at the point the branch appears, and expand whichever term occurs least

**Lesson:** Working through any argument about a piece of code — a proof, a review, a debugging session, a mental simulation — you are repeatedly choosing what to unfold next, and those choices decide whether the thing stays tractable or explodes. Two heuristics do most of the work, and both are about controlling size rather than about being clever.

The first: when a branch shows up, split into cases immediately, before doing anything else with the surrounding expression. The alternative is to keep the branch as a value and carry it forward, and that is fatal, because every subsequent unfolding duplicates it. A conditional dragged three substitutions deep has been copied into every place its result is used, and now each copy needs its own case analysis, which is the same analysis you declined to do once at the top. Splitting early costs you two smaller problems. Splitting late costs you two large ones, several times over. The general form is that a case distinction is cheapest exactly where it is introduced, and grows more expensive with every step you postpone it past.

The second: when you can unfold more than one thing, unfold whichever occurs fewest times. Substituting a definition that appears once leaves the argument the same size; substituting one that appears four times quadruples that part of it. This sounds like bookkeeping and it is, but it is the difference between an argument a person can read and one nobody will check. Notice too that the order of independent unfoldings never changes the outcome — each step replaces something with an equivalent, so nothing about correctness depends on the sequence. Order is purely about how large the intermediate forms get, which is another way of saying that being strategic about it is free.

Both heuristics point at the same underlying discipline: reasoning about code fails from volume far more often than from difficulty, so the skill worth developing is the one that keeps the working expression small at every step, not the one that finds the ingenious step.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 3's "Conditional Functions" section, in the worked treatment of a maximum function and a sign function: the choice to substitute the realization rather than the post-condition because the result term occurs four times in the latter; the observation that substituting into the post-condition at that point would create an unwieldy expression; and the closing recommendation that case distinctions be made as soon as conditional expressions appear after substitution, since proliferating a conditional by substituting it further is likely to generate unnecessarily long expressions. The remark in the preceding section that the order of substitutions is unimportant, each merely changing an expression into an equivalent one, supplies the reason order can be chosen freely on grounds of size alone.
