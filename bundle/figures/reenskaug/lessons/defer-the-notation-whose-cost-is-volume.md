---
type: lesson
title: "Introduce the expensive notation last, and prefer redesigning the thing so you never need it"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Introduce the expensive notation last, and prefer redesigning the thing so you never need it

**Lesson:** Notations differ enormously in what they cost per unit of insight, and the expensive ones are expensive in a specific way: they multiply the *volume* of description. Spelling out every legal state of a component and every transition between them is the clear example — it is precise, occasionally indispensable, and it inflates the description dramatically, which then makes everything downstream harder. More text to write, more to check for consistency, more to update whenever anything moves. The cost is not the effort of the first draft; it is the permanent drag on every later change.

So treat such notations as a last resort with two escapes tried first. The first escape is timing: if you do need them, apply them late, once the structure has stopped moving, so you pay the volume cost once instead of repeatedly. The second and better escape is to make the need go away — if the design can be simplified enough that the detailed behaviour is obvious and can safely be left to implementation, then the right move is to simplify rather than to document. Choosing not to write the expensive description is a legitimate outcome, and often the superior one, which is worth stating explicitly because the professional instinct runs the other way: more rigour looks more responsible.

There is a limit that keeps this from becoming an excuse, and it is worth knowing where it falls. A per-component behavioural description cannot establish that the assembly behaves correctly, because the property you care about lives in how the components interact — you have to widen your scope to the whole collaboration to argue about that, and when parts are composed you must consider all the composed behaviours together. So the expensive notation does not even buy the guarantee people reach for it hoping to get. It answers a narrower question than it appears to, which is one more reason to reach for it late, sparingly, and only when a simpler structure genuinely could not be found.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 6's state diagram section, which advises using state diagrams sparingly and only late in the design process because description volume increases dramatically, notes they may be omitted when the design is simple enough to postpone the problem to implementation, and states that dynamic correctness cannot be determined from a single state diagram.
