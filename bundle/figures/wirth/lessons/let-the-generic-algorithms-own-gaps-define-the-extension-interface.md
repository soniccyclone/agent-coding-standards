---
type: lesson
title: "Let the generic algorithm's own gaps define the extension interface"
figure: wirth
works: [project-oberon]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Let the generic algorithm's own gaps define the extension interface

**Lesson:** Interfaces for extensible components are usually designed before the component that uses them, by asking what an implementer plausibly ought to supply. That order produces interfaces that are simultaneously too large and too small: they carry members nothing ever calls, and they are missing the one thing the machinery actually turns out to need. Reverse the order. Write the general algorithm first, as if the varying parts were not varying, and run your finger down it until you hit a statement the general code cannot execute because the knowledge required is private to whatever it is operating on. That statement is the extension point, and there is nothing to argue about — it is not a judgement about what implementers ought to provide, it is a place where the code demonstrably stops.

The discipline pays twice. It bounds the interface from above, because a generic algorithm that stalls in exactly one place needs exactly one dispatch, and any additional member you were considering has no caller. And it locates the boundary correctly, because the algorithm keeps everything it does know: the order of the steps, which things get visited, when identity is assigned, when output is emitted. What crosses the boundary is only the single step whose content varies. This is a much better split than the common one where the framework hands control wholesale to the implementation and hopes it comes back — there, the sequencing knowledge has escaped, and every implementer has to re-derive it and can get it wrong.

Notice what the gap tells you about the shape of the fix, too. The general code stalls because it lacks knowledge of *internal structure*, which is a property of the individual thing, not of the collection or the operation. That is why the answer is a dispatch on the instance rather than a parameter to the operation or a registry consulted by the framework: a parameter would have to be supplied by a caller who is equally ignorant, and a registry would have to be keyed by something, and the only key available is the thing itself. Reading off *what* the general code was missing therefore also settles *where* the missing piece has to come from, and that is a question people otherwise resolve by taste.

The habit generalizes past dispatch. Any time you are about to specify a contract for parties you have not met, write the consumer of that contract first and let the contract be the transcript of everything the consumer could not do alone. A contract derived this way is minimal by construction and has at least one demonstrated user, which is more than most designed-in-advance interfaces can claim.

**Source:** [Project Oberon](../works/project-oberon.md) — appendix A.1's marked statements in the generic externalization and internalization algorithms, where the step that stores or loads a main node with pointers replaced by indexes is noted as impossible to execute by a universal library method because the internal structure of an object is unknown to the library, so an instance method call is needed instead; together with the surrounding framing in which objects are abstract and have no concrete functionality on the level of definition, but any participating object is expected to implement a predefined message protocol, likened to components plugging into a hardware bus.
