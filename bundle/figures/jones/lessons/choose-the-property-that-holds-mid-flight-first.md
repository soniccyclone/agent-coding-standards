---
type: lesson
title: "Choose the property that must hold at every intermediate moment before you design the parts that run"
figure: jones
works: [tentative-steps-toward-a-development-method-for-interfering-programs]
axes: [verifiability, parallelizability]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---
# Choose the property that must hold at every intermediate moment before you design the parts that run

**Lesson:** A loop is understood not by its final state but by the relation that survives every trip through the body, and that relation is chosen, not derived. Concurrent composition has the same shape with the iteration count replaced by an arbitrary interleaving: what you need is a relation between the state you started from and any state that can exist while the parts are running, preserved by every step any part can take, and preserved also by whatever the outer environment is permitted to do to you meanwhile. If that relation holds and each part has finished its own obligation, the composite obligation follows. The three checks — established at entry, preserved by each participant, preserved by external interference — are the whole content of "these things can run together."

The order in which you do this matters more than the machinery. It is possible to design the components first and then hunt for a relation that happens to be preserved by all of them, and the hunt sometimes succeeds, but it inverts the dependency: you are reverse-engineering an invariant out of code instead of using it to decide what the code should be. Fixing the mid-flight relation first turns the design of each participant into a bounded question — what may I change, and in which direction, without breaking this — and the answers are exactly the interference obligations each component needs to carry. The relation becomes the shared design document that the participants are written against, rather than the report you write afterwards.

The payoff is that coordination stops being the first tool you reach for. A component's freedom is bounded by the invariant rather than by other components' schedules, so parts that would appear to need mutual exclusion often need none at all once you see which changes actually threaten the relation. Deciding what must stay true throughout is therefore prior to deciding who waits for whom, and getting it in that order routinely reveals that far less synchronization is required than intuition demanded.

**Source:** [Tentative Steps Toward a Development Method for Interfering Programs](../works/tentative-steps-toward-a-development-method-for-interfering-programs.md) — the dynamic-invariant rules for parallel decomposition and their stated analogy to the relational loop invariant; the parenthetical advice that in real development one should begin with the invariant as an aid to designing the subcomponents rather than find it afterwards; and the observation in the equivalence-relation example that far less coordination between parallel tasks proved necessary than originally expected.
