---
type: lesson
title: "\"Can it happen?\" and \"must it always hold?\" need approximations that err in opposite directions"
figure: sifakis
works: [property-preserving-abstractions-1995]
axes: [verifiability, expressiveness]
subdomains: [formal-methods-and-verification, algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# "Can it happen?" and "must it always hold?" need approximations that err in opposite directions

**Lesson:** A coarsened model built by collapsing groups of concrete states into single abstract states has a choice to make about transitions, and the choice is not a detail. If you draw an abstract transition whenever *some* member of the source group can take it, the coarse model admits every concrete behavior and possibly more. Claims of the form "along every execution, this holds" then transfer downward safely, because the coarse model has strictly more executions to violate them. But claims of the form "there is an execution reaching this" do not transfer at all, since the witness path you found may be stitched together from steps no single concrete state could actually chain. To get those, you must draw an abstract transition only when *every* member of the group can take it — which yields a model admitting fewer behaviors, on which found paths are real and absent paths prove nothing.

So the two families of question want approximations pointing opposite ways, and one collapsed model cannot serve both. Sifakis and co-authors are explicit that the abstraction construction they develop supports the universal fragment of the logic and that reachability questions require an abstract system built by a different rule. The consequence for practice is that "we made a simplified model of the system" is an incomplete statement: the simplification is only meaningful relative to a direction of inference, and a model that answered one kind of question correctly last month can silently produce nonsense the first time somebody asks the mirror-image question of it.

The general shape is worth carrying beyond verification. Any conservative analysis — a type system, an alias analysis, a cost model, a capacity plan — is an approximation with a direction, and the direction is set by which errors you were willing to make. Over-approximating what can happen is the right posture when you are trying to rule things out; under-approximating it is the right posture when you are trying to demonstrate something is achievable. When a tool starts being used for the second kind of question after being built for the first, the answers become unsound without anything visibly breaking. Make the direction an explicit, stated property of every approximation you build, and treat a request that runs against it as a request for a different artifact rather than a new query.

**Source:** [Property Preserving Abstractions for the Verification of Concurrent Systems](../works/property-preserving-abstractions-1995.md) — section 10's discussion of why reachability properties, the interesting ones for the existential fragment of the mu-calculus, do not hold on abstract systems built the way the paper's abstraction is built, and its description of the alternative construction that admits only abstract transitions available to every concrete state of the group.
