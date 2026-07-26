---
type: lesson
title: "Requirements can contradict each other, so make the contradiction detectable before implementation"
figure: emerson
works: [using-branching-time-temporal-logic-to-synthesize-synchronization-skeletons]
axes: [verifiability, expressiveness]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# Requirements can contradict each other, so make the contradiction detectable before implementation

**Lesson:** A set of requirements is normally treated as a wish list: each item is judged on its own, and the interaction between items is discovered later by whoever tries to satisfy them all. That ordering wastes the most expensive resource, which is the time spent building against an impossible target. A specification written in a formalism with a decision procedure inverts it. Asking whether the conjunction of the requirements has any model at all is a question that can be answered mechanically, before a line of implementation exists, and a negative answer is as valuable as a positive one: it says no implementation can exist, so the requirements themselves are the defect.

The illustrative case is small and instructive. Take a coordination problem and demand both that one participant always gets priority when both are waiting, and that the other is nevertheless guaranteed to eventually proceed. Each demand is individually reasonable and individually satisfiable. Together they are unsatisfiable, and the reason is structural rather than clever: a fast-enough privileged participant can keep re-entering forever, so the guarantee for the other one has no way to be discharged. Weaken the guarantee, replacing the unconditional promise with one conditioned on the privileged participant not being active, and the requirements admit a model. The formalism does not merely reject; the shape of the failure tells you which requirement to weaken and how far.

The habit worth adopting is to treat the requirement set as an object with its own consistency, distinct from any implementation of it, and to ask for evidence of satisfiability rather than assuming it. Concretely: before building a system, look for the pair of requirements that pull in opposite directions under adversarial timing, and either prove the pair is jointly achievable or find the weakest strengthening of the assumptions under which it becomes achievable. In coordination and scheduling this pattern shows up constantly — fairness against priority, liveness against exclusivity, availability against consistency — and each time, the useful move is to name the condition under which the guarantee is offered instead of offering it unconditionally and discovering the impossibility in production.

**Source:** [Using Branching Time Temporal Logic to Synthesize Synchronization Skeletons](../works/using-branching-time-temporal-logic-to-synthesize-synchronization-skeletons.md) — the synthesis section's third worked example, an intentionally inconsistent variant of the readers-writers requirements, where the decision procedure's deletion rules fail to certify the eventuality and propagate inconsistency to the root; contrasted with the satisfiable variant in which the starvation guarantee is made conditional.
