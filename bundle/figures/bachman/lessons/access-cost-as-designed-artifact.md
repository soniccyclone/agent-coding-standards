---
type: lesson
title: "The cost of reaching data is a designed artifact, not an inherited accident"
figure: bachman
works: [the-programmer-as-navigator]
axes: [hardware-affinity]
subdomains: [databases-and-data-management, operating-systems-and-systems-programming]
tags: [lesson]
---
# The cost of reaching data is a designed artifact, not an inherited accident

**Lesson:** Bachman treats the physical cost of getting from one piece of data to another as a first-class design object. In the navigational model, a relationship between record types is not an abstract fact to be recomputed on demand; it is a declared, materialized path, and related records are deliberately placed on the same page or block so that following the path is cheap in seek terms. He closes the lecture by asking for a real engineering discipline of data mechanics, one that could yield minimum-energy routes through a database the way celestial mechanics yields minimum-energy trajectories through space — including the problem of restructuring a database later, once access patterns have drifted away from the layout that once served them.

The way of thinking underneath: anticipate the traversals your system will actually perform, and let those traversals shape physical structure, rather than laying data out by some neutral logic and paying whatever access cost falls out. The dominant costs are physical (in his era, disk seeks against processors that had already outrun storage; today, cache lines and memory hierarchy), so a design that ignores the geometry of storage has not avoided the question, it has just answered it badly by default.

A programmer who believes this enumerates the expected access paths before choosing a representation, encodes the frequent ones as adjacency or direct linkage, and treats "how does this layout age as access patterns change" as a standing design question rather than a surprise. The relational tradition later won the argument about what the *logical* interface should be, but this lesson survives underneath it: someone, at some layer, still has to do Bachman's thinking about where the bytes sit, and pretending otherwise just moves the cost where it can't be seen.

**Source:** [The Programmer as Navigator](../works/the-programmer-as-navigator.md) — the discussion of database sets, clustering, and declared retrieval order replacing indices, and the closing call for a taught engineering discipline of data-structure mechanics.
