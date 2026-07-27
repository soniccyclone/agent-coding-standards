---
type: lesson
title: "A specification needs separate words for what a program must not do and what an implementation must catch, used with mechanical consistency"
figure: steele
works: [common-lisp-the-language-2nd-edition]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A specification needs separate words for what a program must not do and what an implementation must catch, used with mechanical consistency

**Lesson:** Very early on, before describing any feature, this document defines two phrases and commits to using them as terms of art for the next thousand pages. One phrase means: no valid program does this, the consequences are entirely undefined, and no implementation is obliged to notice. The other means: this will be detected, a program may rely on the detection happening, and every implementation must provide it. The document then unpacks each phrase into its numbered consequences, states which incidental wordings ("must", "may not") collapse into which of the two, and promises that the stronger reading is only ever expressed with the one word reserved for it — so a reader can determine which regime applies by looking for a keyword rather than by inferring intent from tone.

The reason this matters more than it looks is that these two regimes have opposite economics and get confused constantly. Undefined behaviour is a licence granted to implementors: it lets them skip checks in hot paths, and it lets a good implementation add a helpful diagnostic without that diagnostic becoming a promise. Mandatory detection is a licence granted to programmers: it lets them write code whose correctness depends on the error surfacing. A specification that leaves the boundary implicit hands out both licences everywhere, and then either implementors pay for checks nobody wanted or programmers depend on checks that vanish under a different compiler. Distinguishing them is what lets the same document serve two audiences with contradictory interests without lying to either.

The specification also shows the boundary is not always binary, and handles that explicitly rather than by fudging the vocabulary. Some conditions are required to be detected only at the highest safety setting and are undefined otherwise, which is a third regime — conditional detection, selected by the programmer — and it is described as such rather than being smuggled in under one of the existing two words. Elsewhere, where implementations plainly disagreed and could not be forced to converge, the document says so and declines to promise, rather than writing a requirement it knew would go unhonoured. That restraint is the same discipline applied to itself: a specification that mandates what it cannot enforce has silently converted a requirement into a lie.

A programmer who has internalised this reads every interface contract looking for which of the regimes each clause is in, and writes their own contracts the same way: naming precisely which misuses are caught and which are simply forbidden, and never letting a defensive check that happens to exist today be mistaken for a guarantee. It is also the discipline that makes safety levels coherent instead of a vague speed knob — a check is either part of the contract, part of the contract only at a stated setting, or not part of the contract, and every check should be classifiable.

**Source:** [Common Lisp the Language, 2nd Edition](../works/common-lisp-the-language-2nd-edition.md) — the notational-conventions section of the introduction, where the two phrases for erroneous situations are defined and their consequences enumerated, read together with the later clarification making some detections contingent on the safety setting.
