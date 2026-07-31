---
type: work
title: "Software Development: A Rigorous Approach"
figure: jones
description: Jones's first book-length treatment of VDM, showing how a program can be developed from a formal specification through a sequence of data reification and operation decomposition steps, each discharged with proof obligations. Establishes the specify-then-refine-with-proof-obligations pattern that later VDM texts and tools build on. Written while Jones was still at IBM Hursley, drawing on the VDM work done there.
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
year: 1980
url: http://homepages.cs.ncl.ac.uk/cliff.jones/publications/Books/SDRA.pdf
survey_pages: 400
survey_text_layer: ocr
survey_fetch_mb: 89
access: public
host: self-archived
tags: [work]
---

# Software Development: A Rigorous Approach

**Venue/year:** Prentice Hall International, 1980.
**Source:** http://homepages.cs.ncl.ac.uk/cliff.jones/publications/Books/SDRA.pdf — full scanned book self-archived on Jones's own Newcastle homepage, linked directly from his publications list (HTTP 200, confirmed live). Phase 1 had flagged this `paywalled`; a legitimate open copy exists on the author's own site.
**Reading copy:** `scratchpad/ocr-text/jones__software-development-a-rigorous-approach.txt` — OCR of the scanned original by tesseract at 300dpi. Running prose is reliable; **mathematical and logical notation is not** — turnstiles, implication arrows, subscripts and small-caps headings come through mangled. Ground every lesson in the prose argument and do not transcribe or rely on a formula from this text. Page markers `=== page N ===` correspond to PDF pages.

## Coverage

**Not yet attested — partial read across two sessions.** Line numbers below refer to
the OCR reading copy named above. PDF page = book page + 12.

An earlier session extracted 39 lessons whose source lines cite chapters 1-14, 17,
18, 19, 21 and 22, but left no coverage note and no attestation; it appears to have
died at the end without recording where it had been. Chapters 15, 16 and 20 and the
appendices carried no lessons at all, which is what the second session targeted.

Read in the second session (lines 14255-14926, 14927-15401, 16783-17740,
18190-19070, 19195-19603): the tail of chapter 14, all of chapter 15 (*On Being
Sufficiently Abstract), all of chapter 16 (*Implicit Definition of Data Types), the
Part C preamble, chapter 17 through "Language Support for Abstract Data Types", the
close of chapter 19 (Input/Output Statements) with its proof rules, all of chapter
20 (Josephus Rings), the opening of chapter 21, the close of chapter 22 from
"Anticipating Change" through "Environment Independence", appendix A (*Language
Definition), appendices B and C (rule and operator reference tables — no prose to
mine), the start of appendix D (*Selected Detailed Proofs — formal proof, no prose),
and the glossary in full. The tail from line 19604 to the end of file (20771) was
structurally sampled and confirmed to be answers to selected exercises, the
bibliography, the index and a colophon; none of it is lesson-bearing.

**Third session (complete).** Read lines 341-14254 in full and sequentially — the
front matter and preface, chapter 1 (Introduction), all of Part A (chapters 2-6:
Specifying Functions, Proofs About Functions, Specifying Programs, Proofs in Program
Development, Other Issues) and all of Part B (chapters 7-14: On Data Types, Set
Notation, List Notation, Data Type Invariants, Data Refinement, Mapping Notation,
*Theories of Data Types, Abstract Syntax). This was the span the coverage note
previously flagged as never read by anyone.

