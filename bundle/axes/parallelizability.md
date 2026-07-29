---
type: axis
title: Parallelizability
description: How naturally a construct decomposes into independently executable pieces without hidden shared-mutable-state coordination.
tags: [axis, concurrency, parallelizability]
---

# Parallelizability

## Definition
How naturally a construct splits into pieces that can execute independently —
whether concurrency requires explicit, hidden coordination over shared
mutable state, or whether the construct's own structure (e.g. no shared state
to begin with) makes independent execution the default rather than something
bolted on. Distinct from verifiability: a construct can be easy to prove
correct sequentially while still resisting decomposition into independent
units of work.

## Rollup
No lessons scored on this axis yet.

## Lessons scored here
175 lessons from 65 figures.

**abiteboul** (2)
- [How you schedule the steps is part of what the program means](../figures/abiteboul/lessons/how-you-schedule-the-rules-is-part-of-what-they-mean.md)
- [Restrict the language until the guarantee you need is a theorem about the language](../figures/abiteboul/lessons/restrict-the-language-until-the-guarantee-is-a-theorem.md)

**abrial** (2)
- [Make hypothesis a first-class scope, so that asking what if uses the same machinery as recording what is](../figures/abrial/lessons/give-hypothesis-the-same-standing-as-fact.md)
- [Order is a claim you either make or decline, and declining it is the same act for a collection as for a sequence of statements](../figures/abrial/lessons/order-is-a-claim-and-parallelism-is-its-absence.md)

**bachman** (1)
- [Sharing durable mutable state is a different problem from sharing the machine](../figures/bachman/lessons/sharing-durable-state-is-the-hard-problem.md)

**backus** (1)
- [Say what the result is over whole values, and name nothing you do not have to](../figures/backus/lessons/operate-on-whole-values-and-name-nothing.md)

**booch** (3)
- [A boundary enforced as an interface is an option on recombinations you cannot forecast](../figures/booch/lessons/an-interface-boundary-is-an-option-on-futures-you-cannot-forecast.md)
- [Computation and the data it consumes have physical cost, and that cost belongs in the design, not in a footnote](../figures/booch/lessons/computation-has-weight-and-data-has-mass.md)
- [The organization is part of the structure, so restructuring the system means restructuring the people](../figures/booch/lessons/the-team-is-part-of-the-architecture.md)

**boyce** (1)
- [State the set you want, not the walk that finds it](../figures/boyce/lessons/state-the-set-not-the-walk.md)

**brewer** (2)
- [Name the guarantee you are forfeiting before the failure names it for you](../figures/brewer/lessons/name-the-guarantee-you-forfeit.md)
- [Widen correctness from a bit to a dial, then engineer the dial](../figures/brewer/lessons/correctness-is-a-continuous-quantity.md)

**brinch-hansen** (3)
- [Assume every participant is broken or hostile, and make whoever opens an interaction carry its risk](../figures/brinch-hansen/lessons/assume-every-participant-may-be-broken.md)
- [Cut module boundaries where simultaneity demands them, not where the data would suggest](../figures/brinch-hansen/lessons/cut-boundaries-where-simultaneity-demands.md)
- [Design concurrent code for reproducible behavior, because the errors that matter are the ones testing can never reach](../figures/brinch-hansen/lessons/design-for-reproducibility-because-testing-cannot-reach.md)

**brooks** (1)
- [Effort and elapsed time trade only for work whose parts need not agree; where they must agree, coordination grows faster than the division saves](../figures/brooks/lessons/coordination-cost-outruns-the-division-of-labour.md)

**cardelli** (2)
- [Before adding a mechanism, check whether a distinction the system already maintains can carry the new job](../figures/cardelli/lessons/get-the-second-mechanism-free-from-a-distinction-you-already-keep.md)
- [Fix what is not allowed to move, then build motion out of ordinary operations instead of a migration feature](../figures/cardelli/lessons/decide-what-must-not-move-then-program-the-motion.md)

