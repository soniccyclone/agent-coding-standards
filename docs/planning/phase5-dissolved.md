---
type: record
title: Phase 5 Dissolved Candidates
description: The 30 apparent cross-figure contradictions that spotting agents examined and judged NOT to be tensions, each with the mechanism that dissolved it. Written 2026-08-01.
tags: [phase5, tensions, okf]
---

# Phase 5 — Dissolved Candidates

Phase 5's spotting pass examined 51 apparent contradictions across six thematic
slices and judged 21 real. This file records the other 30, because knowing that
an apparent conflict *is not one* is a Phase 5 result and the reasoning is worth
more than the verdict. Several of these are pairs a future reader will notice
again; this is the record of why they were already ruled out.

Agents were required to rule out four specific false-positive classes before
calling anything real, and to name which one applied:

- **Different layers** — the corpus's own McCarthy-to-Russell pattern. The two
  sides govern different levels, so both hold at once.
- **Different scope** — one speaks about a shared kernel, the other about an
  application; one about the common case, the other about the exception.
- **Mere emphasis** — each would accept the other's advice, they differ in what
  they stress. The most common false positive.
- **Same claim, different vocabulary** — two fields' words for one idea.

Two mechanisms turned up that were not on that list and are worth naming:
**same word, two referents** (the two figures use one term for different
artifacts), and **not in the corpus** (the conflict is real in the source texts,
but only one side was ever extracted as a lesson — a Phase 4 gap wearing a
tension's clothes, now tracked as Phase 9 item 1).

---

## `abiteboul-vs-himself-viewpoints-vs-substitution`

**Figures:** abiteboul

- A: `abiteboul/the-computation-class-is-the-object-syntaxes-are-viewpoints`
- B: `abiteboul/equal-expressive-power-is-not-a-licence-to-substitute`


**The apparent conflict.**
Flagged in Section D as intentional. The viewpoints lesson says stop arguing
about representation, prove the correspondence once and move across it freely;
the substitution lesson says equivalence never licenses replacing one notation
with another.


**Why it dissolves.**
Dissolves on reading, and more completely than the flag's own reconciliation
suggests — it is not even a tension held in balance, the two lessons push the
same way. Both conclude: keep every notation, use whichever answers the
current question. The viewpoints lesson's named failure mode is "a team fixes
a single canonical form early, and every question thereafter gets asked in a
form that is awkward for it" — that is an argument *against* elimination,
which is exactly what the substitution lesson forbids. Same claim, two
vocabularies (one framed as a positive about translation, one as a negative
about deletion). The flag's phrasing — equivalence licenses translation but
not elimination — is correct and can be carried over verbatim.

---

## `absorb-weak-primitives-vs-manufacture-the-model-you-want`

**Figures:** lamport, lynch

- A: `lamport/assume-the-least-from-your-primitives`
- B: `lynch/build-the-model-you-wish-you-had-then-pay-for-it-once`


**The apparent conflict.**
The decision: your substrate is weaker than your algorithm wants — where does
the compensation live? Lamport pushes it into the algorithm: the bakery
achieves mutual exclusion while tolerating overlapping read/write returning
garbage and writing only to local memory, and every assumption removed is both
a hardware requirement removed and a shared fate removed. Lynch pushes it into
a layer: name the comfortable model (tidy numbered rounds), solve and prove
the idea there once, and treat every real environment as an obligation to
manufacture that model, discharged by a simulation argument in a swappable
piece — because 'scattering the compensations for those assumptions through
the logic that actually solves your problem produces code where nobody can
tell which lines are the idea and which are the apology to reality.'


**Why it dissolves.**
MERE EMPHASIS. The two worked examples diverge but the stated transferable
advice is the same instruction. Lamport's own qualifier: 'The point is not
that weaker is always better; it is that unexamined strength is unpriced
debt.' Lynch's: 'be deliberate about where an assumption is discharged.' Both
say: make the assumption list a first-class object and price each entry.
Lamport's genuine extra claim — that a manufactured strong primitive still
concentrates failure where a weak-primitive algorithm does not — is a fact
about a particular substrate, not advice that contradicts Lynch's placement
rule. Worth keeping in the corpus as a pair of complementary discharge
strategies, not a tension.

---

## `added-vocabulary-is-not-added-power-vs-no-licence-to-substitute`

**Figures:** church, reynolds, abiteboul

- A: `church/added-vocabulary-is-not-added-power`
- B: `abiteboul/equal-expressive-power-is-not-a-licence-to-substitute`


**The apparent conflict.**
Church: if a feature's laws can be premises and its names parameters without
changing what is expressible or provable, "the feature is notation and belongs
outside the core," and most requests to add a primitive dissolve at that step.
Reynolds: "a construct that can be defined by translation into what you
already have adds no reasoning burden at all." Abiteboul: refuse to conclude
anything about whether to offer the construct from the fact that it is
simulable.


**Why it dissolves.**
They agree, and the agreement is worth recording because it is what isolates
the real Stonebraker tension above. Church says the redundant feature belongs
*outside the core*, not that it should not exist; Reynolds draws the explicit
conclusion — "which is the right reason to admit convenient notation freely
while keeping the set of genuinely primitive constructs small"; Abiteboul's
own recommendation is "keep the small implicit core because it makes the
semantics tractable, and expose the explicit constructs because they make the
programs legible." Three statements of one position. Church and Reynolds are
also in a setting where sugar is genuinely free (a definitional extension of a
formal system costs no implementer anything), which is the scope difference
that lets them sit alongside Stonebraker without contradicting him and leaves
Abiteboul, working in the same shipped-system setting Stonebraker is, as the
only real collision.

---

## `algebra-of-programs-vs-denotational-and-axiomatic-semantics`

**Figures:** backus, hoare, dijkstra, strachey

- A: `backus/choose-combining-operators-for-the-laws-they-obey`
- B: `hoare/let-the-reasoning-rule-be-the-definition-and-the-grade, strachey/give-a-construct-a-meaning-not-another-notation`


**The apparent conflict.**
The Section D flag: Backus's Turing lecture holds that axiomatic and
denotational semantics are the wrong playing field for real programs and names
them. The banked version of the claim is in choose-combining-operators-for-
the-laws-they-obey: the conventional arrangement puts proofs in a separate
logical system that talks about programs from the outside, the translation
between them is the practitioner's burden, and that burden is why proof stays
the specialty of people who study proof; the fix is to select combining
operators for the algebraic identities they participate in so manipulation
happens on the program text itself in the notation the programmer already
writes. Strachey's give-a-construct-a-meaning-not-another-notation appears to
be the direct denial: equivalence is not answerable at the level of the
strings, so each construct must denote a mathematical object existing
independently of any notation.


**Why it dissolves.**
Verified against the banked lessons and it dissolves, by the McCarthy-to-
Russell layer pattern plus one scope difference. On criterion the three
figures are identical, in three vocabularies for one idea: Backus judges an
operator by the laws it obeys and calls one that obeys no useful laws a
liability even when convenient; Strachey (judge-a-semantics-by-the-equalities-
it-lets-you-prove) says the test of a definition of meaning is whether it lets
you show two programs that look nothing alike are the same, and faithfulness
with no algebra attached leaves you with a picture; Hoare (let-the-reasoning-
rule-be-the-definition-and-the-grade) says when a construct's reasoning rule
comes out ugly the correct response is to suspect the feature, and the
constructs that fail are the ones breaking locality, arbitrary transfers,
indirection through stored locations, deferred argument evaluation, which is
Backus's own list. Hoare's choose-between-adequate-models-by-the-laws-you-need
is Backus's criterion applied verbatim. On the residue, where reasoning is
carried out, the two operate at different layers rather than competing: Backus
explicitly says the theoretical apparatus guaranteeing the manipulations are
sound still exists but can be pushed underneath, so that using it requires
knowing a couple of conclusions rather than a field. Strachey's denotation is
that apparatus underneath; Backus is prescribing the working programmer's
surface, Strachey the language definition's foundation. Both hold at once and
Backus says so. The remaining difference is scope of remedy: Hoare grades and
revises individual features (and in a-feature-added-to-serve-a-proof-method-
must-be-re-examined-when-the-method-is-dropped even concedes that a feature
bent to serve an abandoned proof style is dead weight to be removed), whereas
Backus concludes the whole von Neumann model must go (audit-the-machine-model-
a-language-commits-you-to-before-its-features). Feature-level versus model-
level, not incompatible advice on one decision. The flagged conflict is
between Backus's 1977 rhetoric and the title of Hoare's 1969 paper, not
between the two figures' lessons. Note that backus/estimate-the-dynamics-you-
cannot-prove (ship on empirical adequacy while being clear it is not proof) is
the closer thing to a real Backus-versus-Dijkstra collision, but that belongs
with the already-flagged Chaitin-versus-Dijkstra tension outside this slice.

---

## `anticipated-change-as-design-criterion`

**Figures:** parnas, reenskaug, jones

- A: `parnas/cut-along-anticipated-change-not-along-processing-order`
- B: `reenskaug/hooks-for-every-need-refuted-by-its-own-usage-data`


**The apparent conflict.**
Apparent conflict: Parnas makes anticipation the load-bearing design act —
produce the list of decisions likely to move, give each exactly one keeper,
and accept that 'this makes decomposition an act of prediction';
parnas/planning-for-change-is-a-bet-on-your-own-success doubles down, since
programs nobody asks to change are the ones nobody cared about. Reenskaug
answers with measurement rather than principle: a team with twenty person-
years of OO experience built a list-display component with hooks for every
foreseeable requirement, audited four years of real usage, and found both that
many expensive advanced features were never used and that they had still been
forced to write eleven subclasses for requirements that arrived anyway — so
the anticipation failed on its own terms. His conclusion is to stop asking the
unfalsifiable 'what might someone need here?' and start asking 'what have
people actually done with this?' jones/a-change-you-anticipated-is-not-
evidence-your-design-absorbs-change is the same attack from the evidence side:
a design 'decorated with parameters and hooks at all the places its author
could imagine variation... has recorded its author's imagination.'


**Why it dissolves.**
Different currencies — and Parnas draws the distinction himself.
parnas/generality-and-flexibility-are-bought-in-different-currencies separates
generality (run-time machinery carried for variety you may never serve, paid
continuously) from flexibility (cheap alterability, paid once in design
effort), and says the mathematician's reflex to always generalize is exactly
wrong for artifacts that behave like engineered products. Reenskaug's
UltimateListView is a purchase of the first kind; Parnas's decomposition
criterion is a purchase of the second, and boundaries have to go somewhere
regardless, so drawing them at the volatile decisions costs nothing extra.
Reenskaug independently endorses the Parnas criterion elsewhere:
reenskaug/sort-behavior-by-rate-of-change-not-by-the-noun-it-mentions and
reenskaug/allow-coupling-only-toward-what-changes-more-slowly are information
hiding by rate of change, and the DCI lesson's heresy is to keep entities
deliberately unintelligent — i.e. cut the boundary, refuse the capability.
Jones is a different layer again: his is a rule about what counts as evidence,
not about what criterion to design by. Both of Parnas's halves survive it,
since parnas/planning-for-change already concedes foresight is finite, the
structure eventually breaks, and scheduled structural repair must be budgeted.

---

## `bound-eventually-or-keep-it-unknown`

**Figures:** hoare, liskov, lynch, dijkstra

- A: `hoare/replace-eventually-with-a-bound-you-can-observe`
- B: `liskov/never-let-a-timing-guess-be-load-bearing-for-correctness`


**The apparent conflict.**
Reads as a flat contradiction about liveness. Hoare: an unbounded promise 'can
be signed off by everybody and delivered by nobody'; insisting on an event
means asserting an n such that every trace longer than n contains it, and
building a component that keeps score and removes the option to defer once the
count is used up. Liskov (PBFT): the timing assumption 'does not need a bound
anybody knows; it is enough that delay does not grow without limit forever,
coupled with a mechanism that stretches its own patience each time it is
disappointed' — and a stated bound is what makes the assumption implausible in
a real network.


**Why it dissolves.**
DIFFERENT SCOPE — bound what you control, refuse to fake a bound on what you
do not. Hoare's n is a step count on deferral inside a process whose scheduler
is the system's own; his lesson even routes the remainder to Liskov's case
('requirements that cannot be given a bound by anyone are usually revealed to
be someone else's problem'). Liskov's unknown bound is on adversarial network
delay, where a stated number is exactly the 'assumption the underlying model
does not license' that Hoare is warning against. Lynch holds both positions
simultaneously without strain — turn-eventually-into-a-quantity-that-shrinks
computes a hard round count from a contracting potential function, keep-
timing-assumptions-out-of-safety uses the unknown-bound form — which is the
strongest evidence this is a distinction rather than a disagreement. Same for
dijkstra/never-let-correctness-depend-on-timing: his refusal is about clocks
and speed ratios, and a step-count bound is not a clock.

---

## `build-the-invariant-in-vs-loosen-the-invariant`

**Figures:** reynolds

- A: `reynolds/build-the-invariant-into-the-connective`
- B: `reynolds/loosen-the-invariant-to-buy-freedom-of-movement`


**The apparent conflict.**
Read on titles: harden the constraint into the notation versus weaken the
constraint to admit faster implementations.


**Why it dissolves.**
Different objects, not different advice. build-the-invariant does not add
constraint - it relocates a constraint that was already being restated
pairwise in every clause into the meaning of the combining operator, so the
specification says the same thing with a better growth curve. loosen-the-
invariant is about a loop invariant that pinned a quantity the specification
never required, and it explicitly says the specification is unchanged. One
internalizes a required constraint so it cannot be forgotten (the same move as
move-the-side-condition-inside-the-claim); the other deletes an incidental one
that was never required (the same move as leave-the-choice-open-and-demand-
every-resolution-be-correct). Reynolds runs both consistently: state what you
need where the formalism can enforce it, and state nothing you do not need.
The real Reynolds self-conflict is the reasoning-principle one above, not
this.

---

## `collapse-the-duplicate-vs-give-two-semantics-two-names`

**Figures:** stonebraker, chamberlin, codd

- A: `stonebraker/three-features-that-rewrite-the-same-tree-are-one-feature`
- B: `chamberlin/two-semantics-for-one-idea-need-two-names`


**The apparent conflict.**
Stonebraker collapses views, integrity assertions and access control into one
mechanism once he sees all three are conjunction onto a request tree.
Chamberlin refuses to unify value comparison and general comparison behind one
syntax and ships two operator families. Codd, third voice, refines definitions
"until its arbitrary distinctions vanish."


**Why it dissolves.**
Different layers, the McCarthy-to-Russell pattern exactly. Stonebraker
collapses the *implementation mechanism* and is explicit that the three user-
facing features remain three; Chamberlin splits the *surface vocabulary* and
says nothing about whether one evaluator serves both. Each would accept the
other's move at the other's layer. Codd does not adjudicate either way: his
stated test is whether a distinction "tracks anything in the underlying
structure or merely tracks the order in which the ideas were found," and
Chamberlin's distinction tracks something structural and checkable (the
general comparison is not transitive and not closed under negation), so it
passes Codd's test rather than failing it.

