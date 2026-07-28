---
type: lesson
title: "Keep correctness claims and performance claims in separate ledgers"
figure: saltzer
works: [end-to-end-arguments-in-system-design]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# Keep correctness claims and performance claims in separate ledgers

**Lesson:** Most architectural arguments go bad at the moment two different kinds
of justification get mixed in one sentence. "We need this in the lower layer"
sounds like one claim but is usually two: a claim that the system is incorrect
without it, and a claim that the system is slow without it. These have completely
different consequences. A correctness need fixes the location of the function and
admits no negotiation. A performance need is a tunable quantity, settled by
measurement, and it is legitimate to satisfy it partway, badly, or not at all.
Once you insist on labelling which one you are making, whole categories of design
dispute dissolve, because the participants discover they were not disagreeing about
the same thing.

The discipline matters more than it sounds, because a performance justification
smuggled in as a correctness justification is very hard to retire later. Labelled
as correctness, the mechanism becomes load-bearing and nobody dares remove it. This
work's own treatment of the effort budget for lower-layer reliability shows the
right handling of the honest version: since the outer check must exist regardless,
the inner effort is bought only up to the point where the outer retry rate becomes
tolerable, and there is nothing to be gained by pushing past it. Striving for a
negligible failure rate below the level that actually adjudicates correctness is
work spent on a number nobody depends on.

There is a second trap on the performance side alone, and it cuts against the
reflex that lower is faster. A shared lower layer charges every client for the
function, including the clients that do not want it and the ones actively harmed by
it — the real-time case where added delay is worse than the error the delay
prevents. And the lower layer is working with less information, so its version of
an optimization can be genuinely worse than the one the application could have
written. So even the pure efficiency argument for pushing function downward has to
be established rather than assumed, case by case, with knowledge of the whole
system.

A programmer holding this distinction writes down, for each mechanism they inherit
or add, which ledger it is in. That single annotation tells them whether the
mechanism can be tuned, weakened, made optional, or deleted when the workload
changes — and prevents the far more common outcome, where an optimization ossifies
into an invariant because nobody remembers which it was.

**Source:** [End-to-End Arguments in System Design](../works/end-to-end-arguments-in-system-design.md)
— the performance discussion following the file-transfer case study, where
lower-layer reliability effort is recast as an engineering tradeoff rather than a
requirement, together with the two stated reasons a low-level implementation can
cost more than a high-level one.