**chaitin** (1)
- [A part that declares its own extent can be composed; one that does not must be framed by its caller](../figures/chaitin/lessons/make-every-part-declare-where-it-ends.md)

**chamberlin** (1)
- [Write down what the optimizer is allowed to skip, and give the programmer a way to opt out](../figures/chamberlin/lessons/license-the-optimizer-in-writing-and-provide-an-opt-out.md)

**chuck-moore** (1)
- [Accept a restriction that makes the bookkeeping vanish rather than a generality that makes it permanent](../figures/chuck-moore/lessons/choose-the-restricted-regime-whose-bookkeeping-disappears.md)

**church** (1)
- [Order independence is a property you purchase with restrictions, and convenience in the core can spend it](../figures/church/lessons/order-independence-is-bought-not-given.md)

**clarke** (3)
- [A specification tight enough to check is tight enough to build from](../figures/clarke/lessons/a-spec-tight-enough-to-check-is-tight-enough-to-build-from.md)
- [Compose so that adding context can only take behaviour away](../figures/clarke/lessons/compose-so-context-only-removes-behavior.md)
- [Interleaving is what costs; independence is what refunds](../figures/clarke/lessons/interleaving-costs-independence-refunds.md)

**codd** (1)
- [State the properties of the result; let the system choose the procedure](../figures/codd/lessons/state-properties-let-the-system-choose-the-procedure.md)

