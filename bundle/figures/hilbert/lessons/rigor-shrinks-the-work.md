---
type: lesson
title: "Precision is not the tax you pay for correctness; it is what makes the work smaller"
figure: hilbert
works: [mathematische-probleme]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Precision is not the tax you pay for correctness; it is what makes the work smaller

**Lesson:** The common assumption is that demanding a rigorous argument makes everything heavier — more cases, more machinery, more ceremony — and that informal reasoning is the economical option. Hilbert calls this an error and offers his own field as the counterexample: the effort to make an argument airtight is precisely what drives you to find a simpler argument, because the complicated route resists being made airtight at all. He points at the calculus of variations, where the older informal treatments demanded punishing calculations of second-order effects, and shows in the same lecture how a properly organized formulation makes an entire layer of that labor unnecessary. The rigorous version was not the elaborate version. It was the short one.

The mechanism is worth naming, because it generalizes past mathematics. An imprecise formulation lets you carry unexamined assumptions along silently, and every silent assumption is a case you will eventually have to handle by hand, one at a time, forever. Forcing the argument to be checkable surfaces those assumptions, and once surfaced most of them turn out to be either derivable from something you already have or unnecessary. What remains is a smaller basis doing more work. That is why rigor and simplicity travel together rather than trading off: they are both consequences of having found the real structure, and complexity is usually the residue of not having found it yet.

Hilbert guards the flank too. He rejects the position that only arithmetic or analysis can be treated rigorously, warning that such purism amputates geometry and physics and cuts off the flow of problems from the world. The demand is not that everything be expressed in one privileged formalism, but that whatever concepts you do admit — including ones that arrived from messy experience — get put on an explicit and complete enough footing to reason from. A programmer who takes this seriously treats the moment of writing down precise invariants, types, or preconditions as a design activity rather than a documentation chore, and expects the code to get shorter afterward. If it did not get shorter, that is evidence the formulation is still wrong, not evidence that rigor costs too much.

**Source:** [Mathematische Probleme](../works/mathematische-probleme.md) — the introductory methodological section that denies any conflict between rigor and simplicity, its calculus-of-variations illustration, and the adjacent refusal to restrict rigorous treatment to arithmetic alone.
