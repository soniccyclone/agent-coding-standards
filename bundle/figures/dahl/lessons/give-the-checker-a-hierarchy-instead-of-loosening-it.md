---
type: lesson
title: "When safety and flexibility seem to trade off, the fix is more structure in the type space, not a weaker check"
figure: dahl
works: [class-and-subclass-declarations, simula-67-common-base-language]
axes: [verifiability, expressiveness, hardware-affinity]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# When safety and flexibility seem to trade off, the fix is more structure in the type space, not a weaker check

**Lesson:** The apparent dilemma is familiar. A statically checked record discipline where every reference must range over exactly one record class is safe and fast and unusable, because real data collections hold things that are partly alike and partly different. A dynamically discriminated discipline where the programmer must interrogate the class of anything before touching it is safe and general but pays a test on every access and clutters the code with interrogation. Presented with those two options one is tempted to split the difference by relaxing the check — to allow references that promise nothing and trust the programmer. That move looks like flexibility and is actually the abandonment of the property both disciplines were built to deliver.

The productive move is to notice that the dilemma comes from an impoverished space of types, not from an excess of checking. Give the classes a partial order, so that a class can be an extension of another and every object of the extension is also legitimately an object of what it extends. Now a reference can state a class and mean "this or anything below it," which is exactly the honest description of a heterogeneous collection that shares a common part. Most access is to the shared part and is checked statically against the stated bound. Assignment is legal whenever the two bounds are ordered, in whichever direction; the only residue needing a runtime decision is narrowing, where the static bound is weaker than the code's assumption. Precision goes up, the number of runtime tests goes down, and expressiveness goes up, all from the same structural addition.

The general shape of the lesson: when a checked discipline is strangling you, look first at whether the discipline has enough vocabulary to describe what you are actually doing. A check that rejects a sound program is usually evidence that the type space cannot express the relationship the program depends on. Adding that relationship as structure gives the checker purchase where it had none, and the cost falls in the right place — a one-time enrichment of the language's model rather than a per-access tax or a permanent loss of guarantee. Reaching for an escape hatch instead ends the conversation and leaves the sound program indistinguishable from an unsound one.

**Source:** [Class and Subclass Declarations](../works/class-and-subclass-declarations.md) — the introduction, which weighs a strict record-class scheme against SIMULA's runtime connection mechanism and presents subclassing as the way past both, together with the reference-assignment section that enumerates the legality cases by how the two qualifying classes are related. Also [SIMULA 67 Common Base Language](../works/simula-67-common-base-language.md) — the definition of qualified references and the subclass inclusion ordering they are checked against.
