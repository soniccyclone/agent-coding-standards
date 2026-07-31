---
type: lesson
title: "A heuristic win obliges you to name the class — and its complement"
figure: mcmillan
works: [symbolic-model-checking-10-20-states-and-beyond]
axes: [verifiability, hardware-affinity]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# A heuristic win obliges you to name the class — and its complement

The experimental section opens by conceding everything an unfriendly reader might have been preparing to say. The underlying problem is NP-complete and this work does not touch that. The representation being championed does not improve the asymptotic complexity of anything. The entire claim being made is that it behaves well on certain useful families of inputs. Only after establishing that does the paper argue that empirical results are therefore *required* — not as supporting colour, but because no other kind of argument is available for the claim being made.

That ordering is the discipline. Before gathering any evidence, decide which of two things you are asserting. If the assertion is asymptotic, a proof settles it and measurements merely illustrate. If the assertion is that a technique is fast on the inputs that actually occur, then no proof is coming, the measurements *are* the argument, and a second obligation attaches that people routinely skip: you must say which inputs, and by implication which inputs not. A class-conditional claim with no stated class is not a weak claim, it is an empty one, because every technique is fast on something.

The paper honours the second obligation in both directions. It names a family it fails on — multiplier circuits are known to have no compact representation here — and it works forward from that to predict the failure of pipelines containing similar operations, so the boundary is not just acknowledged but pushed on. And it declines to pretend the boundary is fully mapped: characterising exactly which models this is efficient for is listed among the open problems, which is a considerably more useful thing to publish than a confident summary of the successes. A reader can act on a stated ignorance. They cannot act on a silence.

There is a structural reward for this precision that shows up in the same closing pages, and it is the part most worth carrying. Because the contingent claim was pinned to the *representation* rather than to the method, the authors can note that the method transfers intact to any better representation someone later invents for a useful class. Locating the heuristic exactly is what makes it replaceable. Had the empirical success been attributed vaguely to the approach as a whole, the approach would have had to be rebuilt when the representation was eventually superseded — which it was.

The habit: when something you built is fast, work out whether it is fast for a reason that scales or fast because your inputs are shaped conveniently, say which out loud, and go hunting for the inputs where it collapses. Then confine the fragile assumption to one replaceable component, so that when the class shifts underneath you the rest survives.

**Source:** [Symbolic Model Checking: 10^20 States and Beyond](../works/symbolic-model-checking-10-20-states-and-beyond.md) — the opening of the empirical results section disclaiming any asymptotic improvement and framing the claim as heuristic performance on useful classes, and the conclusions, which name the known failure case, extrapolate it to circuit operations with unbounded inter-position information flow, list class characterisation as an open problem, and observe that the algorithm accepts alternative representations.
