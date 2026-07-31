---
type: lesson
title: "Peel away what violates your method's precondition, solve, then rebuild in reverse order"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Peel away what violates your method's precondition, solve, then rebuild in reverse order

**Lesson:** When a technique requires a structural property the real input lacks, there are two honest responses and one dishonest one. The dishonest one is to run it anyway and hope the violation is rare. The two honest ones are to weaken the technique so it tolerates the violation, or to strip the offending part of the input, solve the clean remainder, and then extend the answer back out to what was stripped. The second is often much cheaper than it looks, and it is underused because people think of preprocessing as data cleaning — throwing away inconvenient records — when here nothing is discarded, only deferred.

The pattern has a shape worth memorising. Removal is applied to a fixed point, not once: excising the offending elements can turn previously-fine elements into new offenders, so you iterate until nothing more qualifies. What remains satisfies the precondition by construction, which is the whole point — you are no longer arguing that the assumption approximately holds, you have manufactured a subproblem where it exactly holds. Then, crucially, the removals happened in a definite order, and reversing that order is exactly the order in which the removed elements' answers become computable, because each one depends only on things removed later or never removed at all. The deletion sequence is not scaffolding to be thrown away; it is the schedule for the reconstruction phase.

This reframes a common architectural instinct. The usual move when input violates an invariant is to generalise the algorithm — add cases, add fallbacks, add a tuning parameter that softens the assumption. That grows the core, and the added cases are the ones least exercised and most likely wrong. The peel-and-rebuild alternative keeps the core narrow and pushes the messy part into a separate, simpler pass that is often nothing more than a fold over a dependency order. Two small components with clean contracts beat one component with a special case, and the invariant stated as a precondition can actually be checked, whereas an invariant that was softened into a parameter can only be tuned.

Knowing when it does not apply is part of the lesson. Peeling works when the violating elements form a set you can identify locally and whose answers depend one-directionally on the retained core. When the violation is entangled — when the offending elements' values depend on each other cyclically, or on parts of the core that in turn depend on them — there is no reconstruction order and you genuinely do need the weakened method instead. Checking which situation you are in is a question about the dependency structure, answerable before implementation, and it decides which of the two honest responses you owe the problem.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the link-analysis chapter's treatment of dead-end nodes, where the iterative method's convergence assumption fails, and the recursive-deletion remedy that solves the residual strongly connected portion first and then assigns values to the deleted nodes in the reverse of their deletion order.
