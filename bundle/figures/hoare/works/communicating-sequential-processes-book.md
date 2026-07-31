---
type: work
title: "Communicating Sequential Processes"
figure: hoare
description: The full book-length treatment of CSP, developing a process algebra where concurrent systems are built from sequential processes that interact only through synchronized, unbuffered message-passing events. Works through the algebraic laws for composing processes, traces as a model of process behavior, and worked examples ranging from simple buffers to concurrent scheduling problems. Hoare made an updated electronic version freely distributable after the original Prentice Hall edition went out of print.
subdomains: [distributed-systems-and-concurrency]
year: 1985 (revised through 2015)
url: http://web.archive.org/web/20250104082500/http://www.usingcsp.com/cspbook.pdf
survey_pages: 260
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: self-archived
tags: [work]
---

# Communicating Sequential Processes

**Venue/year:** Originally Prentice Hall International, 1985. Revised electronic edition maintained by Hoare (with Jim Davies) through at least 2015.
**Source:** http://web.archive.org/web/20250104082500/http://www.usingcsp.com/cspbook.pdf — the live site (usingcsp.com) is currently unresolvable (DNS failure at time of check), so this is a Wayback Machine snapshot from January 2025. Content verified by decompressing the PDF's text streams directly: title page reads "Communicating Sequential Processes / C. A. R. Hoare," and a copyright page states "© C. A. R. Hoare, 1985–2022. This document is an electronic version of..." confirming it as Hoare's own authorized free distribution (self-archived, not a third party's copy).

**Coverage note (partial extraction — NOT exhausted):** A 260-page book; one Phase 4
pass could not reach the end. Read in full and mined: the foreword and preface, and
Chapter 1 (Processes) sections 1.1 (introduction, prefix, recursion, choice, mutual
recursion), 1.2 (pictures), 1.3 (laws), and 1.4 (implementation of processes) up to
the interactive-explorer function. **Not read at all:** the remainder of Chapter 1
(1.5 traces onward, 1.6-1.10 including specifications and the `sat` proof rules),
and Chapters 2-7 in their entirety — concurrency, nondeterminism, communication,
sequential processes, shared resources, and discussion. That is roughly 85% of the
book.

To resume, use `pdftotext -layout` on the URL above and **start at line 1540** of the
resulting text (mid-section 1.4, just after the `interact` function is introduced).
Page markers are absent; the text runs to line 12215. Chapter 2 (Concurrency) begins
around line 2830 — locate chapter and section boundaries by grepping the running
heads and section numbers (e.g. `2   Concurrency`, `^2\.3`), since the PDF's own page
numbers appear inline in those running heads.

**READ IN PROGRESS (2026-07-31):** a second Phase 4 pass has resumed at line 1540 of
the `pdftotext -layout` output (12215 lines total) and is working forward
sequentially. This line is updated as the read advances; if it still says 1540 the
pass died immediately. Current position: **line 10980** — Chapters 1 (from 1.5),
2, 3, 4, 5 and 6 read in full; Chapter 7 read through 7.2.4 (start).

