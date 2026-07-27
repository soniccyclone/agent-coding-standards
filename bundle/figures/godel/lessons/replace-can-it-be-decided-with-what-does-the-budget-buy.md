---
type: lesson
title: "Once you attach a budget, the question stops being whether it can be decided and becomes how the cost climbs with the budget"
figure: godel
works: [letter-to-von-neumann]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Once you attach a budget, the question stops being whether it can be decided and becomes how the cost climbs with the budget

**Lesson:** Gödel's letter opens by conceding that the general question is undecidable and then declining to treat that as the end of the matter. He attaches a size budget to the object being searched for, observes that the budgeted version is trivially decidable by brute force, and redirects all the interest onto a single function: the worst-case work needed as the budget grows. The reframing is the entire content of the letter's mathematical part, and it is a change of subject that costs nothing. The undecidable problem and the budgeted problem have the same practical purpose. What changed is that the second one has a cost curve you can ask questions about, while the first only has a yes-or-no verdict that was already known and already negative.

His justification for treating the budgeted version as good enough is worth copying exactly. A procedure that searches within the budget and reports nothing found is not a decision procedure; it answers "not within this budget" rather than "no". Gödel argues this distinction stops mattering in practice once the budget can be pushed high enough cheaply, because past some point the absence of a result is itself decision-grade information about where to spend further effort. That is the standard justification for every real tool that lives under a resource ceiling: a bounded model checker, a solver with a timeout, a type inferencer with a depth limit, an SLA-bounded retry. None of them decides the general question. Each is useful in proportion to how far you can raise its ceiling per unit of compute, which means the honest figure of merit for such a tool is the shape of its cost-versus-ceiling curve, not the theoretical class of the problem it approximates.

The habit this produces is to refuse both of the lazy positions. The pessimist reads an undecidability or intractability result and concludes the tool cannot exist; the optimist ships a tool and never states its ceiling. The productive position is to name the budget parameter explicitly, make sure the tool reports whether it hit the ceiling instead of silently answering as though it had not, and then treat the growth of cost in that parameter as the number the engineering work is actually aimed at. Gödel also notes the least interesting version of the curve — searching every candidate — which is the baseline any such tool must beat to justify itself. Existence of the brute-force version is what makes the problem well-posed; the distance between brute force and what you achieve is the whole product.

**Source:** [Letter to John von Neumann](../works/letter-to-von-neumann.md) — the central paragraph, which sets up the machine deciding proof-existence within a length bound, names the worst-case step count as a function of that bound, and argues that a fast enough such function would let a machine take over yes-or-no mathematical work despite the general problem being undecidable, since a large enough bound with no result found is itself actionable.
