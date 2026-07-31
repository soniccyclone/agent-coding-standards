---
type: lesson
title: "Let the progress counter be the precondition check, and know what it cannot tell you"
figure: wirth
works: [algorithms-and-data-structures]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Let the progress counter be the precondition check, and know what it cannot tell you

**Lesson:** Many algorithms are correct only on inputs with a structural property their caller is trusted to supply. The obvious way to stop trusting is a separate validation pass that goes looking for violations before the real work starts, and it is often the wrong way, because the validation duplicates the traversal the algorithm was going to do anyway and needs its own correctness argument. The cheaper route is to notice that an algorithm which consumes its input in steps usually already fails to make progress on a bad input — it stalls with work remaining and nothing eligible to do — and that stalling is observable for the price of one counter. Count what entered, decrement on each unit produced, and check for zero at the end. A nonzero residue is a proof that the property did not hold, obtained as a by-product of running rather than as a separate phase.

What makes this work is that the counter is measuring the same thing the termination argument depends on, so the check and the progress proof are the same fact viewed from two sides. That is the property to look for when deciding whether a conservation check is available: is there a quantity that the algorithm strictly decreases on every step, whose reaching zero is equivalent to complete success? If so, testing it costs nothing and cannot be fooled by any input, because it does not depend on recognizing the shape of the violation — it depends only on the algorithm having run out of moves. Checks of this kind are unusually robust, since they detect every failure mode that manifests as stalling, including ones nobody anticipated when writing a targeted validator.

The cost is precision, and it should be stated rather than discovered by a user. A residue says that something remained, not what it was or why, and the diagnosis a person needs — the specific cycle, the particular pair of items that cannot both be satisfied — is not recoverable from a count. So the honest position is that the conservation check is the right *detector* and a poor *explainer*, and if explanation matters the reconstruction of a witness is a separate piece of work built on top, not a reason to abandon the cheap detector. Design accordingly: use the invariant to decide whether to fail, and a deliberately separate, only-on-failure pass to say why.

**Source:** [Algorithms and Data Structures](../works/algorithms-and-data-structures.md) — section 4.3.3's topological sort, where a counter is incremented once per distinct element created during the input phase and decremented once per element emitted during the output phase, and the note that its failure to return to zero indicates elements remain when none is without a predecessor, which is the evidence that the input set was not partially ordered; together with the chapter's own exercise observing that the resulting diagnostic message is not very helpful and asking for the program to be extended to output a sequence of elements forming a loop.
