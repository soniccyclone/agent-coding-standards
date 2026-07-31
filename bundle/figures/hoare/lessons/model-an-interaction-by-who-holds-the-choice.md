---
type: lesson
title: "Model an interaction by who holds the choice: input and output differ in nothing else"
figure: hoare
works: [communicating-sequential-processes-book]
axes: [expressiveness, verifiability, parallelizability]
subdomains: [distributed-systems-and-concurrency, programming-languages-and-semantics]
tags: [lesson]
---
# Model an interaction by who holds the choice: input and output differ in nothing else

**Lesson:** Describe a component not by what it does next but by what it is currently willing to do — the set of interactions it is offering at this moment. Which of them actually happens is then decided by whoever is on the other side. This single reframing dissolves a distinction that normally has to be built into a system's foundations. Receiving is offering several alternatives and letting the environment select among them; sending is offering exactly one and letting the environment take it or wait. There is no separate notion of direction, no notion of who acts and who is acted upon, and no concept of causation anywhere in the model. The asymmetry everyone means when they say "input" versus "output" turns out to be entirely an asymmetry in the size of the offered set.

The practical yield is that a component's specification becomes a menu at each point rather than a script, and a menu is exactly what a caller needs to know. It also makes a certain class of design error visible as a shape rather than as a symptom. If a component offers alternatives it cannot honour, or offers nothing in a state its partner will reach, that is legible directly from the menus, without simulating the interaction. And the classic bug of a component that "appears to offer a choice but does not" — two apparent alternatives that are really the same offer — is caught by inspecting whether the offered items are actually distinguishable to the party doing the choosing.

Two habits follow. First, write down the menu at each state, including the empty menu, since a state offering nothing is a legitimate and important thing to be able to say rather than an oversight. Second, when a design feels asymmetric — this side drives, that side responds — check whether the asymmetry is real or an artifact of the vocabulary. Frequently the two sides are doing the same thing with differently sized offers, and noticing this collapses two mechanisms into one, along with two sets of rules for reasoning about them.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-book.md) — the choice section of the chapter on processes, where a process offers alternatives whose selection is exercised by the customer or environment; the bit-copying example, which notes that the process lets its environment choose which value is input but offers no choice on output, and identifies this as the main difference between input and output in the later treatment of communication; the general choice form in which a set of events is the initial menu, degenerating to a single prefix when the menu is a singleton and to a permanently stopped process when it is empty; and the introduction's earlier observation that no distinction is drawn between events initiated by the object and by its environment, since avoiding causality simplifies both the theory and its application.
