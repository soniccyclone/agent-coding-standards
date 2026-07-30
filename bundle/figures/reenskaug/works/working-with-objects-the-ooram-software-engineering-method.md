---
type: work
title: "Working with Objects: The OOram Software Engineering Method"
figure: reenskaug
description: A book-length treatment of OOram, Reenskaug's role-modeling method for object-oriented analysis and design, built around the idea of describing a system as a set of collaborating roles before ever committing to classes. The book works through the method across the full lifecycle — analysis, design, and synthesis of roles into concrete classes — with worked examples throughout. Now out of print; the authors put the final pre-publication draft online themselves once it went out of circulation, noting it lacks only the copy editor's final pass.
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
year: 1996
url: https://folk.universitetetioslo.no/trygver/1996/book/WorkingWithObjects.pdf
survey_pages: 497
survey_text_layer: full
survey_fetch_mb: 1
access: public
host: self-archived
extraction: complete
tags: [work]
---

# Working with Objects: The OOram Software Engineering Method

**Author(s):** Trygve Reenskaug, with Per Wold and Odd Arild Lehne
**Venue/year:** Prentice Hall, 1996 (this self-archived copy is the final pre-publication draft, dated 2001).
**Source:** https://folk.universitetetioslo.no/trygver/1996/book/WorkingWithObjects.pdf — self-archived by Reenskaug on his University of Oslo homepage after the printed book went out of print; the PDF's own title page states it's made freely available for that reason. Verified live (HTTP 200, direct PDF, ~2MB) and confirmed by extracting the text of the first pages.

## Lessons
- [Without the question, there is nothing in a model to judge](../lessons/a-model-answers-a-question-or-cannot-be-judged.md)
- [Hierarchy is an artifact of thought, not a property of the world](../lessons/hierarchy-is-an-artifact-of-thought-not-a-property-of-the-world.md)
- [Composition is reuse only when it preserves what you already checked](../lessons/composition-is-reuse-only-if-it-preserves-what-you-already-checked.md)
- [Extending one part alone is meaningless; extend the arrangement](../lessons/extend-the-arrangement-not-the-part.md)
- [Permission belongs to the relationship, not to the interface](../lessons/permission-belongs-to-the-relationship-not-the-interface.md)
- [The rigidity that makes an organization inhuman is exactly right for machines](../lessons/rigidity-that-is-inhuman-is-correct-for-machines.md)
- [Many views, one model — never let a view become the model](../lessons/many-views-one-model-never-let-a-view-become-the-model.md)