## Lessons
- [What a thing could do is part of what it is: fix the vocabulary of possible interactions before describing behaviour](../lessons/declared-capability-is-part-of-identity.md)
- [Make the awkward question unaskable rather than answering it carefully: drop time, keep order](../lessons/make-the-question-unaskable-rather-than-answering-it-carefully.md)
- [A self-referential definition means something only if it commits to an observable step before referring to itself](../lessons/a-self-referential-definition-must-commit-to-a-step-first.md)
- [Model an interaction by who holds the choice: input and output differ in nothing else](../lessons/model-an-interaction-by-who-holds-the-choice.md)
- [Refuse the syntax that would let nonsense be written, then find the one general form the rest are special cases of](../lessons/deny-the-syntax-that-would-let-you-write-nonsense.md)
- [Find the form every term reduces to: it is what makes the laws few and the implementation direct](../lessons/a-normal-form-is-what-makes-laws-and-implementation-cheap.md)
- [Pictures build intuition but cannot carry an argument, and they fail exactly where the system gets interesting](../lessons/pictures-build-intuition-but-cannot-carry-an-argument.md)
- [Attack an intractable problem with a model too small to be fair to it, then add back only what proves necessary](../lessons/attack-an-intractable-problem-with-a-model-too-small-to-be-fair.md)
- [Let breakdown show up as the absence of any continuation rather than as a distinguished event](../lessons/failure-shows-up-as-the-absence-of-a-continuation.md)
- [Make an operation distribute over composition and you need only define it on the atoms](../lessons/make-an-operation-distribute-and-you-need-only-define-it-on-atoms.md)
- [A new operator can silently invalidate the well-formedness test every other definition depends on](../lessons/a-new-operator-can-silently-invalidate-your-well-formedness-test.md)
- [Write down the closure conditions your observation-set satisfies; they may turn out to be the whole structure](../lessons/the-closure-conditions-on-your-observations-may-be-the-whole-structure.md)
- [A specification made only of prohibitions is satisfied by doing nothing, and no amount of tightening fixes that](../lessons/a-specification-made-only-of-prohibitions-is-satisfied-by-doing-nothing.md)
- [Make coupling a parameter of the participants, not a choice of construct](../lessons/make-coupling-a-parameter-not-a-construct.md)
- [Composition intersects possibilities, so a stuck system need not contain a faulty part](../lessons/composition-intersects-possibilities-so-stuckness-has-no-owner.md)
- [Refuse to distinguish a component from its environment, and make the joining operator closed, symmetric and associative](../lessons/refuse-to-distinguish-a-component-from-its-environment.md)
- [Express a global policy as an extra participant that adds no actions of its own and can therefore only forbid](../lessons/express-a-global-policy-as-a-participant-that-only-forbids.md)
- [Before betting on exhaustive search, work out whether you would be enumerating configurations or histories](../lessons/enumerating-configurations-versus-enumerating-histories.md)
- [Where interaction is by name-matching, two copies of a thing are one thing until you rename them](../lessons/naming-is-wiring-so-instantiation-is-renaming.md)
- [When state is a participant, reading it is a forced case analysis — and if reading requires acting, a repair obligation too](../lessons/reading-state-as-a-case-analysis-and-a-repair-obligation.md)
- [When you know a generalization is coming, refuse to state the laws it will break](../lessons/dont-state-the-laws-your-planned-generalization-will-break.md)
- [Existence and uniqueness of a solution are bought by different properties — know which one you actually need](../lessons/existence-and-uniqueness-are-bought-by-different-properties.md)
- [A law about a specification constrains the set of permitted implementations, not any single one](../lessons/a-law-about-a-specification-constrains-the-set-of-implementations.md)
- [Replace "eventually" with a bound, because no finite observation can ever refute an unbounded promise](../lessons/replace-eventually-with-a-bound-you-can-observe.md)
- [Deferring a choice costs the upkeep of every option you kept open, for as long as they stay indistinguishable](../lessons/deferring-a-choice-costs-the-upkeep-of-every-option.md)
- [Choosing once and choosing every time round are different systems, and the loop is exactly where distribution fails](../lessons/choosing-once-versus-choosing-every-time-round.md)
- [Nondeterminism in a model is the shadow of what you chose not to observe, which makes it a control rather than an affliction](../lessons/nondeterminism-is-the-shadow-of-what-you-chose-not-to-observe.md)
- [When two designs you must distinguish look identical, find the discriminating situation and let it name the missing observable](../lessons/when-two-designs-look-identical-extend-what-you-record.md)
- [Hidden internal activity that never finishes is indistinguishable from being hung, so hiding obliges you to bound it](../lessons/hidden-activity-that-never-finishes-is-indistinguishable-from-being-hung.md)
- [If a property is inexpressible, enrich what you observe rather than reaching for a second logic](../lessons/if-a-property-is-inexpressible-enrich-what-you-observe.md)
- [Pooling interchangeable units buys capacity and spends addressability, in one transaction](../lessons/pooling-buys-capacity-and-spends-addressability.md)
- [To prove something cannot happen, build a model in which it can](../lessons/to-prove-something-cannot-happen-model-it-happening.md)
- [Define "better" as "more predictable", and let implementation be a walk up that order](../lessons/define-better-as-more-predictable-and-implement-upward.md)
- [When the latency is waiting, widen what you are willing to accept — speed cannot help you](../lessons/when-latency-is-waiting-widen-what-you-accept.md)
- [Specify a stream component as a relation between its channel histories, plus a bound on how far behind it may fall](../lessons/specify-a-stream-component-by-history-relation-plus-lag-bound.md)
- [Coarsen the model to exactly the property you are proving, and structural certificates appear](../lessons/coarsen-the-model-to-the-property-you-are-proving.md)
- [Let the rate budget fix how many components there are, and the formula's own shape fix how they are wired](../lessons/let-the-rate-budget-fix-the-component-count-and-the-formula-fix-the-wiring.md)
- [When two structures each demand to be the outer loop, give each its own and connect them](../lessons/when-two-structures-demand-the-outer-loop-give-each-its-own.md)
- [A restricted combinator earns its keep with a simpler law — and trades one hazard for another you must name](../lessons/a-restricted-combinator-earns-its-keep-with-a-simpler-law.md)
- [Define a fault-masking layer's correctness as indistinguishability from the ideal component it imitates](../lessons/define-a-masking-layer-by-the-ideal-component-it-imitates.md)
- [Design in nested layers, deploy as two stacks, and let associativity be what licenses the regrouping](../lessons/design-in-nested-layers-deploy-as-stacks-and-let-associativity-license-it.md)
- [Multiplexing independent streams couples them, buffering only postpones the coupling, and per-stream backpressure is the only cure](../lessons/multiplexing-couples-independent-streams-and-only-backpressure-uncouples-them.md)
- [A recursively subordinated process and an unbounded data structure are one construction, held together by local naming](../lessons/a-recursively-subordinated-process-is-an-unbounded-data-structure.md)
- [Where a notation forces you to commit is what determines the class of things it can recognize](../lessons/where-a-notation-forces-you-to-commit-determines-what-it-can-recognize.md)
- [Run independent constraint-checkers side by side and you enforce conjunctions no single traversal can](../lessons/run-independent-checkers-side-by-side-to-enforce-conjunctions.md)
- [Make restart, rollback and task-switching operators over a component that knows nothing about them](../lessons/make-recovery-an-operator-over-a-component-that-knows-nothing-about-it.md)
- [Choose between two adequate models by the laws you need to hold, not by which can mimic the behaviour](../lessons/choose-between-adequate-models-by-the-laws-you-need.md)
- [Declare each participant's read and write sets; their disjointness is what licenses moving code across the concurrency boundary](../lessons/declare-read-and-write-sets-and-disjointness-licenses-code-motion.md)
- [Partial operations invalidate the laws you rewrite with, so carry a definedness condition rather than pretending undefined is a value](../lessons/partial-operations-invalidate-your-laws-so-guard-each-law-with-definedness.md)
- [Derive a loop's termination precondition by parameterizing on "finishes within n" — the union over n is exactly the precondition](../lessons/derive-the-termination-precondition-rather-than-assuming-it.md)
- [Check a general framework by what it degenerates to, and charge its extra notation only to the general case](../lessons/check-a-generalization-by-what-it-degenerates-to.md)
- [Deadlock is a shape in the state space — a concavity in the forbidden region facing the start — and the cure is to enlarge the forbidden region](../lessons/deadlock-is-a-concavity-in-the-forbidden-region.md)
- [Share purpose-built resources whose operations are already atomic, never general storage guarded by a convention](../lessons/share-purpose-built-resources-not-storage.md)
- [Let the act of acquiring an anonymous instance bind the identity of the one you got](../lessons/let-acquisition-bind-the-identity-of-what-you-got.md)
- [Enforce a discipline through an interface so pleasant that nobody wants an escape hatch](../lessons/enforce-discipline-through-an-interface-nobody-wants-to-bypass.md)
- [Make the degree of concurrency a parameter that leaves the specification unchanged](../lessons/make-the-degree-of-concurrency-a-spec-preserving-parameter.md)
- [You cannot schedule what you cannot see waiting: split the atomic acquire into a request and a grant](../lessons/you-cannot-schedule-what-you-cannot-see-waiting.md)
- [Measure modularity by listing prospective changes and counting the modules each touches — including the ones that come out badly](../lessons/measure-modularity-by-listing-changes-and-counting-modules.md)
- [An access restriction is what turns polling into event-driven re-evaluation](../lessons/an-access-restriction-turns-polling-into-event-driven-reevaluation.md)
- [Performance controls should be annotations that cannot change meaning, so they can be tuned by experiment](../lessons/performance-controls-must-not-be-able-to-change-meaning.md)
- [The mark of a successful abstraction is that it admits several implementations, each efficient in different circumstances](../lessons/a-successful-abstraction-admits-several-implementations.md)
- [In a cyclic network, buffer capacity is a semantic parameter, and behaviour can depend on it non-monotonically](../lessons/buffer-capacity-is-a-semantic-parameter-in-a-cyclic-network.md)
- [If the replacement formalism turns out just as complicated, the complication belonged to the problem and not to the notation you rejected](../lessons/if-the-replacement-formalism-is-just-as-complicated-the-complication-was-real.md)
- [A timeout is an admission of unmodelled failure, and in a model without time it can only appear as pure nondeterminism](../lessons/a-timeout-is-an-admission-of-unmodelled-failure-and-reads-as-nondeterminism.md)
- [A feature's real meaning is whatever the optimizer is permitted to assume about it, not what its syntax suggests](../lessons/a-features-meaning-is-what-the-optimizer-is-permitted-to-assume-about-it.md)
