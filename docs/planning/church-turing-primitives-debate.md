---
type: discussion-log
title: Church vs Turing — Primitives Debate (Source Discussion)
description: Full back-and-forth that produced reasoning-primer.md. Use this to understand the objections already raised and answered before re-litigating them.
tags: [church-turing, primitives, occam, epistemology]
---

> **FROZEN as of 2026-07-23.** Already a historical transcript by design; note
> added for consistency with the other three original docs. Live planning is
> in [technical-plan.md](technical-plan.md) and [ledger.md](ledger.md).

# Source Debate for the Reasoning Primer

This is the actual argument that produced `reasoning-primer.md`. If you (the
agent) are about to push back on the primer's Church-over-Turing default,
read this first — several obvious objections were already raised and worked
through below.

## The core claim
Lambda calculus and Turing machines are proven computationally equivalent
(Kleene 1936, Turing 1936–37 appendix): same class of computable functions.
This is a real, checkable syntactic proof (mutual simulation — TM transitions
encode as beta-reductions and vice versa) — not in dispute.

## What's actually in dispute
Equivalence of *computability class* (what's computable at all — the
extension) is not equivalence of *structure* (how many irreducible primitives
each formalism needs to get there). The primer's author holds that:

- Lambda calculus needs two primitives: abstraction, application. Numerals,
  booleans, recursion, etc. all derive from these two via encoding.
- Turing machines need four-plus: tape, head, state register, transition
  function — and the transition table itself grows unboundedly per problem,
  which arguably isn't a fixed primitive count at all.
- Fewer irreducible primitives = closer to the "true" minimal representation
  of computation, *if* you hold that mathematical structures are discovered
  rather than invented (platonism) — the position the primer's author holds
  on independent (theological, but also independently defensible — see
  Gödel, Hardy, Penrose) grounds.

## Objections already raised, and how they were resolved

**"Isn't this like geocentrism vs heliocentrism — models get equally far?"**
No, and this cuts a specific way. Geocentric and heliocentric were *not*
equally capable: Ptolemaic epicycles needed continual ad hoc patching to
match observation; Keplerian ellipses collapsed that apparatus into one law
*and* predicted positions Ptolemy's model couldn't. That's measurable
predictive superiority, not aesthetic preference. The parallel that *does*
hold: primitive-count reduction (epicycles → ellipse) is the same move as
primitive-count reduction (four-plus TM primitives → two lambda-calculus
primitives), under an Occam's-razor / discovery framing.

**"Isn't 'computing is computation' just asserting your conclusion?"**
Yes — flagged as the actual weak point in the argument. Church's formalism
(function evaluation) and Turing's (state transition over time) are proven
extensionally equivalent; neither is definitionally "what computing really
is" without first stipulating a definition. The strongest version of the
Turing-first counter-argument: physical Church-Turing thesis / Landauer —
computation is physically realized as state transitions in matter, so
mechanism could be argued ontologically prior to any calculus describing it.
This is a live counter-argument, not fully defeated here, and is exactly the
kind of thing worth re-raising.

**"Isn't Turing's model 'state-dense' in its own favor?"**
Rejected as a non sequitur once state is understood as data: mutation is just
address-indexed data update, no ontological difference from substitution —
so "state density" isn't a separate, coequal axis to composition density.
Conceded by both parties.

**"Doesn't complexity theory (P vs NP, lower bounds) live in the gap between
these formalisms?"**
Yes, explicitly acknowledged: the equivalence proof only guarantees identical
*computability*, not identical cost/structure/expressiveness under any
resource bound (time, space, code size, human cognition). This gap is where
legitimate structural comparison — including a "which has fewer primitives"
argument — actually has to be made, rather than resting on the equivalence
proof alone.

**"Why does corpus-frequent (imperative/Turing-style) code dominate if it's
not more primitive-minimal?"**
Historical/contingent, not epistemic: 1950s hardware (sequential mutation)
was cheap, substitution/reduction was expensive, so the industry — and
therefore the training corpus — ossified around Turing-style mechanism. LLMs
trained on that corpus reproduce frequency as if it were correctness. This is
the actual motivating problem for the whole project: an agent should rank
constructs by primitive-count under a stated axis, not by how common they are
on GitHub.

## What the primer asks the agent to do differently
Per `reasoning-primer.md` §§1–2: before ranking any two abstractions, name the
optimization axis (expressiveness / verifiability / parallelizability /
hardware-affinity / cognitive load / primitive-count) rather than asserting
one is categorically "more correct." Church-over-Turing is the *default*
under the primitive-count axis specifically — not a blanket claim that lambda
calculus wins on every axis. If you're pushing back that primitives aren't
"necessarily simpler," the sharpest form of that objection is: contest the
primitive *count* itself (e.g., argue TM's transition function is one
primitive, not several, or that lambda's encodings for numerals/booleans
smuggle in hidden complexity Church calculus doesn't get credit for) — that's
a real fight worth having, rather than reopening the extension/structure
conflation already addressed above.