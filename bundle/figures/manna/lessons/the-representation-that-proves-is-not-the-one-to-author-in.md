---
type: lesson
title: "The representation that makes the metatheory tractable is not the one people should write in"
figure: manna
works: [completing-the-temporal-picture]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# The representation that makes the metatheory tractable is not the one people should write in

**Lesson:** To prove their proof system complete, Manna and Pnueli first take the interesting feature out. Every reference to the past inside a specification is replaced by a fresh boolean variable, and the program is instrumented with update logic that keeps each variable's value equal to the truth of the historical claim it stands for. What remains is a specification with no history in it at all, over a slightly larger program — and completeness in that impoverished setting is easier to establish. Proofs are then mechanically lifted back into the original language, premise by premise. The reduction is a scaffold for the argument, not a change to the system.

Then they say the thing that makes this a lesson rather than a technique: do not actually work that way. An invariant stating that reaching one value must have been preceded by another is, in their judgment, plainly better than the encoded version — a claim about an anonymous boolean flag, carrying alongside it an unwritten understanding of what that flag is supposed to track. Both are the same property. One states its meaning; the other outsources the meaning to whoever remembers the encoding. That undocumented correspondence is exactly the kind of coupling that survives review and then rots.

The general principle: a system usually needs two representations of the same content, chosen against different criteria. The internal one is picked to make analysis, proofs, and mechanical checking tractable — small, uniform, free of derived constructs. The authored one is picked so that a reader can recover intent without external knowledge. Collapsing them is the failure mode in both directions. Force people to author in the analysis representation and every artifact acquires a tacit decoding ring; make the analyzer swallow the full surface language and its metatheory becomes intractable. The connective tissue is the translation, and its quality is measured by whether results proven downstream can be carried back up and stated in the language the author used.

This is a normal, recurring shape and not an exotic one: desugaring to a core calculus, lowering to an intermediate representation, normalizing a query, flattening a schema for storage. What Manna and Pnueli add is the discipline of keeping the direction of travel explicit and refusing to let the core language leak upward into how humans state their intent, even when the encoding is only one variable and a comment away.

**Source:** [Completing the Temporal Picture](../works/completing-the-temporal-picture.md) — the past-elimination construction and the proof-transformation sections that use it, followed by the closing remark that this encoding is deliberately not recommended as a way to verify real programs.