---

## `cox-vs-brooks-on-essential-difficulty`

**Figures:** cox, brooks

- A: `brooks/complexity-that-is-the-subject-cannot-be-abstracted-away`
- B: `(no opposing Cox lesson exists in the corpus)`


**The apparent conflict.**
Section D flags that Cox names Brooks explicitly and argues every essential
difficulty on Brooks's list is a surmountable obstacle, adding two Brooks
omitted. Verified against all eight banked Cox lessons: that argument was
never extracted. Nothing in cox/ asserts the essential difficulties are
surmountable. The Cox lessons that touch Brooks's territory either agree with
him or are orthogonal — cox/standardize-the-artifact-not-the-method is the
same claim as brooks/commit-to-the-interface-and-leave-the-mechanism-free, and
cox/reuse-only-appears-at-the-granularity-the-incentives-reach argues a
component marketplace is blocked by economics rather than by technology, which
is not a claim about essence at all. Brooks's side is banked and unopposed.


**Why it dissolves.**
NOT IN THE CORPUS — the conflict is real in the source texts but only one side
was extracted as a lesson. Either close the flag, or send a targeted
extraction pass at Cox's 'What if there's a Silver Bullet' rebuttal of the
essence/accident split before opening a tension file. Do not write a tension
against a lesson that does not exist.

