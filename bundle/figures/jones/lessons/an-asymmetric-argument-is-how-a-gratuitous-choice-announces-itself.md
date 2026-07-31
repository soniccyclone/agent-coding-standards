---
type: lesson
title: "An argument that goes lopsided is telling you the code made a choice it did not have to make"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# An argument that goes lopsided is telling you the code made a choice it did not have to make

**Lesson:** Reasoning about a piece of code is usually treated as a one-way check: either the argument goes through or you have a bug. It is more useful than that. The *shape* of the argument carries information about the code that nothing else surfaces, and the most legible signal is asymmetry. When a description of what is wanted treats two things interchangeably, but the argument that the code meets it has to split them apart or lean on a condition stronger than the description ever asked for, the extra strength did not come from the problem. It came from a decision the code made that the problem left open.

The clean example is a piece of code that must return one of two equally acceptable answers. The description says either will do. The code, being code, has to pick, and picks the first. Nothing is wrong — the code is correct. But now the argument for it needs a strictly-greater-than where the description only had a greater-or-equal, and that mismatch is the arbitrary tie-break making itself visible. The reasoning is not being difficult; it is reporting a commitment that exists in the artifact and not in the requirement.

Why care about a commitment that costs nothing here? Because the arbitrary choices are exactly the ones that are unsafe to rely on and unsafe to change without knowing who relies on them. A caller that happens to depend on getting the first argument back has a dependency nobody wrote down and nobody agreed to; the day someone reorders the branch for unrelated reasons, that caller breaks and the change looks innocent. Every gratuitous commitment is a latent coupling, and coupling you did not intend is the kind you cannot maintain. The reasoning is the only place it shows up before a failure does.

The general practice is to read your justifications diagnostically rather than pass/fail. If the argument needed an assumption the specification never stated, ask where the extra strength came from. If a case split appeared in the argument with no corresponding distinction in the requirement, ask what the code decided that it was never asked to decide. Sometimes the answer is that the commitment is fine and you record it, so it is at least deliberate. Sometimes the answer is that a construct exists which lets you not commit at all — the machinery for expressing "any of these, I do not care" rather than being forced into an ordered if-then-else — and reaching for it removes the phantom coupling instead of documenting it. Either way the diagnosis came free, from work you were doing anyway.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 3's "Conditional Functions" section, in the parenthetical remark following the proof of the maximum function: that the temporary assumption used in the second case was unnecessarily strong, that this resulted from the explicit definition being over-constrained since either argument would be an acceptable result when the two are equal, that the choice of the first was embodied arbitrarily in the conditional expression, and that the effect of that asymmetry reappeared in the proof — together with the pointer to guarded-command work as the direction in which the arbitrariness can be avoided rather than merely noted.
