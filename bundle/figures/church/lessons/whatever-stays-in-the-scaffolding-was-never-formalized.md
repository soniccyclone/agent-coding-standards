---
type: lesson
title: "Whatever stays in the scaffolding was never really formalized, and the finished thing must stand without it"
figure: church
works: [introduction-to-mathematical-logic]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Whatever stays in the scaffolding was never really formalized, and the finished thing must stand without it

Setting up a precise language requires an imprecise one to set it up in, and Church is careful about the status of that borrowed language. He describes it as a deliberately small fragment of English — enough to give directions for manipulating physical marks, with no bound on how many marks or how long the manipulation takes, and specifically excluding the parts of English needed to discuss infinite collections and other abstract objects. That fragment is chosen to be so elementary that doubting its reliability would amount to doubting whether mathematics is possible at all. It is scaffolding selected for trustworthiness, not for power.

Two obligations follow, and he states both. First, derivations in the constructed system must proceed only by its own rules, with no appeal to any interpretation, however obvious the interpretation makes a step seem. Second, and more pointed: whatever part of an argument remains in the informal outer language is a part whose logical analysis is incomplete. He explicitly refuses to let a derivation carry annotations in the metalanguage explaining which rule justified which step, on the ground that anything doing real work outside the object language has not been formalized. Once the language is set up, it has to be capable of expressing on its own what it was designed to express, without continued support from the language used to introduce it.

The payoff for that severity is generality. A derivation that never touched meaning holds under every interpretation the system admits, so one derivation discharges the same argument across all of its readings, and proofs alike in form but different in subject matter need never be repeated. Independence from the scaffolding is exactly what buys reuse across models: the more a result leans on one intended reading, the fewer situations it covers.

A programmer meets this as the question of what remains load-bearing after the build. A generator whose output cannot be understood or modified without rerunning the generator, a service whose correctness argument lives in a design document rather than in its types and tests, a schema whose real constraints exist only in the validator someone wrote by hand, a deployment that works only because of undocumented knowledge in the operator's head — each is content left in the metalanguage. The test to apply is whether the artifact still means what you think it means when the person and process that produced it are gone. And when a component's justification appeals to what the caller presumably intends, that component is not verified; it is annotated.

**Source:** [Introduction to Mathematical Logic](../works/introduction-to-mathematical-logic.md) — the section on the logistic method, which characterizes the restricted metalanguage used to lay down a primitive basis, demands that proofs proceed without reference to any interpretation, rejects informal annotation as part of a proof, and draws out the resulting economy of one derivation holding under all interpretations.
