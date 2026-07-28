---
type: lesson
title: "A claim that your model captures reality is a hypothesis, not a definition"
figure: post
works: [finite-combinatory-processes-formulation-1]
axes: [verifiability, expressiveness]
subdomains: [foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# A claim that your model captures reality is a hypothesis, not a definition

There are two very different things a formalism can be doing, and they are easy to confuse because they look identical on the page. It can be *stipulating* a meaning — declaring that from here on, a word denotes exactly this construction, in which case nothing can ever contradict it. Or it can be *asserting* that this construction exhausts some phenomenon out in the world that existed before the formalism did, in which case the assertion could be wrong and every new attempt to exceed it is a test. Post insists on the second reading for the identification of mechanical computability with his primitive vocabulary, and objects specifically to the practice of packaging that identification as a definition. Wrapping an empirical discovery in definitional clothing does not make it safer; it makes it unfalsifiable, which is worse, because it conceals that a real claim about the limits of what any rule-follower can do has been made and needs continued checking.

The reason this holds is that the interesting content of such a claim lives entirely on the outside of the formalism. Inside, everything is provable and boring. The question of whether any process a person could carry out by fixed rules can be re-expressed in this handful of acts is not a question the formalism can answer about itself — it is answered only by repeatedly inventing richer notations and then showing they collapse back down. Post commits to that program explicitly: expect wider formulations, and expect to have to demonstrate each one reduces. Every such demonstration is a passed test rather than a theorem, and no number of them closes the question.

A programmer who takes this seriously stops treating specifications and models as self-justifying. When you write down a state machine you believe describes a protocol, or a type system you believe rules out a class of failure, or a cost model you believe predicts performance, the interesting statement is the correspondence between the model and the thing modeled — and that statement is not inside the model. So you keep it visible, you keep it phrased as something that could be false, and you keep looking for the case that breaks it. The failure mode this guards against is the specification that has silently become a tautology: it agrees with itself perfectly, has stopped saying anything about the system, and nobody notices because it never fails.

**Source:** [Finite Combinatory Processes — Formulation 1](../works/finite-combinatory-processes-formulation-1.md) — the closing argument, where Post frames the equivalence of his formulation with recursiveness as a working hypothesis he hopes will attain the status of a natural law, and criticizes the alternative of hiding it inside a definition.
