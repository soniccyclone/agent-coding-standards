---
type: lesson
title: "Refusing to call a slow participant broken is what makes a fault budget mean anything"
figure: lynch
works: [consensus-in-the-presence-of-partial-synchrony]
axes: [verifiability, cognitive-load, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---
# Refusing to call a slow participant broken is what makes a fault budget mean anything

There is a shortcut every engineer reaches for when a protocol needs a delay bound it does not actually have: invent one, and declare anybody who exceeds it faulty. It looks like a free conversion of an unknown timing parameter into a known one. It is not free, and the reason is worth internalizing. A correctness specification only makes promises about the behavior of non-faulty participants; faulty ones are excused from everything. So each time you reclassify a merely slow participant as faulty, you shrink the set of participants your guarantee covers. Guess the bound too tight and the classification cascades — everyone eventually gets declared faulty, at which point the specification promises nothing at all and is trivially satisfied by a system that does whatever it likes.

Slowness and brokenness therefore need separate budgets, and the budgets are not interchangeable. This is visible in what changes when a timing bound goes from known-in-advance to merely existing: for the mildest failure mode, tolerating a given number of crashes stops needing barely more participants than crashes and starts needing roughly twice as many. The lower-bound arguments show precisely where the extra headroom goes. Split the participants into two groups that cannot hear each other because their messages are running late rather than because anything is broken; each group, unable to distinguish this from the other group being dead, must proceed on its own or violate termination, and if each group could ever be large enough to act alone the two of them act inconsistently. The resource that buys safety here is the guaranteed overlap between any two groups large enough to proceed — a quorum intersection argument, arrived at by refusing to let a delayed message masquerade as a failure.

The habit to carry away is to keep failure detection epistemically honest in your own designs. A timeout tells you that you have not heard from someone, which is genuinely different from knowing they are gone, and the code should represent it as such: as a trigger to fall back to a different participant, never as a license to write them out of the guarantee. Concretely, a component that shrinks its own quorum whenever peers seem slow has traded a real safety property for a fictional liveness one; a component that keeps the quorum fixed and instead rotates whose turn it is to lead has kept both. Real networks and real machines do not fail cleanly, they fail slowly, and a system whose safety argument depends on telling those two apart has no safety argument.

**Source:** [Consensus in the Presence of Partial Synchrony](../works/consensus-in-the-presence-of-partial-synchrony.md) — the argument is set out in the introduction's rejection of treating late or lost messages as processor faults, and its cost is quantified by the lower-bound theorems for partially synchronous communication, which use runs where two initially isolated groups each behave as though the other had died.
