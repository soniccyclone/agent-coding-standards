---
type: lesson
title: "Order independence is a property you purchase with restrictions, and convenience in the core can spend it"
figure: church
works: [the-calculi-of-lambda-conversion]
axes: [parallelizability, verifiability, expressiveness]
subdomains: [programming-languages-and-semantics, distributed-systems-and-concurrency]
tags: [lesson]
---
# Order independence is a property you purchase with restrictions, and convenience in the core can spend it

**Lesson:** Separate two relations that are easy to conflate. One is the equational relation: two expressions mean the same thing, and it runs in both directions. The other is the directed relation: this expression steps toward that one. Computation is the directed slice of an equational theory, and evaluation strategy is a question only about the directed slice. The results worth having say that the slice does not matter: if an expression has a fully evaluated form at all, that form is essentially unique, and every way of stepping toward it gets there in a bounded number of steps. When that holds, evaluation order is outside the meaning of the program. Independent subexpressions can be reduced in any interleaving, in parallel, or speculatively, because no schedule can lose an answer that another schedule would have found.

This property is bought, not given. In the version of the calculus where a binder is required to actually use the variable it binds, the strategy-independence theorems hold. Relax that one clause so you can write a function that ignores its argument, which is exactly what you need for a natural zero and for constant functions, and several of those theorems fail. Now a result can converge while a subterm it discarded never would, and evaluation order becomes semantically load-bearing. The fix that recovers the theorems is instructive: require that an argument be already fully evaluated before substituting it. That side condition is checkable by inspection, whereas the property you might have wished for, that the argument eventually terminates, is not checkable at all.

So the design space has three named points, and each is a different bargain among expressive comfort, order independence, and provability. A programmer who has internalized this stops arguing about eager and lazy evaluation as a matter of taste. The question becomes which theorems you want to keep, which core restriction pays for them, and whether the guard you propose is decidable. The same reasoning transfers directly to concurrency: independent work can be reordered freely exactly to the extent that the calculus of your effects is confluent, and every convenience you add to the core is a candidate for having quietly spent that freedom.

**Source:** [The Calculi of Lambda-Conversion](../works/the-calculi-of-lambda-conversion.md) — the fundamental theorems chapter establishing uniqueness of the fully reduced form and the bound on any reduction sequence, read against the later chapter that introduces the unrestricted variant, lists which of those theorems fail in it, and presents Bernays' restricted variant that recovers them by a normal-form side condition.
