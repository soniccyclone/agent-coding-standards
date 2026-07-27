---
type: lesson
title: "Trace every complication in an inherited framework back to the single decision that forces it, then check whether that decision was ever justified"
figure: girard
works: [the-system-f-of-variable-types-fifteen-years-later]
axes: [primitive-count, cognitive-load, verifiability]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Trace every complication in an inherited framework back to the single decision that forces it, then check whether that decision was ever justified

**Lesson:** Established frameworks accumulate machinery whose necessity nobody re-examines, because it arrived with the framework and everyone learned it as part of the package. The productive audit is per-complication and forensic: for each piece of apparatus, find the specific earlier decision that makes it unavoidable, then ask whether that decision was ever argued for. The result is often that a whole class of bookkeeping exists to compensate for one seemingly innocuous choice made for other reasons entirely. In the case examined here, an entire species of extra closure conditions in the received notion of domain traces back to comparing functions pointwise rather than by a finer, structurally motivated ordering. Change the ordering and the closure conditions simply do not arise — not because they were wrong, but because they were repairs to damage that had a single cause.

The audit has to be conducted honestly, which means keeping the cases where the complication turns out to be load-bearing. Here, disjoint sums genuinely resist the simplified framework, and the result is stated as an explicit dilemma with both horns priced: accept a slightly awkward encoding of sums inside the simple framework, or readmit a restricted, characterized class of the more complicated structures. Naming the tradeoff and bounding how much complexity readmission costs is the deliverable — not a triumphant claim that nothing was lost.

The second half of the method is looking for where the complexity naturally bottoms out. Incompatibility between two things arises inherently from forming function spaces; nothing in any construction ever generates an irreducible incompatibility among three. So restrict the framework to structures where pairwise information suffices, and the payoff is immediate and concrete: quantities that were unbounded, and therefore uncomputable in general, acquire a bound of two, and what was undecidable becomes decidable. That is a general pattern worth hunting for. Find the arity, depth, or degree at which your constraints actually saturate — resisting both the reflex to allow the general case "for uniformity" and the reflex to hardcode the specific number without checking — and make it a stated invariant of the framework rather than an accident of the examples you happened to try.

For a programmer the habit is the same one applied to a codebase or a dependency: for every layer of defensive machinery, identify what would have to be true for it to be unnecessary, and check whether the thing that makes it necessary was a deliberate decision or an inherited default. Inherited defaults are where the deletions are.

**Source:** [The System F of Variable Types, Fifteen Years Later](../works/the-system-f-of-variable-types-fifteen-years-later.md) — the appendix comparing the simplified domains against the received ones, which localizes the extra axioms to the choice of ordering and states the sum-type tradeoff explicitly, and the following appendix establishing that incompatibility never exceeds pairs and using that bound to recover decidability.
