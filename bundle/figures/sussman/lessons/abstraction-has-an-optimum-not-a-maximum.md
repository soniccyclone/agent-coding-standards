---
type: lesson
title: "Abstraction has an optimum, not a maximum"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Abstraction has an optimum, not a maximum

**Lesson:** After several pages demonstrating how far a general method can be pushed -- a square-root routine recast as a fixed-point search, then as damping applied to a transformation, then as an instance of a still more general fixed-point-of-transform -- the authors stop and say plainly that this is not an argument for always writing programs in the most abstract way possible, and that expert programmers know how to choose the level of abstraction appropriate to the task.

That sentence does real work in a chapter whose entire momentum runs the other way, and it is worth extracting precisely because the surrounding demonstration is what makes people over-apply the technique. Having watched a specific procedure dissolve into a composition of general methods, the natural conclusion is that more dissolution is better. The correction is that abstraction is a positioned choice with a cost on both sides: too little and you restate instances forever, too much and the reader must reassemble the meaning from parts whose generality serves no case actually present.

The cost is easy to miss because each individual generalization looks free -- more powerful, subsuming what came before, elegant. The price appears only in aggregate, as the distance a reader must travel between the concrete problem and the code that solves it, and it is paid by people who did not attend the derivation.

The formulation that makes this usable is the authors' own: it is important to be able to *think* in terms of these abstractions so as to be ready to apply them in new contexts. Recognizing that your problem is an instance of a general method is always valuable, because it imports everything known about the method. Writing your program at that generality is a separate decision, made per case, on whether the additional cases the generality admits are ones you have or expect. Keeping recognition and expression apart is what distinguishes judgement from the reflex of always climbing one rung higher.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - chapter 1 section 1.3.4's closing, which having just recast the square-root computation as increasingly general fixed-point formulations urges alertness to opportunities to identify underlying abstractions and build on them, then immediately qualifies that this is not to say one should always write programs in the most abstract way possible -- expert programmers know how to choose the level of abstraction appropriate to their task -- while stressing the importance of being able to think in terms of such abstractions so as to apply them in new contexts.
