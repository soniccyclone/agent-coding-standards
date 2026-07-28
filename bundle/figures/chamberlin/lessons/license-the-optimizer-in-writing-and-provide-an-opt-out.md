---
type: lesson
title: "Write down what the optimizer is allowed to skip, and give the programmer a way to opt out"
figure: chamberlin
works: [xquery-1.0-an-xml-query-language]
axes: [verifiability, parallelizability, expressiveness]
subdomains: [programming-languages-and-semantics, databases-and-data-management]
tags: [lesson]
---
# Write down what the optimizer is allowed to skip, and give the programmer a way to opt out

A declarative language earns its speed by not doing what its own semantics literally describe: not scanning the whole input when an index answers the question, not evaluating both operands when one settles the result, not materializing a sequence whose order nobody observes. Every such shortcut is visible in exactly one place — error behavior. The abbreviated evaluation returns the same value, but it fails to hit the item that would have raised the type error, so a program's failure becomes a function of the implementation's cleverness. The wrong response is to forbid the shortcuts, and the equally wrong response is to say nothing and let each vendor decide. The right one is to state the license precisely: an implementation may stop evaluating an operand as soon as the only remaining outcomes are one particular value or an error, and it may then deliver the value.

What makes that a specification rather than a shrug is the carve-outs. Constraints on how many items an operand may produce are exempt: a processor may not conclude from the first item that the answer is decided, because a second item would be a violation it is still obliged to notice. The license cascades through nested operands, so a partial evaluation of an inner expression suffices for a partial evaluation of an outer one, which is what makes the rule usable for real query rewriting rather than only for short-circuit booleans. And because rewriting can move a guard past the thing it guards, the design owes the programmer a construct whose branches are genuinely not evaluated — a conditional and a type dispatch that suppress failures in the branches not taken — so that "test before you convert" is expressible in a way no reordering can break.

The mirror image is ordering. Guaranteeing document order everywhere costs joins their freedom to be driven from whichever side has the index, so the design exposes a lexically scoped mode that relaxes it, and then does the unpleasant work of saying exactly what becomes unpredictable under it: positional predicates, position and last, anything that reads an index into a sequence. Naming the fallout is what makes the relaxation safe to use; a knob whose consequences are undocumented is a trap dressed as a tuning option.

The transferable habit is to treat nondeterminism as something you grant explicitly and bound, never as something that leaks. If your system may skip work, say which observations can change as a result, exempt the checks that must always happen, and ship a construct that turns the freedom off where correctness needs it. A system whose failure modes depend on the mood of its optimizer is not fast, it is unpredictable.

**Source:** [XQuery 1.0: An XML Query Language](../works/xquery-1.0-an-xml-query-language.md) — the errors-and-optimization section, which states the sufficient-sample evaluation license, its cardinality-check exception, and its cascading through nested operands, then points to the conditional and type-dispatch expressions as the way to write guards that survive rewriting; together with the ordered/unordered expression section and its enumeration of what becomes nondeterministic.
