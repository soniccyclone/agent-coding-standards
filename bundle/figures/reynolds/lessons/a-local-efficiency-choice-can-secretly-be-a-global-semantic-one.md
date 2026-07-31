---
type: lesson
title: "A choice you make for local efficiency may be deciding a global property nobody was choosing"
figure: reynolds
works: [the-craft-of-programming]
axes: [hardware-affinity, cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# A choice you make for local efficiency may be deciding a global property nobody was choosing

**Lesson:** Deliberately leaving a decision open is supposed to be safe, because you proved that every way of resolving it is correct. It is safe with respect to correctness, and that is all it is safe with respect to. When the moment comes to resolve it — usually deep in a representation decision, on grounds as mundane as which end of an array is cheaper to edit — the resolution can determine an emergent property of the whole computation that no line of the program mentions and no part of the proof constrains. Remove from the end you add to and the pending work behaves as a queue; remove from the end you added to last and it behaves as a stack; those two are a breadth-first and a depth-first exploration, which differ in memory profile, in the order results become available, and in which practical uses the program is fit for. Both are equally correct, and they were selected by a decision made on the grounds of one arithmetic operation.

The lesson is not to stop leaving choices open. It is that the freedom you banked has a second denomination you did not price. When you resolve an indeterminacy, the question to ask is not only "is this still correct" — you already answered that — but "what property of the whole run does this now fix, and did I mean to fix it?" Any invariant strong enough to let both options through is by construction silent about the difference between them, so the proof cannot warn you. You have to go looking, and the place to look is at properties that are about the aggregate behaviour rather than the result: order of production, depth of nesting, peak resource use, latency to the first answer.

The corollary is a good reason to write down the resolution and its consequence together, even when the resolution feels arbitrary. Somebody later will read a one-character difference in an index update and have no way of recovering that this was where the traversal discipline of the entire algorithm was chosen. The efficiency argument that motivated it is legible from the code; the behavioural consequence is not, and it is usually the one that matters to whoever is debugging.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 5.1.4, which resolves the abstract program's indeterminate choice of an unprocessed node by noting that deletion is easier if the chosen element sits at one end of the array segment, gives the two resulting options of advancing the lower bound or retracting the upper bound, observes that these make the array behave as a queue and as a stack respectively, and then records that the difference has a profound effect on the order in which reachable nodes are processed — breadth-first in one case, depth-first in the other — with the remark that the freedom to make either especially efficient choice was itself a consequence of having left the member selection indeterminate at the abstract level.
