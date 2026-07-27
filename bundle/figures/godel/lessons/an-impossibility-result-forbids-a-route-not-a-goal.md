---
type: lesson
title: "An impossibility result forbids a route, not a goal — read its hypotheses before you give up"
figure: godel
works: [remarks-before-the-princeton-bicentennial-conference]
axes: [verifiability, expressiveness]
subdomains: [foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# An impossibility result forbids a route, not a goal — read its hypotheses before you give up

**Lesson:** The man who proved the two most famous limitative theorems in logic spends this talk arguing that limitative theorems are routinely over-read. He notes the obvious objection to what he is proposing — that incompleteness and the definability paradoxes stand in the way — and answers it directly: those results do not rule out the goal under all circumstances, they rule out certain ways of pursuing it, and at minimum they leave closely related concepts available in the stronger form. He then does the work rather than asserting it, sketching two candidate notions that thread the needle. That is the whole method in miniature: an impossibility theorem is a conditional, its hypotheses are load-bearing, and the interesting move is to find which hypothesis you were never actually committed to.

The reason this matters is that impossibility results get compressed in transmission, and the compression always drops the hypotheses. What survives is a slogan, and slogans forbid far more than the theorems do. Incompleteness gets remembered as "formal reasoning cannot be complete," dropping the requirements that the rule-set be fixed, mechanically recognizable, consistent, and rich enough to encode its own syntax — every one of which is a place a real design might not be. In practice this is how limitative results are misused across engineering: as an excuse for not attempting something, invoked from memory, with the actual statement never consulted. The person who does consult it usually finds room, because the theorem was proved about a specific formulation and your situation differs in at least one respect that was not incidental.

What the practising programmer does differently is mechanical. When a result is cited as a reason a thing cannot be built, go read the statement and list its hypotheses. Then check each against your case: is your rule-set actually fixed, or does it get extended by hand each release? Do you need the property for all inputs, or for the inputs you actually receive? Do you need a decision procedure, or a procedure that answers correctly when it answers and says "unknown" otherwise? Is the property required to be checkable inside the system, or is an external checker acceptable? Static analysis, type inference, termination checking, and schedulability all became practical by finding that one of the hypotheses in the relevant impossibility theorem was negotiable — usually by accepting partiality, restricting the input domain, or moving the judgement to a stronger layer.

The mirror-image discipline is just as important and Gödel models it too: when you loosen a hypothesis, say which one, and be clear that you are now solving a nearby problem rather than the original. The move is legitimate exactly because it is explicit. What is not legitimate is quietly claiming the impossible thing, and the way to tell the two apart is whether the person can name the hypothesis they dropped.

**Source:** [Remarks before the Princeton Bicentennial Conference on Problems in Mathematics](../works/remarks-before-the-princeton-bicentennial-conference.md) — the passage answering the objection from incompleteness and the definability paradoxes, which argues those negative results exclude particular ways of defining the notions rather than the notions themselves, followed by the two constructive proposals he offers in their place.
