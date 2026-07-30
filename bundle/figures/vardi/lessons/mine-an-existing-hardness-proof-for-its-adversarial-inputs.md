---
type: lesson
title: "Mine an existing hardness proof for its adversarial inputs, not just its conclusion"
figure: vardi
works: [on-the-expressive-power-of-datalog]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Mine an existing hardness proof for its adversarial inputs, not just its conclusion

**Lesson:** The hard part of any argument that something is indistinguishable, unreachable, or impossible is finding the specific inputs on which to make the argument. Kolaitis and Vardi name this openly as the main difficulty of their proof technique, and their answer is that somebody has already built the inputs. A reduction proving a problem computationally hard is, underneath the theorem, a machine that manufactures instances designed to be maximally confusing about exactly the property in question. That machinery is reusable for an entirely different kind of hardness. They take the construction from a known intractability proof, run it on a deliberately chosen family of unsatisfiable inputs, and play their indistinguishability game on the graphs it produces.

The payoff is worth generalizing well beyond logic. A proof is usually read as an assertion — the theorem — and discarded once believed. But a constructive proof also contains an *artifact generator*, and generators of pathological cases are the scarcest resource in testing, benchmarking, and any argument about limits. Existing reduction constructions, known counterexample families, the witnesses attached to old bug reports, the inputs that broke a previous implementation: all of these are stockpiles of adversarial structure that took someone real effort to design and that you get for free.

There is a matching-the-budget subtlety that makes the reuse work. The instances are not chosen arbitrarily; the family is indexed so that the amount of confusion available scales with the adversary's budget. For each probe budget they pick the input on which a budget that size can be fooled while a slightly larger one could not. Reusing someone's construction is therefore not just running their code — it is parameterizing their construction against your resource bound, so that each level of your adversary's power meets an instance calibrated to defeat it. When you inherit a pathological input family, look for the knob that scales with whatever budget you are arguing against, and turn it.

**Source:** [On the Expressive Power of Datalog: Tools and a Case Study](../works/on-the-expressive-power-of-datalog.md) — section six's negative results: the stated intention to convert a complexity lower-bound proof into an expressibility lower-bound proof, the detailed re-presentation of the earlier satisfiability reduction with its switch gadget, the choice of the complete unsatisfiable formula on k variables as the instance for probe budget k together with the observation that the prober wins with one more pebble than variables, and the pair of structures extracted from that reduction on which the game is then played.
