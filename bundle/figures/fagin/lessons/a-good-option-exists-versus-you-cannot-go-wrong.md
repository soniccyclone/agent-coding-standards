---
type: lesson
title: "\"A good option exists\" and \"you cannot go wrong\" are different guarantees, and only the second licenses delegation"
figure: fagin
works: [degrees-of-acyclicity-for-hypergraphs-and-relational-database-schemes]
axes: [verifiability, hardware-affinity, cognitive-load]
subdomains: [databases-and-data-management, algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# "A good option exists" and "you cannot go wrong" are different guarantees, and only the second licenses delegation

**Lesson:** The weaker structural condition in Fagin's hierarchy is equivalent to the existence of at least one combining order that never inflates an intermediate result beyond the final answer. The stronger condition is equivalent to every sensible combining order having that property. Existential and universal, with the same subject matter, and the gap between them is exactly the gap between two named degrees of a graph property. Reading them side by side makes visible something engineers usually blur: knowing a good path exists is a weak guarantee that puts the burden of finding it on whoever acts, while knowing no path is bad is a strong guarantee that makes the choice free.

Only the universal version supports handing the decision to someone else. Under the existential condition, an optimizer or a user must be steered, because most of the orders available to them are bad and only careful analysis distinguishes them. Under the universal condition the choice can be delegated downward without oversight, since anything they pick works. Fagin spells out the one caveat, which is instructive on its own: the universal claim holds for orders that never combine two pieces sharing nothing in common, and he proves separately that combining unrelated pieces can never be part of a good order anyway. So the exception is not a hole in the guarantee. It is a triviality that a caller cannot stumble into by accident, which is precisely what makes the guarantee delegable in practice.

The generalizable point concerns where you aim your design effort. Most systems settle for the existential guarantee and then spend forever building the thing that finds the good path: the query planner, the scheduling heuristic, the configuration guide, the wiki page explaining which of five approaches to use. That machinery exists because the structure permits bad choices. Buying the universal guarantee instead, when it is available, deletes the machinery rather than improving it. The cost is a stronger constraint on the structure, and the return is that a whole layer of guidance, tuning, and documentation stops being necessary.

A programmer who holds this distinction asks of every API, schema, or protocol whether misuse is possible or merely discouraged. An interface where any legal call sequence is correct needs no usage guide; one where a good sequence exists needs one forever, and the guide will be wrong eventually. The same reading applies to reviewing someone else's guarantee: when a claim is that something can be done efficiently or safely, the useful follow-up is whether it can also be done inefficiently or unsafely, because that answer determines how much surrounding apparatus the claim implies.

**Source:** [Degrees of Acyclicity for Hypergraphs and Relational Database Schemes](../works/degrees-of-acyclicity-for-hypergraphs-and-relational-database-schemes.md) — the contrast drawn in the section on the strongest degree between the earlier result equating the weak degree with the existence of a well-behaved join expression and the new result equating the strong degree with every connected join expression being well-behaved, together with the theorem showing that expressions containing a Cartesian product can never be well-behaved.