---

## `declarative-request-vs-programmer-as-navigator`

**Figures:** codd, stonebraker, bachman

- A: `stonebraker/state-what-you-want-and-surrender-the-plan`
- B: `bachman/data-as-the-fixed-center`


**The apparent conflict.**
The apparent collision of the 1970s debate: Codd and Stonebraker say a request
must contain no procedure, and treat "any API that forces clients to navigate
step-by-step as both an intent-destroyer and a parallelism-destroyer," while
Bachman's navigator writes "programs as traversals" of the shared structure.


**Why it dissolves.**
Different claims wearing the same historical costume. Bachman's lesson is
about which entity is the fixed frame of reference — durable shared data, not
the executing program — and its actual instruction is "designs the shared data
model first, as a description of the enterprise rather than of any one
application." Codd and Stonebraker agree with every word of that;
stonebraker/design-interfaces-so-data-outlives-the-programs-that-touch-it is
the same claim. The word "traversal" is doing all the apparent work, and it
names Bachman's mental picture of a program's relation to durable state, not a
demand that the request interface be record-at-a-time. The genuine
Codd/Bachman conflict is the structure-shaping one above; this pairing is a
false positive and reporting it would put a fake version of a real
disagreement into the corpus.

---

## `design-notation-unimplemented-vs-must-be-a-readable-program`

**Figures:** hoare

- A: `hoare/keep-the-design-notation-deliberately-unimplemented`
- B: `hoare/whatever-runs-must-be-a-readable-program-in-the-same-language`


**The apparent conflict.**
Read on titles: one says the notation you design in must have no compiler, the
other says whatever runs must be printable as an ordinary program in the same
language you claim to work in.


**Why it dissolves.**
Different layers, the McCarthy-to-Russell pattern almost exactly. keep-the-
design-notation is explicit that there are two languages - design chosen for
expressive fit, implementation chosen for proximity to the machine - and that
refinement is the passage between them. whatever-runs constrains only the
packaging and assembly mechanism of the implementation language: after
linking, the result must be exhibitable as one text in the base language.
Neither claims the design notation must run, and keep-the-design-notation even
welcomes the case where the implementation language is a subset of the design
language, which is the arrangement whatever-runs would want. They agree; the
collision is entirely in the phrase 'the same language' meaning the
implementation language in one and the design language in the other.

---

## `does-a-bad-worst-case-veto-a-design`

**Figures:** knuth, wirth, tarjan

