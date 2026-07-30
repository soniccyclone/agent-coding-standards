---
type: lesson
title: "Give up on the general theory: specialize the argument to one property and one architecture"
figure: sifakis
works: [turing-lecture-2009]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# Give up on the general theory: specialize the argument to one property and one architecture

**Lesson:** The obvious way to make whole-system reasoning tractable is divide and conquer: establish something about each part, then combine. The obvious formulation of that — attach to each component an assumption about the environment it sits in and a promise it keeps when the assumption holds — has been pursued for decades and disappoints, largely because discovering the right assumptions can cost as much as analyzing the undivided system. Sifakis's diagnosis is that any compositional theory general enough to cover arbitrary properties of arbitrary systems will be intractable by construction, and worth only theoretical attention. The escape is to stop looking for the theory and start collecting narrow results.

Narrow means keyed to two things at once. First, a specific property rather than a whole class: rules that establish freedom from deadlock are a different investigation than rules that establish mutual exclusion, and lumping both under "safety" throws away exactly the structure that would have made either cheap. Second, a specific way of wiring components together — a ring, a star, a fixed-priority schedule with preemption, a time-triggered bus. A worked example: check that each component can only block while waiting on a partner, then check that the graph of interactions has no cycle. The second check looks only at the wiring, not at any component's internals, and where it succeeds it discharges a global property for almost nothing. Measured against general-purpose whole-system tools, that kind of specialization wins by wide margins.

The habit to build is suspicion of the impulse to generalize an analysis before it has proven itself narrowly. Generality in a proof technique is not free the way generality in an interface is; it usually costs you the assumption that made the argument short. When a global property resists, the productive question is which specific structural feature of your architecture would make it obvious, and whether you are willing to commit to that feature.

**Source:** [Model Checking: Algorithmic Verification and Debugging](../works/turing-lecture-2009.md) — Sifakis's argument that a general compositional verification theory will be intractable, his two proposed directions of specialization by property class and by architecture, and the deadlock-freedom method built on component-local checks plus acyclicity of the interaction graph.
