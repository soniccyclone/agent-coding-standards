---
type: lesson
title: "Two things whose live regions grow and shrink in step can share one store, and the whole argument is a footprint check"
figure: reynolds
works: [the-craft-of-programming]
axes: [hardware-affinity, verifiability]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Two things whose live regions grow and shrink in step can share one store, and the whole argument is a footprint check

**Lesson:** Look for pairs of variables whose *live* extents are complementary — one grows by exactly one element each time the other's shrinks, and vice versa on the way back. When you find such a pair, the auxiliary structure never needs storage of its own; it can live inside the part of the other that has gone dead. The tell is arithmetic: if the size of one region plus the size of the other is constant across the whole run, they can be laid on top of each other, and a working area that looked like it needed space proportional to the input turns out to need a constant.

The mechanical obstacle is almost always a direction mismatch — the dead region of the host grows from one end while the guest grows from the other. This is not a reason to abandon the overlay; it is a reason to index the guest backwards inside the host. Write the correspondence as a representation invariant relating the two index spaces by subtraction, and the reversal stops being a trick you have to hold in your head and becomes a formula the rest of the derivation carries for you. Notice also that such an invariant usually couples two counters, so it only holds if certain assignment pairs are treated as indivisible; the right response is to declare that granularity explicitly rather than to weaken the invariant into something unusable.

The reason this is safe, and the reason it is worth doing this way rather than by inspection, is that the safety condition is narrow and checkable: every write you add must land inside the host's dead region, and nothing the rest of the program reads may live there. That is a statement about footprints, not about the algorithm's cleverness. Once it holds, the guest can be made auxiliary — every read of it rewritten as a read of the host through the index formula — and its declaration and all its writes fall away. Simplifications you did not plan for tend to fall out at the end, including guards that become tautologies once the substituted arithmetic is visible; take them, but do not go looking for them first.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 5.3.3's final transformation, which observes that the active segment of the heap array grows and shrinks at the same rate as the inactive segment of the array being sorted, notes that the two vary at opposite ends and therefore must be related in reverse order, states the representation invariant tying the loop counter to the heap size and each heap element to a mirrored position in the input array, requires certain counter-update pairs to be regarded as indivisible for the first conjunct to hold already, augments each assignment with a corresponding write into the input array while checking that these writes touch only the inactive segment the rest of the program does not depend on, then makes both the heap array and the counter auxiliary and collapses the resulting always-true conditional, ending with a sort that uses a constant amount of local storage.
