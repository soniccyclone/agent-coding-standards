---
type: work
title: "Algorithms and Data Structures"
figure: wirth
description: A textbook built on the thesis that a program is inseparable from the data structures it manipulates, working through sorting, searching, recursion, dynamic data structures, and language-level abstractions like sets and files as a unified design vocabulary rather than a grab-bag of techniques. Originally published in 1976 as "Algorithms + Data Structures = Programs" using Pascal, then revised over successive editions; the self-archived copy is the later revision recast around Oberon. It functioned as a primary teaching text translating Wirth's stepwise-refinement philosophy into concrete algorithmic practice.
subdomains: [algorithms-and-complexity]
year: 1976 (Oberon revision: 2004)
url: https://people.inf.ethz.ch/wirth/AD.pdf
survey_pages: 212
survey_text_layer: full
survey_fetch_mb: 2
access: public
host: self-archived
tags: [work]
---

# Algorithms and Data Structures

**Venue/year:** Prentice-Hall, 1976, as "Algorithms + Data Structures = Programs" (Pascal). Revised edition "Algorithms and Data Structures," 1985 (Modula-2); self-archived PDF is the August 2004 Oberon-language revision.
**Source:** https://people.inf.ethz.ch/wirth/AD.pdf — live PDF, self-archived on Niklaus Wirth's ETH Zurich personal page.

