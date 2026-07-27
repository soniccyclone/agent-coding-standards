---
type: lesson
title: "Find the smallest set of facts only a human could have supplied, and treat everything downstream of them as machine work"
figure: floyd
works: [assigning-meanings-to-programs]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Find the smallest set of facts only a human could have supplied, and treat everything downstream of them as machine work

**Lesson:** When a reasoning discipline looks expensive, the useful question is not "how do we make people do more of it?" but "how much of it is actually irreducible?" For assertion-based reasoning about programs the answer is sharp and surprisingly small. Given what holds before an operation, the strongest thing that necessarily holds after it can be computed from the operation itself, mechanically, with no insight required. So annotations propagate forward on their own along straight-line code and through branches, and the only places where propagation cannot get started are the entry point and the cycles, because a cycle has no beginning to propagate from. Cut every loop with one supplied claim and the rest of the annotation is derivable.

That observation reorganizes the entire activity. The programmer's obligation shrinks to stating the entry conditions and one invariant per innermost loop, which is precisely the creative content of the argument: the part that encodes why the algorithm works. Everything else, the accumulation of consequences and the discharging of the local checks, is a mechanical procedure and therefore a candidate for automation. Knowing where the boundary falls is what makes tool-building possible at all, and it is also what makes the discipline teachable, because it tells a person exactly what they are on the hook for.

There is a further benefit to computing strongest consequences rather than merely checking supplied ones. The strongest consequence of a fragment is a canonical summary of its effect, so two fragments that produce the same one are interchangeable no matter how different their text. This gives a criterion for equivalence that does not depend on inspecting behavior: reorderings, rewrites, and optimizations are justified by showing their summaries coincide. A programmer thinking this way treats refactoring as a claim to be established rather than a change to be tested, and treats the propagation itself as the compiler's job, not theirs.

**Source:** [Assigning Meanings to Programs](../works/assigning-meanings-to-programs.md) — the discussion of the strongest verifiable consequent, its distribution over conjunction, disjunction, and quantification, the resulting observation that a programmer need only tag entrances and one edge per innermost loop for a verifier to complete the interpretation, and the worked demonstration that three differently written assignment sequences share one verification condition.
