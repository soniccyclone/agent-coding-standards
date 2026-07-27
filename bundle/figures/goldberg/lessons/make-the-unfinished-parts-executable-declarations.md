---
type: lesson
title: "Keep the promise and the mechanism in separate documents, and turn every deliberate hole into something the system can state at runtime"
figure: goldberg
works: [smalltalk-80-the-language-and-its-implementation]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Keep the promise and the mechanism in separate documents, and turn every deliberate hole into something the system can state at runtime

**Lesson:** This book presents each part of the system twice, on purpose, in two documents with different jobs. One states, for each request an object answers, what happens and what comes back, under a stated rule that the wording describe the effect and never the technique. The other gives the private state and the bodies. The separation is not editorial tidiness; it is a claim about what a client is entitled to depend on. If a promise is written in terms of how it is currently kept, then every reader has silently acquired a dependency on the mechanism, and the mechanism can no longer change. Writing the two apart forces the author to discover whether a coherent promise even exists — a promise that cannot be stated without describing the code is not yet an abstraction.

The second half of the idea is the more unusual one: incompleteness gets declared rather than implied. A superclass in this system is often deliberately partial — it lays out the shape of an activity and leaves specific steps for its specializations, so the general sequence lives in exactly one place and the varying parts are supplied below. The hole is not left as a comment or a convention. It is filled with an explicit response that says, when reached, that a specialization owed this and did not supply it. There is a matching declaration for the opposite case: a request inherited from above that this kind of thing must not honor announces itself as such rather than silently misbehaving. In the framework built later in the book, the abstract distribution class does exactly this — the general sampling procedure is written once in terms of a step that every concrete distribution must define, and that step's placeholder is a runnable statement of the obligation.

Why this beats documentation is straightforward. A stated obligation that only exists in prose is checked by human diligence at a moment when the human is busy. An obligation encoded as behavior is checked by the system at the moment it matters, reports itself in the vocabulary of the failure, and cannot drift away from the code it constrains. It also converts a nasty class of bug — inheriting a plausible-looking default that happens to be wrong for this case — into an unambiguous, locatable complaint.

A programmer who works this way writes the abstract half of a design as a real artifact with real declared gaps, rather than as an empty base with optimistic comments. The practical test: for every place where a subordinate part is *supposed* to take over, ask what the system does if it does not. If the answer is "something silently reasonable," the design has hidden a hole instead of declaring one.

**Source:** [Smalltalk-80: The Language and Its Implementation](../works/smalltalk-80-the-language-and-its-implementation.md) — the chapters that establish protocol descriptions and implementation descriptions as two separate presentations with a stated rule about what a comment may say, the treatment of abstract superclasses and their framework messages that mark responsibilities and prohibitions as executable responses, and the probability-distribution framework in Part Three where the shared sampling procedure is defined against a subclass-supplied step.
