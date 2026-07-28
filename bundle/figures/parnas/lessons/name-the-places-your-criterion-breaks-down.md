---
type: lesson
title: "Write down where your dividing criterion goes fuzzy, and name the arbiter that settles it"
figure: parnas
works: [the-modular-structure-of-complex-systems]
axes: [verifiability, hardware-affinity]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Write down where your dividing criterion goes fuzzy, and name the arbiter that settles it

**Lesson:** Any criterion sharp enough to divide a system will have regions where
it genuinely fails to decide. Is a facility a property of the hardware or a choice
the programmers made? It depends on whether the next generation of hardware might
implement it — a question about the future, not about the current machine. Is an
algorithm a requirement or an implementation decision? That depends entirely on
whether whoever wrote down what was wanted chose to specify it. These are not
oversights in the criterion; they are places where the answer legitimately comes
from outside it. The tempting responses are both bad: pretend the boundary is crisp
and let each designer resolve it privately, or conclude the criterion is too vague
to use.

The third response is to enumerate the fuzzy regions explicitly, in the same
document that states the criterion, and to designate what resolves each one. Parnas's
team points at a precise statement of requirements as the arbiter — it is the thing
that fixes where behaviour ends and design begins, so appeals go there rather than
to argument. Where even that leaves a choice, the boundary encodes a prediction, and
the prediction gets written down as a prediction: their split between what the
computer hides and what individual devices hide rests on an explicit expectation
about how replacement will actually happen — one device at a time, or the processor
alone, rather than everything at once. Stating that lets a future reader check
whether the bet still holds, instead of reverse-engineering it from the structure and
guessing.

The same honesty extends to the cases where the ideal is simply unreachable.
Sometimes a fact cannot be confined to one place — diagnostic detail about hardware
has to reach whatever shows it to a human, so anything consuming it inherits
liability for hardware change. Rather than either abandoning confinement or
pretending it held, such interfaces are marked as restricted, so the leak is visible
and its blast radius is known. Occasionally the reverse: a component's existence is
itself something that ought to be concealed, yet it gets mentioned anyway so that
nobody is left wondering where a function lives. In both cases the principle is
knowingly bent and the bend is recorded. A programmer who works this way produces
designs whose weak points are the documented parts, which is the opposite of the
usual outcome, where the documentation covers the parts that were easy to describe
and is silent exactly where a maintainer will need help.

**Source:** [The Modular Structure of Complex Systems](../works/the-modular-structure-of-complex-systems.md)
— the notes following the top-level A-7E decomposition, which list the sources of
fuzziness and then resolve them by appeal to the requirements document, together with
the earlier treatment of restricted and hidden components.
