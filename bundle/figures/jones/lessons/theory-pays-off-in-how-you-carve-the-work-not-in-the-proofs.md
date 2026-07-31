---
type: lesson
title: "Theory pays off mostly in how it makes you carve the work, not in the proofs you write"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Theory pays off mostly in how it makes you carve the work, not in the proofs you write

**Lesson:** Learn a body of theory about how designs are justified and you expect the return to arrive in the form of justifications: proofs written, obligations discharged, artifacts you could show someone. On real work the larger return arrives somewhere else and is easy to miss. It shows up as the decomposition — where you decided one stage ends and the next begins, which change you were willing to make in a single move, what you insisted on settling before opening the next question. Those choices are what make a development comprehensible, and someone who knows how the arguments would go makes them differently from someone who does not, even when neither writes a single argument down.

The mechanism is not mysterious. Knowing what it would take to justify a step tells you when a step is too big, because you can feel the argument becoming one you could not construct. It tells you which two changes must not share a stage, because their justifications would tangle. It tells you when a stage is doing nothing, because its argument would be trivial. So the theory operates as a sizing instrument applied continuously, and the sizing survives whether or not the proof is ever written out. That is why a development carried out with rigour but without formality can be far more trustworthy than an informal one, and why it can be strictly cheaper: the expensive part was never the proofs.

Two practical consequences. First, do not judge whether the theory was worth learning by counting the proofs you produced; judge it by whether your stages got smaller, more separable, and more obviously right. Second, keep the finer decomposition in reserve rather than in the document. A stage that combines two kinds of change is acceptable when you can say exactly how it would be split and argued if a reader found it unclear; it is not acceptable when the combination happened because you never asked. The difference between those two cases is invisible in the artifact and total in what it is worth.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 21's summary of the telegram analysis development, which states that the steps have not been formal but a rigorous structure has been preserved and the missing details such as the retrieve functions could be filled in to make a formal proof, that the increased confidence has been achieved more by the choice of stages than by writing out details of the formal proof, and that what guided the choice of stages was the formal material presented earlier in the book; together with the chapter's first development step, which combines a data refinement with a decomposition into an iterative statement while explicitly preserving the option of showing a more formal development should the step be considered unclear.
