---
type: lesson
title: "Judge a system's extensibility by how little of its innards a contributor must understand, and buy that with order-independent statements instead of procedure edits"
figure: mccarthy
works: [programs-with-common-sense]
axes: [expressiveness, cognitive-load, parallelizability]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Judge a system's extensibility by how little of its innards a contributor must understand, and buy that with order-independent statements instead of procedure edits

**Lesson:** McCarthy sets an unusual acceptance criterion for the system he proposes: it must be possible to change its behaviour by telling it something, where "telling" requires no more familiarity with its internal construction or its accumulated prior content than instructing a person would. That criterion is the interesting part, independent of the artificial-intelligence ambitions wrapped around it. It reframes extensibility as a property of what the extender must hold in their head, not as a property of the code's factoring. A system with beautiful internal structure that nonetheless demands you understand its control flow before you can safely modify its behaviour has failed this test. A system whose behaviour is a function of a body of stated facts has passed it, because the fact can be written by someone who knows the domain and nothing else.

The structural reason this works is worth separating from the aspiration. Imperative instruction says what to do in sequence, so the meaning of any one step depends on the position it occupies and on the state the previous steps left behind. To add a step safely you must reconstruct that state. Declarative statements have neither dependence: their content does not shift with position, and their effect is largely independent of what the system happens to have done so far. Order-independence is what makes afterthoughts cheap, and state-independence is what lets a contributor skip learning the history. Both properties also mean two contributors can add unrelated statements without coordinating, because their contributions commute. The same property that makes a body of facts easy to extend by hand makes it decomposable for machines.

McCarthy is fair about the other side of the trade, and the fairness is instructive. A procedure written as imperatives is already laid out and therefore runs faster, and it assumes nothing already present in the machine, so it can start from a blank state. Declarative instruction only pays off when there is a substantial body of prior knowledge for a new statement to combine with, and it pays for its flexibility in execution cost. This is not a claim that declarative form is superior; it is a claim about which regime each form suits. Small, self-contained, performance-critical, no prior context: write the procedure. Large, long-lived, many contributors, much accumulated context: state facts.

A programmer who works from this asks, of any configuration or extension surface they build, what a newcomer must know to use it correctly, and treats a long answer as a defect in the surface rather than a documentation problem. They notice when adding a case to a system requires understanding where in a sequence the case goes, because that is the symptom of policy encoded imperatively, and they push such policy into data whose ordering does not matter.

**Source:** [Programs with Common Sense](../works/programs-with-common-sense.md) — the introduction's statement of the design goal that behaviour be improvable purely by making statements to the system without knowledge of its internals, and the explicit comparison table of the advantages of imperative versus declarative instruction, which names order-independence and independence from prior state as the declarative side's benefits and speed plus a blank starting state as the imperative side's.
