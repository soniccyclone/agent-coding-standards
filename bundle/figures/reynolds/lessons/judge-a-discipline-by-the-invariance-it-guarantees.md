---
type: lesson
title: "Judge a discipline by an invariance it guarantees, not by the mistakes it happens to catch"
figure: reynolds
works: [towards-a-theory-of-type-structure]
axes: [verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Judge a discipline by an invariance it guarantees, not by the mistakes it happens to catch

**Lesson:** Arguments about whether a discipline is any good tend to degenerate into inventories: here are the errors it rejects, here are the ones it lets through, here is the annoyance it costs. That framing produces endless controversy because the inventories are incommensurable. The alternative is to commit to a single invariance property and treat the discipline as correct exactly insofar as it delivers it. The property proposed here is that the meaning of a valid program must not depend on the representations chosen for its types — imagine the identical program running on two machines whose notion of a given type ranges over entirely different sets, with corresponding inputs and correspondingly implemented operations, and demand that the outputs correspond too. Stated that way, the quality of the discipline becomes a theorem about the language rather than a matter of taste, and disagreements move to the definition of correspondence, which is at least the kind of question that can be settled.

The discipline of picking one invariance also disciplines the designer, because it must apply without exception. If representation independence is the criterion, it cannot hold only for the types the language happens to build in; it has to hold for types introduced by the programmer, which immediately dictates what introducing a type must mean. It splits a program into a region where the new type is used through operations it does not define, and a region where both the representation and those operations are supplied — and the invariance then says that swapping the second region for a consistent alternative leaves the whole program's meaning alone. The criterion, chosen up front for the built-in case, ends up determining the shape of a language feature nobody had yet designed. That is the sign of a well-chosen criterion: it generates requirements instead of merely grading them.

The general habit is to look for the change you want to be free to make, and then define the discipline as whatever makes that change unobservable. Any privileged case you carve out — one class of entity that gets the guarantee and another that does not — is a defect in the discipline rather than a pragmatic concession, because the whole value of an invariance is that you can rely on it without checking which case you are in.

**Source:** [Towards a Theory of Type Structure](../works/towards-a-theory-of-type-structure.md) — the introduction's statement that a type-correct program's meaning should never depend on the representations of its primitive types, developed through the two-machine comparison, together with the thesis that this independence must extend to user-defined types and the resulting inner/outer partition of a program around a type definition.
