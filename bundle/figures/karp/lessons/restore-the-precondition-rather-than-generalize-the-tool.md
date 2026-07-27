---
type: lesson
title: "Reshape the data to fit your cheap tool's preconditions instead of reaching for a more general tool"
figure: karp
works: [theoretical-improvements-in-algorithmic-efficiency-for-network-flow-problems]
axes: [primitive-count, cognitive-load]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Reshape the data to fit your cheap tool's preconditions instead of reaching for a more general tool

**Lesson:** Cheap subroutines usually come with a precondition, and the fast path evaporates the moment the precondition is violated. In the minimum-cost part of this paper the cheap subroutine is the shortest-path search, which visits each reachable node once and costs roughly one pass when all the weights it sees are nonnegative. Let negative weights in and the same search has to revisit nodes, and the cost multiplies by something on the order of the node count. The obvious response is to accept the more general and slower subroutine, since the data has negative weights and that is simply the situation. Karp's response is the better one, and he pointedly remarks that the field had underattended to it: change the data so the precondition holds again.

The instrument is a per-node offset added on the way in and subtracted on the way out. Adjusting each connection's weight by the difference between its endpoints' offsets leaves every path's ranking intact, because the intermediate adjustments cancel and only the endpoints survive, so the shortest path is the same path before and after. Choose the offsets well and every adjusted weight comes out nonnegative. The negative weights did not disappear from the problem; they were absorbed into a bookkeeping layer that the fast subroutine never sees. You keep the simple tool, and you keep its guarantee, and you pay only for a transformation that costs nothing asymptotically.

This is a general move and it deserves to be a reflex. Before adopting a heavier mechanism because your data is awkward, ask whether some answer-preserving transformation puts the data back inside the cheap mechanism's comfortable regime: normalize, shift, rescale, sort, deduplicate, partition, canonicalize. The two conditions to check are the ones that make the trick sound rather than merely convenient. The transformation must provably preserve the thing you are computing, and it must be cheap relative to the work it protects. When both hold, you have kept your toolkit small, which matters more than the speed: one subroutine with one clear precondition is far less to hold in your head, and far less to get wrong, than two subroutines and a rule for choosing between them.

**Source:** [Theoretical Improvements in Algorithmic Efficiency for Network Flow Problems](../works/theoretical-improvements-in-algorithmic-efficiency-for-network-flow-problems.md) — the minimum-cost flow section, which notes the efficiency available when all weights are nonnegative and then constructs the algorithm so every shortest-path computation is performed on a reweighted network where that condition holds.
