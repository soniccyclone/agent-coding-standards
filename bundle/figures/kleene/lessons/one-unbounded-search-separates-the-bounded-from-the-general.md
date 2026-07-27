---
type: lesson
title: "Exactly one capability separates the always-terminating from the fully general: search with no bound on how long it runs"
figure: kleene
works: [general-recursive-functions-of-natural-numbers]
axes: [primitive-count, expressiveness, verifiability]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Exactly one capability separates the always-terminating from the fully general: search with no bound on how long it runs

**Lesson:** Start with a computing vocabulary in which every construct is guaranteed to finish: build functions by plugging functions into each other, and by stepping a counter with each step's result available to the next. Everything in that vocabulary halts on every input, by construction, and its resource use is bounded by a function you can also write in the vocabulary. Then ask what the whole open-ended class of step-by-step-computable functions adds over it. The answer is one operator and nothing else: scan the numbers upward until you hit one satisfying a decidable test, with no prior bound on how far you must go. Every generally computable function can be written as a guaranteed-terminating function applied to the result of exactly one such search over a guaranteed-terminating test. Not a search inside a search inside a loop — one, at one place, on the outside.

That collapse is the payoff of taking primitive count seriously. It says the intuitive picture of "computation" as an open-ended zoo of recursion schemes, mutual definitions, simultaneous recursions, and clever tricks is an illusion of presentation. Structurally there are two ingredients: a bounded, totally predictable core, and a single unbounded search wrapped around it. Any implementation strategy or proof that handles those two cases handles all computation. Nested and iterated searches over arbitrary computable tests buy nothing beyond the single outermost one, so the apparent expressive richness of stacking them is zero.

The design consequence is that termination is not spread diffusely through a program; it is localized. Every partial function is a total function composed with a place where you gave up on a bound. A programmer who has internalized this treats unbounded iteration as the single scarce resource in a language and accounts for it explicitly — because everything else costs nothing in verifiability. It also explains why languages that forbid unbounded search (total languages, terminating type theories, bounded loops in critical code) lose exactly the functions whose running time outgrows any bound they could state, and no others. And it reframes what "more expressive" means: the honest question about a new construct is not what it lets you write but whether it lets you write anything that a bounded core plus one search cannot.

**Source:** [General Recursive Functions of Natural Numbers](../works/general-recursive-functions-of-natural-numbers.md) — the normal-form result in §1 reducing every function of the general class to a bounded-construction function applied to a single minimization over a bounded-construction relation, together with the converse showing that adding that one operator to the bounded core stays inside the class, and the accompanying remark that repeating the operator over general rather than bounded tests gains nothing.
