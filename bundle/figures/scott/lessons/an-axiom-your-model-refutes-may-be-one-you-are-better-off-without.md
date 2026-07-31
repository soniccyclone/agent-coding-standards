---
type: lesson
title: "An axiom your model refutes may be one you are better off without"
figure: scott
works: [data-types-as-lattices]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# An axiom your model refutes may be one you are better off without

**Lesson:** Build a concrete model of a formal system and sooner or later one of the received laws comes out false in it. The reflex is to treat this as a defect of the model and start patching until the law holds. The better first move is to stop and read the law for what it actually asserts about the world you are modelling, because the model may be reporting a fact you wanted to know. Scott's model validates the core conversion rules but refutes a stronger extensionality principle, and rather than repairing anything he points out what that principle amounts to: the supposition that every object whatsoever is a function. In a formalism where nothing but functions exists, that supposition is invisible and free. In a domain built to hold integers, pairs, relations, functions and higher operators together, it is simply false, and a model that satisfied it would be one that had quietly collapsed the distinctions the whole construction exists to support.

The payoff of losing the law is concrete rather than consoling. Where the law holds, being a function is a triviality that distinguishes nothing; where it fails, being a function becomes a genuine property, so the functions form an identifiable part of the domain that you can name, test membership in, and use as a building block in further definitions. The same reversal applies far outside logic. A property every value in your system satisfies is a property you cannot branch on, cannot check, and cannot use to organize anything. Universality of a predicate and usefulness of a predicate pull against each other, and a law that fails on some inhabitants is what makes the predicate load-bearing.

The discipline this asks for is deliberateness, not tolerance of breakage. Scott is careful to note that models satisfying the stronger law are easy to construct if you want them, so the failure is a choice made with the alternative in hand rather than an obstacle he could not overcome. That is the standard to hold yourself to: when a principle fails in your setting, know what it would cost to make it hold, know what it would cost you to have it hold, and record which way you decided. A failure you can explain and could have avoided is a design decision; the same failure unexamined is a bug you have learned to live with.

**Source:** [Data Types as Lattices](../works/data-types-as-lattices.md) — the Introduction's discussion of Table 1, which reports that the first three principles of lambda conversion hold in the model while the stronger extensionality rule fails, argues this is not a disadvantage because that rule's import is to suppose every object is a function, and notes that models satisfying it can be constructed quickly; together with Section 2's identification of functions with their graphs and its definition of the subspace of those elements that are functions.
