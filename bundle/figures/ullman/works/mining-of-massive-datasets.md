---
type: work
title: "Mining of Massive Datasets"
figure: ullman
description: A textbook, built out of Stanford's CS246/CS345A courses, covering the algorithmic side of large-scale data analysis — MapReduce, locality-sensitive hashing, stream algorithms, link analysis (PageRank), recommendation systems, clustering, and (in the 3rd edition) deep learning. Cambridge University Press returned the rights to the authors, who now give the full book away free rather than let it go out of print. It's the same "textbook as the mechanism for shaping how a subfield is taught" pattern as Ullman's earlier database books, just applied to data mining instead of relational/Datalog theory.
subdomains: [databases-and-data-management, algorithms-and-complexity]
year: 2020
url: http://infolab.stanford.edu/~ullman/mmds/book0n.pdf
survey_pages: 603
survey_text_layer: full
survey_fetch_mb: 3
access: public
host: self-archived
tags: [work]
---

# Mining of Massive Datasets

**Author(s):** Jure Leskovec, Anand Rajaraman, Jeffrey D. Ullman
**Venue/year:** 3rd edition, 2020 (1st ed. 2011, published by Cambridge University Press; rights reverted to the authors, who distribute it free by agreement with the publisher).
**Source:** http://infolab.stanford.edu/~ullman/mmds/book0n.pdf — live, self-archived full-book PDF (603 pp.) on Ullman's own Stanford InfoLab page, linked from the book's own site http://www.mmds.org (verified 200 via direct fetch).

## Lessons
- [Compute what randomness alone would hand you, before you trust any discovery](../lessons/compute-what-randomness-alone-would-hand-you.md)
- [Learn only the part of the problem you cannot state yourself](../lessons/learn-only-what-you-cannot-state-yourself.md)
- [Restartability is a shape you keep, not a feature you add](../lessons/restartability-is-a-shape-not-a-feature.md)
- [A cost model is a claim about which resource runs out first](../lessons/a-cost-model-is-a-claim-about-what-runs-out-first.md)
- [The dependency between inputs and outputs bounds what any parallel version can cost](../lessons/what-each-output-needs-bounds-what-parallelism-can-cost.md)
- [Compress so that one question survives exactly, not so the data gets smaller](../lessons/compress-so-that-one-question-survives-exactly.md)
- [Build the error curve you want by composing tests too weak to use alone](../lessons/build-the-error-curve-you-want-from-weak-tests.md)
- [Hold a signal out of the score so it can tell you what the score means](../lessons/hold-back-a-signal-to-calibrate-the-score.md)
- [Sample the entity your question quantifies over, not the records in front of you](../lessons/sample-the-entity-your-question-is-about.md)
- [How you combine independent estimates is part of the estimator, not a formality](../lessons/how-you-combine-estimates-is-part-of-the-estimator.md)
- [When the exact question is provably unaffordable, change the question](../lessons/when-the-exact-question-is-unaffordable-change-the-question.md)

- [Set the explainability requirement from who bears the decision and can contest it](../lessons/set-the-explainability-requirement-from-who-can-contest-the-decision.md)
- [Rank by concentration, because neither frequency nor rarity identifies signal](../lessons/rank-by-concentration-not-by-frequency-or-rarity.md)
- [Find which half of the problem is hard, because the deployed part is often trivial](../lessons/find-where-the-difficulty-lives-before-choosing-what-to-build.md)
- [When a field renames itself every decade, check whether the substance moved at all](../lessons/a-field-that-keeps-renaming-itself-is-telling-you-the-substance-held.md)
- [A randomizing function is only random relative to the input population you actually feed it](../lessons/a-randomizing-function-is-only-random-against-the-inputs-you-feed-it.md)
- [Learn to recognize your algorithm being performed without a computer](../lessons/learn-to-see-your-algorithm-being-performed-without-a-computer.md)

