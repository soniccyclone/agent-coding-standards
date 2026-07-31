---
type: lesson
title: "Reason through objects that do not exist, provided every conclusion lands back where they do"
figure: kolmogorov
works: [grundbegriffe-der-wahrscheinlichkeitsrechnung]
axes: [expressiveness, verifiability]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Reason through objects that do not exist, provided every conclusion lands back where they do

**Lesson:** Kolmogorov's extension theorem lets him always work in a closed system: a probability assignment on any collection of events extends, in exactly one way, to the smallest closed-under-countable-operations collection containing it. That closure is what makes the machinery usable, because unions and intersections of unboundedly many events stay inside and you never encounter an event that has no probability at all. But he immediately adds the honest caveat: even when the original events are actual and at least approximately observable, nothing licenses reading the newly added sets that way. They are generally ideal events with nothing corresponding to them in the world. And then the release: if reasoning that passes through the probabilities of those ideal events arrives at the probability of an actual one, that determination cannot be empirically contradictory either.

This is a complete account of when a fiction is safe to compute with, and it is a condition on conclusions rather than on intermediate steps. Inside the reasoning you may use whatever the extended system provides. What you may not do is let an ideal object be the answer, or start believing it denotes something. Two obligations make the passage sound. The extension has to be forced rather than chosen — Kolmogorov's is unique, so no arbitrary decision made in the ideal region can be secretly carrying the conclusion. And the exit has to be back into the interpretable part, where the claim is one someone could in principle check.

That pattern underwrites a great deal of legitimate unreal machinery. Ghost state that a proof quantifies over and the compiled program does not contain. An intermediate representation with constructs no source language exposes. A relaxed problem solved over an infeasible region and rounded back to a feasible point. A sentinel value no real record could hold. In each case the same discipline applies, and the recognizable failures are the two obligations being dropped: an ideal value escaping to a caller who takes it for real, or an extension that involved a free choice, so that the conclusion depends on a convention nobody agreed to. Keep the closure for the reasoning, keep the interpretation for the boundary, and be able to say which side of that line any given quantity is on.

**Source:** [Grundbegriffe der Wahrscheinlichkeitsrechnung](../works/grundbegriffe-der-wahrscheinlichkeitsrechnung.md) — Chapter II, §2, the extension theorem establishing that a probability extends uniquely to the smallest Borel field, followed by the closing remark that sets of the extension are generally ideal events with nothing corresponding to them in the outside world, and that reasoning using them which determines the probability of an actual event automatically fails to be contradictory from the empirical standpoint.
