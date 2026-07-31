---
type: lesson
title: "Name the settings at which your generalization becomes the old thing"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, foundations-of-computation]
tags: [lesson]
---
# Name the settings at which your generalization becomes the old thing

**Lesson:** When you propose a richer construct to replace a simpler one, there is a cheap and decisive test of whether it is genuinely a generalization: find the values of its new parameters at which it reduces exactly to the thing it replaces. If you can name that point, you have proved that nothing was lost — every behaviour the old construct could produce is still reachable — and you have converted a claim about improvement into a claim about strictly added reach. If you cannot name it, then what you have is not a generalization but a different design, and the honest framing is a trade, with cases the old one handled that the new one does not.

The exercise pays for itself even when it succeeds, because the reduction point is the most informative thing you can tell a reader about the new construct. It says which of the new degrees of freedom are the substantive ones and what each is doing, since each is described by what happens when it is pinned to its degenerate value. It also gives you a test case that must pass: run the general implementation with the parameters pinned and check that it reproduces the old implementation. That is a strong regression test, and it is available to almost nobody who has not done this analysis.

Be exact about how exact the reduction is. Frequently it is not perfect — the general construct with parameters pinned is nearly but not quite the old one, differing by an extra transformation somewhere. Saying so precisely is much better than either claiming a clean reduction or abandoning the framing, because the residual difference is itself a design decision that was made and deserves to be visible. A near-reduction with the discrepancy named is a completely satisfactory result.

There is a corollary about cost. A construct that strictly contains another has strictly more to determine, and that budget comes from somewhere — more evidence, more memory, more tuning. So the reduction argument establishes that the general version can do everything, and does not establish that it should be used. When the extra reach is not needed, the simpler member of the family remains the right choice, and knowing they are members of one family is exactly what makes that a decision rather than a preference.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the long-short-term-memory section of the recurrent-networks chapter, which pins the forget gate to all zeros, the input gate and output gate to all ones, and observes that what remains is very close to a plain recurrent network apart from one extra activation factor, followed by the note that the added capability costs many more parameters and that a variant with a single state vector may suit smaller datasets better.
