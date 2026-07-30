---
type: lesson
title: "Judge an extension mechanism by the marginal cost of the Nth addition, not by what one addition costs"
figure: ingalls
works: [a-simple-technique-for-handling-multiple-polymorphism]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Judge an extension mechanism by the marginal cost of the Nth addition, not by what one addition costs

**Lesson:** Extensibility is easy to demonstrate and hard to sustain, and the two get confused because a demonstration only ever shows the first extension. The honest measure is how the cost of describing a new participant behaves as the system already contains many: if it stays flat, the mechanism works; if it climbs with what is already there, the mechanism has merely deferred a collapse. Early extensible languages died on exactly this. They could describe a new domain impressively, but every procedure that had to accommodate the new domain grew another arm of case analysis, so the description cost of each addition scaled with the size of the system it was joining. What rescued the idea was not more expressive procedures but relocating the case analysis into the language's own invocation mechanism, where it is performed once, by the runtime, at a cost near that of an ordinary call.

The structural test that follows is concrete and cheap to apply: when you add the next kind of thing, count how many existing, working definitions you must edit. Zero means the mechanism is carrying the extension for you. Anything above zero means the case matrix is still living in your code, and every future addition will pay that same tax plus interest. This is why locality of code matters more than its total volume — an implementation spread across many small definitions, each owned by the type it concerns, is strictly better than a compact centralized one that must be reopened for every new case, even though the centralized version looks tidier the day it is written.

There is a second cost, easy to miss outside a live system, that pushes the same direction harder. Editing working code to accommodate a new case does not just risk a bug in the new feature; it risks breaking the machinery you are using to do the editing. In a self-hosted environment the tooling and the program share one address space and one class library, so a mistake in the central dispatch code can remove your ability to fix the mistake. Under that regime, an extension mechanism that requires no edits to existing definitions is not merely elegant, it is the difference between a failed experiment and an unusable environment.

**Source:** [A Simple Technique for Handling Multiple Polymorphism](../works/a-simple-technique-for-handling-multiple-polymorphism.md) — the opening account of why earlier extensible languages failed to keep economy of description as systems grew, the observation that message sending absorbs type testing at near procedure-call cost, and the passage noting that an error while augmenting central type-test code can destroy environmental support altogether.
