---
type: lesson
title: "Grant the system unlimited patience and no cleverness, to find out which of its limits are real"
figure: turing
works: [systems-of-logic-based-on-ordinals]
axes: [verifiability, cognitive-load, parallelizability]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# Grant the system unlimited patience and no cleverness, to find out which of its limits are real

**Lesson:** Two very different things get called "we can't do that." One is that no amount of work would suffice: the capability is absent in principle. The other is that the work required is prohibitive: the capability is there but the search for it is expensive, and finding it quickly takes skill. Mixing these up is the most common way that architectural discussions go nowhere, because the fix for one is to change the design and the fix for the other is to spend more resources or get better at searching. The clean way to separate them is a thought experiment: strip the clever part out of the system entirely, replace it with exhaustive mechanical enumeration, hand it unlimited time, and see what remains out of reach.

What survives that experiment is a structural limit and tells you something about the design. What dissolves was never a limit on the system, only on the effort or the ingenuity applied to it — real constraints, but constraints of a different kind, to be attacked with different tools and reasoned about separately. Deliberately assuming away the resource dimension is what makes the structural dimension visible; keeping both in play at once produces arguments in which every claim about capability is contaminated by an unstated assumption about budget. The same move works in reverse: once you know the structural limits, you can safely fix them in place and reason purely about cost, knowing you are no longer confusing the two.

The practical form is to ask, of any system you are designing, what would still be impossible with infinite compute and an exhaustive search. Those answers are the architecture. Everything else is scheduling, heuristics, and budget, and should be discussed under those headings — where estimates, caching, and better search strategies are the appropriate moves. Making this separation an explicit step also protects against its opposite failure: declaring something impossible when it is merely slow, and rebuilding a system that only needed more patience.

**Source:** [Systems of Logic Based on Ordinals](../works/systems-of-logic-based-on-ordinals.md) — the section on the purpose of these constructions, which distinguishes two faculties in mathematical work and then deliberately assumes one of them in unlimited supply so that the other can be studied on its own, noting that under that assumption skill in finding proofs reduces to willingness to enumerate them.
