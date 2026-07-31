---
type: lesson
title: "Check which direction your formalism can assert in before setting a goal it cannot state"
figure: stearns
works: [its-time-to-reconsider-time, on-the-computational-complexity-of-algorithms]
axes: [verifiability, expressiveness]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Check which direction your formalism can assert in before setting a goal it cannot state

**Lesson:** A framework built around bounded resources is a machinery for certifying achievement: exhibit a method that stays within a budget and the problem is placed inside the corresponding class. Difficulty then has no positive form at all — the only way to say a problem is intrinsically hard is to say it fails to be in some class, which is a claim about the nonexistence of every method of a given kind. Once you see this, the notorious lopsidedness of such fields stops being mysterious. Upper bounds accumulate steadily because each one is a single witness; lower bounds barely accumulate because each one is a universal negation. The classes deserve to be called easiness classes, and the naming matters: calling them complexity classes disguises the fact that the vocabulary can only speak fluently about what is easy.

The productive response was not to attack the negation head-on but to change what is being asserted. Instead of claiming no efficient method exists for a problem, claim that an efficient method for it would yield efficient methods for a large family of problems that many capable people have failed to crack. That converts an unprovable absolute statement into a comparative one anchored in collective failure, and it is genuinely useful — it explains why such labels became the working currency of the field. But the currency is evidence, not proof, and the distinction erodes silently because the vocabulary is the same in both cases. Guarding it takes deliberate effort: the strongest available evidence for a proposition is a different claim from the proposition, and a hierarchy of such evidence does not become a hierarchy of established facts by being widely quoted.

The transferable habit is to check, before adopting a goal, whether the language you are working in has any way to express it. If every statement your apparatus can prove is an existence claim and your objective is an impossibility claim, you have three honest options: reformulate the objective as a relative statement, build new apparatus capable of asserting in the other direction, or accept that you are gathering evidence and label your conclusions accordingly. What you must not do is pursue the unstatable goal in the existing language and let accumulated failure to refute stand in for a result.

**Source:** [It's Time to Reconsider Time](../works/its-time-to-reconsider-time.md) — the remark that the classes should be called easiness classes because inherent hardness can only be expressed as non-membership, and the hardness-concepts section where relative hardness via reduction to a family of resistant problems is introduced as the workaround and explicitly characterised as accepted evidence rather than demonstration. The asymmetry is visible at the origin in [On the Computational Complexity of Algorithms](../works/on-the-computational-complexity-of-algorithms.md), whose open questions have to introduce a separate collection just to express the idea of a bound being a problem's genuine cost rather than an achievable one — and then ask whether that collection is ever nonempty.
