---
type: lesson
title: "Build levels so that each one offers a different kind of change"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Build levels so that each one offers a different kind of change

**Lesson:** A complex system is best structured as a sequence of levels, each described in its own language: parts treated as primitive at one level are combined there, and the results become the primitives of the level above. Every level gets its own primitives, its own means of combination, and its own means of abstraction, chosen to suit the detail at that level rather than inherited from below.

What makes this more than a restatement of layering is the definition of robustness attached to it. A design is robust when a small change to the specification requires a correspondingly small change to the program -- change-proportionality, not absence of change. And stratification delivers that because each level supplies *a different kind of ability to change*. In the worked example, altering the appearance of the basic element, altering how it is replicated, and altering how the replicas are arranged are three different edits at three different levels, each small, each expressed in the vocabulary where that concept is native. Without the stratification all three would be the same tangled edit in one place.

That reframes the design question productively. Rather than asking how to decompose the system, ask what kinds of change you expect and whether each has a level whose vocabulary makes it a local edit. A change that has no natural level is the diagnostic: it means the concept it modifies is not represented anywhere as a thing, so the modification is forced to spread. That is a much more actionable test than counting dependencies, and it is testable in advance by naming candidate changes and locating where each would land.

The generalization is that this is how engineering handles complexity everywhere, and the book's examples run from circuit elements up through gates, processors, machines, and networks -- each a language whose primitives are the previous level's compounds. The move worth copying is not the layering itself but the deliberate provision, at each level, of a vocabulary in which one whole category of anticipated change is a small local statement.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - chapter 2 section 2.2.4's closing on levels of language for robust design, which introduces stratified design as structuring a system as a sequence of levels described by a sequence of languages, each level combining parts primitive at that level to produce the primitives of the next, with the picture language's own three levels as an instance; observes that stratified design makes programs robust in the sense that small changes in a specification require correspondingly small changes in the program; and states that each level provides a different vocabulary for expressing the system's characteristics and a different kind of ability to change it -- illustrated by three separate edits to the same image at three different levels.
