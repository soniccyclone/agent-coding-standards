---
type: lesson
title: "A meaning you can state without a machine is a standard machines can be measured against; a meaning that needs one has nothing left to judge it"
figure: landin
works: [correspondence-algol-60-church-lambda-notation-part-i]
axes: [verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification, foundations-of-computation]
tags: [lesson]
---
# A meaning you can state without a machine is a standard machines can be measured against; a meaning that needs one has nothing left to judge it

**Lesson:** There are two very different situations you can be in when you say what a program means. In the first, meaning is fixed independently of any evaluator, so an evaluator becomes a candidate to be assessed: it either agrees with the independent account or it does not, and more than one evaluator can be correct. In the second, the only way you can say what a program means is to describe a particular apparatus running it. Meaning and mechanism have collapsed into one thing, and the notion of the apparatus being wrong has quietly evaporated — whatever it does is, by construction, what the program meant.

This distinction is not academic bookkeeping; it is a property you can lose by adding a feature. A calculus of application and abstraction alone admits an evaluator-free account of what expressions denote. Introduce assignment and a jump-like escape and that account stops being reachable: the meaning of an expression now involves how the surrounding state changes, which positions in that state are the same position, and in what order things touch them — and stating all of that turns out to be indistinguishable from describing a machine. The feature was added for expressive convenience, and the hidden charge on the bill was the independence of the specification from its implementation.

A programmer who takes this seriously treats "can I say what this means without reference to my runtime?" as a first-class design question rather than a philosophical one. It changes what you do with a reference implementation: where an independent account exists, the reference implementation is a suspect to be tested against the account, and disagreement is a bug in the implementation. Where no such account exists, the reference implementation *is* the specification, so its accidents become law, second implementations become archaeology of the first, and the only available notion of correctness is imitation. Recognising which regime a feature drops you into tells you what the feature actually cost, and warns you that the moment of loss is the moment to think hardest, because afterwards there is no vantage point outside the machine from which to notice anything is wrong.

**Source:** [A Correspondence Between ALGOL 60 and Church's Lambda-Notation: Part I](../works/correspondence-algol-60-church-lambda-notation-part-i.md) — the passage introducing the imperative extension of applicative expressions, where Landin contrasts the evaluator-independent account available for the purely applicative language with the apparent unavoidability of defining the imperative one by its executing machine.
