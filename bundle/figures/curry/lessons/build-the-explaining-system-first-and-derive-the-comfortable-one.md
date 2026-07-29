---
type: lesson
title: "Build the system that explains before the system that feels natural, then derive the second from the first"
figure: curry
works: [a-theory-of-formal-deducibility]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [foundations-of-computation, software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Build the system that explains before the system that feels natural, then derive the second from the first

Curry ends the book by taking apart the word "natural," and the distinction he
draws is worth more than most architecture advice. A thing can be natural in the
sense of matching the essential character of its subject, or natural in the sense
of matching what people do instinctively. He notes that a logarithm to base *e*
is natural in the first sense and emphatically not in the second, then delivers
the punchline about his own work: the system everyone calls natural — the one
that reasons from suppositions and discharges them, the one that mirrors how
humans actually argue — is natural only instinctively. The system that is natural
to the *subject* is the other one, the awkward-looking apparatus with sequences
on both sides of a turnstile. He built the awkward one first on purpose, and
derived the comfortable one from it.

This ordering is not aesthetics. It is where justification comes from. The
comfortable system's rules are convenient manipulations; nothing in them says why
those manipulations are the right ones, and if you had started there you would
have had no way to answer a challenge to any particular rule. The explanatory
system's rules come from stated conditions of use, so each one is answerable, and
once you derive the comfortable rules from them, the comfortable system inherits
a justification it could never have generated for itself. Curry pays real money
for this — he describes the derivation as long and tedious, and mentions in the
preface that an earlier draft had gone the other way, starting from the intuitive
system and reaching for the explanatory one only as an instrument. He scrapped
it and recast the whole structure, on the judgment that a fresh start from the
deeper foundation would be cheaper in the long run than bridging to it.

The practical version: the ergonomic surface and the explanatory core are two
different artifacts, and which one you build first determines whether your
system has an account of itself. Build the core first — the minimal set of
operations whose correctness you can argue directly — then define the pleasant
API as a derived layer, with the derivation itself as the correctness argument.
Do it in the other order and you get a pleasant API resting on nothing, whose
rules can only be defended by appeal to how familiar they feel, and whose
edge-case behavior is whatever the implementation happened to do. This is the
real content of "don't design the DSL before the semantics," and the reason
Curry's ordering matters is that the comfortable layer stays comfortable — he
does not ask anyone to reason in the awkward system. It exists so the pleasant
one can be trusted.

There is a second, sharper reading available. Curry notes that two formalizations
of the same content can be provably equivalent and still differ entirely in
which habits of thought they break: one keeps the original notation and stays
close to the intended interpretation, the other forces a wholly new symbolism
and thereby dismantles ingrained bad reflexes. He says the reader should
understand both. Equivalence in content is not interchangeability in use, so
when two representations are demonstrably the same, the choice between them is a
choice about the humans, and the right answer is sometimes the harder notation
precisely because it refuses to let you coast on old habits.

**Source:** [A Theory of Formal Deducibility](../works/a-theory-of-formal-deducibility.md) — the concluding remarks of the chapter on the finite positive connectives, which distinguish the two senses of "natural" and argue the sequent system is the one natural to the subject, together with the section deriving the supposition-based system's rules from it, the preface's account of abandoning the reverse ordering, and the discussion in the opening chapter of two equivalent routes to formalization differing only in cognitive effect.
