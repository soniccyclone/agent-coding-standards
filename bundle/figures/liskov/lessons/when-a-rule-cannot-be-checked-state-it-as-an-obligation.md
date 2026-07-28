---
type: lesson
title: "When a rule cannot be checked, state it as an obligation instead of approximating it"
figure: liskov
works: [clu-reference-manual]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# When a rule cannot be checked, state it as an obligation instead of approximating it

**Lesson:** Some correctness rules are mechanically checkable and some are not, and the design mistake is to react to an uncheckable rule by inventing a checkable rule that resembles it. Consider what it takes to reuse a familiar notation for a new type: the real requirement is semantic, that the comparison behave like an equivalence relation supporting substitution of one thing for another, that a duplicate be independent enough that later changes to either copy do not disturb the other, that a selection not alter anything. None of that is decidable from syntax. What is decidable is the shape — argument count, result count, whether a result exists at all. A design that checks the shape and stops has caught the part that almost never goes wrong while leaving the part that actually goes wrong untouched, and worse, has told the programmer that their code passed.

The honest move is to make the mechanical constraints as minimal as they can be, permit the reuse broadly, and write down the semantic obligations explicitly and prominently as duties the implementer takes on. Then nobody mistakes the check for the requirement. The obligations also become the vocabulary for reviewing an implementation and the material for a real proof later; they are not a substitute for verification, they are the statement of what verification would have to establish.

The same distinction runs through the harder cases. An implementation of an abstract type typically admits only some of the possible underlying representations as legitimate — not every arrangement of the underlying data corresponds to a sensible abstract value — and no language mechanism will notice a representation that has gone out of bounds. So the legitimacy condition is stated as an obligation on the abstraction's author, and every operation must be shown to preserve it wherever it hands a value back out, including at each step of an operation that yields values one at a time. Likewise, the meaning of an abstract value must be settled before the operations can be written: whether identity or contents is what distinguishes two values determines what comparison, duplication, and state-equivalence must each mean, and confusion there produces operations that quietly contradict each other.

A programmer who believes this labels the rules that can be checked and the rules that must be honored, and refuses to let the first stand in for the second. Faced with a temptation to add a partial check that would catch the easy cases, they weigh it against the false confidence it creates — and frequently prefer no check plus a written obligation, which at least leaves the reader knowing the work is theirs.

**Source:** [CLU Reference Manual](../works/clu-reference-manual.md) — the cluster section's remarks, which decline to add syntactic constraints on reusing notation because such constraints capture only a fraction of correct usage, spell out the semantic duties of comparison, duplication, and state-equivalence operations, and require the author to state and preserve the condition distinguishing legal representations.
