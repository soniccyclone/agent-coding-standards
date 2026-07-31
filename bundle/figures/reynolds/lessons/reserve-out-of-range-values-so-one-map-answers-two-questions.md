---
type: lesson
title: "Reserve values outside the legitimate range so one map answers both where-is-it and which-set-is-it-in"
figure: reynolds
works: [the-craft-of-programming]
axes: [hardware-affinity, primitive-count, verifiability]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# Reserve values outside the legitimate range so one map answers both where-is-it and which-set-is-it-in

**Lesson:** Two questions that programs ask constantly are "which of these several sets does this item belong to" and "where in the working structure is it". They look like they need two tables. They usually need one, because the answer to the second question is drawn from a bounded range of legitimate positions, and every value outside that range is free for you to spend as a tag. Give each membership class that has no position a distinct out-of-range value, and a single lookup returns the class and, when the class has one, the position — one array, one probe, no consistency problem between two structures that could disagree.

The technique is only as good as the statement of what the values mean, so write the correspondence as a representation invariant with one clause per class, in the form of a case analysis over the item: this class implies this reserved value, that class implies a value inside the live range that also indexes back to the item itself. Two things fall out of writing it that way. The invariant is now the single place where every update site's obligation is defined, so adding a new operation is a matter of checking one condition rather than remembering an unwritten convention. And the round-trip clause — the position indexes a cell that holds the item back — is the part that makes the map usable in the direction you did not build it for, which is normally the reason you wanted a position at all.

One presentational discipline is worth adopting with it: name the sentinel by its role, not by its numeric value. The actual choice is an arbitrary integer just past the largest legitimate index, and putting that arithmetic into the program's text buries the logic under a coincidence about sizes. Use a symbolic name that says "larger than any real position", carry it through the reasoning, and substitute the concrete value at the very end. This keeps the argument about the sentinel's *property* — that it can never be mistaken for a position — separate from the argument that some particular number has that property, and the two go wrong for different reasons.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 5.4.3, which introduces an integer array indexed by node serving two purposes at once: for nodes in the unclassified set it gives the node's position in the enumerating array, with the invariant clause that indexing that array at the stored position returns the node; and for every node it distinguishes not-yet-visited from already-emitted from unclassified by storing zero, a value too large to be a legitimate position, or a legitimate position respectively, with the whole correspondence written as a three-branch representation invariant; Reynolds notes that in practice one more than the node count suffices as the large value but writes an infinity symbol instead to keep the program's logic clear.
