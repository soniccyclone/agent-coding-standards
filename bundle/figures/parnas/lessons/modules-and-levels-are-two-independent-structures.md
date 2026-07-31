---
type: lesson
title: "Modules and levels are two independent structures over the same parts, and expecting them to coincide is what forces the splitting"
figure: parnas
works: [designing-software-for-ease-of-extension-and-contraction]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Modules and levels are two independent structures over the same parts, and expecting them to coincide is what forces the splitting

Two different questions get asked about a system's parts, and because a few influential early systems answered them with the same partition, the field fused them into one word. One question is what may depend on what: an ordering, imposed to make subsets runnable and correctness arguments closeable. The other is what changes together: a grouping of the programs that must be designed and revised as a unit, because they share a concealed decision. Parnas insists there is no correspondence between the two. A single change-unit will normally have its programs scattered across several positions in the ordering, and that is not a compromise, it is what the two structures being independent looks like when you draw them over the same set of programs.

The practical evidence is the repair work. When designers find themselves repeatedly having to slice a component in two so that a dependency can be admitted, the usual reading is that the ordering discipline is unrealistic. Parnas reports the opposite cause: the slicing is needed most often precisely because they had assumed a position in the ordering would be a change-unit. Drop that assumption and the pressure drops with it, because the two halves of the sliced thing were never two design units to begin with — they were one unit whose programs simply belong at different heights. Which also disposes of the objection that spreading a change-unit across the ordering weakens its integrity: any error inside it can violate its own guarantee regardless of where its programs sit, all of its programs present in a given configuration have to be considered when arguing that guarantee, and none of that gets harder because they occupy several positions. Its boundary stays exactly as firm as it was.

Parnas is blunt about the vocabulary that hides all this. Talking about levels of abstraction implies a more-abstract-than relation doing the ordering, and he could not find one; the relation he actually has is about dependency, and the phrase is an abuse of language that he admits committing himself. That matters beyond pedantry, because the phrase is what licenses the fusion: if the strata really were degrees of abstraction, it would be natural for each to be an abstraction-bearing unit, and the two structures would collapse. Keep the relations distinct and you get to design them separately — decide what conceals what, decide what may rest on what, and expect the two answers to cut across each other.

**Source:** [Designing Software for Ease of Extension and Contraction](../works/designing-software-for-ease-of-extension-and-contraction.md) — the section on the distinction between modules, subprograms and levels, its report that splitting and sandwiching are most often needed because a level was assumed to be a module, its response to the objection about module programs residing on different levels, and its remark that no more-abstract-than relation was found and the phrase "levels of abstraction" is therefore an abuse of language.
