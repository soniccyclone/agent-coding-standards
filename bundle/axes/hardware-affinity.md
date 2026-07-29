---
type: axis
title: Hardware Affinity
description: How directly a construct maps onto the physical mechanism it ultimately runs on — cache locality, register allocation, memory model — as opposed to the abstraction it's designed in.
tags: [axis, hardware, mechanism, implementation-mapping]
---

# Hardware Affinity

## Definition
How directly a construct maps onto the real, physical mechanism it must
ultimately execute on — cache locality, register allocation, memory model,
concurrency primitives actually offered by the hardware. This is the axis the
implementation-mapping layer of this corpus is organized around: design
thought happens in small-primitive-basis terms, and hardware affinity is the
axis that measures how well a given mapping from that design down onto
physical mechanism holds up — not a competing way of thinking about
programming, but the axis that scores the compilation step itself.

## Rollup
No lessons scored on this axis yet.

## Lessons scored here
269 lessons from 66 figures.

**abiteboul** (1)
- [Every detail you refuse to expose is expressive power you have spent](../figures/abiteboul/lessons/every-detail-you-refuse-to-expose-is-power-you-spend.md)

**abrial** (3)
- [Asking a question should not reveal whether the answer is stored, computed, or remembered](../figures/abrial/lessons/asking-must-not-reveal-how-the-answer-is-produced.md)
- [Begin at a level of description you cannot run, then descend along two axes that are never mixed](../figures/abrial/lessons/start-above-executability-and-descend-along-two-axes.md)
- [Every guarantee has an edge; state where it is and cover the outside with a mechanism of a different kind](../figures/abrial/lessons/name-the-edge-of-your-guarantee.md)

**bachman** (1)
- [The cost of reaching data is a designed artifact, not an inherited accident](../figures/bachman/lessons/access-cost-as-designed-artifact.md)

**backus** (5)
- [An abstraction is rented against whatever overhead the current hardware still hides](../figures/backus/lessons/abstraction-is-rented-against-the-overhead-the-hardware-hides.md)
- [Audit the machine model a language commits you to before comparing its features](../figures/backus/lessons/audit-the-machine-model-a-language-commits-you-to-before-its-features.md)
- [Give up the expectation that output resembles input, and whole-program optimization becomes available](../figures/backus/lessons/give-up-local-correspondence-to-optimize-the-whole.md)
- [Solve the problem against an unlimited resource, then treat scarcity as a separate stage](../figures/backus/lessons/solve-against-an-idealized-resource-then-map-scarcity-separately.md)
- [When the right static decision depends on unknowable dynamics, estimate the dynamics instead of assuming them away](../figures/backus/lessons/estimate-the-dynamics-you-cannot-prove.md)

**boehm** (1)
- [A practice is a fit to conditions, and the conditions move](../figures/boehm/lessons/a-practice-is-a-fit-to-conditions-that-move.md)

**booch** (2)
- [Before you optimize anything, identify which layer your binding constraint actually sits on](../figures/booch/lessons/find-which-layer-your-real-constraint-lives-on.md)
- [Computation and the data it consumes have physical cost, and that cost belongs in the design, not in a footnote](../figures/booch/lessons/computation-has-weight-and-data-has-mass.md)

**brinch-hansen** (5)
- [Cut module boundaries where simultaneity demands them, not where the data would suggest](../figures/brinch-hansen/lessons/cut-boundaries-where-simultaneity-demands.md)
- [Design the machine you wish you had been given, then hold the layer above it to explaining itself without ever mentioning it](../figures/brinch-hansen/lessons/design-the-machine-under-the-language.md)
- [Look for the concept that erases a boundary, because whatever sits on either side then becomes substitutable](../figures/brinch-hansen/lessons/erase-the-boundary-to-gain-substitutability.md)
- [Systems code earns no exemption from the disciplines you would demand of any other program](../figures/brinch-hansen/lessons/systems-code-earns-no-exemption.md)
- [Trade generality for tractability on purpose, and keep a ledger of what the trade cost you](../figures/brinch-hansen/lessons/trade-generality-for-tractability-on-purpose.md)

**brooks** (5)
- [A design is only good relative to alternatives costing the same, and the metric that decides belongs at the level of the user's result, not the component's](../figures/brooks/lessons/compare-only-against-equal-cost-alternatives.md)
- [Commit to what a thing does and refuse to commit to how, because the visible contract must outlive every mechanism that satisfies it](../figures/brooks/lessons/commit-to-the-interface-and-leave-the-mechanism-free.md)
- [State what you do not guarantee as carefully as what you do, and make the mechanism reject it, or the running implementation becomes the specification](../figures/brooks/lessons/specify-the-undefined-and-trap-it-in-the-mechanism.md)
- [The leverage lives in how the data is represented; when a program resists, stop reading the logic and go look at the tables](../figures/brooks/lessons/study-the-data-before-the-control-flow.md)
- [The parts of a system improve at different speeds, so put the seams where the rates diverge and keep spare room in every vocabulary you fix](../figures/brooks/lessons/design-where-the-rates-of-change-differ.md)

**cardelli** (5)
- [Buy performance with an invariant your own semantics guarantees, and quarantine the exceptions rather than generalizing](../figures/cardelli/lessons/buy-speed-with-an-invariant-the-semantics-guarantees.md)
- [Collapsing two levels to save concepts also destroys the questions those levels let you answer](../figures/cardelli/lessons/collapsing-two-levels-forfeits-the-decisions-above-them.md)
- [Identify the operation your programs perform constantly, make it cheap, and factor it so common sequences cancel](../figures/cardelli/lessons/make-the-hot-operation-cheap-and-let-composites-cancel.md)
- [Minimality is owed by the layer you reason in, speed by the layer you run on, and neither should be asked of the other](../figures/cardelli/lessons/each-layer-owes-a-different-virtue.md)
- [State the semantics over the mechanism you will actually run, so the theorem covers the thing you ship](../figures/cardelli/lessons/prove-it-about-the-machine-you-will-actually-run.md)

