---
type: lesson
title: "Turn a question about what can be said into a game about what an adversary can distinguish"
figure: vardi
works: [on-the-expressive-power-of-datalog]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# Turn a question about what can be said into a game about what an adversary can distinguish

**Lesson:** "Is there any expression in this language that separates these two situations" is a question about an infinite space of texts, and searching that space is hopeless. The productive reformulation replaces it with a two-party contest: one side tries to expose a difference by probing a bounded number of positions at a time, the other tries to answer every probe consistently forever. If the answerer can survive indefinitely, no expression in the language separates the two situations. Humans are far better at constructing and reasoning about strategies than at reasoning about the non-existence of texts, so the reformulation converts an unattackable problem into a tractable one — and the bounded number of probes corresponds exactly to the bounded number of names the language may hold at once, which is why the correspondence is tight rather than merely suggestive.

Two properties make this a tool rather than a trick. First, the correspondence goes both ways: expressibility in the language is *equivalent* to the prober having a winning strategy, so failing to find a separating strategy is not merely inconclusive — if the thing were expressible, a strategy would have to exist. A proof method that is complete in this sense lets you interpret failure as evidence, which one-directional methods never do. Second, the relation the game characterizes is deliberately not an equivalence. Because the language is positive and existential, everything it can say is preserved in one direction only, so the right structural relation is a preorder, and the game is asymmetric: the answerer can survive copying moves from a short configuration into a longer one while the reverse collapses quickly. Reaching for symmetry here would have destroyed the correspondence.

The generalizable habit: whenever you need to know whether some observer can tell two things apart, stop enumerating observations and define the game that the observer plays. Then ask what budget the observer has — how many things it may inspect simultaneously, how many rounds it gets, whether it may revisit. That budget is the real parameter, and the strategy that defeats it is the proof. This is the shape of bisimulation and simulation arguments, of indistinguishability in security proofs, and of every argument that a refactoring is unobservable.

**Source:** [On the Expressive Power of Datalog: Tools and a Case Study](../works/on-the-expressive-power-of-datalog.md) — section four's definition of the existential k-pebble game and of the one-directional preservation relation between structures, the theorem establishing their equivalence in both directions, the resulting characterization of definability with a fixed number of variables and the accompanying remark that the method is complete, and the two worked examples showing the relation is reflexive and transitive but not symmetric.
