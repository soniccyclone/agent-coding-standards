---
type: lesson
title: "To change a representation, run both levels at once under a stated invariant, then delete the upper one"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# To change a representation, run both levels at once under a stated invariant, then delete the upper one

**Lesson:** Replacing an idealized description of some data with a real layout is the step where most rewrites go wrong, because people do it by translating: read the old code, imagine the new storage, write the new code, and hope the two agree. There is a version of the same move that is mechanical and leaves an audit trail. Bring the concrete variables into existence alongside the abstract ones instead of in place of them. Write down, as a standing condition, the exact relationship the two are supposed to bear to each other. Then discharge two obligations that between them exhaust the program: every place that writes the abstract thing gets extra writes that restore the relationship, and every place that reads the abstract thing gets rewritten into a read of the concrete thing that the relationship guarantees has the same value. When both are done the abstract variables are being written and never read, which is precisely the condition for deleting them.

What makes this more than a tidy ritual is that the relationship, once written down, does the reasoning for you. Every correctness claim you established at the abstract level survives untouched — you never edited the abstract program, you only shadowed it — so no argument has to be redone in the concrete vocabulary. And the two obligations are enumerable: you can find every write and every read by inspection, which turns "did I convert this correctly?" from a judgement call into a checklist that can be run to exhaustion. Errors, when they happen, are localized to a single site failing to restore the relationship, rather than diffused across a translation.

The general shape is worth extracting from the setting. Any migration — a schema change, a new index, a cached denormalization, a different in-memory structure — becomes tractable if you can pass through a phase where old and new coexist and one stated condition ties them together. The condition is the thing to write first, before either the reads or the writes are touched, because it is what tells you what "correct" means for every individual edit. Teams that migrate by dual-writing have found this by instinct; the part usually skipped is naming the invariant explicitly and then using it, rather than a diff, to justify each rewritten read.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 5.1.4's four-step general method for replacing an abstract variable by its representation: introduce concrete variables, introduce a representation invariant relating abstract to concrete as a general invariant, augment each assignment affecting that invariant with assignments that reestablish it, and replace each expression mentioning an abstract variable outside such an assignment by an equivalent expression the invariant guarantees, with the closing observation that the last step renders the abstract variables auxiliary so their declarations and assignments can be eliminated — worked through on the reachability program by representing the result set as a characteristic vector over the node universe.
