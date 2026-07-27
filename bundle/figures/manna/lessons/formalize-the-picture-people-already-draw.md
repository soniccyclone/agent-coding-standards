---
type: lesson
title: "Formalize the picture people already draw instead of leaving it as illustration"
figure: manna
works: [temporal-verification-diagrams]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Formalize the picture people already draw instead of leaving it as illustration

**Lesson:** Manna and Pnueli had been drawing diagrams alongside their proof rules for years, and in every earlier paper the diagram was decoration — the rule carried the formal weight, the picture helped the reader. Here they invert it: the diagram becomes the proof, and the rules are removed from the system entirely. A graph whose nodes are assertions about program states and whose edges are labeled with the transitions that can move between them mechanically determines a finite set of obligations — for each node and each transition, where the successor state is allowed to land — and if all of those obligations hold, the temporal property follows. Nothing is lost by deleting the rules, because the rules were only ever a linear serialization of what the picture already said.

The move is worth studying because of what it says about where formality should sit. The informal artifact was doing real cognitive work that the formal one wasn't: it showed at a glance which intermediate situations a computation passes through and what can move it between them, whereas the corresponding rule was a list of premises whose relationship to each other you had to reconstruct. Faced with that gap the tempting response is to write better prose around the rule. The better response is to notice that the thing people reach for when they need to *understand* is the thing that should be load-bearing, and give it a precise meaning. A representation that reads as intuition in one direction and expands into mechanical obligations in the other is strictly better than either half alone, and the second reading is what makes it safe to trust the first.

There is a hard condition on doing this, and it is the whole engineering content: the informal artifact must determine its obligations completely and unambiguously, including for the cases it does not visibly mention. The diagrams achieve this by fixing a default — a transition that labels no departing edge from a node is treated as an edge from that node back to itself, meaning it must preserve the assertion. Without that convention the picture would be silent about most transitions and the two readings would come apart. Every diagram-as-specification scheme lives or dies on whether the absent cases have a defined meaning rather than an undefined one.

The transferable habit: when a team communicates a design or an argument through a whiteboard artifact that the official documentation does not capture, that is a signal about which representation is right, not about the team's rigor. The productive response is to give the sketch a precise semantics — what does a box mean, what does an arrow mean, what does an *absent* arrow mean, and what checkable obligations does the whole thing generate — and then delete the redundant formal artifact rather than maintaining both.

**Source:** [Temporal Verification Diagrams](../works/temporal-verification-diagrams.md) — the introduction, where the authors state that previous uses of these diagrams were secondary to the rules and that this is their first rule-free system, and the section defining diagrams together with the verification conditions each node and transition spawns, including the implicit self-edge convention.
