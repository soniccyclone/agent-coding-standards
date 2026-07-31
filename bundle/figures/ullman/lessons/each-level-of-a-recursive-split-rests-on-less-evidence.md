---
type: lesson
title: "Each level of a recursive split rests on less evidence"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Each level of a recursive split rests on less evidence

**Lesson:** Procedures that build a structure by repeatedly subdividing — split the population, then split each part, then split those — have a property that is easy to miss because every level looks like the same operation. The evidence supporting each decision shrinks geometrically with depth. The first split is chosen against everything you have and, if it is any good, expresses a real regularity. A split six levels down is chosen against a handful of cases, and with enough candidate criteria available, one of them will separate those few cases perfectly by accident. The procedure cannot tell the difference: a criterion that perfectly separates the cases in front of it looks equally good at every depth, and it is only meaningful at the top.

So the resulting structure is not uniformly trustworthy. Its shallow parts encode findings and its deep parts encode coincidences, with no marker between them. This is why depth-limiting is such an effective control — it is not a crude approximation of a more principled method, it is a direct expression of "beyond this point the decisions are not supported." It is also why the shallow part of such a structure is usually the readable part: the criteria near the root can be stated in domain terms and defended, while the ones near the leaves tend to be arbitrary-looking cuts on quantities that have no plausible relationship to the outcome.

That last observation gives a cheap and underused diagnostic. Read the criteria off the structure and ask, of each, whether there is a reason the world would work that way. A split that says the outcome depends on which region a case is from may correspond to something real. A split that says the outcome depends on a numeric quantity falling into a narrow band, on a quantity with no causal connection to the outcome, is a fingerprint of the procedure using whatever was handy to separate the few cases it had left. You do not need held-out evidence to notice that; you need to read the model.

The general point applies to any recursive refinement, not just to classifiers: hierarchical rules, nested configuration overrides, cascading special cases in a codebase. The refinements near the root were made under pressure from many cases and generally state something true. The ones near the leaves were each added for one or two situations, and their generality was never tested. Both the trust you extend and the effort you spend maintaining them should be graded accordingly.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the worked decision-tree example in the large-scale-machine-learning chapter, where the root test on continent captures a genuine regularity while the second-level tests on population merely separate the handful of countries reaching those nodes, leading the tree to a confidently wrong prediction for an unseen country — and the chapter's accompanying remarks on limiting tree depth and on removing nodes to reduce overfitting.
