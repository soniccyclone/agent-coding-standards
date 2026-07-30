---
type: lesson
title: "The machine's tolerance is exactly why you must declare your meaning above it"
figure: hoare
works: [hints-on-programming-language-design]
axes: [verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# The machine's tolerance is exactly why you must declare your meaning above it

**Lesson:** The hardware will accept nearly any sequence of operations over nearly any bit pattern and produce a well-defined result. That permissiveness is not a defect to be engineered away; it is where the power, the simplicity, and much of the reliability of the underlying machine come from, and a designer who tries to make the substrate opinionated usually makes it worse. The defect appears one level up. When a mistake at the level you are thinking in — treating one kind of thing as another, misplacing a field, mixing quantities that do not belong together — produces an answer that is fully explicable in terms of bit patterns and totally unrelated to the concepts you were reasoning with, the diagnosis has to be conducted in a vocabulary you were not using. That translation is the actual cost, and it is why an intermediate layer exists at all: it is the place where you say what you meant, so that meaninglessness can be rejected before it becomes a bit pattern.

This reframes declarations as something other than bureaucracy for the checker. Deciding the shape and range of the values a name will hold is one of the first instruments for sharpening an unclear problem, and the set of such decisions is what fixes the interfaces between parts of a large system; writing down each name's relationship to the others is a large part of the annotation, and saying informally what a name is for is a large part of the documentation. The check is a by-product of having stated your intent — worth pushing further than the usual boundary, since the same reasoning that catches adding a truth value to a count would catch adding a height to a weight, if only the notation let you say which is which.

Two moves quietly forfeit this and both are popular. The first is to infer intent from elaborate conversion rules, so mismatched things are silently made compatible: results come out nearly right instead of visibly wrong, which is worse than wrong; the conversion costs something nobody budgeted; the rules become a substantial thing to learn; and genuine extension by users becomes much harder because the automatic behavior is already occupying the space. The second is to let intent go unstated and supply defaults, which reproduces the machine's tolerance at the level where tolerance is fatal, and does it under rules complex enough that the outcome regularly surprises the person who wrote the code. The practitioner's tell is diagnostic: when experienced users of a system develop the habit of scanning its output to confirm that what it assumed on their behalf is acceptable, the defaults have converted a design decision into recurring manual labor.

**Source:** [Hints on Programming Language Design](../works/hints-on-programming-language-design.md) — the Types section, which grounds the case for compile-time type checking in the hardware's willingness to make sense of anything, argues declarations are primarily a design and documentation instrument, proposes checking units of measure, and lists the specific harms of automatic coercion and default declaration rules.
