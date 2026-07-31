---
type: lesson
title: "An extension mechanism is a bet that the variant set is still open"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, expressiveness, verifiability]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# An extension mechanism is a bet that the variant set is still open

**Lesson:** When a central structure has to represent several kinds of thing that share a frame but differ in their attributes, the reflex is to give each kind its own refined type. The reflex is usually defended on the grounds that the kinds genuinely differ — but that is not what the mechanism is for. Variation is handled adequately by a discriminant field and a handful of general-purpose slots whose meaning depends on the discriminant. What a refinement mechanism buys, and the only thing it buys that the cruder arrangement does not, is the ability for someone to add a kind later without editing the definition. So the question that decides the design is not "do the kinds differ" but "is the set of kinds still open at the moment this is written."

Frequently it is not. A structure internal to one program, designed after the problem is fully understood, has a closed and enumerable set of variants, and the person choosing the representation can list them. In that situation the mechanism is paying for a property nobody will consume, and it is not free: it introduces one named type per variant into a design that could have had one, it commits the program to a feature of whatever language it is written in, and it makes the program harder to move to a setting where that feature is absent. That last cost lands hardest on exactly the kind of program most likely to be moved — a tool whose whole purpose is to be reproduced on new ground has to be written in the intersection of what its destinations offer, not the union.

The honest accounting requires naming what the crude version gives up, because it is real. A slot that means an address for one variant, an offset for another and a value for a third has left the type system and entered convention; nothing checks that a reader of the slot has first checked the discriminant. That is a genuine loss of verifiability, traded knowingly for a smaller vocabulary and a portable program, and the trade is defensible precisely when the variant set is closed — because a closed set can be tabulated, and a table showing which slot means what for each variant restores by documentation what the type system stopped enforcing. The failure mode to avoid is not choosing either arrangement; it is reaching for the mechanism reflexively, on the strength of an extensibility argument nobody checked was still true.

**Source:** [Project Oberon](../works/project-oberon.md) — the discussion in section 12.3 of the symbol table's Object type, which explains that different kinds of entry carry different attributes and that introducing an extended record type per kind would seem advisable, but was not done for three stated reasons: the compiler was first written in a subset of a language lacking type extension, avoiding it made translating the compiler into other languages for porting simpler, and all extensions were known when the compiler was planned so extensibility provided no argument for the variety of types; followed by the adoption of multi-purpose fields for variant-specific attributes, the same decision repeated for the Struct type's forms, and the tables later in the section listing what each field means for each mode and form.
