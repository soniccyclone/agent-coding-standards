---
type: work
title: "Project Oberon: The Design of an Operating System and Compiler"
figure: wirth
description: A full workstation environment — operating system, compiler, and user interface for the Oberon language and its Ceres hardware — documented top to bottom, including source code, as a demonstration that a complete, usable system could be built and understood by a tiny team instead of a large organization. Written with Jurg Gutknecht, it operationalizes Wirth's stepwise-refinement and lean-software convictions at the scale of a whole system rather than a single program. The book doubles as an extended case study in single-author-comprehensible systems design, later re-issued with updated editions targeting FPGA-based RISC hardware.
subdomains: [operating-systems-and-systems-programming, programming-environments-and-object-systems]
year: 1992
url: https://people.inf.ethz.ch/wirth/ProjectOberon1992.pdf
survey_pages: 441
survey_text_layer: full
survey_fetch_mb: 4
access: public
host: self-archived
tags: [work]
---

# Project Oberon: The Design of an Operating System and Compiler

**Author(s):** Niklaus Wirth and Jurg Gutknecht
**Venue/year:** Addison-Wesley / ACM Press, 1992.
**Source:** https://people.inf.ethz.ch/wirth/ProjectOberon1992.pdf — live PDF, self-archived on Niklaus Wirth's ETH Zurich personal page.

## Coverage note (partial extraction — NOT exhausted)

**READ IN PROGRESS (2026-07-31 session, seventh agent): resumed at line 18598, working
forward toward line 22864 (the end). Current position recorded below; if this file still
says "in progress" the session died and the position line is the truth.**

**Current position: line 18598 — seventh agent starting here. Identity re-verified against
`scratchpad/PO.txt` (22864 lines, title page names Wirth and Gutknecht). Sixth agent left
no new lessons and no position advance beyond 18598. Plan: module OCC listing (source, scan
for prose) to 19181, then 12.9 onward, ch. 13 (graphics editor), ch. 14 at 22341,
appendix A.**

**Third agent's handoff: had read and mined chapter 12 through
section 12.8's prose (code patterns 1-15; Object/Item/Struct; the OCS/OCE/OCH interfaces;
12.4 parser, 12.5 scanner, 12.6 symbol table and symbol files, 12.7 code selection incl.
the OCH statement/call/case commentary at 17902-17958, 12.8 code generation incl. the
NS-32000 format summary, the object file / reference block passage and the two-address
emission remark). Lines 14830-15799 (Compiler), 15825-16108 (OCS), 16294-16781 (OCT) and
16957-17900 (OCE) are pure Oberon source, checked and confirmed to hold no prose. Now in
the module OCC listing at 18598; next prose section is 12.9 at line 19181.**

