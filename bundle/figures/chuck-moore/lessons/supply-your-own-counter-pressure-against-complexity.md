---
type: lesson
title: "Complexity has no natural opponent, so the programmer has to be one on purpose"
figure: chuck-moore
works: [programming-a-problem-oriented-language, the-evolution-of-forth, colorforth-documentation]
axes: [cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Complexity has no natural opponent, so the programmer has to be one on purpose

**Lesson:** Capabilities do not add up; they multiply. Each new feature has to remain consistent with every feature already present, so the burden of keeping a system coherent rises far faster than the count of things it can do. The asymmetry that follows is the important part: every force acting on a program pushes toward more. The person asking wants one more case handled, the implementer can see that it would only take a handful of instructions, and no stakeholder anywhere is charged with saying no. Absent a deliberately held commitment to smallness, there is literally nothing on the other side of the scale, which is why systems drift toward incoherence without anyone choosing it.

Treating simplicity as a taste, or as something one prefers when convenient, therefore fails structurally. It has to be held as a rule invoked at the moment of decision, and it is most useful when it carries numbers. Saying a routine should fit in tens of instructions rather than hundreds, or that a whole working system should fit in a few thousand words of memory, converts a vague aesthetic into something that can actually block a proposal. Such figures are less about the machine than about the intrinsic difficulty of the task; when an implementation badly exceeds them, the excess is evidence that the problem has been misconceived rather than that the problem is large.

The programmer who internalizes this behaves oddly by prevailing standards. Elaboration is treated as expensive even when the increment looks trivial, because the cost lands on the interactions rather than on the increment. Stripping something back to essentials is recognized as much harder work than adding to it, so the stripping is done first and defended afterward. Existing systems are read as cautionary evidence: whenever software has grown to the point where nobody can hold its behavior in mind, the diagnosis is not that the problem was hard but that no one was ever pushing back.

**Source:** [Programming a Problem-Oriented-Language](../works/programming-a-problem-oriented-language.md) — the opening chapter's statement of its governing principle, including the observation that the pressures all run one direction and the deliberate use of instruction counts as a discipline. Also [The Evolution of Forth](../works/the-evolution-of-forth.md) — the philosophy-and-goals section, where the same principle is presented as the author's lifelong operating rule. Also [colorForth: Programming Language and Operating System](../works/colorforth-documentation.md) — the rationale section, which measures decades-old system software against that standard and finds it indefensible.
