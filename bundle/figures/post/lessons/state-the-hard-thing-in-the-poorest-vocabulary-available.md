---
type: lesson
title: "State a result in the poorest vocabulary you can, and it becomes everyone's building block"
figure: post
works: [a-variant-of-a-recursively-unsolvable-problem]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# State a result in the poorest vocabulary you can, and it becomes everyone's building block

The problem this paper isolates mentions nothing about computation. There are two parallel lists of strings and a question about whether some sequence of picks, repeats allowed, makes the two concatenations agree. No machines, no logic, no derivations, no vocabulary borrowed from the field the result came out of. Post arrives at that austerity deliberately, and the last thing he does before finishing is push it further: the construction naturally needed extra symbols, and he removes them by translating each into a distinct pattern over just two letters, arguing that the translation cannot be misread because the patterns force their own parsing. The final statement uses the smallest alphabet and the fewest concepts that will carry it.

The payoff is entirely in what other people can do with the result afterward. A hardness result phrased in the machinery it was proved with can only be applied by someone willing to learn that machinery and build a translation into it. The same result phrased as a bare combinatorial puzzle can be aimed at anything — and this one was, becoming a standard starting point for undecidability arguments in areas with no connection to its origin. The impoverishment is not modesty about the result's importance; it is what makes the result composable. Every domain-specific term in a statement is a barrier to reuse, and the work of removing those terms is real work, done after the theorem is already true.

The same economics apply to anything you build for others to build on. A protocol whose messages presuppose your service's internal model can be spoken by nobody else. A library whose central function takes your framework's context object cannot be called outside your framework. A data format that assumes your enumerations is not a format. The discipline is to finish by asking what the artifact would look like stated in the poorest terms that still express it — plain bytes, plain integers, plain pairs — and to add whatever translation layer is needed to get there, keeping the richer internal vocabulary strictly internal.

Note the shape of the whole exercise: build with whatever symbols make the construction tractable, then pay the cost of eliminating them at the boundary. Post does not restrict himself to two letters while working; he uses the extra symbols freely for the argument's sake and encodes them away at the end. The poverty belongs to the published interface, not to the process that produced it, and confusing those two makes the work harder for no gain.

**Source:** [A Variant of a Recursively Unsolvable Problem](../works/a-variant-of-a-recursively-unsolvable-problem.md) — the framing of the correspondence decision problem in purely combinatorial terms at the outset, and the final step translating the auxiliary symbols into self-delimiting patterns over the two-letter alphabet.
