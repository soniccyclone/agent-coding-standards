---
type: lesson
title: "The interesting structure begins after you already know a thing is computable"
figure: hartmanis
works: [on-the-computational-complexity-of-algorithms]
axes: [hardware-affinity, verifiability]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# The interesting structure begins after you already know a thing is computable

**Lesson:** A yes/no verdict on whether something can be done in principle is nearly useless as design information, because it groups together tasks that a machine finishes before you look away and tasks no machine will finish before the sun burns out. The move that founded a discipline was to stop treating the computable things as one undifferentiated bag and instead index them by a resource budget: for each growth rate of allowed work, ask which problems fit inside it. What had looked flat turns out to be layered, and the layering is not an artifact of taste. It is forced, because the problems fitting any fixed budget can be listed mechanically, and anything you can list you can step outside of by constructing something that consults the list and disagrees with it everywhere. So there is no widest budget, no final class, and no ceiling: whatever resource envelope you name, something provably needs more.

The mechanism deserves attention on its own, because it recurs far outside complexity theory. Effective enumerability is a weakness, not a strength. Any collection of behaviors you can systematically catalogue, whether that is a rule set, a whitelist, a test suite, or a set of programs meeting a bound, admits a constructible member of the surrounding universe that defeats the whole catalogue at once. Completeness claims about listable collections are therefore not merely unproven; they are refutable by construction.

A programmer who internalizes this stops asking whether an approach works and starts asking at what growth rate it works, treats "it terminates" as the beginning of the analysis rather than the end of it, and expects every resource ceiling in the system to have something interesting sitting just above it. The stance also cures a specific bad habit: reaching for an exhaustive enumeration of cases as a completeness argument. If the cases can be enumerated, the enumeration is a target, and someone or something will eventually be built against it.

**Source:** [On the Computational Complexity of Algorithms](../works/on-the-computational-complexity-of-algorithms.md) — the framing in the introduction, which distinguishes easy from inherently hard computable sequences, and the opening results establishing that each time-bounded class is recursively enumerable and therefore strictly contained in a larger one, giving infinite ascending chains.
