---
type: lesson
title: "A guarantee about one trial says nothing about many, and one about many says nothing about any"
figure: kolmogorov
works: [grundbegriffe-der-wahrscheinlichkeitsrechnung]
axes: [verifiability]
subdomains: [software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# A guarantee about one trial says nothing about many, and one about many says nothing about any

**Lesson:** Kolmogorov attaches two warnings to the empirical reading of his axioms, and they are the same warning pointed in opposite directions. If two statements are each practically reliable, their conjunction is still reliable, though at a somewhat lowered degree — but once the number of such statements is very large, the reliability of each says nothing whatever about all of them holding together. So the frequency principle, that an observed ratio comes close to the probability, cannot be upgraded into a claim that across a great many series of trials every series behaves that way. Pointed the other way: an event of probability zero is not impossible. Zero licenses only the claim that in a single realization the event practically will not occur; across a long enough run it may well occur, and the frequency for a zero-probability event, while small, need not be zero.

The structure worth internalizing is that a guarantee always carries a quantifier — for one run, for one item, for one pair, in the limit, in expectation — and moving it outside that scope is not a mild extrapolation but a new and unsupported claim. Aggregating a per-item guarantee into an all-items guarantee degrades it multiplicatively and silently, until at large counts it carries nothing at all. Specializing an aggregate guarantee down to a single case gives nothing either, because the aggregate was compatible with arbitrary behavior in any particular instance. Both moves feel harmless because the number attached to the claim does not visibly change while its meaning collapses.

In practice this means reading every reliability figure with its quantifier stapled on. Availability per request is not availability per user session of forty requests. A suite whose tests each fail one time in a thousand is not a suite that passes. Eventual consistency is a statement about limits with no content about the read you are about to serve. A bound that holds in expectation constrains no particular execution, so it cannot answer a question about this execution. And in the other direction, an aggregate is simply the wrong instrument for a decision about one case: no amount of correct fleet-level statistics tells you whether this transaction settled. The repair is cheap and mechanical — state the scope inside the guarantee, and when the scope changes, recompute rather than reuse.

**Source:** [Grundbegriffe der Wahrscheinlichkeitsrechnung](../works/grundbegriffe-der-wahrscheinlichkeitsrechnung.md) — Chapter I, §2, Remark 1 on the conjunction of practically reliable statements failing to give practical reliability of all when the number is large, hence the frequency principle not extending across many series, and Remark 2 on probability zero implying practical impossibility only for a single realization while permitting occurrence in a sufficiently long series.