**Fourth session (IN PROGRESS — read started, note written before reading).**
Targeting the last spans nobody had read-and-attested: lines 1-340 (title pages and
table of contents), 15402-16782 (balance of chapter 17 from the class-construct
example onward, all of chapter 18 *Earley's Recognizer, opening of chapter 19),
17740-18189 (balance of chapter 21 Telegram Analysis, opening of chapter 22 through
"Programs and Their Data"), and the 19071-19194 gap between the third session's
recorded spans.

**Current position: line 17740** — span 15402-16835 read in full (balance of chapter
17 from the class-construct example through "Limitations", all of chapter 18
*Earley's Recognizer including Modifications, Summary and exercises, and the opening
of chapter 19 Input/Output Statements through the start of its Proofs section).
Moving to the next unread span, 17740-18189. This number is updated as the read
advances, so whatever it says is the resume point.
Position log: 341 -> 14254 (span complete) -> 15402 -> 16835 (span complete) -> 17740.

## Lessons
- [An argument cannot be retrofitted onto a finished artifact, so redevelop rather than reason backwards](../lessons/an-argument-cannot-be-retrofitted-onto-a-finished-artifact.md)
- [A prohibition does not travel; a discipline that tells you what to do next does](../lessons/a-prohibition-does-not-travel-a-constructive-discipline-does.md)
- [Borrow a notation that already has a discipline behind it, and treat it as shorthand rather than as ceremony](../lessons/borrow-a-notation-that-already-has-a-discipline-behind-it.md)
- [Say what you want by naming the check the answer must pass, ideally using an operation you already have](../lessons/specify-with-the-inverse-you-already-have.md)
- [Split cases at the point the branch appears, and expand whichever term occurs least](../lessons/split-the-cases-where-they-appear-and-expand-what-occurs-once.md)
- [Guard the partial term rather than teaching every operator about failure](../lessons/guard-the-partial-term-rather-than-teaching-every-operator-about-failure.md)
- [Minimize the basis you justify things against, then refuse to make anyone work in it](../lessons/minimize-the-basis-but-do-not-make-people-work-in-it.md)
- [Into a description you may borrow anything that denotes, and nothing that sequences](../lessons/borrow-things-that-denote-never-things-that-sequence.md)
- [Most obligations are vacuous, which is exactly what makes checking every one of them affordable](../lessons/most-obligations-are-vacuous-which-is-what-makes-checking-everything-affordable.md)
- [Give a sub-unit the widest terms it can honour, never the terms its one caller happens to need](../lessons/give-a-sub-unit-the-widest-terms-it-can-honour-not-the-ones-its-caller-needs.md)
- [Derive the invariant from the goal by putting the progress variable where the target value stands](../lessons/derive-the-invariant-from-the-goal-by-substituting-the-progress-variable.md)
- [Two descriptions from different viewpoints catch errors because their mistakes do not conspire](../lessons/errors-in-two-descriptions-do-not-conspire.md)
- [A method cannot be judged on small examples, because the property you are buying is invisible there](../lessons/a-method-cannot-be-judged-on-small-examples.md)
- [Put the proven artifact above the level where arbitrary commitments live, so one argument covers a family](../lessons/put-the-proven-artifact-above-the-level-where-arbitrary-commitments-live.md)
- [Support the form people actually write, and buy back the simplicity with a discipline on how it is used](../lessons/support-the-form-people-write-and-buy-simplicity-with-a-usage-discipline.md)
- [A correspondence established operation by operation never has to be executed](../lessons/a-correspondence-proved-per-operation-is-never-executed.md)
- [The abstract description is the instrument you use to collect what the representation decision requires](../lessons/the-abstract-model-is-the-instrument-for-gathering-what-the-representation-decision-needs.md)
- [Impose an arbitrary order on the elements and cycles stop being something you check for](../lessons/impose-an-arbitrary-order-to-make-cycles-impossible.md)
- [Separate what a thing means from how it is written, and watch the notation improve the thing](../lessons/separate-what-a-command-means-from-how-it-is-written.md)
- [Two things with identical contents are not the same thing, so let the construction carry the distinction](../lessons/identical-contents-are-not-the-same-thing-so-carry-the-tag.md)
- [Name the separable parts explicitly, so that what remains is the coupling you actually have to solve](../lessons/name-the-separable-parts-so-the-inseparable-one-is-what-you-work-on.md)
- [A language cannot pick your representation for you, because it cannot see how the operations will be used](../lessons/a-language-cannot-pick-the-representation-because-it-cannot-see-the-profile.md)
- [The decisions that actually decide performance are only visible once the detail is stripped away](../lessons/the-decisions-that-decide-performance-are-only-visible-with-detail-removed.md)
- [Narrow the boundary to a system you do not control, even when it costs you capability](../lessons/narrow-the-boundary-to-a-foreign-system-even-at-the-cost-of-capability.md)
- [Change the representation or the control flow, never both in one step, and do representation first](../lessons/change-the-representation-or-the-control-flow-never-both-at-once.md)
- [Make the control state explicit data and the order of work becomes yours to choose](../lessons/make-the-implicit-control-state-explicit-and-order-becomes-free.md)
- [Split a program into input, process, and output so the part worth reasoning about is a relation](../lessons/split-input-process-output-so-the-core-can-be-described-as-a-relation.md)
- [Write down every interpretation you had to make, because each one is a question you are answering for someone else](../lessons/write-down-every-interpretation-you-had-to-make.md)
- [Control flow shows what can happen; a variable hides it, so do not encode the one into the other](../lessons/control-flow-shows-what-can-happen-a-variable-hides-it.md)
- [Rank the requirements by how firm they are, and put your seams where the soft ones are](../lessons/rank-the-requirements-by-firmness-and-put-the-seams-there.md)
- [Move the volatile policy into a table its owner can edit, and let the program interpret the table](../lessons/move-the-volatile-policy-into-a-table-the-owner-can-edit.md)
- [Design the error-free case first, then add checking in a form that does not disturb its shape](../lessons/design-the-error-free-case-then-add-checking-without-disturbing-its-shape.md)
- [A proof covers your reasoning, not the substrate underneath it, so keep a cheap check at run time](../lessons/a-proof-covers-your-reasoning-not-your-substrate.md)
- [The reason a design is believed correct is an output of designing it, and nobody downstream can reconstruct it](../lessons/the-reason-is-an-output-of-design-and-nobody-else-can-reconstruct-it.md)
- [Make the skeleton formal and leave the leaves soft, so precision can be bought one place at a time](../lessons/make-the-skeleton-formal-and-leave-the-leaves-soft.md)
- [Among models that describe the same thing, pick the one that entails the properties you would otherwise have to maintain](../lessons/among-faithful-models-pick-the-one-that-entails-what-you-would-have-to-maintain.md)
- [A property names a thing only when it pins the thing down, so find out which parts of the structure it leaves free](../lessons/a-property-names-a-thing-only-when-it-pins-it-down.md)
- [An unenforced boundary still pays, so pick the strength of enforcement you can actually afford](../lessons/an-unenforced-boundary-still-pays-so-pick-the-enforcement-you-can-afford.md)
- [Re-enter a change at the level where the decision was made, because a design record left stale is worse than no record](../lessons/re-enter-a-change-at-the-level-that-decided-it-and-a-stale-record-is-worse-than-none.md)
- [An invariant is a promise at the boundaries, not a claim about every instant](../lessons/an-invariant-is-a-promise-at-the-boundaries-not-at-every-instant.md)
- [A formal notation removes ambiguity but not incompleteness or self-contradiction, so bring a discipline that tells you when you have said enough](../lessons/formality-removes-ambiguity-not-incompleteness-or-contradiction.md)
- [Run the over-specification check before there is an implementation to hide it, because the first builder never feels the cost and the second cannot avoid it](../lessons/run-the-over-specification-check-before-there-is-an-implementation-to-hide-it.md)
- [A value invented to satisfy the machinery is indistinguishable from a requirement once it is written down](../lessons/a-value-invented-to-please-the-machinery-reads-as-a-requirement.md)
- [Encoding a new kind of thing into machinery you already have costs you exactly the property that made it a new kind of thing](../lessons/encoding-a-new-thing-into-old-machinery-costs-you-the-property-that-made-it-new.md)
- [Justify a step against its nearest predecessor, and when several predecessors would do, pick whichever makes the argument shortest](../lessons/justify-each-step-against-its-cheapest-predecessor-not-against-the-origin.md)
- [What outgrew your methods is the interaction surface, not the size of your program](../lessons/what-grew-is-the-interaction-surface-not-your-program.md)
- [An argument that goes lopsided is telling you the code made a choice it did not have to make](../lessons/an-asymmetric-argument-is-how-a-gratuitous-choice-announces-itself.md)
- [The cases your argument fails to reach are the inputs your code fails to return on](../lessons/the-cases-your-argument-misses-are-the-inputs-that-diverge.md)
- [Deciding that a thing has state at all is a design step, and it should not be the first one](../lessons/deciding-that-there-is-state-at-all-is-its-own-step.md)
- [Fold the awkward global property into what 'meets its description' locally means, and composition stops charging you for it](../lessons/fold-the-global-property-into-the-local-contract.md)
- [A repetition can be described by what it has accomplished or by what it has left to do, and the code tells you which](../lessons/describe-a-repetition-by-progress-made-or-work-remaining.md)
- [Find the right abstraction by looking at the implementations you would consider and keeping only what they agree on](../lessons/find-the-abstraction-by-abstracting-over-the-implementations-you-would-consider.md)
- [Write down the consequence even though it already follows, because derivable is not the same as available](../lessons/write-down-the-consequence-even-though-it-follows.md)
- [Do not let the formalism you must store things in be the vocabulary you describe them in](../lessons/do-not-let-the-storage-formalism-be-your-description-language.md)
- [A housekeeping operation is exactly one that is the identity when viewed through the abstraction, and proving that buys you everything else](../lessons/a-housekeeping-operation-is-one-that-is-invisible-through-the-abstraction.md)
- [A published algorithm arrives already partway down the development chain, so work out which step it is](../lessons/a-published-algorithm-arrives-partway-down-the-chain.md)
- [The first design step is to restate the check as a construction, before any representation or ordering is chosen](../lessons/the-first-design-step-is-to-restate-the-check-as-a-construction.md)
- [Bound an accumulating structure from both sides, and you have characterised a family of algorithms rather than checked one](../lessons/bound-a-structure-from-both-sides-to-characterise-a-family.md)
- [Put a penultimate level between the abstraction and the machine: target shape, reasoning notation](../lessons/put-a-penultimate-level-between-the-abstraction-and-the-machine.md)
- [Justify skipping work by showing what you skipped was empty, and prefer a filter that can only err toward doing it](../lessons/justify-a-skip-by-showing-the-skipped-work-was-empty.md)
- [If the algorithm did not change, you simulated the description rather than implemented it](../lessons/if-the-algorithm-did-not-change-you-simulated-rather-than-refined.md)
- [A change you anticipated is not evidence your design absorbs change](../lessons/a-change-you-anticipated-is-not-evidence-your-design-absorbs-change.md)
