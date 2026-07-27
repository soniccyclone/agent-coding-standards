---
type: lesson
title: "A measure robust enough to mean something is too robust to be decidable"
figure: hartmanis
works: [on-the-computational-complexity-of-algorithms]
axes: [verifiability]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# A measure robust enough to mean something is too robust to be decidable

**Lesson:** Any difficulty measure worth trusting has to ignore finite noise. If patching a handful of special cases into a lookup table could move a problem into an easier category, the categories would be describing the patch rather than the problem, so a usable measure is deliberately blind to differences confined to finitely many inputs. That blindness is exactly what makes membership undecidable. Once the measure cannot see a finite prefix, you can build an object whose behavior after some point depends on whether an arbitrary machine ever halts, and asking which category the object belongs to becomes a way of asking whether that machine halts. The undecidability is not a defect in one particular scheme; it falls out of the insensitivity property itself, and so it will reappear in any classification scheme that has the property.

This is a general shape worth recognizing: the invariances you build into a metric to make it meaningful are the same invariances an adversary uses to smuggle an undecidable question inside it. Coarse-graining buys robustness and pays for it in computability. The trade is not negotiable by cleverness, because the proof does not attack the mechanism of the measure — it attacks the fact that the measure refuses to look at finite detail. So there is no tool that decides, in general, which difficulty class a given program's behavior lives in, and no tool that decides whether one resource budget is genuinely weaker than another.

The practical consequence is that classification is a human argument, not a pipeline stage. A programmer who has absorbed this expects a proof obligation wherever they wanted an oracle: no analyzer will tell you your algorithm's true asymptotic class in general, no checker will confirm that your two cost bounds really differ, and any tool claiming to do so is either working on a restricted syntactic fragment or is quietly answering a different, easier question. The corollary for design is to prefer measures and properties whose robustness you actually need, and to notice when you have chosen a definition so forgiving that nothing can compute against it.

There is also a caution here about the reflex of adding invariance to a specification because invariance sounds like rigor. Every equivalence you declare — these inputs don't count, this difference is immaterial, that constant is noise — enlarges the space of objects the specification can no longer distinguish, and somewhere in that enlarged space sits a construction that makes the specification unanswerable. Deciding what a measure is allowed to be blind to is therefore a load-bearing design decision, not a convenience.

**Source:** [On the Computational Complexity of Algorithms](../works/on-the-computational-complexity-of-algorithms.md) — the result that class membership admits no decision procedure, its corollary that class containment is likewise undecidable, and the closing remark that this consequence follows from the finite-difference-invariance property rather than from anything specific to the authors' definitions.
