---
type: lesson
title: "Which simplifications are legal depends on the question being asked, so shrink the model per query"
figure: sifakis
works: [cesar-1982]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, algorithms-and-complexity]
tags: [lesson]
---
# Which simplifications are legal depends on the question being asked, so shrink the model per query

**Lesson:** Before checking a formula, the model is reduced by transformation rules — but the reduction is not a general-purpose cleanup performed once. It is parameterized by the formula: the rules must preserve the specific property under examination, and any part of the model the formula refers to by name is pinned and left intact. Simplification is thus a per-query operation, and the same system gets a different reduced form for a different question. Trying to compute one canonical minimal model for all questions is either impossible or so conservative that it removes nothing.

The reason this is not merely an optimization is that it inverts the usual dependency. Normally you build a representation, then ask things of it; here the thing being asked determines what the representation is allowed to lose. That gives you far more room, because a property that mentions only a handful of control points does not care about distinctions the rest of the model draws, and those distinctions are precisely where the state count lives. The prerequisite is a stock of transformations each labeled with what it preserves, so that selecting a legal subset for a given query is mechanical rather than a judgment call.

Two supporting habits come from the same passage. Structural facts that fall out of how the model was constructed — here, that each translated process is in exactly one control state at a time, an invariant emitted by the translator rather than discovered by the analyzer — are free algebraic leverage, and a construction should be designed to preserve such facts rather than merely to be correct. And the composition rule that joins processes was chosen to keep those per-process guarantees intact, so that combining components does not destroy what makes each one tractable. Cheap analysis is usually the accumulated result of choices like these made upstream, not a clever algorithm at the end.

**Source:** [Specification and Verification of Concurrent Systems in CESAR](../works/cesar-1982.md) — section 4.2's property-preserving net reduction with the places named by the formula held fixed, section 2.2's safety-preserving composition rule, and the invariants used to simplify the computed predicates in section 4.3.
