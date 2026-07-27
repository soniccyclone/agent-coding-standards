---
type: lesson
title: "Before you rewrite freely, check that your notion of sameness survives every context your operators can put a term in"
figure: kleene
works: [representation-of-events-in-nerve-nets-and-finite-automata]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Before you rewrite freely, check that your notion of sameness survives every context your operators can put a term in

**Lesson:** Two descriptions can pick out exactly the same behaviour and still not be interchangeable. Kleene runs headlong into this and, instead of glossing it, stops and separates two relations. The coarse one is behavioural: two descriptions are the same when they accept precisely the same inputs — the relation you actually care about, since it is what an observer of the finished machine can see. The fine one is structural: two descriptions are the same when the underlying families of fixed-length input patterns they were assembled from coincide. He then exhibits a pair that are behaviourally identical but structurally different, and shows that substituting one for the other inside a larger description changes what that description accepts.

The reason is worth understanding because it generalizes far beyond his subject. Two of his three combinators do not consult only the *set* a subterm accepts; they consult how far back in time each accepted pattern reaches, because "this followed by that" has to know where one ends for the other to begin. Duration is structural information invisible to the behavioural relation. So the coarse equality is not preserved by those two operators, while it is preserved by the others — and he spells out exactly which substitutions are licensed under which relation, rather than leaving readers to assume that equals may replace equals. His algebraic laws are then stated over the relation that actually is a congruence, and he notes at the end that he is really axiomatizing expressions for behaviours, not behaviours.

The habit this teaches is to treat "these two things are the same" as a claim that must be checked against every context your language can build, not as a property of the two things alone. Whenever you define an equivalence — observational equality of two functions, two configs that produce the same deployment, two queries with the same result set, two objects that compare equal — the operative question is whether every operator in the surrounding language is blind to whatever the equivalence throws away. If some operator reads a field your equivalence ignores, that equivalence cannot be used as a rewriting rule inside it, and any refactoring that assumes otherwise is a latent bug that will surface only in the composing contexts.

There are two exits, and knowing both is the point. Refine the equivalence until it captures everything the operators can see, which is what Kleene does — accepting a finer, less intuitive relation as the price of being allowed to compute with it. Or restrict the operators so they can only observe the coarse data, which in his terms would mean combinators that never consult duration. The wrong move, and the tempting one, is to keep the intuitive equality and the peeking operators and hope the two never meet, because that hope holds right up until someone rewrites a subterm inside a composition.

**Source:** [Representation of Events in Nerve Nets and Finite Automata](../works/representation-of-events-in-nerve-nets-and-finite-automata.md) — the section distinguishing identity from equivalence in Part I, which gives the counterexample pair, identifies subterm duration as the structural information the concatenation and iteration operators depend on, and enumerates which inferences hold under each relation before the algebraic laws are used in the main construction.