## Lessons
- [Buy mechanization with a restriction on access, and expect it to redraw the algorithms](../lessons/buy-mechanization-with-a-restriction-on-access.md)
- [Separate the structure from the position in it, and give the position its own invariant](../lessons/separate-the-structure-from-the-position-in-it.md)
- [Pick the representation that turns the operations into machine primitives, then bound the abstraction to keep it](../lessons/pick-the-representation-that-turns-the-operations-into-machine-primitives.md)
- [Admit to the foundation only what one representation can serve for nearly everyone](../lessons/admit-to-the-foundation-only-what-one-representation-can-serve.md)
- [Improve the dominant term or do not call it an improvement](../lessons/improve-the-dominant-term-or-do-not-call-it-an-improvement.md)
- [When a method hits its floor, find what each step computes and throws away](../lessons/find-what-each-step-throws-away.md)
- [Repair the part that broke its own contract; weakening the requirement instead has to be priced out loud](../lessons/repair-the-part-that-broke-its-own-contract.md)
- [Encode the live set in the arrangement, so the hot loop has nothing to test](../lessons/encode-the-live-set-in-the-arrangement.md)
- [Let the shape of the definition decide recursion or iteration, and prove the depth is small](../lessons/let-the-shape-of-the-definition-decide-recursion-or-iteration.md)
- [Put the degenerate case inside the operation, and postpone the optimization that moves it out](../lessons/put-the-degenerate-case-inside-the-operation.md)
- [The more demanding specification can be the simpler program](../lessons/the-more-demanding-specification-can-be-the-simpler-program.md)
- [An exhaustive search still has a preference, and it belongs to whoever drives the outer loop](../lessons/an-exhaustive-search-still-has-a-preference.md)
- [Find the data counterpart of every control construct, then carry the discipline across with it](../lessons/find-the-data-counterpart-of-every-control-construct.md)
- [Sharing is only observable under update, which is exactly why it has to be sayable](../lessons/sharing-is-only-observable-under-update-so-make-it-sayable.md)
- [Guarantee the answer exists, then ask where it was found](../lessons/guarantee-the-answer-exists-then-ask-where-it-was-found.md)
- [A gain that grows with size is marking the structure's ceiling, not raising it](../lessons/a-gain-that-grows-with-size-is-marking-the-structures-ceiling.md)
- [Represent each direction of a relation by the question asked of it, not by symmetry](../lessons/represent-each-direction-of-a-relation-by-the-question-asked-of-it.md)
- [Let the progress counter be the precondition check, and know what it cannot tell you](../lessons/let-the-progress-counter-be-the-precondition-check.md)
- [Competing notations are usually traversal orders of one structure](../lessons/competing-notations-are-usually-traversal-orders-of-one-structure.md)
- [Decide whether an operation needs the value or the place, and let the interface say which](../lessons/decide-whether-the-operation-needs-the-value-or-the-place.md)
- [Compute the distance to the ideal first; it is the entire budget for the fix](../lessons/compute-the-distance-to-the-ideal-it-is-the-budget-for-the-fix.md)
- [Weaken the invariant until restoring it is cheap, but not past the point where it still bounds the worst case](../lessons/weaken-the-invariant-until-restoring-it-is-cheap.md)
- [Move the contents to a position where the operation is easy](../lessons/move-the-contents-to-a-position-where-the-operation-is-easy.md)
- [Small bookkeeping is charged at the layout's rate, not at its size](../lessons/small-bookkeeping-is-charged-at-the-layouts-rate.md)
- [Worst case decides admissibility; expected case decides the choice](../lessons/worst-case-decides-admissibility-expected-case-decides-choice.md)
- [Optimality is relative to an access model, and the misses belong in it](../lessons/optimality-is-relative-to-an-access-model-and-the-misses-count.md)
- [Every speedup is bought with a claim; name the claim and notice when you stop proving it](../lessons/every-speedup-is-bought-with-a-claim-name-the-claim.md)
- [Match the structure's granularity to the transfer unit, then re-derive the cost](../lessons/match-the-structures-granularity-to-the-transfer-unit.md)
- [Same shape is not same meaning: keep roles distinct even when the picture collapses them](../lessons/same-shape-is-not-same-meaning.md)
- [When a repair forces an expensive access, take everything it offers — and check the opposite repair is its mirror](../lessons/pay-once-take-everything-and-keep-repair-symmetric.md)
- [Examine the degenerate instance, and when you re-represent it keep only the distinction that mattered](../lessons/examine-the-degenerate-instance-and-keep-only-the-distinction.md)
- [Restate the rule as the property you actually need, and drop the concept you arrived by](../lessons/restate-the-rule-as-the-property-you-need-and-drop-the-scaffolding.md)
- [An attribute of a connection can live at either end; pick the end with fewer connections](../lessons/store-an-edges-attribute-at-the-endpoint-with-fewer-edges.md)
- [Every invariant spends the freedom that performance was buying](../lessons/every-invariant-spends-the-freedom-performance-was-buying.md)
- [Partition the key space, not the data, and the structure stops depending on its history](../lessons/partition-the-key-space-not-the-data.md)
- [Measure the whole task, not the operation you benchmarked](../lessons/measure-the-whole-task-not-the-operation-you-benchmarked.md)
- [Uniformity is a property of the function and the population together](../lessons/uniformity-is-a-property-of-the-function-and-the-population-together.md)
- [Find the ratio that governs behaviour, not the magnitude](../lessons/find-the-ratio-that-governs-behaviour-not-the-magnitude.md)
- [A computed location is a hypothesis, not an answer](../lessons/a-computed-location-is-a-hypothesis-not-an-answer.md)
- [A structure is defined by its selectors, not by the set of values it can hold](../lessons/a-structure-is-defined-by-its-selectors.md)
- [Name the gap between the type and the reality, and say who is holding it](../lessons/name-the-gap-between-the-type-and-the-reality.md)
- [A buffer absorbs variance, not a difference in rate](../lessons/a-buffer-absorbs-variance-not-a-difference-in-rate.md)
- [Classify an unmet condition as a caller's error, an implementation's limit, or a wait — before you choose how to report it](../lessons/classify-an-unmet-condition-before-choosing-how-to-report-it.md)
- [An idle participant that polls is competing with the one making progress](../lessons/an-idle-participant-that-polls-is-competing-with-the-one-making-progress.md)
- [You can write by naming the type, but you cannot read by naming it](../lessons/you-can-write-by-naming-the-type-but-you-cannot-read-by-naming-it.md)
- [A condition that fires once should not be tested on every step](../lessons/a-condition-that-fires-once-should-not-be-tested-every-step.md)
- [Keep the redundancy that exhibits the correspondence to the algorithm you already trust](../lessons/keep-the-redundancy-that-exhibits-the-correspondence.md)
- [When an optimization forces two loops together, give each advance its own guard](../lessons/when-an-optimization-forces-two-loops-together-give-each-advance-its-own-guard.md)
- [Two optimizations that each win do not compose into a win](../lessons/two-optimizations-that-each-win-do-not-compose-into-a-win.md)
- [Monotone access is a separate deliverable from the cost bound](../lessons/monotone-access-is-a-separate-deliverable-from-the-cost-bound.md)
- [Choose passes that preserve each other's work — and that overlap](../lessons/choose-passes-that-preserve-each-others-work-and-that-overlap.md)
- [Find the phase that moves data without changing the invariant, and fuse it away](../lessons/find-the-phase-that-moves-data-without-changing-the-invariant.md)
- [If you need one part of the answer, descend into one part only](../lessons/if-you-need-one-part-of-the-answer-descend-into-one-part-only.md)
- [When the algorithm needs lookahead, extend the access mechanism rather than the algorithm](../lessons/when-the-algorithm-needs-lookahead-extend-the-access-mechanism-not-the-algorithm.md)
- [Prefer a design whose correctness does not depend on a count you cannot reliably track](../lessons/prefer-a-design-whose-correctness-does-not-depend-on-a-count.md)
- [When both halves want to be the caller, neither should be](../lessons/when-both-halves-want-to-be-the-caller-neither-should-be.md)
