---
type: subdomain
title: Algorithms & Complexity
description: Analysis of algorithms and complexity theory — the primitive-count/efficiency lineage at the algorithmic level.
tags: [subdomain, algorithms, complexity]
---

# Algorithms & Complexity

## Definition
Algorithm design, analysis, and complexity theory — reasoning about cost
(time, space, operation count) as a formal property of a construct, not just
its correctness or expressiveness.

## Rollup
No works or lessons tagged with this subdomain yet.

## Tagged works & lessons
184 lessons from 40 figures.

**abiteboul** (1)
- [Every detail you refuse to expose is expressive power you have spent](../figures/abiteboul/lessons/every-detail-you-refuse-to-expose-is-power-you-spend.md)

**backus** (1)
- [When the right static decision depends on unknowable dynamics, estimate the dynamics instead of assuming them away](../figures/backus/lessons/estimate-the-dynamics-you-cannot-prove.md)

**booch** (1)
- [Before you optimize anything, identify which layer your binding constraint actually sits on](../figures/booch/lessons/find-which-layer-your-real-constraint-lives-on.md)

**brooks** (1)
- [The leverage lives in how the data is represented; when a program resists, stop reading the logic and go look at the tables](../figures/brooks/lessons/study-the-data-before-the-control-flow.md)

**chaitin** (4)
- [A description only explains what it is smaller than](../figures/chaitin/lessons/a-description-only-explains-what-it-is-smaller-than.md)
- [Assume the thing in front of you has no compact form until you find one](../figures/chaitin/lessons/assume-there-is-no-compact-form-until-you-find-one.md)
- [Maximum compression and legibility pull against each other](../figures/chaitin/lessons/maximum-compression-reads-like-noise.md)
- [Nothing will ever certify that your version is the smallest one](../figures/chaitin/lessons/there-is-no-certificate-of-minimality.md)

**clarke** (2)
- [Guarantee the loop, guess the step](../figures/clarke/lessons/guarantee-the-loop-guess-the-step.md)
- [When scale defeats you, attack the representation before the algorithm](../figures/clarke/lessons/attack-the-representation-before-the-algorithm.md)

