---
type: lesson
title: "Name the gap between the type and the reality, and say who is holding it"
figure: wirth
works: [algorithms-and-data-structures]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Name the gap between the type and the reality, and say who is holding it

**Lesson:** A compound type admits every combination of its parts' values, and reality admits fewer. Composing a day, a month and a year produces dates that never existed; the type is a superset of the thing it models, and the surplus is not an edge case but a large fraction of the value space. This is not a defect to be designed away in every instance — a type whose value set exactly matched the meaningful cases would often be far more awkward to define and to compute with — but it is a debt, and the only way it stays paid is if someone is named as holding it. The unstated version, where the type is treated as if it were the domain, is how programs end up with values that pass every check and mean nothing.

So make the accounting explicit at the moment of definition. State the invariant that separates the meaningful values from the representable ones, and state where it is enforced: at construction, at each mutation, at the boundary where data enters, or nowhere, with the burden falling on every author of every operation. All four are legitimate answers and they have very different costs; what is illegitimate is not answering. The reason this specific discipline matters more than general carefulness is that nothing in the program will ever remind you — the surplus values are perfectly well-typed, so the mechanism that catches most mistakes is structurally blind to this one.

The same accounting applies on the other side, where the model omits things reality has. Every model deletes something, and deletion is what makes a problem tractable; a matching problem becomes solvable precisely by assuming the participants' preferences do not change once a match is made, which is a considerable distortion of how anything actually behaves. Calling that assumption an abstraction is accurate, and it is also how the distortion gets forgotten, because the word makes a deliberate falsehood sound like a technical operation. The useful habit is to write the deletions down next to the model as plainly as the surplus: here is what this representation admits that cannot happen, and here is what it assumes away that can. Both lists are short, both are quickly written at design time, and both are nearly impossible to reconstruct later from the code.

**Source:** [Algorithms and Data Structures](../works/algorithms-and-data-structures.md) — section 1.5's observation that the Cartesian product contains all combinations of the constituent types' elements while in practical applications not all of them may be meaningful, the date type admitting days that never occurred, the assessment that the definition does not mirror the actual situation entirely correctly but is close enough for practical purposes, and the explicit assignment of responsibility to the programmer for ensuring meaningless values never occur during execution; together with section 3.6's note that the stable-matching formulation assumes each participant's stated list of preferences is invariant and does not change after an assignment has been made, that this simplifies the problem, and that it also represents a grave distortion of reality — which the text names, parenthetically, as abstraction.
