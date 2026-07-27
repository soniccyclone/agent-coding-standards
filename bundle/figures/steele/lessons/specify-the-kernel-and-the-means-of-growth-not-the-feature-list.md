---
type: lesson
title: "Specify an irreducible kernel plus the right to grow it; anything you can define away is not part of the language"
figure: steele
works: [the-revised-report-on-scheme]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Specify an irreducible kernel plus the right to grow it; anything you can define away is not part of the language

**Lesson:** When this work moves from describing an interpreter to defining a language, it faces the question every specification faces: where does the language stop and the convenience layer begin? The answer it adopts is that the definition has exactly two obligations. It must fix the handful of constructs from which nothing can be subtracted, and it must guarantee that a mechanism exists for users to add constructs of their own. The guarantee of extensibility is itself part of the irreducible core; no particular extension is. Everything the report goes on to describe as a standard convenience — sequencing, simultaneous binding, the loop forms, the multi-armed conditional, the mapping operators — is presented with its reduction to the core spelled out, which is the report's way of saying these are furniture, not architecture, and an implementation that lacks them is still the language.

The consequence that makes this more than bookkeeping is that a construct's definition and its implementation become independent artifacts. The report is explicit that reducing a form to the core is an account of what the form *means*, not a mandate for how it must be realized; the reference implementation had already promoted one of the reducible forms into a primitive for speed while leaving its compiler working from the reduction, and the report's position is that users need not know which. This is only safe because the reduction is normative and the implementation is not. Get that ordering backwards — let the fast path define the semantics — and you no longer have a specification, you have documentation of a program.

The report is also candid about where the boundary is soft, and the candour is instructive. Facilities it could not yet justify on principle are described and then explicitly placed outside the core, with the admission that the authors do not claim them to be right. That is a third move available to a specifier: rather than either blessing an unprincipled design or omitting a capability people need, you can ship it labelled as not-yet-load-bearing, so that later revision costs nothing.

A designer who thinks this way stops treating a system's public surface as one flat list of features. They separate what must exist for anything else to be expressible, from what merely happens to be provided, from what exists only because users asked and nobody has a theory yet. They write the derivations down, because a derivation is what lets a feature be removed, replaced, or reimplemented without renegotiating the whole contract — and they treat the extension mechanism as load-bearing infrastructure rather than an advanced-user escape hatch, because it is the thing that makes the small core survivable.

**Source:** [The Revised Report on Scheme: A Dialect of LISP](../works/the-revised-report-on-scheme.md) — the opening account of what constitutes the kernel and why the definition is deliberately fuzzy at the edges, the reductions given for the system-supplied syntactic extensions, and the note defending an implementation's right to realize a reducible form primitively.
