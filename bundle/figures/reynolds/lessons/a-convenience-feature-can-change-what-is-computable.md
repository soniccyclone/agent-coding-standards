---
type: lesson
title: "A feature added for convenience can change what is computable, so measure its power instead of assuming"
figure: reynolds
works: [towards-a-theory-of-type-structure]
axes: [expressiveness, primitive-count, verifiability]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# A feature added for convenience can change what is computable, so measure its power instead of assuming

**Lesson:** The facility for abstracting over types was introduced to solve an engineering irritation: writing the same routine once per kind of data. Nothing in that motivation suggests any change to the set of functions the language can express — the routines being unified were all already writable, just repetitively. Yet the resulting language can express a function that grows faster than anything the underlying calculus could reach, one traditionally used as the standard example of a total function beyond a whole class of recursion schemes. The lesson is that the justification for a feature tells you nothing reliable about its strength. Convenience arguments and power arguments are independent, and a device whose whole purpose was to avoid retyping can turn out to enlarge the space of expressible computations.

That cuts both ways, and the second direction is the one that bites. The base calculus had a global structural property — every expression reduces to a finished form, so nothing runs forever — and that property was doing real work. Once the type-abstraction facility is present, whether the property survives is simply an open question the author cannot settle, and the newly expressible fast-growing function is exactly the kind of evidence that should make you nervous rather than pleased. So the discipline is: before adding a facility, write down the global properties you are currently relying on, and treat each one as something to be reestablished rather than inherited. The properties you rely on most are the ones you are least likely to remember you are relying on, because they have never been threatened before.

The practical upshot for anyone weighing a language or library extension is to run both measurements and keep them separate. Ask what the feature lets you *say* more briefly, which is the case that was made for it, and ask independently what it lets you *compute* and what invariants it costs, which nobody argued about because nobody expected an effect. A feature can be worth having on all three counts, but they have to be established separately; power that arrives unmeasured is power you cannot reason about, and an invariant that lapses silently is worse than one you deliberately gave up.

**Source:** [Towards a Theory of Type Structure](../works/towards-a-theory-of-type-structure.md) — the section on syntactic manipulations, which contrasts the normal-form property of the typed lambda calculus with the author's inability to resolve the question for the extended language, and exhibits interconvertible expressions from which Ackermann's function is obtained.
