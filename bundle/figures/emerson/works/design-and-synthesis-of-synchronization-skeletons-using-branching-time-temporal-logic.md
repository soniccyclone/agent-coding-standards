---
type: work
title: "Design and Synthesis of Synchronization Skeletons Using Branching Time Temporal Logic"
figure: emerson
description: One of the two founding model-checking papers (the other being Queille and Sifakis' contemporaneous, independent work). Shows that whether a finite-state concurrent program satisfies a branching-time temporal-logic (CTL) specification can be checked algorithmically against the program's state-transition graph, rather than by hand-built inductive proof. Frames this as a tool for both verifying and synthesizing the "synchronization skeleton" — the bare control structure governing process interleaving, with sequential internals abstracted away.
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
year: 1981
url: https://www.cs.cmu.edu/~emc/papers/Conference%20Papers/Design%20and%20synthesis%20of%20synchronization%20skeletons%20using%20branching%20time%20temporal%20logic.pdf
access: public
host: self-archived
tags: [work]
---

# Design and Synthesis of Synchronization Skeletons Using Branching Time Temporal Logic

**Author(s):** with Edmund M. Clarke
**Venue/year:** Logics of Programs (Yorktown Heights workshop), LNCS 131, Springer, 1981, pp. 52-71.
**Source:** https://www.cs.cmu.edu/~emc/papers/Conference%20Papers/Design%20and%20synthesis%20of%20synchronization%20skeletons%20using%20branching%20time%20temporal%20logic.pdf — self-archived PDF on co-author Edmund Clarke's own CMU faculty page, live and directly downloadable (HTTP 200).

## Lessons
- [When the state space is finite, stop constructing proofs and start deciding truth](../lessons/check-the-model-instead-of-constructing-the-proof.md)
- [Pick the abstraction from the property you intend to check, then own the claim that it is faithful](../lessons/the-abstraction-you-check-is-a-claim-about-the-real-artifact.md)
- [Extra expressive power in a specification notation is billed at checking time, so buy the weakest one that says what you mean](../lessons/every-gain-in-what-a-notation-can-say-is-charged-at-checking-time.md)
- [A recursive definition has two solutions, and which one you meant is the difference between an obligation and a constraint](../lessons/two-kinds-of-recurrence.md)
- [Treat global behavior as primary and each component as a projection of it; shared state is the price of projecting](../lessons/local-processes-are-projections-of-a-global-behavior.md)
