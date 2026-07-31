---
type: work
title: "Structure and Interpretation of Computer Programs"
figure: sussman
description: The textbook for MIT's introductory computer science course (6.001), built around the idea that a programming language is best understood by building an evaluator for it and that most of "design" is choosing the right abstraction barriers between layers. It works through procedural and data abstraction, generic operations and message-passing object systems, streams and lazy evaluation, explicit state and its costs, and finally a metacircular Scheme evaluator and a small register-machine compiler. Enormously influential as a way of teaching computing as applied abstraction-building rather than syntax memorization.
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
year: 1985
url: https://web.mit.edu/6.001/6.037/sicp.pdf
survey_pages: 883
survey_text_layer: full
survey_fetch_mb: 7
access: public
host: institutional
tags: [work]
---

# Structure and Interpretation of Computer Programs

**Author(s):** Harold Abelson and Gerald Jay Sussman, with Julie Sussman
**Venue/year:** MIT Press, 1st edition 1985 (2nd edition 1996); MIT released the full text free.
**Source:** https://web.mit.edu/6.001/6.037/sicp.pdf — live PDF hosted on MIT's own web.mit.edu domain under the 6.001/6.037 course materials.

## Lessons
- [Judge a system by its primitives, its means of combination, and its means of abstraction](../lessons/judge-a-system-by-its-three-mechanisms-not-its-features.md)
- [A definition that lets you recognize the answer is not one that produces it](../lessons/a-definition-that-identifies-is-not-a-definition-that-produces.md)
- [Adopt a model you have already decided to outgrow, and say where it will break](../lessons/adopt-a-model-you-have-already-decided-to-outgrow.md)
- [An abstraction boundary is a claim that a whole class of implementations is interchangeable](../lessons/an-abstraction-boundary-is-a-claim-about-an-equivalence-class.md)
- [What you may freely rename is exactly what you do not depend on](../lessons/what-you-may-rename-is-exactly-what-you-do-not-depend-on.md)
- [Scope exists so that strangers can both use the obvious name](../lessons/scope-exists-so-strangers-can-both-use-the-obvious-name.md)
- [Ask whether you could stop and resume from the named state; that is the test for whether the state is complete](../lessons/resumability-is-the-test-for-whether-your-state-is-complete.md)
- [A construct that looks essential may only be compensating for an implementation defect](../lessons/a-feature-that-looks-essential-may-be-compensating-for-a-defect.md)
- [Choose a measure for what it refuses to distinguish, not for its accuracy](../lessons/a-crude-measure-is-useful-because-of-what-it-refuses-to-see.md)
- [Distinguish a cost you incurred by transcribing the definition from a cost the problem actually has](../lessons/distinguish-naive-transcription-from-inherent-difficulty.md)
- [Compare your algorithm's error rate against the machine's, not against zero](../lessons/compare-your-error-rate-against-the-substrate-not-against-zero.md)
- [Repeating a test buys confidence only if you have proved the failures are independent](../lessons/repetition-buys-confidence-only-if-failures-are-independent.md)

- [Being able to compute a thing and being able to express the concept are different powers](../lessons/computing-a-thing-and-expressing-the-concept-are-different-powers.md)
- [When you see the same shape three times, write the template and turn its holes into parameters](../lessons/let-repetition-hand-you-the-abstraction-by-templating-it.md)
- [When an iteration oscillates instead of converging, damp the step rather than abandoning the formulation](../lessons/when-an-iteration-oscillates-damp-it-toward-the-previous-value.md)
- [First-class status is a checklist you can audit, not a compliment](../lessons/first-class-is-a-checklist-not-a-compliment.md)
- [Abstraction has an optimum, not a maximum](../lessons/abstraction-has-an-optimum-not-a-maximum.md)

- [Name the interface you wish you had, build everything on it, and decide the representation last](../lessons/name-the-interface-you-wish-you-had-and-build-on-it-first.md)
- [An interface without its laws is not a specification](../lessons/an-interface-without-its-laws-is-not-a-specification.md)
- [Algebraically equivalent formulas stop being equivalent once the values carry uncertainty](../lessons/rearranging-a-formula-is-not-safe-when-values-carry-uncertainty.md)
- [A means of combination that cannot consume its own output cannot build hierarchy](../lessons/a-combiner-that-cannot-consume-its-own-output-cannot-build-hierarchy.md)
- [An abstraction that changes nothing about execution can still be the whole point](../lessons/an-abstraction-can-change-nothing-about-execution-and-still-be-the-point.md)

