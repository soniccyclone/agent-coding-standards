---
type: lesson
title: "Correctness is a claim about the whole system; a claim about the code alone is a smaller and different thing"
figure: abrial
works: [faultless-systems-yes-we-can, formal-methods-in-industry-achievements-problems-future]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Correctness is a claim about the whole system; a claim about the code alone is a smaller and different thing

**Lesson:** There are two utterly different activities that both get called validation, and conflating them is how catastrophes get shipped with a clean verification report. One establishes properties of the software artifact: no out-of-range index, no dereferenced null, no arithmetic that silently wraps. The other establishes the property the enterprise actually exists to guarantee, which is invariably a statement about the physical world — that no two vehicles occupy the same stretch of track — and that statement is unprovable about the code alone, because the code is one participant among motors, sensors, track geometry, operators, and other software. A complete audit of the first kind tells you nothing about the second. Abrial's example is a launch failure whose fatal defect was precisely of the code-property kind that had not been checked, but his sharper point is that even a perfect code-property audit would not have licensed the safety claim, because the safety claim was never a claim about the program.

The move that follows is to make the object of rigor the entire system, software and environment together, and to model all of it in one uniform vocabulary. A human pressing a button, a motor spinning up, and a routine computing a control decision are all just state changing discretely; refusing to give the software component a privileged ontology is what lets a single invariant span several components at once, which is the shape most real safety properties have. This inverts what the work of engineering is for. Writing code is an attempt to instruct a machine; modeling is an attempt to instruct yourself, and it necessarily covers things no machine will ever execute — the equipment, the physics, the assumptions about users. Once the model exists and the properties are discharged, producing the program becomes a downstream and largely mechanical task.

A programmer who accepts this stops treating the environment as out of scope. The failure mode to watch for is the retrofit: bolting fictitious bookkeeping variables into a program so that a system-level property can be stated in program terms, then stripping them out of the shipped build. That trick is a confession that the property belongs to a model that was never written down. Build the model first, and the property has a natural home; skip it, and every system-level guarantee has to be smuggled into a language that cannot express it.

**Source:** [Faultless Systems: Yes We Can!](../works/faultless-systems-yes-we-can.md) — the modeling-versus-programming argument and the section drawing the solution-validation/problem-validation distinction, using a train network as the running case. Also [Formal Methods in Industry: Achievements, Problems, Future](../works/formal-methods-in-industry-achievements-problems-future.md) — the closing proposal to model the system requirements before any software/equipment split has been made.
