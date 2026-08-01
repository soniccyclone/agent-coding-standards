---
type: lesson
title: "Check whether the pathology belongs to your data or to your formulation"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Check whether the pathology belongs to your data or to your formulation

**Lesson:** A method acquires a list of input structures it cannot handle, and a matching list of repairs for them. Over time the repairs stop looking like repairs and start looking like part of the method, with their own parameters, their own literature and their own tuning folklore. The question nobody re-asks is whether those structures were ever hostile to the *problem* or only to the *encoding of the problem* that happened to get written down first. That question has a decisive test: formulate the same problem a second way, and see which of the pathologies survive.

The instructive case is two iterative scorings of the same graph. One distributes a conserved quantity along edges, so every node hands out exactly what it receives; the other simply sums neighbours' scores and rescales the whole vector afterwards. The first is destroyed by nodes with no outgoing edges, which leak the conserved quantity until nothing is left, and by closed regions, which absorb all of it. Both defects require a correction with a tunable constant, plus a preprocessing pass, plus an argument about what the corrected numbers now mean. The second formulation meets those same structures and does nothing special. Sinks get a score of zero and pass it along, which is the correct answer. Absorbing regions capture nothing, because nothing is being conserved for them to capture. The defect was never a property of graphs with sinks. It was a property of insisting the score be a probability distribution.

What makes this worth generalising is that conservation is exactly the sort of assumption that feels like rigour. Building the model as a distribution buys a clean interpretation, a limit theorem, and a story about surfers. It also imports every degenerate case that a distribution has, and those cases then get attributed to the messiness of the real world rather than to the modelling choice that created them. The tell is a repair that has no meaning in the problem domain: a constant with no interpretation other than "the amount of correction needed", a preprocessing step whose only justification is that the method breaks without it, an output whose documented caveats are all about structures rather than about the question being asked. Each of those is a receipt for a decision made upstream.

The habit to build is to treat the repair list as a diagnostic rather than a feature list. Before adding the next patch, write down the weakest formulation that would still answer your question, drop whatever invariant the current one is enforcing, and check which pathologies evaporate. Sometimes none do and the structures really are hard, which is worth knowing with confidence rather than by assumption. Often several do, and you have traded a tuning constant and a preprocessing pass for a normalisation step at the end. The two formulations are not interchangeable in general, and the one with the conservation law may still be what you want for other reasons, but you should be paying for it knowingly rather than paying for it in patches.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 5's transition from PageRank to the hubs-and-authorities computation, in particular the observation accompanying the worked HITS example that dead ends and spider traps do not stop the iteration from converging to meaningful vectors, so the graph can be used directly with no taxation or alteration, contrasted against the earlier sections where those same structures force recursive node deletion and a taxation parameter.