- [Two programs can share a deep structure that neither one exhibits](../lessons/the-shared-structure-may-be-real-and-still-absent-from-the-text.md)
- [Modularity comes from agreeing on one interchange representation, not from splitting code into modules](../lessons/modularity-comes-from-agreeing-on-one-interchange-representation.md)

- [Build levels so that each one offers a different kind of change](../lessons/build-levels-each-of-which-offers-a-different-kind-of-change.md)
- [Embed a notation in a host language and it inherits the host abstraction machinery for free](../lessons/embed-your-notation-in-a-host-and-inherit-its-abstraction-for-free.md)

- [The power to mention your own expressions costs you the right to substitute equals for equals](../lessons/the-power-to-mention-costs-you-substitution-of-equals.md)
- [When the answers are correct but unusable, the fix belongs in the constructors, not the algorithm](../lessons/put-normalization-in-the-constructor-not-in-the-algorithm.md)
- [An invariant on the representation lets you conclude things about data you never looked at](../lessons/an-invariant-lets-you-conclude-things-about-data-you-never-looked-at.md)
- [Design the encoding so boundaries are unambiguous, rather than marking them](../lessons/make-the-stream-self-delimiting-instead-of-adding-separators.md)
- [Consume the statistics into the structure so the runtime never needs them](../lessons/consume-the-statistics-into-the-structure.md)
- [The argument for generic operations is organizational, not aesthetic: nobody can agree in advance](../lessons/the-case-for-genericity-is-that-agreement-is-impossible.md)
- [Deferring a decision and turning it into data are different moves, and the second costs you self-evident meaning](../lessons/deferring-a-choice-and-turning-it-into-data-are-different-moves.md)
- [Let the new part announce itself to the old part, never the reverse](../lessons/let-the-new-part-announce-itself-to-the-old-part.md)
- [An interaction between two modules has no natural owner, and that is the cost, not the code](../lessons/an-interaction-between-two-modules-has-no-natural-owner.md)
- [Look for the part that depends on fewer things than the whole, and factor along that seam](../lessons/factor-out-the-part-that-depends-on-fewer-things.md)
- [A hierarchy earns its keep by making one path unique, not by classifying things](../lessons/a-hierarchy-earns-its-keep-by-making-the-path-unique.md)
- [Decide whether a value really belongs to the simpler type by round-tripping the lossy conversion](../lessons/decide-membership-by-round-tripping-the-lossy-conversion.md)
- [When a question about your objects has no affordable answer, redefine the objects so it cannot be asked](../lessons/decide-what-your-object-is-so-the-unanswerable-question-cannot-arise.md)
- [Combine your parts with the generic operation and the data, not the author, decides how deep the structure goes](../lessons/call-the-generic-operation-and-the-data-decides-the-recursion.md)
- [Distort the input to stay inside the domain you can compute in, when the consumer cancels the distortion](../lessons/accept-a-wrong-answer-the-consumer-will-cancel.md)

