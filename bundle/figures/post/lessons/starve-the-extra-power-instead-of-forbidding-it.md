---
type: lesson
title: "When you cannot forbid the extra power, build the case where it is unreachable"
figure: post
works: [recursive-unsolvability-of-a-problem-of-thue]
axes: [verifiability, expressiveness]
subdomains: [foundations-of-computation, formal-methods-and-verification, algorithms-and-complexity]
tags: [lesson]
---
# When you cannot forbid the extra power, build the case where it is unreachable

Post faces a system he cannot reason about directly. Rewriting where every rule also runs backwards destroys the property he depends on — with one-directional rules the derivation from a starting string is a single deterministic line, and once both directions are available it fans out into a branching space where nothing is pinned down. The obvious moves are to restrict the system, or to reason about the branching space directly. He does neither. He builds a one-directional system so carefully that when the reverse rules are switched on, they add no reachable results at all: the extra power is present, permitted, and useless. The reasoning then happens entirely in the well-behaved system, and transfers to the general one for free.

The machinery that makes this work is worth separating from the specific proof. Two things are engineered in from the start. Every string the system can produce carries a structural invariant, and the rule set is arranged so that at most one rule ever applies to a string satisfying that invariant, in at most one way. Together these mean a backwards step can only ever retrace the forwards step that produced the string — there is nowhere else for it to go. The generality is not blocked; it is starved. Post gives the technique a name of his own, observing that a known-hard problem can be reduced not to the target but to something that *becomes* the target under a modification which provably cannot change any answer, and that the modification is free to be either a simplification or, as here, a complication.

The transferable habit is a way out of a common trap. You have a component whose general behavior you cannot characterize — a lock-free structure under arbitrary interleaving, a cache with arbitrary eviction, a distributed protocol under arbitrary message reordering. The instinct is to restrict the component so the general case cannot arise, which changes the artifact you shipped into a different one you did not, and leaves you having proven something about the wrong system. The alternative is to establish an invariant about the states actually reachable in your usage, strong enough that the general mechanism's extra freedom has no state to exercise it on. The system keeps its full generality; your argument only has to cover what can happen.

What makes this more than a trick is the direction of work. Restricting the system is cheap to state and yields a theorem about a system nobody runs. Engineering reachability is expensive up front — the invariant has to be designed into the construction, not discovered afterward — and yields a theorem about the real thing. The lesson is to spend on the second, and to recognize the moment when "I need to disallow this" is really "I need to make this unreachable."

**Source:** [Recursive Unsolvability of a Problem of Thue](../works/recursive-unsolvability-of-a-problem-of-thue.md) — the strategy stated early on, the pair of lemmas showing the reversed system's derivations collapse back onto the forward ones, and the closing remarks where Post names the method of the irrelevant modification.
