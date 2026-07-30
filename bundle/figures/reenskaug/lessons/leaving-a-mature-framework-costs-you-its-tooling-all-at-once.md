---
type: lesson
title: "Leaving a mature framework costs you all of its tooling at once — so decide whether you are stepping outside it or widening it"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, databases-and-data-management]
tags: [lesson]
---
# Leaving a mature framework costs you all of its tooling at once — so decide whether you are stepping outside it or widening it

**Lesson:** What a mature conceptual framework actually delivers is best seen through a practitioner describing her working day inside one: draw the model on screen, press a button, and the finished application is generated correctly and automatically — working immediately, every time, with no hand coding and no obscure defects to hunt. Set against that, the prospect of a more general technology reads to her not as an advance but as a return to nights spent finding the last bug before installation and further nights keeping the system alive. The author records the reaction rather than correcting it, and treats the trauma of moving outside an established framework with mature tool support as a real cost rather than resistance to change.

The point worth keeping is what the cost consists of. The framework's value is not mainly its notation; it is the accumulated apparatus around the notation — the generator, the editors that permit only legal constructions, the runtime, the accumulated knowledge of what goes wrong. All of it is coupled to the restricted world the notation defines, so stepping outside that world forfeits the whole bundle simultaneously. This is why the comparison "the new technology is more expressive" is not the relevant comparison, and why an honest evaluation prices the tooling you lose rather than only the expressiveness you gain.

Sometimes real requirements do exceed the boundary, and then there are exactly two moves, worth naming because they are usually conflated. You can add special programs that live outside the framework — a hand-written interface reaching into the data without being part of the model — which is cheap and immediate and leaves you with a permanent piece of code that none of the framework's guarantees or tools cover, and which everyone will forget is unprotected. Or you can extend the conceptual framework itself so the needed capability falls inside its new boundary, which is expensive, requires understanding the framework deeply enough to widen it without breaking its generation story, and preserves the guarantees for everything including the new part.

Neither is wrong; drifting between them is. The failure mode is to take the first option repeatedly without deciding, so the framework quietly becomes the smaller half of the system, still credited with a coverage it no longer has. Making the choice explicit, per capability, keeps the accounting honest: this part is inside and protected, this part is outside and on its own.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 11 section 11.3's boxed account of the database manager who draws a conceptual schema and pushes a button to get a correct generated program that works immediately every time; the second lesson drawn, that it is traumatic for any informatician to move outside an established conceptual framework with mature tool support, that every framework has limits, and that there are basically two ways to exceed them — adding special programs outside the framework, or extending the framework so the desired functionality falls within its new boundaries.
