---
type: lesson
title: "A checker that has never been seen to fire earns no trust; build a way to break the system on purpose"
figure: turing
works: [proposed-electronic-calculator-ace-report]
axes: [verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# A checker that has never been seen to fire earns no trust; build a way to break the system on purpose

**Lesson:** Checking machinery has an obligation people usually forget. Catching errors and localizing them are the two obvious jobs; the third is producing belief in the answers, and a checking system that silently succeeds delivers nothing on that third front. Worse, a silent checker and an absent checker are observationally identical, so a system whose checks have never visibly triggered gives you no evidence that they work at all — you cannot distinguish "nothing has gone wrong" from "the detector is dead." A correct system that nobody trusts gets its results second-guessed, recomputed by hand, or ignored, and the checking effort is wasted.

The fix is to make failure observable on demand: a facility for injecting a fault deliberately and watching the report come out. That converts the checking layer from an assertion into a demonstration, and it does so cheaply, because a way to disturb the machine from outside is far less work than a proof. Two related habits follow. Push components toward failure under conditions harsher than normal operation so the marginal ones declare themselves while there is still margin left, rather than waiting for the intermittent failures that ageing produces first. And when a new procedure is written, run the same job through a slower, more obviously-correct procedure and compare, since agreement between two independent routes is the only check that covers a mistake in your understanding of the problem rather than a fault in the machinery.

For a programmer this is the argument for fault injection, for exercising the alerting path rather than only the happy path, and for keeping a deliberately naive reference implementation around to cross-check the fast one. The test that matters is not "do the checks pass" but "have I seen these checks fail when they should" — and if you cannot make a check fail on demand, you do not yet know that you have a check. Confidence is a design requirement with its own mechanisms, not a mood that correctness produces on its own.

**Source:** [Proposed Electronic Calculator (Report on the ACE)](../works/proposed-electronic-calculator-ace-report.md) — the chapter on checking, which names inspiring confidence as one of three functions of the checking system, warns of a machine whose warnings nobody believes, proposes an artificial-error facility and stress test-runs, and recommends validating a new instruction table against a slower straightforward one.
