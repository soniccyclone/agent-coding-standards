---
type: lesson
title: "Cut the model along the seam where two subsystems stop influencing each other"
figure: turing
works: [the-chemical-basis-of-morphogenesis]
axes: [cognitive-load, verifiability]
subdomains: [foundations-of-computation, software-engineering-and-architecture]
tags: [lesson]
---
# Cut the model along the seam where two subsystems stop influencing each other

**Lesson:** When a phenomenon has two intertwined aspects and their mutual dependence is what makes it intractable, the productive move is not to model both badly but to hunt for the regime in which one aspect stops mattering, and to work entirely inside that regime. The choice of what to leave out is then not an act of laziness or convenience; it is chosen precisely because the interaction term is small there, which is what buys you an exactly solvable problem instead of an approximately solvable mess. This is a different discipline from "simplify until you can compute" — you simplify along the one cut where the discarded coupling is genuinely weak, and you say out loud which cut you took.

The reason this works is that difficulty in a coupled system is superlinear in the coupling, not in the parts. Two subsystems each with a well-developed theory can become jointly hopeless the moment each one's state feeds the other's rate of change. Finding a corner of the parameter space where the feedback loop is effectively cut turns a joint problem back into a sequential one, and the sequential version often has closed-form answers that generalize far outside the corner you proved them in.

A programmer who believes this stops trying to build the one model that covers everything and starts looking for the decoupled regime. Concretely: find the configuration where the cache never invalidates, where the schema never migrates, where the network never partitions — solve that completely, learn the shape of the answer, then argue about how far it carries. The rejected alternative is the usual one, a single model with every interaction included and no analysis possible, whose behaviour you can only observe rather than predict. Also: state which aspect you froze. A frozen aspect that nobody names becomes an unexamined assumption in everyone else's reading of your result.

**Source:** [The Chemical Basis of Morphogenesis](../works/the-chemical-basis-of-morphogenesis.md) — the early framing section, where Turing lays out the full state of a developing tissue as mechanical plus chemical, notes that their interdependence is what makes the problem formidable, and deliberately restricts attention to non-growing tissue so the chemical side can be analyzed alone.
