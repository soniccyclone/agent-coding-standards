---
type: lesson
title: "Anything precise enough to be worth writing will contain mistakes, so make it run rather than making it a specification"
figure: kay
works: [steps-toward-the-reinvention-of-programming]
axes: [verifiability, expressiveness]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Anything precise enough to be worth writing will contain mistakes, so make it run rather than making it a specification

**Lesson:** The habit of separating the description of what a system means from the thing that carries it out rests on an assumption worth challenging: that a description, being shorter and more abstract, is reliable in a way an implementation is not. It is not. Any statement precise enough to constrain an implementation is precise enough to be wrong, and its errors are the same kind of errors — a case not considered, a relationship stated backwards — differing only in that nothing exercises them. Large proofs get debugged like large programs, and so do specifications. Once you accept that the description will need debugging, the question is what tool debugs it, and the only general answer available is execution. So a description worth the effort of writing should simply be made to run, and at that point there is no reason for it to be a separate artifact from the program. It is the program.

This is a demand on the languages you build, not a licence to skip the description. What it rules out is the two-artifact arrangement, where the honest statement of intent lives in a notation that cannot be tested and the executed thing lives somewhere else, guaranteeing that the two diverge and that the divergence is discovered by users. What it demands instead is that the notation you would have written the specification in be strong enough to be executed directly — which is achievable, since the reason such notations traditionally do not run is usually a decision about their purpose rather than a property of what they express.

The same reasoning constrains derived descriptions. A model of a system is only trustworthy to the extent that it is mechanically obtained from the system, because a hand-maintained model is a second artifact under exactly the divergence pressure just described. Extraction is what makes it worth having, and an extracted model can then be fed back as a checking layer, in the way a type discipline is a checking layer over expressions. The version of typing that earns its cost, on this view, is one that states expectations about meaning and can be confronted with the running thing, rather than one that demands extra declaration work up front in exchange for catching a narrow class of slip.

**Source:** [STEPS Toward the Reinvention of Programming](../works/steps-toward-the-reinvention-of-programming.md) — the section relating the project to specification languages and models, which argues that every expression in any language requires debugging so any language worth writing meaning in should just be made to run and be the language, that models are convincing only if automatically extracted and can then serve as an integrity layer extending a type system, and the earlier statement that this kind of mathematics must be runnable because artifacts of interest need debugging as much as proving.