**Earlier: chapter 9 complete and mined (9.1-9.4, including the
serial line, the network driver and its comment list, and the SCSI disk driver); chapter 10
read and mined in full including the module Net listing (pure Oberon source, no prose);
chapter 11 read and mined in full; chapter 12 read and mined through section 12.2's opening
(to line 13764). Earlier state, still true:
chapter 5 prose complete through section 5.5 (text frames,
font machinery, edit toolbox) and the chapter-5 literature list; chapter 5's
complete-implementations listing (lines ~4900-7049, modules Fonts, Texts, TextFrames,
Edit) checked for prose and confirmed to be pure Oberon source with no explanatory
paragraphs; chapter 6 complete and mined (6.1-6.5, including the loader toolbox and the
object file format); chapter 7 read and mined in full (7.1 files and riders, 7.2 files on a
random-access store, 7.3 files on a disk plus the trailing commentary, 7.4 the B-tree
directory, 7.5 the file utility toolbox and the chapter's literature list). Chapter 7's
interleaved module listings were checked for prose and are pure Oberon source. Chapter 8
read and mined in full (8.1 storage layout, 8.2 module blocks, 8.3 dynamic storage and
the collector, 8.4 the kernel); chapter 9 read and mined through section 9.2's UART
discussion (to line 10480).**

Read against `pdftotext -layout` output of the 2005 edition PDF (441 pages → 22864 lines
of extracted text). Identity verified: title page and preface name N. Wirth and J.
Gutknecht, Project Oberon, ETH Zurich, February 1992. Re-verified 2026-07-31 against
`scratchpad/PO.txt` (22864 lines, matches).

**Read and mined:** front matter and table of contents; chapter 5 sections 5.1 and 5.2
(text as abstract data type; text management and the piece-chain representation, through
the auxiliary FindPiece/SplitPiece procedures at line 3991); chapter 1 (Historical Background
and Motivation); chapter 2 in full (Basic Concepts and Structure of the System — viewers,
commands, tasks, tool texts, extensibility, dynamic loading, module hierarchy, chapter
tour); chapter 3 in full (The Tasking System — interactive and background tasks, the
scheduler, the concept of command, generic facilities, toolboxes, and the complete
listings of modules Oberon and System); chapter 4 through section 4.6 (The Display System
— screen layout model and the tiling comparison, viewers as objects, frames, display
management including viewer management, menu viewers and cursor management, raster
operations, standard display configurations). Extraction stops mid-way through the
literature list at the end of chapter 4.

**Not read:** the remainder of chapter 5 from line 3991 on — the rest of the piece-chain
implementation, section 5.3 (text frames), 5.4 (the font machinery), 5.5 (the edit
toolbox) — and everything after it: chapter 6 (The Module
Loader); chapter 7 (The File System); chapter 8 (Storage Layout and Management); chapter 9
(Device Drivers); chapter 10 (The Network); chapter 11 (the dedicated server); chapter 12
(The Compiler); chapter 13 (A Graphics Editor); chapter 14 (Building and Maintenance
Tools); and appendix A (Ten Years After: From Objects to Components).

**Resume at line 3991** of the extracted text — inside procedure `SplitPiece`, part way
through section 5.2's implementation walkthrough. Everything above that line has been
read, including the complete listings of modules Viewers, MenuViewers and the display
section of System at lines 2917–3504, which are source code and yielded no lesson beyond
what the chapter-4 prose already gave. Regenerate the text with:
`pdftotext -layout ProjectOberon1992.pdf PO.txt`.

Chapter start lines in the extracted text, for planning a resumed pass: ch. 5 at 3532,
ch. 6 at 7049, ch. 7 at 7696, ch. 8 at 9747, ch. 14 at 22341 (chapters 9–13 fall between
9747 and 22341 and their headings did not extract as clean line starts).

Note that a large fraction of the remaining lines are complete Oberon source listings
rather than prose; the prose sections at the head of each chapter and each numbered
section are where the extractable lessons are.

## Lessons
- [Separate the unit of action from the unit of packaging](../lessons/separate-the-unit-of-action-from-the-unit-of-compilation.md)
- [Pick the switching granularity first; the protection machinery follows from it](../lessons/pick-the-switching-granularity-first-the-protection-follows-from-it.md)
- [Root a tree of requests instead of fixing a set of operations](../lessons/root-a-tree-of-requests-instead-of-fixing-a-set-of-methods.md)
- [Prefer the state that is already visible as the interface between steps](../lessons/prefer-the-state-that-is-already-visible-as-the-interface.md)
- [A participant that can fail should be removed before it runs, not after](../lessons/a-repeatedly-failing-participant-should-eject-itself.md)
- [Price a metaphor by the actions it actually produces](../lessons/price-a-metaphor-by-the-actions-it-actually-produces.md)
- [Bind at the latest moment, so each part exists exactly once](../lessons/bind-at-the-latest-moment-so-each-part-exists-once.md)
- [Choose the arrangement whose undo is simple, not the one whose forward move is free](../lessons/choose-the-arrangement-whose-undo-is-simple.md)
- [Ask the population instead of maintaining a registry](../lessons/ask-the-population-instead-of-maintaining-a-registry.md)
- [Make the container and the contained the same kind of thing, and global policy becomes a local default](../lessons/make-the-container-and-the-contained-the-same-kind-of-thing.md)
- [A self-inverse operation needs no saved copy and no precondition](../lessons/a-self-inverse-operation-needs-no-saved-copy.md)
- [Let each level transform requests for the level below it, and never reach past a child](../lessons/let-each-level-transform-requests-for-the-level-below-it.md)
- [Edit the description, not the contents](../lessons/edit-the-description-not-the-contents.md)
- [An indirection relocates cost into demands on the layer below](../lessons/an-indirection-relocates-cost-into-demands-on-the-layer-below.md)
- [Attach state to the level you want to have several of](../lessons/attach-state-to-the-level-you-want-several-of.md)
- [Export the default and the parts it was assembled from](../lessons/export-the-default-and-the-parts-it-was-assembled-from.md)
- [A requirement that lets later input revise earlier output costs you a whole pass](../lessons/a-requirement-that-lets-later-input-revise-earlier-output-costs-a-pass.md)
- [A cache is a question about its two neighbours, not about itself](../lessons/a-cache-is-a-question-about-its-two-neighbours.md)
- [Privacy in the module graph is not privacy in time](../lessons/privacy-in-the-module-graph-is-not-privacy-in-time.md)
- [Re-read a specialized notion as a pair, and discover the general case is already built](../lessons/reread-a-specialized-notion-as-a-pair-and-the-general-case-is-already-built.md)
- [Test an extension point by rebuilding something already built in](../lessons/test-an-extension-point-by-rebuilding-something-already-built-in.md)
- [Split a description where the cheap half answers most of the questions](../lessons/split-a-description-where-the-cheap-half-answers-most-questions.md)
- [A proposed extra stage is evidence of an undiagnosed cost](../lessons/a-proposed-extra-stage-is-evidence-of-an-undiagnosed-cost.md)
- [Indirect when references outnumber referents, and count before deciding](../lessons/indirect-when-references-outnumber-referents.md)
- [An interface should publish an ordinal, not a fact about the implementation](../lessons/an-interface-should-publish-an-ordinal-not-a-fact-about-the-implementation.md)
- [Ship what the compiler knew, and let the transport carry it uninterpreted](../lessons/ship-what-the-compiler-knew-and-let-the-transport-carry-it-uninterpreted.md)
- [A reference count counts only the references your mechanism can see](../lessons/a-reference-count-counts-only-the-references-your-mechanism-can-see.md)
- [State that duplicates a shared fact belongs to the shared thing, not to the accessor](../lessons/state-that-duplicates-a-shared-fact-belongs-to-the-shared-thing.md)
- [Schedule the global analysis for the moment its input is simplest](../lessons/schedule-the-global-analysis-for-the-moment-its-input-is-simplest.md)
- [Prefer the base structure whose shape needs no separate encoding](../lessons/prefer-the-base-structure-whose-shape-needs-no-separate-encoding.md)
- [State the instruction budget for the frequent case before choosing a representation](../lessons/state-the-instruction-budget-for-the-frequent-case-before-choosing-a-representation.md)
- [Place an operation by who may call it, not by what it touches](../lessons/place-an-operation-by-who-may-call-it-not-by-what-it-touches.md)
- [An unwinnable argument about a constant means it should not be one constant](../lessons/an-unwinnable-argument-about-a-constant-means-it-should-not-be-one.md)
- [A hint is a cache that owes nothing to coherence](../lessons/a-hint-is-a-cache-that-owes-nothing-to-coherence.md)
- [Nesting a searchable set costs you unless the nesting factors out a shared attribute](../lessons/nesting-a-searchable-set-costs-you-unless-it-factors-a-shared-attribute.md)
- [An optimization that holds durable state in volatile store is a correctness change](../lessons/an-optimization-that-holds-durable-state-in-volatile-store-is-a-correctness-change.md)
- [Obtaining a handle to something external is a lookup, not an allocation](../lessons/obtaining-a-handle-to-something-external-is-a-lookup-not-an-allocation.md)
- [Buy detection by representing a critical value sparsely](../lessons/buy-detection-by-representing-a-critical-value-sparsely.md)
- [Two growing consumers of one resource need no boundary; three do](../lessons/two-consumers-of-one-resource-need-no-boundary-three-do.md)
- [An algorithm triggered by exhaustion may not consume the resource it was called about](../lessons/an-algorithm-triggered-by-exhaustion-may-not-consume-the-resource.md)
- [Re-audit a mechanism against the requirement that introduced it](../lessons/re-audit-a-mechanism-against-the-requirement-that-introduced-it.md)
- [Refuse the caller assertion you can neither check nor survive](../lessons/refuse-the-assertion-you-cannot-check-and-cannot-survive.md)
- [Metadata lives as long as the longest-lived thing it describes](../lessons/metadata-lives-as-long-as-the-longest-lived-thing-it-describes.md)
- [Argue correctness as a state-to-state transition at an arbitrary element](../lessons/argue-correctness-as-a-state-transition-at-an-arbitrary-element.md)
- [Store how far you got, not whether you have been](../lessons/store-how-far-you-got-not-whether-you-have-been.md)
- [Enforce a policy by what the tool cannot express](../lessons/enforce-a-policy-by-what-the-tool-cannot-express.md)
- [Simultaneous claims cannot be encoded, so the population is bounded by the width](../lessons/simultaneous-claims-cannot-be-encoded-so-population-is-bounded-by-width.md)
- [The escape must not travel the path it is escaping](../lessons/the-escape-must-not-travel-the-path-it-is-escaping.md)
- [A delimiter drawn from the alphabet buys itself a transformation at both ends](../lessons/a-delimiter-drawn-from-the-alphabet-buys-a-transformation.md)
- [A deadline downstream forbids producing while you send](../lessons/a-deadline-downstream-forbids-producing-while-you-send.md)
- [Reject at the lowest layer that can tell, and give it the one fact it needs](../lessons/reject-at-the-lowest-layer-that-can-tell.md)
- [Break a retry tie with an identifier you already have](../lessons/break-a-retry-tie-with-an-identifier-you-already-have.md)
- [Code that compensates for a defect below will look wrong, and should be labelled rather than beautified](../lessons/code-that-compensates-for-a-lower-layer-will-look-wrong.md)
- [Do not hide a difference in kind behind a uniform interface](../lessons/do-not-hide-a-difference-in-cost-behind-a-uniform-interface.md)
- [When a requirement seems to break the global model, look for the one module that can absorb it](../lessons/absorb-the-violation-in-one-module-rather-than-abandon-the-model.md)
- [Refine a protocol by naming what the current version cannot survive](../lessons/refine-a-protocol-by-naming-what-the-current-version-cannot-survive.md)
- ["Is this for me" and "is this the one I am waiting for" are different questions](../lessons/is-this-for-me-and-is-this-the-one-i-am-waiting-for-are-different-questions.md)
- [Who starts an exchange need not be who paces it](../lessons/who-starts-the-exchange-need-not-be-who-paces-it.md)
- [Derive each timeout from the one beneath it, and stay until the other side can no longer ask](../lessons/derive-each-timeout-from-the-one-beneath-it.md)
- [Join peers through a structure neither of them owns](../lessons/join-peers-through-a-structure-neither-of-them-owns.md)
- [Name which of the reasons to centralize applies, or keep the function where it is](../lessons/name-which-of-the-reasons-to-centralize-applies.md)
- [Write down what the thing is not for; the fixed limits then stop being defects](../lessons/write-down-what-the-thing-is-not-for.md)
- [The adapter to the outside world costs more than the function it adapts](../lessons/the-adapter-to-the-outside-costs-more-than-the-function-it-adapts.md)
- [Apply a mechanism only where its reason holds, and let the system be asymmetric](../lessons/apply-a-mechanism-only-where-its-reason-holds.md)
- [Name the terminal sink, and say where the loss happens](../lessons/name-the-terminal-sink-and-say-where-the-loss-happens.md)
- [Finish every test before the first mutation, and failure needs no undo](../lessons/finish-every-test-before-the-first-mutation.md)
- [Reusing a general store inherits its access model, not only its allocator](../lessons/reusing-a-general-store-inherits-its-access-model.md)
- [Justify a partition by the change it must absorb, and name the change](../lessons/justify-a-partition-by-the-change-it-must-absorb-and-name-the-change.md)
- [Cut a long job where its resource demand changes, and let each piece name its successor](../lessons/cut-a-long-job-where-its-resource-demand-changes.md)
- [Keep what lets you check, not what lets you act](../lessons/keep-what-lets-you-check-not-what-lets-you-act.md)
- [Admission and ownership are two different protections, and only one of them changes the data model](../lessons/admission-and-ownership-are-two-different-protections.md)
- [Price protection against a stated motive, and write the premise down](../lessons/price-protection-against-a-stated-motive.md)
- [Removing the prize beats defending it](../lessons/removing-the-prize-beats-defending-it.md)
- [When a system sits between two things that vary independently, partition by which side each part depends on](../lessons/partition-by-which-side-each-part-depends-on.md)
- [A layer holds when the layer above never names the vocabulary below](../lessons/a-layer-holds-when-the-layer-above-cannot-name-what-is-below.md)
- [Name the exact non-locality that forces a shared structure](../lessons/name-the-non-locality-that-forces-the-shared-structure.md)
- [Tabulate the intended output before writing the thing that produces it](../lessons/tabulate-the-intended-output-before-writing-the-producer.md)
- [Choose the equivalence rule that makes identity a token comparison](../lessons/choose-the-equivalence-rule-that-makes-identity-a-token-comparison.md)
- [An extension mechanism is a bet that the variant set is still open](../lessons/an-extension-mechanism-is-a-bet-that-the-variant-set-is-open.md)
- [A translator's case count is set by the destination's variety, not the source's](../lessons/a-translators-case-count-is-set-by-the-destinations-variety.md)
- [Recoverability after a bad input is a property of the input language](../lessons/recoverability-after-a-bad-input-is-a-property-of-the-input-language.md)
- [An unresolvable reference needs a placeholder and a named expiry moment](../lessons/an-unresolvable-reference-needs-a-placeholder-and-a-named-expiry.md)
- [Enumerate your rule violations and grade them by what they constrain](../lessons/enumerate-your-rule-violations-and-grade-them-by-what-they-constrain.md)
- [Accept the general form, then classify against a closed set](../lessons/accept-the-general-form-then-classify-against-a-closed-set.md)
- [A tag that trails its payload forces the reader to buffer](../lessons/a-tag-that-trails-its-payload-forces-the-reader-to-buffer.md)
- [Inlining dependencies to stop a chain reaction requires a global identity](../lessons/inlining-dependencies-to-stop-a-chain-reaction-requires-global-identity.md)
- [Order a serialized form so the reader never has to back-patch](../lessons/order-a-serialized-form-so-the-reader-never-back-patches.md)
- [Compare the artifact, not the meaning — and check which way the test errs](../lessons/compare-the-artifact-not-the-meaning-and-check-which-way-it-errs.md)
- [Publish the obligation without publishing the name](../lessons/publish-the-obligation-without-publishing-the-name.md)
- [A faster structure that cannot retire the old one is an addition, not a replacement](../lessons/a-faster-structure-that-cannot-retire-the-old-one-is-an-addition.md)
- [Precompute only what you can also precompute the failure of](../lessons/precompute-only-what-you-can-also-precompute-the-failure-of.md)
- [Thread the list of pending holes through the holes themselves](../lessons/thread-the-list-of-pending-holes-through-the-holes.md)
- [Keep the description unmaterialized until a step cannot be absorbed](../lessons/keep-the-description-unmaterialized-until-a-step-cannot-be-absorbed.md)
- [A subsumption rule must be checked once per position, not once](../lessons/a-subsumption-rule-must-be-checked-once-per-position-not-once.md)
- [A name-based rule needs a fallback for whatever has no name](../lessons/a-name-based-rule-needs-a-fallback-for-whatever-has-no-name.md)
- [Make the dispatch table total by giving its gaps the failure action](../lessons/make-the-dispatch-table-total-by-giving-gaps-the-failure-action.md)
- [Put the diagnostic map inside the artifact, in a region the consumer skips](../lessons/put-the-diagnostic-map-in-the-artifact-where-the-consumer-skips-it.md)
- [An encoding's regularity decides whether its producer can be a pipeline](../lessons/an-encodings-regularity-decides-whether-its-producer-is-a-pipeline.md)
- [Either the parties agree on a rate or they acknowledge each unit](../lessons/either-the-parties-agree-on-a-rate-or-they-acknowledge-each-unit.md)
