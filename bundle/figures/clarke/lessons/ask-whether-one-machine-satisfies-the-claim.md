---
type: lesson
title: "Ask whether one machine satisfies the claim, not whether the claim is provable"
figure: clarke
works: [design-and-synthesis-of-synchronization-skeletons-using-branching-time-temporal-logic, automatic-verification-of-finite-state-concurrent-systems-using-temporal-logic-specifications, model-checking-algorithmic-verification-and-debugging]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [lesson]
---
# Ask whether one machine satisfies the claim, not whether the claim is provable

**Lesson:** Two very different questions hide behind the phrase "is this program correct." The first asks whether a correctness assertion follows from axioms, which means constructing a derivation, which means inventing the intermediate assertions that make the derivation go through. The second asks whether one particular finite machine, the one actually in front of you, happens to satisfy the assertion. The first question is open-ended and needs human invention; the second is a computation over a graph. The decisive move here was noticing that for a large class of real systems only the second question needs answering, and that answering it is cheap: a labeling pass over the state graph, linear in the graph and in the formula, closer in spirit to compiler dataflow analysis than to theorem proving.

The reason this holds is that the difficulty in deductive verification was never in the logic; it was in the quantification. Validity ranges over all structures, so establishing it requires an argument that covers structures you have never seen, and the general validity problem for the relevant logics is expensive enough that mechanical provers could not carry the load either. Truth under a single fixed interpretation ranges over nothing. It is a finite question, answerable by search, and the search does not need to be clever about the system's meaning, only exhaustive about its states. The interesting consequence is a decoupling: whoever builds the system and whoever checks it no longer need to be the same person or work in the same rhythm, because checking is not a creative act that must be interleaved with design.

A programmer who takes this seriously stops treating "prove it" as the only rigorous option, and starts asking what the smallest closed world is in which the property becomes decidable. That question has a practical answer far more often than people expect, because the properties worth worrying about in a concurrent system usually depend on a small, finite skeleton of coordination states rather than on the unbounded data flowing through. Once the world is closed, the tool can be a button rather than a collaborator, and the discipline shifts from finding proofs to defining the model and stating the property carefully.

**Source:** [Design and Synthesis of Synchronization Skeletons Using Branching Time Temporal Logic](../works/design-and-synthesis-of-synchronization-skeletons-using-branching-time-temporal-logic.md) argues in its opening that proof construction is unnecessary for finite-state concurrent systems and can be replaced by a mechanical check; the 1986 journal paper's introduction sharpens this into the model-checker framing with its linear-time labeling algorithm, and the Turing lecture's opening section contrasts the approach explicitly with Floyd–Hoare deductive verification and with the satisfiability-centred research culture it grew up in.
