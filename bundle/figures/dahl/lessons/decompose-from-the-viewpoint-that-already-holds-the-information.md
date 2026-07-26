---
type: lesson
title: "Choose the entity whose viewpoint already holds the information the behavior needs, and the program shrinks"
figure: dahl
works: [simula-an-algol-based-simulation-language]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Choose the entity whose viewpoint already holds the information the behavior needs, and the program shrinks

**Lesson:** Given a shop of machine groups processing orders, both decompositions are available and both are faithful to reality. You can make the machines the active entities, each pulling work from its queue and operating on orders as passive data, or you can make the orders active, each walking the route it was given and claiming a machine at each stop. The paper picks the second and gives the reason: an order already carries everything relevant to routing and processing, so writing the behavior from its point of view produces the shortest program. The observation is small and the principle behind it is not. Which candidate entities you promote to active status is a real design decision with a large effect on program size and clarity, and it has a criterion rather than being a matter of taste.

The criterion is where the information lives. Behavior written from a viewpoint that lacks the facts it needs must import them, and importing means parameters, shared structures, back-references, and coordination between entities that each hold half of a decision. Behavior written from the viewpoint that already owns the facts reads as a sequence of local decisions. So the question to ask about a proposed decomposition is not which entities are most prominent in the domain, nor which ones a diagram of the domain would draw largest, but which ones hold the state that the interesting behavior consults. Prominence and information-ownership frequently diverge, and the machines-versus-orders case is exactly such a divergence: the machines are the expensive, visible, physically real things, and the orders are where the knowledge is.

There is a second, quieter consequence. The unchosen entities do not disappear, they become resources: counts, queues, and availability, which is a much cheaper representation than a full active entity with its own lifetime. Choosing the information-bearing viewpoint therefore reduces the number of entities that need behavior at all, not merely the length of the behavior you write.

A programmer applying this asks, for each behavior in the specification, which noun in the system would need to be told the least in order to carry it out, and lets the answers accumulate before assigning responsibilities. Where the answer is that no existing noun holds enough, that is evidence for a missing entity rather than for adding another parameter. The failure mode this replaces is decomposing along the shape of the domain's org chart or its physical inventory and then spending the rest of the project passing information between the pieces.

**Source:** [SIMULA - an ALGOL-Based Simulation Language](../works/simula-an-algol-based-simulation-language.md) — the worked job-shop example, whose accompanying remarks note that the system could equally have been formulated with machines as the processes acting on orders, and explain the choice of the order's viewpoint by the fact that it already contains the routing and processing information.
