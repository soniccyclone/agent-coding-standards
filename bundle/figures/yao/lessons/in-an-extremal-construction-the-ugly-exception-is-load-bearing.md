---
type: lesson
title: "In a construction that is already at the limit, the ugly exception is load-bearing — delete it and watch it fail"
figure: yao
works: [should-tables-be-sorted]
axes: [cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# In a construction that is already at the limit, the ugly exception is load-bearing — delete it and watch it fail

**Lesson:** Constructions that achieve the best possible bound tend to look arbitrary. They have special cases carved out near the boundary, asymmetries with no evident reason, a handful of positions treated unlike all the others. The instinct is to read this as unfinished work and tidy it — unify the special cases, restore the symmetry, and pick up the extra capacity the exception was apparently wasting. That instinct is exactly backwards when the construction is extremal. Extremal means there is no slack; every irregularity is either forced by the bound or the construction is not extremal. So irregularity is a claim, and the way to evaluate it is to remove it and hunt for the input that then has nowhere to go.

The hunt is concrete and worth doing by hand. Take the tidied version, and rather than testing typical inputs, construct the arrival pattern that maximally stresses the collapsed exception — usually one that saturates the regular positions and then presents one more item that the exception used to absorb. If no valid placement exists, you have learned that the exception was purchasing precisely the capacity you were trying to reclaim, and you now understand the construction rather than merely trusting it. If a placement does exist, you have found a genuine improvement, which is worth more than the tidying. Either outcome is informative; skipping the test and reasoning from aesthetics is the only move that gains nothing.

There is a wider point about where surprise should be directed. Being surprised that an ugly scheme is optimal is a signal that your model of what makes schemes good is calibrated on non-extremal designs, where symmetry usually does come free and usually does help. Near a limit that intuition inverts, because the symmetric design is spending its uniformity on cases that no longer need to be handled uniformly. Practically, this means the reviewer's question "why is this case special?" deserves an answer of the form "here is the input that breaks it if it is not," and a construction whose author cannot produce that input has an exception that probably should be removed. Load-bearing irregularity and accidental irregularity look identical on the page and are distinguished only by the adversarial input, so the input is the artifact worth recording alongside the code.

**Source:** [Should Tables Be Sorted?](../works/should-tables-be-sorted.md) — the single-probe construction, presented as an occupancy assignment in which two of the positions are given a different status from the rest, and the remark following it that observes how arbitrary the optimal scheme looks, asks why the special positions are needed, and answers by exhibiting the arrival sequence that makes the assignment impossible when only one special position is retained; the accompanying appendix supplies the matching impossibility argument.
