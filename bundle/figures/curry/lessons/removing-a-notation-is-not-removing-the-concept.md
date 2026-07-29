---
type: lesson
title: "Removing a notation only removes the concept if the new form can prove what the old one could"
figure: curry
works: [grundlagen-der-kombinatorischen-logik]
axes: [expressiveness, verifiability, primitive-count]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Removing a notation only removes the concept if the new form can prove what the old one could

**Lesson:** A translation that makes some construct disappear from the surface syntax is routinely reported as having eliminated the construct. Curry shows why that report is premature. Given a scheme that rewrites every expression built from constants and numbered argument slots into an application of a fixed operator to those constants, with no slots left anywhere, the operator is not unique: two visibly different operators can stand for the same expression. And the identity between them is not derivable from the rewriting rules — to establish it you have to put the argument slots back, run both sides, and compare. So the slots are gone from the formulas and still fully present in the reasoning, along with every notion that came with them. Nothing was eliminated; a less convenient notation was gained.

The test that separates a real elimination from a cosmetic one is therefore not "does the construct appear in the output" but "can I prove, inside the target system and without reaching back to the source, all the facts about the encoding that I need." Curry accepts this as the actual specification of the job and sets himself the corresponding task: arrange the primitive frame so that every one of those identities is derivable purely formally, with the eliminated notation never appearing in any proof. That reframing is what turns a notational trick into a foundation, and it is why the bulk of the work is a completeness and uniqueness result about which operators represent which expressions rather than a catalogue of clever encodings.

The same trap has a second lobe, and Curry names it too: an encoding can also smuggle back a concept through the side door of well-definedness. If every operator carries an argument domain, and domains are explained in terms of the very categories you claimed to have discarded, the claim fails again — the general laws of the system only hold when the arguments are of the right sort, and you have no way to say "the right sort."

A programmer who internalizes this stops accepting desugarings, encodings and compilation schemes on the strength of the target program's shape. They ask what has to be proved about the target, and whether the proof can be carried out in the target's own vocabulary. Under that test, an encoding whose correctness argument is always "decode it and see" has not removed the source language — it has hidden it in the metatheory, where it is unmaintained and unchecked. Conversely, an encoding with its own internal laws is genuinely a smaller system, and can be reasoned about by people who never learn what it was encoding.

**Source:** [Grundlagen der kombinatorischen Logik](../works/grundlagen-der-kombinatorischen-logik.md) — the assessment of Schönfinkel's programme in Chapter I A, both objections raised there against the claim to have eliminated variables and propositional functions, and the restatement of the problem as making every such identity formally derivable, which Chapter II then discharges through its three main theorems.
