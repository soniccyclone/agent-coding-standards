---
type: lesson
title: "Let the machine's cost model set the grain of your abstractions, and refuse any mechanism whose expense is invisible to whoever uses it"
figure: dahl
works: [class-and-subclass-declarations, simula-an-algol-based-simulation-language]
axes: [hardware-affinity, primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics, operating-systems-and-systems-programming]
tags: [lesson]
---
# Let the machine's cost model set the grain of your abstractions, and refuse any mechanism whose expense is invisible to whoever uses it

**Lesson:** A uniform design says every value is an independently existing entity with its own identity and lifetime. The uniform design was considered and deliberately not taken. An array gets independent existence because an array is usually large enough that treating it as its own allocatable thing is reasonable; a single scalar does not, because giving each one independent existence would fragment the store badly, and fragmentation costs twice, lengthening each reclamation pass and making passes more frequent. The grain of the object model was set by the behavior of the storage system rather than by the elegance of the model. This is the hardware-affinity axis applied to a language design decision rather than to a compiler one: the boundary at which a design abstraction stops being worth its allocation is a real boundary, discoverable only by knowing how allocation actually behaves.

The same reasoning appears as an explicit trade elsewhere. Adding entities that outlive their creators is flatly incompatible with running everything on a simple stack, and the response was to state restrictions on what such a declaration may take as parameters and where it may appear, so an efficient allocation strategy remained possible. A restriction the programmer can read is a better payment for a new abstraction than a cost the programmer cannot see. The strongest form of the argument is the rejection of general call-by-name for classes: it was declined not only for implementation difficulty but because it would invite programs in which nothing can ever be reclaimed, with the author having no way to notice. A mechanism whose expense is invisible at the point of use is a defect however clean it looks, because it removes the user's ability to make the trade at all.

There is a methodological point riding alongside. Asked whether reference counting would beat garbage collection, the answer given was that their own experiments suggested it might not, against the intuition in the room. The people who set the grain of this design by cost had measured the costs.

A programmer who works this way treats "what does one of these cost to create, keep, and reclaim" as a first-class design input, not an optimization concern to revisit later, because the answer determines whether a given thing should be an entity at all or a field inside one. Two working rules follow. Uniformity in the model is worth breaking where the cost curve breaks, and the break should be documented as a restriction rather than absorbed as a mystery. And any convenience whose price is paid in resources the caller cannot observe should be rejected outright, or made observable before it ships.

**Source:** [Class and Subclass Declarations](../works/class-and-subclass-declarations.md) — the recorded discussion following the paper, where Dahl answers Petrone on why arrays but not scalars are separate objects (store fragmentation), answers Strachey on measurements of reference counting against collection, and explains the rejection of a call-by-name mechanism for classes on grounds of invisible non-reclamation. Also [SIMULA - an ALGOL-Based Simulation Language](../works/simula-an-algol-based-simulation-language.md), whose parameters-and-nonlocals section states plainly that the new sequencing model breaks the simple stack and imposes named restrictions to keep storage allocation efficient.
