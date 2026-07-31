---
type: lesson
title: "An invariant is a promise at the boundaries, not a claim about every instant"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [verifiability, expressiveness, parallelizability]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [lesson]
---
# An invariant is a promise at the boundaries, not a claim about every instant

**Lesson:** A constraint attached to a data type is discharged by showing that each operation, started from a state satisfying it, finishes in a state satisfying it. That phrasing is doing more work than it looks. It says nothing whatever about the middle of an operation, and it is deliberate that it does not: an update that has to move an item out of one collection and into another will, between those two steps, have the item in both or in neither, and the constraint will be plainly false. Forbidding that would mean requiring every state change to be structurally atomic, which for anything larger than a single field is not achievable. So the constraint is a boundary condition on a set of entry and exit points, and the interior is deliberately left unconstrained.

The consequence worth carrying around is that the strength of the guarantee is fixed by who is allowed to look, not by what the code does. As long as the only way to reach the representation is through the named operations, the window during which the constraint is false is invisible, and reasoning may treat it as though it always held. The moment something else acquires a way to observe the state in that window — another thread, a callback invoked from inside the update, an error unwinding out of the middle, a debugger or a persistence layer walking the structure — the property being relied on simply is not there. Nothing about the operations changed; the boundary moved. This is why "does this hold?" is the wrong question to ask about an invariant and "who can be looking, and when?" is the right one.

That reframing also tells you where to spend effort when you want a stronger guarantee. You do not get it by making the constraint more elaborate or by re-checking it more often. You get it by shrinking the set of parties with access, or by shrinking the interval in which the constraint is false — pushing the two steps together, or restructuring so the update is one step against the structure that carries the constraint. Both are changes to the boundary, not to the predicate. And the diagnostic value runs the other way too: if you find yourself unable to state a window in which a constraint may be broken, you have either an operation set that is too fine-grained to be the real interface, or a constraint that is not about the type at all.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 10's statement of the general obligation for data type invariants, which requires only that a valid state and a satisfied pre-condition yield a valid state after the operation, together with the paragraph immediately following the worked proofs for the students-who-complete-exercises problem, which observes that the invariant is proved to hold at the end of each operation but that during an operation the predicate may fail to hold, illustrated by an update performed in two steps whose first step causes the two sets to overlap before the overlap is removed prior to termination.
