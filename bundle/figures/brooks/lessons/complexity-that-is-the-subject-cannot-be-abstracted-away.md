---
type: lesson
title: "When the complexity is the subject, simplifying models lose the subject; expect no unifying law behind requirements written by many minds"
figure: brooks
works: [no-silver-bullet, computer-scientist-as-toolsmith-ii]
axes: [cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# When the complexity is the subject, simplifying models lose the subject; expect no unifying law behind requirements written by many minds

**Lesson:** The physical sciences advanced for centuries by a reliable trick: build a stripped-down model, derive consequences from it, check them against the world. The trick works because what the model discards is not what the phenomenon fundamentally is. Software resists the trick, because the intricate web of distinctions is the artifact rather than a surface feature of it. Above the level of individual statements, a program has almost no repeated parts, since any genuine repetition gets named and factored out on sight. So growth in size is growth in the number of *different* elements, interacting non-linearly, and a description that abstracts the differences away has abstracted away the program. This is a claim about irreducible construct count, not about tidiness.

There is a second, harsher asymmetry. A physicist digging into apparent messiness works in the confidence that some consistent underlying order exists to be found, and that confidence has repeatedly been rewarded. Whoever builds software gets no such guarantee. Much of what a system must accommodate is arbitrary in the strict sense: the interfaces, formats, exceptions, and rules it must match were each settled by some independent group of people for their own reasons, at different times, and they are mutually inconsistent for no deeper cause than that. No redesign of your own code removes that complexity, because it does not originate in your code. Arbitrary intricacy arriving from many independent sources is the native terrain of this discipline rather than a temporary embarrassment on the way to a clean theory.

Believing this changes what you do when a system feels unreasonably complicated. You stop waiting for the insight that will collapse it, and you start distinguishing the intricacy that reflects a genuinely tangled world from the intricacy you added yourself. The first has to be organized, layered, and confined; the second should be deleted. It also changes how you read proposals: anyone claiming that a new formalism dissolves the difficulty is implicitly claiming that the difficulty was never inherent, which is a strong empirical claim about the problem rather than a property of the formalism. And it explains why practitioners trained in mathematics or natural science are so often repelled by these problems, the former by the sheer mess and the latter by its unprincipled origin.

**Source:** [No Silver Bullet: Essence and Accidents of Software Engineering](../works/no-silver-bullet.md) — the treatment of inherent complexity and of the requirement to conform to externally fixed interfaces, including the contrast drawn with how the physical sciences make progress. [The Computer Scientist as Toolsmith II](../works/computer-scientist-as-toolsmith-ii.md) restates the point as a claim about the discipline's proper domain, arguing that problems whose constraints spring from many independent minds are exactly where this field's best effort belongs.