- [A metric survives adversaries only if the measured party doesn't own its inputs](../lessons/measure-with-signals-the-measured-party-does-not-control.md)
- [Peel away what violates your method's precondition, solve, then rebuild in reverse order](../lessons/delete-what-violates-the-precondition-then-rebuild-in-reverse.md)
- [Give a feedback process an exit that ignores its own structure](../lessons/give-the-process-an-exit-that-ignores-its-own-structure.md)
- [Store only what an invariant cannot recompute for you](../lessons/store-only-what-an-invariant-cannot-recompute.md)
- [Partition so that both ends of an update stay resident, and resend the cheap side](../lessons/partition-so-both-ends-of-the-update-stay-resident.md)
- [When per-entity customization is unaffordable, pick a basis and store coordinates](../lessons/when-per-entity-customization-is-unaffordable-pick-a-basis.md)
- [The constant you hardcoded is usually where the whole family of algorithms lives](../lessons/the-constant-you-hardcoded-is-where-the-family-lives.md)
- [Change what pays off instead of enumerating the shapes of the attack](../lessons/change-the-payoff-instead-of-enumerating-the-attack.md)
- [Run the same computation under two assumptions and treat the gap as the measurement](../lessons/run-the-same-computation-under-two-assumptions-and-read-the-gap.md)
- [Trust attaches to a channel, not to the entity that owns it](../lessons/trust-attaches-to-a-channel-not-to-an-entity.md)
- [When one score conflates two kinds of value, define them by mutual reference](../lessons/split-a-conflated-score-into-mutually-defining-roles.md)
- [Eliminating the intermediate can destroy the structure that made it cheap](../lessons/algebraic-simplification-can-destroy-the-structure-that-made-it-cheap.md)
- [The roles in a relation are the least constrained part of your model — try swapping them](../lessons/the-roles-in-a-relation-are-the-least-constrained-part-of-your-model.md)
- [Let the consumer's capacity to act set the threshold, then build on that assumption](../lessons/let-the-consumers-capacity-to-act-set-the-threshold.md)
- [Your bookkeeping, not your input, sets the problem size you can handle](../lessons/your-bookkeeping-not-your-input-sets-the-problem-size-you-can-handle.md)
- [The intervention you plan decides which correlation measure is the right one](../lessons/the-intervention-you-plan-decides-which-correlation-measure-is-right.md)
- [Find the closure property that turns exhaustive search into frontier expansion](../lessons/find-the-closure-property-that-turns-search-into-frontier-expansion.md)
- [Spend a phase's idle capacity on evidence the next phase can use](../lessons/spend-a-phases-idle-capacity-on-evidence-the-next-phase-can-use.md)
- [A test's guarantee covers only what the test actually examined](../lessons/a-tests-guarantee-covers-only-what-the-test-examined.md)
- [Independent filters sharing one budget have an interior optimum, not a monotone one](../lessons/independent-filters-sharing-one-budget-have-an-interior-optimum.md)
- [Make the cheap stage err in the direction the expensive stage can repair](../lessons/make-the-cheap-stage-err-in-the-direction-the-expensive-stage-can-fix.md)
- [Find the pigeonhole that makes a local test a complete filter for a global property](../lessons/find-the-pigeonhole-that-makes-a-local-test-a-complete-global-filter.md)
- [Certify that you missed nothing by counting the boundary of what you accepted](../lessons/certify-completeness-by-counting-the-boundary.md)
- [An update rule that can only demote needs a separate discovery path](../lessons/an-update-rule-that-only-demotes-needs-a-separate-discovery-path.md)
- [Check that your measure still discriminates at the scale you will use it](../lessons/check-that-your-measure-still-discriminates-at-your-scale.md)
- [Whether you can synthesize a summary is a property of the space, not of your algorithm](../lessons/whether-you-can-synthesize-a-summary-is-a-property-of-the-space.md)
- [When the stopping rule comes from outside, return the whole trajectory](../lessons/return-the-whole-trajectory-when-the-stopping-rule-is-external.md)
- [Store the form that composes, and derive the form you report](../lessons/store-the-form-that-composes-not-the-form-you-report.md)
- [Give observations tiers of commitment instead of forcing one decision](../lessons/give-observations-tiers-of-commitment-instead-of-one-decision.md)
- [When you cannot justify a level, watch the rate of change instead](../lessons/watch-the-rate-of-change-when-you-cannot-set-a-level.md)
- [Double until you overshoot, then bisect — searching for an unbounded unknown](../lessons/double-until-you-overshoot-then-bisect.md)
- [For coverage, greedily maximize the minimum — not the total](../lessons/for-coverage-maximize-the-minimum-not-the-total.md)
- [Make dimensions commensurable before you combine them, and set the threshold in meaningful units](../lessons/make-dimensions-commensurable-before-you-combine-them.md)
- [A single-point summary smuggles in an assumption about shape](../lessons/a-single-point-summary-smuggles-in-a-shape-assumption.md)
- [Let the decisions you will face decide what the summary keeps](../lessons/let-the-decisions-you-will-face-decide-what-the-summary-keeps.md)
- [An approximate model needs both a repair path and a coarsening path](../lessons/an-approximate-model-needs-a-repair-path-and-a-coarsening-path.md)
- [Keep history at geometrically decaying resolution](../lessons/keep-history-at-geometrically-decaying-resolution.md)

- [An estimate that decides what you observe will confirm itself](../lessons/an-estimate-that-decides-what-you-observe-will-confirm-itself.md)
- [Grade a procedure that must decide now against what hindsight could have done](../lessons/grade-irreversible-decisions-against-hindsight.md)
- [Close a guarantee from both sides, with a witness above and a structural argument below](../lessons/close-a-guarantee-from-both-sides-with-different-kinds-of-argument.md)
- [Spend from the deepest reserve, so the future still has someone who can serve it](../lessons/spend-from-the-deepest-reserve-to-keep-the-future-servable.md)
- [An ignored factor with no bound destroys a guarantee rather than degrading it](../lessons/an-ignored-unbounded-factor-destroys-a-guarantee-rather-than-degrading-it.md)
- [A worst-case guarantee is priced against an adversary — say who it is before you pay for it](../lessons/a-worst-case-guarantee-is-priced-against-an-adversary-name-them.md)
- [When the queries outlive the data, index the queries instead](../lessons/when-the-queries-outlive-the-data-index-the-queries.md)
- [Partitioning the channel is a proxy for knowing the requester](../lessons/partitioning-the-channel-is-a-proxy-for-knowing-the-requester.md)
- [The risk in derived personal data sits at the exit from automation, not at its collection](../lessons/the-risk-in-derived-personal-data-is-at-the-exit-from-automation.md)

- [Absence is not a value — keep 'unknown' distinct from 'lowest'](../lessons/absence-is-not-a-value-keep-unknown-distinct-from-zero.md)
- [Removing a constraint removes the work the constraint was silently doing](../lessons/removing-a-constraint-removes-the-work-it-was-doing.md)
- [State the weakest output that would satisfy the use, then choose the method](../lessons/state-the-weakest-output-that-would-satisfy-the-use.md)
- [The properties you can compute from an artifact are not the ones that matter about it](../lessons/computable-properties-of-an-artifact-are-not-its-meaningful-ones.md)

_EXTRACTION IN PROGRESS — this 603-page book is being hand-read in the main loop,
not by a subagent, because the enormous books need the top-level orchestrator.
Source text: `scratchpad/ullman/mmds.txt` (27,631 lines); chapter offsets in
`scratchpad/ullman/CHAPTERS.md`._

_Chapters 1-4 (pp. 1-174) had been read by an earlier agent pass, yielding the
lessons above the divider. **Chapter 1 was then re-read by hand on 2026-07-30 and
yielded six further lessons** (the six immediately above this note) — worth
recording as evidence about method: a careful second pass over 20 pages that were
already marked "read in full" found six ideas the first pass missed, and two more
that legitimately duplicated existing lessons and were dropped. One draft lesson on
aggressive summarization was written and then deleted as a genuine duplicate of
`compress-so-that-one-question-survives-exactly`, which makes the same claim from
the min-hashing chapter._

_Chapter 5 (link analysis, lines 8703-10453) was read in full on 2026-07-31,
yielding the eleven lessons below the second divider._

_Chapter 6 (frequent itemsets, lines 10454-12231) was read in full on 2026-07-31._

_Correction (2026-07-31, second agent pass): the "next unread line 12232" note
below was **stale**. Chapter 7 (clustering, lines 12232-14091) had in fact already
been read — the lessons on centroids-vs-clustroids, the curse of dimensionality,
hierarchical stopping rules, BFR, CURE, GRGPF and stream clustering all cite it by
section. Verified by auditing every lesson's `**Source:**` line against the chapter
map. Next genuinely unread line is **14092**, the start of chapter 8._

_Next unread line was recorded as **12232**, the start of chapter 7. Remaining:
ch8 advertising, ch9 recommendation systems,
ch10 social-network graphs, ch11 dimensionality reduction, ch12 large-scale ML,
ch13 neural nets. Chapters 2-4 should also get a hand re-read at the same depth as
chapter 1 before this work is attested. `extraction: complete` deliberately
withheld._
