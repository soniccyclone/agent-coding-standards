---
type: lesson
title: "Cut module boundaries where simultaneity demands them, not where the data would suggest"
figure: brinch-hansen
works: [the-programming-language-concurrent-pascal, monitors-and-concurrent-pascal-a-personal-history]
axes: [parallelizability, hardware-affinity, cognitive-load]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Cut module boundaries where simultaneity demands them, not where the data would suggest

**Lesson:** Data cohesion is the usual guide to where a module boundary goes, and in concurrent code it is not enough. Consider a contended device: the obvious design puts the device, the queue of pending users, and the transfer itself into one module that guarantees exclusive access. It is cohesive, it is small, and it destroys the thing it was built for. Because the module excludes others while a transfer is running, nobody can arrive and join the queue during a transfer, so requests can only enter one at a time between transfers and any ordering policy programmed inside becomes fiction. Arrival and service are potentially simultaneous events, and two events that must be able to happen at once cannot live inside the same mutually exclusive region. The boundary has to be cut between them even though the data says keep them together.

The general rule this generalizes to is worth stating in both directions. Splitting is forced wherever activities must be able to proceed at the same time; joining is penalized wherever an exclusion region covers state that different callers use for unrelated purposes, since a single guard over independent data means work on one part blocks work on another for no reason at all. Neither of those constraints is visible in a data-flow diagram. They are visible only when you ask, of each proposed module, which pairs of operations must be able to overlap and which are truly in contention for the same thing.

There is a second-order consequence about where policy can live. A system will have some built-in arbitration at its lowest level, chosen for speed and therefore crude — first-come service, typically, which for a device with a moving head is close to the worst rule available. Better policies have to be programmable in the layer above, which means the module structure must leave room for a policy module to observe and order requests independently of whoever is executing them. Get the boundary wrong and no amount of cleverness in the policy code recovers the ability, because the structure has already serialized the information the policy needed. A programmer who thinks this way sizes exclusion regions as tightly as the invariants allow and treats "which operations must overlap" as a first-class input to decomposition alongside the data relationships.

**Source:** [The Programming Language Concurrent Pascal](../works/the-programming-language-concurrent-pascal.md) — the system-design section, which works through why the virtual devices, the arbitrator, and the transfers must be separate components, and why folding them together would make programmed scheduling illusory given the built-in short-term rule. Also [Monitors and Concurrent Pascal: A Personal History](../works/monitors-and-concurrent-pascal-a-personal-history.md) — the recorded discussion of why a single monolithic exclusion region is the wrong structure when it covers unrelated sets of data.
