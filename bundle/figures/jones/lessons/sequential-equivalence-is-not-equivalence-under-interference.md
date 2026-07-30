---
type: lesson
title: "Two fragments with the same effect in isolation are not interchangeable once anything else can watch"
figure: jones
works: [development-methods-for-computer-programs-including-a-notion-of-interference]
axes: [parallelizability, verifiability, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, programming-languages-and-semantics]
tags: [lesson]
---
# Two fragments with the same effect in isolation are not interchangeable once anything else can watch

**Lesson:** Describing a fragment of code by the relation it establishes between its starting and finishing state is complete only while nothing else is running. Take a value, add to it, store it back; or increment it in place. Identical relations, and identical in every sequential sense — yet put either next to a concurrent participant touching the same value and they behave differently, because they differ in how many separately observable moments they pass through. The consequence for practice is uncomfortable and worth stating plainly: refactorings justified by input-output equivalence are not sound in the presence of interference, and neither are the mental substitutions programmers make constantly while reading code.

What this forces into the open is that the grain of atomicity is part of a specification, not an implementation detail. You cannot say what a participant guarantees without saying over what unit that guarantee holds, because the guarantee is a claim about every transition an outside observer could catch. Equally, you cannot say what a participant assumes without accepting that the assumed disturbance can be inserted between any two of its own indivisible steps — including before its first step and after its last, since the moment of being scheduled is not privileged. A specification that names its atomic unit is checkable; one that does not is an invitation to a class of bug that testing finds by accident.

The usable model is to imagine an adversarial operation spliced into every gap in your code, constrained only by what you declared you could tolerate. Read your fragment with that operation present at every gap and the questions that matter surface immediately: which of these local variables still means what I think it means, which of these two reads of the same shared value are allowed to disagree, which conclusion did I draw from a snapshot that has since expired. This is the only reliable way to read concurrent code, and it is also an argument for keeping the number of gaps small — every additional indivisible step is another place the world gets to move.

**Source:** [Development Methods for Computer Programs including a Notion of Interference](../works/development-methods-for-computer-programs-including-a-notion-of-interference.md) — the opening of the specification-extensions section, where two parallel read-modify-write sequences yield a range of outcomes no pair of postconditions predicts and where two sequentially equivalent increment forms are shown to differ once a shared variable is involved; the accompanying note that developing to such a specification must allow for interference before the first and after the last step of the written code; and the guarantee-conditions subsection, which characterizes the rely-condition as the postcondition of an interfering operation slotted between any two atomic steps.
