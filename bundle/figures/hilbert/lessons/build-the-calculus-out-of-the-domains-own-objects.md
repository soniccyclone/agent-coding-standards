---
type: lesson
title: "Build the calculus out of the domain's own objects, then read your assumptions off its algebraic laws"
figure: hilbert
works: [grundlagen-der-geometrie]
axes: [expressiveness, verifiability, primitive-count]
subdomains: [programming-languages-and-semantics, foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# Build the calculus out of the domain's own objects, then read your assumptions off its algebraic laws

**Lesson:** Rather than importing numbers into geometry from outside, Hilbert defines addition and multiplication on the segments themselves, using nothing but the constructions the axioms already license — laying off segments end to end, and a parallel-line construction against a chosen unit that plays the role of multiplication. The result is an arithmetic whose elements are geometric objects. He then asks, one law at a time, which of the ordinary rules of calculation this arithmetic satisfies, and proves each from the geometry. What emerges is a precise correspondence: the incidence statement he attributes to Pascal turns out to be nothing other than commutativity of this multiplication, and Desargues's statement is what underwrites associativity and distributivity. Two apparently unrelated worlds — configurations of lines, identities of algebra — turn out to be the same facts in different notation.

Once that correspondence is in place, the algebra becomes a measuring instrument for the axioms. Weakening a geometric assumption shows up as a specific identity going missing, and he can trace it exactly: with the Archimedean rule in force, commutativity of multiplication follows from the other laws and so the Pascal configuration is unavoidable; drop that rule and he can exhibit a number system, built from formal series in two parameters that fail to commute, whose corresponding geometry satisfies everything else and refutes the configuration. The chain runs both ways — from a missing geometric axiom to a missing algebraic law, and from a hand-built non-commutative algebra back to a geometry nobody would have thought to look for.

For a programmer this is the payoff of taking algebraic laws seriously rather than treating them as academic decoration. Construct your operations on the domain's own values, then ask which laws they satisfy, and the answers tell you what you may safely do: an associative combine lets you regroup work arbitrarily, a commutative one lets you drop ordering guarantees, and each law that fails marks a freedom you do not have. The deeper move is the same as Hilbert's diagnostic direction: when a law you wanted is absent, do not patch around it — go find which structural assumption its absence corresponds to, because that assumption is the real thing you are missing, and the law was only its visible symptom.

**Source:** [Grundlagen der Geometrie](../works/grundlagen-der-geometrie.md) — the chapters constructing an algebra of segments, first from the Pascal configuration and then from the Desargues configuration, and the later analysis identifying commutativity of segment multiplication with the Pascal configuration and showing what happens when the Archimedean assumption is dropped.
