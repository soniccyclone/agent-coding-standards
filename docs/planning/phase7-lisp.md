---
type: record
title: DISTILLED-LISP.md — Selection Notes and Leftovers
description: Why the Lisp-tradition document exists, the through-line its author found, the cross-document tension it had to handle, and the claims it could not fit. Written 2026-08-03.
tags: [phase7, distillation, lisp, okf]
---

# DISTILLED-LISP.md — Notes and Leftovers

## Why it exists

Phase 7's main pass sliced the corpus by subdomain and fanned out ten agents. It
produced a good document and almost entirely lost the Lisp tradition. McCarthy was
nominated zero times despite 29 lessons; Sussman was the second-most-nominated
figure in the whole corpus and went 1-for-9 at the strike pass, with every survivor
a tactic about concurrency or retries.

Two causes, and the second is the interesting one. Lisp thinking is a stance that
cuts across every subdomain, so sliced nine ways it belonged to no slice and each
fragment looked minor. And each slice was judged through an Algol-family lens, in
which "build the notation up toward the problem" reads as over-engineering. Almost
all training code is Algol-descended, so that lineage's instincts arrive feeling
like neutral engineering judgement rather than one tradition's answers.

The fix was structural: one agent holding the whole tradition at once, no chunking,
explicitly briefed on the bias it was there to correct. Nathan's call, and correct.

## The through-line, which was not the one I proposed

I gave the agent a starting hypothesis (notation upward, evaluator as design tool,
program/data boundary as a choice) and told it the sketch might be shallow. It
found something better: **the difference between having a capability and having
earned it**, made testable by four instruments — locality of encoding (Steele),
size of the diff for anticipated change (McCarthy), what a model states versus
inherits (Reynolds), and the marginal cost of the Nth addition (Ingalls).

"Build the notation up toward the problem" is the consequence of those tests, not
the claim itself. That distinction is what keeps the document from being advocacy.

Its own assessment of the most decision-changing claim in the set: the seam
(Steele, Kay, Ingalls), because agents build plugin APIs weaker than their own core
as a reflex.

## A genuine cross-document tension

`bundle/DISTILLED.md` carries Pike: treat a request for hooks, plugins, config
knobs, or a DSL as a measurement of friction in the underlying primitives. That is
the Algol-lens read and it conflicts with Steele.

The agent resolved it with a guard paragraph rather than routing around it: extend
the vocabulary you already write in, and do not bolt a config layer beside your
code. Pike's target is the parallel mechanism; Steele's is the vocabulary itself.
That is an honest reconciliation and it holds, but a later pass may want to name
the disagreement outright and open a proper `tension` file. It is exactly the shape
Phase 5 exists for, and it was found after Phase 5 closed.

## Found, judged important, could not fit

Recorded verbatim in substance from the writing agent. Several are strong enough
that a future re-distillation should start here rather than re-derive them.

1. **Backus — the width of a system's interface to its state bounds what changes
   are thinkable.** A program talking to state through many bespoke channels
   forecloses whole-state transformation entirely. Backus has zero citations in
   either document, which is a real gap; this is the claim to close it with.

2. **Steele — when requests form a family, ship the generator, not the members.** A
   backlog of individually reasonable, jointly unaffordable requests is diagnostic
   rather than a prioritisation problem. Sort by shape, find the largest
   isomorphism class, and test the generator by whether the user-built result is as
   good as the built-in would have been. If it is worse, you declined the problem
   while appearing to solve it. Cut purely for length; among the strongest claims
   in the corpus.

3. **McCarthy — the fast artifact is a cache; changes enter through the
   definitions.** For every build product, generated client, vendored bundle or
   lockfile: which file is the input, and is the derived thing reachable by a
   command anyone can run? Hand-edited even once, the derived artifact silently
   became the source.

4. **Sussman — deferring a choice and turning it into data are different moves.**
   Deferral has a deadline; per-value tagging does not. Once two representations
   share a shape, meaning must be carried explicitly or it is gone, which is what a
   type tag actually is. The disciplined version of "make it data", and the anchor
   for a section on when not to.

5. **McCarthy — the regime split on declarative versus imperative extension.**
   Small, hot, self-contained, no prior context: write the procedure. Large,
   long-lived, many contributors: state facts. Cut for space, and the document is
   slightly less honest without the counterweight.

6. **Kay — progress is moving decisions later, with the fast-path-plus-trap
   technique.** The standing answer to the efficiency objection against late
   binding: arrange the common case to run at full speed under a cheap check that
   diverts only on unusual operands.

7. **Landin — translation is a diagnostic instrument.** Every adapter, serializer
   and interop layer is a report on the thing being adapted. A threaded mutable
   context names what the source leaves implicit, and combinations the target
   admits but the source refuses are free design leads.

8. **An unrepresented cluster: judge an abstraction by what it lets you prove,
   not by what it lets you write.** Reynolds on a blocked proof step signalling a
   too-weak specification; Strachey on judging a semantics by the equalities it
   establishes. Nothing in either document covers this.
