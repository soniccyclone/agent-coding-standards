---
type: lesson
title: "Hoist what recurs everywhere into a convention, and name every exemption"
figure: milner
works: [the-definition-of-standard-ml]
axes: [cognitive-load, verifiability, primitive-count]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Hoist what recurs everywhere into a convention, and name every exemption

**Lesson:** Two mechanisms in a language with mutable state and exceptions touch nearly every construct: the store has to be threaded through evaluation in order, and a raised exception has to abandon the current computation and propagate outward. Written out honestly, both appear in every rule, and the number of rules roughly doubles for the second one alone. The choice made here is to write neither. Instead, rules are stated in a stripped form and two conventions are declared once, at the meta level, saying how to expand them: premises are understood as threading state left to right, and for each premise that could yield an exception, an extra rule is understood to exist that discards the rest and propagates. The rules on the page are the interesting content; the plumbing is a stated rewriting applied uniformly.

The reason this improves reliability rather than merely shortening the document is that repetitive text is exactly where inconsistency hides. If the store is threaded by hand in ninety rules, one of them threads it wrong, and nothing about the local text looks unusual. Stated as a convention, the ordering is asserted once and holds everywhere by construction — and it yields a free theorem worth having: a rule with no premises causes no side effect, readable straight off the page. The same device compresses variant forms of a construct into one rule with optional fragments, under a stipulation that the optional parts are all present or all absent, which prevents the combinatorial family of near-duplicate rules a naive presentation would need.

What makes the technique trustworthy is the discipline about exceptions to it. Exactly one rule must not receive the propagation treatment — the one for handling an exception, since a handler is the only thing that can stop propagation — and that exemption is called out in a footnote at the point where the convention is stated, not left to be discovered by a reader who wonders why the expansion produces nonsense. A blanket rule with a hidden exception is worse than no rule; a blanket rule with its exceptions enumerated where the rule is declared is the strongest form of the technique.

Any codebase with a cross-cutting obligation faces this choice — transaction propagation, cancellation, tracing context, error wrapping. Threading it manually through every function is auditable but wrong somewhere; hoisting it into a single mechanism is correct by construction but obscures the places that must opt out. The resolution is to hoist, and then to make the opt-out list explicit, short, and adjacent to the mechanism's own definition.

**Source:** [The Definition of Standard ML (Revised)](../works/the-definition-of-standard-ml.md) — the opening of the Core dynamic semantics section, which states the state convention, the exception convention with its single footnoted exemption for handlers, and the convention on optional phrase fragments used throughout both static and dynamic rules.
