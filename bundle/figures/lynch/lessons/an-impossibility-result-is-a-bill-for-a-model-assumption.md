---
type: lesson
title: "An impossibility result is an invoice for a model assumption, so learn to read which assumption it is charging you for"
figure: lynch
works: [brewers-conjecture-and-the-feasibility-of-consistent-available-partition-tolerant-web-services]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [distributed-systems-and-concurrency, databases-and-data-management]
tags: [lesson]
---
# An impossibility result is an invoice for a model assumption, so learn to read which assumption it is charging you for

A negative theorem feels like a wall, and engineers tend to treat it as one: the properties are incompatible, pick two, move on. That reading throws away most of the information. Every impossibility proof is parameterized by a system model, and the proof consumes specific powers that the model denied the algorithm. The productive question is never "which property do I sacrifice" but "which modeling assumption did the proof spend, and can I buy it back?" The same three desirable properties stay jointly unachievable across two different models here, yet what is achievable *underneath* the impossibility changes completely between them — because the two proofs draw on different powers of the adversary.

The demonstration is in the gap between the asynchronous corollary and its partially synchronous counterpart. Asynchronously, you cannot even promise the weaker thing of behaving consistently whenever the network happens to cooperate, and the reason is epistemic rather than architectural: a process with no clock cannot separate a message that will never arrive from one that is merely slow, so any behavior it can produce under loss it can also produce under delay, and a guarantee conditioned on "no loss occurred" is unwritable. Grant every process a local timer that merely advances at a common rate — not synchronized clocks, not shared time, just a way to notice that an interval has elapsed — and that particular corollary evaporates while the headline theorem survives untouched. Timeouts do not defeat the impossibility. They restore the ability to *condition on* a failure, which is a different and cheaper thing to want.

A programmer who internalizes this stops shopping for tradeoffs and starts auditing proofs. Before conceding a guarantee, they locate the exact step where the adversary wins and ask what the adversary was allowed to do there: reorder, delay indefinitely, drop silently, lie. Then they check what their real deployment actually permits and what a small addition to the model would cost. Very often the honest impossibility is narrower than the folklore version, and the narrow version leaves a design worth building — as here, where the theorem forbids consistency under partition but says nothing against a system that is fully consistent whenever the network is healthy and knows, locally, when it has stopped being so.

**Source:** [Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services](../works/brewers-conjecture-and-the-feasibility-of-consistent-available-partition-tolerant-web-services.md) — the thinking lives in the contrast between the asynchronous corollary (which extends the impossibility even to loss-free runs, arguing from a process's inability to distinguish loss from delay) and the later section showing that this extension, unlike the main theorem, fails once nodes have local timers.
