---
type: lesson
title: "In a recursive program you need two tiers of invariant, and which tier one belongs to is read off the names it mentions"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# In a recursive program you need two tiers of invariant, and which tier one belongs to is read off the names it mentions

**Lesson:** A recursive procedure has more than one thing that stays true, and the kinds are genuinely different. Some properties hold of the whole system at every instant, no matter which activation is currently running or how deep the nesting goes — relationships among the shared variables that every level maintains and every level relies on. Others are true only within a single activation, relating what that activation found on entry to what it has done since. Conflating the two produces the standard confusion of recursive reasoning: an assertion that is obviously true, but that you cannot use, because you cannot tell whether an inner call is entitled to disturb it.

The criterion for sorting them is syntactic and completely reliable: look at which names the assertion mentions. An assertion phrased entirely in globals belongs to the whole computation and must be re-established before every call and after every return, at every depth simultaneously. An assertion that mentions a local variable, or a ghost parameter standing for the state at entry, cannot even be *stated* outside one activation — the names have no referent there — and therefore describes exactly one level. Placement follows: the global one is declared outside the block that declares the procedure, the per-activation one inside its body. This is not bookkeeping; it is the same thing as scope, applied to facts rather than to storage.

The reason to insist on the discipline is that the two tiers are used differently in a proof, and the hard steps need both. When you assume a specification for the recursive call in order to prove the body, you are using the global tier to know what state the callee inherits and the per-activation tier to know what your own frame still guarantees afterwards. A per-activation invariant is the only vehicle for saying "whatever the callee did, it did not touch what I set aside", and a global invariant is the only vehicle for saying "the callee found the world in the condition it requires". Neither substitutes for the other, and a program with only one of them written down will have its hardest step justified by hand-waving.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 5.4.2, which declares the general invariant relating the output collection, the classified nodes and the unclassified set before the block declaring the search procedure, so that it holds throughout execution at all recursive levels, and separately introduces an invariant inside the procedure body relating the saved entry value of the unclassified set to its current value; Reynolds notes explicitly that the latter is a local invariant because it mentions a local variable and the ghost parameters standing for the entry state, and therefore describes a particular level of recursion, in contrast to the global assertion which holds for all levels.