- [Objects are the right decomposition only when the state actually clusters](../lessons/the-object-view-is-earned-by-clustered-state-not-chosen.md)
- [State you thread by hand infects every signature it passes through, and kills the general combinator](../lessons/state-you-thread-explicitly-infects-every-signature-it-passes-through.md)
- [Sameness and change are each defined in terms of the other, so neither can be settled by observation alone](../lessons/sameness-and-change-are-defined-in-terms-of-each-other.md)
- [Assignment converts choices that were free into commitments nothing writes down](../lessons/assignment-turns-free-choices-into-commitments.md)
- [No expression carries its own meaning; a context supplies it, and there is no privileged context](../lessons/no-expression-carries-its-own-meaning.md)
- [An object turns out to be shared code plus a frame that outlived the call that made it](../lessons/an-object-is-shared-code-plus-a-frame-that-outlived-its-call.md)
- [Adding one operation can promote an invisible property into the interface and void every equivalence you relied on](../lessons/adding-an-operation-can-promote-an-invisible-property-into-the-interface.md)
- [Give a mutable aggregate a handle that never moves, and hold the facts its operations would otherwise recompute](../lessons/give-a-mutable-aggregate-a-handle-that-never-moves.md)
- [An abstraction is unfinished until it supplies its own way of being looked at](../lessons/an-abstraction-owes-you-a-way-of-being-looked-at.md)
- [Wrapping a function optimizes only the calls that go through the wrapper, which the inner calls usually do not](../lessons/an-optimization-at-the-boundary-does-nothing-unless-the-recursion-routes-through-it.md)
- [Make time an explicit data structure, then decide what simultaneity means inside it](../lessons/make-time-a-data-structure-you-schedule-against.md)
- [A subscriber to changes learns nothing about the present, so joining must deliver a synthetic first event](../lessons/a-change-feed-tells-a-late-subscriber-nothing.md)
- [Concurrency correctness is a graded scale; pick the weakest rung the application can live with](../lessons/pick-the-weakest-correctness-criterion-the-application-can-live-with.md)
- [When the space of behaviours is combinatorial, shrink the space instead of checking it](../lessons/do-not-enumerate-the-interleavings-shrink-the-space-they-live-in.md)
- [The unit of atomicity belongs to the transaction, not the object, so no object can encapsulate its own concurrency control](../lessons/atomicity-belongs-to-the-transaction-not-the-object.md)
- [Every synchronization scheme bottoms out in a primitive you were given, and the bottom has physical limits](../lessons/every-synchronization-scheme-bottoms-out-in-something-given.md)
- [Shared state is not a thing that exists but an agreement communication produces, so questions about it between agreements can be meaningless](../lessons/shared-state-is-an-agreement-produced-by-communication.md)
- [A changing quantity and a fixed history are two descriptions of one thing; choosing the second deletes state without deleting the phenomenon](../lessons/a-changing-quantity-and-a-fixed-history-are-the-same-thing.md)
- [A thing may be defined in terms of itself whenever consumption provably lags production](../lessons/a-definition-may-use-itself-if-consumption-lags-production.md)
- [Reify the whole trajectory and improving the convergence becomes an ordinary program](../lessons/reify-the-whole-trajectory-and-improvements-to-convergence-become-ordinary-programs.md)
- [An enumeration of an unbounded space is correct only if every element has a finite arrival position](../lessons/an-enumeration-is-only-correct-if-every-element-has-a-finite-arrival-time.md)
- [A component that must see all its input before emitting anything cannot be placed in a loop](../lessons/a-component-that-needs-all-its-input-before-emitting-anything-forbids-feedback.md)
- [Whether a system has state is a fact about where the observer stands, not about the system](../lessons/whether-a-system-has-state-depends-on-where-the-observer-stands.md)
- [The ordering constraint is imposed from outside the program, so no programming style can remove it](../lessons/the-ordering-constraint-comes-from-outside-the-program-so-no-style-removes-it.md)

