---
type: lesson
title: "Where a claim gets evaluated is part of the claim"
figure: manna
works: [the-anchored-version-of-the-temporal-framework]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Where a claim gets evaluated is part of the claim

**Lesson:** A specification language does not just need operators; it needs a decision about the vantage point from which its sentences are read. Two systems can share every operator and still differ in whether a sentence is asserted about the start of an execution or about every moment of it. That single choice propagates everywhere. Read a sentence as holding at all moments and the ordinary properties a programmer actually wants — this run terminates, this response was requested before it arrived — can only be written with an explicit marker dragged along to pin the reader back to the beginning. Read it as holding at the start and those properties become the short, unguarded default, while the genuinely all-moments claims are the ones that must say so.

The deeper cost of the wrong default is not verbosity, it's that the algebra around the language quietly stops working. Manna and Pnueli's complaint against the everywhere-reading is precise: it forces a generalization step that breaks the equivalence between "q follows from p" and "p implies q," which is one of the load-bearing manipulations anyone reasoning inside the system relies on. It also forces the set of runs under consideration to be padded with every tail of every run, purely so a proof rule remains sound — a definition nobody would write down for its own sake. When a formalism needs an artificial enlargement of its models to keep one rule alive, the rule is telling you the frame is wrong.

A programmer who takes this seriously stops treating the reference frame of an assertion as an implementation detail of the checker and treats it as a first-class design decision, made in favor of whatever the frequent case is. Concretely: decide once whether a contract, invariant, log predicate, or type refinement speaks about the entry state, every state, or the terminal state, make the frequent one syntactically free, and require the rare ones to be explicit. The corollary is a diagnostic — when the common case in your notation needs a guard clause bolted on to be true, the default frame is inverted, and the fix is at the level of the language, not the individual specification.

**Source:** [The Anchored Version of the Temporal Framework](../works/the-anchored-version-of-the-temporal-framework.md) — the paper's central design decision, argued in its introductory section on why the earlier "floating" reading of validity was abandoned in favor of one tied to the initial state, including the list of specific dissatisfactions with the older convention.