**chaitin** (1)
- [Price a restriction instead of judging how restrictive it feels](../figures/chaitin/lessons/price-a-restriction-do-not-feel-it.md)

**chamberlin** (1)
- [Give performance tuning its own channel, and admit nothing into it that carries information](../figures/chamberlin/lessons/give-tuning-its-own-channel-that-carries-no-meaning.md)

**chen** (1)
- [Never let one mark carry both a claim about the world and a route through the machine](../figures/chen/lessons/keep-what-is-true-separate-from-how-it-is-reached.md)

**chuck-moore** (5)
- [Accept a restriction that makes the bookkeeping vanish rather than a generality that makes it permanent](../figures/chuck-moore/lessons/choose-the-restricted-regime-whose-bookkeeping-disappears.md)
- [Count the layers standing between you and the machine, because each one silently sets your limits](../figures/chuck-moore/lessons/every-intervening-layer-is-a-tax-you-cannot-audit.md)
- [Knowing exactly how something will be used is worth more than a general solution written by someone who did not](../figures/chuck-moore/lessons/code-written-for-this-use-beats-general-code-you-inherit.md)
- [The price of combining two pieces of code determines how well a system will be factored](../figures/chuck-moore/lessons/cheap-composition-makes-factoring-the-default.md)
- [When the notation and the mechanism are designed together, the translation between them stops existing](../figures/chuck-moore/lessons/design-the-notation-and-the-machine-as-one-artifact.md)

**clarke** (1)
- [When scale defeats you, attack the representation before the algorithm](../figures/clarke/lessons/attack-the-representation-before-the-algorithm.md)

**cook** (3)
- [A construction with no bound on its cost is not usable knowledge, so put the budget inside the definition](../figures/cook/lessons/a-method-without-a-resource-bound-is-not-a-method.md)
- [An abstraction is only worth reasoning in if its lowering preserves cost, and a concept is only objective if every reasonable translation preserves it](../figures/cook/lessons/an-abstraction-worth-reasoning-in-preserves-its-cost.md)
- [Price each primitive operation at what the physical machine would really pay, or your analysis describes a machine that cannot exist](../figures/cook/lessons/charge-for-the-work-the-machine-actually-does.md)

**corbato** (6)
- [A Name Where an Address Would Go](../figures/corbato/lessons/a-name-where-an-address-would-go.md)
- [Build the Frame Along the Axis Change Arrives On](../figures/corbato/lessons/build-the-frame-along-the-axis-change-arrives-on.md)
- [Complexity Lives in the Decomposition](../figures/corbato/lessons/complexity-lives-in-the-decomposition.md)
- [Design the Region Past Saturation](../figures/corbato/lessons/design-the-region-past-saturation.md)
- [Efficiency Is Usually Paid For in Redundancy You Were Not Tracking](../figures/corbato/lessons/efficiency-is-usually-paid-for-in-redundancy.md)
- [The Machine Should Wait for the Person](../figures/corbato/lessons/the-machine-should-wait-for-the-person.md)

**cox** (2)
- [Build the mechanism on the event the machine can actually observe](../figures/cox/lessons/build-the-mechanism-on-what-the-machine-can-actually-observe.md)
- [Deciding when a connection is checked decides who is allowed to make it](../figures/cox/lessons/binding-time-belongs-to-the-consumer-not-the-producer.md)