- A: `knuth/a-theoretical-weakness-is-a-hypothesis-about-inputs-measure-before-you-fix-it`
- B: `wirth/worst-case-decides-admissibility-expected-case-decides-choice`


**The apparent conflict.**
Apparent conflict over whether a bad worst-case bound disqualifies a method.
Wirth: 'the worst case answers whether an operation is admissible at all —
whether there exists an input that makes it unacceptably slow'; establish the
bound first as a gate, then choose among survivors on measured expected cost.
Knuth: 'an argument showing a technique is fragile is not a fact about the
technique; it is a fact about the technique on adversarial inputs, and it is
silent about the inputs you have' — sequence soundness, then adversarial
analysis, then measurement, then mitigation only for the survivors; most of
the machinery he built to defend against the theoretical weakness turned out
not to be worth using. Tarjan (a-worst-case-must-be-reachable-and-pay-for-
itself, measure-your-improvement-against-the-inputs-that-actually-occur) sits
with Knuth.


**Why it dissolves.**
Different decisions, and the texts already agree. Knuth's advice governs
whether to build defensive machinery inside a method you have chosen; Wirth's
governs whether to admit a candidate operation at all. More decisively,
Wirth's own lesson makes Knuth's argument for him: worst cases 'are usually
conjunctions', they 'describe a corner of the input space that a realistic
workload may never visit', and once the bound is acceptable you must stop
using it for comparison and measure instead. Wirth's other lesson (improve-
the-dominant-term-or-do-not-call-it-an-improvement) explicitly rules an
asymptotic improvement a deterioration on the workload that actually occurs,
which is Knuth's KMP concession verbatim. Same claim, different vocabulary,
plus a scope difference about which question the bound answers.

---

## `does-a-boundary-discount-hidden-complexity`

**Figures:** thompson, hoare

- A: `thompson/admit-complexity-only-where-it-can-be-quarantined`
- B: `hoare/simplicity-has-counterfeits`


**The apparent conflict.**
Apparent conflict over whether a module boundary lets you buy speed with
complexity. Thompson: if the cleverness can be sealed so 'callers get a plain
description and never need to know how it is achieved', admit it — 'a design
containing three localised complexities is comprehensible; the same amount of
complexity smeared across the interfaces between subsystems is not, even
though the sums are equal.' Hoare names modularity as a counterfeit for
simplicity: 'you only need to know this subset' is true exactly while the
user's work is correct and false the moment it stops being, the diagnostic
arrives in vocabulary the user does not have, and layered on a complex
implementation and runtime the practitioner is overwhelmed by accumulated
incidental complexity.


**Why it dissolves.**
Same claim, different vocabulary. Both make total system comprehensibility the
objective and treat modularity as a means judged by whether the boundary
actually holds. Thompson's containment test is Hoare's caveat stated as an
operational criterion: the leak signature he names — deferred work surfacing
as out-of-order observable state and errors reported far from the decision
that caused them — is precisely Hoare's 'the mistake reaches into the parts
the user never learned'. Thompson even applies it against himself, conceding
what the deferred-write cache broke. Neither adopts modularity as the goal;
neither would admit a complexity whose boundary leaks.

---

## `does-abstraction-hide-cost-or-reveal-it`

**Figures:** jones, wirth, lampson

- A: `jones/the-decisions-that-decide-performance-are-only-visible-with-detail-removed`
- B: `wirth/every-facility-owes-the-user-a-cost-model`


**The apparent conflict.**
Apparent conflict on the slice's headline axis. Jones inverts the usual
framing: abstraction and speed are opponents only for the narrow endgame
activity of squeezing a finished system; the decisions that actually decide
performance are structural, made early, and 'you can only see if you are
looking at something small enough to hold in your head' — a description free
of implementation detail lets you see the whole operation set, ask which are
frequent, and compare candidate representations in a page of thinking. Wirth
demands the opposite-looking thing: 'hiding a mechanism is only legitimate if
using it costs something predictable,' each facility's realization must be
explainable independently and precisely enough to estimate the work a program
will do, and 'making the mechanism visible is a service, not a leak of
implementation.' lampson/an-interface-is-a-small-language-and-its-real-
contract-includes-cost is with Wirth: the written spec is half the contract,
the unwritten half is that an operation costs something proportional to what
it does, and 'break that half and you have broken the interface, even though
every stated guarantee still holds.'


**Why it dissolves.**
Different layers — the McCarthy-to-Russell pattern. Jones is describing the
design activity (where you stand to choose a representation: at the abstract
model, because that is the only vantage point from which the operation profile
is visible). Wirth and Lampson are describing the artifact you publish (what a
caller must be able to estimate from the text). Both are followable
simultaneously and Jones says as much: jones/a-language-cannot-pick-the-
representation-because-it-cannot-see-the-profile concludes that a language
implementing the abstraction directly must either choose naively or infer the
profile, so choosing the representation 'is the programmer's own work...
precisely why it cannot be automated away' — which is Wirth's four-access-
techniques argument reached from the formal-methods side. Wirth's target is
the uniform-looking mechanism with wildly varying realizations, not
abstraction; Jones's target is profile-and-patch as a first move, not cost
transparency.

---

## `escape-hatch-dominated-vs-optimizer-opt-out`

**Figures:** church, chamberlin

- A: `church/a-restriction-plus-an-escape-hatch-is-dominated-by-both-endpoints`
- B: `chamberlin/license-the-optimizer-in-writing-and-provide-an-opt-out`


**The apparent conflict.**
Same decision: a discipline (declarative semantics the optimizer is licensed
to violate; document order) blocks something users need. Church says an
exemption that recovers the blocked capability leaves you strictly dominated
by both endpoints — full cost of the discipline, none of the guarantee.
Chamberlin's whole design move is to ship the discipline *with* the exemption:
a lexically scoped unordered mode, and conditionals whose untaken branches
genuinely do not evaluate.


