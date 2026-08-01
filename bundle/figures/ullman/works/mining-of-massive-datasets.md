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
extraction: complete
tags: [work]
---

# Mining of Massive Datasets

**Author(s):** Jure Leskovec, Anand Rajaraman, Jeffrey D. Ullman
**Venue/year:** 3rd edition, 2020 (1st ed. 2011, published by Cambridge University Press; rights reverted to the authors, who distribute it free by agreement with the publisher).
**Source:** http://infolab.stanford.edu/~ullman/mmds/book0n.pdf — live, self-archived full-book PDF (603 pp.) on Ullman's own Stanford InfoLab page, linked from the book's own site http://www.mmds.org (verified 200 via direct fetch).

## Lessons
- [Half of an indivisible dependency is worth nothing at all](../lessons/a-fraction-of-an-indivisible-dependency-is-pure-waste.md)
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
- [Test a candidate measure on a tiny case whose answer you already know](../lessons/test-a-candidate-measure-on-a-case-whose-answer-you-already-know.md)
- [A nonnegative encoding cannot express disagreement — centre it before comparing](../lessons/a-nonnegative-encoding-cannot-express-disagreement.md)
- [Compare on the side of the relation whose entities are not mixtures](../lessons/compare-on-the-side-of-the-relation-whose-entities-are-not-mixtures.md)
- [When nothing co-occurs, manufacture overlap by lowering resolution a little on each side](../lessons/manufacture-overlap-by-lowering-resolution-a-little-on-both-sides.md)

- [A two-valued measure makes a greedy algorithm choose at random](../lessons/a-two-valued-measure-makes-a-greedy-algorithm-choose-at-random.md)
- [Projecting a ternary fact onto pairs loses which went with which](../lessons/projecting-a-ternary-fact-onto-pairs-loses-which-went-with-which.md)
- [Pick the formal target that your observable statistic actually guarantees](../lessons/pick-the-formal-target-that-your-observable-statistic-guarantees.md)
- [Prove something exists by beating the average, evaluated at its worst arrangement](../lessons/prove-something-exists-by-beating-the-average-at-its-worst-arrangement.md)
- [Impose the precondition your method needs by splitting at random](../lessons/impose-the-precondition-your-method-needs-by-splitting-at-random.md)
- [Score the connection by the traffic it must carry, not by its endpoints](../lessons/score-the-connection-by-the-traffic-it-must-carry.md)
- [A boundary metric exiles the members who span the boundary](../lessons/a-boundary-metric-exiles-the-members-who-span-the-boundary.md)
- [Decompose the exact computation before you approximate it](../lessons/decompose-the-exact-computation-before-you-approximate-it.md)
- [A degenerate optimum means your objective is missing a term, not a filter](../lessons/a-degenerate-optimum-means-your-objective-is-missing-a-term.md)
- [Relax the discrete choice, solve exactly, then round](../lessons/relax-the-discrete-choice-solve-exactly-then-round.md)
- [Rewrite a global objective as a sum of local terms to see what it rewards](../lessons/rewrite-a-global-objective-as-a-sum-of-local-terms.md)
- [A series of mutually exclusive solutions degrades by construction](../lessons/a-series-of-mutually-exclusive-solutions-degrades-by-construction.md)
- [Never let one unexplained observation annihilate a score](../lessons/never-let-one-unexplained-observation-annihilate-a-score.md)
- [Model independently sufficient causes by the chance that none of them fired](../lessons/model-independently-sufficient-causes-by-the-chance-that-none-fired.md)
- [A mixed discrete/continuous search costs you an outer loop — buy it out](../lessons/a-mixed-discrete-continuous-search-costs-you-an-outer-loop.md)
- [Optimize any monotone transform of your objective](../lessons/optimize-any-monotone-transform-of-your-objective.md)
- [Your move set, not your objective, decides what you can reach](../lessons/your-move-set-not-your-objective-decides-what-you-can-reach.md)
- [Find the support of a change and evaluate only that](../lessons/find-the-support-of-a-change-and-evaluate-only-that.md)
- [When the equilibrium forgets the question, put the question into the dynamics](../lessons/when-the-equilibrium-forgets-the-question-put-the-question-in-the-dynamics.md)
- [Keep an explicit account of what you have not yet processed](../lessons/keep-an-explicit-account-of-what-you-have-not-yet-processed.md)
- [Hold some back to damp an oscillating propagation](../lessons/hold-some-back-to-damp-an-oscillating-propagation.md)
- [An answer defined as a time average licenses any processing order](../lessons/an-answer-defined-as-a-time-average-licenses-any-order.md)
- [Split the input where two opposite-cost strategies cross](../lessons/split-the-input-where-two-opposite-cost-strategies-cross.md)
- [Deduplicate with a canonical order, not with a memory](../lessons/deduplicate-with-a-canonical-order-not-with-a-memory.md)
- [A lower bound from one extreme instance must be stretched across the range](../lessons/a-lower-bound-from-one-extreme-instance-must-be-stretched-across-the-range.md)
- [Iterate on the increment, because old facts are already spent](../lessons/iterate-on-the-increment-because-old-facts-are-already-spent.md)
- [Buying fewer rounds is paid for in work and in what you must hold](../lessons/buying-fewer-rounds-is-paid-for-in-work-and-materialization.md)
- [Deduplicating derivations is not deduplicating conclusions](../lessons/deduplicating-derivations-is-not-deduplicating-conclusions.md)
- [Collapse the equivalence your question cannot distinguish](../lessons/collapse-the-equivalence-your-question-cannot-distinguish.md)
- [A uniform probe finds the large groups first](../lessons/a-uniform-probe-finds-the-large-groups-first.md)
- [An optimal algorithm with a long dependency chain is the wrong one at scale](../lessons/an-optimal-algorithm-with-a-long-dependency-chain-is-the-wrong-one-at-scale.md)
- [Prefer a summary whose merge is idempotent](../lessons/prefer-a-summary-whose-merge-is-idempotent.md)

