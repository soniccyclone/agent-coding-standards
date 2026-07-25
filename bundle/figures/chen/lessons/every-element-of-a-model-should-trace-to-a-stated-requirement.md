---
type: lesson
title: "Every element of a model should trace to something someone actually said"
figure: chen
works: [english-sentence-structure-and-entity-relationship-diagrams]
axes: [verifiability, cognitive-load]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Every element of a model should trace to something someone actually said

**Lesson:** The most instructive part of Chen's second paper is not the translation rules, it is the audit he runs with them. He takes a published model that other authors built from a written description of a manufacturing firm's needs, rebuilds one himself from the same text by working through it a statement at a time, and compares. The differences are not stylistic. The published version contains categories and associations the text never asserts, and omits one the text does assert. His diagnosis is that knowledge the original designers happened to carry entered the model without being written down, and the consequence he names is the damning one: nobody starting from the description could reproduce their picture. The model had stopped being derivable from its inputs.

That reframes what a model is for. When every element traces to a specific statement, the model is checkable against its source, and arguments about the model become arguments about the source — which is progress, because the source is a shared artifact. When elements have untraceable origins, the model has become one person's private summary of their own judgment, and every later question about it has to be routed through that person. Notice Chen is not claiming his rules are correct; he says outright they are fallible guidelines with counterexamples. The value is not infallibility, it is that mechanical application leaves a visible trail. Deliberate exclusions are part of that trail too: statements about the apparatus by which data gets collected are ruled out of the structural model on purpose, and the ruling is stated rather than performed silently.

A programmer who works this way treats "which requirement is this table, field, or type here for?" as a question with a recorded answer, and when they add something from their own experience of the domain rather than from the brief, they say so. Two people modeling the same brief should converge; where they diverge, the divergence localizes an undocumented assumption, which is exactly the thing worth finding. Checking a model against the text it came from costs an afternoon. Discovering the assumption after it has shaped a schema costs considerably more.

**Source:** [English Sentence Structure and Entity-Relationship Diagrams](../works/english-sentence-structure-and-entity-relationship-diagrams.md) — the worked case study rebuilding another team's published model from the same requirements text, and the comparison section arguing which version is more faithful to its source and why the extra elements are undocumented designer knowledge.
