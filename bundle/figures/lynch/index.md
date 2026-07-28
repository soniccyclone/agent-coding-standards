---
type: figure
title: Nancy Lynch
description: b. 1948, MIT. Co-author of the FLP impossibility proof; author of Distributed Algorithms, the field's standard formal-methods textbook.
status: accepted
layer: implementation-mapping
subdomains: [distributed-systems-and-concurrency]
tags: [figure, accepted]
---

# Nancy Lynch

**Dates:** b. 1948. NEC Professor of Software Science and Engineering at MIT, heads the Theory of Distributed Systems group at CSAIL.

## Why a candidate
Co-author of the FLP impossibility proof and author of *Distributed Algorithms*, the field's standard formal-methods textbook — arguably the single most systematic academic formalization of the subdomain.

## Top 10 most influential works
1. "Impossibility of Distributed Consensus with One Faulty Process" (1985, with Fischer, Paterson) — `public` (self-archived at MIT CSAIL)
2. "Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services" (2002, with Gilbert) — `public` (self-archived/course-mirrored)
3. *Distributed Algorithms* (1996, textbook) — `paywalled` (Internet Archive controlled lending)
4. "An Introduction to Input/Output Automata" (1989, with Tuttle) — `uncertain`
5. "Consensus in the Presence of Partial Synchrony" (1988, with Dwork, Stockmeyer) — `uncertain`
6. "Reaching Approximate Agreement in the Presence of Faults" (1986, with Dolev, Pinter, Stark, Weihl) — `uncertain`
7. *Atomic Transactions* (1993, book with Merritt, Weihl, Wing) — `paywalled`

## Phase 3 access flag
*Distributed Algorithms* (1996) — the textbook explicitly named in this
figure's "why a candidate" case — has no open-access full text anywhere.
The TDS group's official book page
(http://groups.csail.mit.edu/tds/distalgs.html) offers only a
table-of-contents postscript and a link to buy the Morgan
Kaufmann/Elsevier edition; no self-archived PDF exists on Lynch's own
pages or MIT CSAIL's group site (checked directly, no Wayback snapshot of
a full text either). The only free-to-read copy located is Internet
Archive's controlled-lending scan
(https://archive.org/details/distributedalgor0000lync), which requires an
account, a borrow queue, and in-browser DRM — not public access per this
pass's rules. *Atomic Transactions* (1993) is in the same position
(TOC-only page at http://groups.csail.mit.edu/tds/atomictrans.html, same
IA controlled-lending scan as the only free copy) but isn't named in the
why-candidate case, so it's excluded without a flag — see Phase 3 report.

## Lessons

Lynch's body of work teaches that a distributed system is only as
trustworthy as the model it was proved in, and that the model is where the
engineering actually happens. Her method is to make specifications and
implementations the same kind of mathematical object so correctness reduces
to containment, to insist that any composition operator preserve the
reasoning you carried across it, and to define a component by what it cannot
refuse and by the obligation never to be the first to break a shared
invariant — then to reason forward over the set of outcomes still reachable
rather than backward over the history that produced the current state. On top
of that machinery sits a sharp discipline about assumptions. Correctness can
only rest on distinctions a participant is actually able to draw, so a
fault-tolerance claim means nothing until you say when the faults may occur,
a slow participant must never be laundered into a broken one, and every
timing assumption belongs in the liveness obligation and none of it in the
safety obligation. Her impossibility results are meant to be read as
itemized invoices rather than walls: each one names a modeling power the
adversary was granted, and the productive response is to buy that power back
where it is cheap (local timers, eventual stabilization), to weaken exactness
rather than the model when closeness is genuinely what the caller needs, or
to write the degraded mode down as a real, quantified specification instead
of declaring a tradeoff and letting the fallback path go unspecified. Where
she builds, she builds in layers — solve the problem in the model you wish
you had and discharge that model once in a replaceable simulation — and she
prefers properties you can compute with: a spread that provably contracts
each round, a filter width derived from how far two honest views can diverge,
a quorum whose intersection is the thing actually buying safety.