**Why it dissolves.**
Mere emphasis — and more than that, Church names Chamberlin's design as his
own single approved case. His text: "the only good middle — the exemption is
narrow, its scope is stated in advance, and there is a real argument that the
property survives inside the reduced scope." Chamberlin satisfies all three
explicitly: the license is written down with carve-outs (cardinality checks
stay mandatory), the relaxation is lexically scoped, and the fallout is
enumerated ("positional predicates, position and last, anything that reads an
index into a sequence"). Church's diagnostic — look at where the hatch
actually gets used, and if it is used in the region the discipline was
designed to police, pick an end — is a test Chamberlin's design passes rather
than a verdict against it. Worth banking as a worked example of the approved
middle, not as a tension.

---

## `executable-specification`

**Figures:** cox, jones

- A: `cox/a-specification-is-an-instrument-you-can-run`
- B: `jones/a-specification-you-can-run-stops-being-a-specification`


**The apparent conflict.**
Titles are head-on: Cox says a specification is an instrument you can run
against a candidate; Jones says a specification you can run stops being a
specification. Read fully, they are about two different artifacts wearing one
word. Jones's target is executing the specification itself — interpreting a
model-oriented spec as a very-high-level implementation, at which point 'the
description drifts toward things that run acceptably, then toward things that
run well, and what you have is a slow implementation with a misleading name.'
Cox's gauge is never the implementation and never generates one: it is a
predicate applied from the consumer's side to a finished part made by any
means, and Cox's whole argument is against the derivation-based view — the
same view Jones is defending the spec from. Cox explicitly separates the
measuring tool from the shaping tool ('the gauge is not a fancier lathe'),
which is Jones's separation of the thinking model from the program, drawn from
the other side. Jones's stated argument does not reach Cox's proposal.


**Why it dissolves.**
SAME WORD, TWO REFERENTS — 'runnable specification' means spec-as-
implementation-generator for Jones and spec-as-acceptance-gauge for Cox; they
are not addressing the same artifact. The residual substantive disagreement
(can a decisive-within-tolerance finite procedure be the authoritative
interface contract?) is real, but it is the tolerance-vs-demonstrated-
correctness tension above, and should be resolved there rather than duplicated
here.

---

## `how-much-power-each-part-gets`

**Figures:** kay, reenskaug

- A: `kay/never-divide-a-system-into-things-weaker-than-itself`
- B: `reenskaug/strip-a-component-of-its-own-initiative-to-make-it-composable`


**The apparent conflict.**
Apparent conflict, and the texts contradict each other almost word for word.
Kay: divide a system only into parts that each have the same power as the
whole, never into weaker kinds of stuff, and the protection has to be
universal — 'a part that receives a request should be able to decline it, and
decline it based on who is asking.' Reenskaug: 'the reusable version of a
display element is strictly weaker than the standalone version... demoted from
agent to instrument,' because 'capability, in the sense of self-initiated
action, is precisely what makes a component uncomposable' — convert every
place the component acted on its own judgment into a question it can answer or
a request it can obey, so 'it no longer decides anything.'


**Why it dissolves.**
Same word, two concepts. Kay's 'power' is first-class-ness: whether a thing
can hold state, be sent any message, and protect itself, versus being
consigned to a privileged/unprivileged two-tier scheme where 'the interesting
capabilities keep turning out to be available only to the privileged
category.' His declining-a-request is a protection mechanism (who is asking),
not task policy. Reenskaug's 'weaker' is ownership of task policy — who
decides what the mouse-down means. A Reenskaug view is still a full object
that answers questions, holds state and could protect itself; nothing about it
is a weaker kind of stuff, and the demotion is applied uniformly rather than
creating a privileged category, so Kay's actual prohibition is not violated.
Reenskaug is also recursive in Kay's sense elsewhere: reenskaug/an-entity-at-
one-level-is-a-collaboration-at-the-level-below. The two claims answer
different questions — what kinds of thing exist (Kay) versus where initiative
is homed among things of one kind (Reenskaug).

---

## `may-a-layer-impersonate-the-ideal-component`

**Figures:** hoare, wirth, liskov

- A: `hoare/define-a-masking-layer-by-the-ideal-component-it-imitates`
- B: `wirth/do-not-hide-a-difference-in-cost-behind-a-uniform-interface`


**The apparent conflict.**
Apparent conflict on the classic case, a layer over an unreliable remote
medium. Hoare: specify it as indistinguishability from the perfect component
it pretends to be — 'retry logic is pretending to be a call that does not
fail, a cache is pretending to be the store behind it, a replica set is
pretending to be a single copy' — which is complete by construction, composes
(two buffers in series are a buffer), and grants the implementer maximum
freedom because nothing is said about how. Wirth: an interface presenting
remote and local as the same operation 'is not abstracting over a detail; it
is asserting an equivalence that does not hold,' so name the remote thing
differently, invoke it deliberately, and put it in a layer the base system can
decline to depend on. liskov/hide-the-mechanism-never-the-possibility-of-
failure lands with Wirth — mask packetization, retransmission and location;
never mask ultimate failure or the cost — 'the useful goal is to make the
remote thing easy to use, not to make it a convincing forgery.'


**Why it dissolves.**
Different scope, on the defect catalogue. Hoare's ideal buffer is defined over
defects that are actually maskable given a fair medium (loss, corruption,
reordering, delay — 'possibly after delay'), and his construction is a
specification technique whose whole selling point is that the pretence becomes
'a claim you can lose honestly.' Wirth and Liskov are legislating about the
residue Hoare's technique cannot cover: partial failure, failure after
apparent success, and slowdown large enough that a reasonable algorithm
becomes absurd. On Hoare's own terms an assembly with those properties simply
is not a buffer, and the claim has been lost — which is Wirth's conclusion
reached through Hoare's machinery. Nor is Hoare indifferent to the cost half:
hoare/dont-pre-spend-your-users-efficiency-budget prices abstraction slack
more strictly than Wirth does. The apparent clash is between a spec-writing
technique and an interface-naming rule, and both can be followed at once:
state the ideal you are imitating, and where you cannot be it, say so in the
name.

---

## `monitors-vs-message-passing`

**Figures:** hoare, brinch-hansen, milner, liskov

- A: `hoare/share-purpose-built-resources-not-storage`
- B: `brinch-hansen/put-the-operations-where-the-data-lives`


**The apparent conflict.**
Reads as the canonical CSP-vs-monitors split: Hoare says never share general
storage guarded by a convention, expose a counter whose increment is one
indivisible occurrence, and notes such designs 'run unchanged on distributed
hardware' where shared-store designs cannot. Brinch Hansen says colocate the
data declaration with the complete set of permitted operations in one unit of
text so a compiler can decide, before anything runs, which code may touch
which state.


**Why it dissolves.**
SAME CLAIM, DIFFERENT VOCABULARY. Both say: the unit of sharing is a set of
operations, never a location plus a discipline, because a discipline that
depends on every participant remembering a step fails silently and
unreproducibly. Hoare's 'purpose-built resource whose operations are already
atomic' and Brinch Hansen's monitor are the same object described from the
semantics side and the compiler side; milner/transmit-access-not-the-thing-
itself and liskov/your-representation-choice-sets-the-concurrency-ceiling say
it again in reference-passing and abstract-data-type words. Hoare's
portability remark (shared store is confined to multiprocessors and
timesharing) is an observation about where the pattern can be deployed, not a
contrary instruction. The message-passing/shared-state axis in this slice does
not actually contain a fight.

---

## `naur-vs-dijkstra-on-what-counts-as-justification`

**Figures:** naur, dijkstra

- A: `dijkstra/reason-about-the-program-not-its-runs`
- B: `naur/the-artifact-is-the-theory-not-the-text`


**The apparent conflict.**
Looks head-on: Dijkstra says treat the program as one half of a conjecture and
settle it by manipulation of the text, never by narrating executions; Naur
says 'justification bottoms out in judgment, not in derivation' and that what
you should demand of a design discussion is 'not a chain of derivations from
stated principles, but evidence that the person can situate the program in the
world it serves.' But they answer different questions. Dijkstra's object is
whether the text meets a given specification — a closed formal claim. Naur's
object is why this specification, this boundary, this shape and not another —
and he is explicit that the reasoning which drew the boundary lives outside
the system by construction, so no artifact inside it can contain that
reasoning. Dijkstra himself puts the creative act outside the calculus
(dijkstra/let-the-proof-lead-the-program: choosing the invariant and the
variant 'is genuine creative work; everything after that choice is
systematic'), which is Naur's judgment under another name.


**Why it dissolves.**
DIFFERENT LAYERS, and the corpus already carries the bridge: abrial/proof-
cannot-tell-you-that-you-wanted-this occupies exactly the gap between them,
and jones/a-proof-covers-your-reasoning-not-your-substrate makes the layering
explicit for the failure-class version ('careful reasoning and runtime
checking are not competing approaches to reliability where one makes the other
unnecessary; they cover disjoint failure classes'). Dissolves McCarthy-to-
Russell style.

---

## `principled-first-or-fast-first`

**Figures:** wilkes, lampson, knuth, tarjan

- A: `wilkes/keep-the-principled-layout-as-the-yardstick-for-every-economy`
- B: `tarjan/get-the-bound-first-then-spend-a-separate-revision-buying-simplicity`


**The apparent conflict.**
Apparent conflict over the ordering of a two-stage process. Wilkes: build the
regular, principled version first even though it is extravagant, and treat it
as the reference every economy is measured from — 'starting from an economical
tangle and trying to tidy it afterwards has no such property'. Lampson (build-
the-impractical-complete-model-first) and Knuth (write-the-provable-form-
first-then-transform-it) say the same in different domains: the unaffordable
reference version first, the fast one derived from it by named
transformations. Tarjan says the reverse — 'simplicity is not something you
can usually pursue at the same time as a hard performance target, because you
do not yet know which of your mechanisms are essential'; the first version to
hit the bound is complicated by necessity, and simplification is a separate
scheduled revision afterwards.


**Why it dissolves.**
Different layers, and different objects. Wilkes/Lampson/Knuth's first artifact
is a reference specification — deliberately unaffordable, kept permanently,
never the shipped thing — used to price departures. Tarjan's first artifact is
a shipped implementation in a setting where whether the target is achievable
at all is the open research question; his complicated version is complicated
because the necessary-mechanism question was still open, not because anyone
economized. Tarjan nowhere forbids a clean reference, and Wilkes nowhere
claims the principled version will meet the bound (he says explicitly 'the
principled version does not have to survive to be worth building'). All four
can be followed on one project: write the reference, discover the bound with
whatever machinery it takes, then simplify against the reference. Knuth's case
in particular is a constant-factor transform of an algorithm whose asymptotics
are already settled, which is not the situation Tarjan is describing.

---

## `prohibition-vs-better-construct`

**Figures:** steele, sussman, dijkstra, hoare, wirth

- A: `steele/prohibition-is-not-design-provide-the-better-construct and sussman/invent-better-constructs-instead-of-forbidding-bad-ones`
- B: `hoare/deny-the-syntax-that-would-let-you-write-nonsense, wirth/enforce-a-policy-by-what-the-tool-cannot-express, dijkstra/shorten-the-gap-between-text-and-computation`


**The apparent conflict.**
Apparent decision: a construct is associated with bad code. Do you remove it
from the language, or supply a better-fitting one and let the bad practice
lose on the merits? Steele and Sussman (co-authors, one voice, from Lambda:
The Ultimate Imperative) say prohibition is confused twice over, mechanically
because any language with procedure values, conditionals, lexical scope and
value-free transfer reconstructs the banned construct as a short idiom, and
substantively because disorder comes from a muddled conception of the problem
that no vocabulary restriction repairs. Hoare, Wirth and Dijkstra all appear
to prescribe the opposite: shape the notation so the bad form cannot be
written, enforce policy by what the tool cannot express, and admit a control
feature only if a programmer-independent description of progress survives its
use.


**Why it dissolves.**
This is the slice's headline question and it dissolves, mostly on scope and
partly on emphasis, and the corpus already contains its own resolution. (1)
Different scope on what is forbidden. Hoare's deny-the-syntax targets
degenerate forms with no sensible reading, explicitly "a defect nobody would
write deliberately and everybody writes accidentally", and he notes
prohibitions are cheap to lift once the theory can say what the case means.
Steele/Sussman target constructs people genuinely need. Nobody is telling you
to ban a form that has a use. (2) The prohibition side already carries
Steele/Sussman's failure condition as a precondition. Wirth's enforce-a-policy
lesson spends its last paragraph on it: check that the code which genuinely
needs the capability is the same code the restriction still admits, because
otherwise it is not self-enforcing policy but an obstacle people route around
in ways you will like less than the rule. That is Steele/Sussman's argument,
adopted. Wirth's assembler case passes it because nothing remains to
reconstruct the removed capability, which is exactly where Steele/Sussman's
mechanical objection does not bite. (3) Dijkstra's positive doctrine is
Steele/Sussman's. tortuous-solutions-indict-the-primitives says when a trivial
requirement demands heroic code the productive move is to identify the missing
capability and introduce it as a new primitive, and that a primitive earns its
place by what it makes expressible and cheap rather than by irreducibility,
keeping the richer form even when it is demonstrably encodable in the poorer
one. (4) hoare/enforce-discipline-through-an-interface-nobody-wants-to-bypass
states Steele/Sussman's thesis outright: an enforced but inconvenient
discipline generates a steady demand for an exemption, and the exemption
dismantles the guarantee, so interface quality is structurally load-bearing
for the safety property. Residue worth recording rather than promoting:
wirth/unbreakable-static-typing says a modelling discipline must be judged by
what the language forbids, not by what vocabulary it supplies, which reads as
a direct denial of Steele/Sussman. It is a different good, not the same one.
Wirth is asking whether a guarantee exists, which only unreconstructible
removal can deliver; Steele/Sussman are asking whether clarity of program
organization is produced, which removal cannot deliver. The live version of
that disagreement is captured in static-declaration-vs-late-binding, against
Kay rather than against Steele/Sussman.

---

## `proof-and-the-residual-specification-risk`

**Figures:** brooks, abrial, jones

- A: `brooks/proof-relocates-the-difficulty-into-the-specification`
- B: `abrial/proof-cannot-tell-you-that-you-wanted-this`


**The apparent conflict.**
Section D says Cox's value-rigidity claim 'extends the conflict to Dijkstra
and Abrial.' On the specification-residue question Abrial is not on the other
side of Brooks — he is on Brooks's side and states it more harshly. Brooks: a
proof 'establishes a relation between two descriptions, and it says nothing
about whether the second description is the one you wanted.' Abrial:
'discharging every obligation establishes that a model is coherent with
itself. It says nothing whatever about whether the model describes the system
anybody wanted... No amount of additional proof closes that gap.' Jones says
the same thing a third time (jones/spend-the-dividend-of-rigour-on-safety-not-
ambition: 'nothing can be proved about the fit between a description and a
need'). Where they differ is only what follows: Brooks concludes formal
methods pay best on small sharply bounded kernels inside a system whose
requirements are still being discovered; Abrial concludes you build a signed,
doubly-classified requirements document plus an independent inspection team
plus model animation, all deliberately outside the proof loop.


**Why it dissolves.**
AGREEMENT, not conflict — three figures state the identical claim in three
vocabularies, and the difference is what each does about it, which is emphasis
plus scope. Worth recording because it corrects the Section D flag: Abrial is
not a target of Cox's charge on this point. Cox's charge lands on Abrial only
at the acceptance-standard level, which is the tolerance-vs-demonstrated-
correctness candidate.

---

## `reproducibility-vs-nondeterminacy`

**Figures:** brinch-hansen, dijkstra, hoare

- A: `brinch-hansen/design-for-reproducibility-because-testing-cannot-reach`
- B: `dijkstra/nondeterminacy-strips-the-incidental`


**The apparent conflict.**
Reads as: Brinch Hansen reorders the entire design of a concurrent system
around the guarantee that timing cannot change the result, 'justifying real
sacrifices in language power'; Dijkstra says forced choices are noise, a
program whose final state is any member of a characterized acceptable set is
fully specified, and insisting on one particular member 'costs simplicity
while buying nothing the specification asked for.' Hoare adds a third position
— hoare/guaranteed-determinism-costs-you-arrival-order-and-bounded-storage
prices total determinism at unbounded buffering plus the inexpressibility of
any arrival-order-dependent behaviour, and says inexpressibility is a wall.


**Why it dissolves.**
DIFFERENT SCOPE, twice over. (1) Dijkstra himself supplies the reconciliation
inside his own lesson: 'distinguish unpredictability you suffer from freedom
you grant.' Brinch Hansen's target is the suffered kind — a file copy with one
right answer that the interleaving can silently corrupt; Dijkstra's is the
granted kind — a tiebreak the specification never asked for. Neither would
accept the other's case as their own. (2) Against Hoare the scope gap is
explicit in the texts: Hoare is pricing total functional determinism whose
defining flaw is that there is 'no escape hatch,' while Brinch Hansen's
reproducibility deliberately leaves 'a small, explicit set of places where
timing matters at all.' Brinch Hansen keeps exactly the hatch whose absence is
Hoare's third complaint.

---

## `restrict-the-language-to-get-the-guarantee`

**Figures:** abiteboul, codd, ullman, scott, church

- A: `abiteboul/restrict-the-language-until-the-guarantee-is-a-theorem`
- B: `codd/bind-programs-to-information-not-arrangement`


**The apparent conflict.**
Flagged in Section D as "likely overlap rather than conflict" against Codd,
Dijkstra and Hoare. Verified: overlap.


**Why it dissolves.**
Same claim, different vocabulary, and it is a cluster rather than a pair.
Abiteboul: forbid retraction and polynomial termination follows from counting;
forbid negation and containment stays decidable so a complete optimizer can
exist. Codd: make representational questions unaskable — "if a client cannot
express 'the next record' or 'follow this chain,' it cannot come to depend on
adjacency or chains" — which is the same move, buying a change-survivability
guarantee by deleting a construct. ullman/a-capability-you-must-not-use-is-
not-a-capability supplies the converse and states it outright: "Restrictions
are what let a system make promises about things it has not seen yet...
Removing the restriction removes the promise." scott/pick-the-structure-whose-
weakness-buys-the-guarantee-you-need gives the mathematical form ("find the
single operation whose existence would refute the property you want, and then
choose your notion of well-behavedness precisely so that operation falls
outside it"). No figure in the slice argues against restriction as such.
scott/test-whether-a-restriction-is-mathematics-or-inherited-caution and
church/a-restriction-you-can-restate-around-is-not-a-restriction are audits
*of* restrictions, not opposition to them — they refine the cluster rather
than contest it. The flag should be struck as verified overlap.

---

## `runnable-meaning-vs-machine-independent-meaning`

**Figures:** landin, kay

- A: `landin/a-meaning-that-needs-a-machine-cannot-judge-machines`
- B: `kay/anything-worth-stating-precisely-must-be-runnable`


**The apparent conflict.**
Landin: where meaning is fixed independently of any evaluator, an evaluator is
a candidate to be assessed and can be wrong; where the only way to say what a
program means is to describe an apparatus running it, meaning and mechanism
have collapsed, the reference implementation is the specification, its
accidents become law and second implementations become archaeology of the
first. Kay: the description should simply be made to run, and at that point
there is no reason for it to be a separate artifact from the program, it is
the program. Read quickly, Kay is prescribing exactly the collapse Landin
warns is a loss.


**Why it dissolves.**
Different axes mistaken for one, and once separated the two are orthogonal
rather than opposed. Landin's variable is whether the account of meaning is
evaluator-independent; Kay's is whether the artifact carrying the account is
executable. A notation can be both, which is what Kay's own construction
claims to be, and Kay's other lesson (make-the-explanation-be-the-program) is
about raising the notation to the domain's own picture, not about lowering
meaning to whatever the machine does. Landin's target is a feature whose
meaning can only be given by describing state, aliasing and order of touching,
which is what makes the account machine-shaped; that has nothing to do with
whether the account compiles. Kay's target is the unchecked second artifact.
Neither prescription forces the other's failure. Worth recording because the
collision is tempting on the titles, and because it is the counterexample that
keeps executable-design-notation honest: Hoare's objection to executable
design notation is about a cost model pruning the design vocabulary, which is
a different and live objection, not this one.

---

## `scheduling-as-meaning-vs-tuning-that-carries-no-meaning`

**Figures:** abiteboul, chamberlin

- A: `abiteboul/how-you-schedule-the-rules-is-part-of-what-they-mean`
- B: `chamberlin/give-tuning-its-own-channel-that-carries-no-meaning`


**The apparent conflict.**
Abiteboul: whether the runtime fires one applicable rule instance or all of
them changes which stable state you reach, so "write the scheduling discipline
into the specification rather than leaving it to the runtime." Chamberlin: a
tuning surface must be designed "so that removing the tuning changes only
timing, never results," and "any tunable whose removal changes an answer" is
"a modeling mistake rather than a knob."


**Why it dissolves.**
Same claim, different vocabulary. Chamberlin's rule is a sorting rule:
anything that changes answers belongs in the meaning-carrying channel, not the
tuning channel. Abiteboul finds that scheduling changes answers and concludes
it belongs in the specification. That is Chamberlin's rule applied, not
contradicted — Chamberlin's own phrase for the case is "a modeling mistake
rather than a knob," i.e. move it into the model, which is what Abiteboul
does. There is also a clean scope split underneath: Abiteboul explicitly
conditions the whole result on rules "with any negative condition" and points
at negative dependencies as where the two disciplines diverge; Chamberlin,
Codd and Stonebraker are working in a language deliberately restricted so that
no such dependency exists, which is abiteboul/restrict-the-language-until-the-
guarantee-is-a-theorem doing its job.

---

## `whole-value-notation-vs-the-overhead-budget`

**Figures:** backus

- A: `backus/operate-on-whole-values-and-name-nothing`
- B: `backus/abstraction-is-rented-against-the-overhead-the-hardware-hides`


**The apparent conflict.**
Read as the FORTRAN-versus-Turing-lecture split: reach first for a statement
over whole values and treat every index and accumulator as a concession,
versus an abstraction lives inside whatever overhead budget the current
machine still hides, and expressive power without an execution cost near the
incumbent's does not spread.


**Why it dissolves.**
Mere emphasis, and already reconciled inside the corpus, so it is not even a
worked example that needs a tension file. abstraction-is-rented does not tell
you to avoid whole-value notation; it tells you that proposing it is half a
project and that the mapping down to mechanism is the expensive half - which
is a diagnosis of why the FP paper's program stayed in papers, not a
retraction of it. operate-on-whole-values makes no cost claim to contradict.
One lesson supplies the constraint the other omits; you can follow both by
adopting the notation and owning the translator, which is precisely what
abstraction-is-rented says the FORTRAN group did.

---

## `witness-outranks-proof`

**Figures:** mcmillan, dijkstra, sifakis

- A: `mcmillan/a-witness-outranks-a-proof`
- B: `dijkstra/correctness-comes-from-structure-not-testing`


**The apparent conflict.**
Reads as: McMillan says a counterexample may be worth more than a proof of
correctness and tells you to 'distrust green results in proportion to how much
modelling stands between your artefact and the thing being checked,' since a
positive result is conditional on the abstraction being faithful, the
requirement being right, and the requirement set being complete. Dijkstra says
confidence can come only from structure carrying the argument, and that no
black box can be convincingly validated.


**Why it dissolves.**
DIFFERENT LAYERS plus emphasis. McMillan is ranking two outputs of a
verification tool (reproducer vs verdict) and making an epistemic point about
what a green result is conditional on; Dijkstra is ranking two sources of
confidence in an artifact (its construction vs sampling its behaviour). They
agree on the thing that would make it a fight: McMillan's own argument is that
sampling is 'structurally the wrong kind of tool' for failures needing long
coordinated sequences, which is Dijkstra's no-continuity argument arriving
from the complexity side. McMillan never says skip the proof; Dijkstra never
says trust a verdict. Their shared enemy is random simulation.

---

## `worst-case-failure-as-a-legitimate-trade`

**Figures:** lampson, wirth

- A: `lampson/normal-and-worst-case-are-two-different-design-problems`
- B: `wirth/worst-case-decides-admissibility-expected-case-decides-choice`


**The apparent conflict.**
Apparent conflict: Lampson's 'heresy' says a system may be allowed to fail
outright in the worst case — 'deadlocking, starving a client, or restarting
from scratch are all acceptable outcomes if the alternative is carrying
prevention machinery through every ordinary operation' — because the recovery
path is a sunk cost created by hardware faults and bugs anyway, so permitting
a few more entries into it buys real speed for free. Wirth's gate says the
worst case decides admissibility, and names 'an unlucky order of events' as
exactly the exposure the gate protects against, which is Lampson's rare
deadlock.


**Why it dissolves.**
Different scope. Wirth's gate is about a pure operation that stays correct and
only gets slow — an AVL deletion whose rebalancing cost is bounded by a growth
rate — where 'inadmissible' means the cost bound exceeds what you can accept.
Lampson's heresy is about a multiplexed shared resource in a system that
already carries a mechanically-triggered recovery path as a sunk cost, and his
precondition set (failure detected mechanically, rare, recovery already
exists, prevention machinery would tax every ordinary operation) has no
analogue in Wirth's setting; Wirth never addresses a case where the failure
path is pre-paid. Conversely Lampson would not defend a quadratic inner loop
as 'rare failure'. The collision exists only at the level of the slogan.

---
