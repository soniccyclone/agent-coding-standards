---
type: lesson
title: "Take the weakest notion of time the property needs, and know what forced you to need any"
figure: pnueli
works: [the-temporal-logic-of-programs]
axes: [primitive-count, cognitive-load, expressiveness]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---

# Take the weakest notion of time the property needs, and know what forced you to need any

**Lesson:** Faced with reasoning about when things happen, the obvious solution is to give yourself a clock: attach an explicit time value to every event, quantify over those values, and any temporal relationship whatsoever becomes expressible. This works and is a mistake. A formalism that can say anything about time tells you nothing about which features of time your argument actually leaned on, and it drags the full apparatus of arithmetic into proofs that never needed to compare two instants. The alternative is to grade properties by how much temporal structure they require — how many distinct moments must be related to state the property at all — and then deliberately adopt only the machinery that grade demands. Properties about a single moment universally quantified are invariants, and need no notion of time beyond "always". Properties relating two moments in order are eventualities, and need only "sometime after". Fairness between competing requesters needs four moments and is genuinely harder to state; quantitative deadlines are a different question again.

Deliberately capping expressive power is the discipline here, and it pays twice. Once, in proof: a weak logic has few axioms, so each step of an argument is forced and checkable, and the whole system can be shown decidable — an unrestricted clock buys you no such thing. Once, in understanding: when your vocabulary can only say "always" and "eventually", the fact that a specification is expressible tells you something true about the specification, and the fact that one is not tells you the property is more delicate than it looked.

The companion habit is to ask what made temporal reasoning necessary in the first place, rather than importing it reflexively. A deterministic sequential program carries its own clock: the program counter plus the loop counters locate you in the execution exactly, so "before" and "after" are already available and no external time scale is needed. The clock breaks the moment you cannot tell, from your position in the code, which pass through it you are on — cycles, nondeterminism, interleaved processes, unstructured control. At that point "where" and "when" come apart and an outside time scale becomes unavoidable. Knowing which of your programs have an intact internal clock and which do not tells you exactly where the heavier reasoning is owed, and where it would be waste.

**Source:** [The Temporal Logic of Programs](../works/the-temporal-logic-of-programs.md) — the hierarchy of specifications organized by how many time instances a property needs, the argument against carrying an explicit real-time parameter as too powerful for the job, and the closing discussion asking whether external time is needed at all, which answers by pointing at the program's own execution as an internal clock and identifying the program shapes that destroy it.
