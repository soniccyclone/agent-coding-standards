---
type: lesson
title: "How much history to keep is the design variable — deliberate forgetting is legitimate, and its price is paid in the proof"
figure: knuth
works: [fast-pattern-matching-in-strings]
axes: [primitive-count, verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# How much history to keep is the design variable — deliberate forgetting is legitimate, and its price is paid in the proof

**Lesson:** The postscript added to this paper covers a rival method that scans each candidate alignment from its far end rather than its near end, which lets it leap over stretches of text it has no reason to examine and inspect only a fraction of the characters on typical input. Knuth analyses it, and the sentence that carries the design insight is his observation about what the method throws away: when it shifts the pattern along, it discards everything it had learned about the characters it just matched. It starts the next attempt knowing nothing. That is why proving it does not degenerate is hard, and the proof he gives is long and yields an unappealing constant, which he invites the reader to improve.

He also spells out the alternative. You could build a version that forgets nothing, encoding into its state exactly which text positions are already known to agree with the pattern, and dispatching on that. He constructs one for a short pattern and it has over forty distinguishable states; the count is bounded by an exponential in the pattern length and he notes it is not clear which patterns are worst or whether the true maximum really is exponential. So the two ends of the spectrum are visible: retain everything and the state space is intractable to build and reason about, or retain nothing and the algorithm is small, fast, and awkward to prove linear. Neither is wrong. They are different points on a trade-off whose axis is how much of the past you compress into state.

The part worth internalizing is where the cost of forgetting lands. It does not land on correctness — the forgetful algorithm is correct. It does not reliably land on performance — the forgetful algorithm is faster in practice than the one that remembers, because maintaining and consulting a large state is itself work. It lands on the difficulty of *establishing* that nothing pathological happens, because the argument now has to rule out the algorithm rediscovering the same facts many times over. That is a real cost and it should be counted, but it is a cost in analysis effort, not in the artifact. A designer who understands this will accept redundant work in exchange for a small, fast, stateless-ish implementation, and will budget for a harder proof rather than treating the redundancy itself as the defect to be engineered away.

Knuth also records what happens when you try to improve such a method by adding heuristics: the extra skip rule sometimes makes things worse, and the refined shift table is sometimes beaten by the crude one. Local improvements to a method that discards information are not monotone, because the value of a heuristic depends on what the algorithm happens to know at the moment it fires — which, having forgotten, varies. Anyone stacking heuristics onto a fast path should expect exactly this and measure combinations rather than components.

**Source:** [Fast Pattern Matching in Strings](../works/fast-pattern-matching-in-strings.md) — the postscript's treatment of the right-to-left scanning method: its linearity theorem, the remark that the method forgets what it has matched and that this is why linearity is hard to establish, the sketched state-machine variant with its large state count, and the noted cases where the extra heuristic and the refined table each lose.
