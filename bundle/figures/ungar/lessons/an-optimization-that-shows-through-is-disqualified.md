---
type: lesson
title: "Judge an optimization by whether it shows through, not by how much it saves"
figure: ungar
works: [programming-as-an-experience]
axes: [hardware-affinity, cognitive-load, verifiability]
subdomains: [programming-environments-and-object-systems, operating-systems-and-systems-programming]
tags: [lesson]
---
# Judge an optimization by whether it shows through, not by how much it saves

Most implementation work treats the model a language presents as a specification to be met approximately: the compiler is free to do anything, and where the shortcut is visible — a call frame that vanished, a primitive that can no longer be overridden, a pause while something recompiles — that visibility is filed as an acceptable cost of speed. There is a stricter stance available, and taking it changes which optimizations are even candidates. If the implementation's actual job is to make the presented model *indistinguishable from reality*, then any optimization whose effects leak into what a programmer can observe is not a trade-off to be weighed. It is disqualified, however fast it is, because it breaks the one property the whole system was built to have.

The consequences are concrete and initially painful. Eliminating a self-call at the end of a routine is free performance and standard practice, but it destroys the record of how control got where it is, so it goes. Special-casing conditional dispatch in the runtime is an obvious win, but it means a programmer who edits the definition of conditional behavior sees no change, which is worse than slow — it tells them the thing they are editing is not the thing that runs, and once they know that, they no longer trust any of it. The stance also rules out a tempting escape: exposing knobs so users can choose optimization levels. Offering the choice is itself a leak, since it forces the programmer to think about the gap between what they wrote and what executes.

What makes the stance viable rather than merely principled is that it redirects effort instead of abandoning performance. Barred from optimizations that show through, you are pushed toward ones that cannot: compiling lazily and then recompiling hot code using type information gathered from actual execution, so that speed comes from observed behavior rather than from discarded information, and keeping enough data to reconstruct the unoptimized view on demand. That path costs memory and implementation complexity, and the honest accounting includes those. It does not cost the model's integrity.

The same discipline governs how you measure. A system's individual pauses are the wrong unit, because a person does not experience events, they experience intervals of unresponsiveness; several short delays with no useful gap between them are one long delay. Measure at the granularity of perception and the numbers get worse and become true, and the optimization priorities they imply are the ones that actually matter. A programmer who works this way asks of every performance change not "what did it save" but "what can someone now see that they could not see before" — and treats a yes as a reason to look for a different technique.

**Source:** [Programming as an Experience: The Inspiration for Self](../works/programming-as-an-experience.md) — the implementation section, which frames the implementer's goal as sustaining belief in the language's objects, lists specific standard optimizations declined on those grounds, and describes clustering pause measurements to match what a user perceives rather than what the mechanism does.
