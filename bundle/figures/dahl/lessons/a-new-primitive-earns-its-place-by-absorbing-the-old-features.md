---
type: lesson
title: "Judge a proposed primitive by how many existing built-in features it can dissolve into ordinary definitions"
figure: dahl
works: [class-and-subclass-declarations, simula-67-common-base-language]
axes: [primitive-count, expressiveness]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# Judge a proposed primitive by how many existing built-in features it can dissolve into ordinary definitions

**Lesson:** Most arguments for a new construct are arguments from convenience: here is something awkward to write, and the construct makes it shorter. That test is nearly worthless, because it is satisfiable by any amount of special-purpose syntax and the result is a language that grows without becoming more powerful. A much sharper test is available. Take the features the language already provides as built-in special forms — the ones the compiler knows about and the user cannot have written — and try to define them using nothing but the proposed construct. What comes back as a plain definition was never a primitive. What resists tells you either that the proposal is too weak or that you have found a genuine irreducible.

Applying that test is uncomfortable and therefore informative. A first version of a language may hand the user built-in list membership, built-in process declarations, built-in scheduling statements, each with its own syntax and its own place in the manual. If a general notion of an instantiable, extendable, referenceable definition is powerful enough, all of that collapses: the list vocabulary becomes a couple of definitions the user could have written, the process notion becomes an ordinary extension of that vocabulary, and the sequencing operations become procedures over a small handful of genuinely primitive control transfers. The manual shrinks, the compiler shrinks, and — the part that matters most — everything the built-ins used to do exclusively becomes available for the user to do differently.

The test also fails informatively, which is its best property. Reconstructing an old feature from the new mechanism will expose the places where the reconstruction is not quite faithful, and each of those is a precise, small statement about what the new mechanism still lacks. That is far more useful design feedback than a general sense that something is missing, and it arrives while the language is still changeable. A designer who runs this test habitually ends up with fewer primitives, a compiler that privileges less, and a defensible answer to the question of why each remaining primitive is there.

**Source:** [Class and Subclass Declarations](../works/class-and-subclass-declarations.md) — the extended example that reconstructs the earlier language's process, main-program and simulation-block notions from class prefixing plus three control-transfer procedures, the circular-list example that recovers its set facilities as user-level definitions, and the candid remark that the reconstruction of activity declarations is not yet entirely satisfactory. Also [SIMULA 67 Common Base Language](../works/simula-67-common-base-language.md) — the system-classes chapter, where the list and simulation facilities of the predecessor language appear as ordinary class declarations layered on one another.
