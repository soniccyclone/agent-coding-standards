---
type: lesson
title: "An abstraction is only as strong as its weakest bypass: leave exactly one path to every value"
figure: ungar
works: [self-the-power-of-simplicity]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# An abstraction is only as strong as its weakest bypass: leave exactly one path to every value

**Lesson:** Most object systems offer two ways to get at a value: ask the object for it, or reach in and read the field. The second path looks harmless — cheaper, more direct, obviously equivalent — and it is what dilutes the whole model. Every later refinement that wants to interpose on a value can only interpose on the asking path, so any code that took the direct route is immune to the refinement. That is the real reason a subtype cannot generally swap a stored field for a computed one, or interpose a check on writes, or arrange for two objects to genuinely share a value: not because those things are hard, but because somewhere a caller was allowed to skip the point where interposition happens. This work's response is to delete the shortcut entirely and make the indirect path the only path, at the very bottom of the language, so that reading state and invoking behavior are literally the same operation.

The lesson generalizes far past language design, because the shape recurs everywhere: a field accessible both through a method and directly, a cache with a read-through API and a back door, a resource reachable both through the handle layer and by raw descriptor. In each case the abstraction's power is not the average of its two paths, it is set by the weakest one, because attackers of your invariants — and refactorings, and instrumentation, and alternate implementations — will find the unguarded route. Uniformity here is not aesthetic preference; it is what makes a substitution safe to perform without auditing every caller first.

There is a second, less obvious payoff. Two access paths do not just weaken invariants, they force a whole apparatus into existence to explain how names resolve on each path. When variables are separate from messages, you need scoping rules; when the ways of holding a name multiply, so do the kinds of scope, until the language has half a dozen categories of variable whose lifetimes and visibilities the programmer must hold in mind simultaneously. Collapsing to a single path lets one existing mechanism — here, the inheritance chain — absorb the job of name resolution that scoping rules were doing. So the programmer who believes this looks at a proliferation of resolution rules as a symptom rather than a necessity, and asks which redundant access path is generating them.

**Source:** [Self: The Power of Simplicity](../works/self-the-power-of-simplicity.md) — the messages-at-the-bottom principle and the section on blending state and behavior, including the worked substitutions (a computed coordinate, a write trap, a coordinate shared between two objects) and the closing argument about how variable access dilutes message passing and multiplies kinds of scope.
