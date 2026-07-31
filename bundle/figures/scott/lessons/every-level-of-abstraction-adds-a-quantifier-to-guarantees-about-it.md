---
type: lesson
title: "Every level of abstraction adds a quantifier to any guarantee you want about it"
figure: scott
works: [data-types-as-lattices]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Every level of abstraction adds a quantifier to any guarantee you want about it

**Lesson:** Scott tracks the cost of one particular guarantee — that a thing always yields a proper answer rather than a degenerate one — as he climbs the ladder of function types. At the bottom, for plain integer data with the junk elements excluded, the condition is simple and lands in a class he can characterize by an equation. One level up, for functions from integers to integers, it is still manageable. One more level and it is not, and his explanation is a single sentence: to say a function is total is to say all its values are well behaved, so when the domain is itself a complicated space, the statement of totality inherits that complication. Each arrow adds a quantifier.

That is a rule of thumb worth having before you need it rather than discovering afterward. A guarantee about a value is a claim about one thing. A guarantee about a function is a claim about a whole family of behaviors. A guarantee about a higher-order construct is a claim about a family of guarantees, and it is not merely a larger claim of the same kind — each layer of quantification moves it strictly further from anything a finite observation could settle. The cost tracks the order of the object the claim is about, not the size of the system, which is why a small, elegant, highly abstract design can be much harder to make honest promises about than a large concrete one.

Two consequences follow. Arrange for the things you actually want to check to be low order — first-order data and first-order operations over it — and let the higher-order machinery be what constructs them rather than what you make promises about; a property is easiest to state exactly where the objects are dullest. And when you meet a strong-sounding guarantee about a higher-order construct — every callback behaves, every registered strategy terminates, every plugin preserves the invariant — count the layers in the sentence and ask how it could ever be established. Usually the claim is not false. Usually it was never the kind of claim anyone could confirm, and it has been doing the work of reassurance rather than of specification.

**Source:** [Data Types as Lattices](../works/data-types-as-lattices.md) — Section 7's discussion of the type of total integers and the successive function types built over it, where Scott classifies the low levels by the form of their defining conditions, notes that the higher type spaces become ever more complicated with each function arrow adding another quantifier to the definition, and gives as the reason that totality means all values are well behaved, so a complex domain makes the statement of totality more complex still.
