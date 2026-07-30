---
type: lesson
title: "Find the loop's invariant by asking how much of the goal you can have for free"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, algorithms-and-complexity]
tags: [lesson]
---
# Find the loop's invariant by asking how much of the goal you can have for free

**Lesson:** The hard part of building an iterative process is not writing the body; it is deciding what relation the body has to preserve, and that decision has to be made before a single line of the body exists. There is a reliable way to generate candidates. Take the condition you want to hold at the end, and ask which of its conjuncts you could establish immediately, without any iteration at all, by assigning obvious values. Those become the relation you carry. Whatever is left over — the part you could not simply grab — becomes the condition under which the loop keeps going, so that exhausting it is what makes the loop stop. Division shows the shape at its clearest: the equation relating quotient, divisor and remainder to the dividend can be made true in one step by taking the whole dividend as remainder and zero as quotient, which leaves only the requirement that the remainder be small, and that residue is exactly the loop's guard.

The reason this works is that a loop's job is to close a gap, and you cannot see the gap until you have separated what is cheap from what is not. Reversing the order — write the body first, then reconstruct what it happens to preserve — inverts the difficulty, because the body has many accidental properties and only one of them is the design. It also tends to produce loops that maintain more than they need to, since anything the body incidentally leaves alone looks like part of the invariant. Working from the goal backwards forces the relation to be exactly as strong as the exit needs and no stronger.

Two practical addenda follow from the same analysis. Include in the relation whatever range facts the termination argument will consume, even though correctness alone does not need them — you know in advance that progress will be measured by some quantity approaching a bound, so put the bound in the relation while you are choosing it rather than bolting it on after the loop misbehaves. And expect the initialization step to be omissible when the entry condition already implies the relation, and the finalization step to be omissible when the relation together with the negated guard already implies the goal. Those two omissions are the sign that the split was made in the right place; needing substantial work at both ends usually means the relation you picked is not the natural one.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 1.3.4's development of integer division, where the invariant is found by asking how much of the final assertion can be achieved directly; together with Section 1.3.3's general recipe for meeting a specification with a while statement, including the conditions under which the initialize and finalize parts may be dropped and the separate obligation to exhibit a decreasing quantity.
