---
type: lesson
title: "Make the system an object that a weaker tool can inspect from outside"
figure: church
works: [a-set-of-postulates-for-the-foundation-of-logic]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [formal-methods-and-verification, foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Make the system an object that a weaker tool can inspect from outside

Church wants to know whether his logic can contradict itself, and he notices that its complete formality is what makes the question approachable. Because every rule is stated as an operation on symbols, one can drop the interpretation entirely and view proving as a game of marks on paper played by fixed rules, then stand outside that game and reason about which arrangements of marks it can ever produce. The system's own strength is irrelevant to this outside reasoning; what matters is that the system is a finite-rule generator over a countable supply of symbols, so its formulas and its proofs are enumerable objects.

The ambition he attaches to that observation is the part worth carrying. He hopes the reasoning needed about the game will require nothing stronger than the logic of enumerable collections and the ordinary positive integers — that is, far less than the logic being studied. That hope is not modesty; it is the whole point. An analysis conducted with tools as powerful as the thing analyzed establishes very little, because your confidence in the analysis is then hostage to the same doubts. The value of an external check scales with how much weaker and more obviously trustworthy the checker is than its subject.

Two design consequences follow for anyone building systems rather than logics. First, formality is leverage, not bureaucracy: the more of a component's behavior is determined by a small set of mechanical rules over inspectable structures, the more can be settled about it by an outside tool that never runs it. Second, deliberately keeping the artifact's state space enumerable — bounded configurations, explicit transitions, no reliance on unrestricted runtime behavior — is what makes exhaustive checking available at all. Systems whose behavior can only be known by execution have foreclosed this option, usually without noticing they had it.

A programmer thinking this way asks of every component what could be decided about it without running it, and treats the answer as a design variable rather than a fact of nature. They prefer configuration that a small script can enumerate over configuration that only the application can interpret, and they keep the verifier plain — a modest checker over a restricted representation buys more real confidence than an elaborate one that reproduces the complexity it is meant to police.

**Source:** [A Set of Postulates for the Foundation of Logic](../works/a-set-of-postulates-for-the-foundation-of-logic.md) — the section discussing the possibility of a consistency proof, which recasts derivation as a rule-governed game over marks and appeals to the enumerability of formulas and proofs to hope for a metatheory no stronger than arithmetic on the positive integers.
