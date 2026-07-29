---
type: lesson
title: "Judge a semantics by the equalities it lets you prove"
figure: strachey
works: [continuations-a-mathematical-semantics-for-handling-full-jumps]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Judge a semantics by the equalities it lets you prove

**Lesson:** The test of a definition of meaning is not that it can be written down for every construct in the language. That much is cheap; an interpreter does it. The test is whether the definition lets you show that two programs which look nothing alike are the same program. Once meaning is a mathematical object rather than a recipe, sameness becomes equality of objects, and equality is something you can compute your way to by substitution and rearrangement rather than argue about by inspecting execution traces.

The continuation account demonstrates this repeatedly and almost casually. A loop written with a conditional and a backward jump reduces, by grinding through the equations, to the identical object as the loop written with the language's own iteration construct. A jump followed by unreachable code reduces to the jump alone, for every environment, every continuation, every store — which is exactly the statement that the trailing code is dead, arrived at without any notion of reachability having been defined. That last point deserves attention: the redundancy fell out of the meaning rather than being detected by a separate analysis bolted on beside it.

This is where the practical payoff of a good abstraction lives, and it is why elegance and utility are not in tension. Provable equalities are the currency of every optimisation, every refactoring, and every claim that a rewritten module still does what the old one did. A formalism that cannot express "these two are the same" leaves you defending each such transformation by hand, forever. So when choosing between representations of anything — a state machine, a query plan, an effect system, a configuration language — the right question is not which one describes the domain most faithfully but which one makes the equations you actually want to prove fall out by calculation. Faithfulness with no algebra attached leaves you with a picture; the algebra is what lets you act.

**Source:** [Continuations: A Mathematical Semantics for Handling Full Jumps](../works/continuations-a-mathematical-semantics-for-handling-full-jumps.md) — the treatment of iteration, where a jump-based block is calculated to the same fixed point as the loop construct, and the short catalogue of program equivalences that follows it.