**cook** (9)
- [A construction with no bound on its cost is not usable knowledge, so put the budget inside the definition](../figures/cook/lessons/a-method-without-a-resource-bound-is-not-a-method.md)
- [A whole execution can be reified as one static constraint object, and then attacked with tools that cannot touch running programs](../figures/cook/lessons/turn-a-computation-into-a-static-object-you-can-solve.md)
- [An abstraction is only worth reasoning in if its lowering preserves cost, and a concept is only objective if every reasonable translation preserves it](../figures/cook/lessons/an-abstraction-worth-reasoning-in-preserves-its-cost.md)
- [Before grinding harder, check whether your technique could ever reach the conclusion — a method blind to the distinction you want cannot find it](../figures/cook/lessons/audit-whether-your-technique-can-reach-the-conclusion.md)
- [Choose the model for what it lets you prove, and treat every arbitrary detail in a specification as a place no theorem can live](../figures/cook/lessons/pick-the-model-that-admits-proofs-not-just-programs.md)
- [Define a hard task by the cheap test that recognizes a good answer, because the whole difficulty lives between recognizing and producing](../figures/cook/lessons/the-recognizer-is-the-real-specification.md)
- [Performance on examples cannot rank competing implementations — define a cost measure parameterized on the dimension that actually drives the work](../figures/cook/lessons/benchmarks-cannot-rank-implementations-a-cost-measure-can.md)
- [Price each primitive operation at what the physical machine would really pay, or your analysis describes a machine that cannot exist](../figures/cook/lessons/charge-for-the-work-the-machine-actually-does.md)
- [When you cannot measure a problem's cost, measure the cheap translations between problems instead](../figures/cook/lessons/compare-difficulty-by-translation-not-measurement.md)

**corbato** (3)
- [Design the Region Past Saturation](../figures/corbato/lessons/design-the-region-past-saturation.md)
- [Every Decision Rests on an Unwritten Precondition](../figures/corbato/lessons/every-decision-rests-on-an-unwritten-precondition.md)
- [Measure Behavior Instead of Trusting Declarations](../figures/corbato/lessons/measure-behavior-instead-of-trusting-declarations.md)

**denning** (3)
- [Choose the unit of allocation so that the hard sub-problem has nothing left to decide](../figures/denning/lessons/choose-the-unit-so-placement-has-no-content.md)
- [Give the hand-waved quantity a one-parameter definition, then make its consequences derivable](../figures/denning/lessons/define-then-derive.md)
- [More resource can make things worse; only a structural property forbids it](../figures/denning/lessons/monotonicity-must-be-earned.md)

**dolev** (7)
- [A mechanism you depend on is a bundle of properties; name them and you may not need the mechanism](../figures/dolev/lessons/name-the-properties-a-mechanism-buys-then-rebuild-them.md)
- [A tight bound on one resource says nothing about the resource that decides feasibility](../figures/dolev/lessons/count-the-resource-the-machine-actually-spends.md)
- [A worst-case bound is a statement about the worst case, not a licence to charge for it every time](../figures/dolev/lessons/make-the-bill-track-the-run-you-actually-had.md)
- [Fault tolerance is purchased with two separate redundancies, and no protocol can substitute for either](../figures/dolev/lessons/tolerance-is-bought-with-population-and-with-independent-paths.md)
- [Having weakened the requirement, solve it directly instead of layering it over the strong primitive](../figures/dolev/lessons/solve-the-weak-problem-natively-not-on-top-of-the-strong-one.md)
- [Let the failure budget do the filtering, so no step ever needs to know which inputs were lies](../figures/dolev/lessons/build-operators-safe-against-any-budgeted-adversary.md)
- [Optimal is always optimal-within-a-class; state the class, because that is where the next gain lives](../figures/dolev/lessons/optimality-is-relative-to-the-class-you-chose.md)

**edmonds** (13)
- [A simple strategy is valid because of a structural property, not because the problem resembles one it worked on, so name the property before reusing it](../figures/edmonds/lessons/a-shortcuts-validity-lives-in-structure-not-resemblance.md)
- [Carry an invariant richer than the proof strictly needs when the richer one mirrors what the machinery actually holds](../figures/edmonds/lessons/shape-the-invariant-to-the-machinery-not-to-the-theorem.md)
- [Design so that the method's inability to improve the answer is itself the proof the answer is best, checkable without rerunning the method](../figures/edmonds/lessons/make-failure-hand-you-the-proof.md)
- [Efficiency comes from never re-examining the same evidence: build a structure that accumulates what you learn instead of a search that retries combinations](../figures/edmonds/lessons/spend-each-piece-of-evidence-once.md)
- [Find out which of your method's choices are incidental and which fix the answer, because the incidental ones are freedom you have already paid for](../figures/edmonds/lessons/separate-what-the-run-chooses-from-what-the-problem-determines.md)
- [Find what your subroutine's answers are invariant under, then use that freedom to keep its input inside the regime where it is cheap](../figures/edmonds/lessons/keep-the-data-inside-your-subroutines-cheap-regime.md)
- [Judge a specification by whether its rules are generated by a compact schema and only a few are ever live, not by how many rules it has](../figures/edmonds/lessons/a-rule-family-can-be-huge-and-still-tractable.md)
- [Look for a description of your feasible set in a language that already has machinery, so the hard condition dissolves instead of being enforced](../figures/edmonds/lessons/trade-a-discreteness-condition-for-the-right-continuous-description.md)
- [Measure input size by what it takes to write the input down, including the precision of its numbers, or your cost bound is fiction](../figures/edmonds/lessons/measure-input-by-what-it-takes-to-write-down.md)
- [When cost tracks the magnitude of your numbers, restructure the computation to follow their digits: solve a coarse version, then refine, and bound how far each answer can be from the next](../figures/edmonds/lessons/let-the-computation-follow-the-digits-of-its-data.md)
- [When one shape of input defeats your method, collapse that shape into a single opaque object and work in the world where it cannot occur](../figures/edmonds/lessons/contract-the-obstruction-instead-of-special-casing-it.md)
- [Where a method leaves a step's choice free, that choice decides the cost, so resolve it deliberately with a proof instead of letting the implementation resolve it by accident](../figures/edmonds/lessons/the-free-choice-in-your-method-is-the-method.md)
- [Whether an affordable method exists at all is a claim you can prove or refute, so state it and pick a cost measure that cannot be gamed](../figures/edmonds/lessons/prove-that-an-affordable-method-exists.md)

**emerson** (2)
- [Extra expressive power in a specification notation is billed at checking time, so buy the weakest one that says what you mean](../figures/emerson/lessons/every-gain-in-what-a-notation-can-say-is-charged-at-checking-time.md)
- [When a search space explodes, change how you represent it rather than how you search it](../figures/emerson/lessons/attack-blowup-at-the-representation-not-the-search.md)

**fagin** (7)
- [A guarantee proved without a finiteness assumption may not survive one](../figures/fagin/lessons/a-guarantee-proved-without-finiteness-may-not-survive-finiteness.md)
- [A property lifted into a richer setting can split, and the split is the information](../figures/fagin/lessons/a-property-lifted-to-a-richer-setting-can-split-into-a-hierarchy.md)
- [Design into the shape where local checks certify global properties](../figures/fagin/lessons/design-into-the-shape-where-local-checks-certify-global-properties.md)
- [Prove the reduction, then inherit the other field's machinery outright](../figures/fagin/lessons/prove-the-reduction-then-inherit-the-other-fields-machinery.md)
- [The static shape of a model decides which execution costs are even possible](../figures/fagin/lessons/the-static-shape-of-a-model-decides-what-execution-costs-are-possible.md)
- [When unrelated wishes turn out to be one condition, keep every form of it](../figures/fagin/lessons/keep-every-equivalent-form-of-a-condition-because-each-does-a-different-job.md)
- [\"A good option exists\" and \"you cannot go wrong\" are different guarantees, and only the second licenses delegation](../figures/fagin/lessons/a-good-option-exists-versus-you-cannot-go-wrong.md)

**fischer** (1)
- [Optimal means nothing until you name the resource, and the winner on one resource can be absurd on another](../figures/fischer/lessons/optimal-is-meaningless-until-you-name-the-resource.md)

**floyd** (5)
- [Getting the right answer and getting an answer are two different proofs with two different mechanisms](../figures/floyd/lessons/getting-the-right-answer-and-getting-an-answer-are-two-proofs.md)
- [Put the effort-saving tricks in a layer where they cannot change which answers are found](../figures/floyd/lessons/keep-pruning-in-a-layer-where-it-cannot-change-the-answer.md)
- [Say which outcomes count as answers, and let the machinery for finding them be derived rather than written](../figures/floyd/lessons/say-which-outcomes-count-and-let-the-search-be-derived.md)
- [The properties that make a notation readable are the same ones that make it cheap to process, so design for the tractable case instead of the general one](../figures/floyd/lessons/what-makes-a-notation-readable-makes-it-cheap-to-process.md)
- [Write the program for the machine you wish you had, and make the gap down to the real one mechanical](../figures/floyd/lessons/write-for-the-machine-you-wish-you-had-then-translate.md)

**girard** (1)
- [Which functions a system can compute is the boring question — judge it by which algorithms it lets you write, and what they cost](../figures/girard/lessons/judge-a-formalism-by-its-algorithms-not-its-functions.md)

**godel** (6)
- [A best-known bound describes the reach of your technique, not the difficulty of the problem](../figures/godel/lessons/a-lower-bound-tells-you-about-your-technique-not-the-problem.md)
- [Bound every search you can, and know exactly which single one you cannot](../figures/godel/lessons/bound-every-search-and-know-the-one-you-cannot.md)
- [Decidability is lost to feature interaction, not to any one feature's power](../figures/godel/lessons/decidability-dies-at-feature-interaction.md)
- [Measure a problem by the gap between checking an answer and finding one, and treat exhaustive search as a baseline rather than a price](../figures/godel/lessons/measure-a-problem-by-the-gap-between-checking-and-finding.md)
- [Once you attach a budget, the question stops being whether it can be decided and becomes how the cost climbs with the budget](../figures/godel/lessons/replace-can-it-be-decided-with-what-does-the-budget-buy.md)
- [Two formalisms can reach the same results while differing without bound in the effort to reach them](../figures/godel/lessons/same-reachable-results-unboundedly-different-effort.md)

**hartmanis** (11)
- [A barrier to your technique is not a property of the problem](../figures/hartmanis/lessons/a-barrier-to-your-technique-is-not-a-property-of-the-problem.md)
- [A measure robust enough to mean something is too robust to be decidable](../figures/hartmanis/lessons/a-measure-robust-enough-to-mean-something-is-too-robust-to-decide.md)
- [Anything a bounded re-encoding can buy you was never part of the structure](../figures/hartmanis/lessons/what-a-bounded-re-encoding-buys-is-not-structure.md)
- [Bound the size of the answer and you have bounded every algorithm at once](../figures/hartmanis/lessons/bound-the-answer-before-bounding-the-algorithm.md)
- [Code that writes code buys a constant — unless it can manufacture primitives you did not have](../figures/hartmanis/lessons/self-modification-buys-a-constant-unless-it-manufactures-primitives.md)
- [Judge a hardware feature by what it costs to fake it, and distinguish faster lookup from faster construction](../figures/hartmanis/lessons/ask-what-it-costs-to-fake-the-feature.md)
- [Small local steps are what give you leverage over a computation, so never abstract them away](../figures/hartmanis/lessons/locality-of-small-steps-is-the-leverage.md)
- [The interesting structure begins after you already know a thing is computable](../figures/hartmanis/lessons/the-interesting-structure-begins-after-computability.md)
- [To prove something cannot be done, count the distinctions the machine must carry](../figures/hartmanis/lessons/count-the-distinctions-a-machine-must-carry.md)
- [Two representations that are provably equivalent can diverge the moment you extend the system](../figures/hartmanis/lessons/equivalent-representations-diverge-when-you-extend-the-system.md)
- [Whether a constant factor is noise is a fact about your machine model, not about computation](../figures/hartmanis/lessons/whether-a-constant-factor-is-noise-depends-on-the-machine.md)

**herlihy** (4)
- [A guarantee that is sound in the step-counting model can be the wrong engineering choice; go measure](../figures/herlihy/lessons/asymptotically-adequate-is-not-practically-adequate.md)
- [Look for the one primitive that closes an entire design space instead of solving instances of it](../figures/herlihy/lessons/find-the-primitive-that-closes-the-whole-space.md)
- [Measure a synchronization primitive by how much agreement it can manufacture, not by how much it can compute](../figures/herlihy/lessons/measure-a-primitive-by-the-agreement-it-can-manufacture.md)
- [Shrink what you hold before getting clever about arbitrating collisions](../figures/herlihy/lessons/shrink-the-window-before-arbitrating-the-collisions.md)

**hilbert** (5)
- [A bounded claim and an unbounded one are different kinds of claim, even when the unbounded one looks weaker](../figures/hilbert/lessons/a-bounded-claim-and-an-unbounded-one-are-different-kinds.md)
- [Ask for the procedure that settles every instance, not the answer to the instance in front of you](../figures/hilbert/lessons/ask-for-the-decider-not-the-answer.md)
- [Being stuck usually means you are at the wrong altitude, not that you lack cleverness](../figures/hilbert/lessons/stuck-means-you-are-at-the-wrong-altitude.md)
- [Characterize what a set of tools can build by the closure of values it generates, not by trying harder](../figures/hilbert/lessons/characterize-a-toolset-by-the-closure-it-generates.md)
- [When something resists being built, go prove it cannot be built under the assumptions you made](../figures/hilbert/lessons/an-impossibility-proof-is-a-result.md)

**karp** (20)
- [Ask how hard the answer is to check before asking how hard it is to find](../figures/karp/lessons/separate-the-cost-of-checking-from-the-cost-of-finding.md)
- [Cost that scales with the magnitude of your numbers rather than the size of your data is exponential in disguise](../figures/karp/lessons/cost-must-scale-with-input-size-not-input-magnitude.md)
- [Derive the reasoning in the general setting and let only the implementation depend on your special case](../figures/karp/lessons/derive-in-the-general-setting-specialize-only-at-the-implementation.md)
- [Design the search so every step permanently retires part of the input, and the cost bound becomes a census instead of a trace](../figures/karp/lessons/make-each-step-retire-input-permanently.md)
- [Every performance claim names an adversary; know which one yours assumed](../figures/karp/lessons/know-which-adversary-your-performance-claim-is-made-against.md)
- [If the uncertainty sits where you cannot reason about it, look for a symmetry that lets you move it somewhere you can](../figures/karp/lessons/find-the-symmetry-that-relocates-the-uncertainty.md)
- [Know whether your local check certifies a global property, because that decides if hill climbing is a proof or a guess](../figures/karp/lessons/when-no-local-improvement-exists-means-globally-optimal.md)
- [Make your own behavior unpredictable instead of assuming the inputs will be kind](../figures/karp/lessons/be-unpredictable-instead-of-assuming-the-world-is-kind.md)
- [Prove you dominate a deliberately crippled version of yourself, then study the crippled version instead](../figures/karp/lessons/analyze-a-crippled-version-you-can-prove-you-dominate.md)
- [Refinement never repairs a growth rate, and a working demo on small inputs is not evidence](../figures/karp/lessons/refinement-never-repairs-a-growth-rate.md)
- [Reshape the data to fit your cheap tool's preconditions instead of reaching for a more general tool](../figures/karp/lessons/restore-the-precondition-rather-than-generalize-the-tool.md)
- [Route many problems through one universal format instead of building translators between every pair](../figures/karp/lessons/route-everything-through-one-universal-format.md)
- [Solve a coarse version first, carry the answer forward, and pay for a repair step you can bound](../figures/karp/lessons/solve-it-coarsely-then-refine-with-a-bounded-repair.md)
- [Solve a new problem by translating it into one whose difficulty you already know](../figures/karp/lessons/translate-the-new-problem-into-one-you-already-understand.md)
- [Stop optimizing the single step; find the batch of non-interfering steps and bound how many batches there are](../figures/karp/lessons/batch-non-interfering-improvements-into-phases.md)
- [Trust only the distinctions that survive a change of machine and a change of representation](../figures/karp/lessons/trust-only-classifications-that-survive-a-change-of-machine.md)
- [Weaken the problem on purpose, then prove something exact about the weakened version](../figures/karp/lessons/weaken-the-problem-on-purpose-then-prove-something-about-it.md)
- [When decisions are irrevocable and the future is unknown, redefine quality as a ratio to an oracle, then prove the ceiling so you know when to stop trying](../figures/karp/lessons/judge-irrevocable-decisions-against-an-oracle-and-prove-the-ceiling.md)
- [Where you inject randomness matters more than how much: one hidden commitment held consistently beats a fresh coin flip per decision](../figures/karp/lessons/commit-to-one-random-choice-instead-of-re-rolling-each-decision.md)
- [Wherever a method says choose any, you have a family of algorithms and you will get its worst member](../figures/karp/lessons/an-unspecified-choice-is-where-the-pathology-hides.md)

**kleene** (1)
- [Listing a set and deciding membership in it are different powers, and the bridge between them is output order](../figures/kleene/lessons/a-generator-becomes-a-decision-procedure-exactly-when-it-emits-in-order.md)

**knuth** (14)
- [A general procedure is only communicable when a concrete instance is carried alongside it](../figures/knuth/lessons/a-general-procedure-needs-a-worked-instance-to-be-understood.md)
- [A theoretical weakness is a hypothesis about your inputs — measure whether it bites before building the machinery that fixes it](../figures/knuth/lessons/a-theoretical-weakness-is-a-hypothesis-about-inputs-measure-before-you-fix-it.md)
- [A vocabulary missing a distinction does not stay silent about it — it gets abused into stating it wrongly](../figures/knuth/lessons/a-vocabulary-that-cannot-state-a-distinction-gets-abused-into-stating-it-wrongly.md)
- [An approximate quantity is a set of behaviors, so relations over it legitimately run one way only](../figures/knuth/lessons/an-approximate-quantity-is-a-set-of-behaviors-so-its-relations-run-one-way.md)
- [An incremental algorithm is licensed by an algebraic property of its domain, not by the plausibility of its steps](../figures/knuth/lessons/an-incremental-algorithm-is-licensed-by-an-algebraic-property-not-by-plausibility.md)
- [Correctness pins down a family of programs, not one program — cost is the free parameter you then choose](../figures/knuth/lessons/correctness-pins-down-a-family-of-programs-not-one-program.md)
- [Find the state that makes already-consumed input unnecessary, and a scan becomes a stream](../figures/knuth/lessons/find-the-state-that-makes-the-consumed-input-unnecessary.md)
- [How much history to keep is the design variable — deliberate forgetting is legitimate, and its price is paid in the proof](../figures/knuth/lessons/how-much-history-to-keep-is-the-design-variable-and-forgetting-is-legitimate.md)
- [Right on average is not the same as informative — the shape of the error distribution is the real question](../figures/knuth/lessons/right-on-average-is-not-informative-variance-is-the-real-question.md)
- [The primitives a notation lacks are visible as duplication in everything written in it](../figures/knuth/lessons/missing-control-flow-shows-up-as-duplicated-procedure-text.md)
- [Think in the most spartan formalism the problem fits, and let a general theorem generate the concrete algorithm](../figures/knuth/lessons/think-in-the-most-spartan-formalism-that-fits.md)
- [When a cost cannot be derived or afforded, sample it: one weighted traversal estimates a structure you can never build](../figures/knuth/lessons/sample-the-aggregate-instead-of-analyzing-or-running-it.md)
- [When a method needs a table about its own input, try computing it by running the method against itself](../figures/knuth/lessons/preprocessing-should-be-the-method-applied-to-itself.md)
- [Write the form you can prove, then transform it into the form that runs — they are different artifacts of one algorithm](../figures/knuth/lessons/write-the-provable-form-first-then-transform-it.md)

**lamport** (1)
- [Design algorithms to survive the weakest primitives you can, and count every assumption you keep](../figures/lamport/lessons/assume-the-least-from-your-primitives.md)

**liskov** (2)
- [If you can name the dependency, you do not need the coordination](../figures/liskov/lessons/if-you-can-name-the-dependency-you-do-not-need-the-coordination.md)
- [When a primitive is too expensive, find out which of its powers you actually use](../figures/liskov/lessons/when-a-primitive-is-too-expensive-ask-which-of-its-powers-you-use.md)

**lynch** (6)
- [A fault-tolerance claim is meaningless until you say when the faults are allowed to happen](../figures/lynch/lessons/impossibility-is-a-statement-about-when-the-adversary-may-act.md)
- [Check whether the impossibility is about exactness rather than difficulty, because arbitrarily close is often reachable when equal is not](../figures/lynch/lessons/impossibility-often-attaches-to-exactness-not-to-closeness.md)
- [Refusing to call a slow participant broken is what makes a fault budget mean anything](../figures/lynch/lessons/a-slow-participant-is-not-a-broken-one.md)
- [Size a robust aggregate by how far two honest observers' views can diverge, not by how many liars there are](../figures/lynch/lessons/size-a-robust-aggregate-by-how-far-two-honest-views-can-diverge.md)
- [Turn \"eventually\" into a quantity that provably shrinks, and both the deadline and the freedom to stop early follow](../figures/lynch/lessons/turn-eventually-into-a-quantity-that-shrinks.md)
- [When you cannot agree on an answer, try agreeing on who counts and derive the answer](../figures/lynch/lessons/reduce-agreement-on-data-to-agreement-on-membership.md)

**manna** (1)
- [Define the shape of a counterexample first; the proof and the checking algorithm are both readings of it](../figures/manna/lessons/the-counterexample-is-the-object-the-proof-is-its-shadow.md)

**mcmillan** (8)
- [A failed search leaves behind a reusable argument, not just a verdict](../figures/mcmillan/lessons/a-failed-search-leaves-behind-a-reusable-argument.md)
- [Buy tractability with deliberate imprecision, then pay for it with a convergence argument](../figures/mcmillan/lessons/buy-tractability-with-imprecision-then-pay-for-it-with-a-convergence-argument.md)
- [Change the representation underneath your algorithms, not the algorithms](../figures/mcmillan/lessons/change-the-representation-under-the-algorithms-not-the-algorithms.md)
- [Let cost track the description's structure, not the population it describes](../figures/mcmillan/lessons/let-cost-track-structure-not-size.md)
- [Measure the exponent of a parameterised family, not the runtime of a benchmark](../figures/mcmillan/lessons/measure-the-exponent-not-the-benchmark.md)
- [Never assemble the object you only need to interrogate; the peak intermediate is your real limit](../figures/mcmillan/lessons/the-peak-intermediate-is-the-real-limit.md)
- [Refuse to decide what nobody asked you to decide](../figures/mcmillan/lessons/refuse-to-decide-what-you-were-not-asked.md)
- [Systems are only well behaved where they can actually go](../figures/mcmillan/lessons/systems-are-only-well-behaved-where-they-can-actually-go.md)

**peter** (1)
- [To prove one level stronger than another, make it enumerate the weaker one](../figures/peter/lessons/separate-two-levels-of-power-by-making-the-higher-enumerate-the-lower.md)

**pnueli** (2)
- [Bill the unavoidable blowup to the input dimension that stays small in practice](../figures/pnueli/lessons/bill-the-blowup-to-the-dimension-that-stays-small.md)
- [Bounding the state space converts a proof obligation into a decision procedure](../figures/pnueli/lessons/bounding-the-state-space-turns-proof-into-decision.md)

**post** (5)
- [State a result in the poorest vocabulary you can, and it becomes everyone's building block](../figures/post/lessons/state-the-hard-thing-in-the-poorest-vocabulary-available.md)
- [Undecidable in general still leaves cheap answers in the cases you actually meet](../figures/post/lessons/undecidable-in-general-still-leaves-cheap-answers-in-particular.md)
- [When the comparison you need is out of reach, grade it into weaker ones you can actually make](../figures/post/lessons/grade-the-comparison-you-cannot-make-directly.md)
- [When the easiest instance resists you, stop solving and start proving impossible](../figures/post/lessons/when-the-solution-keeps-escaping-invert-the-goal.md)
- [When you cannot forbid the extra power, build the case where it is unreachable](../figures/post/lessons/starve-the-extra-power-instead-of-forbidding-it.md)

**rabin** (6)
- [Build on the operation that already is the hard problem, and pay for it in interface tidiness](../figures/rabin/lessons/build-on-the-operation-that-is-the-hard-problem.md)
- [Every capability you add is paid for in questions you can no longer answer](../figures/rabin/lessons/every-added-capability-is-paid-for-in-questions-you-can-no-longer-answer.md)
- [Give up unbounded power on purpose: a bounded state space converts infinite checks into finite ones](../figures/rabin/lessons/a-bounded-state-space-turns-infinite-checks-into-finite-ones.md)
- [Match the quantifier in your guarantee to whoever gets to pick the input](../figures/rabin/lessons/match-the-quantifier-to-whoever-picks-the-input.md)
- [Take the choice of input away from whoever benefits from choosing it](../figures/rabin/lessons/randomize-the-inputs-an-adversary-would-otherwise-choose.md)
- [When checking is cheap, guess and retry instead of constructing](../figures/rabin/lessons/when-checking-is-cheap-guess-and-retry.md)

**ritchie** (2)
- [Set a defensive parameter by paying the attacker's cost yourself, not by arguing about it](../figures/ritchie/lessons/set-the-parameter-by-paying-the-attackers-cost.md)
- [Unifying features into one mechanism buys simplicity by pinning semantics you may later need to loosen](../figures/ritchie/lessons/unification-buys-simplicity-and-forecloses-reinterpretation.md)

**stonebraker** (1)
- [Solve one case completely and make everything else reduce to it](../figures/stonebraker/lessons/solve-one-case-completely-and-make-everything-else-reduce-to-it.md)

**sutherland** (3)
- [Keep the slow general method underneath the fast special one](../figures/sutherland/lessons/keep-the-general-slow-method-under-the-fast-special-one.md)
- [Rank candidate methods by how they grow, then cut what still will not fit](../figures/sutherland/lessons/rank-candidates-by-how-they-grow-not-how-they-look-today.md)
- [Search for an evaluation order, not for the answer](../figures/sutherland/lessons/search-for-the-evaluation-order-not-the-answer.md)

**thompson** (4)
- [Carry the whole set of live possibilities forward instead of backtracking through one](../figures/thompson/lessons/carry-the-set-of-live-possibilities-forward-instead-of-backtracking.md)
- [Force the frontier to be a set and its worst case collapses to a static count](../figures/thompson/lessons/force-the-frontier-to-be-a-set-and-the-worst-case-becomes-static.md)
- [Let the machine's own dispatch be your data structure](../figures/thompson/lessons/let-the-machines-own-dispatch-be-your-data-structure.md)
- [When every intermediate result is the same kind of thing, composition rules replace case analysis](../figures/thompson/lessons/uniform-intermediate-results-turn-case-analysis-into-composition.md)

**turing** (9)
- [Calibrate against the whole space by computing its summary in closed form, never by walking it](../figures/turing/lessons/calibrate-against-a-space-too-large-to-walk.md)
- [Choose the representation in which combining results is your executor's cheapest operation](../figures/turing/lessons/choose-the-representation-where-combination-is-your-cheapest-operation.md)
- [Count what your machinery finds cheap, then recover the number you actually wanted by arithmetic](../figures/turing/lessons/count-what-is-cheap-and-invert-for-what-you-wanted.md)
- [Grant the system unlimited patience and no cleverness, to find out which of its limits are real](../figures/turing/lessons/grant-unlimited-patience-to-find-out-what-is-actually-impossible.md)
- [Isolate the part of a problem that is irreducibly a guess, then keep the rest strictly mechanical](../figures/turing/lessons/separate-the-judgement-input-from-the-mechanical-remainder.md)
- [Name the false assumption you are buying tractability with, and say where it fails](../figures/turing/lessons/name-the-false-assumption-you-are-buying-tractability-with.md)
- [Pose the question as a ratio between rival explanations so the term you cannot compute cancels](../figures/turing/lessons/pose-the-question-as-a-ratio-so-the-uncomputable-term-cancels.md)
- [Postulate the capability you lack as a primitive, then re-run your impossibility argument against the enlarged machine](../figures/turing/lessons/postulate-the-missing-capability-as-a-primitive-and-re-run-the-limit-argument.md)
- [Put a cheap approximate filter in front of the expensive procedure, and size its accuracy by the cost it saves](../figures/turing/lessons/size-the-cheap-screening-pass-by-the-cost-of-the-expensive-one.md)

**ullman** (8)
- [A cost model is a claim about which resource runs out first](../figures/ullman/lessons/a-cost-model-is-a-claim-about-what-runs-out-first.md)
- [Build the error curve you want by composing tests too weak to use alone](../figures/ullman/lessons/build-the-error-curve-you-want-from-weak-tests.md)
- [Compress so that one question survives exactly, not so the data gets smaller](../figures/ullman/lessons/compress-so-that-one-question-survives-exactly.md)
- [Compute what randomness alone would hand you, before you trust any discovery](../figures/ullman/lessons/compute-what-randomness-alone-would-hand-you.md)
- [How you combine independent estimates is part of the estimator, not a formality](../figures/ullman/lessons/how-you-combine-estimates-is-part-of-the-estimator.md)
- [Sample the entity your question quantifies over, not the records in front of you](../figures/ullman/lessons/sample-the-entity-your-question-is-about.md)
- [The dependency between inputs and outputs bounds what any parallel version can cost](../figures/ullman/lessons/what-each-output-needs-bounds-what-parallelism-can-cost.md)
- [When the exact question is provably unaffordable, change the question](../figures/ullman/lessons/when-the-exact-question-is-unaffordable-change-the-question.md)

**ungar** (1)
- [When a population's behavior is sharply split, find the cheap observable that separates it and stop treating it uniformly](../figures/ungar/lessons/stratify-a-population-by-a-cheap-predictor.md)

**von-thun** (2)
- [Abstract over the shape of the recursion, not only over its values](../figures/von-thun/lessons/abstract-over-the-shape-of-the-recursion-not-only-over-its-values.md)
- [Reinterpretation can do the work of computation — at a cost in generality](../figures/von-thun/lessons/reinterpretation-can-do-the-work-of-computation.md)
