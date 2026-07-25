---
type: lesson
title: "The long-run goal you adopt decides what you are able to build, so aim at coupling a mind to a machine rather than at replacing the mind"
figure: brooks
works: [computer-scientist-as-toolsmith-ii]
axes: [cognitive-load, expressiveness]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# The long-run goal you adopt decides what you are able to build, so aim at coupling a mind to a machine rather than at replacing the mind

**Lesson:** A stated long-run objective is not decoration on top of the technical work; it points the work, and a goal can be both motivating and wrong. It can be wrong in a specific and expensive way: not merely harder than expected, but oriented such that decades of talented effort accumulate in a direction that was never going to arrive. The diagnostic is not that the goal failed to be reached. It is that the by-products turned out to be the durable contributions while the declared objective kept receding, and that the honest rhetoric of the field moderated in step with real accomplishment, drifting from claims about replacement toward claims about assistance. That drift is the evidence, and it is worth reading rather than glossing.

The alternative framing is that a mind working with a machine beats a machine built to imitate a mind, at any given level of available technology. Note the qualifier — this is not a claim about what is permanently impossible, it is a claim about where the achievable frontier lies at each moment, and therefore about where to aim. Adopting it moves the hard problems somewhere else entirely. If the objective is a coupled system, then the interesting engineering is the coupling: how much can be pushed into a head per second, which sensory channels are underused, and the fact that on the return path the natural expression of intent is rarely a string of characters. Under the replacement objective none of those questions are central; under the amplification objective they are the whole game, and they had received a small fraction of the attention.

There is also a scaling lesson underneath, and it generalises past its original setting. A body of rules that grows past a few thousand members becomes unmaintainable not because it runs slowly but because determining whether a new rule is consistent with the existing ones gets prohibitively hard, which puts a ceiling on the useful size of the whole thing. That is the shape of a great many limits in this field: the binding constraint is the cost of establishing that a change did not break something already there, and a design whose consistency-checking cost grows badly has a maximum size regardless of how much machinery is thrown at it. A builder who thinks this way asks of any accumulating structure what it will cost to add the ten-thousandth item, not the tenth.

**Source:** [The Computer Scientist as Toolsmith II](../works/computer-scientist-as-toolsmith-ii.md) — the section reassessing the field's original objectives as glamorous but misdirecting, the inequality it proposes in their place and the research programme that follows from taking the coupling seriously, and the account of why large rule bases stop scaling once consistency between new and existing rules becomes the dominant difficulty.