- [Put the notation behind predicates and selectors, and the rules of meaning outlive any notation](../lessons/put-the-notation-behind-predicates-and-selectors-and-the-meaning-outlives-it.md)
- [An implementation answers questions its own text never addressed, by silently borrowing the host's answers](../lessons/an-implementation-answers-questions-its-text-never-addressed.md)
- [Universality is cheap in a medium where machines are describable as data](../lessons/universality-is-cheap-when-the-machine-is-describable-as-data.md)
- [A boundary between two worlds can pass data across, but not behaviour](../lessons/a-boundary-between-two-worlds-passes-data-but-not-behaviour.md)
- [Working code is not evidence that you implemented the rule you meant](../lessons/working-code-is-not-evidence-that-you-implemented-the-rule-you-meant.md)
- [Split a computation along the line where its inputs arrive at different times](../lessons/split-a-computation-by-when-its-inputs-arrive.md)
- [Argue a design change by shipping something that runs it, not by describing it](../lessons/argue-a-design-by-shipping-something-that-runs-it.md)
- [Structure can be computed without content, which is why constructors are the things worth making non-strict](../lessons/structure-can-be-computed-without-content-so-constructors-should-be-non-strict.md)
- [A duplicated API is the symptom of a property missing one level down](../lessons/a-duplicated-api-is-the-symptom-of-a-property-missing-one-level-down.md)

- [Whether a description counts as a program is a fact about the evaluator, not about the description](../lessons/the-line-between-describing-and-computing-belongs-to-the-evaluator.md)
- [The constraints commute; their costs do not, so place each one where its inputs first exist](../lessons/constraints-commute-but-their-costs-do-not.md)
- [A rule set that returns one answer can never tell you it was ambiguous](../lessons/a-rule-set-that-returns-one-answer-cannot-tell-you-it-is-ambiguous.md)
- [A specification runs in both directions; the search order it inherits does not](../lessons/a-reversible-specification-carries-an-enumeration-order-that-is-not.md)
- [Adding a second way to fail obliges you to reclassify every existing failure](../lessons/adding-a-failure-channel-forces-you-to-reclassify-every-existing-failure.md)
- [You can only offer to rewind what you mediate, so the undo obligation lands on whoever owns the effect](../lessons/you-can-only-offer-to-rewind-what-you-mediate.md)
- [Name a handle for what it does, not for the circumstance that first needed it](../lessons/naming-a-handle-after-its-first-caller-hides-its-other-uses.md)
- [A declarative system does not remove method; it relocates the method into your choice among equivalent formulations](../lessons/declarative-does-not-remove-method-it-relocates-it-into-choosing-a-formulation.md)
- [In a formalism built on names, sameness is free and difference must be asserted](../lessons/identity-is-free-in-a-naming-formalism-but-distinctness-must-be-asserted.md)
- [A symmetric relation has no preferred side, so removing the duplicate requires an order the relation does not contain](../lessons/a-symmetric-relation-has-no-canonical-member-so-dedup-needs-an-outside-order.md)
- [Conjunction becomes composition, not intersection, once every stage accepts a partial answer](../lessons/conjunction-is-composition-when-each-stage-accepts-a-partial-answer.md)
- [Front an expensive test with a cheap one that is allowed to be wrong in only one direction](../lessons/front-an-expensive-test-with-a-cheap-one-that-can-only-be-wrong-one-way.md)
- [Any negative answer computed from a finite store is secretly a claim that the store is complete](../lessons/a-negative-answer-from-a-finite-store-is-a-claim-that-the-store-is-complete.md)
- [An operator implemented by removal only means what you think once its subject is determined](../lessons/an-operator-that-removes-has-a-precondition-the-notation-does-not-show.md)
- [A derivation engine hands you proofs, not facts, so anything you count over its output counts derivations](../lessons/a-derivation-engine-returns-proofs-not-facts-so-never-aggregate-its-output.md)
- [Adding a true statement can break a system that reads statements procedurally](../lessons/adding-a-true-statement-can-break-a-system-that-reads-statements-procedurally.md)
- [Design by choosing the weakest formalism that still says what you need, because weakness is what buys mechanical treatment](../lessons/choose-the-weakest-formalism-that-still-says-what-you-need.md)
- [A manipulation that goes through is not thereby meaningful, so validity must be established outside the symbols](../lessons/a-manipulation-that-goes-through-is-not-thereby-meaningful.md)
- [Where there is no scope there must be freshening, because a template used twice will otherwise constrain itself](../lessons/without-scope-you-must-freshen-names-at-every-instantiation.md)
- [Every joining operator has two dual implementations, and selectivity decides which one you want](../lessons/every-joining-operator-has-a-dual-implementation-and-selectivity-picks.md)
- [When an operation's precondition is not met yet, attach it to the data as a pending obligation rather than running or failing](../lessons/turn-an-unsatisfiable-precondition-into-an-obligation-carried-by-the-data.md)

- [A notation that resembles a more powerful one will be used as though it were that one](../lessons/a-borrowed-syntax-borrows-expectations-it-cannot-meet.md)
- [Information arriving from outside your model can be squeezed into an ordinary value; effects leaving it cannot](../lessons/effects-that-leave-your-boundary-need-their-own-category.md)
- [A dispatch whose arms grow with the number of callers means the caller should have passed the answer, not a token for it](../lessons/a-dispatch-that-grows-with-callers-means-the-caller-should-have-passed-the-answer.md)
- [Preserving more than is live is always correct, which is exactly why the waste never announces itself](../lessons/preserving-more-than-is-live-is-correct-and-therefore-invisible.md)

_EXTRACTION IN PROGRESS — 883 pages, hand-read in the main loop. Source text:
`scratchpad/sicp/sicp.txt` (30,343 lines). Body starts at line 784. Chapter
offsets: ch1 784, ch2 4662, ch3 10939, ch4 17804, ch5 23936, index ~29990.

**Read so far: all of chapter 1 and all of chapter 2 (lines 784-10940)** - data
abstraction, what data means, interval arithmetic, closure, sequences,
hierarchical structures, sequences as conventional interfaces, the picture
language with stratified design, symbolic data and quotation, symbolic
differentiation, set representations, Huffman encoding trees, multiple
representations and type tags, data-directed programming and message passing,
generic arithmetic, coercion, type towers, and symbolic algebra / polynomial
arithmetic including the rational-function extended exercise. Chapter 3 read
through the end of 3.2.3 (lines 10941-12340) - local state variables, benefits and
costs of assignment, sameness and change, and the environment model of evaluation.
Chapter 3 further read through 3.3.5 (lines 12341-14440) - internal definitions,
mutable list structure, sharing and identity, queues, tables, memoization, the
digital-circuit simulator and its agenda, and the start of constraint propagation.
Chapter 3 further read through the start of 3.5.1 (lines 14441-15840) - the rest of
constraint propagation, all of 3.4 Concurrency (nature of time, serializers,
mutexes, deadlock, communication), and the opening of 3.5 Streams.
**Chapter 3 is now complete (lines 15841-17639)** - the rest of 3.5.1 (delay/force
and memoization), 3.5.2 infinite streams and implicit definitions, 3.5.3 exploiting
the stream paradigm (iterations as stream processes, sequence acceleration and the
tableau, infinite streams of pairs, interleaving and weighted merge, streams as
signals), 3.5.4 streams and delayed evaluation (feedback loops, the delayed
integrand, normal-order evaluation), and 3.5.5 modularity of functional programs
versus modularity of objects (stream Monte Carlo, the functional view of time, the
joint-account merge problem). **Chapter 4 read through the start of 4.2.3 (lines
17804-20100)** - the whole of 4.1 The Metacircular Evaluator (eval/apply core,
representing expressions and abstract syntax, derived expressions, evaluator data
structures and environments, running the evaluator, data as programs and the
universal machine, internal definitions and simultaneous scope, separating
syntactic analysis from execution), 4.2.1 normal versus applicative order, 4.2.2
the lazy interpreter with thunks and memoization, and the opening of 4.2.3 streams
as lazy lists. Next unread line is **20100**. Rest of chapter 4 and all of chapter 5
are unread.

**READ IN PROGRESS (bucket 310 session):** resumed at line 20100. Read
20100-21200 — the rest of 4.2.3 lazy lists, all of 4.3.1 amb and search, 4.3.2
examples of nondeterministic programs (logic puzzles, natural-language parsing,
generation), and 4.3.3 implementing the amb evaluator through procedure
applications. Read 21200-21750 — the rest of 4.3.3 (evaluating amb expressions,
the driver loop and try-again), and the opening of 4.4 Logic Programming through
the start of 4.4.1 simple queries and pattern matching. Read 21750-22310 — the
rest of 4.4.1 (compound queries and the logical connectives, rules and rule
abstraction, recursive rules, logic as programs and the multi-directional append
relation), and 4.4.2 through the compound-query stream diagrams (pattern
matching, streams of frames, and/or as series and parallel combination).
Read 22310-22870 — the rest of 4.4.2 (negation and host-predicate filters,
unification and its partial solutions, applying rules and the analogy to
procedure application, the query evaluator and driver loop), all of 4.4.3 (is
logic programming mathematical logic — infinite loops, problems with negation,
the closed-world assumption), and the start of 4.4.4 implementation. **Next
Read 22870-23430 — 4.4.4.1 driver loop and instantiation, 4.4.4.2 the evaluator
(simple queries, conjoin/disjoin, the negation and host-predicate filters),
4.4.4.3 finding assertions by pattern matching, 4.4.4.4 rules and unification
(variable renaming, the unifier, the occurs check), and the start of 4.4.4.5
maintaining the data base. Read 23430-23990 — **all of chapter 4 is now
complete** (4.4.4.5 through 4.4.4.8: the index, stream operations, query syntax
procedures, frames and bindings, and the closing exercises) — plus the chapter 5
preamble and the opening of 5.1 designing register machines. **Next unread line
Read 23990-24550 — 5.1 designing register machines (data paths and controller
for the gcd machine), 5.1.1 the register-machine language and its two notations,
actions, 5.1.2 abstraction in machine design, and 5.1.3 subroutines through the
label-in-a-register solution. Read 24550-25110 — the rest of 5.1.3, 5.1.4 using
a stack to implement recursion (factorial and the double recursion for
Fibonacci), 5.1.5 instruction summary, 5.2 the register-machine simulator, and
5.2.1 the machine model through registers, the stack and the basic machine.
**Next unread line is 25110.** Currently
reading forward from there toward the index at ~29990. This line is updated as
chunks are finished — if this note still says a line below 29990 and there is no
`extraction: complete`, that number is the true resume point.
`extraction: complete` withheld until all five chapters are read._
