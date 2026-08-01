---
type: lesson
title: "Make the identifier a path to its own implementation"
figure: wirth
works: [project-oberon]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Make the identifier a path to its own implementation

**Lesson:** A format that admits element kinds defined outside itself has to answer where the definition of an unfamiliar kind comes from. The usual answer is a registry: a table mapping kind identifiers to the code that handles them, filled in at start-up or by a build step, which every new kind must be added to. That table is a second thing to keep correct, it is edited by people who are not adding the kind, and it makes the set of kinds a property of the installation rather than of the artifact — the same file means different things on two machines depending on what got registered.

There is a cheaper arrangement, available whenever the code that handles a kind is itself something the system can name and fetch. Give the kind an identifier that decomposes into the coordinates of its implementation: a part that names the unit of code to bring in, and a part that names what to invoke inside it. Resolution is then not a lookup but a parse followed by a load. Nothing central knows the set of kinds; the artifact states its own dependencies, and encountering one is what causes the corresponding code to arrive. Adding a kind requires writing the code and nothing else, which is the difference between an extension mechanism that works for strangers and one that only works for people with commit access to the registry.

The requirement this quietly places on the rest of the system is worth stating, because it is what makes the trick available at all: there must be a way to obtain executable code by name at run time, and a convention by which a named entry point can be invoked without the caller knowing its type beyond an agreed signature. Systems that have loading and a uniform allocation convention get open-ended formats almost for free; systems that resolve everything before running cannot have this and must pay for the registry. So the decision about whether identifiers can be paths is made much earlier and much lower down than the format is. When you find yourself designing a registry, check first whether the naming scheme underneath you could have carried the information instead.

The complement, and it is not optional, is a way to keep reading when the named implementation cannot be found. A self-locating identifier turns a missing definition into a run-time failure at exactly the moment of use, so the artifact must also say how much of itself to skip when that happens. Locate-by-name and skip-by-length are two halves of the same design: one makes the format open, the other makes it survivable.

**Source:** [Project Oberon](../works/project-oberon.md) — section 13.8.3's account of class handling in graphics files, where an index/name pair preceding an element triggers loading of the module specifying the class and its methods, the name consists of a module part taken as the parameter of the call to the loader and a second part naming the allocation procedure that returns a fresh object, and each extension's data is headed by a byte count used to skip the element when the requested module is not present.
