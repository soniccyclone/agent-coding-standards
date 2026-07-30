---
type: lesson
title: "A service that both a layer and its clients require cannot live in either, and that is a verdict on the layering"
figure: wilkes
works: [cambridge-cap-computer-and-its-operating-system]
axes: [cognitive-load, verifiability]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# A service that both a layer and its clients require cannot live in either, and that is a verdict on the layering

**Lesson:** When you propose inserting a layer, test it against the services that everything needs. Put such a service above the new boundary and the layer's own machinery cannot reach it, so that machinery has to grow a private, rudimentary version — which will diverge, and which will be needed earliest of all if the layer must bring itself up from nothing. Put it below, and the clients can only reach it through the layer, which means either a pass-through for every operation or a translation of one naming scheme into another at a cost paid on every call. There is no third option inside the proposed structure, and the choice between two bad ones is not a design decision to be made carefully; it is evidence that the boundary is in the wrong place.

The reason this recurs is that layering assumes a dependency ordering, and a universally required service has no position in that ordering — it is depended on by the layer and by what the layer serves. The reliable diagnostic is to enumerate, before committing to a boundary, the things that both sides of it will need, and specifically the things needed during initialization, since bootstrapping is where mutual dependency is exposed most brutally. If that list is non-empty and the items on it are substantial, the boundary as drawn does not exist.

The historical shape of the failure is worth recognizing because it repeats whenever one system is run under another rather than beside it. The recurring hard part is never the arithmetic or the scheduling; it is giving the inner system access to the outer system's persistent state at acceptable cost. Systems that took this route successfully generally did so by giving up and maintaining a second, entirely separate store — which is the same admission in a different form, paid for with duplication instead of complexity.

**Source:** [The Cambridge CAP Computer and Its Operating System](../works/cambridge-cap-computer-and-its-operating-system.md) — Chapter 5's discussion of running one coordinator under another, where the recurring major difficulty is giving lower-level users access to the main filing system at acceptable cost, noting that some successful early time-sharing systems run under batch systems provided a wholly separate filing system of their own, and the dilemma that defining the filing system at the upper level makes it inefficient for users while defining it at user level leaves the system's own processes needing a rudimentary one for bootstrapping.
