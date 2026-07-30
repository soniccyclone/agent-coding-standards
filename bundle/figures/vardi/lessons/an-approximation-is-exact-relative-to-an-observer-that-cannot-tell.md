---
type: lesson
title: "A cheap test may replace an expensive one exactly when the language asking cannot tell them apart"
figure: vardi
works: [on-the-expressive-power-of-datalog]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# A cheap test may replace an expensive one exactly when the language asking cannot tell them apart

**Lesson:** Substituting a cheap approximate check for an expensive exact one is normally a compromise you apologize for. Sometimes it is not a compromise at all. If the property being decided is stated in a language whose observations cannot distinguish the exact condition from the cheap one, then on every case the language can pose, the two agree, and the substitution is not an approximation but an equality. Kolaitis and Vardi get a real result out of this: for a class of tasks whose answer amounts to "does one of these patterns embed here", they replace the expensive embedding test with the question of whether the survivor wins their indistinguishability game — which is decidable in polynomial time by exhaustive configuration search — and the replacement is sound precisely because the task was stated in a language the game characterizes. An intractable-looking task becomes tractable with no algorithm invented and no accuracy given up.

The general shape is worth naming carefully, because it is easy to get backwards. The licence to substitute does not come from the two tests being close in some numeric sense; it comes from a proof that no expressible query separates them. So the question to ask is never "how good is this approximation" but "what is the observation language, and can it see the difference." Change the observation language — add a construct, expose a new predicate, let a caller inspect an internal — and a substitution that was exact silently becomes wrong. This is why the boundary of an abstraction and the soundness of its optimizations are the same fact, and why widening an interface can invalidate optimizations that had nothing visibly to do with the new feature.

The everyday version is the argument that a refactoring, cache, memo, or representation change is safe. The honest form of that argument is not "it produces the same answers on the tests" but "here is the set of observations clients can make, and here is why none of them can distinguish the two." Written that way, the argument also tells you exactly which future interface change would break it — which is information you cannot get from a test suite.

**Source:** [On the Expressive Power of Datalog: Tools and a Case Study](../works/on-the-expressive-power-of-datalog.md) — section five's definition of pattern-based queries, the proposition that a structure satisfies such a query exactly when the survivor wins the pebble game against some generated pattern (justified by the game characterization of the logic rather than by any similarity between the two tests), the proposition establishing the game is decidable in polynomial time by bounding the number of configurations, and the resulting theorem that any pattern-based query expressible in the logic is polynomial-time answerable.
