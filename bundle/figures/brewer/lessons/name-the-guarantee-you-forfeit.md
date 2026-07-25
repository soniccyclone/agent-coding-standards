---
type: lesson
title: "Name the guarantee you are forfeiting before the failure names it for you"
figure: brewer
works: [towards-robust-distributed-systems, harvest-yield-and-scalable-tolerant-systems]
axes: [parallelizability, verifiability]
subdomains: [distributed-systems-and-concurrency, databases-and-data-management]
tags: [lesson]
---
# Name the guarantee you are forfeiting before the failure names it for you

**Lesson:** When a system spans a network, certain combinations of guarantees are jointly unachievable, so every design already embodies a sacrifice whether the designer chose it or not. The productive move is to make that sacrifice a first-class design decision: state which property you will give up under which failure, and let the rest of the architecture follow from that choice. A designer who skips this step has not avoided the trade-off; they have merely delegated it to whatever the code happens to do when a link drops, which is usually the worst of the available options.

The deeper habit here is treating impossibility as a design instrument rather than a discouragement. Knowing that a region of the design space is unreachable is what gives the reachable regions their shape: it tells you the axes along which systems can legitimately differ, and it converts vague debates about "reliability" into a concrete question with a small number of defensible answers. Brewer also insists the choice is a spectrum, not a binary. Between the transactional extreme and the availability-first extreme lies a continuum of weakened guarantees, and real systems are mixtures, applying strict guarantees only to the small subsystems whose semantics demand them (revenue paths, say) while the bulk of the system runs relaxed.

A programmer who internalizes this stops asking "how do I make this component never fail?" and starts asking "which promise does this component break when its peers become unreachable, and is that the promise we can afford to break?" That question can be asked per subsystem, per operation, even per datum, and each asking is cheap compared with discovering the answer in production.

**Source:** [Towards Robust Distributed Systems](../works/towards-robust-distributed-systems.md) — the middle arc of the keynote, where the consistency/availability tension is posed as a theorem-shaped constraint with worked examples of forfeiting each corner in turn, and the ACID/BASE contrast is presented as a spectrum rather than a duel. [Harvest, Yield, and Scalable Tolerant Systems](../works/harvest-yield-and-scalable-tolerant-systems.md) — the opening sections, which state the pick-at-most-two principle in print and sketch its proof by exhausting the pairings.
