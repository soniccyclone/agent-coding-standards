---
type: lesson
title: "Keep structural virtues separate: layering and clean boundaries are independent, and each buys something different"
figure: parnas
works: [on-the-criteria-to-be-used-in-decomposing-systems-into-modules]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Keep structural virtues separate: layering and clean boundaries are independent, and each buys something different

**Lesson:** Praise for a system's structure usually arrives as a blur — it is layered, it is modular, it is clean — as if these were one property observed from different angles. They are not, and conflating them lets a design collect credit it has not earned. Layering is a claim that some dependency relation among the parts is a partial order, with no cycles. Clean decomposition is a claim about what the parts know about each other. A system can be perfectly stratified and still have every important representational decision baked into the agreements between strata, in which case the acyclicity bought you nothing when a decision moves. The two properties are separately desirable and separately absent, so they must be separately checked.

The other half of the discipline is being precise about what relation you are ordering. "Calls" is the relation people reach for and it is the wrong one: what matters is depends-upon, and dependency is often on a part of another component rather than the whole of it — a client may rely on the retrieval behavior of something while being entirely indifferent to whether its mutation behavior works. Defining the order over units that are too coarse manufactures cycles that do not exist and hides real couplings inside a node. Get the relation right and layering starts paying: lower parts are simpler because they lean on nothing, and you can lop off the top of the structure and still hold a working system, which is what makes parts reusable in unrelated applications rather than merely tidy.

A programmer who separates these asks two independent questions of any architecture. Is the depends-upon relation actually acyclic, at the granularity of what is really depended on? And separately, for each edge in it, what does the upper end have to know about the lower — a name and a shape, or a layout? An affirmative answer to the first with a bad answer to the second is the common case in systems that everyone agrees are well structured and nobody can change.

**Source:** [On the Criteria To Be Used in Decomposing Systems into Modules](../works/on-the-criteria-to-be-used-in-decomposing-systems-into-modules.md) — the hierarchical-structure section, which works out the levels of the second decomposition, argues for depends-upon over calls and for relating programs rather than whole modules, and closes by insisting the two properties are desirable but independent.
