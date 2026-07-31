---
type: lesson
title: "A requirement that lets later input revise earlier output costs you a whole pass"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, hardware-affinity, expressiveness]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# A requirement that lets later input revise earlier output costs you a whole pass

**Lesson:** The number of passes an algorithm needs is not a property of the algorithm, it is a property of the requirements it was given, and the dependence is a cliff rather than a slope. There is a single question that decides which side of the cliff you are on: can an element encountered later change a decision already committed for an element encountered earlier? If it cannot, everything can be emitted as it is read, and one traversal suffices. If it can, nothing can be committed until the enclosing group is complete, so the group must be traversed once to determine the collective decision and again to act on it — plus, usually, an intermediate structure to hold what the first traversal learned. That intermediate structure and the second traversal both exist because of a clause in the requirements, not because of anything intrinsic to the task.

The practical consequence is that requirement-setting is algorithm-design done under a different name, and it happens earlier, in a conversation where nobody is thinking about passes. Two requirements that sound like minor conveniences can each independently push you over: one that makes a group's geometry depend on the extreme member of the group, and one that lets the system, rather than the input, decide where a group ends. Either one alone is enough, because either one alone means the disposition of the first element cannot be known until the last has been seen. So when a requirement is proposed, the useful question is not whether it is desirable but whether it introduces a backward dependency — and if it does, the price should be quoted at that moment, while declining is still cheap, rather than discovered by whoever implements the update logic.

The other half of the discipline is naming what the restriction costs, in the same breath. Constraining a design so that its algorithm stays single-pass does forbid things, and those things should be stated concretely rather than left as a vague sense that the design is austere — here it is variation along the axis that would have changed group geometry, while variation along axes that do not is still permitted. A restriction stated with its exact consequence can be revisited later by someone who finds the consequence unacceptable and is willing to pay the pass. A restriction stated as a matter of taste cannot be revisited at all, because nobody knows what buying it back would cost.

**Source:** [Project Oberon](../works/project-oberon.md) — section 5.3's discussion of the update procedure for text frames, which observes that the formatting rules govern the complexity of such procedures and that the simplest possible set was consciously chosen: fixed distance between lines within a frame, and no implicit line breaks; the accompanying claim that exactly this pair of rules is what permits a line to be displayed in a single pass, and that two passes become unavoidable once line distances must adjust to font sizes or lines must be broken implicitly; and the section's closing statement of the resulting limitation, that different styles of a base font are possible within a frame while different sizes are not.
