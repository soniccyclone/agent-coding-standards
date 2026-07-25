---
type: lesson
title: "State a property as the equation it solves, and the algorithm falls out"
figure: clarke
works: [design-and-synthesis-of-synchronization-skeletons-using-branching-time-temporal-logic, automatic-verification-of-finite-state-concurrent-systems-using-temporal-logic-specifications, model-checking-survey-clarke-grumberg-long, model-checking-algorithmic-verification-and-debugging]
axes: [expressiveness, verifiability, primitive-count]
subdomains: [formal-methods-and-verification, foundations-of-computation]
tags: [lesson]
---
# State a property as the equation it solves, and the algorithm falls out

**Lesson:** Every temporal property in this family has a recursive character: inevitability of some fact holds at a state exactly when the fact holds now or inevitability holds at every successor. Written that way, the property is a solution to an equation over sets of states, and because the underlying transformer is monotone, the lattice-theoretic fixpoint theorem hands you both the existence of the solution you want and the iteration that computes it. Start from the empty set and climb for the least fixpoint, start from everything and descend for the greatest. Eventualities are least fixpoints, because least fixpoints capture only the well-founded behaviours; invariants are greatest fixpoints.

The reason this is a way of thinking and not a piece of algorithm trivia is what it buys. The specification language stops needing one bespoke procedure per operator; it needs one iteration parameterized by a transformer, and every operator reduces to a choice of transformer and a starting point. The primitive count of the implementation collapses. In the earliest version, the same idea appears in operational clothing — satisfaction radiating outward from states where the property holds immediately, one layer per iteration, bounded by the length of the longest loop-free path — which is exactly the ascending chain of approximations seen from the inside.

The deeper payoff is representational independence. The fixpoint iteration never inspects individual states; it applies a set-to-set transformer and tests two sets for equality. So any data structure that can represent sets of states, take images under the transition relation, and decide equality can host the entire model checker unchanged. That is precisely the hinge on which symbolic model checking later turned. It is also the common foundation that makes model checking and abstract interpretation two dialects of one activity, both solving fixpoint equations in some semantic domain, a convergence the Turing lecture names as an unfinished opportunity.

A programmer who absorbs this looks for the recursive characterization of a computation before writing a loop, because the characterization tells you what you are computing, whether it terminates, which of several candidate answers you get, and — most valuably — what parts of the implementation are interchangeable. Code that grows directly out of the equation tends to be short, uniform across cases, and portable across representations. Code written case by case tends to be none of those.

**Source:** [Model Checking](../works/model-checking-survey-clarke-grumberg-long.md) gives the least- and greatest-fixpoint characterizations of the temporal operators together with the generic iteration procedures and then reuses them verbatim over a symbolic set representation; the Turing lecture's account of the original algorithm derives the same thing from the Tarski–Knaster theorem, and the 1981 paper's "radiating outward" argument for the until operator is the early operational form.