**cook** (2)
- [Choose the model for what it lets you prove, and treat every arbitrary detail in a specification as a place no theorem can live](../figures/cook/lessons/pick-the-model-that-admits-proofs-not-just-programs.md)
- [When you cannot measure a problem's cost, measure the cheap translations between problems instead](../figures/cook/lessons/compare-difficulty-by-translation-not-measurement.md)

**corbato** (1)
- [Authority That Routes Through the Center Is a Bottleneck](../figures/corbato/lessons/authority-that-routes-through-the-center-is-a-bottleneck.md)

**cox** (1)
- [Design vocabulary is scale-relative: fix the integration level before arguing about the word](../figures/cox/lessons/fix-the-scale-before-arguing-about-the-word.md)

**cutler** (4)
- [Any behavior you put in shared implicit state serializes every operation that reads it; encode it in the operation instead](../figures/cutler/lessons/implicit-mode-state-serializes-what-touches-it.md)
- [As a system's defects thin out, the survivors are almost all synchronization, so design for concurrency at the start or not at all](../figures/cutler/lessons/synchronization-is-where-the-residual-bugs-live.md)
- [Enumerate the mechanisms your abstraction silently requires from the layer beneath it, then price their absence as recurring](../figures/cutler/lessons/inventory-what-your-abstraction-demands-from-below.md)
- [When predictability is the requirement, remove the sharing instead of scheduling it better](../figures/cutler/lessons/partition-instead-of-scheduling-when-predictability-is-the-product.md)

**dahl** (4)
- [Give each component its own resumption point, and the state machine you would have hand-encoded disappears](../figures/dahl/lessons/give-each-component-its-own-sequence-control.md)
- [Give every entity its own place in its own text, so a life spread over time still reads as one story](../figures/dahl/lessons/give-each-entity-its-own-sequence-control.md)
- [Make concurrency a nestable construct, so a subsystem's interleaving is invisible from outside it](../figures/dahl/lessons/nest-concurrency-so-interleaving-stays-local.md)
- [Separate the concurrency in your description from the concurrency in your execution, and make the scheduler an inspectable data structure](../figures/dahl/lessons/concurrency-as-description-with-scheduling-as-data.md)

**date** (1)
- [Choose the grain of your operators and you choose who owns performance](../figures/date/lessons/choose-the-grain-of-your-operators-and-you-choose-who-owns-performance.md)

**denning** (3)
- [Allocate per unit of work so each one's performance depends only on itself](../figures/denning/lessons/per-unit-isolation-over-global-policy.md)
- [Differentiate before you tune: a large hardware ratio can leave no safe operating margin at all](../figures/denning/lessons/sensitivity-before-tuning.md)
- [Two resources that constrain each other need one allocator, not two good ones](../figures/denning/lessons/coupled-resources-single-decision.md)

**dijkstra** (4)
- [Design distributed rules so the legitimate states are an attractor, not a fortress](../figures/dijkstra/lessons/make-the-legal-state-an-attractor.md)
- [In concurrency, proving nothing bad happens is half a proof: demand progress against an adversarial schedule](../figures/dijkstra/lessons/safety-without-progress-is-not-correctness.md)
- [Leave choices the problem does not force unmade: nondeterminacy exposes the essential program](../figures/dijkstra/lessons/nondeterminacy-strips-the-incidental.md)
- [Make cooperating processes correct under every speed ratio, because timing assumptions are hidden coupling](../figures/dijkstra/lessons/never-let-correctness-depend-on-timing.md)

**dolev** (6)
- [A tight bound on one resource says nothing about the resource that decides feasibility](../figures/dolev/lessons/count-the-resource-the-machine-actually-spends.md)
- [A worst-case bound is a statement about the worst case, not a licence to charge for it every time](../figures/dolev/lessons/make-the-bill-track-the-run-you-actually-had.md)
- [Budget failures happening at once, not failures ever; then rejoining costs nothing](../figures/dolev/lessons/budget-simultaneous-failure-not-lifetime-failure.md)
- [Having weakened the requirement, solve it directly instead of layering it over the strong primitive](../figures/dolev/lessons/solve-the-weak-problem-natively-not-on-top-of-the-strong-one.md)
- [Mine your proofs for a rule of thumb you can guess with before proving anything](../figures/dolev/lessons/turn-your-proofs-into-a-rule-you-can-guess-with.md)
- [The exact shape of the agreement you demand is the biggest lever you have, and its price is discontinuous](../figures/dolev/lessons/the-shape-of-agreement-you-demand-is-the-largest-lever.md)

**edmonds** (1)
- [Find out which of your method's choices are incidental and which fix the answer, because the incidental ones are freedom you have already paid for](../figures/edmonds/lessons/separate-what-the-run-chooses-from-what-the-problem-determines.md)

**emerson** (3)
- [Specify what must remain possible, or a generator will hand you the least capable thing that qualifies](../figures/emerson/lessons/demand-possibility-or-be-handed-the-least-capable-thing.md)
- [Treat global behavior as primary and each component as a projection of it; shared state is the price of projecting](../figures/emerson/lessons/local-processes-are-projections-of-a-global-behavior.md)
- [Verifiability is a property of the architecture you chose, so pick structures whose guarantees compose](../figures/emerson/lessons/verifiability-is-an-architectural-property-you-design-for.md)

**fagin** (2)
- [Design into the shape where local checks certify global properties](../figures/fagin/lessons/design-into-the-shape-where-local-checks-certify-global-properties.md)
- [The static shape of a model decides which execution costs are even possible](../figures/fagin/lessons/the-static-shape-of-a-model-decides-what-execution-costs-are-possible.md)

**fischer** (4)
- [Optimal means nothing until you name the resource, and the winner on one resource can be absurd on another](../figures/fischer/lessons/optimal-is-meaningless-until-you-name-the-resource.md)
- [Reason about a protocol by what it has not yet ruled out, not by tracing its runs](../figures/fischer/lessons/reason-about-what-remains-undecided.md)
- [The binding constraint on a distributed component is what its local view cannot tell apart](../figures/fischer/lessons/what-cannot-be-distinguished-bounds-what-can-be-decided.md)
- [Without a timing assumption, slow and dead are the same observation](../figures/fischer/lessons/a-slow-participant-and-a-dead-one-are-the-same-observation.md)

**floyd** (1)
- [Write the program for the machine you wish you had, and make the gap down to the real one mechanical](../figures/floyd/lessons/write-for-the-machine-you-wish-you-had-then-translate.md)

**gang-of-four** (1)
- [Whether a thing can be shared is decided entirely by whether it remembers its context](../figures/gang-of-four/lessons/context-dependence-is-what-forbids-sharing.md)

**girard** (2)
- [Earn parallelism from the structure of the program itself, and treat every synchronization point as a visible defect in that structure](../figures/girard/lessons/let-parallelism-fall-out-of-the-structure.md)
- [The distinguished result is an assumption, not a fact — give it up and composition becomes symmetric](../figures/girard/lessons/give-up-the-privileged-output.md)

**goldberg** (2)
- [Carve a domain by what its things do and what they need coordinated, and say out loud over what interval your idealizations hold](../figures/goldberg/lessons/model-by-what-things-do-and-name-the-interval-your-idealization-holds.md)
- [When a concept keeps showing up only in explanations, promote it to a thing the program can hold](../figures/goldberg/lessons/give-an-object-to-the-thing-you-keep-explaining-in-comments.md)

**herlihy** (10)
- [A guarantee that is sound in the step-counting model can be the wrong engineering choice; go measure](../figures/herlihy/lessons/asymptotically-adequate-is-not-practically-adequate.md)
- [A pure safety condition can quietly forbid progress; audit what your consistency contract makes impossible](../figures/herlihy/lessons/a-safety-condition-can-silently-cost-you-liveness.md)
- [Guarantees are not a ladder to climb: decompose one into its clauses and keep only the clause that is load-bearing](../figures/herlihy/lessons/decompose-a-guarantee-and-keep-only-the-clause-you-need.md)
- [Insist that a correctness property hold object by object, or you have bought a global scheduler without noticing](../figures/herlihy/lessons/insist-the-correctness-property-be-local.md)
- [Let the system own correctness and the programmer own cost: write sequential code, mechanize the concurrency](../figures/herlihy/lessons/write-sequential-code-and-let-the-system-own-concurrency.md)
- [Make progress a guarantee the shared object owes each caller, not a favor its callers do each other](../figures/herlihy/lessons/make-progress-a-guarantee-the-object-owes-each-caller.md)
- [Measure a synchronization primitive by how much agreement it can manufacture, not by how much it can compute](../figures/herlihy/lessons/measure-a-primitive-by-the-agreement-it-can-manufacture.md)
- [Pessimistic protocols make you declare a footprint you do not yet know, and the concurrency you lose is the state-dependent kind](../figures/herlihy/lessons/pessimistic-protocols-make-you-declare-a-footprint-you-cannot-yet-know.md)
- [Separate the part that must be correct from the part that must be tuned, and let only the tuned part be replaceable](../figures/herlihy/lessons/separate-the-mechanism-that-is-correct-from-the-policy-that-makes-progress.md)
- [Shrink what you hold before getting clever about arbitrating collisions](../figures/herlihy/lessons/shrink-the-window-before-arbitrating-the-collisions.md)

**karp** (1)
- [Stop optimizing the single step; find the batch of non-interfering steps and bound how many batches there are](../figures/karp/lessons/batch-non-interfering-improvements-into-phases.md)

**lamport** (5)
- [Correct parts do not make a correct whole; name the composition condition and price it](../figures/lamport/lessons/local-correctness-does-not-compose.md)
- [Design algorithms to survive the weakest primitives you can, and count every assumption you keep](../figures/lamport/lessons/assume-the-least-from-your-primitives.md)
- [Every reliability guarantee is relative to a failure model; state it, and know what weakening it costs](../figures/lamport/lessons/make-the-failure-model-explicit.md)
- [Observation of a running system yields a state that never occurred, and that can be enough](../figures/lamport/lessons/a-consistent-snapshot-need-not-have-happened.md)
- [Order events by what the system can observe, not by an imagined universal clock](../figures/lamport/lessons/order-events-by-causality-not-clocks.md)

**lampson** (7)
- [A rule about how costs must be attributed is an architectural constraint in disguise: decide what it forbids before you adopt it, and make sure every exhaustible resource is inside the model rather than beside it](../figures/lampson/lessons/an-accounting-rule-is-an-architectural-constraint-in-disguise.md)
- [Act only on facts that can never become false again, and keep strengthening the invariant until it is something each participant can maintain alone — the algorithm is what is left over](../figures/lampson/lessons/act-only-on-facts-that-cannot-be-retracted.md)
- [Deliberately weaken what a synchronization event promises, because a weaker guarantee makes every proof local and every later extension free](../figures/lampson/lessons/weaken-the-promise-to-localize-the-proof.md)
- [Mutual exclusion between participants of very different speeds destroys the fast one's worst-case guarantee, so a speed boundary is where a coordination model has to change](../figures/lampson/lessons/never-share-exclusion-across-a-speed-boundary.md)
- [Redundancy only helps if the redundant parts are functions: force determinism first, and the whole reliability problem collapses into agreeing on one sequence of inputs](../figures/lampson/lessons/make-the-component-a-function-then-agreement-is-the-only-hard-part.md)
- [The measured price of a primitive decides which program structures are available to you, so publish the price and treat granularity as a consequence of it](../figures/lampson/lessons/the-price-of-a-primitive-decides-which-structures-you-can-think-in.md)
- [Withdrawing a fact by notifying everyone who holds it is a distributed problem you cannot win; give the fact an expiry and make withdrawal a refusal to renew](../figures/lampson/lessons/give-every-belief-an-expiry-instead-of-a-notification-list.md)

**landin** (2)
- [Whether a representation choice is invisible depends on what else the language admits; adding effects promotes it into a semantic decision](../figures/landin/lessons/whether-a-representation-choice-is-observable-depends-on-what-else-the-language-admits.md)
- [Written order is a claim about order, and most programs assert far more of it than they mean](../figures/landin/lessons/sequence-is-information-you-may-not-mean-to-assert.md)

**lehman** (1)
- [Push the world's uncertainty out to the seams so that every leaf module is fully specified](../figures/lehman/lessons/quarantine-irreducible-uncertainty-at-module-boundaries.md)

**liskov** (8)
- [Consistency strength belongs to the operation, not to the system](../figures/liskov/lessons/consistency-strength-is-a-per-operation-choice.md)
- [Design so that no irreversible step rests on a judgment you cannot make reliably](../figures/liskov/lessons/no-irreversible-step-on-an-unreliable-judgment.md)
- [Extra capability is invisible only in a closed world](../figures/liskov/lessons/extra-capability-is-invisible-only-in-a-closed-world.md)
- [If you can name the dependency, you do not need the coordination](../figures/liskov/lessons/if-you-can-name-the-dependency-you-do-not-need-the-coordination.md)
- [Make the unit of failure nestable and failure handling becomes composable](../figures/liskov/lessons/make-the-unit-of-failure-nestable.md)
- [Never let a timing guess be load-bearing for correctness; spend it on progress instead](../figures/liskov/lessons/never-let-a-timing-guess-be-load-bearing-for-correctness.md)
- [Never show anyone an effect that is less durable than the promise you made about it](../figures/liskov/lessons/never-show-anyone-an-effect-less-durable-than-your-promise.md)
- [Your representation choice sets the concurrency ceiling, not your concurrency constructs](../figures/liskov/lessons/your-representation-choice-sets-the-concurrency-ceiling.md)

**lynch** (6)
- [A distributed algorithm can only depend on what its participants can actually tell apart](../figures/lynch/lessons/correctness-can-only-rest-on-what-a-process-can-distinguish.md)
- [A fault-tolerance claim is meaningless until you say when the faults are allowed to happen](../figures/lynch/lessons/impossibility-is-a-statement-about-when-the-adversary-may-act.md)
- [Judge a composition operator by whether your reasoning survives it in both directions](../figures/lynch/lessons/an-abstraction-operator-must-preserve-the-properties-you-reason-with.md)
- [Reason about a concurrent system by the set of outcomes still reachable, not by the history that produced the current state](../figures/lynch/lessons/track-what-outcomes-are-still-open-not-what-has-happened.md)
- [The right obligation on an open component is never to be the first to break the invariant](../figures/lynch/lessons/never-be-the-first-to-break-the-invariant.md)
- [Turn \"eventually\" into a quantity that provably shrinks, and both the deadline and the freedom to stop early follow](../figures/lynch/lessons/turn-eventually-into-a-quantity-that-shrinks.md)

**manna** (7)
- [A fairness assumption is a debt someone has to implement, not a fact about the world](../figures/manna/lessons/a-fairness-assumption-is-a-debt-someone-must-implement.md)
- [A progress argument has to track who is responsible, not only how far away the goal is](../figures/manna/lessons/progress-arguments-must-track-who-is-responsible.md)
- [For an unbounded ensemble, the measure is a shrinking set of participants, and it shrinks via the one nobody can block](../figures/manna/lessons/measure-an-unbounded-ensemble-by-a-shrinking-set.md)
- [Model concurrency as one uniform machine plus explicit, single-purpose scheduling assumptions](../figures/manna/lessons/make-scheduling-assumptions-explicit-and-single-purpose.md)
- [Proof cost tracks how many things can change the answer, not how big the program is](../figures/manna/lessons/proof-cost-tracks-what-can-change-the-answer.md)
- [Reason about a component against an environment allowed to do anything except touch what the component owns](../figures/manna/lessons/reason-against-an-environment-that-may-do-anything-you-do-not-own.md)
- [Somebody progresses and everybody progresses are different guarantees, and which one you can have is decided by your primitive](../figures/manna/lessons/somebody-progresses-and-everybody-progresses-are-different-guarantees.md)

**mccarthy** (1)
- [Judge a system's extensibility by how little of its innards a contributor must understand, and buy that with order-independent statements instead of procedure edits](../figures/mccarthy/lessons/extend-by-adding-facts-not-by-editing-procedure.md)

**mcmillan** (2)
- [Refuse to decide what nobody asked you to decide](../figures/mcmillan/lessons/refuse-to-decide-what-you-were-not-asked.md)
- [Separate the structure that is in the system from the structure your model imposes on it](../figures/mcmillan/lessons/separate-structure-in-the-system-from-structure-your-model-imposes.md)

**milner** (1)
- [A freshly created private name buys atomicity and isolation without a new primitive](../figures/milner/lessons/a-fresh-private-name-buys-atomicity-for-free.md)

**nygaard** (1)
- [Put Only Suspend-And-Resume In The Machine; Keep Scheduling Policy In Libraries](../figures/nygaard/lessons/minimum-interleaving-primitive-policy-above.md)

**parnas** (2)
- [No ordering of decisions can be backed out of cleanly, so buy independence rather than a better order](../figures/parnas/lessons/no-ordering-of-decisions-can-be-backed-out-of-cleanly.md)
- [Scrutiny held collectively is held by nobody, so partition it and keep a check on the partition](../figures/parnas/lessons/responsibility-held-collectively-is-held-by-nobody.md)

**peter** (1)
- [Swap a construction for a checkable record plus a search you can guarantee](../figures/peter/lessons/swap-a-construction-for-a-checkable-record-and-a-guarded-search.md)

**pike** (5)
- [A primitive that encodes a usage style cannot be reused](../figures/pike/lessons/a-primitive-that-encodes-a-usage-style-cannot-be-reused.md)
- [Both ends modelling what the other knows beats asking](../figures/pike/lessons/both-ends-modelling-what-the-other-knows-beats-asking.md)
- [Let a process's position hold the state a queue would track](../figures/pike/lessons/let-a-process-position-hold-the-state-a-queue-would-track.md)
- [Mechanical analyzability is what buys the right to change your mind](../figures/pike/lessons/mechanical-analyzability-is-what-buys-the-right-to-change-your-mind.md)
- [Notify after the fact rather than mediating every change](../figures/pike/lessons/notify-after-the-fact-rather-than-mediating-every-change.md)

**pnueli** (3)
- [An abstraction that discards something must pay it back as an explicit, calibrated assumption](../figures/pnueli/lessons/pay-back-what-your-abstraction-discards.md)
- [Treat whatever you do not control as an adversary, not a partner](../figures/pnueli/lessons/treat-what-you-do-not-control-as-an-adversary.md)
- [Two shapes of property over one model of execution beats a proof theory per paradigm](../figures/pnueli/lessons/two-property-shapes-over-one-model-of-execution.md)

**rashid** (2)
- [Choose the semantics you can reason about, then buy the cost back underneath where nobody has to know](../figures/rashid/lessons/choose-the-semantics-you-can-reason-about-and-buy-the-cost-back-underneath.md)
- [When an abstraction is too expensive to use the way the problem wants, look for two concerns fused inside it](../figures/rashid/lessons/split-the-abstraction-that-bundles-ownership-with-execution.md)

**reenskaug** (1)
- [A new binding mechanism must be restricted until local reasoning survives it](../figures/reenskaug/lessons/restrict-a-dynamic-binding-mechanism-until-local-reasoning-survives.md)

**ritchie** (3)
- [Put the variability in the joints between components, not inside the components](../figures/ritchie/lessons/put-the-variability-in-the-joints.md)
- [Unifying features into one mechanism buys simplicity by pinning semantics you may later need to loosen](../figures/ritchie/lessons/unification-buys-simplicity-and-forecloses-reinterpretation.md)
- [When a new mechanism breaks something unrelated, you have found state attached to the wrong lifetime](../figures/ritchie/lessons/unrelated-breakage-reveals-state-on-the-wrong-lifetime.md)

**saltzer** (4)
- [Choose primitives that funnel every race into one](../figures/saltzer/lessons/choose-primitives-that-funnel-every-race-into-one.md)
- [Decide up front what your overhead is allowed to scale with](../figures/saltzer/lessons/decide-up-front-what-your-overhead-is-allowed-to-scale-with.md)
- [Send the decision to the data, not the data to the decision](../figures/saltzer/lessons/send-the-decision-to-the-data-not-the-data-to-the-decision.md)
- [Waiting for the answer is what creates the dependency](../figures/saltzer/lessons/waiting-for-the-answer-is-what-creates-the-dependency.md)

**schneider** (4)
- [A designated role is hidden state that has to be rebuilt after a crash; symmetric designs have nothing to re-elect](../figures/schneider/lessons/a-role-is-state-that-must-be-rebuilt.md)
- [Derive knowledge from what a participant can no longer say, not from what it has said](../figures/schneider/lessons/infer-from-what-a-participant-can-no-longer-say.md)
- [Make every distributed decision rule immune to learning more, and interference disappears](../figures/schneider/lessons/decisions-that-later-news-cannot-falsify.md)
- [The cost of coordination is set by the size of its audience, so shrink the audience before tuning the protocol](../figures/schneider/lessons/shrink-the-audience-before-optimizing-the-protocol.md)

**steele** (4)
- [A dynamic phenomenon cannot be governed by a construct with lexical scope, and shipping one anyway is worse than shipping nothing](../figures/steele/lessons/a-dynamic-phenomenon-cannot-be-controlled-by-a-lexical-construct.md)
- [A model that works by copying can never express sharing, so its blind spots tell you which features are really primitive](../figures/steele/lessons/a-semantic-model-that-copies-cannot-express-sharing.md)
- [Refuse to specify the things you do not want depended on, even when every implementation agrees on them](../figures/steele/lessons/refuse-to-specify-what-you-do-not-want-depended-on.md)
- [To gain control of a hidden mechanism, rewrite it as an ordinary value you pass around — then let the notation hide it again](../figures/steele/lessons/make-the-hidden-mechanism-an-ordinary-value-then-hide-it-again.md)

**stonebraker** (8)
- [A closed set of programs turns runtime decisions into design-time ones](../figures/stonebraker/lessons/a-closed-set-of-programs-turns-runtime-decisions-into-design-time-ones.md)
- [An atomic unit can only be as large as what you can undo](../figures/stonebraker/lessons/an-atomic-unit-can-only-be-as-large-as-what-you-can-undo.md)
- [Escalate mechanism on measured failure, not on its possibility](../figures/stonebraker/lessons/escalate-mechanism-on-measured-failure-not-on-its-possibility.md)
- [Name the workload property that lets a mechanism be deleted](../figures/stonebraker/lessons/name-the-workload-property-that-lets-a-mechanism-be-deleted.md)
- [Never schedule the cleanup below the work that depends on it](../figures/stonebraker/lessons/never-schedule-the-cleanup-below-the-work-that-depends-on-it.md)
- [Separate the model from the implementation before you blame either](../figures/stonebraker/lessons/separate-the-model-from-the-implementation-before-you-blame-either.md)
- [State what you want and surrender the plan](../figures/stonebraker/lessons/state-what-you-want-and-surrender-the-plan.md)
- [Weaken a guarantee nobody needs and whole mechanisms vanish](../figures/stonebraker/lessons/weaken-a-guarantee-nobody-needs-and-whole-mechanisms-vanish.md)

**strachey** (3)
- [Keep what is settled by context apart from what is settled by history](../figures/strachey/lessons/keep-what-is-settled-by-context-apart-from-what-is-settled-by-history.md)
- [Preserve the programmer's indifference to order](../figures/strachey/lessons/preserve-the-programmers-indifference-to-order.md)
- [Rank urgency by what cannot be made to wait](../figures/strachey/lessons/rank-urgency-by-what-cannot-be-made-to-wait.md)

**sutherland** (1)
- [Let stages negotiate locally instead of scheduling them globally](../figures/sutherland/lessons/let-stages-negotiate-locally-instead-of-scheduling-them-globally.md)

**thompson** (3)
- [A primitive that carries no state has handed that state to every caller](../figures/thompson/lessons/a-primitive-that-carries-no-state-hands-its-state-to-every-caller.md)
- [Carry the whole set of live possibilities forward instead of backtracking through one](../figures/thompson/lessons/carry-the-set-of-live-possibilities-forward-instead-of-backtracking.md)
- [Named variants are frozen points in a space; expose the axes instead](../figures/thompson/lessons/named-variants-are-frozen-points-expose-the-axes.md)

**torvalds** (4)
- [Existence and coherence are different problems: count references to keep a thing alive, take locks to keep it consistent](../figures/torvalds/lessons/existence-and-coherence-are-different-problems.md)
- [Keep every participant's state complete and local, then refuse to encode who is in charge](../figures/torvalds/lessons/keep-the-whole-state-local-and-refuse-to-encode-policy.md)
- [Ordering is a protocol between participants, never a property of one of them, and the set of observers who agree is part of the specification](../figures/torvalds/lessons/ordering-is-a-two-party-protocol.md)
- [Treat your compiler as an adversary wherever memory is shared, and mark the sharing at each access rather than fencing broadly](../figures/torvalds/lessons/mark-the-sharing-at-every-access.md)

**turing** (2)
- [Grant the system unlimited patience and no cleverness, to find out which of its limits are real](../figures/turing/lessons/grant-unlimited-patience-to-find-out-what-is-actually-impossible.md)
- [Put a cheap approximate filter in front of the expensive procedure, and size its accuracy by the cost it saves](../figures/turing/lessons/size-the-cheap-screening-pass-by-the-cost-of-the-expensive-one.md)

**ullman** (3)
- [A cost model is a claim about which resource runs out first](../figures/ullman/lessons/a-cost-model-is-a-claim-about-what-runs-out-first.md)
- [Restartability is a shape you keep, not a feature you add](../figures/ullman/lessons/restartability-is-a-shape-not-a-feature.md)
- [The dependency between inputs and outputs bounds what any parallel version can cost](../figures/ullman/lessons/what-each-output-needs-bounds-what-parallelism-can-cost.md)

**ungar** (1)
- [Start the likely case and check the assumption alongside it, rather than checking first](../figures/ungar/lessons/assume-the-common-case-and-verify-it-concurrently.md)

**von-thun** (1)
- [Notation that over-specifies order hides independence you already have](../figures/von-thun/lessons/notation-that-over-specifies-order-hides-independence-you-already-have.md)
