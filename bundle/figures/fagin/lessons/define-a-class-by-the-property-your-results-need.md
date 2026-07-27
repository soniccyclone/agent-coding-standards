---
type: lesson
title: "Define a class by the property your results need, not by listing its members"
figure: fagin
works: [horn-clauses-and-database-dependencies]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [databases-and-data-management, foundations-of-computation]
tags: [lesson]
---
# Define a class by the property your results need, not by listing its members

**Lesson:** By 1980 the constraint notions in database theory had multiplied into a dozen incompatible named kinds, each introduced by a different author to cover a case the previous ones missed, each generalizing two or three of its predecessors along a different direction. Fagin describes his aim as bringing order to that mess, and the method he chooses is worth more than the specific order he brings. He does not attempt a taxonomy, and he does not add a thirteenth notion that subsumes the other twelve by construction. He asks instead what abstract property every one of the existing notions happens to have, finds one, and then proposes that the right definition of the whole category is simply "the statements with that property." Membership stops being a list you consult and becomes a test you apply.

The property he selects is not chosen for elegance. It is chosen because it is exactly what the theorems need: the results he wants about the existence of canonical example structures follow from that property and nothing else. That inverts the usual order of definition. Rather than defining a class from intuition and then discovering which theorems survive, he identifies the load-bearing hypothesis of the theorem he cares about and promotes it to the definition. The class that results is wider than the union of everything previously studied, and the extra generality costs nothing because the proof never touched the specifics anyway.

Two pieces of external evidence confirm the class was found rather than invented. A pair of researchers working independently arrived at what looked like an entirely different definition, built from relational operations instead of logical form, and the two classes turned out to coincide. A third group's two separate constraint families, taken together, coincide with the same class. Fagin reads the convergence as evidence that the boundary is natural. That is the right inference: when unrelated routes to a definition land on the same set, the set is probably a real seam in the subject rather than an artifact of one person's taste.

A programmer who works this way stops writing interfaces that enumerate the cases they support. When a codebase accumulates a family of near-duplicate handlers, the productive question is not which of them to make canonical but what single property all of them satisfy that makes the shared machinery work at all. Naming that property yields a definition with fewer moving parts, admits cases nobody had thought of yet, and gives a decision procedure for whether a new case belongs. Enumeration, by contrast, guarantees that the list will be wrong again next quarter.

**Source:** [Horn Clauses and Database Dependencies](../works/horn-clauses-and-database-dependencies.md) — the introduction, which surveys the proliferation of dependency notions and states the goal of unifying them by shared mathematical properties, together with the remarks on the independently discovered equivalent characterizations that Fagin treats as evidence of the class's naturalness.