**cutler** (10)
- [An interface is a promise about every future implementation, so whatever it leaves unsaid is where incompatibility will grow](../figures/cutler/lessons/an-architecture-is-a-promise-across-implementations.md)
- [Any behavior you put in shared implicit state serializes every operation that reads it; encode it in the operation instead](../figures/cutler/lessons/implicit-mode-state-serializes-what-touches-it.md)
- [As a system's defects thin out, the survivors are almost all synchronization, so design for concurrency at the start or not at all](../figures/cutler/lessons/synchronization-is-where-the-residual-bugs-live.md)
- [Compatibility with what already runs is the mass of a system, and the only way to carry it is at a boundary you design on purpose](../figures/cutler/lessons/compatibility-is-the-mass-of-a-system.md)
- [Enumerate the mechanisms your abstraction silently requires from the layer beneath it, then price their absence as recurring](../figures/cutler/lessons/inventory-what-your-abstraction-demands-from-below.md)
- [Minimality is a means, and treating it as the goal loses to whoever spends their budget on outcomes instead](../figures/cutler/lessons/minimality-is-not-the-objective-function.md)
- [Portability comes from naming the seam where the machine shows through, not from hiding the machine](../figures/cutler/lessons/name-the-seam-where-the-machine-shows-through.md)
- [The fastest route to a working model of a system is being forced to explain its failures](../figures/cutler/lessons/learn-a-system-by-hunting-why-it-fails.md)
- [Turn a global limit into per-owner budgets before anyone writes code](../figures/cutler/lessons/turn-a-global-limit-into-per-owner-budgets.md)
- [When predictability is the requirement, remove the sharing instead of scheduling it better](../figures/cutler/lessons/partition-instead-of-scheduling-when-predictability-is-the-product.md)

**dahl** (3)
- [Let the machine's cost model set the grain of your abstractions, and refuse any mechanism whose expense is invisible to whoever uses it](../figures/dahl/lessons/let-the-machines-cost-model-set-the-grain-of-your-abstractions.md)
- [Refuse expressive power whose cost is invisible at the point where it is used](../figures/dahl/lessons/refuse-power-whose-cost-is-invisible.md)
- [When safety and flexibility seem to trade off, the fix is more structure in the type space, not a weaker check](../figures/dahl/lessons/give-the-checker-a-hierarchy-instead-of-loosening-it.md)

**date** (2)
- [Choose the grain of your operators and you choose who owns performance](../figures/date/lessons/choose-the-grain-of-your-operators-and-you-choose-who-owns-performance.md)
- [Get the abstract machine right before you earn the right to optimize](../figures/date/lessons/get-the-abstract-machine-right-before-you-earn-the-right-to-optimize.md)

**denning** (8)
- [A single parameter pulled by two objectives with distant optima cannot be tuned, only split](../figures/denning/lessons/one-knob-two-objectives.md)
- [Differentiate before you tune: a large hardware ratio can leave no safe operating margin at all](../figures/denning/lessons/sensitivity-before-tuning.md)
- [Find out which variable the outcome actually obeys before improving the one you find interesting](../figures/denning/lessons/measure-which-variable-the-outcome-obeys.md)
- [Give the hand-waved quantity a one-parameter definition, then make its consequences derivable](../figures/denning/lessons/define-then-derive.md)
- [Idle capacity in one resource is usually a symptom of scarcity in another](../figures/denning/lessons/idle-capacity-names-the-real-shortage.md)
- [Knowing what will be needed is not permission to fetch it early](../figures/denning/lessons/speculation-defeated-by-its-own-trigger.md)
- [When a technique 'doesn't work,' suspect the relation between its parts before condemning any one part](../figures/denning/lessons/failure-lives-in-the-relation.md)
- [When composition destroys foreknowledge, build an observer instead of a predictor](../figures/denning/lessons/observing-beats-preplanning.md)

**dijkstra** (2)
- [Make cooperating processes correct under every speed ratio, because timing assumptions are hidden coupling](../figures/dijkstra/lessons/never-let-correctness-depend-on-timing.md)
- [Structure a system as a stack of complete machines, each one abstracting a physical resource out of existence](../figures/dijkstra/lessons/build-systems-as-layers-of-complete-machines.md)

**dolev** (4)
- [A tight bound on one resource says nothing about the resource that decides feasibility](../figures/dolev/lessons/count-the-resource-the-machine-actually-spends.md)
- [A worst-case bound is a statement about the worst case, not a licence to charge for it every time](../figures/dolev/lessons/make-the-bill-track-the-run-you-actually-had.md)
- [An omnibus assumption hides several independent dials; separate them before believing anything proved about it](../figures/dolev/lessons/split-omnibus-assumptions-into-independent-dials.md)
- [Fault tolerance is purchased with two separate redundancies, and no protocol can substitute for either](../figures/dolev/lessons/tolerance-is-bought-with-population-and-with-independent-paths.md)

**edmonds** (4)
- [Find what your subroutine's answers are invariant under, then use that freedom to keep its input inside the regime where it is cheap](../figures/edmonds/lessons/keep-the-data-inside-your-subroutines-cheap-regime.md)
- [Measure input size by what it takes to write the input down, including the precision of its numbers, or your cost bound is fiction](../figures/edmonds/lessons/measure-input-by-what-it-takes-to-write-down.md)
- [When cost tracks the magnitude of your numbers, restructure the computation to follow their digits: solve a coarse version, then refine, and bound how far each answer can be from the next](../figures/edmonds/lessons/let-the-computation-follow-the-digits-of-its-data.md)
- [Whether an affordable method exists at all is a claim you can prove or refute, so state it and pick a cost measure that cannot be gamed](../figures/edmonds/lessons/prove-that-an-affordable-method-exists.md)

**emerson** (2)
- [Pick the abstraction from the property you intend to check, then own the claim that it is faithful](../figures/emerson/lessons/the-abstraction-you-check-is-a-claim-about-the-real-artifact.md)
- [When a search space explodes, change how you represent it rather than how you search it](../figures/emerson/lessons/attack-blowup-at-the-representation-not-the-search.md)

**fagin** (4)
- [A guarantee proved without a finiteness assumption may not survive one](../figures/fagin/lessons/a-guarantee-proved-without-finiteness-may-not-survive-finiteness.md)
- [Define goodness in terms of the constraints your mechanism already enforces for free](../figures/fagin/lessons/define-goodness-in-terms-of-what-the-mechanism-already-enforces.md)
- [The static shape of a model decides which execution costs are even possible](../figures/fagin/lessons/the-static-shape-of-a-model-decides-what-execution-costs-are-possible.md)
- [\"A good option exists\" and \"you cannot go wrong\" are different guarantees, and only the second licenses delegation](../figures/fagin/lessons/a-good-option-exists-versus-you-cannot-go-wrong.md)

**fischer** (2)
- [Optimal means nothing until you name the resource, and the winner on one resource can be absurd on another](../figures/fischer/lessons/optimal-is-meaningless-until-you-name-the-resource.md)
- [Without a timing assumption, slow and dead are the same observation](../figures/fischer/lessons/a-slow-participant-and-a-dead-one-are-the-same-observation.md)

**floyd** (2)
- [The properties that make a notation readable are the same ones that make it cheap to process, so design for the tractable case instead of the general one](../figures/floyd/lessons/what-makes-a-notation-readable-makes-it-cheap-to-process.md)
- [Write the program for the machine you wish you had, and make the gap down to the real one mechanical](../figures/floyd/lessons/write-for-the-machine-you-wish-you-had-then-translate.md)

**gang-of-four** (1)
- [Whether a thing can be shared is decided entirely by whether it remembers its context](../figures/gang-of-four/lessons/context-dependence-is-what-forbids-sharing.md)

**girard** (3)
- [An answer and the question it answers are different objects — a formalism that identifies them has thrown away the half you get paid for](../figures/girard/lessons/an-answer-is-not-the-question-it-answers.md)
- [Treat copying and discarding as operations that must be licensed, not as background privileges of notation](../figures/girard/lessons/make-copying-and-discarding-cost-something-visible.md)
- [Which functions a system can compute is the boring question — judge it by which algorithms it lets you write, and what they cost](../figures/girard/lessons/judge-a-formalism-by-its-algorithms-not-its-functions.md)

**goldberg** (5)
- [A specification is finished when a stranger can rebuild the machine from it — which means fixing behavior and leaving code shape free](../figures/goldberg/lessons/a-spec-is-done-when-a-stranger-can-rebuild-the-machine.md)
- [Reach the machine through the abstraction, not around it: build the escape hatch so the model never notices](../figures/goldberg/lessons/escape-hatches-to-the-machine-that-stay-inside-the-model.md)
- [Refuse privileged tiers: make one mechanism cover everything, and accept the implementation bill on the expectation that technique will pay it down](../figures/goldberg/lessons/buy-uniformity-and-pay-the-implementation-bill.md)
- [Settle performance by measurement, using an instrument built out of the system rather than bolted onto it](../figures/goldberg/lessons/measure-before-optimizing-with-instruments-made-of-the-system.md)
- [Treat response time and bandwidth as properties of what can be thought, not as performance numbers to tune later](../figures/goldberg/lessons/latency-and-bandwidth-are-semantic-properties.md)

**hartmanis** (7)
- [Anything a bounded re-encoding can buy you was never part of the structure](../figures/hartmanis/lessons/what-a-bounded-re-encoding-buys-is-not-structure.md)
- [Bound the size of the answer and you have bounded every algorithm at once](../figures/hartmanis/lessons/bound-the-answer-before-bounding-the-algorithm.md)
- [Judge a hardware feature by what it costs to fake it, and distinguish faster lookup from faster construction](../figures/hartmanis/lessons/ask-what-it-costs-to-fake-the-feature.md)
- [Small local steps are what give you leverage over a computation, so never abstract them away](../figures/hartmanis/lessons/locality-of-small-steps-is-the-leverage.md)
- [The interesting structure begins after you already know a thing is computable](../figures/hartmanis/lessons/the-interesting-structure-begins-after-computability.md)
- [To prove something cannot be done, count the distinctions the machine must carry](../figures/hartmanis/lessons/count-the-distinctions-a-machine-must-carry.md)
- [Whether a constant factor is noise is a fact about your machine model, not about computation](../figures/hartmanis/lessons/whether-a-constant-factor-is-noise-depends-on-the-machine.md)

**herlihy** (10)
- [A guarantee that is sound in the step-counting model can be the wrong engineering choice; go measure](../figures/herlihy/lessons/asymptotically-adequate-is-not-practically-adequate.md)
- [A mechanism with a physical limit is only usable if the limit is part of its published contract](../figures/herlihy/lessons/a-bounded-mechanism-must-publish-its-bound.md)
- [Before adding a mechanism, ask whether the machine already computes the predicate you need](../figures/herlihy/lessons/the-machine-may-already-be-computing-the-predicate-you-need.md)
- [If your code may be run speculatively, it must be defined on states that could never legally occur](../figures/herlihy/lessons/speculative-execution-demands-code-that-is-total-over-nonsense.md)
- [Look for the one primitive that closes an entire design space instead of solving instances of it](../figures/herlihy/lessons/find-the-primitive-that-closes-the-whole-space.md)
- [Make progress a guarantee the shared object owes each caller, not a favor its callers do each other](../figures/herlihy/lessons/make-progress-a-guarantee-the-object-owes-each-caller.md)
- [Measure a synchronization primitive by how much agreement it can manufacture, not by how much it can compute](../figures/herlihy/lessons/measure-a-primitive-by-the-agreement-it-can-manufacture.md)
- [Once two primitives are both powerful enough, choose between them by what they can detect](../figures/herlihy/lessons/above-the-power-threshold-choose-primitives-by-what-they-detect.md)
- [The bookkeeping a mechanism needs is a cost of the mechanism, not of the problem](../figures/herlihy/lessons/auxiliary-state-is-a-cost-of-the-mechanism-not-the-problem.md)
- [When the machine's atomic unit is narrower than your invariant, restructure the data until the invariant fits behind one reference](../figures/herlihy/lessons/group-an-invariant-behind-one-reference-when-the-atomic-unit-is-too-narrow.md)

**hilbert** (1)
- [Nothing you actually run is infinite; every guarantee has to be cashed out against the finite mechanism](../figures/hilbert/lessons/cash-out-the-idealization-against-the-finite-machine.md)

**karp** (4)
- [Cost that scales with the magnitude of your numbers rather than the size of your data is exponential in disguise](../figures/karp/lessons/cost-must-scale-with-input-size-not-input-magnitude.md)
- [Design the search so every step permanently retires part of the input, and the cost bound becomes a census instead of a trace](../figures/karp/lessons/make-each-step-retire-input-permanently.md)
- [Refinement never repairs a growth rate, and a working demo on small inputs is not evidence](../figures/karp/lessons/refinement-never-repairs-a-growth-rate.md)
- [Trust only the distinctions that survive a change of machine and a change of representation](../figures/karp/lessons/trust-only-classifications-that-survive-a-change-of-machine.md)

**kleene** (1)
- [Canonical form buys you the proof, not the artifact — and the compiled shape follows the shape you wrote](../figures/kleene/lessons/canonical-forms-buy-proofs-not-artifacts.md)

**knuth** (2)
- [Find the state that makes already-consumed input unnecessary, and a scan becomes a stream](../figures/knuth/lessons/find-the-state-that-makes-the-consumed-input-unnecessary.md)
- [Write the form you can prove, then transform it into the form that runs — they are different artifacts of one algorithm](../figures/knuth/lessons/write-the-provable-form-first-then-transform-it.md)

**lamport** (2)
- [Correct parts do not make a correct whole; name the composition condition and price it](../figures/lamport/lessons/local-correctness-does-not-compose.md)
- [Design algorithms to survive the weakest primitives you can, and count every assumption you keep](../figures/lamport/lessons/assume-the-least-from-your-primitives.md)

**lampson** (9)
- [An abstraction exists to erase the properties you don't want, so anything good underneath must survive the trip upward](../figures/lampson/lessons/abstraction-should-erase-defects-not-capabilities.md)
- [An indirection is only real if absence is representable and detectable; without a fault on 'not here yet' you must materialize everything in advance, and that eagerness spreads into layers with no business knowing](../figures/lampson/lessons/indirection-you-cannot-fault-on-is-not-indirection.md)
- [Designate exactly one representation as authoritative, optimize it for being checkable rather than for being fast, and let every faster structure be a guess you are allowed to discard](../figures/lampson/lessons/put-the-truth-in-one-place-and-let-everything-faster-be-a-guess.md)
- [Every shared mechanism is a communication channel, so a component's real interface is everything an observer can measure about its execution — and containment becomes a quantity, not a yes or no](../figures/lampson/lessons/every-shared-mechanism-is-a-channel.md)
- [Mutual exclusion between participants of very different speeds destroys the fast one's worst-case guarantee, so a speed boundary is where a coordination model has to change](../figures/lampson/lessons/never-share-exclusion-across-a-speed-boundary.md)
- [Spend the expensive agreement on who is allowed to decide, not on each decision — and notice that the cheap path then rests on a physical assumption, not a logical one](../figures/lampson/lessons/spend-agreement-on-who-decides-not-on-what-is-decided.md)
- [The measured price of a primitive decides which program structures are available to you, so publish the price and treat granularity as a consequence of it](../figures/lampson/lessons/the-price-of-a-primitive-decides-which-structures-you-can-think-in.md)
- [The normal case and the worst case are two different design problems with two different success criteria, and one mechanism serving both will serve neither](../figures/lampson/lessons/normal-and-worst-case-are-two-different-design-problems.md)
- [When a field is full of rival mechanisms, look for the single relation they are all storing, then treat each mechanism as a layout choice for it](../figures/lampson/lessons/rival-mechanisms-are-often-storage-layouts-of-one-relation.md)

**landin** (2)
- [Ask what an apparently non-denotable construct stands for; the answer is the surrounding situation it silently refers to](../figures/landin/lessons/ask-what-the-unaskable-thing-denotes.md)
- [To understand a computation mechanically, turn everything implicit about it into named parts of an explicit state](../figures/landin/lessons/make-the-implicit-context-of-execution-into-explicit-data.md)

**liskov** (7)
- [Cut the hard problem out of scope on purpose, and ship the mechanism you can implement simply](../figures/liskov/lessons/cut-the-hard-problem-out-of-scope-on-purpose.md)
- [Hide the mechanism and the location; never hide the possibility of failure or the cost](../figures/liskov/lessons/hide-the-mechanism-never-the-possibility-of-failure.md)
- [Independence of failure is something you build, not a number you pick](../figures/liskov/lessons/independence-of-failure-is-built-not-assumed.md)
- [Let logical structure and physical structure diverge, and make the compiler own the gap](../figures/liskov/lessons/logical-structure-and-physical-structure-are-allowed-to-diverge.md)
- [Never let a timing guess be load-bearing for correctness; spend it on progress instead](../figures/liskov/lessons/never-let-a-timing-guess-be-load-bearing-for-correctness.md)
- [Never show anyone an effect that is less durable than the promise you made about it](../figures/liskov/lessons/never-show-anyone-an-effect-less-durable-than-your-promise.md)
- [When a primitive is too expensive, find out which of its powers you actually use](../figures/liskov/lessons/when-a-primitive-is-too-expensive-ask-which-of-its-powers-you-use.md)

**lynch** (3)
- [A distributed algorithm can only depend on what its participants can actually tell apart](../figures/lynch/lessons/correctness-can-only-rest-on-what-a-process-can-distinguish.md)
- [A fault-tolerance claim is meaningless until you say when the faults are allowed to happen](../figures/lynch/lessons/impossibility-is-a-statement-about-when-the-adversary-may-act.md)
- [Refusing to call a slow participant broken is what makes a fault budget mean anything](../figures/lynch/lessons/a-slow-participant-is-not-a-broken-one.md)

**manna** (2)
- [A fairness assumption is a debt someone has to implement, not a fact about the world](../figures/manna/lessons/a-fairness-assumption-is-a-debt-someone-must-implement.md)
- [Somebody progresses and everybody progresses are different guarantees, and which one you can have is decided by your primitive](../figures/manna/lessons/somebody-progresses-and-everybody-progresses-are-different-guarantees.md)

**mccarthy** (7)
- [If a bookkeeping fact is derivable from the program's own structure, make the machine derive it instead of making the programmer track it](../figures/mccarthy/lessons/let-the-machine-compute-what-the-machine-can-know.md)
- [In a self-hosted system the fast artifact is a cache, so name the high-level definitions as the only place a change may enter](../figures/mccarthy/lessons/the-fast-artifact-is-a-cache-changes-enter-through-the-definitions.md)
- [State the criterion before the method, and a translator's correctness becomes an equation between two routes rather than a matter of testing](../figures/mccarthy/lessons/translation-correctness-is-a-commuting-equation.md)
- [Turn the mutable environment into a single value with stated laws, and imperative code becomes reasonable by the same means as functional code](../figures/mccarthy/lessons/make-the-mutable-environment-a-value-with-laws.md)
- [Two formalisms of identical power can still be unequal designs: judge a basis by which operations it makes elementary](../figures/mccarthy/lessons/equal-power-is-not-equal-structure.md)
- [When an abstraction cannot be uniformly cheap, expose its cost tiers as declarations rather than picking one price and hiding it](../figures/mccarthy/lessons/make-the-cost-tier-a-declaration-instead-of-a-hidden-uniform-choice.md)
- [When the machine forecloses an option, check whether what survived is cleaner before you mourn the loss](../figures/mccarthy/lessons/let-the-machine-prune-your-primitives.md)

**mcmillan** (5)
- [Let cost track the description's structure, not the population it describes](../figures/mcmillan/lessons/let-cost-track-structure-not-size.md)
- [Measure the exponent of a parameterised family, not the runtime of a benchmark](../figures/mcmillan/lessons/measure-the-exponent-not-the-benchmark.md)
- [Never assemble the object you only need to interrogate; the peak intermediate is your real limit](../figures/mcmillan/lessons/the-peak-intermediate-is-the-real-limit.md)
- [Separate the structure that is in the system from the structure your model imposes on it](../figures/mcmillan/lessons/separate-structure-in-the-system-from-structure-your-model-imposes.md)
- [Systems are only well behaved where they can actually go](../figures/mcmillan/lessons/systems-are-only-well-behaved-where-they-can-actually-go.md)

**nygaard** (1)
- [Constrain What A Pointer May Denote, And Check At Runtime What You Cannot Prove](../figures/nygaard/lessons/qualified-references-bound-wrong-assumptions.md)

**parnas** (3)
- [A module is an assignment of responsibility, not a unit of the running program](../figures/parnas/lessons/modules-are-responsibility-assignments-not-runtime-objects.md)
- [A program can be entirely correct and still have decayed into worthlessness](../figures/parnas/lessons/a-correct-program-can-still-lose-all-its-value.md)
- [Write down where your dividing criterion goes fuzzy, and name the arbiter that settles it](../figures/parnas/lessons/name-the-places-your-criterion-breaks-down.md)

**pike** (4)
- [An abstraction that wins erases the variety it served](../figures/pike/lessons/an-abstraction-that-wins-erases-the-variety-it-served.md)
- [Changing a type does not find the assumptions it breaks](../figures/pike/lessons/changing-a-type-does-not-find-the-assumptions-it-breaks.md)
- [Put the fix where it belongs, even if that means owning more](../figures/pike/lessons/put-the-fix-where-it-belongs-even-if-that-means-owning-more.md)
- [Spend a representation's design budget on what stays correct](../figures/pike/lessons/spend-the-representations-design-budget-on-what-stays-correct.md)

**pnueli** (1)
- [A specification must fix what the implementation is allowed to know, and when](../figures/pnueli/lessons/a-specification-must-fix-what-is-knowable-when.md)

**post** (2)
- [Choose primitives for fidelity to whoever executes them, then earn expressiveness by reduction](../figures/post/lessons/pick-primitives-by-fidelity-to-the-executing-agent.md)
- [Trace a boundary problem back to the idealization that caused it](../figures/post/lessons/an-idealization-you-cannot-supply-becomes-an-interface-bug.md)

**rabin** (2)
- [Build on the operation that already is the hard problem, and pay for it in interface tidiness](../figures/rabin/lessons/build-on-the-operation-that-is-the-hard-problem.md)
- [Give up unbounded power on purpose: a bounded state space converts infinite checks into finite ones](../figures/rabin/lessons/a-bounded-state-space-turns-infinite-checks-into-finite-ones.md)

**rashid** (6)
- [A capacity limit low in the system reappears as permanent structural complexity everywhere above it](../figures/rashid/lessons/a-capacity-limit-low-down-becomes-structural-complexity-everywhere-above.md)
- [A portability boundary holds only when the machine-specific side owns no truth and can be thrown away and rebuilt](../figures/rashid/lessons/keep-truth-in-the-portable-layer-and-let-the-machine-layer-be-a-discardable-cache.md)
- [An abstraction everyone knows is slow is usually just the one the hardware was never tuned for](../figures/rashid/lessons/an-abstraction-known-to-be-slow-is-usually-just-the-one-the-hardware-was-not-tuned-for.md)
- [Choose the semantics you can reason about, then buy the cost back underneath where nobody has to know](../figures/rashid/lessons/choose-the-semantics-you-can-reason-about-and-buy-the-cost-back-underneath.md)
- [When an abstraction is too expensive to use the way the problem wants, look for two concerns fused inside it](../figures/rashid/lessons/split-the-abstraction-that-bundles-ownership-with-execution.md)
- [Whether a design survives is decided outside its own quality: does it match the next machine, and can it host the software that already exists](../figures/rashid/lessons/a-design-survives-by-matching-the-next-machine-and-hosting-the-existing-software.md)

**reenskaug** (2)
- [Announce change at the granularity of intent, not of mutation](../figures/reenskaug/lessons/notify-at-the-granularity-of-intent-not-of-mutation.md)
- [Derivability, not layering etiquette, decides which side of a boundary a piece of state belongs on](../figures/reenskaug/lessons/derivability-decides-which-side-of-a-boundary-state-lives-on.md)

**ritchie** (6)
- [A feature that will not fit is evidence against your model, not a case for a special rule](../figures/ritchie/lessons/a-feature-that-will-not-fit-indicts-the-model.md)
- [Know in advance which measurements could change your decision, and say so when none of them could](../figures/ritchie/lessons/know-which-measurements-can-change-a-decision.md)
- [Mark where the specification stops and the machine begins, and classify each divergence by what should happen to it](../figures/ritchie/lessons/mark-where-the-spec-stops-and-the-machine-begins.md)
- [Pick the representation whose global invariant is cheap to check, not the one that reads best](../figures/ritchie/lessons/pick-representations-whose-invariants-are-cheap-to-check.md)
- [Set a defensive parameter by paying the attacker's cost yourself, not by arguing about it](../figures/ritchie/lessons/set-the-parameter-by-paying-the-attackers-cost.md)
- [Unifying features into one mechanism buys simplicity by pinning semantics you may later need to loosen](../figures/ritchie/lessons/unification-buys-simplicity-and-forecloses-reinterpretation.md)

**royce** (2)
- [Allocate the scarce resource before detailed work spends it for you](../figures/royce/lessons/allocate-the-scarce-resource-before-detail-spends-it.md)
- [Separate what you can compute from what you can only observe](../figures/royce/lessons/separate-what-you-can-compute-from-what-you-can-only-observe.md)

**saltzer** (5)
- [Decide up front what your overhead is allowed to scale with](../figures/saltzer/lessons/decide-up-front-what-your-overhead-is-allowed-to-scale-with.md)
- [Hold the privileged code to the same discipline as the rest](../figures/saltzer/lessons/hold-the-privileged-code-to-the-same-discipline-as-the-rest.md)
- [Interface conveniences are billed to the implementation](../figures/saltzer/lessons/interface-conveniences-are-billed-to-the-implementation.md)
- [Keep only the state you could not rebuild](../figures/saltzer/lessons/keep-only-the-state-you-could-not-rebuild.md)
- [Sort problems by whether better technology would erase them](../figures/saltzer/lessons/sort-problems-by-whether-better-technology-would-erase-them.md)

**schneider** (6)
- [Compare two architectures by which event fires their expensive operation, not by how expensive the operation is](../figures/schneider/lessons/compare-designs-by-what-triggers-the-expensive-operation.md)
- [Noticing a fault is cheaper than surviving one, so buy redundancy per layer instead of uniformly](../figures/schneider/lessons/detect-cheaply-mask-expensively.md)
- [Redundancy is unfinished until you can name who does the final combining, and shared fate can make a component free](../figures/schneider/lessons/follow-the-single-failure-argument-past-the-system-edge.md)
- [The cheapest message is the one nobody sends: elapsed time can carry information if you have paid for synchrony](../figures/schneider/lessons/silence-as-a-channel.md)
- [The cost of coordination is set by the size of its audience, so shrink the audience before tuning the protocol](../figures/schneider/lessons/shrink-the-audience-before-optimizing-the-protocol.md)
- [When an ideal is unbuildable, keep its interface and make the gap a parameter](../figures/schneider/lessons/index-an-unreachable-abstraction-by-its-breaking-point.md)

**steele** (10)
- [A description of a thing is not the thing; specify a constructor by the behaviour it must yield, never by the form it must produce](../figures/steele/lessons/specify-a-constructor-by-the-behaviour-it-must-yield-not-the-form.md)
- [Advice you attach to a program must never change what a correct program means, and the exceptions must be countable on one hand](../figures/steele/lessons/annotations-must-be-strippable-and-the-exceptions-countable-on-one-hand.md)
- [Judge a control structure by how its state grows, not by whether the code appears to call itself](../figures/steele/lessons/iteration-is-a-property-of-reduction-shape-not-of-syntax.md)
- [Pick the binding rule that keeps your reasoning laws true, then check the cost model before believing it is expensive](../figures/steele/lessons/choose-the-binding-rule-that-keeps-your-reasoning-laws-true.md)
- [Refuse to specify the things you do not want depended on, even when every implementation agrees on them](../figures/steele/lessons/refuse-to-specify-what-you-do-not-want-depended-on.md)
- [Separate the values a type denotes from the representations a machine may use for it, and let code declare whether it wants the latitude](../figures/steele/lessons/separate-the-values-a-type-denotes-from-the-representation-permitted-at-runtime.md)
- [The features that move a proof obligation onto the programmer are the ones that need the most formal precision, not the least](../figures/steele/lessons/an-unsafe-escape-hatch-needs-more-formal-precision-than-a-safe-feature.md)
- [Think of a value as acquiring names rather than a name as acquiring values](../figures/steele/lessons/values-acquire-names-names-do-not-acquire-values.md)
- [When an abstraction is expensive, the defect is in the implementation; do not teach programmers to hand-compile around it](../figures/steele/lessons/fix-the-implementation-not-the-language.md)
- [You cannot implement a mechanism more general than the host mechanism you borrowed to implement it](../figures/steele/lessons/never-inherit-the-mechanism-you-are-trying-to-generalize.md)

**stonebraker** (12)
- [A live copy can replace a record of the past](../figures/stonebraker/lessons/a-live-copy-can-replace-a-record-of-the-past.md)
- [A retrofitted opposite is always a second-class citizen](../figures/stonebraker/lessons/a-retrofitted-opposite-is-always-a-second-class-citizen.md)
- [A stable interface is a license to rebuild everything beneath it](../figures/stonebraker/lessons/a-stable-interface-is-a-license-to-rebuild-everything-beneath-it.md)
- [Ask which side holds still — the data or the question](../figures/stonebraker/lessons/ask-which-side-holds-still-the-data-or-the-question.md)
- [Decide where in a data set's life you pay the cost](../figures/stonebraker/lessons/decide-where-in-a-data-set-s-life-you-pay-the-cost.md)
- [Design against the ratio between resources, not their absolute speed](../figures/stonebraker/lessons/design-against-the-ratio-between-resources-not-their-absolute-speed.md)
- [Measure useful work as a fraction of runtime](../figures/stonebraker/lessons/measure-useful-work-as-a-fraction-of-runtime.md)
- [Never schedule the cleanup below the work that depends on it](../figures/stonebraker/lessons/never-schedule-the-cleanup-below-the-work-that-depends-on-it.md)
- [Separate the model from the implementation before you blame either](../figures/stonebraker/lessons/separate-the-model-from-the-implementation-before-you-blame-either.md)
- [The boundaries between components are inherited, not derived](../figures/stonebraker/lessons/the-boundaries-between-components-are-inherited-not-derived.md)
- [Wanting to be different is not a design criterion](../figures/stonebraker/lessons/wanting-to-be-different-is-not-a-design-criterion.md)
- [When two goals fight, build two structures and a reconciler](../figures/stonebraker/lessons/when-two-goals-fight-build-two-structures-and-a-reconciler.md)

**strachey** (6)
- [Hand each user a whole smaller machine, not a slice of yours](../figures/strachey/lessons/hand-each-user-a-whole-smaller-machine.md)
- [Let a program do the organising, and hardware only what a program cannot](../figures/strachey/lessons/let-a-program-do-the-organising-and-hardware-only-what-a-program-cannot.md)
- [Make the machine's reality sayable instead of escapable](../figures/strachey/lessons/make-the-machines-reality-sayable-instead-of-escapable.md)
- [Put the power to change a guard out of reach of what it guards](../figures/strachey/lessons/put-the-power-to-change-a-guard-out-of-reach-of-what-it-guards.md)
- [Rank urgency by what cannot be made to wait](../figures/strachey/lessons/rank-urgency-by-what-cannot-be-made-to-wait.md)
- [Say what happens and stay silent about the bookkeeping](../figures/strachey/lessons/say-what-happens-and-stay-silent-about-the-bookkeeping.md)

**sutherland** (7)
- [A projection is only usable if it carries the way back to the node that made it](../figures/sutherland/lessons/a-projection-must-carry-its-way-back-to-the-node.md)
- [Computation the apparatus performs for free is also a dependency on that apparatus](../figures/sutherland/lessons/work-the-apparatus-does-for-free-is-also-a-dependency.md)
- [Derive a component's tolerance from the error already present in the chain](../figures/sutherland/lessons/derive-a-components-tolerance-from-the-error-already-in-the-chain.md)
- [Find which variables the result is actually a function of, and stop measuring the rest](../figures/sutherland/lessons/find-which-variables-the-perception-is-actually-a-function-of.md)
- [Let stages negotiate locally instead of scheduling them globally](../figures/sutherland/lessons/let-stages-negotiate-locally-instead-of-scheduling-them-globally.md)
- [Rank candidate methods by how they grow, then cut what still will not fit](../figures/sutherland/lessons/rank-candidates-by-how-they-grow-not-how-they-look-today.md)
- [Trade unstructured noise for an ambiguity you can compute away](../figures/sutherland/lessons/trade-unstructured-noise-for-an-ambiguity-you-can-compute-away.md)

**thompson** (7)
- [Absorb hardware variety at the lowest boundary so nothing above it has to know](../figures/thompson/lessons/absorb-variety-at-the-lowest-boundary.md)
- [An abstraction's limit is what it implies, not what it can be made to encode](../figures/thompson/lessons/an-abstractions-limit-is-what-it-implies-not-what-it-can-encode.md)
- [An unnegotiable ceiling forces factoring where a generous one permits accumulation](../figures/thompson/lessons/an-unnegotiable-ceiling-forces-factoring-instead-of-accumulation.md)
- [Carry the whole set of live possibilities forward instead of backtracking through one](../figures/thompson/lessons/carry-the-set-of-live-possibilities-forward-instead-of-backtracking.md)
- [Delete the privileged default so the general path is the only path](../figures/thompson/lessons/delete-the-privileged-default-so-the-general-path-is-the-only-path.md)
- [Detectability falls off as you descend the stack, so reason about depth before reasoning about cleverness](../figures/thompson/lessons/detectability-falls-off-as-you-descend-the-stack.md)
- [Let the machine's own dispatch be your data structure](../figures/thompson/lessons/let-the-machines-own-dispatch-be-your-data-structure.md)

**torvalds** (7)
- [A cache earns its place by being destroyable, and it is only sound if it knows the window where its key is a lie](../figures/torvalds/lessons/a-cache-must-be-disposable-and-distrust-its-own-key.md)
- [Build the first version for the machine you actually own, and let generality be earned later](../figures/torvalds/lessons/build-for-the-machine-you-actually-own.md)
- [Define your portable contract as the weakest behavior any target could exhibit, and quarantine every place you exploit more](../figures/torvalds/lessons/write-against-the-weakest-machine-in-the-set.md)
- [Make meaning independent of layout, and layout becomes a free variable you can spend entirely on the machine](../figures/torvalds/lessons/make-meaning-independent-of-layout.md)
- [Optimize against the machine's real cost hierarchy, not the operation you can see](../figures/torvalds/lessons/optimize-against-the-machines-cost-model-not-your-intuition.md)
- [Spend all your stability at one boundary: freeze what outsiders observe, churn everything behind it, and make the breaker do the fixing](../figures/torvalds/lessons/spend-all-your-stability-at-one-boundary.md)
- [Treat your compiler as an adversary wherever memory is shared, and mark the sharing at each access rather than fencing broadly](../figures/torvalds/lessons/mark-the-sharing-at-every-access.md)

**turing** (8)
- [Calibrate against the whole space by computing its summary in closed form, never by walking it](../figures/turing/lessons/calibrate-against-a-space-too-large-to-walk.md)
- [Choose the representation in which combining results is your executor's cheapest operation](../figures/turing/lessons/choose-the-representation-where-combination-is-your-cheapest-operation.md)
- [Count what your machinery finds cheap, then recover the number you actually wanted by arithmetic](../figures/turing/lessons/count-what-is-cheap-and-invert-for-what-you-wanted.md)
- [Once your operations can all simulate each other, the primitive set is an economic choice, not a logical one](../figures/turing/lessons/when-everything-reduces-to-everything-choose-primitives-by-cost.md)
- [Put the description of the behaviour into the same medium as the data, and one artifact replaces an infinite family](../figures/turing/lessons/a-program-is-just-more-data-on-the-same-tape.md)
- [Shared implementation medium is not evidence of shared behaviour; only functional correspondence is](../figures/turing/lessons/shared-substrate-is-not-shared-behaviour.md)
- [State an interface as classes separated by a margin, and error stops accumulating across the boundary](../figures/turing/lessons/state-the-contract-as-classes-far-enough-apart-to-restore.md)
- [The rate at which you cross a threshold changes the outcome, not just the time it takes to get there](../figures/turing/lessons/how-fast-you-cross-a-threshold-changes-the-result.md)

**ullman** (2)
- [A cost model is a claim about which resource runs out first](../figures/ullman/lessons/a-cost-model-is-a-claim-about-what-runs-out-first.md)
- [How you group data is a search strategy in disguise](../figures/ullman/lessons/how-you-group-data-is-an-access-plan-in-disguise.md)

**ungar** (8)
- [Judge an optimization by whether it shows through, not by how much it saves](../figures/ungar/lessons/an-optimization-that-shows-through-is-disqualified.md)
- [Price every feature by what its absence would cost, in a unit that lets the prices add up](../figures/ungar/lessons/price-a-feature-by-the-cost-of-removing-it.md)
- [Report performance in the unit a person actually experiences, or your numbers will flatter you](../figures/ungar/lessons/measure-in-the-unit-the-user-perceives.md)
- [Start the likely case and check the assumption alongside it, rather than checking first](../figures/ungar/lessons/assume-the-common-case-and-verify-it-concurrently.md)
- [Treat the boundary between layers as a design variable, and decide what lives on each side last](../figures/ungar/lessons/keep-the-layer-boundary-movable.md)
- [Whatever dimension your metric leaves out is the dimension your design will quietly spend](../figures/ungar/lessons/a-metric-that-omits-a-dimension-gets-spent-there.md)
- [When a population's behavior is sharply split, find the cheap observable that separates it and stop treating it uniformly](../figures/ungar/lessons/stratify-a-population-by-a-cheap-predictor.md)
- [Your cost model is the style guide people actually obey; make the good structure the cheap one](../figures/ungar/lessons/your-cost-model-is-a-style-guide-people-actually-obey.md)
