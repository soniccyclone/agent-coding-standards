---
type: lesson
title: "Undecidable in general still leaves cheap answers in the cases you actually meet"
figure: post
works: [a-variant-of-a-recursively-unsolvable-problem]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Undecidable in general still leaves cheap answers in the cases you actually meet

Post spends most of this paper proving that a certain matching question about lists of strings admits no general procedure. But before the proof he does something easy to skip past: he shows the question is often settled instantly. One worked instance is answered by exhibiting a match. Two whole families are answered negatively by inspection — if each string on one side is longer than its partner, the two sides can never come out to the same length; if each pair disagrees on its first letter, no sequence can begin. Neither observation requires any machinery. They are one-line checks on the input, and they dispose of enormous swathes of instances. The impossibility result is precisely and only about full generality.

Getting the relationship right between these two facts matters more than either alone. Undecidability is a statement about the nonexistence of a procedure correct on every input, and it is compatible with a procedure that is correct whenever it answers and merely declines on the rest. That third outcome is what makes the practical world work. The hard instances that force undecidability are constructed adversarially, by encoding an arbitrary computation into the problem; they are not what shows up when you have a real question about real data. So the correct response to "this is undecidable" is not to abandon the problem but to go looking for the decidable fragment — the syntactic conditions, the conserved quantities, the counting arguments that settle most instances without solving any of them in the general sense.

The failure mode this guards against is a specific kind of learned helplessness among people who know just enough theory. Whether a program halts is undecidable, so we cannot detect infinite loops — and yet every serious compiler warns about a great many of them. Type inference in a rich system is undecidable, so annotation is unavoidable everywhere — yet inference handles most code and asks for help at the edges. Alias analysis, termination of a recursive query, reachability of a state in a protocol: all undecidable in general, all routinely answered in practice by a sound one-sided check. Invoking the impossibility theorem to justify not trying is a misreading of what the theorem says.

The habit is to look for the conserved or monotone quantity. Post's easy cases are both of that shape — a length that can only grow, a first letter that can never be revised. That is where cheap partial decision procedures come from: find something the process cannot change, and the instances that require changing it are answered without any search at all.

**Source:** [A Variant of a Recursively Unsolvable Problem](../works/a-variant-of-a-recursively-unsolvable-problem.md) — the opening paragraphs, which give a solvable instance and two easily recognized classes of unsolvable ones before asserting unsolvability only for the problem in full generality.
