---
type: lesson
title: "Never add state to the artifact for the sake of the argument about it"
figure: jones
works: [development-methods-for-computer-programs-including-a-notion-of-interference]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Never add state to the artifact for the sake of the argument about it

**Lesson:** A recurring temptation when reasoning about a program is to introduce something into the program that exists only to make the reasoning work: a variable holding an initial value the code no longer needs, a counter recording history nobody reads, a shadow copy of a structure kept purely so a statement about it can be phrased. It is always available and it always works. It should be read as a diagnosis rather than a technique. The need for it means the description you are reasoning in cannot express the fact you need, and the honest fix is to change the description, not to deform the thing being described.

The reason this matters more than tidiness is that the deformation propagates. If a reasoning style makes it awkward to talk about a value that has been overwritten, then programs that overwrite their inputs become hard to justify, and so people stop writing them — which quietly imposes a requirement for extra storage on algorithms that never needed it, and produces contorted explanations of algorithms that genuinely do consume their inputs. The reasoning apparatus has silently become a design constraint, and nobody involved would have accepted that constraint if it had been stated openly. Whenever you notice a class of perfectly good implementations that your verification approach cannot comfortably discuss, you have found a defect in the approach and a hidden tax on the design.

The same test catches poorly chosen abstractions. If proving one representation adequate against another requires reconstructing discarded information first, the specification was carrying detail no observer could ever see, and the reconstruction is just paying that debt at proof time. Fixing the abstraction removes the need entirely. The general rule: auxiliary machinery is a signal pointing at the wrong place, and the correct response is always to look where it points rather than to get better at building the machinery.

**Source:** [Development Methods for Computer Programs including a Notion of Interference](../works/development-methods-for-computer-programs-including-a-notion-of-interference.md) — the discussion of ghost variables in the alternatives section on data refinement, which reads their necessity as a symptom of a poorly chosen specification and asks whether the same avoidance is possible for parallelism; and the comparison of postcondition styles, which notes that published proofs rarely overwrite initial values because the prevailing method makes it awkward, that this distorts the description of algorithms which genuinely consume their inputs, and that saving initial values in the state solely for the proof should be resisted.
