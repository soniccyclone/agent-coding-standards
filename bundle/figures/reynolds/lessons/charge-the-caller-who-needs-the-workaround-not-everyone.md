---
type: lesson
title: "Do not make everyone pay for a safety measure that only one kind of caller needs"
figure: reynolds
works: [the-craft-of-programming]
axes: [hardware-affinity, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Do not make everyone pay for a safety measure that only one kind of caller needs

**Lesson:** A component that misbehaves when two of its arguments happen to be the same object presents you with a fork. You can defend inside — copy the input into private storage, work on the copy, write the result back at the end — and then no caller can break it. Or you can leave the component as it is, say precisely which combinations of arguments are illegitimate, and let the callers who actually have that combination arrange their own copy. The defensive version looks strictly better because it removes a way to be wrong. It is usually the worse choice, because it charges every caller for a hazard that only some callers can even encounter, and it charges them in the one currency the component was supposed to be honest about: the space and time it consumes.

The asymmetry that decides it is informational. At the call site, whether the two arguments alias is a known fact; inside the component it is an unknown that must be defended against unconditionally. The caller can also pick the cheapest repair available in its own situation — sometimes a copy, but often a different decomposition that avoids the collision entirely. Absorbing the defense into the component throws all of that away and replaces it with the worst-case fix applied everywhere. The same reasoning explains why a language might deliberately refuse to offer an implicit copying mode for large aggregates: adding it would smuggle an unbounded operation into a construct that otherwise costs nothing, and would hide it in exactly the place a reader is least likely to look for it.

The obligation this creates is real and it is not "add a comment." Leaving the hazard to the caller only works if the restriction is stated as sharply as the rest of the interface — which arguments must be distinct from which, in a fixed notation, in a fixed position — so that a reader can check compliance without reading the body. A component that quietly assumes non-overlap and does not say so has taken the cheap path without doing the work that justifies it, and is simply a trap. The rule is: keep the fast version, publish the constraint, and let the exceptional caller pay for being exceptional.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 3.1.6 on array parameters, which explains the omission of call by value and result for arrays as avoiding implicit array assignment in a language with no explicit array assignment and as keeping space and time requirements from being obscured, then works the merging procedure whose output may alias either input, shows the defensive rewrite with a local copy, and argues that this imposes the penalty on all usages to accommodate one kind of usage where the more flexible approach is to retain the original, state its limitations clearly, and leave circumvention to its users.
