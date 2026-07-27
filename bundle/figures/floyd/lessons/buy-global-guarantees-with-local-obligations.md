---
type: lesson
title: "Trade one unmanageable whole-program argument for many tiny local ones, and let induction assemble the result"
figure: floyd
works: [assigning-meanings-to-programs]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Trade one unmanageable whole-program argument for many tiny local ones, and let induction assemble the result

**Lesson:** A claim about a program's finished output is a claim about an execution of unbounded length, and reasoning about it directly means reasoning about every path the program can take. The escape is to stop reasoning about executions at all. Decorate each point where control can pass with a claim that must hold whenever control passes there, then check, separately for each individual operation, only this: if the claim on the way in was true, the claim on the way out will be too. Nothing in that check mentions how control arrived, how many times it has looped, or what happens afterwards. Once every operation passes its own check, induction on the number of steps taken hands you the whole-program property for free.

What makes this more than a bookkeeping trick is what it does to the size of the thing you must hold in your head. The verification burden becomes proportional to the number of operations rather than to the number of paths, which is the difference between linear and exponential. It also becomes composable in the way engineering requires: two independent proofs about the same program combine by conjoining the claims edge by edge, and a case analysis over ranges of inputs combines by disjoining them, so partial results accumulate rather than needing to be redone. Strengthening what you assume on entry or weakening what you promise on exit can never invalidate a check that already passed, which means local reasoning stays local under revision.

The practical consequence for a programmer is that the interesting design work moves to choosing where the claims go and what they say. The claims at loop entry carry all the weight, because they are the ones that must be simultaneously strong enough to imply the final result and weak enough to survive an arbitrary number of iterations. Everything else is derivable. Someone who has internalized this writes loops by first asking what stays true across them, and treats a program whose invariants cannot be stated compactly as a program whose structure is wrong, not as a program that merely needs more testing.

**Source:** [Assigning Meanings to Programs](../works/assigning-meanings-to-programs.md) — the construction of per-command verification conditions over an assertion-tagged flowchart, and the general axioms showing that separate verified interpretations combine by conjunction, disjunction, quantification, and strengthening or weakening of the endpoints.
