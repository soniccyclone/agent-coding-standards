---
type: lesson
title: "A transformation that preserves the property you are asking about cannot answer the question"
figure: valiant
works: [np-is-as-easy-as-detecting-unique-solutions]
axes: [verifiability, expressiveness]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# A transformation that preserves the property you are asking about cannot answer the question

**Lesson:** Whenever a field settles on a standard way of translating one problem into another, the translation acquires invariants that nobody chose deliberately — they came along because they were convenient or because the first few constructions happened to have them. Those invariants are invisible until you ask a question about exactly one of them, at which point the whole toolkit goes blind: every translation you know how to build carries the property across unchanged, so no translation can ever distinguish instances by it. The correct diagnosis is not that the question is hard but that the tools are the wrong shape, and the fix is to deliberately build a translation that breaks the invariant while keeping whatever else you need.

Recognizing this requires separating what a transformation is *for* from what it happens to preserve. A reduction between decision problems exists to move the yes/no answer faithfully; that it also carries the exact number of witnesses across is an accident of construction — a useful accident when you want to transfer counting results, a fatal one when the question you are asking is whether having many witnesses is what makes the problem hard. Once that is clear the requirement can be stated backwards, as a property the new construction must *not* have, and the design problem becomes tractable: keep unsatisfiable instances unsatisfiable, but reshape satisfiable ones so their witness count is driven somewhere you choose.

The general habit is to catalogue what your standard machinery leaves fixed, and to treat each fixed quantity as a question that machinery is constitutionally unable to answer. This applies well beyond reductions. A refactoring discipline that preserves observable behavior cannot tell you anything about behavior; a benchmark harness that normalizes away input distribution cannot tell you about distributional effects; a type system that erases at runtime cannot be interrogated at runtime. When a question keeps resisting, check whether every instrument you are pointing at it was built to hold the answer constant.

**Source:** [NP Is as Easy as Detecting Unique Solutions](../works/np-is-as-easy-as-detecting-unique-solutions.md) — the introduction's observation that the known reductions among complete problems preserve solution counts, and the explicit statement in section 2 that solution-count preservation is precisely the property the new reduction must lack, which motivates replacing the deterministic construction with a randomized one.
