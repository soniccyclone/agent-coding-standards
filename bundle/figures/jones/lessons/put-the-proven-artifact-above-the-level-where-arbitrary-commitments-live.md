---
type: lesson
title: "Put the proven artifact above the level where arbitrary commitments live, so one argument covers a family"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Put the proven artifact above the level where arbitrary commitments live, so one argument covers a family

**Lesson:** An idea for computing something and a program that computes it are different objects, and conflating them is expensive in a specific way. The program contains the idea plus a pile of decisions the idea never made: which of two independent updates goes first, which representation holds the intermediate values, whether a step is written as one statement or two. Swapping two independent assignments produces a different program and the same idea. Nobody disputes this in principle; the cost shows up in practice, because if the artifact you invested in justifying is the program, then that swap has invalidated your justification and you must redo work whose subject matter did not change.

So the question of what level to write down and argue about is an economic one, and the answer is: the most abstract level that still determines the answer. Above that level you have not said enough to be right or wrong. At that level, one argument covers every program that embodies the idea, and the remaining work for any particular program is only to show that its extra commitments are consistent with the ones the abstract version left open — which is much smaller work, and independent of the argument you already made. Below that level, you have tied a proof to decisions that were never part of the claim, and every one of those decisions is a way for the proof to become stale.

This changes how you use other people's work, too. A proven idea recorded at the right level is something you can *start from*: pick it up, add your ordering and representation choices, discharge the small consistency obligations, and you have a justified program without reconstructing the reasoning. The same idea recorded as a program in some language is much less reusable, because you cannot tell which of its features carried the argument and which were the author's language showing through — so in practice you re-derive it, or you copy it and hope.

The recognizable symptom that you have written at the wrong level is that a change you consider trivial forces you to revisit reasoning you consider settled. That is not a sign the reasoning was fragile. It is a sign the reasoning was attached to something below the level of the claim it was making.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 6's "Documenting Algorithms" section: the argument that programs include detail unnecessary for computing a result, illustrated by the independent assignment pairs in the multiplication program and the two orderings of the factorial body which are held to be the same algorithm; the resulting distinction between an algorithm and the class of programs that embody it, and the conclusion that a programming language is not a viable tool for algorithm documentation because it forces commitments irrelevant to the essence; the presentation of the multiplication algorithm as an outer loop with its component operations given only by pre- and post-conditions, described as documenting the essential decisions without fixing details that differ between programs, and as a starting point that obviates reconstructing the argument; and the criticism that textbook algorithms documented in a programming language must have their whole proof revised when a change as simple as inverting two assignments is made.
