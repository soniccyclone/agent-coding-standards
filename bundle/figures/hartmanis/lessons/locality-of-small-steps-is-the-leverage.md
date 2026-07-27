---
type: lesson
title: "Small local steps are what give you leverage over a computation, so never abstract them away"
figure: hartmanis
works: [relativization-a-revisionistic-retrospective]
axes: [verifiability, hardware-affinity]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Small local steps are what give you leverage over a computation, so never abstract them away

**Lesson:** The convenient high-level picture of a computation is a sequence of steps in which the size of a step does not matter — whether a transition is decided by a small fixed table or by consulting an all-knowing external source, the shape of the run looks the same. That picture is what makes it seem harmless to grant a machine extra power in the form of answers to arbitrary questions, and it is exactly the assumption that misleads. A step of an ordinary computation is small and local: the next configuration depends only on the finite control and on what sits near the heads. That property is not a technicality. It is the reason an entire run can be squeezed into a compact algebraic or logical object and then attacked with tools that know nothing about machines, and it is the reason a run can be re-executed piecewise instead of stored, trading time for space in a way that beats the naive bound. Grant a step the power to depend on an unbounded query and every one of those handles disappears at once, because there is no longer any small local fact from which the step follows.

So the moral is inverted from the usual instinct. The restrictions in a model are not obstacles to be relaxed for realism; they are the surface you get to push on. A system whose transitions are bounded and locally determined is a system whose behavior can be summarized, compressed, replayed, and reasoned about globally. A system in which any step may consult anything is intractable to reason about even though it is more powerful, and the power is the reason. When both non-relativizing families of results turned out to depend on exactly this local coherence, what looked like two unrelated breakthroughs was one insight applied twice.

A programmer who holds this reads architectural decisions differently. Every unrestricted escape hatch — an arbitrary callback in the middle of a state machine, a plugin point that can observe or mutate anything, a query that can reach any data during a transition — buys expressive power by destroying the property that made the surrounding system analyzable, replayable, and testable in pieces. The step that can do anything cannot be summarized, so nothing containing it can be summarized either. This is the mechanism behind the familiar advice to keep effects at the edges and transitions pure, stated as a claim about what proofs and tools remain available rather than as a matter of taste.

The related observation about instability is worth keeping too: because a computation's verdict can be flipped by a change that any sensible metric would call negligible, machine-level descriptions are a poor substrate for reasoning about approximate or robust behavior. When you want to talk about nearness, quality, or degradation, the useful move is to re-describe the object in a formalism where small changes to the description mean small changes in meaning, rather than to reason about the execution directly.

**Source:** [Relativization: A Revisionistic Retrospective](../works/relativization-a-revisionistic-retrospective.md) — the closing section on coherence, which identifies the locality and bounded step size of unrelativized computation as the property exploited both by the algebraic interactive-proof techniques and by the earlier pebbling-based time-versus-space simulation, and which quotes the complaint about computation being an unstable object under small perturbations.
