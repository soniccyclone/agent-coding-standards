---
type: lesson
title: "Restoring a saved mark is only sound if every intervening operation is proved never to shrink past it or rewrite below it"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, hardware-affinity]
subdomains: [formal-methods-and-verification, operating-systems-and-systems-programming]
tags: [lesson]
---
# Restoring a saved mark is only sound if every intervening operation is proved never to shrink past it or rewrite below it

**Lesson:** Replacing a set-valued variable by an array plus a fill pointer turns "restore the set to what it was on entry" into "put the pointer back where it was", and that looks free. It is not free. Assigning the old index back is only equivalent to restoring the old set if the region below the mark still holds what it held — same contents, same order, same length — and nothing in the code you are looking at establishes that. The truth of the substitution depends entirely on the behaviour of everything that ran in between, which in a recursive procedure is an unbounded number of activations of the procedure itself.

So the mark-and-restore idiom carries a proof obligation, and it is a specification you have to write for the callee rather than an observation about the caller. Two clauses: the pointer on exit is never below the pointer on entry, and the array prefix up to the entry pointer is unchanged. That is the abstract content of "stack discipline" — the callee may pile things on and may take its own things off, but it may never eat into what was already there. Once stated, it is proved the usual way, assumed for the recursive calls and then discharged for the body, and it composes across a sequence of calls because each one's guarantee starts where the previous one's left off. Only with that in hand does the pointer assignment become a legitimate implementation of the set restoration.

The general point is worth carrying beyond arrays. Any time you make a cheap operation stand in for an expensive one by remembering a position — an index, a file offset, a log sequence number, a checkpoint — you are asserting something about everyone else's access pattern, not about your own. The assertion is usually true, which is why it is usually not written down, and why the eventual violation is so hard to find: someone adds an operation that reaches below the mark, every individual piece of code still looks correct, and the failure appears in a component that never changed. Write the discipline into the callee's specification while it is still obvious, so the person who breaks it fails a check instead of shipping.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 5.4.3, where the unclassified-node set is represented by an array segment and a fill pointer, the restoration of the set to its saved value is implemented by restoring the pointer to a saved index, and Reynolds observes that the argument this preserves the representation invariant is more subtle than it appears: it requires proving that search satisfies a specification saying the pointer never ends below its entry value and the array prefix up to the entry value is unmodified, assumed for recursive calls and then established for the body, and used to show that the composed sequence of calls in the successor loop leaves the saved prefix intact.
