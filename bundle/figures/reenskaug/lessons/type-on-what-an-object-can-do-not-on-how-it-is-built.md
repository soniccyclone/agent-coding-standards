---
type: lesson
title: "Constrain a variable by what its occupant must be able to do, never by how the occupant is built"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [expressiveness, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Constrain a variable by what its occupant must be able to do, never by how the occupant is built

**Lesson:** Having a type system is not in question — it eliminates a class of runtime failure and forces variables to be documented precisely. The question is what the constraint should be *about*. Tying a variable to a particular implementation says "whatever lives here is built this way," and that description carries the entire internal construction of the thing along with it. The encapsulation you were relying on is then gone at the point where it matters most: you have made the holder of the reference depend on the callee's internals rather than on its behaviour, and you lose the ability to have several differently-built things that are externally indistinguishable.

The cost shows up during change rather than during construction, which is why it is easy to miss. Real systems accumulate a better version of some subsystem alongside the old one, and the new version has to be introduced gradually as confidence grows, which means both must coexist for a long time. If references are constrained by construction, coexistence requires the two to share ancestry — an artificial relationship invented to satisfy the type checker rather than because the things are related. If references are constrained by required capability, they simply both qualify, and no relationship between them is needed at all.

The honest coda is that this is a wish rather than a solved problem. An attempt to encode per-collaborator capability constraints in a real language's type system collapsed on something mundane: the same object, referenced from two contexts that need different capabilities of it, cannot satisfy both constraints, so passing it as a parameter produces a type error no widening fixes. The lesson from *that* is separate and also useful — when you find yourself building elaborate machinery to make a language's type system express something it was not designed for, the machinery is the signal, and the honest options are to accept the language's model or use a different language, not to keep fighting.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 4's comparison of static and dynamic typing, which affirms the benefits of typing while doubting the wisdom of typing on the implementing class because it breaks encapsulation, gives the coexisting-old-and-new-hierarchy case as motivation, and reports in a boxed aside the failed Eiffel experiment where per-port interface classes broke on object references in message parameters.
