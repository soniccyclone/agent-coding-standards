---
type: lesson
title: "Sometimes leave bad programs expressible and carry the obligation instead"
figure: post
works: [finite-combinatory-processes-formulation-1]
axes: [expressiveness, verifiability, primitive-count]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Sometimes leave bad programs expressible and carry the obligation instead

Post's primitive acts have preconditions: marking assumes the current box is empty, erasing assumes it is not. A direction set that could violate either is simply not admissible for the problem class, and whether it can is a separate property to be established rather than something the notation guarantees. He remarks in a footnote that he could easily have arranged the direction forms so that this could never go wrong, and chose not to. The design deliberately permits writing something ill-behaved, and moves the burden of ruling it out onto a proof about the particular direction set.

The reasoning behind that choice is the ordinary tension between making a notation total and keeping it faithful. Making every syntactically writable thing meaningful requires either widening the primitives — an unconditional mark that silently tolerates an already-marked box, say — or complicating the control forms until the bad cases are unrepresentable. Both purchase safety with distortion. The unconditional version blurs two acts a real worker would distinguish; the complicated version makes the base larger and less obviously a faithful account of what the executor does. Post's core exists to support a claim about the outer limit of mechanical procedure, and blunting the primitives to make the notation total would have cost the very precision the claim needs. So the primitives stay sharp, well-behavedness becomes a theorem about programs rather than a property of the language, and the notion of a process that actually halts on every instance is defined separately again, on top of that.

What follows for practice is that "make it impossible to express" and "make it provable that we never express it" are both legitimate answers, and the second is right more often than the current fashion admits. The relevant question is whether pushing the guarantee into the notation costs you accuracy about the thing underneath. If a stronger type or a totalizing default would force the model to lie — every operation quietly succeeding when the real device would fault, an API that cannot represent the distinction the hardware makes — take the partial operation, state the precondition, and prove your callers respect it. The instinct to make all errors unrepresentable is good; it stops being good at the point where the only remaining way to do it is to make the model less true.

Note also the layering Post uses: applicability first, then termination on every instance, then correctness of the answers. Three separate obligations, each named, none folded into the others. Keeping obligations distinct is what makes it possible to discharge them, and what makes it obvious which one a given program fails.

**Source:** [Finite Combinatory Processes — Formulation 1](../works/finite-combinatory-processes-formulation-1.md) — the definition of a direction set being applicable to a general problem, with the accompanying footnote declining to make applicability automatic, and the stacked definitions of a finite process and of a solution built on top of it.