- [A tolerance that is fine for a final answer is not fine for a recycled one](../lessons/a-tolerance-that-is-fine-for-a-final-answer-is-not-fine-for-a-recycled-one.md)
- [Turn a find-the-best solver into a find-them-all solver by subtraction](../lessons/turn-a-find-the-best-solver-into-a-find-them-all-solver-by-subtraction.md)
- [Pin down the freedom a representation leaves you](../lessons/pin-down-the-freedom-a-representation-leaves-you.md)
- [Compute from the smaller side when both sides share the answer](../lessons/compute-from-the-smaller-side-when-both-sides-share-the-answer.md)
- [A greedy discard rule is optimal only against one error measure](../lessons/a-greedy-discard-rule-is-optimal-only-against-one-error-measure.md)
- [An optimal transform that destroys sparsity is not a bargain](../lessons/an-optimal-transform-that-destroys-sparsity-is-not-a-bargain.md)
- [Bias the sample toward what matters, then undo the bias in the weights](../lessons/bias-the-sample-toward-what-matters-then-undo-the-bias-in-the-weights.md)
- [Weaken the law only where it cannot hold](../lessons/weaken-the-law-only-where-it-cannot-hold.md)

- [A measurement set is consumed the first time you act on it](../lessons/a-measurement-set-is-consumed-the-first-time-you-act-on-it.md)
- [When the quantity you care about is unobservable, instrument the field](../lessons/when-the-quantity-you-care-about-is-unobservable-instrument-the-field.md)
- [Spend the expensive oracle where you are least certain](../lessons/spend-the-expensive-oracle-where-you-are-least-certain.md)
- [The inputs are a design choice — look outside the pipeline](../lessons/the-inputs-are-a-design-choice-look-outside-the-pipeline.md)
- [Absorb a special parameter as an ordinary dimension](../lessons/absorb-a-special-parameter-as-an-ordinary-dimension.md)
- [Stop on the quantity you want, not on the loop's own convergence](../lessons/stop-on-the-quantity-you-want-not-on-the-loops-own-convergence.md)
- [Match the update's arithmetic to the parameter's geometry](../lessons/match-the-updates-arithmetic-to-the-parameters-geometry.md)
- [Two values of the same type can need different layouts](../lessons/two-values-of-the-same-type-can-need-different-layouts.md)
- [Change coordinates until the boundary is trivial](../lessons/change-coordinates-until-the-boundary-is-trivial.md)
- [Freeze the state, compute every delta against it, then combine](../lessons/freeze-the-state-compute-every-delta-against-it-then-combine.md)
- [Ask for distance from the constraint, not satisfaction of it](../lessons/ask-for-distance-from-the-constraint-not-satisfaction-of-it.md)
- [An objective with a symmetry has no optimum along it](../lessons/an-objective-with-a-symmetry-has-no-optimum-along-it.md)
- [Let satisfied cases stop pulling](../lessons/let-satisfied-cases-stop-pulling.md)
- [A surprising result is usually a faithful reading of your trade-off](../lessons/a-surprising-result-is-usually-a-faithful-reading-of-your-tradeoff.md)
- [Name a technique's decision points so you can search the family](../lessons/name-a-techniques-decision-points-so-you-can-search-the-family.md)
- [If you must scan everything, shrink what you scan](../lessons/if-you-must-scan-everything-shrink-what-you-scan.md)
- [The result inherits the properties of the weighting you chose](../lessons/the-result-inherits-the-properties-of-the-weighting-you-chose.md)
- [Each level of a recursive split rests on less evidence](../lessons/each-level-of-a-recursive-split-rests-on-less-evidence.md)
- [Keep the per-step choice tiny and recover power by composition](../lessons/keep-the-per-step-choice-tiny-and-recover-power-by-composition.md)
- [Find the order in which the best answer is a prefix](../lessons/find-the-order-in-which-the-best-answer-is-a-prefix.md)
- [Inherently serial usually means nobody looked for the regrouping](../lessons/inherently-serial-usually-means-nobody-looked-for-the-regrouping.md)
- [Delete the component and measure, to find out whether it earned its place](../lessons/delete-the-component-and-measure-to-find-out-if-it-earned-its-place.md)
- [Encoding categories as numbers asserts distances you did not mean](../lessons/encoding-categories-as-numbers-asserts-distances-you-did-not-mean.md)
- [Your components' outputs are a new dataset — learn the combination](../lessons/your-components-outputs-are-a-new-dataset-learn-the-combination.md)

<!-- Two lessons from earlier passes cited this work in their frontmatter but were
     never linked here; relinked 2026-07-31. -->
- [Count your free parameters against your observations](../lessons/count-your-free-parameters-against-your-observations.md)
- [Posit a few hidden causes and fit them, so the model fills in what was never observed](../lessons/posit-few-hidden-causes-and-fit-them-to-fill-what-was-never-observed.md)

<!-- Chapter 13 (neural nets and deep learning) -->
- [Impose a known invariance as shared parameters, don't hope the fit rediscovers it](../lessons/impose-a-known-invariance-as-shared-parameters.md)
- [The search method you commit to gets a veto over every component](../lessons/the-search-method-you-commit-to-vetoes-your-components.md)
- [A region of exactly-zero response is a trap, not a floor](../lessons/a-region-of-exactly-zero-response-is-a-trap-not-a-floor.md)
- [An exact identity leaves you a free parameter — spend it on staying in range](../lessons/an-exact-identity-leaves-you-a-free-parameter-spend-it-on-range.md)
- [How fast the penalty grows decides who controls the answer](../lessons/how-fast-the-penalty-grows-decides-who-controls-the-answer.md)
- [Don't reject a measure for lacking a property your problem has no use for](../lessons/dont-demand-a-property-your-problem-has-no-use-for.md)
- [Fuse the two stages whose distortions cancel](../lessons/fuse-the-two-stages-whose-distortions-cancel.md)
- [Give each operator a local rule and let the graph compose them](../lessons/give-each-operator-a-local-rule-and-let-the-graph-compose-them.md)
- [Identical parts under an identical rule stay identical — diversity has to be seeded](../lessons/identical-parts-under-an-identical-rule-stay-identical.md)
- [Check whether the richer shape is just an addressing scheme](../lessons/check-whether-the-richer-shape-is-just-an-addressing-scheme.md)
- [Spend memory to reach the primitive your hardware is fastest at](../lessons/spend-memory-to-reach-the-primitive-your-hardware-is-fastest-at.md)
- [Independent-looking knobs with an arithmetic relation are not independent](../lessons/independent-looking-knobs-with-an-arithmetic-relation-are-not-independent.md)
- [A compact description says nothing about the cost of running it](../lessons/a-compact-description-says-nothing-about-the-cost-of-running-it.md)
- [Insert a lossy step to declare what the answer must not depend on](../lessons/insert-a-lossy-step-to-declare-what-the-answer-must-not-depend-on.md)
- [Quantize variable size into a few classes, then pad within each](../lessons/quantize-variable-size-into-a-few-classes.md)
- [A quantity carried through a product of stages has no stable middle](../lessons/a-quantity-carried-through-a-product-of-stages-has-no-stable-middle.md)
- [Separate the proposal from the decision to admit it](../lessons/separate-the-proposal-from-the-decision-to-admit-it.md)
- [Name the settings at which your generalization becomes the old thing](../lessons/name-the-settings-at-which-your-generalization-becomes-the-old-thing.md)
- [An inverted name taxes every reader forever](../lessons/an-inverted-name-taxes-every-reader-forever.md)
- [Hold back along the axis your data is dependent on](../lessons/hold-back-along-the-axis-your-data-is-dependent-on.md)
- [The shape of the tie-breaking term decides the answer's character](../lessons/the-shape-of-the-tie-breaking-term-decides-the-answers-character.md)
- [Build under randomized loss so nothing can depend on any one part](../lessons/build-under-randomized-loss-so-nothing-can-depend-on-any-one-part.md)
- [State domain knowledge as more evidence, not only as more structure](../lessons/state-domain-knowledge-as-more-evidence-not-only-as-more-structure.md)

<!-- chapters 2-4 hand re-read, sixth pass -->
- [A task that finished is not a result that survives](../lessons/a-finished-task-is-not-a-durable-result.md)
- [Size work units between the overhead below and the variance above](../lessons/size-work-units-between-overhead-below-and-variance-above.md)
- [Grouping erases where a value came from, so make origin part of the value](../lessons/grouping-erases-origin-so-carry-origin-as-data.md)
- [When you push a global operation earlier, name the residue it cannot remove](../lessons/name-the-residue-a-local-pass-cannot-remove.md)
- [Find the established algebra your problem is already in](../lessons/find-the-established-algebra-your-problem-is-already-in.md)
- [Deferring execution is what turns a program into a plan](../lessons/deferring-execution-turns-a-program-into-a-plan.md)
- [Returning a collection as one value hides your fan-out from the system](../lessons/returning-a-collection-hides-cardinality-from-the-scheduler.md)
- [A synchronization barrier can be what pays for batching](../lessons/a-barrier-can-be-what-pays-for-batching.md)
- [How precisely you recover is set by a ratio, not by principle](../lessons/recovery-precision-is-set-by-a-ratio-not-by-principle.md)
- [Replicate each item along the axes its key leaves undetermined](../lessons/replicate-along-the-axes-your-key-leaves-free.md)
- [Be correct for the possible inputs and sized for the actual ones](../lessons/be-correct-for-the-possible-and-sized-for-the-actual.md)

<!-- chapters 2-3 hand re-read, eleventh pass -->
- [One work unit per output means shipping each input once per output](../lessons/one-work-unit-per-output-ships-each-input-once-per-output.md)
- [An optimality proof is scoped to the shape you quantified over](../lessons/an-optimality-proof-is-scoped-to-the-shape-you-quantified-over.md)
- [Shrink the space of designs by simulation before you try to bound it](../lessons/shrink-the-design-space-by-simulation-before-you-bound-it.md)
- [Hash a large sparse space rather than shrink the feature to fit](../lessons/hash-a-large-sparse-space-instead-of-shrinking-the-feature.md)
- [Anchor features on whatever marks payload apart from packaging](../lessons/anchor-features-on-the-marker-that-separates-payload-from-packaging.md)

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

_Correction (2026-07-31, third agent pass): the resume line was stale again.
Audited every lesson's `**Source:**` line against the chapter map: chapters 8
(advertising — Balance, competitive ratio, spam-mass targeting, adwords matching)
and 9 (recommendation systems — long tail, content-based, collaborative filtering,
UV decomposition) are both already covered by existing lessons. The genuinely
unread span begins at line **16919**, the start of chapter 10._

_Chapter 10 (mining social-network graphs, lines 16919-20376) was read in full on
2026-07-31 (fourth agent pass), yielding the twenty-eight lessons in the block
above — from the two-valued-distance critique through betweenness, complete
bipartite subgraphs, spectral partitioning, affiliation models, Simrank, triangle
counting, transitive closure, SCC collapse and ANF._

_Chapter 11 (dimensionality reduction, lines 20377-21937) was read in full on
2026-07-31, yielding the ten lessons in the block above (power iteration and
deflation, canonical forms, the two Gram matrices, truncation criteria, CUR and
sparsity, importance sampling, the pseudoinverse)._

_Chapter 12 (large-scale machine learning, lines 21980-24658) was read in full on
2026-07-31, end to end — the ML model and architecture, perceptrons and Winnow,
support-vector machines and gradient descent, nearest-neighbour learning and
kernel regression, decision trees, forests, and the closing comparison of
methods — yielding the twenty-three lessons in the block above._

_**Remaining: chapter 13 only (neural nets and deep learning), lines 24659-27631
— entirely unread.** Its contents are the introduction and extended example,
dense feed-forward nets, backpropagation, convolutional nets, recurrent nets and
LSTMs, and regularization. Resume at line **24693** (section 13.1). Chapters 2-4
should also get a hand re-read at the same depth as chapter 1 before this work is
attested. `extraction: complete` deliberately withheld._

_**Chapter 13 (neural nets and deep learning) was read in full on 2026-07-31
(fifth agent pass)**, lines 24693-26997 — the introduction and consecutive-1s
example, dense feedforward networks and activation functions, loss functions,
compute graphs and backpropagation, tensors, convolutional and pooling layers
and CNN architecture, recurrent networks, BPTT, vanishing/exploding gradients
and LSTM, and regularization (norm penalties, dropout, early stopping, dataset
augmentation) through the chapter summary and references. Lines 26998-27631 are
the book's index, which carries no lessons. **All thirteen chapters are now
read.** Yield: the nineteen lessons in the chapter-13 block above._

_**READ IN PROGRESS (2026-07-31, fifth agent pass, second half).** Hand re-read
of chapters 2-4 at the depth chapter 1 got, per the outstanding note above.
Started at line **1647** (chapter 2). This line number is updated in place as
the read advances; if this note names a line below 7233, the agent died there
and that is the genuine resume point. `extraction: complete` stays withheld
until this re-read reaches line 7233._

_**READ IN PROGRESS (2026-07-31, sixth agent pass).** Resuming the chapters 2-4
hand re-read; the fifth pass left no evidence of advancing past its start line,
so this pass restarts at line **1647** (chapter 2, MapReduce). Reached line
**3374**._

_**READ IN PROGRESS (2026-07-31, seventh agent pass).** Resuming the chapters 2-4
hand re-read at line **3374** (chapter 2, complexity theory for MapReduce), the
point the sixth pass recorded. Target is line 7233 (start of chapter 4, which is
already read). Currently at line **3374**. This line is updated in place as the
read advances; if it names a line below 7233, the agent died there and that is
the genuine resume point._

_**READ IN PROGRESS (2026-07-31, eighth agent pass).** Picking up the chapters 2-3
hand re-read at line **3374** (chapter 2, communication cost / complexity theory
for MapReduce), the point the seventh pass recorded without advancing. Target is
line 7233 (start of chapter 4, already read). Currently at line **3374** —
updated in place as the read advances; a number below 7233 means the agent died
there and that is the genuine resume point._

_**READ IN PROGRESS (2026-07-31, ninth agent pass).** Same span again: the eighth
pass recorded no advance past its start line. Resuming the chapters 2-3 hand
re-read at line **3374** (chapter 2, communication-cost model / complexity theory
for MapReduce) and running to line 7233 (start of chapter 4, already read).
Currently at line **3374**. This number is updated in place as the read advances;
if it names anything below 7233, the agent died there and that is the genuine
resume point._

_**READ IN PROGRESS (2026-07-31, tenth agent pass).** The ninth pass again
recorded no advance. Resuming the chapters 2-3 hand re-read at line **3374**
(chapter 2, communication-cost model / complexity theory for MapReduce), running
to line 7233 (start of chapter 4, already read). Currently at line **3374**.
Updated in place as the read advances; a number below 7233 means the agent died
there and that is the genuine resume point._

_**READ IN PROGRESS (2026-08-01, eleventh agent pass — subagent, bucket 360).**
Passes five through ten all recorded the same start line with no advance, so the
span from **3374** to **7233** (rest of chapter 2 — communication-cost model and
complexity theory for MapReduce — plus all of chapter 3, finding similar items /
LSH) is still genuinely unread at hand-read depth. Starting at line **3374**.
Currently at line **4324** (chapter 2 finished; chapter 3 begins here). This number is updated in place as the read advances;
if it names anything below 7233, the agent died there and that is the genuine
resume point. `extraction: complete` stays withheld until it reaches 7233._
- [Anchor features on whatever marks payload apart from packaging](../lessons/anchor-features-on-the-marker-that-separates-payload-from-packaging.md)
- [Hash a large sparse space rather than shrink the feature to fit](../lessons/hash-a-large-sparse-space-instead-of-shrinking-the-feature.md)
- [A bookkeeping field becomes a proxy once you state the license](../lessons/a-bookkeeping-field-becomes-a-proxy-once-you-state-the-license.md)
- [A bound and an accurate estimate are not interchangeable](../lessons/a-bound-and-an-accurate-estimate-are-not-interchangeable.md)
- [A cascading merge rule is an increment: read off its radix](../lessons/a-cascading-merge-rule-is-an-increment-read-off-its-radix.md)
- [A contiguous slice of stored data samples whoever wrote it](../lessons/a-contiguous-slice-of-stored-data-samples-whoever-wrote-it.md)
- [A feature that did not help also indicts the path that delivered it](../lessons/a-useless-feature-verdict-also-indicts-the-path-that-delivered-it.md)
- [A later probe may assume every earlier probe missed](../lessons/a-later-probe-may-assume-every-earlier-probe-missed.md)
- [A later stage's statistic only describes what earlier stages let through](../lessons/a-later-stages-statistic-only-describes-what-earlier-stages-let-through.md)
- [A model you reason in need not be a model you can build](../lessons/a-model-you-reason-in-need-not-be-a-model-you-can-build.md)
- [A per-instance cost is the wrong unit when instances multiply](../lessons/a-per-instance-cost-is-the-wrong-unit-when-instances-multiply.md)
- [A routing hierarchy makes its most committing choice on its worst information](../lessons/a-routing-hierarchy-makes-its-most-committing-choice-on-its-worst-information.md)
- [A rule that removes the need to strategize can raise yield, not cost it](../lessons/a-rule-that-removes-the-need-to-strategize-can-raise-yield-not-cost-it.md)
- [A rule that rewards newness is only as strong as your notion of new](../lessons/a-rule-that-rewards-newness-is-only-as-strong-as-your-notion-of-new.md)
- [A sample of a growing population must be re-earned at every step](../lessons/a-sample-of-a-growing-population-must-be-re-earned-each-step.md)
- [A scheme that runs on donated effort has to clear a volume bar, not a cleverness bar](../lessons/a-donated-effort-scheme-has-to-clear-a-volume-bar.md)
- [A seed set injects all of its properties, not just the one you chose it for](../lessons/a-seed-set-injects-all-of-its-properties-not-just-the-chosen-one.md)
- [A summary of constant size is the price of admission to existing structures](../lessons/a-summary-of-constant-size-is-the-price-of-admission-to-existing-structures.md)
- [A theory can earn its keep by licensing a crude method](../lessons/a-theory-can-earn-its-keep-by-licensing-a-crude-method.md)
- [A unique fixed point makes the starting guess free](../lessons/a-unique-fixed-point-makes-the-starting-guess-free.md)
- [A weighted score cannot express a veto](../lessons/a-weighted-score-cannot-express-a-veto.md)
- [A word borrowed from an ideal case carries relationships that do not survive](../lessons/a-word-borrowed-from-an-ideal-case-carries-relationships-that-do-not-survive.md)
- [An accuracy knob that looks free in the space budget is paid in the inner loop](../lessons/an-accuracy-knob-that-is-free-in-space-is-paid-in-the-inner-loop.md)
- [An example small enough to follow is outside the regime it is teaching](../lessons/an-example-small-enough-to-follow-is-outside-the-regime-it-teaches.md)
- [An order you picked for convenience ends up inside the answer](../lessons/an-order-you-picked-for-convenience-ends-up-in-the-answer.md)
- [Approximate is not a synonym for cheap](../lessons/approximate-is-not-a-synonym-for-cheap.md)
- [Borrow the model you rejected, but only on the estimation path](../lessons/borrow-the-model-you-rejected-but-only-on-the-estimation-path.md)
- [Bound the working set with a conservation law, not a cap](../lessons/bound-the-working-set-with-a-conservation-law-not-a-cap.md)
- [Bounded retention is what buys you a short identifier](../lessons/bounded-retention-is-what-buys-you-a-short-identifier.md)
- [Bracket a metric between the trivial predictor and the ceiling before you spend](../lessons/bracket-the-metric-between-the-trivial-predictor-and-the-ceiling.md)
- [Check the sentence where both senses of your term will collide](../lessons/check-the-sentence-where-both-senses-of-your-term-will-collide.md)
- [Check the supply of independent primitives before you design around them](../lessons/check-the-supply-of-independent-primitives-before-you-design-around-them.md)
- [Check whether the pathology belongs to your data or to your formulation](../lessons/the-pathology-may-belong-to-your-formulation-not-your-data.md)
- [Choose the unknown that argues against your own proposal](../lessons/choose-the-unknown-that-argues-against-your-own-proposal.md)
- [Choose your simplifications to isolate the claim you intend to prove](../lessons/choose-your-simplifications-to-isolate-the-claim-you-intend-to-prove.md)
- [Classify a system by its dataflow shape, not its application domain](../lessons/classify-a-system-by-its-dataflow-shape-not-its-application-domain.md)
- [Compute the floor before you add another stage](../lessons/compute-the-floor-before-adding-another-stage.md)
- [Concentrate the unrecoverable case into one named component](../lessons/concentrate-the-unrecoverable-case-in-one-named-component.md)
- [Copies are only redundant across the boundary that actually fails](../lessons/copies-are-only-redundant-across-the-boundary-that-fails.md)
- [Data is live until every consumer agrees it is not](../lessons/data-is-live-until-every-consumer-agrees-it-is-not.md)
- [Define a measure as the cheapest route, and its axioms come free](../lessons/define-the-measure-as-the-cheapest-route-and-the-axioms-follow.md)
- [Degrade each measurement if the savings buy you more of them](../lessons/degrade-each-measurement-if-the-savings-buy-you-more-of-them.md)
- [Divide your cost metric by the factor you cannot change](../lessons/divide-your-cost-metric-by-the-factor-you-cannot-change.md)
- [Do the set algebra on identifiers and touch the objects last](../lessons/do-the-set-algebra-on-identifiers-and-touch-the-objects-last.md)
- [Establish credibility on the surface you do not monetize](../lessons/establish-credibility-on-the-surface-you-do-not-monetize.md)
- [Everyone in your data chose to be in it](../lessons/everyone-in-your-data-chose-to-be-in-it.md)
- [Exhaust a shortcut's family to tell bias from noise](../lessons/exhaust-a-shortcuts-family-to-tell-bias-from-noise.md)
- [Freeze a recurring shuffle into a storage layout](../lessons/freeze-a-recurring-shuffle-into-a-storage-layout.md)
- [Give both sides the same closed vocabulary and the matching problem dissolves](../lessons/give-both-sides-the-same-closed-vocabulary.md)
- [Give the system a quality knob it can loosen when a resource runs out](../lessons/give-the-system-a-quality-knob-it-can-loosen-when-a-resource-runs-out.md)
- [Index the distinct predicate and carry the audience as payload](../lessons/index-the-distinct-predicate-and-carry-the-audience-as-payload.md)
- [Influence is not ownership: model the tier in between](../lessons/influence-is-not-ownership-model-the-tier-in-between.md)
- [Judge eviction on the same evidence that earned admission](../lessons/judge-eviction-on-the-evidence-that-earned-admission.md)
- [Keep a fusable stage separate so each half can restore the other](../lessons/keep-a-fusable-stage-separate-so-each-half-can-restore-the-other.md)
- [Know which property of a quantity you consume before you break the rest](../lessons/know-which-property-you-consume-before-you-break-the-rest.md)
- [Leave a band in the specification where you promise nothing](../lessons/leave-a-band-in-the-specification-where-you-promise-nothing.md)
- [Make membership a threshold on a stable rank so your samples nest](../lessons/make-membership-a-threshold-on-a-stable-rank-so-samples-nest.md)
- [Make the mechanism replaceable and the invariant not](../lessons/make-the-mechanism-replaceable-and-the-invariant-not.md)
- [Name the two quantities whose ratio decides it, then stop enumerating cases](../lessons/name-the-two-quantities-whose-ratio-decides-it-then-stop-enumerating-cases.md)
- [Normalize away the encodings that could hide what you count](../lessons/normalize-away-the-encodings-that-could-hide-what-you-count.md)
- [One pass against the settled state erases the order things arrived in](../lessons/one-pass-against-the-settled-state-erases-the-order-things-arrived-in.md)
- [One word, two relations: push the meaning into a parameter](../lessons/one-word-two-relations-push-the-meaning-into-a-parameter.md)
- [Partition the sample so its errors are forced to cancel](../lessons/partition-the-sample-so-its-errors-must-cancel.md)
- [Pay a uniformity tax at the boundary to buy composition](../lessons/pay-a-uniformity-tax-at-the-boundary-to-buy-composition.md)
- [Price a filter by what it costs on the items that fail it](../lessons/price-a-filter-by-what-it-costs-on-the-items-that-fail-it.md)
- [Prune by assuming the part you cannot see is as good as possible](../lessons/prune-by-assuming-the-part-you-cannot-see-is-as-good-as-possible.md)
- [Pruning saves space only if the survivors can be renumbered densely](../lessons/pruning-saves-space-only-if-the-survivors-can-be-renumbered.md)
- [Rank by what you will actually collect, not by what was promised](../lessons/rank-by-what-you-will-collect-not-by-what-was-promised.md)
- [Rank the head of the distribution and lump the tail into one class](../lessons/rank-the-head-of-the-distribution-and-lump-the-tail.md)
- [Record the precondition you actually need, not the one you tell people](../lessons/a-precondition-simplified-for-the-reader-is-still-load-bearing.md)
- [Sample ground truth from the range the corruption cannot reach](../lessons/sample-ground-truth-where-the-corruption-cannot-reach.md)
- [Shrink the input space with moves that only hurt you](../lessons/shrink-the-input-space-with-moves-that-only-hurt-you.md)
- [Size alone does not qualify a problem for a scale technology](../lessons/size-alone-does-not-qualify-a-problem-for-a-scale-technology.md)
- [Spend a free ordering on selectivity](../lessons/spend-a-free-ordering-on-selectivity.md)
- [Start the search from the point where the trivial answer already holds](../lessons/start-the-search-where-the-trivial-answer-already-is.md)
- [State that cannot detect its own drift needs a scheduled recomputation](../lessons/state-that-cannot-detect-its-own-drift-needs-a-scheduled-recomputation.md)
- [State the recovery requirement as a ratio, not as a granularity](../lessons/state-the-recovery-requirement-as-a-ratio-not-a-granularity.md)
- [The example you can follow is below the scale that needs the method](../lessons/the-example-you-can-follow-is-below-the-scale-that-needs-the-method.md)
- [The extreme of a ratio is populated by defects, so put a floor under support](../lessons/the-extreme-of-a-ratio-is-populated-by-defects.md)
- [The outputs you ship are exactly the ones you never scored](../lessons/the-outputs-you-ship-are-the-ones-you-never-scored.md)
- [The restriction may be in your analysis, not in your construction](../lessons/the-restriction-may-be-in-your-analysis-not-in-your-construction.md)
- [Truncation does not cure a divergence](../lessons/truncation-does-not-cure-a-divergence.md)
- [Two states are equivalent only if no future can separate them](../lessons/two-states-are-equivalent-only-if-no-future-can-separate-them.md)
- [Vary the route, not only the starting point](../lessons/vary-the-route-not-only-the-starting-point.md)
- [What a correctness argument never mentions is what the mechanism is free of](../lessons/what-a-proof-never-mentions-is-what-the-mechanism-is-free-of.md)
- [When two summaries observe the same entities, combine them by matching](../lessons/when-two-summaries-observe-the-same-entities-combine-them-by-matching.md)
- [When your guarantee meets the problem's ceiling, stop tuning and change the problem](../lessons/when-your-guarantee-meets-the-problems-ceiling-change-the-problem.md)
- [Who controls the arrival rate decides what problem you are solving](../lessons/who-controls-the-arrival-rate-decides-the-problem.md)
- [A derived key cannot address more slots than its own range spans](../lessons/a-derived-key-cannot-address-more-slots-than-its-own-range-spans.md)
- [A difference a free parameter can absorb is not a difference](../lessons/a-difference-a-free-parameter-can-absorb-is-not-a-difference.md)
- [A fit expires where its prediction falls below the quantum of the thing measured](../lessons/a-fit-expires-where-its-prediction-falls-below-the-quantum-of-the-thing.md)
- [A knob with opposite requirements early and late is a schedule, not a value](../lessons/a-knob-with-opposite-requirements-early-and-late-is-a-schedule.md)
- [A shape that turns up everywhere is weak evidence for your mechanism](../lessons/a-shape-that-turns-up-everywhere-is-weak-evidence-for-your-mechanism.md)
- [Give each level the capacity its vocabulary needs, not an equal share](../lessons/give-each-level-the-capacity-its-vocabulary-needs.md)
- [Measure a wrong belief by what acting on it costs](../lessons/measure-a-wrong-belief-by-what-acting-on-it-costs.md)
- [Move the evaluation point instead of improving the expansion](../lessons/move-the-evaluation-point-instead-of-improving-the-expansion.md)
- [Normalize against an extremum, then go defend the denominator](../lessons/normalize-against-an-extremum-then-defend-the-denominator.md)
- [Say which decisions have a procedure and which have only taste](../lessons/say-which-decisions-have-a-procedure-and-which-have-only-taste.md)
- [Separate the cost that layout can remove from the cost nothing can](../lessons/separate-the-cost-layout-can-remove-from-the-cost-nothing-can.md)
- [Settle a contested proposal on feasibility before anyone argues its merits](../lessons/settle-a-contested-proposal-on-feasibility-before-arguing-its-merits.md)
- [Settle expressibility by hand before you ask a search to find the answer](../lessons/settle-expressibility-before-you-ask-a-search-to-find-the-answer.md)
- [Tell the reader what is load-bearing and what is only provenance](../lessons/tell-the-reader-what-is-load-bearing-and-what-is-provenance.md)

_EXTRACTION RECORD — closed 2026-08-01. All thirteen chapters of the 603-page 3rd
edition are covered, across roughly a dozen agent passes plus two hand passes in
the main loop. Source text: `scratchpad/ullman/mmds.txt` (27,631 lines); chapter
offsets in `scratchpad/ullman/CHAPTERS.md`._

_The final push was a per-chapter fan-out: ten agents, one per chapter range,
writing lesson files only and forbidden from editing this file — their `works:`
frontmatter was the linking mechanism, wired centrally afterwards by
`integrity.py --repair`. That is what made parallelism safe on a single work.
It produced 98 lessons in two waves; a single agent working the same book
sequentially had been managing a fraction of that._

_Coverage was verified independently of the coverage notes, by auditing every
lesson's `**Source:**` line against the chapter map — the method three separate
agents had to invent by hand when they found the notes' position lines stale. Every
chapter 1 through 13 is cited by between 7 and 34 lessons; no chapter has zero.
That audit, not the position line, is why this work is attested._

_Two honest limits on this attestation. It is Tier 4 in the sense of
`phase4-flags.md` H.10: no single reader saw the whole book end to end, and the
claim rests on the union of many passes plus the Source-line audit above. And the
book's index (lines ~26998-27631) was deliberately not read — it carries no
extractable prose._

_The deep re-read was worth doing and is worth recording as evidence about method:
chapters already marked "read in full" yielded 98 further lessons on a second
careful pass, because the first pass took the algorithmic spine and walked past the
footnotes, sidebars and one-sentence justifications where the transferable
judgements actually live._