- [Sort your correctness claims by who can check them, because a tool's silence is not approval](../lessons/classify-your-correctness-claims-by-who-can-check-them.md)
- [Start where the risk is, not at the top of the abstraction ladder](../lessons/start-where-the-risk-is-not-where-the-abstraction-is.md)
- [When the ugly requirement arrives, describe it somewhere else and compose, rather than spoiling the clean description](../lessons/model-the-mess-separately-and-compose-it-in.md)
- [When you borrow a mechanism, permit it less than its source did](../lessons/deliberately-narrow-a-borrowed-mechanism.md)
- [Size each description to what a reader can hold at once, and exempt the pieces that get reused everywhere](../lessons/size-a-description-to-working-memory-with-a-reuse-exception.md)
- [Reuse costs you the fresh look, and the person advocating it should be the one to say so](../lessons/name-reuses-own-cost.md)

- [Of the programs that work, confine yourself to the ones you can understand — the machine will accept far worse](../lessons/restrict-yourself-to-the-programs-you-can-understand.md)
- [Building it is the experiment that tells you whether your separation of concerns was real](../lessons/implementation-is-the-test-of-whether-your-decomposition-was-real.md)
- [A description complete enough to generate the system has become the system, and needs its own abstraction](../lessons/a-description-detailed-enough-to-generate-code-is-code.md)

- [A picture too tangled to draw honestly is evidence about the program, not about the picture](../lessons/a-diagram-too-complex-to-draw-indicts-the-program.md)
- [Draw a boundary, distrust everything crossing it, and trust everything inside](../lessons/check-at-the-firewall-and-trust-inside-it.md)
- [Learn a new way of thinking in a language that forbids the old one, even if you will ship in one that permits both](../lessons/similarity-to-the-old-paradigm-impedes-learning-the-new.md)
- [Constrain a variable by what its occupant must be able to do, never by how the occupant is built](../lessons/type-on-what-an-object-can-do-not-on-how-it-is-built.md)

- [Whether a component gets adopted is uncorrelated with how good it is](../lessons/adoption-does-not-track-technical-quality.md)
- [Anticipated flexibility goes unused and does not prevent the extensions you failed to anticipate](../lessons/hooks-for-every-need-refuted-by-its-own-usage-data.md)
- [Write the consumer's instructions before you build the thing, and let your laziness simplify the interface](../lessons/write-the-manual-before-the-thing-and-let-laziness-design-it.md)
- [Name every assumption that crosses a component boundary, then freeze exactly that and improve everything behind it](../lessons/specify-and-freeze-the-surface-area.md)
- [Separate what a reader can already do from what they can only recognize, and layer the documentation on that seam](../lessons/layer-documentation-by-active-versus-passive-competence.md)
- [Your process is varnish over your people's competence, and it only holds where that competence already reaches](../lessons/formalism-is-varnish-on-competence.md)

- [A description in terms of kinds cannot say it was the same one throughout](../lessons/types-cannot-express-that-it-is-the-same-one.md)
- [The compositions that stay safe are exactly the ones that refuse to multiply the state space](../lessons/safe-composition-is-composition-that-does-not-multiply-states.md)
- [Two organizations can share one coherent system while nobody anywhere understands all of it](../lessons/integrate-through-shared-models-so-nobody-holds-the-whole.md)
- [Introduce the expensive notation last, and prefer redesigning the thing so you never need it](../lessons/defer-the-notation-whose-cost-is-volume.md)

- [Known confusion is safe; it is the undetected mismatch that destroys projects](../lessons/undetected-agreement-is-the-dangerous-state.md)
- [What matters most about how work gets done is what nobody thinks to mention](../lessons/the-most-important-facts-are-the-ones-nobody-mentions.md)
- [Before integrating two groups' data, separate their words from their concepts](../lessons/separate-the-term-from-the-concept-before-integrating.md)
- [The channel you are automating is also carrying the social and teaching traffic](../lessons/a-work-channel-carries-social-and-training-traffic-too.md)
- [Permit a dependency only in the direction of the thing that changes more slowly](../lessons/allow-coupling-only-toward-what-changes-more-slowly.md)

- [When two groups mean different things by one word, translating beats forcing them to agree](../lessons/translate-to-the-users-model-rather-than-harmonizing-vocabularies.md)
- [Treat any exclamation of surprise from a user as a bug report against the design](../lessons/astonishment-is-a-defect-report.md)
- [Slowness costs you the user's held state, so make every operation small enough to complete inside their attention](../lessons/latency-breaks-the-circuit-so-make-operations-closeable.md)
- [Let people point at what they can see, and accept that some things should have no name](../lessons/pointing-beats-naming-and-not-everything-needs-a-name.md)

- [Choose the conformance check that works in every case over the one that would be elegant](../lessons/prefer-the-conformance-check-that-always-applies.md)
- [A design idea impossible to express in one substrate can be the native vocabulary of another](../lessons/the-same-design-idea-can-be-native-in-one-substrate-and-impossible-in-another.md)

- [The class hierarchy will not tell you how the thing works; only the collaboration will](../lessons/inheritance-structure-explains-nothing-about-behavior.md)
- [To understand a mechanism, dissect its simplest instance, not its most representative one](../lessons/reverse-engineer-through-the-simplest-instance.md)
- [Ask which parts of a famous decomposition were forced by the language rather than by the problem](../lessons/mvcs-author-on-which-of-its-splits-was-a-language-artifact.md)
- [Showing two views of one thing at once costs the feeling that the thing is real, and that is a choice to make deliberately](../lessons/multiple-views-cost-you-the-illusion-of-a-concrete-thing.md)
- [There are exactly three ways to promise a delivery date, and two of them are honest](../lessons/the-three-ways-to-make-a-firm-commitment.md)
- [A caller that walks the structure to reach a service has absorbed the structure](../lessons/a-caller-that-walks-the-structure-has-absorbed-the-structure.md)
- [Simplicity is a property of the whole a user must hold, not of each part](../lessons/simplicity-is-a-property-of-the-whole-a-user-must-hold.md)
- [Write requirements as limits on what the user is permitted to have to know](../lessons/write-requirements-as-limits-on-what-the-user-must-know.md)
- [Give each attribute one legal direction of inquiry, and forbid the other](../lessons/give-each-attribute-one-legal-direction-of-inquiry.md)
- [When the vocabulary you inherited is ambiguous, coin your own rather than guess at the original intent](../lessons/coin-your-own-terms-rather-than-guess-at-inherited-intent.md)
- [A responsibility that keeps changing owners belongs to whoever already carries its obligations](../lessons/home-a-roving-responsibility-where-its-obligations-already-live.md)
- [Size a general escape hatch to what existing code actually needed, and admit when you cannot justify it](../lessons/size-the-escape-hatch-to-what-existing-code-actually-needed.md)
- [When automatic derivation fails, require a declaration and mechanically audit it for completeness](../lessons/when-derivation-fails-require-a-declaration-you-can-audit.md)

- [A process model with no actor dimension smuggles in the author's own role as the default](../lessons/a-process-model-without-an-actor-dimension-hides-the-handoffs.md)
- [An environment built to satisfy every internal audience will satisfy none of them](../lessons/one-environment-for-every-need-satisfies-nobody.md)
- [Assume your consumers are hostile, but expect ignorance rather than malice — and pair every restriction with completeness](../lessons/the-threat-from-the-layer-above-is-ignorance-not-malice.md)
- [The simple picture is a deliverable someone owns, and that someone is not in the picture](../lessons/someone-must-own-the-simple-picture-and-they-are-not-in-it.md)
- [Delivery adds entropy and generalization removes it; each has a visible failure signature when it dominates](../lessons/production-adds-entropy-cleanup-removes-it-neither-may-dominate.md)
- [Rotate people between building and generalizing, alternately — holding both at once collapses to the nearer deadline](../lessons/alternate-the-two-jobs-over-time-never-hold-both-at-once.md)
- [An investment you cannot price needs a decider who has done both jobs, not a better formula](../lessons/an-investment-you-cannot-price-needs-a-decider-who-has-done-both.md)
- [When your data cannot answer the question, find the person already answering it and name the role](../lessons/when-your-data-cannot-answer-name-the-person-already-answering.md)
- [There is no best reuse mechanism — match it to the layer, and expect the crude one to win somewhere](../lessons/there-is-no-best-reuse-mechanism-match-it-to-the-layer.md)
- [Hold the bespoke one percent to different standards than the library it sits on](../lessons/hold-the-bespoke-one-percent-to-different-standards-than-the-library.md)

- [Broker the match at runtime so installing one part makes it available everywhere it fits](../lessons/broker-the-match-at-runtime-so-installing-a-part-lights-it-up-everywhere.md)
- [The good-default-plus-escape shape is found by failing at both poles, and both failures are necessary](../lessons/good-default-plus-escape-is-found-by-failing-at-both-poles.md)
- [Nobody asks for what they believe is impossible, so absence of a request is not absence of a need](../lessons/nobody-asks-for-what-they-believe-impossible.md)
- [Leaving a mature framework costs you all of its tooling at once — so decide whether you are stepping outside it or widening it](../lessons/leaving-a-mature-framework-costs-you-its-tooling-all-at-once.md)
- [A substrate that can represent anything cannot be used without programming, and that is the trade](../lessons/generality-forecloses-generation.md)
- [Three conceptual frameworks succeeded in fifty years — price your own proposal against that base rate](../lessons/count-the-conceptual-frameworks-that-actually-succeeded.md)
- [Constrain the transitions rather than the states, and schema change stops requiring migration](../lessons/constrain-the-transition-not-the-state.md)
- [Instantiating gives you what the programmer specified; copying a validated master gives you what was learned](../lessons/copying-a-validated-master-is-a-production-technique.md)
- [An operation whose extent depends on the caller's intent cannot have a correct default](../lessons/an-operation-whose-extent-depends-on-intent-has-no-correct-default.md)
- [Separate difficulty that comes from the specification from difficulty that comes from the technology](../lessons/separate-difficulty-in-the-specification-from-difficulty-in-the-technology.md)
- [Let the framework hold the global problem and ask each participant exactly one local question](../lessons/let-the-framework-hold-the-global-problem-and-ask-each-part-one-local-question.md)
- [Require a redundant statement for every choice, so forgetting is distinguishable from deciding](../lessons/make-omission-distinguishable-from-decision.md)

- [Narrow a word deliberately until the goal stated with it becomes checkable](../lessons/narrow-the-definition-until-the-goal-becomes-checkable.md)
- [Let each authority bind the parameters it alone knows and pass the artifact on still open](../lessons/let-each-authority-bind-what-it-knows-and-pass-the-rest-down.md)
- [Gate expressive power by the operator's competence, using the same machinery restricted differently](../lessons/gate-expressive-power-by-competence-using-the-same-machinery.md)
- [Express legality as where things can be placed, not as an error after they are](../lessons/express-legality-as-where-things-can-go-not-as-an-error.md)
- [Make the signed agreement and the deployment input the same artifact](../lessons/one-artifact-that-is-both-the-signed-agreement-and-the-deployment-input.md)
- [Mark the extension surface in the design notation itself, and seal everything else](../lessons/declare-the-extension-surface-in-the-model-and-seal-the-rest.md)
- [A demonstrator validates the shape of an answer, not its scale — so enumerate what it left out](../lessons/a-demonstrator-validates-the-shape-not-the-scale.md)
- [An interface that ships with a reference card is the wrong interface, and invisible modes are why](../lessons/an-interface-needing-a-reference-card-is-the-wrong-interface.md)
- [Split a two-party protocol at the ownership boundary so each side's policy lives in the object it owns](../lessons/split-a-protocol-at-the-ownership-boundary.md)

- [Carry identity in an opaque handle, then constrain the human names by whatever consumes them downstream](../lessons/identity-by-opaque-handle-names-constrained-by-the-generation-target.md)
- [Write the textual grammar even when your tool is graphical — the grammar is where you find out if the concepts cohere](../lessons/write-the-grammar-even-when-the-tool-is-graphical.md)

_EXTRACTION NOTES — updated 2026-07-29. Source is the `pdftotext -layout`
extraction held at `scratchpad/reenskaug/ooram-slim.txt` (21,176 lines = 497 book
pages).

All twelve chapters and the appendix prose were read in full, by hand, in the main
loop rather than by a subagent — the `pdftotext -layout` extraction at
`scratchpad/reenskaug/ooram-slim.txt`, 21,176 lines for 497 book pages. Reading ran
chapter by chapter with lessons written and committed after each, so a death
mid-book would have cost one chapter rather than the run.

Covered: preface and chapters 1-12 (lines 1-19239) plus appendix A1-A3 (19240-19536),
which is the OOram language's purposes, lexical conventions, EBNF grammar and scoping
rules.

Deliberately not treated as lesson-bearing: appendices A4 and A5 (19537-19983) are
tool-generated OOram-language listings of the travel-expense and synthesis models
whose prose treatment is in chapters 7 and 3 and is already extracted; appendix B
(19984-20289) is the bibliography; everything from ~20600 is the table of contents.
Read and checked, no independent content.

`extraction: complete` is set on the strength of that pass._
