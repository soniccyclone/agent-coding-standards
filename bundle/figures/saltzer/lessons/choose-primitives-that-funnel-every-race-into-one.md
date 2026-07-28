---
type: lesson
title: "Choose primitives that funnel every race into one"
figure: saltzer
works: [traffic-control-in-a-multiplexed-computer-system]
axes: [primitive-count, verifiability, parallelizability]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---
# Choose primitives that funnel every race into one

**Lesson:** Two independent parties that coordinate through shared memory can
interleave in an unbounded number of ways, and no amount of care in the parties
themselves reduces that number. What does reduce it is the choice of the two or
three operations they are given to coordinate with. A well-chosen pair collapses
every timing hazard in the whole class of interactions into a single hazard, at a
single point, curable by a single piece of machinery — in the canonical case, a
one-bit record that a signal arrived, checked by the operation that waits, so that
a wait issued after a signal returns immediately instead of sleeping forever. A
badly chosen pair scatters equivalent hazards across every use site, where each
one must be rediscovered by whoever gets paged at three in the morning.

So the right question to ask of a primitive set is not whether it is expressive
or minimal, but how many distinct failure modes it leaves for its callers to
solve. That is a property you can actually enumerate, and it is worth spending
design effort on, because the count is multiplied by every future caller. It also
tells you where the primitive has to live. The classic hazard — check a shared
condition, then go to sleep, with the other party free to act in between — cannot
be closed by any protocol the two parties arrange between themselves, because the
gap they must eliminate is precisely the gap between their own two operations.
Closing it requires the check and the sleep to be inseparable, which only the
layer that implements sleeping can provide. Recognizing that shape saves you from
a long search for a clever user-level protocol that does not exist.

There is a corollary about what does not count as a fix. You can usually make the
hazard stop reproducing by inserting a delay somewhere, and the result will pass
its tests. But its correctness now depends on a constant that was calibrated
against one machine's speed, which means every processor upgrade silently
re-opens the question, in every place someone used the trick. A programmer who
believes this treats any timing constant load-bearing for correctness as an
unpaid debt, and pushes the problem down to the layer that can make the compound
operation indivisible instead.

**Source:** [Traffic Control in a Multiplexed Computer System](../works/traffic-control-in-a-multiplexed-computer-system.md) — the critical-race analysis in chapter three, section two: the missed-signal interleaving, the wakeup-waiting switch introduced to resolve it, the argument that processes cannot arrange the interlock themselves, and the explicit rejection of the fixed-delay workaround.
