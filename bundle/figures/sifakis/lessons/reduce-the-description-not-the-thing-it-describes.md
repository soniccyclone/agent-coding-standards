---
type: lesson
title: "Derive the reduced model by rewriting the description, never by walking the thing described"
figure: sifakis
works: [property-preserving-abstractions-1995]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics, algorithms-and-complexity]
tags: [lesson]
---
# Derive the reduced model by rewriting the description, never by walking the thing described

**Lesson:** A definition of abstraction stated over sets of states reads as an instruction to enumerate: visit every concrete state, find its group, record which groups it can reach. Followed literally, the construction of the simplified model costs at least what analyzing the original would have cost, which defeats the purpose entirely and quietly rules out any system with an unbounded state count. The way out is to notice that you never actually possess the state set — you possess a finite text describing it. Represent transitions as predicates relating unprimed and primed program variables, represent the collapsing map as a predicate relating concrete variables to abstract ones, and the abstract transition relation drops out as a formula built by substitution and quantification over the concrete variables. The whole derivation is symbol pushing on an object whose size is set by the program's syntax and is entirely independent of how many states that syntax denotes.

Two consequences follow that are not available to the enumerative reading. First, systems with infinite or merely astronomical state spaces become abstractable, because nothing in the procedure ever needed the space to be finite — only the description did. Second, the abstraction step becomes composable with the rest of a symbolic toolchain: the output is a formula in the same language as the input, so it can be fed to the same simplifier, the same checker, the same optimizer. An abstraction procedure that produced an explicit graph would sit outside that pipeline and force a conversion at each boundary.

The general instruction is to look for the finite artifact that stands behind the infinite one, and to phrase your transformation as an operation on it. Anywhere you find yourself defining an operation over a collection whose size you do not control, ask what generates that collection and whether the operation can be expressed as a rewriting of the generator. The honest caveat from the same work: the mapping itself — which distinctions to keep — still had to be chosen by a person on the strength of understanding the program, and mechanizing the derivation does not mechanize that choice. Automating the expensive mechanical step while leaving one deliberate human decision is a good trade, and it is worth being explicit about which step is which rather than letting a mostly-automatic method be described as automatic.

**Source:** [Property Preserving Abstractions for the Verification of Concurrent Systems](../works/property-preserving-abstractions-1995.md) — section 4.2's symbolic computation of the abstract system from predicates over program variables, the readers-writers derivation in section 5, and section 10's report of applying the same method to an infinite-state distributed cache protocol by substituting abstract operations for concrete ones in the program text.
